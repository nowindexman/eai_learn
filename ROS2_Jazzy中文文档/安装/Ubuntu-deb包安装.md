> 原文地址：https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html

# Ubuntu deb 包安装

ROS 2 Jazzy Jalisco 的 deb 包目前可用于 Ubuntu Noble (24.04)。目标平台定义在 [REP 2000](https://reps.openrobotics.org/rep-2000/) 中。

## 资源

- **状态页面**：[amd64](http://repo.ros2.org/status_page/ros_jazzy_default.html)、[arm64](http://repo.ros2.org/status_page/ros_jazzy_unv8.html)
- [Jenkins 实例](http://build.ros2.org/)
- [软件仓库](http://repo.ros2.org/)

## 系统配置

### 设置区域（locale）

确保您有一个支持 `UTF-8` 的区域设置。如果您在一个最小化环境中（如 Docker 容器），区域设置可能是最小的 `POSIX`。我们使用以下设置进行测试。不过，如果您使用其他支持 UTF-8 的区域设置，也应该没问题。

```bash
locale  # 检查 UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # 验证设置
```

### 启用所需的软件仓库

您需要将 ROS 2 的 apt 仓库添加到系统中。

首先确保已启用 [Ubuntu Universe 仓库](https://help.ubuntu.com/community/Repositories/Ubuntu)。

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

[ros-apt-source](https://github.com/ros-infrastructure/ros-apt-source/) 包为各种 ROS 仓库提供密钥和 apt 源配置。

安装 ros2-apt-source 包将为您的系统配置 ROS 2 仓库。当此包的新版本发布到 ROS 仓库时，仓库配置会自动更新。

```bash
sudo apt update && sudo apt install curl -y
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F'"' '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb
```

### 安装开发工具（可选）

如果您打算构建 ROS 软件包或进行其他开发工作，可以安装开发工具：

```bash
sudo apt update && sudo apt install ros-dev-tools
```

> **注意**：在 Ubuntu 24.04 上，您的 apt 源可能仅包含基础的 `noble` 套件。这可能会在安装 `ros-dev-tools` 时导致依赖冲突。请检查 `/etc/apt/sources.list.d/ubuntu.sources` 并确保 `Suites:` 行包含 `noble-updates` 和 `noble-backports`。

## 安装 ROS 2

配置好仓库后，更新 apt 仓库缓存。

```bash
sudo apt update
```

ROS 2 包是在频繁更新的 Ubuntu 系统上构建的。建议您在安装新包之前确保系统已是最新状态。

```bash
sudo apt upgrade
```

**桌面版安装（推荐）**：ROS、RViz、演示和教程。

```bash
sudo apt install ros-jazzy-desktop
```

**ROS-Base 安装（精简版）**：通信库、消息包、命令行工具。不包含 GUI 工具。

```bash
sudo apt install ros-jazzy-ros-base
```

### 安装额外的 RMW 实现（可选）

ROS 2 默认使用的中间件是 `Fast DDS`，但中间件（RMW）可以在运行时替换。请参阅[使用多个 RMW 的指南](../操作指南/使用多个RMW实现.md)。

## 配置环境

通过 source 以下文件来设置环境。

```bash
source /opt/ros/jazzy/setup.bash
```

> **注意**：如果您不使用 bash，请将 `.bash` 替换为您的 shell。可选值：`setup.bash`、`setup.sh`、`setup.zsh`。

## 尝试一些示例

如果您上面安装了 `ros-jazzy-desktop`，可以尝试一些示例。

在一个终端中，source 配置文件并运行 C++ `talker`：

```bash
source /opt/ros/jazzy/setup.bash
ros2 run demo_nodes_cpp talker
```

在另一个终端中，source 配置文件并运行 Python `listener`：

```bash
source /opt/ros/jazzy/setup.bash
ros2 run demo_nodes_py listener
```

您应该能看到 `talker` 正在 `Publishing`（发布）消息，而 `listener` 正在说 `I heard`（我听到了）这些消息。这验证了 C++ 和 Python API 都能正常工作。太棒了！

## 后续步骤

继续[教程和演示](../教程/index.md)来配置您的环境、创建自己的工作区和软件包，并学习 ROS 2 的核心概念。

## 故障排除

故障排除技术可以在[这里](../操作指南/安装故障排除.md)找到。

## 卸载

如果您需要卸载 ROS 2 或从二进制安装切换到源码安装，请运行以下命令：

```bash
sudo apt remove '~nros-jazzy-*' && sudo apt autoremove
```

您可能还想移除仓库：

```bash
sudo apt remove ros2-apt-source
sudo apt update
sudo apt autoremove
sudo apt upgrade  # 考虑升级之前被遮蔽的包
```

---

[返回安装概览](index.md)
