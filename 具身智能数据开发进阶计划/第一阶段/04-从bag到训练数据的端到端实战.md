# 04：从 bag 到训练数据的端到端实战

> 本篇是第一阶段的收官实战：把仓库中的真实采集数据转换成模型可消费的 LeRobot 数据集。你仓库里有两类数据：`publish_demo_ros2.py` 生成的模拟 bag（含关节+动作+图像）和 `数据采集样本/` 中的 Orbbec 多相机 BAG（纯视觉）。本篇分别处理两种场景。

## 1. 先搞清楚你的输入数据是什么

### 场景 A：模拟数据（publish_demo_ros2.py 生成的 ROS 2 bag）

```text
来源：publish_demo_ros2.py → ros2 bag record
格式：ROS 2 bag URI（metadata.yaml + .db3/.mcap）
内容：14 个话题，含 JointState、Odometry、Twist、CompressedImage、CameraInfo
特点：关节+动作+图像齐全，适合练习完整转换链路
```

### 场景 B：真实采集数据（数据采集样本/）

```text
来源：5 台 Orbbec Gemini 相机，硬件同步采集
格式：Orbbec SDK native BAG（不是 ROS bag！）
内容：每台相机 color（1280×720 MJPG @30fps）+ depth（848×480 Y16 @30fps）
特点：纯视觉数据，无关节/动作；5 路硬件同步，时间偏差 < 2ms
```

> **关键区分**：`数据采集样本/` 中的 `.bag` 文件是 Orbbec SDK 原生格式，不是 ROS 1 bag。`rosbag info` 和 `rosbags-convert` 无法读取它们，必须使用 Orbbec SDK。你在 `具身智能数据格式转换全景.md` 中已经记录了这个边界。

### 本篇策略

```text
步骤 1：用模拟数据走通完整链路（关节+动作+图像 → LeRobot）
         ← 这是你日常开发的核心场景
步骤 2：用真实 Orbbec 数据做多相机转换（纯视觉 → LeRobot）
         ← 这是你遇到的特殊场景
步骤 3：讨论两者结合时的数据组织策略
```

## 2. 步骤一：ROS 2 bag → LeRobot 数据集（完整链路）

### 2.1 从 bag 中抽取并同步消息

这里复用你在前置计划第二、三周学到的能力。核心是：把不同话题的消息按时间对齐成统一帧序列。

