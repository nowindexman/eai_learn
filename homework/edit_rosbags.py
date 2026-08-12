from os import remove
from pathlib import Path

from typing import cast
from rosbags.rosbag2 import Reader, Writer
from rosbags.typesys import get_typestore, Stores


def remove_topic(src: Path, dst: Path, topic: list[str]) -> None:
    # 定义最后的type_store
    type_store = get_typestore(Stores.LATEST)

    # 读写地址 version=8 是一个通用版本了
    with Reader(src) as reader, Writer(dst, version=8) as writer:

        # 注册conn
        conn_map = {}
        for conn in reader.connections:
            if conn.topic in topic:
                continue
            ext = cast('ConnectionExtRosbag2', conn.ext)
            conn_map[conn.id] = writer.add_connection(
                topic=conn.topic,
                msgtype=conn.msgtype,
                typestore=type_store,
                msgdef=conn.msgdef,
                serialization_format=ext.serialization_format,
                offered_qos_profiles=ext.offered_qos_profiles,
            )
        # 如果是空的 直接停止返回
        if conn_map:
            print("No topics to copy, exiting")
            return

        # 写消息
        for conn, log_time, rawdata in reader.messages(conn_map.values()):
            writer.write(conn, log_time, rawdata)


if __name__ == '__main__':
    remove_topic(
        src=Path('/Users/zhangyawen/Documents/www/zyw/python/eai_learn/标准网上下载.mcap'),
        dst=Path('./数据采集样本1'),
        topic=['/right_camera/image/compressed', '/left_camera/image/compressed'],
    )
