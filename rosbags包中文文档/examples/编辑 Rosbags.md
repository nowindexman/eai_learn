> 原文地址：https://ternaris.gitlab.io/rosbags/examples/edit_rosbags.html

# 编辑 Rosbags

Rosbags 不支持以读写模式打开文件，而是隐式地采用**写时复制（copy-on-write）**语义。除了需要将 reader 的连接（connection）映射到 writer 的连接之外，整个过程相当直接。

## 移除话题（Remove topic）

```python
"""示例：移除话题。"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rosbags.rosbag2 import Reader, Writer
from rosbags.typesys.stores import Stores, get_typestore

if TYPE_CHECKING:
    from pathlib import Path

    from rosbags.interfaces import ConnectionExtRosbag2

def remove_topic(src: Path, dst: Path, topic: str) -> None:
    """从 rosbag2 中移除话题。

    Args:
        src: 源文件路径。
        dst: 目标文件路径。
        topic: 要移除的话题名称。

    """
    typestore = get_typestore(Stores.ROS2_FOXY)
    with Reader(src) as reader, Writer(dst) as writer:
        conn_map = {}
        for conn in reader.connections:
            if conn.topic == topic:
                continue
            ext = cast('ConnectionExtRosbag2', conn.ext)
            conn_map[conn.id] = writer.add_connection(
                conn.topic,
                conn.msgtype,
                typestore=typestore,
                serialization_format=ext.serialization_format,
                offered_qos_profiles=ext.offered_qos_profiles,
            )

        rconns = [reader.connections[x] for x in conn_map]
        for conn, timestamp, data in reader.messages(connections=rconns):
            writer.write(conn_map[conn.id], timestamp, data)
```

## 编辑时间戳（Edit timestamps）

```python
"""示例：编辑时间戳。"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rosbags.rosbag2 import Reader, Writer
from rosbags.typesys import Stores, get_typestore

if TYPE_CHECKING:
    from pathlib import Path

    from rosbags.interfaces import ConnectionExtRosbag2

def offset_timestamps(src: Path, dst: Path, offset: int) -> None:
    """偏移时间戳。

    Args:
        src: 源文件路径。
        dst: 目标文件路径。
        offset: 时间戳偏移量（纳秒）。

    """
    typestore = get_typestore(Stores.ROS2_FOXY)
    with Reader(src) as reader, Writer(dst) as writer:
        conn_map = {}
        for conn in reader.connections:
            ext = cast('ConnectionExtRosbag2', conn.ext)
            conn_map[conn.id] = writer.add_connection(
                conn.topic,
                conn.msgtype,
                typestore=typestore,
                serialization_format=ext.serialization_format,
                offered_qos_profiles=ext.offered_qos_profiles,
            )

        for conn, timestamp, data in reader.messages():
            # 同时调整 header 时间戳
            msg = typestore.deserialize_cdr(data, conn.msgtype)
            if head := getattr(msg, 'header', None):
                headstamp = head.stamp.sec * 10**9 + head.stamp.nanosec + offset
                head.stamp.sec = headstamp // 10**9
                head.stamp.nanosec = headstamp % 10**9
                outdata: memoryview | bytes = typestore.serialize_cdr(msg, conn.msgtype)
            else:
                outdata = data

            writer.write(conn_map[conn.id], timestamp + offset, outdata)
```

---

[← 编辑消息定义](编辑消息定义.md) | [注册自定义类型 →](注册自定义消息类型.md)
