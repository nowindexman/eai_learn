> 原文地址：https://docs.ros.org/en/jazzy/Installation/Alternatives/RHEL-Development-Setup.html

# RHEL（源码构建）

## 系统要求

Jazzy Jalisco 当前的目标 Red Hat 平台：

- Tier 2: RHEL 10 64位

详见 `REP 2000 <https://reps.openrobotics.org/rep-2000/>`_。

## 系统设置

### 设置区域（Locale）

```console
$ sudo dnf install langpacks-en glibc-all-langpacks -y
$ export LANG=en_US.UTF-8
```

### 启用必需的仓库

**RHEL**：

```console
$ sudo dnf install 'dnf-command(config-manager)' epel-release -y
$ sudo dnf config-manager --set-enabled crb
```

**Fedora**：无需额外设置。

### 安装开发工具

```console
$ sudo dnf install -y \
  cmake gcc-c++ git make patch \
  python3-colcon-common-extensions python3-mypy python3-pip \
  python3-pytest python3-pytest-cov python3-pytest-mock \
  python3-pytest-repeat python3-pytest-rerunfailures \
  python3-pytest-runner python3-rosdep python3-setuptools \
  python3-vcstool wget
```

## 构建 ROS 2

### 获取 ROS 2 代码

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

### 构建工作区代码

如果已通过其他方式安装 ROS 2，请确保在未 source 那些安装的新环境中运行：

```console
$ cd ~/ros2_jazzy/
$ colcon build --symlink-install
```

## 环境设置

```console
$ . ~/ros2_jazzy/install/local_setup.bash
```

## 尝试示例

```console
$ . ~/ros2_jazzy/install/local_setup.bash
$ ros2 run demo_nodes_cpp talker
```

```console
$ . ~/ros2_jazzy/install/local_setup.bash
$ ros2 run demo_nodes_py listener
```

## 替代编译器

### Clang

```console
$ sudo dnf install clang
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
