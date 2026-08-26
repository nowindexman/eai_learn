# 02：LeRobot 数据集格式详解

> LeRobot v3.0 是 Hugging Face 生态的机器人数据集标准格式。它的核心设计思想：**Parquet 存表格数据，MP4 存视频，JSON 存元数据**——三种格式各司其职，组合成一个可流式加载、可随机访问、体积高效的训练数据集。

## 1. 完整目录结构

```text
my_dataset/
├── data/
│   ├── train-00000-of-00001.parquet
│   └── train-00001-of-00001.parquet       # 大数据集可分片
│
├── videos/
│   └── chunk-000/                         # 分块目录
│       ├── observation.images.head_camera/
│       │   ├── episode_000000.mp4
│       │   ├── episode_000001.mp4
│       │   └── ...
│       └── observation.images.wrist_camera/
│           ├── episode_000000.mp4
│           └── ...
│
├── meta/
│   ├── info.json          # 数据集级配置（FPS、特征定义、形状）
│   ├── episodes.jsonl     # 每个 episode 的元数据
│   ├── tasks.jsonl        # 任务定义
│   ├── stats.json         # 归一化统计量
│   └── modality.json      # 模态分组（state / action / image）
│
├── images/                # 可选：使用 PNG 而非 MP4 时
│   └── chunk-000/
│       └── observation.images.head_camera/
│           ├── frame_000000.png
│           └── ...
│
└── README.md              # 数据集说明（HF Hub 展示用）
```

## 2. info.json：数据集的 schema 契约

这是最重要的文件，训练代码靠它决定怎么解析数据：

```json
{
  "codebase_version": "v3.0",
  "robot_type": "aloha",
  "fps": 50,
  "total_episodes": 10,
  "total_frames": 5000,
  "data_path": "data/train-{episode_chunk:03d}-{episode_index:06d}.parquet",
  "video_path": "videos/chunk-{episode_chunk:03d}/{video_key}/episode_{episode_index:06d}.mp4",
  "features": {
    "observation.images.head_camera": {
      "dtype": "video",
      "shape": [480, 640, 3],
      "names": {
        "height": [0, 1, "...", 479],
        "width": [0, 1, "...", 639],
        "channel": ["red", "green", "blue"]
      }
    },
    "observation.state": {
      "dtype": "float32",
      "shape": [14],
      "names": {
        "joints": [
          "shoulder_pan_left", "shoulder_lift_left",
          "elbow_left", "wrist_left",
          "gripper_left",
          "shoulder_pan_right", "shoulder_lift_right",
          "elbow_right", "wrist_right",
          "gripper_right"
        ]
      }
    },
    "action": {
      "dtype": "float32",
      "shape": [14],
      "names": {
        "joints": [
          "shoulder_pan_left", "shoulder_lift_left",
          "elbow_left", "wrist_left",
          "gripper_left",
          "shoulder_pan_right", "shoulder_lift_right",
          "elbow_right", "wrist_right",
          "gripper_right"
        ]
      }
    },
    "episode_index": {
      "dtype": "int64",
      "shape": [1]
    },
    "frame_index": {
      "dtype": "int64",
      "shape": [1]
    },
    "timestamp": {
      "dtype": "float32",
      "shape": [1]
    },
    "index": {
      "dtype": "int64",
      "shape": [1]
    }
  }
}
```

### 特征命名规则

LeRobot 使用点号分层命名，这些前缀有语义含义：

| 前缀 | 含义 | 示例 |
|------|------|------|
| `observation.images.*` | 相机图像（会存为 MP4 或 PNG） | `observation.images.head_camera` |
| `observation.state` | 本体状态（关节角度等） | `observation.state` |
| `action` | 动作（模型要预测的目标） | `action` |
| `episode_index` | 所属 episode 编号 | `0, 1, 2, ...` |
| `frame_index` | 在 episode 内的帧序号 | `0, 1, 2, ...` |
| `timestamp` | 相对 episode 开始的秒数 | `0.0, 0.02, 0.04, ...` |
| `index` | 全局帧序号 | `0, 1, 2, ..., 4999` |

> `observation.images.*` 前缀是特殊的——LeRobot 会把带这个前缀的特征识别为视频流，自动存为 MP4。如果叫 `observation.img`（没有 images）就不会被当视频处理。

## 3. Parquet 中的每一行长什么样

每个 Parquet 文件的一行代表**一个时间步**。关键字段：

```text
index | episode_index | frame_index | timestamp | observation.state        | action                  | observation.images.head_camera | observation.images.wrist_camera
0     | 0             | 0           | 0.0       | [0.1, -0.05, 0.3, ...]  | [0.12, -0.03, 0.31, ...]| (视频帧指针)                   | (视频帧指针)
1     | 0             | 1           | 0.02      | [0.12, -0.03, 0.31, ...]| [0.15, -0.01, 0.35, ...]| (视频帧指针)                   | (视频帧指针)
...
```

