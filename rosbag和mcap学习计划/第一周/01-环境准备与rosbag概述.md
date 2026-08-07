# 第一周：环境准备与 rosbag 概述

本周目标是**先用命令行建立正确概念**：能查看、录制、回放和简单处理 ROS bag 与 MCAP，同时分清它们的文件形态和适用边界。

---

## 环境准备：你需要安装哪些工具

你不需要完整的 ROS 开发环境，但至少需要命令行工具来操作文件。可以按以下方式准备：

- **rosbag v1 命令**：需安装 ROS 1 基础包。如果不想装完整 ROS，最简单的是用 Docker：
  ```bash
  docker run -it --rm -v "$(pwd)":/data ros:noetic-ros-base
  ```
  进入容器后，`rosbag` 命令即可用。
- **rosbag2 命令**：需要 ROS 2 环境，同样可用 Docker：
  ```bash
  docker run -it --rm -v "$(pwd)":/data ros:humble-ros-base
  ```
  之后 `ros2 bag` 命令可用。
- **MCAP Python SDK**：只需 Python 环境：
  ```bash
  python -m pip install mcap
  ```
  这安装的是 Python SDK。`mcap` CLI 需要单独安装，安装后先执行 `mcap --help` 确认版本和参数。

> 如果你的主要目的是搭建数据处理系统，MCAP 部分可以立刻在自己电脑上实操；rosbag 部分在容器里练习即可。

---

## 第一部分：rosbag 概念与命令行速通

### 1. 什么是 rosbag？

rosbag 是 ROS 生态中用来记录和回放“话题消息”的工具。它本质上是一个**日志文件**，按时间顺序存储了 ROS 计算图中流通的消息。

- **rosbag1**（ROS 1 时代）：通常是单个 `.bag` 文件，内部保存连接、索引和消息数据；解析仍需要匹配的 ROS 消息定义。
- **rosbag2**（ROS 2 时代）：通常是一个 bag URI 目录，里面有 `metadata.yaml` 和一个或多个 `.db3` 或 `.mcap` 存储文件。默认后端随 ROS 发行版变化，也可以通过插件显式指定。

示例：

```text
my_bag/
├── metadata.yaml
└── my_bag_0.db3 或 my_bag_0.mcap
```