```python
"""从 ROS 2 bag 中抽取关节状态、动作和图像，对齐成帧序列。"""
from __future__ import annotations

import json
from collections.abc import Iterator
from pathlib import Path
from dataclasses import dataclass

import cv2
import numpy as np
from rosbags.highlevel import AnyReader
from rosbags.typesys import Stores, get_typestore


@dataclass(frozen=True)
class FrameData:
    """一个对齐后的时间步的所有数据。"""
    timestamp_ns: int
    state: np.ndarray | None         # (state_dim,) float32
    action: np.ndarray | None        # (action_dim,) float32
    image_head: np.ndarray | None    # (H, W, 3) uint8 BGR
    image_wrist: np.ndarray | None


def stamp_to_ns(stamp: object) -> int:
    return int(stamp.sec) * 1_000_000_000 + int(stamp.nanosec)


def extract_and_align(
    bag_path: Path,
    fps: int = 30,
) -> list[FrameData]:
    """从 bag 中提取消息并按固定 FPS 对齐。

    策略：以 FPS 生成均匀时间轴，对每个时间点用最近邻匹配各话题。
    """
    typestore = get_typestore(Stores.ROS2_HUMBLE)

    with AnyReader([bag_path], default_typestore=typestore) as reader:
        # 第一步：收集各话题的原始消息
        raw: dict[str, list[tuple[int, object]]] = {
            "joint_states": [],
            "cmd_vel": [],
            "head_image": [],
            "wrist_image": [],
        }

        topic_map = {
            "/robot/joint_states": "joint_states",
            "/robot/cmd_vel": "cmd_vel",
            "/camera/head/image": "head_image",
            "/camera/wrist/image": "wrist_image",
        }

        for connection, log_time, rawdata in reader.messages():
            key = topic_map.get(connection.topic)
            if key is None:
                continue
            msg = reader.deserialize(rawdata, connection.msgtype)
            raw[key].append((int(log_time), msg))

        # 第二步：建立固定 FPS 时间轴
        start_ns = reader.start_time
        end_ns = reader.end_time
        step_ns = 1_000_000_000 // fps

        # 第三步：对每个时间点做最近邻匹配
        frames: list[FrameData] = []
        target_ns = start_ns

        while target_ns <= end_ns:
            joint = nearest_joint(raw["joint_states"], target_ns)
            cmd = nearest_cmd_vel(raw["cmd_vel"], target_ns)
            head_img = nearest_image(raw["head_image"], target_ns)
            wrist_img = nearest_image(raw["wrist_image"], target_ns)

            frames.append(FrameData(
                timestamp_ns=target_ns,
                state=joint,
                action=cmd,
                image_head=head_img,
                image_wrist=wrist_img,
            ))
            target_ns += step_ns

        return frames


def nearest_joint(
    messages: list[tuple[int, object]],
    target_ns: int,
    max_delta_ns: int = 100_000_000,
) -> np.ndarray | None:
    """找到最近的 JointState 消息，提取位置数组。"""
    if not messages:
        return None
    best = min(messages, key=lambda item: abs(item[0] - target_ns))
    if abs(best[0] - target_ns) > max_delta_ns:
        return None
    return np.array(best[1].position, dtype=np.float32)


def nearest_cmd_vel(
    messages: list[tuple[int, object]],
    target_ns: int,
    max_delta_ns: int = 100_000_000,
) -> np.ndarray | None:
    """找到最近的 Twist 消息，提取线速度和角速度。"""
    if not messages:
        return None
    best = min(messages, key=lambda item: abs(item[0] - target_ns))
    if abs(best[0] - target_ns) > max_delta_ns:
        return None
    twist = best[1]
    return np.array([
        twist.linear.x, twist.linear.y, twist.linear.z,
        twist.angular.x, twist.angular.y, twist.angular.z,
    ], dtype=np.float32)


def nearest_image(
    messages: list[tuple[int, object]],
    target_ns: int,
    max_delta_ns: int = 50_000_000,
) -> np.ndarray | None:
    """找到最近的 CompressedImage 并解码。"""
    if not messages:
        return None
    best = min(messages, key=lambda item: abs(item[0] - target_ns))
    if abs(best[0] - target_ns) > max_delta_ns:
        return None
    encoded = bytes(best[1].data)
    image = cv2.imdecode(
        np.frombuffer(encoded, dtype=np.uint8),
        cv2.IMREAD_COLOR,
    )
    return image
```

### 2.2 转成 LeRobot 格式

