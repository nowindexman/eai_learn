# 02：用 rosbags 读取 ROS 1 与 rosbag2

## 1. 统一读取模型

`AnyReader.messages()` 的核心返回值是：

```text
(connection, log_time, rawdata)
```

- `connection.topic`：话题名。
- `connection.msgtype`：消息类型名。rosbags 为统一处理，ROS 1 类型可能会按 ROS 2 风格显示，例如 `sensor_msgs/msg/JointState`。
- `log_time`：记录器写入消息时使用的时间，单位纳秒。
- `rawdata`：序列化后的字节串。
- `reader.deserialize(rawdata, connection.msgtype)`：把字节反序列化为生成的消息对象。

这个模型非常适合先做“原始事实检查”，因为你可以在需要时保留 `rawdata`，也可以在需要字段时再反序列化，不必一上来把所有图像都解码进内存。

## 2. 按 topic 选择连接

不要在每条消息上用字符串判断来代替连接过滤。先选出连接，可以减少无关 topic 的遍历：

```python
from pathlib import Path

from rosbags.highlevel import AnyReader


bag_path = Path("/data/raw/run_001.bag")

with AnyReader([bag_path]) as reader:
    wanted = {
        "/robot/joint_states",
        "/robot/odom",
    }
    connections = [
        connection
        for connection in reader.connections
        if connection.topic in wanted
    ]

    for connection, log_time, rawdata in reader.messages(
        connections=connections,
    ):
        message = reader.deserialize(rawdata, connection.msgtype)
        print(connection.topic, connection.msgtype, log_time, message)
```

如果某个 topic 没有匹配到，程序应明确报告，而不是静默生成空数据集：

```python
missing = wanted - {connection.topic for connection in connections}
if missing:
    raise RuntimeError(f"missing topics: {sorted(missing)}")
```

## 3. 消息对象不是字典

下面是常见消息的字段访问方式：

```python
def stamp_to_ns(message: object) -> int | None:
    """读取带 header 的 ROS 时间；无 header 时返回 None。"""
    header = getattr(message, "header", None)
    stamp = getattr(header, "stamp", None)
    if stamp is None:
        return None
    return int(stamp.sec) * 1_000_000_000 + int(stamp.nanosec)


if connection.msgtype.endswith("JointState"):
    print("joint names:", list(message.name))
    print("positions:", list(message.position))
elif connection.msgtype.endswith("Odometry"):
    position = message.pose.pose.position
    print("xyz:", position.x, position.y, position.z)
```

这段代码面向 `rosbags.AnyReader` 反序列化后的统一消息对象；它会将 ROS 1 类型归一化为 ROS 2 风格，因此这里访问的是 `sec`/`nanosec`。若直接处理原生 ROS 1 `genpy.Time`，字段名是 `secs`/`nsecs`，不能混用。

数组长度不是默认固定的。`JointState` 的 `name`、`position`、`velocity`、`effort` 可能长度不同或为空；表格化前要先决定缺失值策略，不能按下标盲目拼接。

## 4. `log_time` 与 `header.stamp`

对每条消息同时保存两个时间字段，后续才有能力判断时间偏差：

```python
rows: list[dict[str, int | str | None]] = []

with AnyReader([bag_path]) as reader:
    for connection, log_time, rawdata in reader.messages(
        connections=connections,
    ):
        message = reader.deserialize(rawdata, connection.msgtype)
        rows.append(
            {
                "topic": connection.topic,
                "log_time_ns": int(log_time),
                "header_stamp_ns": stamp_to_ns(message),
            }
        )
```

两者的语义不同：

| 时间 | 常见含义 | 不能直接推断什么 |
|---|---|---|
| `log_time` | 记录器接收/写入消息时采用的时间 | 不一定是传感器曝光时间 |
| `header.stamp` | 发布者或传感器写入消息的时间 | 不一定和主机时钟同步 |
| `/clock` | ROS 仿真时间源 | 不等于每个消息的 header 时间 |

差值大并不自动等于丢包；可能是传感器时钟、主机时钟、传输延迟或仿真时间造成的。先记录事实，再根据采集系统的时钟设计解释。

## 5. 类型存储与自定义消息

`AnyReader` 会尝试从 bag 元数据或自身类型系统获得定义。旧 rosbag2、私有消息或缺失定义时，需要提供匹配发行版的 typestore：

```python
from pathlib import Path

from rosbags.highlevel import AnyReader
from rosbags.typesys import Stores, get_typestore


typestore = get_typestore(Stores.ROS2_HUMBLE)
with AnyReader(
    [Path("/data/raw/run_002")],
    default_typestore=typestore,
) as reader:
    for connection, log_time, rawdata in reader.messages():
        message = reader.deserialize(rawdata, connection.msgtype)
        # 这里再按 connection.msgtype 处理
```

发行版只应作为起点。若自定义 `.msg`/`.idl` 改过字段，必须注册与录制时完全匹配的定义；“名称相同”不代表布局相同。必要时使用 `get_types_from_msg()`、`get_types_from_idl()` 和 `typestore.register()` 注册自定义类型。

## 6. 一个可复用的字段抽取函数

先固定输出契约，再增加消息类型。示例只抽取标量，不把变长数组偷偷塞进一列：

```python
from collections.abc import Iterator
from pathlib import Path

from rosbags.highlevel import AnyReader


def read_joint_positions(
    bag_path: Path,
    topic: str,
) -> Iterator[dict[str, object]]:
    with AnyReader([bag_path]) as reader:
        connections = [
            connection
            for connection in reader.connections
            if connection.topic == topic
        ]
        for connection, log_time, rawdata in reader.messages(
            connections=connections,
        ):
            message = reader.deserialize(rawdata, connection.msgtype)
            yield {
                "topic": topic,
                "log_time_ns": int(log_time),
                "header_stamp_ns": stamp_to_ns(message),
                "joint_names": tuple(message.name),
                "positions": tuple(float(value) for value in message.position),
            }
```

这一步的结果仍是“消息级记录”，还没有做时间对齐，也没有假设每个时间点所有传感器都存在。同步和缺帧策略放到第三周。

## 7. 本篇练习

1. 分别读取一个 `.bag` 和一个 rosbag2 目录，输出 topic/type/count。
2. 选择一个 `JointState`，打印前三条消息的 `log_time_ns`、`header_stamp_ns` 和关节数组长度。
3. 找一个没有 `header` 的消息，确认代码返回 `None`，而不是抛出 `AttributeError`。
4. 把结果写成 JSON Lines；每行必须带输入文件标识、topic 和两个时间字段。

完成标准是：你能解释每个字段从哪里来，并能指出任何一条消息是“原始字节”“反序列化对象”还是“自己抽取的表格行”。
