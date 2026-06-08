> 原文地址：https://docs.ros.org/en/jazzy/Concepts/Advanced.html

# 高级概念

这些概念文档面向计划修改或贡献 ROS 2 核心的开发者。

## 主题列表

- **[构建系统](关于构建系统.md)** — ROS 2 使用 ament 作为其构建系统。ament 是一个元构建系统，负责协调各个包的构建过程。它支持 CMake（用于 C/C++ 包）和 Python setuptools（用于 Python 包）作为底层构建工具。

- **[内部 ROS 2 接口](关于内部接口.md)** — ROS 2 内部使用了一组标准化的接口来实现不同组件之间的通信。了解这些内部接口对于修改或扩展 ROS 2 核心功能至关重要。

- **[ROS 2 中间件实现](关于中间件实现.md)** — ROS 2 中间件（RMW）层提供了一个抽象接口，使 ROS 2 能够使用不同的 DDS 实现。每个 RMW 实现都需要将 DDS 特定的 API 映射到通用的 RMW 接口。

---

[返回概念概览](../index.md)