```python
"""把对齐后的帧序列写成 LeRobot v3 数据集。"""
import json
from pathlib import Path

import numpy as np
import pandas as pd


def frames_to_lerobot(
    frames: list[FrameData],
    output_dir: Path,
    dataset_name: str = "box_transfer_demo",
    fps: int = 30,
) -> None:
    dataset_path = output_dir / dataset_name
    (dataset_path / "data").mkdir(parents=True, exist_ok=True)
    (dataset_path / "meta").mkdir(parents=True, exist_ok=True)
    (dataset_path / "videos" / "chunk-000" / "observation.images.head").mkdir(parents=True, exist_ok=True)
    (dataset_path / "videos" / "chunk-000" / "observation.images.wrist").mkdir(parents=True, exist_ok=True)

    # 过滤掉没有关键数据的帧
    valid_frames = [
        f for f in frames
        if f.state is not None and f.action is not None
    ]

    # 写图像帧到临时目录（后续编码为 MP4）
    frames_dir = dataset_path / ".tmp_frames"
    head_dir = frames_dir / "head"
    wrist_dir = frames_dir / "wrist"
    head_dir.mkdir(parents=True, exist_ok=True)
    wrist_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, object]] = []
    for idx, frame in enumerate(valid_frames):
        row = {
            "index": idx,
            "episode_index": 0,  # 单 episode；多 episode 扩展此处
            "frame_index": idx,
            "timestamp": idx / fps,
            "observation.state": frame.state.tolist(),
            "action": frame.action.tolist(),
        }
        rows.append(row)

        # 写临时图像帧
        if frame.image_head is not None:
            cv2.imwrite(str(head_dir / f"frame_{idx:06d}.png"), frame.image_head)
        if frame.image_wrist is not None:
            cv2.imwrite(str(wrist_dir / f"frame_{idx:06d}.png"), frame.image_wrist)

    # 写 Parquet
    df = pd.DataFrame(rows)
    df.to_parquet(
        dataset_path / "data" / "train-00000-of-00001.parquet",
        index=False,
    )

    # 编码 MP4
    encode_episode_video(head_dir, dataset_path / "videos" / "chunk-000" / "observation.images.head" / "episode_000000.mp4", fps)
    encode_episode_video(wrist_dir, dataset_path / "videos" / "chunk-000" / "observation.images.wrist" / "episode_000000.mp4", fps)

    # 写元数据
    state_dim = len(valid_frames[0].state)
    action_dim = len(valid_frames[0].action)
    write_meta(dataset_path, fps, state_dim, action_dim, len(valid_frames))

    # 清理临时帧
    import shutil
    shutil.rmtree(frames_dir)

    print(f"数据集已创建: {dataset_path}")
    print(f"  帧数: {len(valid_frames)}")
    print(f"  FPS: {fps}")
    print(f"  state 维度: {state_dim}")
    print(f"  action 维度: {action_dim}")


def encode_episode_video(frames_dir: Path, output_path: Path, fps: int) -> None:
    import subprocess
    subprocess.run([
        "ffmpeg", "-y",
        "-framerate", str(fps),
        "-i", str(frames_dir / "frame_%06d.png"),
        "-c:v", "libx264",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-r", str(fps),
        str(output_path),
    ], check=True, capture_output=True)


def write_meta(
    dataset_path: Path,
    fps: int,
    state_dim: int,
    action_dim: int,
    total_frames: int,
) -> None:
    meta = dataset_path / "meta"

    info = {
        "codebase_version": "v3.0",
        "robot_type": "custom",
        "fps": fps,
        "total_episodes": 1,
        "total_frames": total_frames,
        "features": {
            "observation.images.head": {
                "dtype": "video",
                "shape": [720, 1280, 3],
                "names": {"height": "auto", "width": "auto", "channel": ["red", "green", "blue"]},
            },
            "observation.images.wrist": {
                "dtype": "video",
                "shape": [720, 1280, 3],
                "names": {"height": "auto", "width": "auto", "channel": ["red", "green", "blue"]},
            },
            "observation.state": {
                "dtype": "float32",
                "shape": [state_dim],
                "names": {"joints": [f"joint_{i}" for i in range(state_dim)]},
            },
            "action": {
                "dtype": "float32",
                "shape": [action_dim],
                "names": {"dofs": ["linear_x", "linear_y", "linear_z", "angular_x", "angular_y", "angular_z"][:action_dim]},
            },
            "episode_index": {"dtype": "int64", "shape": [1]},
            "frame_index": {"dtype": "int64", "shape": [1]},
            "timestamp": {"dtype": "float32", "shape": [1]},
            "index": {"dtype": "int64", "shape": [1]},
        },
    }
    (meta / "info.json").write_text(json.dumps(info, indent=2, ensure_ascii=False))

    episodes = [{"episode_index": 0, "tasks": ["box transfer demo"], "length": total_frames}]
    (meta / "episodes.jsonl").write_text(
        "\n".join(json.dumps(e, ensure_ascii=False) for e in episodes) + "\n",
    )

    tasks = [{"task_index": 0, "task": "box transfer demo"}]
    (meta / "tasks.jsonl").write_text(
        "\n".join(json.dumps(t, ensure_ascii=False) for t in tasks) + "\n",
    )

    # 计算 stats
    import pandas as pd
    df = pd.read_parquet(dataset_path / "data" / "train-00000-of-00001.parquet")
    stats: dict[str, dict[str, list[float]]] = {}
    for col in ["observation.state", "action"]:
        values = np.array(df[col].tolist())
        stats[col] = {
            "mean": values.mean(axis=0).tolist(),
            "std": values.std(axis=0).tolist(),
            "min": values.min(axis=0).tolist(),
            "max": values.max(axis=0).tolist(),
        }
    (meta / "stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False))
```

