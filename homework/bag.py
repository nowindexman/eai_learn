from pathlib import Path

from rosbags.highlevel import AnyReader

# 引入地址
bag_path = Path("/Users/zhangyawen/Documents/www/zyw/python/eai_learn/2026-08-07-08-55-59.bag")

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
