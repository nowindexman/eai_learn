> 原文地址：https://docs.ros.org/en/jazzy/How-To-Guides.html

# 操作指南

操作指南针对 ROS 2 关键方面的"如何……"类问题提供直接、模块化的解答。它们包含简洁的步骤，帮助您快速完成重要任务。

操作指南适用于已有一定 ROS 2 知识、只想了解如何实现特定功能的用户。它们不会深入提供背景信息或教授某个概念如何融入整个 ROS 2 生态系统。

如果您是新手，想从头学起，请从[教程](../教程/index.md)开始，以获得更全面的 ROS 2 学习体验。

## 安装与配置

- **[安装故障排除](Installation-Troubleshooting.md)** — 安装过程中常见问题的解决方案
- **[在树莓派上安装 ROS 2](Installing-on-Raspberry-Pi.md)** — 树莓派平台的安装指南
- **[使用 VSCode 和 Docker 配置 ROS 2](Setup-ROS-2-with-VSCode-and-Docker-Container.md)** — VSCode + Docker 开发环境配置
- **[在 Docker 中运行 ROS 2 节点](Run-2-nodes-in-single-or-separate-docker-containers.md)** — Docker 容器化运行方案

## 开发与构建

- **[开发 ROS 2 软件包](Developing-a-ROS-2-Package.md)** — ROS 2 包的开发流程
- **[编写 ROS 2 软件包文档](Documenting-a-ROS-2-Package.md)** — 包文档编写指南
- **[ament_cmake 用户文档](Ament-CMake-Documentation.md)** — ament_cmake 构建系统使用
- **[ament_cmake_python 用户文档](Ament-CMake-Python-Documentation.md)** — Python 包的 ament_cmake 构建
- **[使用 Python 包与 ROS 2](Using-Python-Packages.md)** — Python 依赖管理
- **[构建自定义 deb 包](Building-a-Custom-Deb-Package.md)** — 自定义 deb 包构建
- **[交叉编译](Cross-compilation.md)** — 跨平台编译指南

## Launch 与节点

- **[使用 XML、YAML 和 Python 编写 ROS 2 Launch 文件](Launch-file-different-formats.md)** — Launch 文件的不同格式
- **[使用 ROS 2 launch 启动可组合节点](Launching-composable-nodes.md)** — Launch 系统中的节点组合
- **[通过命令行传递 ROS 参数给节点](Node-arguments.md)** — 命令行参数传递
- **[使用回调组](Using-callback-groups.md)** — 回调组配置
- **[同步与异步服务客户端](Sync-Vs-Async.md)** — 服务调用方式对比

## 通信与中间件

- **[DDS 调优信息](DDS-tuning.md)** — DDS 中间件性能调优
- **[rosbag2：覆盖 QoS 策略](Overriding-QoS-Policies-For-Recording-And-Playback.md)** — 录制和回放时的 QoS 配置
- **[使用多个 ROS 2 中间件实现](Working-with-multiple-RMW-implementations.md)** — 多 RMW 管理
- **[配置零拷贝借用消息](Configure-ZeroCopy-loaned-messages.md)** — 零拷贝通信优化
- **[使用变体（Variants）](Using-Variants.md)** — 消息变体使用

## 迁移与桥接

- **[从 ROS 1 迁移到 ROS 2](Migrating-from-ROS1.md)** — ROS 1 到 ROS 2 的迁移指南
- **[在 Ubuntu 22.04 上使用 ros1_bridge 和上游 ROS](Using-ros1_bridge-Jammy-upstream.md)** — ROS 1/2 桥接

## 工具与调试

- **[使用 ros2 param 命令行工具](Using-ros2-param.md)** — 参数管理命令行
- **[使用 Foxglove Studio 可视化 ROS 2 数据](Visualizing-ROS-2-Data-With-Foxglove-Studio.md)** — 数据可视化
- **[在 ROS 2 中获取回溯信息](Getting-Backtraces-in-ROS-2.md)** — 调试回溯
- **[IDE 和调试](ROS-2-IDEs.md)** — IDE 配置和调试
- **[使用自定义 rosdistro 版本](Using-Custom-Rosdistro.md)** — 自定义发行版配置

## 发布与维护

- **[发布软件包](Releasing/Releasing-a-Package.md)** — ROS 2 包发布流程
- **[ROS 2 核心维护者指南](Core-maintainer-guide.md)** — 核心包维护
- **[使用追踪功能构建 ROS 2](Building-ROS-2-with-Tracing.md)** — 追踪功能集成

---

[返回主页](../index.md)
