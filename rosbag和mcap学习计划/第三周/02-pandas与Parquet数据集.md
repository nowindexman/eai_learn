# 02：用 pandas 与 Parquet 组织数据集

## 1. 为什么从消息变成表格

bag/MCAP 适合保留事件流和原始消息；Parquet 适合列式查询、按列读取、分区存储和下游分析。两者的关系是：

```text
原始 bag/MCAP ──读取/解码/同步──> 规范化表 ──质量检查──> Parquet 派生数据集
```

Parquet 不应替代原始数据。任何列都要能追溯到源 topic、源时间和源文件。

## 2. 表结构先于写文件

以机器人状态为例，推荐把可变长度的关节数组展开为稳定列，或单独设计 Arrow list 列，不能一会儿按名字、一会儿按数组下标：

```text
episode_id: string
frame_index: int64
time_ns: int64
source_time_ns: int64 nullable
time_basis: string
joint_position__left_shoulder: float32 nullable
joint_position__right_shoulder: float32 nullable
action__linear_x_mps: float32 nullable
frame_id: string nullable
source_topic: string
source_bag_sha256: string
```

字段名里的单位是数据契约的一部分。`position` 不能脱离说明变成“可能是弧度也可能是度”。坐标系也要写入字段说明或 manifest，例如 `pose_frame=base_link`。

## 3. 从消息行构造 DataFrame

```python
from __future__ import annotations

from collections.abc import Iterable

import pandas as pd


def joint_rows(messages: Iterable[dict[str, object]]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for message in messages:
        names = message["joint_names"]
        positions = message["positions"]
        if len(names) != len(positions):
            raise ValueError("joint name/position length mismatch")

        row: dict[str, object] = {
            "episode_id": message["episode_id"],
            "time_ns": int(message["log_time_ns"]),
            "source_time_ns": message["header_stamp_ns"],
            "time_basis": "log_time_ns",
            "source_topic": message["topic"],
        }
        for name, position in zip(names, positions, strict=True):
            row[f"joint_position__{name}"] = float(position)
        rows.append(row)

    frame = pd.DataFrame(rows)
    if frame.empty:
        raise ValueError("no rows produced")
    return frame.sort_values("time_ns").reset_index(drop=True)
```

这里使用的是消息抽取后的普通字典，不代表 `rosbags` 直接返回字典。消息对象到字典的边界应在代码中明确。

## 4. 写入与读取 Parquet

```python
from pathlib import Path


output = Path("artifacts/week3/episode_0001/state.parquet")
output.parent.mkdir(parents=True, exist_ok=True)
frame.to_parquet(output, engine="pyarrow", index=False)

loaded = pd.read_parquet(
    output,
    engine="pyarrow",
    columns=["episode_id", "time_ns", "joint_position__left_shoulder"],
)
print(loaded.dtypes)
```

大数据量时按 `episode_id` 或日期分区写入，但不要把每一行随机写成独立文件。分区字段要低基数、稳定且便于查询；episode_id 如果非常多，先评估文件数量和对象存储成本。

## 5. 列表、图像和二进制数据怎么放

- 固定关节集合：展开成标量列，查询和训练最简单。
- 关节集合会变化：保存 `joint_names` 版本和 Arrow list 列，或先做 schema 对齐。
- 图像：通常在 Parquet 中存 `image_path`、`image_time_ns`、`encoding`、`width`、`height`、`decode_ok`，图片字节留在文件系统或对象存储。
- 小型标量数组：可以用 Arrow list，但要固定元素语义和 dtype。
- 原始 ROS message bytes：只有在明确需要时保存，并同时保存 `message_encoding`、schema 标识和源校验和。

把 JPEG bytes 直接塞进训练表并非绝对错误，但会让查询、分片和缓存变复杂；学习阶段先使用图像索引更容易验证时间和质量。

## 6. 训练划分和数据集版本

随机按行切分会把同一个 episode 的相邻帧泄漏到训练集和验证集。应按 episode、场景或任务批次切分：

```python
episode_ids = sorted(frame["episode_id"].unique())
train_ids = set(episode_ids[: max(1, int(len(episode_ids) * 0.8))])
train = frame[frame["episode_id"].isin(train_ids)]
valid = frame[~frame["episode_id"].isin(train_ids)]
```

真实项目要固定随机种子或显式保存 episode 清单，并记录 `dataset_schema_version`。Parquet 文件格式版本、数据集 schema 版本和代码版本是三个不同概念。

## 7. 本篇练习

1. 把一个 `JointState` topic 展开为列，并保存 `state.parquet`。
2. 用 `pd.read_parquet(columns=...)` 只读取两列，观察列式读取的行为。
3. 为图像建立 `images.parquet`，只写路径和时间，不把图片字节混入状态表。
4. 按 episode 而不是按行生成 train/valid 清单。
