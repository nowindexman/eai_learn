> 原文地址：https://docs.ros.org/en/jazzy/The-ROS2-Project/Contributing/Windows-Tips-and-Tricks.html

# Windows 技巧和窍门

在 Windows 上开发 ROS 2 时的一些实用技巧和窍门。

## 开发环境

### Visual Studio

- 安装 Visual Studio 2019 或更高版本
- 确保安装"C++ 桌面开发"工作负载
- 安装 Windows SDK

### 常用工具

- **Git for Windows** — Git 版本控制
- **CMake** — 构建系统
- **Python** — 从 python.org 安装或使用 Chocolatey

## 常见问题

### 路径长度限制

Windows 默认有 260 个字符的路径长度限制。可以通过以下方式解决：
- 在注册表中启用长路径支持
- 使用较短的工作区路径（如 `C:\dev\ros2`）

### 权限问题

- 某些操作可能需要以管理员身份运行命令提示符
- 确保开发目录具有适当的读写权限

### 构建问题

- 确保所有依赖项已正确安装
- 使用 `vcs import` 导入源码时使用最新版本的 vcstool
- 检查环境变量是否正确设置

## 推荐的开发工作流

1. 使用 Windows Terminal 作为终端
2. 在 PowerShell 或 CMD 中 source setup 文件
3. 使用 VSCode 作为编辑器，安装 C/C++ 和 Python 扩展

---

[返回贡献](../贡献.md)
