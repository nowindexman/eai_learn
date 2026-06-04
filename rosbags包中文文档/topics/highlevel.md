# 高级接口

> 原文地址：https://ternaris.gitlab.io/rosbags/topics/highlevel.html

`rosbags.highlevel` 包提供了多种类，将 ROS 类型系统、序列化和消息访问的复杂性抽象为简单易用的统一接口。

## 一体化读取器

`AnyReader` 类的实例可以对一组 ROS1 或 ROS2 bag 文件提供统一的读取访问（但不能混合读取 ROS1 和 ROS2 文件），并按照正确的时间戳顺序回放消息，就像这些消息来自同一个 bag 文件一样。

该读取器还直接暴露了相应的反序列化方法，并会自动将所有消息类型定义注册到其内部的空白类型存储（type store）中。

```python
from pathlib import Path
from rosbags.highlevel import AnyReader

# 创建读取器实例并打开文件
with AnyReader([Path('/home/ros/rosbag_2024_01_26')]) as reader:
    connections = [x for x in reader.connections if x.topic == '/imu_raw/Imu']
    for connection, timestamp, rawdata in reader.messages(connections=connections):
        msg = reader.deserialize(rawdata, connection.msgtype)
        print(msg.header.frame_id)
```

对于缺少消息定义的旧版 ROS2 bag 文件，需要手动创建并提供一个类型存储（typestore）。

```python
from pathlib import Path
from rosbags.highlevel import AnyReader
from rosbags.typesys import Stores, get_typestore

# 为缺少消息定义的旧版 ROS2 bag 显式创建类型存储
typestore = get_typestore(Stores.ROS2_FOXY)

# 创建读取器实例并打开文件
with AnyReader([Path('/home/ros/rosbag_2020_03_24')], default_typestore=typestore) as reader:
    connections = [x for x in reader.connections if x.topic == '/imu_raw/Imu']
    for connection, timestamp, rawdata in reader.messages(connections=connections):
        msg = reader.deserialize(rawdata, connection.msgtype)
        print(msg.header.frame_id)
```

---

[← 首页](../index.md) | [类型系统 →](typesys.md)