### 2.3 运行并验证

```python
from pathlib import Path

# 使用你已有的 ROS 2 bag
bag_path = Path("rosbag2_2026_08_07-09_15_21")
output_dir = Path(".")

# 步骤 1：提取并对齐
frames = extract_and_align(bag_path, fps=30)
print(f"提取 {len(frames)} 帧")

# 步骤 2：转成 LeRobot 格式
frames_to_lerobot(frames, output_dir, dataset_name="box_transfer_v1")
```

验证加载：

```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

dataset = LeRobotDataset("box_transfer_v1")

print(f"FPS: {dataset.fps}")
print(f"Episodes: {dataset.num_episodes}")
print(f"Samples: {dataset.num_samples}")

sample = dataset[0]
print(f"observation.state shape: {sample['observation.state'].shape}")
print(f"action shape: {sample['action'].shape}")
```

## 3. 步骤二：Orbbec 多相机 BAG → LeRobot（纯视觉场景）

你的 `数据采集样本/` 中的数据是 Orbbec SDK native BAG。读取它需要 Orbbec SDK：

```bash
pip install pyorbbecsdk
```

> 如果 `pyorbbecsdk` 在你的平台不可用，可以在装有 Orbbec 驱动的 Linux 机器上操作，或先用 `publish_demo_ros2.py` 的数据走通完整流程。

### 3.1 从 manifest 读取采集元数据

你的数据已经有详细的 manifest，这是宝贵的元数据来源：

```python
import json
from pathlib import Path


def load_manifest(manifest_path: Path) -> dict:
    """读取 Orbbec 采集 manifest。"""
    with manifest_path.open() as f:
        return json.load(f)


manifest = load_manifest(Path(
    "数据采集样本/scene-box-transfer_pick-box_take-003_"
    "20260720T115545.119541Z_manifest.json"
))

# 从 manifest 中提取关键信息
for device in manifest["devices"]:
    role = device["role"]
    cam = device["device"]
    bag_info = device["bag"]
    stats = device["statistics"]

    print(f"设备: {role} ({cam['name']})")
    print(f"  分辨率: {cam['color']['width']}×{cam['color']['height']}")
    print(f"  FPS: {cam['color']['fps']}")
    print(f"  格式: {cam['color']['format']}")
    print(f"  BAG: {bag_info['file']} ({bag_info['format']})")
    print(f"  帧数: {stats['observed_rgbd_frame_sets']}")
    print()
```

### 3.2 多相机同步提取

manifest 中的 `synchronization` 字段提供了硬件同步质量信息。从你的数据看，时间偏差非常小（mean 125-1598 µs），说明硬件同步效果很好。

