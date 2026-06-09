> 原文地址：https://docs.ros.org/en/jazzy/Installation/Alternatives/Ubuntu-Development-Setup.html

# Ubuntu（源码构建）

## 系统要求

Jazzy Jalisco 当前基于 Debian 的目标平台：

- Tier 1: Ubuntu Linux - Resolute (26.04) 64位
- Tier 3: Ubuntu Linux - Noble (24.04) 64位
- Tier 3: Debian Linux - Trixie (13) 64位

详见 `REP 2000 <https://reps.openrobotics.org/rep-2000/>`_。

## 系统设置

### 设置区域（Locale）

```console
$ sudo apt update && sudo apt install locales
$ sudo locale-gen en_US en_US.UTF-8
$ sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
$ export LANG=en_US.UTF-8
```

### 启用必需的仓库

```console
$ sudo apt install software-properties-common
$ sudo add-apt-repository universe
```

添加 ROS 2 GPG 密钥：

```console
$ sudo apt update && sudo apt install curl -y
$ export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F'"' '{print $4}')
$ curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo $VERSION_CODENAME)_all.deb"
$ sudo apt install /tmp/ros2-apt-source.deb
```

### 安装开发工具

```console
$ sudo apt update && sudo apt install -y \
  python3-mypy python3-pip python3-pytest python3-pytest-cov \
  python3-pytest-mock python3-pytest-repeat python3-pytest-rerunfailures \
  python3-pytest-runner python3-pytest-timeout ros-dev-tools
```

## 构建 ROS 2

### 获取 ROS 2 代码

创建工作区并克隆所有仓库：

```console
$ mkdir -p ~/ros2_jazzy/src
$ cd ~/ros2_jazzy
$ vcs import --input https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos src
```

### 使用 rosdep 安装依赖

```console
$ sudo rosdep init
$ rosdep update
$ rosdep install --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-7.7.0 urdfdom_headers"
```

### 安装额外的 RMW 实现（可选）

ROS 2 默认使用 ``Fast DDS``，但可以在构建时或运行时替换。

### 安装 colcon mixins

```console
$ colcon mixin add default https://github.com/colcon/colcon-mixin-repository/raw/master/index.yaml
$ colcon mixin update default
```

### 构建工作区代码

如果已通过其他方式安装 ROS 2（deb 或二进制），请确保在未 source 那些安装的新环境中运行以下命令。
确保 ``.bashrc`` 中没有 ``source /opt/ros/${ROS_DISTRO}/setup.bash``。
使用 ``printenv | grep -i ROS`` 确认 ROS 2 未被 source，输出应为空。

```console
$ cd ~/ros2_jazzy/
$ colcon build --symlink-install --mixin release
```

> 注意：如果编译所有示例时遇到问题，可以使用 ``--packages-skip`` 标志跳过有问题的包。例如不想安装 OpenCV：
>
> ```console
> $ colcon build --symlink-install --packages-skip image_tools intra_process_demo
> ```

## 环境设置

```console
$ . ~/ros2_jazzy/install/local_setup.bash
```

> 注意：如果不使用 bash，请将 ``.bash`` 替换为 ``setup.sh`` 或 ``setup.zsh``。

## 尝试示例

在一个终端中运行 C++ talker，另一个终端运行 Python listener：

```console
$ . ~/ros2_jazzy/install/local_setup.bash
$ ros2 run demo_nodes_cpp talker
```

```console
$ . ~/ros2_jazzy/install/local_setup.bash
$ ros2 run demo_nodes_py listener
```

## 替代编译器

使用 gcc 以外的编译器编译 ROS 2 很简单。设置 ``CC`` 和 ``CXX`` 环境变量指向可用的 C/C++ 编译器，然后重新触发 CMake 配置。

### Clang

```console
$ sudo apt install clang
$ export CC=clang
$ export CXX=clang++
$ colcon build --cmake-force-configure
```

## 保持最新

请参阅 :doc:`维护源码检出 <../维护源码检出>` 定期刷新源码安装。

## 卸载

1. 打开新终端并不 source 工作区的 ``setup`` 文件即可。
2. 释放空间：``rm -rf ~/ros2_jazzy``

---
[返回替代方案](index.md)