图像列在 Parquet 里不存像素字节，而是存一个指向 MP4 帧的指针结构。LeRobot 的 DataLoader 在读取时会解码对应帧。

## 4. episodes.jsonl 和 tasks.jsonl

### episodes.jsonl

每行一个 episode 的元数据：

```json
{"episode_index": 0, "tasks": ["pick up the red block"], "length": 500}
{"episode_index": 1, "tasks": ["pick up the red block"], "length": 480}
{"episode_index": 2, "tasks": ["pick up the blue block"], "length": 510}
```

### tasks.jsonl

任务定义，供跨 episode 查询使用：

```json
{"task_index": 0, "task": "pick up the red block"}
{"task_index": 1, "task": "pick up the blue block"}
```

## 5. stats.json：归一化统计

```json
{
  "observation.state": {
    "mean": [0.12, -0.05, 0.31, -0.15, 0.02, 0.11, -0.04, 0.29, -0.13, 0.01, 0.05, -0.03, 0.02, 0.04],
    "std": [0.08, 0.15, 0.10, 0.12, 0.03, 0.07, 0.14, 0.09, 0.11, 0.02, 0.04, 0.03, 0.05, 0.03],
    "min": [-1.57, -1.20, -0.80, -1.50, 0.00, -1.57, -1.20, -0.80, -1.50, 0.00, 0.00, 0.00, 0.00, 0.00],
    "max": [1.57, 1.20, 0.80, 1.50, 0.05, 1.57, 1.20, 0.80, 1.50, 0.05, 0.05, 0.05, 0.05, 0.05]
  },
  "action": {
    "mean": [0.01, -0.02, 0.05, -0.01, 0.00, 0.01, -0.01, 0.04, -0.02, 0.00, 0.01, 0.00, 0.01, 0.00],
    "std": [0.05, 0.08, 0.06, 0.04, 0.01, 0.04, 0.07, 0.05, 0.03, 0.01, 0.01, 0.01, 0.01, 0.01],
    "min": [-0.15, -0.30, -0.10, -0.12, -0.01, -0.12, -0.25, -0.08, -0.10, -0.01, -0.01, -0.01, -0.01, -0.01],
    "max": [0.15, 0.30, 0.10, 0.12, 0.01, 0.12, 0.25, 0.08, 0.10, 0.01, 0.01, 0.01, 0.01, 0.01]
  }
}
```

**计算方式**：遍历所有训练集帧，对每个特征维度计算 mean/std/min/max。图像特征不需要在这里统计（归一化方式固定为 `[0,1]` 或 `[-1,1]`）。

## 6. MP4 视频编码的注意事项

LeRobot 把整个 episode 的图像序列编码为一个 MP4 文件。这带来高压缩率，但也有代价：

| 优势 | 风险 |
|------|------|
| 体积比 JPEG 帧小 10-50 倍 | 有损编码（H.264/H.265） |
| 加载时按需解码 | 解码需要额外 CPU |
| HF Hub 可流式预览 | 帧索引依赖恒定帧率假设 |

**编码参数建议**：
- 使用 `h264` 编码（兼容性最好）
- 设置 `crf=18`（视觉无损到接近无损）
- 保持恒定帧率（VFR 会破坏帧索引）
- 分辨率和 FPS 必须与 `info.json` 一致

```python
import subprocess

def encode_episode_video(
    frames_dir: str,
    output_path: str,
    fps: int,
) -> None:
    """把一个 episode 的图像帧编码为 MP4。"""
    subprocess.run([
        "ffmpeg",
        "-y",
        "-framerate", str(fps),
        "-i", f"{frames_dir}/frame_%06d.png",
        "-c:v", "libx264",
        "-crf", "18",
        "-pix_fmt", "yuv420p",      # 兼容性最好的像素格式
        "-r", str(fps),
        output_path,
    ], check=True)
```

## 7. 用代码创建一个最小 LeRobot 数据集

下面用 LeRobot SDK 创建一个最小数据集。你需要先安装：

```bash
pip install 'lerobot[common]'
```

