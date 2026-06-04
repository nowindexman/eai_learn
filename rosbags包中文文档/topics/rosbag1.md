> 原文地址：https://ternaris.gitlab.io/rosbags/topics/rosbag1.html

# Rosbags

`rosbags.rosbag1` 包提供对旧版 bag 格式中存储的原始消息的快速只读访问。rosbag1 支持是为 ROS2 环境构建的，部分 API 和值会执行归一化处理以模拟 ROS2 行为，使来自 rosbag1 和 rosbag2 的消息表现一致。最显著的是，消息类型会在内部重命名以匹配其 ROS2 对应类型。

## 写入 rosbag1

`Writer` 类的实例可以创建并写入新的 rosbag1 文件。它通常作为上下文管理器使用。在写入某个主题的第一条消息之前，必须先将该主题添加到 bag 中。以下示例展示了典型的使用模式：

```python
from rosbags.rosbag1 import Writer
from rosbags.typesys import Stores, get_typestore

# 为目标 ROS 发行版创建类型存储，并获取字符串类。
typestore = get_typestore(Stores.ROS1_NOETIC)
String = typestore.types['std_msgs/msg/String']

# 创建 writer 实例并以写入模式打开。
with Writer('/home/ros/rosbag_2020_03_24.bag') as writer:
    # 添加新的连接。
    topic = '/chatter'
    msgtype = String.__msgtype__
    connection = writer.add_connection(topic, msgtype, typestore=typestore)

    # 序列化并写入消息。
    timestamp = 42
    message = String('hello world')
    writer.write(connection, timestamp, typestore.serialize_ros1(message, msgtype))
```

## 读取 rosbag1

`Reader` 类的实例通常作为上下文管理器使用，在 bag 打开后提供对 bag 元数据和内容的访问。以下示例展示了典型的使用模式：

> **注意**
>
> 对于读取 bag，你可能希望使用高层 API [AnyReader](../highlevel/api.md)，因为它为 ROS1 和 ROS2 bag 提供了更简单且统一的 API。

```python
from rosbags.rosbag1 import Reader
from rosbags.typesys import Stores, get_typestore

# 为匹配的 ROS 发行版创建类型存储。
typestore = get_typestore(Stores.ROS1_NOETIC)

# 创建 reader 实例并以读取模式打开。
with Reader('/home/ros/rosbag_2020_03_24') as reader:
    # 主题和消息类型信息可通过 .connections 列表获取。
    for connection in reader.connections:
        print(connection.topic, connection.msgtype)

    # 遍历消息。
    for connection, timestamp, rawdata in reader.messages():
        if connection.topic == '/imu_raw/Imu':
            msg = typestore.deserialize_ros1(rawdata, connection.msgtype)
            print(msg.header.frame_id)

    # .messages() 方法支持连接过滤器。
    connections = [x for x in reader.connections if x.topic == '/imu_raw/Imu']
    for connection, timestamp, rawdata in reader.messages(connections=connections):
        msg = typestore.deserialize_ros1(rawdata, connection.msgtype)
        print(msg.header.frame_id)
```

---

[← 类型系统](typesys.md) | [Rosbag2 →](rosbag2.md)
