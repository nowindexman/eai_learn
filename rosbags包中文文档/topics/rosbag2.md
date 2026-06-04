> 原文地址：https://ternaris.gitlab.io/rosbags/topics/rosbag2.html

# Rosbag2

`rosbags.rosbag2` 包提供了符合 rosbag2 规范的实现。它提供对保存在 rosbag2 容器中的原始消息数据的读写访问，并支持 C++ 参考实现中存在的所有功能。

## 支持的版本

支持从早期版本到当前版本（ROS2 Jazzy）版本 9 的所有版本。

## 支持的功能

Rosbag2 是一种灵活的格式，支持将不同的序列化方法、压缩格式和存储容器插接在一起使用。Rosbag2 C++ 参考实现围绕提供序列化、压缩和存储功能的插件构建。本项目实现了 C++ 参考实现中随附的所有 rosbag2 核心插件。

序列化器（Serializers）：

- cdr（不支持 wstring）

压缩器（Compressors）：

- zstd

存储（Storages）：

- sqlite3
- mcap

## 写入 rosbag2

`Writer` 类的实例可以创建并写入新的 rosbag2 文件。通常作为上下文管理器使用。在写入某个主题的第一条消息之前，必须先将该主题添加到 bag 中。以下示例展示了典型的使用模式：

```python
from rosbags.rosbag2 import Writer
from rosbags.typesys import Stores, get_typestore

# 为目标 ROS 发行版创建 typestore 并获取 string 类
typestore = get_typestore(Stores.LATEST)
String = typestore.types['std_msgs/msg/String']

# 创建 writer 实例并打开以进行写入
with Writer('/home/ros/rosbag_2020_03_24') as writer:
    # 添加新连接
    topic = '/chatter'
    msgtype = String.__msgtype__
    connection = writer.add_connection(topic, msgtype, typestore=typestore)

    # 序列化并写入消息
    timestamp = 42
    message = String('hello world')
    writer.write(connection, timestamp, typestore.serialize_cdr(message, msgtype))
```

## 读取 rosbag2

`Reader` 类的实例用于读取 rosbag2 元数据及其内容。建议将 Reader 作为上下文管理器使用。以下示例展示了典型的使用模式：

> **注意**
> 对于读取 bag 文件，你可能需要使用高级 API `AnyReader`，因为它为 ROS1 和 ROS2 的 bag 文件提供了更简单、统一的 API。

```python
from rosbags.rosbag2 import Reader
from rosbags.typesys import Stores, get_typestore

# 创建 typestore 并获取 string 类
typestore = get_typestore(Stores.LATEST)

# 创建 reader 实例并打开以进行读取
with Reader('/home/ros/rosbag_2020_03_24') as reader:
    # 主题和消息类型信息可通过 .connections 列表获取
    for connection in reader.connections:
        print(connection.topic, connection.msgtype)

    # 遍历消息
    for connection, timestamp, rawdata in reader.messages():
        if connection.topic == '/imu_raw/Imu':
            msg = typestore.deserialize_cdr(rawdata, connection.msgtype)
            print(msg.header.frame_id)

    # .messages() 方法接受连接过滤器
    connections = [x for x in reader.connections if x.topic == '/imu_raw/Imu']
    for connection, timestamp, rawdata in reader.messages(connections=connections):
        msg = typestore.deserialize_cdr(rawdata, connection.msgtype)
        print(msg.header.frame_id)
```

---

[← Rosbag1](rosbag1.md) | [序列化/反序列化 →](serde.md)