```python
"""从已抽取的关节状态和图像帧，创建一个 LeRobot v3 数据集。"""
from pathlib import Path

import numpy as np
import pandas as pd
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

DATASET_NAME = "my_first_dataset"
FPS = 30
STATE_DIM = 14
ACTION_DIM = 14


def create_minimal_dataset(output_dir: Path, num_episodes: int = 3) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    all_rows: list[dict[str, object]] = []
    global_index = 0

    for episode_idx in range(num_episodes):
        num_frames = 100  # 每个 episode 100 帧

        for frame_idx in range(num_frames):
            timestamp = frame_idx / FPS

            # 这里用模拟数据；实际从 bag 读取
            state = np.random.randn(STATE_DIM).astype(np.float32) * 0.1
            action = state + np.random.randn(ACTION_DIM).astype(np.float32) * 0.02

            row: dict[str, object] = {
                "index": global_index,
                "episode_index": episode_idx,
                "frame_index": frame_idx,
                "timestamp": timestamp,
                "observation.state": state.tolist(),
                "action": action.tolist(),
            }
            all_rows.append(row)
            global_index += 1

    df = pd.DataFrame(all_rows)

    # 写 Parquet
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    df.to_parquet(data_dir / "train-00000-of-00001.parquet", index=False)

    # 写 info.json
    meta_dir = output_dir / "meta"
    meta_dir.mkdir(parents=True, exist_ok=True)

    write_info_json(meta_dir, num_episodes, len(all_rows))
    write_episodes_jsonl(meta_dir, num_episodes)
    write_tasks_jsonl(meta_dir)
    write_stats_json(meta_dir, df)


def write_info_json(meta_dir: Path, num_episodes: int, total_frames: int) -> None:
    import json

    info = {
        "codebase_version": "v3.0",
        "robot_type": "custom",
        "fps": FPS,
        "total_episodes": num_episodes,
        "total_frames": total_frames,
        "features": {
            "observation.state": {
                "dtype": "float32",
                "shape": [STATE_DIM],
                "names": {"joints": [f"joint_{i}" for i in range(STATE_DIM)]},
            },
            "action": {
                "dtype": "float32",
                "shape": [ACTION_DIM],
                "names": {"joints": [f"joint_{i}" for i in range(ACTION_DIM)]},
            },
            "episode_index": {"dtype": "int64", "shape": [1]},
            "frame_index": {"dtype": "int64", "shape": [1]},
            "timestamp": {"dtype": "float32", "shape": [1]},
            "index": {"dtype": "int64", "shape": [1]},
        },
    }
    (meta_dir / "info.json").write_text(
        json.dumps(info, indent=2, ensure_ascii=False),
    )


def write_episodes_jsonl(meta_dir: Path, num_episodes: int) -> None:
    lines = []
    for i in range(num_episodes):
        episode = {
            "episode_index": i,
            "tasks": ["demonstration"],
            "length": 100,
        }
        lines.append(json.dumps(episode, ensure_ascii=False))
    (meta_dir / "episodes.jsonl").write_text("\n".join(lines) + "\n")


def write_tasks_jsonl(meta_dir: Path) -> None:
    task = {"task_index": 0, "task": "demonstration"}
    (meta_dir / "tasks.jsonl").write_text(
        json.dumps(task, ensure_ascii=False) + "\n",
    )


def write_stats_json(meta_dir: Path, df: pd.DataFrame) -> None:
    import json

    stats: dict[str, dict[str, list[float]]] = {}
    for col in ["observation.state", "action"]:
        values = np.array(df[col].tolist())
        stats[col] = {
            "mean": values.mean(axis=0).tolist(),
            "std": values.std(axis=0).tolist(),
            "min": values.min(axis=0).tolist(),
            "max": values.max(axis=0).tolist(),
        }
    (meta_dir / "stats.json").write_text(
        json.dumps(stats, indent=2, ensure_ascii=False),
    )


import json

create_minimal_dataset(Path(DATASET_NAME))
```

> 这段代码展示了文件级别的结构。实际项目中，推荐使用 LeRobot SDK 的高层 API（`LeRobotDataset.create`）来创建数据集，它会自动处理路径模板、视频编码和 Hub 上传。上述代码帮助你理解底层结构，便于排查问题和自定义。

## 8. 加载并验证数据集

```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

dataset = LeRobotDataset(DATASET_NAME)

print(f"FPS: {dataset.fps}")
print(f"Episodes: {dataset.num_episodes}")
print(f"Samples: {dataset.num_samples}")
print(f"Features: {list(dataset.features.keys())}")

# 取一条样本
sample = dataset[0]
print(f"observation.state shape: {sample['observation.state'].shape}")
print(f"action shape: {sample['action'].shape}")
print(f"episode_index: {sample['episode_index']}")
```

## 9. 本篇练习

1. 运行上面的代码，生成一个最小 LeRobot 数据集，并用 `LeRobotDataset` 加载验证。
2. 打开生成的 `info.json`，对照本篇第 2 节检查每个字段是否正确。
3. 手动修改 `stats.json` 中的一个 mean 值，观察加载后的数据是否受影响（它不会，因为 stats 是训练代码读取的，不是 DataLoader 自动应用的）。
4. 思考：如果你有 2 个相机，每个 episode 500 帧，30 FPS，你该怎么组织 `videos/` 目录？

下一篇将深入 HDF5 (robomimic) 数据集格式——另一种同样重要的训练数据格式。
