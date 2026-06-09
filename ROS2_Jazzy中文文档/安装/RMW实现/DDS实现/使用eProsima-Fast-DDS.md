> 原文地址：https://docs.ros.org/en/jazzy/Installation/RMW-Implementations/DDS-Implementations/Working-with-eProsima-Fast-DDS.html

# eProsima Fast DDS

eProsima Fast DDS 是一个完整的开源 DDS 实现，适用于实时嵌入式架构和操作系统。
详见：https://www.eprosima.com/index.php/products-all/eprosima-fast-dds

## 前置条件

需已安装 rosdep。

## 安装包

最简单的方式是从 ROS 2 apt 仓库安装：

```console
$ sudo apt install ros-jazzy-rmw-fastrtps-cpp
```

## 从源码构建

在 ROS 2 工作区源码目录中克隆 Fast DDS 和 rmw_fastrtps：

```console
$ cd ros2_ws/src
$ git clone https://github.com/ros2/rmw_fastrtps ros2/rmw_fastrtps -b jazzy
$ git clone https://github.com/eProsima/Fast-DDS eProsima/fastrtps
```

安装必要的包并构建：

```console
$ cd ..
$ rosdep install --from src -i
$ colcon build --symlink-install
```

## 切换到 rmw_fastrtps

```console
$ export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
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
