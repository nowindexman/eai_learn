> 原文地址：https://ternaris.gitlab.io/rosbags/examples/convert_custom_typestore.html

# 使用自定义 Typestore 进行转换

在转换 ROS bag 文件时，转换器需要访问所有相关的消息定义。如果源 bag 文件包含所有必要的定义，则无需进一步操作，转换器会自动检测并使用它们。但如果缺少某些定义，则必须通过 **typestore** 来提供。

## 创建 Typestore 模块

`rosbags-convert` 工具支持从 Python 模块加载 typestore。创建合适 typestore 的最简单方式是基于现有的 typestore 进行扩展，添加所需的额外消息类型。

```python
"""示例：创建自定义 Typestore。

本模块定义了一个全局变量 ``nmea_typestore``，它通过添加一个额外的消息类型
来扩展默认的 Jazzy typestore。

如果此文件保存为 ``my_typestores.py``，则 typestore 的完全限定引用为
``my_typestores:nmea_typestore``。

"""

from __future__ import annotations

from rosbags.typesys import Stores, get_typestore
from rosbags.typesys.msg import get_types_from_msg

NMEA_SENTENCE_MSG = """
std_msgs/msg/Header header
string sentence
"""

nmea_typestore = get_typestore(Stores.ROS2_JAZZY)
nmea_typestore.register(get_types_from_msg(NMEA_SENTENCE_MSG, 'nmea_msgs/msg/Sentence'))
```

## 使用 Typestore 进行转换

要在转换过程中使用自定义 typestore，请通过 `--src-typestore-ref` 选项将其传递给 rosbags-convert。

```
rosbags-convert \
  --src-typestore-ref my_typestores:nmea_typestore \
  --src rosbag_without_types \
  --dst rosbag_with_types
```

> **注意**
>
> 请确保 Python 能够定位到你的 typestore 模块。如果遇到 `ModuleNotFoundError`，请验证包含 typestore 的目录是否已添加到 `PYTHONPATH` 环境变量中。

---

[← 格式转换](../topics/convert.md) | [编辑消息定义 →](编辑消息定义.md)