```python
"""多相机 Orbbec BAG 的概念性处理框架。

注意：具体 API 取决于 pyorbbecsdk 版本，以下展示数据工程逻辑而非可直接运行的代码。
实际使用时请参照 pyorbbecsdk 的 Pipeline.playback 和 FrameCallback API。
"""
from pathlib import Path

import cv2
import numpy as np


def extract_orbbec_multi_camera(
    manifest: dict,
    data_dir: Path,
    output_dir: Path,
    fps: int = 30,
) -> None:
    """从多台 Orbbec 相机的 BAG 中提取同步帧序列。

    核心挑战：5 台相机的帧需要按硬件同步时间对齐。
    manifest 中的 synchronization 字段提供了同步质量信息。
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    # 按 role 组织输出目录
    for device in manifest["devices"]:
        role = device["role"]
        cam_dir = output_dir / role
        (cam_dir / "color").mkdir(parents=True, exist_ok=True)
        (cam_dir / "depth").mkdir(parents=True, exist_ok=True)

    # 实际提取需要 pyorbbecsdk 的 playback API
    # 伪代码框架（具体 API 见 pyorbbecsdk 文档）：
    #
    # for device in manifest["devices"]:
    #     bag_path = data_dir / device["bag"]["file"]
    #     pipeline = ob.Pipeline(bag_path)  # 打开 BAG 回放
    #     # 遍历帧，按时间戳对齐，提取 color + depth
    #     # 保存为按时间戳命名的 PNG
    #
    # 关键：使用 manifest 中的 first/last_timestamp 作为对齐基准
    # 跨相机对齐用 paired_frame_sets_observed 和 timestamp_delta

    print("多相机提取完成。")
    print("注意：此步骤需要 pyorbbecsdk 的实际 API。")
    print("如果 SDK 不可用，先用模拟数据走通流程。")
```

### 3.3 多相机 LeRobot 数据集

当只有相机数据（无关节/动作）时，数据集结构略有不同：

```python
def write_camera_only_info_json(
    meta_dir: Path,
    cameras: list[dict],
    fps: int,
    total_frames: int,
) -> None:
    """为纯视觉数据集写 info.json。

    cameras 示例:
    [
        {"name": "observation.images.primary", "shape": [720, 1280, 3]},
        {"name": "observation.images.secondary_1", "shape": [720, 1280, 3]},
        ...
    ]
    """
    import json

    features = {}
    for cam in cameras:
        features[cam["name"]] = {
            "dtype": "video",
            "shape": cam["shape"],
            "names": {
                "height": "auto",
                "width": "auto",
                "channel": ["red", "green", "blue"],
            },
        }

    # 纯视觉数据集也需要 episode_index/frame_index/timestamp
    features["episode_index"] = {"dtype": "int64", "shape": [1]}
    features["frame_index"] = {"dtype": "int64", "shape": [1]}
    features["timestamp"] = {"dtype": "float32", "shape": [1]}
    features["index"] = {"dtype": "int64", "shape": [1]}

    # 如果后续补充了关节/动作，再加这些字段
    # features["observation.state"] = {...}
    # features["action"] = {...}

    info = {
        "codebase_version": "v3.0",
        "robot_type": "multi_camera_station",
        "fps": fps,
        "total_episodes": 1,
        "total_frames": total_frames,
        "features": features,
    }
    (meta_dir / "info.json").write_text(
        json.dumps(info, indent=2, ensure_ascii=False),
    )
```

## 4. 多 episode 数据集的组织

真实项目通常有几十到几百个 episode。LeRobot 的组织方式：

```text
multi_episode_dataset/
├── data/
│   └── train-00000-of-00001.parquet     # 所有 episode 的帧在同一个 Parquet
│                                            用 episode_index 列区分
├── videos/
│   └── chunk-000/
│       ├── observation.images.head/
│       │   ├── episode_000000.mp4       # 每个 episode 一个视频
│       │   ├── episode_000001.mp4
│       │   └── episode_000002.mp4
│       └── observation.images.wrist/
│           ├── episode_000000.mp4
│           └── ...
└── meta/
    ├── info.json
    ├── episodes.jsonl                   # 每个 episode 一行
    │   {"episode_index": 0, "tasks": ["pick box"], "length": 2097}
    │   {"episode_index": 1, "tasks": ["pick box"], "length": 2050}
    │   {"episode_index": 2, "tasks": ["place box"], "length": 2100}
    ├── tasks.jsonl
    │   {"task_index": 0, "task": "pick box"}
    │   {"task_index": 1, "task": "place box"}
    └── stats.json                        # 跨所有训练 episode 计算
```

