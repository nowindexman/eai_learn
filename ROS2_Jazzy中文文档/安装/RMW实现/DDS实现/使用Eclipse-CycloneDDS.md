> 原文地址：https://docs.ros.org/en/jazzy/Installation/RMW-Implementations/DDS-Implementations/Working-with-Eclipse-CycloneDDS.html

# Eclipse Cyclone DDS

Eclipse Cyclone DDS 是一个非常高性能且稳健的开源 DDS 实现。Cyclone DDS 作为 Eclipse IoT 项目完全在开放环境中开发。
详见：https://projects.eclipse.org/projects/iot.cyclonedds

## 前置条件

需已安装 rosdep。

## 安装包

最简单的方式是从 ROS 2 apt 仓库安装：

```console
$ sudo apt install ros-jazzy-rmw-cyclonedds-cpp
```

## 从源码构建

首先，在 ROS 2 工作区源码目录中克隆 Cyclone DDS 和 rmw_cyclonedds。

获取正确的分支：

```console
$ CYCLONEDDS_BRANCH=$(curl -s https://raw.githubusercontent.com/ros2/ros2/refs/heads/jazzy/ros2.repos | grep -A 3 "eclipse-cyclonedds/cyclonedds:" | grep "version:" | awk '{print $2}')
```

克隆并检出代码：

```console
$ cd ros2_ws/src
$ git clone https://github.com/ros2/rmw_cyclonedds ros2/rmw_cyclonedds -b jazzy
$ git clone https://github.com/eclipse-cyclonedds/cyclonedds eclipse-cyclonedds/cyclonedds -b ${CYCLONEDDS_BRANCH}
```

安装必要的包：

```console
$ cd ..
$ rosdep install --from src -i
```

构建：

```console
$ colcon build --symlink-install
```

## 切换到 rmw_cyclonedds

通过环境变量从其他 RMW 切换到 rmw_cyclonedds：

```console
$ export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
```

## 运行 talker 和 listener

```console
$ source /opt/ros/jazzy/setup.bash
$ ros2 run demo_nodes_cpp talker
```

```console
$ source /opt/ros/jazzy/setup.bash
$ ros2 run demo_nodes_cpp listener
```

---
[返回 DDS 实现](index.md)
