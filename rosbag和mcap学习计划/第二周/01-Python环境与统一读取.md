# 01：Python 环境与统一读取

## 1. 建立隔离环境

在学习计划目录执行。下面命令适用于 macOS/Linux；Windows 需要把激活命令换成 PowerShell 写法。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install rosbags mcap
```

第三周再安装表格和图像依赖，避免一开始把环境弄得过重：

```bash
python -m pip install pandas pyarrow numpy opencv-python-headless
```

确认实际使用的是虚拟环境，而不是系统 Python：

```bash
which python
python -c "from importlib.metadata import version; print('rosbags', version('rosbags'))"
python -c "import rosbags; print(rosbags.__file__)"
```

`rosbags` 是纯 Python 的 bag 读取/写入库，不等于 ROS 运行时；它可以在没有 `roscore` 或 `ros2` 命令的环境中处理支持的 bag。消息定义缺失或版本不匹配时，仍要提供正确的 typestore 或自定义定义。

## 2. 输入路径的约定

```text
ROS 1：/data/raw/run_001.bag
ROS 2：/data/raw/run_002/        # 目录，通常含 metadata.yaml 和存储文件
MCAP： /data/raw/run_003.mcap    # 独立 MCAP，先用 MCAP SDK 读取容器层
```

`AnyReader` 可以统一读取 ROS 1 和 ROS 2，但一次读取器中的输入应属于同一类 ROS bag；不要把 ROS 1 和 ROS 2 路径混在同一个 `AnyReader` 实例里。路径不存在、权限不足和正在写入的文件，都应先作为输入错误处理。

## 3. 用 `AnyReader` 做第一次只读检查

把下面代码保存为 `inspect_rosbag.py`。它只遍历和打印信息，不会修改 bag。

```python
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from rosbags.highlevel import AnyReader


def inspect_bag(path: Path) -> None:
    """打印 bag 的基本事实；输入文件不会被写入。"""
    if not path.exists():
        raise FileNotFoundError(path)

    with AnyReader([path]) as reader:
        print(f"path: {path}")
        print(f"start_time_ns: {reader.start_time}")
        print(f"end_time_ns: {reader.end_time}")
        print(f"duration_ns: {reader.duration}")
        print(f"message_count: {reader.message_count}")

        for connection in reader.connections:
            print(
                "connection:"
                f" topic={connection.topic}"
                f" type={connection.msgtype}"
            )

        counts: Counter[str] = Counter()
        for connection, _log_time, _rawdata in reader.messages():
            counts[connection.topic] += 1

        print("counts:")
        for topic, count in sorted(counts.items()):
            print(f"  {topic}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("bag", type=Path)
    args = parser.parse_args()
    inspect_bag(args.bag)


if __name__ == "__main__":
    main()
```

运行方式：

```bash
python inspect_rosbag.py /data/raw/run_001.bag
python inspect_rosbag.py /data/raw/run_002
```

`reader.start_time`、`reader.end_time` 和 `reader.duration` 的单位是纳秒。它们描述读取器视角下的记录时间范围，不是自动从每个消息的 `header.stamp` 重新计算出来的。

## 4. 第一轮检查应该记录什么

至少保存下面这些字段：

| 字段 | 来源 | 作用 |
|---|---|---|
| 输入路径和文件大小 | 文件系统 | 定位原始输入 |
| ROS bag 类型 | 路径/读取器 | 区分 rosbag1 与 rosbag2 |
| topic、消息类型 | `reader.connections` | 确认数据内容 |
| 总消息数、时长 | `reader.message_count` 等 | 发现空文件或短录制 |
| 每 topic 消息数 | 遍历结果 | 和采集预期对比 |
| 工具版本 | Python 环境 | 使结果可复现 |

这一轮不要做以下事情：改写原 bag、删除“无用 topic”、把消息直接转成没有时间列的 CSV，或凭文件名猜测 ROS 发行版。后面每一步都应建立在这份事实记录之上。