多 episode 转换的核心代码结构：

```python
def convert_multiple_bags(
    bag_paths: list[Path],
    output_dir: Path,
    dataset_name: str,
    fps: int = 30,
) -> None:
    """把多个 bag 转成一个多 episode LeRobot 数据集。"""
    all_frames: list[FrameData] = []
    episode_lengths: list[int] = []
    episode_tasks: list[str] = []

    for episode_idx, bag_path in enumerate(bag_paths):
        frames = extract_and_align(bag_path, fps=fps)
        # 给每帧打上 episode_index
        for frame in frames:
            # 在实际实现中，FrameData 需要增加 episode_index 字段
            pass
        all_frames.extend(frames)
        episode_lengths.append(len(frames))
        episode_tasks.append("box transfer")  # 从 manifest 或标签文件读取

    # 统一写 Parquet、MP4、meta
    # ...（参考 2.2 节的代码，循环处理每个 episode 的视频编码）
```

## 5. 完整转换流水线设计

结合你前置计划第四周学到的工程化原则：

```text
原始 bag
  │
  ├─ inspect：检查话题、消息数、时间范围、编码格式
  │    └─ 输出 inspect_report.json
  │
  ├─ extract：抽取关节、动作、图像消息
  │    └─ 输出临时中间文件（不覆盖原始 bag）
  │
  ├─ align：按 FPS 对齐为帧序列
  │    └─ 输出 aligned_frames.jsonl + 图像帧
  │
  ├─ quality：检查缺帧、时间跳变、解码失败、维度一致性
  │    └─ 输出 quality_report.json
  │
  ├─ encode：图像帧 → MP4 视频
  │    └─ 输出 videos/ 目录
  │
  ├─ format：帧序列 → Parquet + meta/
  │    └─ 输出 LeRobot 数据集
  │
  └─ verify：用 LeRobotDataset 加载验证
       └─ 输出 verification_report.json
```

每一步的输入校验和输出校验都应记录在 manifest 中，可追溯、可重跑。

## 6. 验收清单

### 数据正确性

- [ ] 能从一份 bag 中提取并对齐关节、动作和图像。
- [ ] 对齐后的帧序列在 Foxglove 中回放与原始数据一致。
- [ ] LeRobot 数据集能被 `LeRobotDataset` 成功加载。
- [ ] 加载后的 `observation.state` 和 `action` shape 与 bag 中的实际维度一致。
- [ ] MP4 视频的帧数与 Parquet 中的 `frame_index` 一致。

### 工程质量

- [ ] 原始 bag 未被修改。
- [ ] 转换过程可重跑（幂等）。
- [ ] `stats.json` 只用训练集数据计算。
- [ ] 每个 episode 的 `episode_index`、`frame_index`、`timestamp` 正确。
- [ ] 生成了一份 manifest，记录源 bag 校验和、转换参数和工具版本。

### 能解释

- [ ] 为什么 LeRobot 用 MP4 而不是逐帧 JPEG？
- [ ] 为什么数据集存原始值而不是归一化值？
- [ ] 为什么 episode 边界对 DataLoader 很重要？
- [ ] 你的 Orbbec BAG 和 ROS bag 在读取方式上有什么本质区别？

## 7. 下一步

完成第一阶段后，你具备了**从 bag 到训练数据的完整转换能力**。接下来的方向：

- **第二阶段**：学习 ROS 运行时（QoS、TF、传感器驱动），理解数据是怎么实时采集的
- **第三阶段**：用 Ray 或类似工具处理几百个 episode 的批量转换
- **实操建议**：把 `数据采集样本/` 中的 5 路相机数据转成 LeRobot 格式，尝试用 LeRobot 官方训练脚本跑一个 ACT 或 Diffusion Policy
