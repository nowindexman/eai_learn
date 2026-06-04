> 原文地址：https://ternaris.gitlab.io/rosbags/topics/typesys.html

# 类型系统 (Type System)

Rosbags 包含了自己的纯 Python 类型系统，可通过 `rosbags.typesys` 访问。在内部，它使用解析树（parse trees）来表示消息定义。它内置了 `.idl` 和 `.msg` 定义文件的解析器，能够将消息定义文件转换为内部格式。此外，它还提供了类型存储（type stores）来管理相关类型的集合。Typesys 支持在运行时动态添加自定义消息类型，无需额外的构建步骤。

## 类型存储 (Type Stores)

在 ROS1 和 ROS2 中，消息类型会随着时间推移发生变化，包括新增、修改或删除。这意味着使用某个 ROS1 或 ROS2 发行版创建的 bag 文件可能无法与另一个发行版兼容。为了解决这个问题，rosbags 开箱即带了多个类型存储，确保与当前及之前的 ROS1 和 ROS2 发行版的兼容性。

类型存储具有以下关键功能：

- 作为消息定义的仓库
- 注册新消息并使用 `rosbags.serde` 模块自动生成高效的序列化/反序列化函数
- 处理消息的序列化和反序列化
- 为读取器和写入器提供支持，包括消息定义哈希等功能

## 获取存储句柄

要获取类型存储实例，typesys 模块提供了 `get_typestore()` 函数，使用方式如下：

```python
from rosbags.typesys import Stores, get_typestore

typestore = get_typestore(Stores.ROS2_FOXY)
```

`Stores` 枚举用于指定所需的类型。内置的类型存储包括：

- empty
- ros1_noetic
- ros2_dashing
- ros2_eloquent
- ros2_foxy
- ros2_galactic
- ros2_humble
- ros2_iron
- ros2_jazzy
- ros2_kilted

## 反序列化 (Deserialization)

类型存储实例提供了两个反序列化函数：

- `.deserialize_cdr()` — 将 CDR 消息转换为 Python 对象
- `.deserialize_ros1()` — 将 ROS1 消息转换为 Python 对象

使用示例：

```python
from rosbags.typesys import Stores, get_typestore

typestore = get_typestore(Stores.ROS2_HUMBLE)

# 使用 CDR 格式处理 ROS2，字节序会自动处理
msg = typestore.deserialize_cdr(cdr_bytes, 'geometry_msgs/msg/Quaternion')

# 使用 ROS1 格式处理 ROS1
msg = typestore.deserialize_ros1(ros1_bytes, 'geometry_msgs/msg/Quaternion')
```

## 序列化 (Serialization)

类型存储实例提供了两个序列化函数：

- `.serialize_cdr()` — 将 Python 对象转换为 CDR 字节
- `.serialize_ros1()` — 将 Python 对象转换为 ROS1 字节

```python
from rosbags.typesys import Stores, get_typestore

typestore = get_typestore(Stores.ROS2_HUMBLE)

# 使用 CDR 格式处理 ROS2，使用系统字节序序列化消息
cdr_bytes = typestore.serialize_cdr(msg, 'geometry_msgs/msg/Quaternion')

# 使用 CDR 格式处理 ROS2，显式指定字节序
cdr_bytes = typestore.serialize_cdr(msg, 'geometry_msgs/msg/Quaternion', little_endian=False)

# 使用 ROS1 格式处理 ROS1，该格式仅支持小端序
ros1_bytes = typestore.serialize_ros1(msg, 'geometry_msgs/msg/Quaternion')
```

## 消息实例 (Message Instances)

类型系统为每个消息类型生成一个数据类（data class），允许对消息的所有可变字段进行直接读写访问。但是，修改字段时需要谨慎，因为运行时不会进行类型检查。

> **注意**
> 虽然类型系统会解析消息定义中的数组边界和/或默认值，但边界限制和默认值不会在消息实例上强制执行或赋值。

创建消息实例的示例：

```python
from rosbags.typesys import Stores, get_typestore

typestore = get_typestore(Stores.ROS2_HUMBLE)

Int32 = typestore.types['std_msgs/msg/Int32']
int32 = Int32(data=42)
```

通过 `.types` 字典访问数据类适用于内置类型和自定义类型。为了更好地集成 IDE 和语言服务器，直接导入数据类并绕过类型存储可能更合适。但是，这样做时需要谨慎，以避免混淆不同的类型存储。

```python
from rosbags.typesys.stores.ros2_humble import std_msgs__msg__Int32 as Int32

int32 = Int32(data=42)
```

## 添加自定义类型 (Adding Custom Types)

默认情况下，rosbags 仅包含 ROS 发行版的核心类型。用户通常需要在此基础上添加自己的类型。

要向存储中添加类型，需要从 `.idl` 或 `.msg` 文件中读取消息定义，并使用 `get_types_from_idl()` 或 `get_types_from_msg()` 将其转换为解析树。

由于消息之间往往存在依赖关系，必须按正确的顺序逐一注册，或者一次性全部注册。类型存储的 `.register()` 方法接受一个包含任意数量类型的解析树字典。

示例：

```python
from pathlib import Path

from rosbags.typesys import get_types_from_idl, get_types_from_msg

# 读取定义为 Python 字符串
idl_text = Path('foo_msgs/msg/Foo.idl').read_text()
msg_text = Path('bar_msgs/msg/Bar.msg').read_text()

# 用于存放消息定义的普通字典
add_types = {}

# 将一个 idl 文件中的定义添加到字典中
add_types.update(get_types_from_idl(idl_text))

# 将一个 msg 文件中的定义添加到字典中
add_types.update(get_types_from_msg(msg_text, 'bar_msgs/msg/Bar'))
```

将所有消息定义解析到 `add_types` 字典后，即可添加到类型存储中：

```python
from rosbags.typesys import Stores, get_typestore

typestore = get_typestore(Stores.ROS2_HUMBLE)
typestore.register(add_types)
```

现在类型存储可以处理自定义类型了：

```python
# 反序列化自定义消息
msg = typestore.deserialize_cdr(cdr_bytes, 'foo_msgs/msg/Foo')

# 获取自定义类型 Bar 的 Python 数据类
Bar = typestore.types['bar_msgs/msg/Bar']

# 实例化 Bar，假设它接受 x、y 和 z 参数
bar = Bar(x=1., y=2., z=3.)

# 序列化自定义消息
cdr_bytes = typestore.serialize_cdr(bar, 'bar_msgs/msg/Bar')
```

---

[← 高级接口](highlevel.md) | [Rosbag1 →](rosbag1.md)
