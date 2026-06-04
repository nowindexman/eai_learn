> 原文地址：https://ternaris.gitlab.io/rosbags/topics/serde.html

# Serde

`rosbags.serde` 包提供了一个健壮的序列化与反序列化子系统，提供了专为转换原始消息格式而量身定制的代码生成器。该库支持两种主要的消息格式：

- **Common Data Representation (CDR)**：此序列化格式被大多数 ROS2 中间件广泛使用。有关 CDR 的更多信息请参见[此处](https://www.omg.org/spec/DDS-XTypes/)。
- **ROS1**：此序列化格式专用于 ROS1 技术栈。有关 ROS1 序列化的更多细节请参见[此处](https://wiki.ros.org/ROS/Technical%20Summary)。

对于每种支持的格式，该库集成了代码生成器，它们利用由 `rosbags.typesys` 生成的内部类型描述。这些代码生成器编译生成用于以下目的的函数：

- **大小估算（Size Estimation）**：此功能用于测量序列化 Python 消息对象所需的内存分配量。
- **序列化（Serialization）**：将 Python 消息对象转换为原始字节流，确保高效的数据传输。
- **反序列化（Deserialization）**：将原始字节流转换回 Python 消息对象，实现无缝的数据解释。

此外，serde 模块还提供了在 CDR 和 ROS1 字节流之间直接转换的函数生成能力。这消除了中间反序列化和重新序列化的需要，从而提高了效率。

## 消费字节流

在每一种 rosbag 文件格式中，每条原始消息的大小都是预先确定的。在反序列化原始字节流时，`serde` 模块假设所有消息字节应该被生成的反序列化器完全消费。任何剩余的字节都表明可能存在问题，例如消息类型不正确或版本不匹配，serde 会因此抛出异常。

值得注意的是，serde 在处理 Common Data Representation (CDR) 格式的消息时会进行特殊处理。某些 DDS（Data Distribution Service，数据分发服务）实现可能会在原始消息末尾追加最多三个填充字节，`serde` 会自动处理这些额外的填充字节，确保正确的消费。

---

[← Rosbag2](rosbag2.md) | [格式转换 →](convert.md)
