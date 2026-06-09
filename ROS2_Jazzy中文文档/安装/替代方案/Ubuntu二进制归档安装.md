> 原文地址：https://docs.ros.org/en/jazzy/Installation/Alternatives/Ubuntu-Install-Binary.html

# Ubuntu 二进制归档安装

本页介绍如何在 Ubuntu Linux 上通过预构建的二进制包安装 ROS 2。

> **注意**：预构建二进制包不包含所有 ROS 2 包。包含 [ROS base variant](https://reps.openrobotics.org/rep-2001/#ros-base) 中的所有包，以及 [ROS desktop variant](https://reps.openrobotics.org/rep-2001/#desktop-variants) 中的部分包。也有 [deb 包](../Ubuntu-deb包安装.md) 可用。

## 系统要求

目前支持 Ubuntu Noble（24.04）64 位 x86 和 64 位 ARM。

## 系统设置

### 设置 locale

确保有支持 `UTF-8` 的 locale：

```bash
locale  # 检查 UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # 验证设置
```

### 启用必要的仓库

首先确保启用了 [Ubuntu Universe 仓库](https://help.ubuntu.com/community/Repositories/Ubuntu)：

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

安装 ros-apt-source 包：

```bash
sudo apt update && sudo apt install curl -y
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F'"' '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb
```

### 安装前置条件

```bash
sudo apt install tar bzip2 wget -y
```

### 安装开发工具（可选）

```bash
sudo apt update && sudo apt install ros-dev-tools
```

## 安装 ROS 2

- 前往 [发布页面](https://github.com/ros2/ros2/releases)
- 下载最新的 Ubuntu 包，假设下载到了 `~/Downloads/ros2-package-linux-x86_64.tar.bz2`
- 解压：

```bash
mkdir -p ~/ros2_jazzy
cd ~/ros2_jazzy
tar xf ~/Downloads/ros2-package-linux-x86_64.tar.bz2
```

### 使用 rosdep 安装依赖

```bash
sudo apt upgrade
sudo apt update
sudo apt install -y python3-rosdep
sudo rosdep init
rosdep update
rosdep install --from-paths ~/ros2_jazzy/ros2-linux/share --ignore-src -y --skip-keys "cyclonedds fastcdr fastrtps iceoryx_binding_c rmw_connextdds rti-connext-dds-6.0.1 urdfdom_headers"
```

## 设置环境

```bash
. ~/ros2_jazzy/ros2-linux/setup.bash
```

> 如果不是使用 bash，将 `.bash` 替换为你的 shell：`setup.bash`、`setup.sh`、`setup.zsh`。

## 测试示例

终端 1：

```bash
. ~/ros2_jazzy/ros2-linux/setup.bash
ros2 run demo_nodes_cpp talker
```

终端 2：

```bash
. ~/ros2_jazzy/ros2-linux/setup.bash
ros2 run demo_nodes_py listener
```

## 卸载

```bash
rm -rf ~/ros2_jazzy
```

---
[返回安装](index.md)
