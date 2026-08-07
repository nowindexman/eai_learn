# 03：图像、视频与 Foxglove 验收

## 1. 认识 ROS 图像消息

常见消息有：

| 消息 | 数据位置 | 关键字段 |
|---|---|---|
| `sensor_msgs/CompressedImage` | `data` 中的 JPEG/PNG 字节 | `format`、`header.stamp`、`frame_id` |
| `sensor_msgs/Image` | `data` 中的原始像素 | `encoding`、`height`、`width`、`step` |
| `sensor_msgs/CameraInfo` | 相机模型和标定 | `k`/`d`/`r`/`p`、`header.frame_id` |

`CompressedImage.format` 是提示，不是对字节内容的完整验证；真正解码后还要检查宽高、通道和颜色顺序。`CameraInfo` 应与对应相机 topic、时间和 frame_id 一起处理，不能只抽一份内参文件就假定整段 episode 永远有效。

## 2. 抽取 `CompressedImage`

```python
from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np
from rosbags.highlevel import AnyReader


def stamp_to_ns(message: object) -> int | None:
    header = getattr(message, "header", None)
    stamp = getattr(header, "stamp", None)
    if stamp is None:
        return None
    return int(stamp.sec) * 1_000_000_000 + int(stamp.nanosec)


def extract_compressed_images(
    bag_path: Path,
    topic: str,
    output_dir: Path,
) -> list[dict[str, object]]:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []

    with AnyReader([bag_path]) as reader:
        connections = [
            connection
            for connection in reader.connections
            if connection.topic == topic
        ]
        for index, (connection, log_time, rawdata) in enumerate(
            reader.messages(connections=connections),
        ):
            message = reader.deserialize(rawdata, connection.msgtype)
            encoded = bytes(message.data)
            image = cv2.imdecode(
                np.frombuffer(encoded, dtype=np.uint8),
                cv2.IMREAD_COLOR,
            )
            header_time = stamp_to_ns(message)
            row: dict[str, object] = {
                "index": index,
                "topic": topic,
                "log_time_ns": int(log_time),
                "header_stamp_ns": header_time,
                "format": str(message.format),
                "encoded_bytes": len(encoded),
                "decode_ok": image is not None,
            }
            if image is not None:
                height, width = image.shape[:2]
                format_hint = str(message.format).lower()
                if "png" in format_hint:
                    suffix = ".png"
                elif "jpeg" in format_hint or "jpg" in format_hint:
                    suffix = ".jpg"
                else:
                    suffix = ".bin"
                path = output_dir / f"{int(log_time):020d}_{index:06d}{suffix}"
                path.write_bytes(encoded)
                row.update(
                    {
                        "path": str(path),
                        "width": int(width),
                        "height": int(height),
                        "channels": int(image.shape[2])
                        if image.ndim == 3
                        else 1,
                    }
                )
            rows.append(row)
    return rows
```

OpenCV 默认把彩色图像作为 BGR 读取。如果后续使用 RGB 模型，需要显式 `cv2.cvtColor(image, cv2.COLOR_BGR2RGB)`，并在数据集说明中写明。文件名同时保留 `log_time` 和序号，避免同一纳秒时间戳覆盖文件。

## 3. 原始 `Image` 的注意事项

对 `sensor_msgs/Image`，不能直接把 `data` 当 JPEG。必须根据 `encoding`、`height`、`width`、`step` 解释字节布局；例如 `rgb8`、`bgr8`、`mono8`、`16UC1` 的 dtype 和通道数都不同。学习阶段可以先使用 `CompressedImage`，遇到原始图像时按具体 encoding 写分支，并为未知 encoding 明确报错。

## 4. 图像、视频和数据集的边界

- 图像序列保留每帧独立时间戳，最适合作为 canonical 派生数据。
- 视频适合播放和人工浏览，但编码可能改变时间精度、颜色、压缩和帧率；不要把转成视频当作无损归档。
- 训练表建议保存 `image_path`、`image_time_ns`、`camera_name`、`frame_id`、`decode_ok`、`source_bag_sha256`。
- 只有在确认 topic、编码、颜色、尺寸和时间后，才把图像加入训练样本。

## 5. Foxglove 人工验收

用 Foxglove Studio 打开原始 bag/MCAP 或可被其支持的 rosbag2 目录，按以下顺序检查：

1. 时间轴是否连续，开始/结束时间是否符合 episode。
2. 图像是否有明显花屏、黑帧、颜色反转、分辨率变化。
3. 关节、动作和图像是否在同一事件附近发生；不要只看单独一条曲线。
4. TF 是否能把相机 frame 连接到机器人基座；frame_id 缺失或错误要记录为数据问题。
5. 相机内参与图像 frame_id、尺寸是否匹配。

人工验收不是替代自动检查，而是发现“数值上正常、语义上错误”的最后一道门。验收记录至少包括文件、topic、观察时间段、结论和截图/备注路径。

## 6. 本篇练习

- [ ] 抽取 20 帧 `CompressedImage` 并写出图像索引表。
- [ ] 人为加入一张损坏图片，确认 `decode_ok=false` 而不是让程序静默跳过。
- [ ] 检查 OpenCV BGR/RGB 差异，并在 README 中写清楚。
- [ ] 用 Foxglove 对原始数据和抽取结果各做一次人工验收。
