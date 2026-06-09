> 原文地址：https://docs.ros.org/en/jazzy/Installation/Alternatives/RHEL-Install-Binary.html

# RHEL（二进制归档安装）

本页面介绍如何从预构建的二进制包在 RHEL 上安装 ROS 2。

> 注意：预构建的二进制包不包含所有 ROS 2 包。包含 ROS base 变体中的所有包，但仅包含 ROS desktop 变体中的部分包。

也可使用 :doc:`RPM 包安装 <../RHEL-RPM包安装>`。

## 系统要求

目前支持 RHEL 10 64位。

## 系统设置

### 设置区域（Locale）

```console
$ sudo dnf install langpacks-en glibc-all-langpacks -y
$ export LANG=en_US.UTF-8
```

### 启用必需的仓库

```console
$ sudo dnf install 'dnf-command(config-manager)' epel-release -y
$ sudo dnf config-manager --set-enabled crb
```

### 安装前置条件

```console
$ sudo dnf install tar bzip2 wget -y
```

### 安装开发工具（可选）

```console
$ sudo dnf install -y \
  cmake gcc-c++ git make patch \
  python3-colcon-common-extensions python3-mypy python3-pip \
  python3-pytest python3-pytest-repeat python3-pytest-rerunfailures \
  python3-rosdep python3-setuptools python3-vcstool wget
```

## 安装 ROS 2

* 下载 RHEL 的最新包，假设路径为 ``~/Downloads/ros2-package-linux-x86_64.tar.bz2``。

* 解压：

```console
$ mkdir -p ~/ros2_jazzy
$ cd ~/ros2_jazzy
$ tar xf ~/Downloads/ros2-package-linux-x86_64.tar.bz2
```

### 使用 rosdep 安装依赖

```console
$ sudo rosdep init
$ rosdep update
$ rosdep install --from-paths ~/ros2_jazzy/ros2-linux/share --ignore-src -y --skip-keys "cyclonedds fastcdr fastdds iceoryx_binding_c rti-connext-dds-7.7.0 urdfdom_headers"
```

### 安装额外的 RMW 实现（可选）

ROS 2 默认使用 ``Fast DDS``，但可以在运行时替换 RMW。

## 环境设置

```console
$ . ~/ros2_jazzy/ros2-linux/setup.bash
```

> 注意：如果不使用 bash，请将 ``.bash`` 替换为 ``setup.sh`` 或 ``setup.zsh``。

## 尝试示例

在一个终端中运行 C++ talker：

```console
$ . ~/ros2_jazzy/ros2-linux/setup.bash
$ ros2 run demo_nodes_cpp talker
```

在另一个终端中运行 Python listener：

```console
$ . ~/ros2_jazzy/ros2-linux/setup.bash
$ ros2 run demo_nodes_py listener
```

## 下一步

继续阅读 :doc:`教程和演示 <../../教程/index>` 来配置环境、创建工作区和包。

## 卸载

1. 打开新终端并不 source 工作区的 ``setup`` 文件即可"卸载"。

2. 释放空间：

```console
$ rm -rf ~/ros2_jazzy
```

---
[返回替代方案](index.md)
