from os import remove
from pathlib import Path

from typing import cast
from rosbags.rosbag2 import Reader, Writer, StoragePlugin
from rosbags.typesys import get_typestore, Stores, get_types_from_msg
import json


def remove_topic(src: Path, dst: Path, topic: list[str]) -> None:
    # 定义最后的type_store
    type_store = get_typestore(Stores.LATEST)

    # 读写地址 version=8 是一个通用版本了
    with Reader(src) as reader, Writer(dst, version=8, storage_plugin=StoragePlugin.MCAP) as writer:

        # 注册conn
        conn_map = {}
        for conn in reader.connections:
            # 如果 msgtype 不在 type_store 中 则注册！！！
            # 如果 msgtype 不在 type_store 中 则注册！！！
            # 如果 msgtype 不在 type_store 中 则注册！！！
            if conn.msgtype not in type_store.types:
                msgdef_text = conn.msgdef[1]
                type_store.register(get_types_from_msg(msgdef_text, conn.msgtype))
                # 打印下结果 可注释
                print(json.dumps(conn._asdict(), default=str, indent=2, ensure_ascii=False))

            if conn.topic in topic:
                continue
            ext = cast('ConnectionExtRosbag2', conn.ext)
            conn_map[conn.id] = writer.add_connection(
                topic=conn.topic,
                msgtype=conn.msgtype,
                # typestore 和 msgdef 是互斥的 不能同时使用
                typestore=type_store,
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
    # 项目根目录（homework/ 的上一级）
    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    remove_topic(
        src=PROJECT_ROOT / '标准网上下载.mcap',
        dst=PROJECT_ROOT / '数据采集样本3',
        topic=['/right_camera/image/compressed', '/left_camera/image/compressed'],
    )
