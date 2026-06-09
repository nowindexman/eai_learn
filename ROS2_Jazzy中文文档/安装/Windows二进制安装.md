> 原文地址：https://docs.ros.org/en/jazzy/Installation/Windows-Install-Binary.html

# Windows（二进制安装）

本页面介绍如何从预构建的二进制包在 Windows 上安装 ROS 2。

> 注意：预构建的二进制包不包含所有 ROS 2 包。包含 `ROS base 变体 <https://reps.openrobotics.org/rep-2001/#ros-base>`_ 中的所有包，但仅包含 `ROS desktop 变体 <https://reps.openrobotics.org/rep-2001/#desktop-variants>`_ 中的部分包。

## 系统要求

仅支持 Windows 11。

## 创建 ROS 2 安装位置

此位置将包含已安装的二进制包以及 ROS 2 安装本身。

启动命令提示符会话（通常在开始菜单中搜索 ``Command Prompt``）。

创建一个目录来存储安装。由于 Windows 路径长度限制，路径应尽可能短。使用 ``C:\dev``：

```console
$ md C:\dev
```

## 安装前置条件

ROS 2 使用 `conda-forge <https://conda-forge.org/>`__ 作为包后端，`pixi <https://pixi.sh/latest/>`__ 作为前端。

> 注意：安装 conda-forge 可能会触发 Windows Defender 将其视为威胁，但可以通过点击"更多信息"和"仍然运行"安全忽略。

### 安装 pixi

使用 https://pixi.sh/latest/ 上的说明安装 ``pixi``。安装完成后，关闭命令提示符并重新启动，确保 ``pixi`` 在 PATH 中。

## 安装 ROS 2

* 下载最新的 Windows 包，例如 ``ros2-package-windows-AMD64.zip``。
* 将 zip 文件解压到系统上（假设为 ``C:\dev\``）。
* 将解压后的文件夹重命名以匹配发行版（假设为 ``C:\dev\jazzy``）。

### 安装 Pixi 依赖

进入解压 ROS 2 预发布二进制文件的文件夹并安装依赖：

```console
$ cd C:\dev\jazzy
$ pixi install
```

### 运行预安装脚本

运行预安装设置脚本，确保压缩文件能在 ROS 2 二进制文件解压到的当前文件夹中运行：

```console
$ pixi run python preinstall_setup_windows.py
```

### 安装额外的 RMW 实现（可选）

ROS 2 默认使用 ``Fast DDS``，但可以在运行时替换 RMW。

### 安装 Visual Studio Build Tools 2022（可选）

要编译 C++ 包，需要安装 Visual Studio Build Tools 2022。安装时选择"C++ 桌面开发"工作负载，确保 MSVC 编译器和 Windows SDK 可用。

在"VS 2022 的 x64 原生工具命令提示符"中运行所有命令，这会配置所需的构建环境。

> 注意：不需要完整的 Visual Studio IDE。

## 环境设置

### 配置环境

在打开的每个命令提示符中，配置 pixi 环境和 ROS 2 环境：

```console
$ cd C:\dev\jazzy
$ pixi shell
$ call C:\dev\jazzy\local_setup.bat
```

如果没有安装 RTI Connext DDS，收到缺少它的警告是正常的。

## 尝试示例

在命令提示符中，按上述设置 ROS 2 环境，然后运行 C++ ``talker``：

```console
$ ros2 run demo_nodes_cpp talker
```

启动另一个命令提示符，运行 Python ``listener``：

```console
$ ros2 run demo_nodes_py listener
```

应该能看到 ``talker`` 在 ``Publishing`` 消息，``listener`` 在 ``I heard`` 这些消息。

## 下一步

继续阅读 :doc:`教程和演示 <../教程/index>` 来配置环境、创建工作区和包。

## 卸载

1. 如果按照上述说明使用 colcon 安装了工作区，"卸载"只需打开新终端并不 source 工作区的 ``setup`` 文件即可。

2. 如果要释放空间，可以删除整个工作区目录：

```console
$ rmdir /s /q C:\dev\jazzy
```

---
[返回安装首页](index.md)
