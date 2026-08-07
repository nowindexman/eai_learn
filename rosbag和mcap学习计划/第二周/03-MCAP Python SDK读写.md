# 03：用 MCAP Python SDK 读写容器

## 1. 先分清两个层次

MCAP Python SDK 负责读取 MCAP 记录结构：Header、Schema、Channel、Message、Metadata、Attachment、Summary 等。它不会自动把所有 message bytes 变成机器人语义对象。

```text
MCAP 容器层：能看到 channel、时间、原始 bytes、schema 元信息
消息解码层：根据 message_encoding 和 schema，得到 JSON/Protobuf/ROS 消息对象
任务语义层：单位、坐标系、关节顺序、episode 标签和质量结论
```

三层不能混为一谈。尤其是 ROS 2 常见的 `cdr`，需要 ROS 2 类型定义和 CDR 解码器；仅安装 `mcap` 不等于安装了 ROS 2 解码能力。

## 2. 读取 channel 和原始消息

先用结构读取器，不做业务转换：

```python
from __future__ import annotations

import argparse
from pathlib import Path

from mcap.reader import make_reader


def read_mcap(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(path)

    with path.open("rb") as stream:
        reader = make_reader(stream)
        for schema, channel, message in reader.iter_messages():
            schema_name = schema.name if schema is not None else None
            schema_encoding = schema.encoding if schema is not None else None
            print(
                {
                    "topic": channel.topic,
                    "schema": schema_name,
                    "schema_encoding": schema_encoding,
                    "message_encoding": channel.message_encoding,
                    "log_time_ns": message.log_time,
                    "publish_time_ns": message.publish_time,
                    "bytes": len(message.data),
                }
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mcap", type=Path)
    read_mcap(parser.parse_args().mcap)
```

`schema` 可能是 `None`。这是合法的 MCAP 状态，不能用“没有 schema”直接判定文件损坏；但它会限制后续解码能力。`publish_time` 和 `log_time` 也可能相同或不同，应保留原值，不要覆盖。

## 3. 写一个最小 JSON MCAP

下面例子使用官方 Python SDK 的 `Writer` 注册接口。它写入的是 JSON 消息，不是 ROS 2 CDR：

```python
from __future__ import annotations

import json
import time
from pathlib import Path

from mcap.records import Channel, Message, Schema
from mcap.writer import Writer


def write_json_mcap(path: Path) -> None:
    now_ns = time.time_ns()
    with path.open("wb") as stream:
        writer = Writer(stream)
        writer.start(profile="", library="eai-learn-mcap-example")

        schema_id = writer.register_schema(
            Schema(
                name="ExampleState",
                encoding="jsonschema",
                data=(
                    b'{"type":"object","properties":{"value":{"type":"number"}}}'
                ),
            )
        )
        channel_id = writer.register_channel(
            Channel(
                topic="/example/state",
                message_encoding="json",
                schema_id=schema_id,
            )
        )

        for index in range(3):
            timestamp_ns = now_ns + index * 100_000_000
            payload = json.dumps(
                {"value": index, "source": "exercise"},
                separators=(",", ":"),
            ).encode("utf-8")
            writer.add_message(
                Message(
                    channel_id=channel_id,
                    log_time=timestamp_ns,
                    publish_time=timestamp_ns,
                    data=payload,
                )
            )

        writer.finish()


write_json_mcap(Path("example-json.mcap"))
```

运行后检查：

```bash
mcap info example-json.mcap
mcap list schemas example-json.mcap
mcap cat example-json.mcap --topics /example/state --json
```

如果本机 SDK 版本对 `Writer` 参数有差异，以该版本的官方示例和 `inspect.signature()` 为准；不要凭网上旧示例混用 `Schema`/`Channel` 对象 API 与关键字注册 API。

## 4. 读取 JSON message

```python
import json
from pathlib import Path

from mcap.reader import make_reader


with Path("example-json.mcap").open("rb") as stream:
    reader = make_reader(stream)
    for _schema, channel, message in reader.iter_messages(
        topics=["/example/state"],
    ):
        if channel.message_encoding != "json":
            raise ValueError(channel.message_encoding)
        value = json.loads(message.data.decode("utf-8"))
        print(message.log_time, value["value"])
```

如果某个 SDK 版本的 `iter_messages()` 不接受 `topics` 参数，先遍历后用 `if channel.topic == ...` 过滤；过滤方式不影响概念，具体以安装版本 API 为准。

## 5. ROS 2 MCAP 的正确处理方式

ROS 2 用 MCAP 存储时，常见 channel 的 `message_encoding` 是 `cdr`。推荐分层处理：

1. 用 `mcap info`/Python SDK 做容器级检查，保存 topic、编码、时间和字节数。
2. 用 rosbag2/`rosbags`/ROS 2 类型支持做 CDR 反序列化。
3. 只把经过类型和单位确认的字段写入 Parquet 或训练数据。

不要把以下命令的输出当成已经解码的 ROS 2 消息：

```bash
mcap cat ros2-data.mcap --json
```

当前 CLI 对 `ros1`、`protobuf`、`json` 等部分编码支持 JSON 输出；`cdr` 需要专用解码路径。若只有一个独立 `.mcap` 文件而没有 `metadata.yaml`，也不能仅凭文件数量判断元数据丢失，要先查看 MCAP 内部 schema/channel/metadata，再判断该文件是否包含足够的 ROS 类型信息。

## 6. 本篇练习

- [ ] 写出一个 JSON MCAP，并能被 `mcap info` 和 `mcap cat --json` 读取。
- [ ] 统计每个 channel 的消息数量和 payload 字节数。
- [ ] 找一个 ROS 2 CDR MCAP，说明为什么它可以被 Foxglove 展示但未必能被通用 JSON 工具解码。
- [ ] 对比 `publish_time` 和 `log_time`，不要只保留其中一个。

本篇结束时，你应能回答“MCAP 能不能读”与“消息能不能解码”是两个不同问题。
