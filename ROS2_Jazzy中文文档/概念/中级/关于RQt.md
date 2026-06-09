> 原文地址：https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-RQt.html

# RQt 概述与用法

## 概述

RQt 是一个图形用户界面框架，以插件形式实现各种工具和接口。所有 GUI 工具都可以作为可停靠窗口在 RQt 内运行，也可以在独立模式下运行，但 RQt 可以更轻松地在单个屏幕布局中管理所有窗口。

运行 RQt：
```bash
rqt
```

可以通过以下命令运行独立插件（如 Python 控制台）：
```bash
ros2 run rqt_py_console rqt_py_console
```

用户可以使用 `Python` 或 `C++` 创建自己的 RQt 插件。查看可用插件：
```bash
ros2 pkg list  # 查找以 rqt_ 开头的包
```

## 安装

```bash
sudo apt install ros-{DISTRO}-rqt*
```

## RQt 组件结构

RQt 由两个元包组成：
- **rqt** — 核心基础设施模块
- **rqt_common_plugins** — 常用调试工具

## RQt 框架优势

- 标准化的 GUI 通用流程（启动-关闭钩子、状态恢复）
- 多个组件可停靠在单个窗口中
- 易于将现有 Qt 组件转为 RQt 插件
- 支持多平台和多语言（Python、C++）
- 可管理的生命周期

---
[返回中级概念](../index.md)
