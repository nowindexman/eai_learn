> 原文地址：https://ternaris.gitlab.io/rosbags/topics/convert.html

`rosbags.convert` 包提供了一个 CLI 工具，用于在旧版 rosbag1 文件和 rosbag2 文件之间进行相互转换。

## 特性

- 速度较快，因为它将原始 ROS1 消息直接转换为原始 CDR 消息，无需经过反序列化和序列化过程
- 尝试将 ROS1 消息类型名称与已注册的 ROS2 类型进行匹配
- 自动为转换注册旧版 rosbag 文件中出现的未知消息类型
- 处理两个 ROS 版本之间 `std_msgs/msg/Header` 的差异

## 限制

- 拒绝转换未索引的 rosbag1 文件，请在转换前重新索引文件
- 当前不支持处理分片 bag（split bags）
- 从 rosbag2 转换为 rosbag1 时，仅支持 ROS2 默认消息类型

## 用法

```bash
# 转换 "foo.bag"，结果将为 "foo/"
$ rosbags-convert foo.bag

# 转换 "bar"，结果将为 "bar.bag"
$ rosbags-convert bar

# 转换 "foo.bag"，将结果保存为 "bar"
$ rosbags-convert foo.bag --dst /path/to/bar

# 转换 "bar"，将结果保存为 "foo.bag"
$ rosbags-convert bar --dst /path/to/foo.bag
```

[← 序列化/反序列化](serde.md) | [示例 →](../examples/使用自定义%20Typestore%20进行转换.md)
