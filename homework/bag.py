from pathlib import Path

from rosbags.highlevel import AnyReader

# 项目根目录（homework/ 的上一级）
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# bag 文件路径（请替换为自己的数据文件）
bag_path = PROJECT_ROOT / "2026-08-07-08-55-59.bag"

with AnyReader([bag_path]) as reader:
    # for conn in reader.connections:
    #     print(conn)
    # exit

    wantConnsStr = ["/robot/joint_states"]

    conns = [
        conn
        for conn in reader.connections
        if conn.topic in wantConnsStr
    ]
    for conn, log_time, rawdata in reader.messages(connections=conns):
        data = reader.deserialize(rawdata, conn.msgtype)
        print(conn.topic)
        print(conn.msgtype)
        print(type(data))
        print(data.header.stamp)
        print(data.position[1])
        break
