> 原文地址：https://docs.ros.org/en/jazzy/Installation/Alternatives/Ubuntu-Development-Setup-Pixi.html

# Ubuntu（使用 Pixi 源码构建）

## 系统要求

Jazzy Jalisco 当前基于 Debian 的目标平台：

- Tier 1: Ubuntu Linux - Resolute (26.04) 64位
- Tier 3: Ubuntu Linux - Noble (24.04) 64位
- Tier 3: Debian Linux - Trixie (13) 64位

## 系统设置

### 设置区域（Locale）

```console
$ sudo apt update && sudo apt install locales
$ sudo locale-gen en_US en_US.UTF-8
$ sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
$ export LANG=en_US.UTF-8
```

### 创建 ROS 2 安装位置

```console
$ mkdir ~/ros_ws_pixi
```

## 安装前置条件

### 安装 pixi

ROS 2 使用 `conda-forge <https://conda-forge.org/>`__ 作为包后端，`pixi <https://pixi.sh/latest/>`__ 作为前端。

使用 https://pixi.sh/latest/ 上的说明安装 ``pixi``。安装后关闭终端并重新启动。

### 安装依赖

下载 pixi 配置文件：

```console
$ cd ~/ros_ws_pixi
$ wget https://raw.githubusercontent.com/ros2/ros2/jazzy/pixi.toml -O pixi.toml
```

安装依赖：

```console
$ pixi install
```

## 构建 ROS 2

### 配置 pixi 环境

每个终端都需要配置：

```console
$ cd ~/ros_ws_pixi
$ pixi shell
```

### 获取 ROS 2 代码

```console
$ mkdir ~/ros_ws_pixi/src
$ cd ~/ros_ws_pixi
$ vcs import --input https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos src
```

### 构建工作区代码

```console
$ colcon build --merge-install --event-handlers console_direct+ --cmake-args -D LTTNGPY_DISABLED=1 --packages-skip qt_gui_cpp --packages-skip-by-dep qt_gui_cpp --packages-skip-build-finished
```

> 注意：源码安装可能需要较长时间。

## 环境设置

启动新终端：

```console
$ cd ~/ros_ws_pixi
$ pixi shell
$ source ~/ros_ws_pixi/install/local_setup.bash
```

## 尝试示例

```console
$ source ~/ros_ws_pixi/install/local_setup.bash
$ ros2 run demo_nodes_cpp talker
```

```console
$ source ~/ros_ws_pixi/install/local_setup.bash
$ ros2 run demo_nodes_py listener
```

> 注意：不建议在已 source ``local_setup.bash`` 的终端中构建。

## 卸载

1. 打开新终端并不 source 工作区的 ``setup`` 文件即可。
2. 释放空间：``rm -rf ~/ros_ws_pixi``

---
[返回替代方案](index.md)
