> 原文地址：https://ternaris.gitlab.io/rosbags/index.html

# Rosbags

![pipeline status](https://gitlab.com/ternaris/rosbags/badges/master/pipeline.svg)
![coverage report](https://gitlab.com/ternaris/rosbags/badges/master/coverage.svg)
![python versions](https://img.shields.io/pypi/pyversions/rosbags)
![PyPI - Downloads](https://img.shields.io/pypi/dm/rosbags)

Rosbags 是一个 **纯 Python** 库，用于处理一切与 rosbag 相关的操作。它包含：

- **highlevel** — 易用的高层接口，
- **rosbag2** — 读写器，
- **rosbag1** — 读写器，
- **可扩展的** 类型系统，支持序列化器（serializers）和反序列化器（deserializers），
- **高效的** rosbag1 与 rosbag2 之间的转换器，
- 以及更多功能。

Rosbags 不依赖任何 ROS 软件栈，可以独立使用，也可以与 ROS1 或 ROS2 配合使用。

Rosbags 最初是为 MARV 开发的，MARV 需要一个快速、正确且灵活的库来读取、操作和写入各种 rosbag 文件格式。

## 快速入门

Rosbags 已发布在 PyPI 上，没有特殊的依赖项。使用 pip 即可安装：

```bash
pip install rosbags
```

从 rosbag1 或 rosbag2 文件中读取并反序列化消息：

```python
from pathlib import Path

from rosbags.highlevel import AnyReader
from rosbags.typesys import Stores, get_typestore

bagpath = Path('/home/ros/rosbag_2020_03_24')

# 如果 bag 文件没有消息定义，则创建一个类型存储（type store）
typestore = get_typestore(Stores.ROS2_FOXY)

# 创建读取器实例并打开文件
with AnyReader([bagpath], default_typestore=typestore) as reader:
    connections = [x for x in reader.connections if x.topic == '/imu_raw/Imu']
    for connection, timestamp, rawdata in reader.messages(connections=connections):
         msg = reader.deserialize(rawdata, connection.msgtype)
         print(msg.header.frame_id)
```

在不同版本的 rosbag 之间进行转换：

```bash
# 转换 "foo.bag"，结果将保存为 "foo/"
rosbags-convert foo.bag

# 转换 "bar"，结果将保存为 "bar.bag"
rosbags-convert bar

# 转换 "foo.bag"，将结果保存为 "bar"
rosbags-convert foo.bag --dst /path/to/bar

# 转换 "bar"，将结果保存为 "foo.bag"
rosbags-convert bar --dst /path/to/foo.bag
```

## 参与贡献

感谢您考虑为 rosbags 做出贡献。

如需提交 issue 或创建 merge request，请按照贡献指南中提供的说明操作。

为 rosbags 贡献代码即表示您接受并同意其中列出的条款和条件。

## 开发

克隆仓库并配置本地环境：

```bash
git clone https://gitlab.com/ternaris/rosbags.git

cd rosbags
uv sync
```

这将创建一个新的虚拟环境，安装所需的 Python 依赖，并以可编辑模式安装 rosbags。rosbags 代码库使用 pytest 作为测试运行器，只需执行以下命令即可运行测试套件：

```bash
uv run pytest
```

要从源码构建文档，请运行 sphinx-build：

```bash
uv run sphinx-build -a docs public
```

本地构建的文档入口文件应位于 `public/index.html`。

## 支持

Ternaris 提供专业的商业支持服务。

---

[下一页：Highlevel APIs](topics/highlevel.md)
