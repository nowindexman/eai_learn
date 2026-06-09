> 原文地址：https://docs.ros.org/en/jazzy/Installation/RHEL-Install-RPMs.html

# RHEL（RPM 包安装）

ROS 2 Jazzy Jalisco 的 RPM 包目前可用于 RHEL 10。
Rolling Ridley 发行版会随着新平台被选定而不时更改目标平台。
目标平台在 `REP 2000 <https://reps.openrobotics.org/rep-2000/>`__ 中定义。
大多数人会希望使用稳定的 ROS 发行版。

## 资源

- 状态页面：
  - ROS 2 Jazzy (RHEL 10)：`amd64 <http://repo.ros2.org/status_page/ros_jazzy_rhel.html>`__
- `Jenkins 实例 <http://build.ros2.org/>`__
- `仓库 <http://repo.ros2.org>`__

## 系统设置

### 设置区域（Locale）

确保系统支持 UTF-8 区域设置：

```console
$ sudo dnf install langpacks-en glibc-all-langpacks -y
$ export LANG=en_US.UTF-8
```

### 启用必需的仓库

需要启用 EPEL 和 PowerTools 仓库：

```console
$ sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-$(rpm -E %rhel).noarch.rpm
$ sudo env FORCE_DNF=1 crb enable
```

> 注意：此步骤可能因使用的发行版略有不同。请参阅 `EPEL 文档 <https://docs.fedoraproject.org/en-US/epel/getting-started/>`_。

接下来，下载 ``ros2-release`` 包并安装：

```console
$ sudo dnf install curl
$ export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F'"' '{print $4}')
$ sudo dnf install "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-release-${ROS_APT_SOURCE_VERSION}-1.noarch.rpm"
```

`ros2-release <https://github.com/ros-infrastructure/ros-apt-source/>`_ 包提供了各个 ROS 仓库的密钥和仓库配置。当新版本发布到 ROS 仓库时，仓库配置会自动更新。

### 安装开发工具（可选）

如果要构建 ROS 包或进行其他开发，可以安装开发工具：

```console
$ sudo dnf install -y \
  cmake \
  gcc-c++ \
  git \
  make \
  patch \
  python3-colcon-common-extensions \
  python3-mypy \
  python3-pip \
  python3-pytest \
  python3-pytest-repeat \
  python3-pytest-rerunfailures \
  python3-rosdep \
  python3-setuptools \
  python3-vcstool \
  wget
```

## 安装 ROS 2

桌面安装（推荐）：包含 ROS、RViz、演示和教程。

```console
$ sudo dnf install ros-jazzy-desktop
```

ROS-Base 安装（精简版）：通信库、消息包、命令行工具，无 GUI 工具。

```console
$ sudo dnf install ros-jazzy-ros-base
```

### 安装额外的 RMW 实现（可选）

ROS 2 默认使用 ``Fast DDS`` 作为中间件，但可以在运行时替换 RMW 实现。
请参阅 :doc:`使用多个 RMW 实现指南 <../操作指南/使用多个RMW实现>`。

## 环境设置

通过 source 以下文件来设置环境：

```console
$ source /opt/ros/jazzy/setup.bash
```

> 注意：如果不使用 bash，请将 ``.bash`` 替换为对应的 shell。可选值：``setup.bash``、``setup.sh``、``setup.zsh``。

## 尝试示例

如果安装了 ``ros-jazzy-desktop``，可以尝试一些示例。

在一个终端中，source 设置文件然后运行 C++ ``talker``：

```console
$ source /opt/ros/jazzy/setup.bash
$ ros2 run demo_nodes_cpp talker
```

在另一个终端中，source 设置文件然后运行 Python ``listener``：

```console
$ source /opt/ros/jazzy/setup.bash
$ ros2 run demo_nodes_py listener
```

应该能看到 ``talker`` 在 ``Publishing`` 消息，``listener`` 在 ``I heard`` 这些消息。
这验证了 C++ 和 Python API 都能正常工作。

## 下一步

继续阅读 :doc:`教程和演示 <../教程/index>` 来配置环境、创建工作区和包，以及学习 ROS 2 核心概念。

## 故障排除

故障排除技术可以在 :doc:`这里 <../操作指南/安装故障排除>` 找到。

## 卸载

如果需要卸载 ROS 2 或从二进制安装切换到源码安装：

```console
$ sudo dnf remove ros-jazzy-*
```

移除仓库配置：

```console
$ sudo dnf remove ros2-release
```

---
[返回安装首页](index.md)
