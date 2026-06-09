> 原文地址：https://docs.ros.org/en/jazzy/Installation/RMW-Implementations/DDS-Implementations/Working-with-GurumNetworks-GurumDDS.html

# GurumNetworks GurumDDS

``rmw_gurumdds`` 是使用 GurumNetworks GurumDDS 的 ROS 中间件接口实现。
有关 GurumDDS 的更多信息，请访问 `GurumNetworks 网站 <https://gurum.cc/index_eng>`_。

## 前置条件

需已完成 ROS 2 环境设置。

版本要求：

| ROS 2 发行版 | GurumDDS 版本 |
|-------------|-------------|
| jazzy | ``>= 3.2.0`` |
| humble | ``3.1.x`` |

可从 `GurumDDS 免费试用页面 <https://gurum.cc/free_trial_eng.html>`_ 获取免费试用许可证。获取许可证后，放置在 ``/etc/gurumnet``。

## 安装

### 方式 1：从 ROS 2 apt 仓库安装（推荐）

```console
$ sudo apt install ros-jazzy-rmw-gurumdds-cpp
```

这会同时安装 ``rmw_gurumdds_cpp`` 和 ``gurumdds``。

### 方式 2：从源码构建

1. 克隆仓库：

```console
$ cd ros2_ws/src
$ git clone https://github.com/ros2/rmw_gurumdds -b jazzy ros2/rmw_gurumdds
```

2. 安装依赖：

```console
$ cd ..
$ rosdep install --from src -i --rosdistro jazzy
```

3. 构建：

```console
$ colcon build --symlink-install
```

## 切换到 rmw_gurumdds

```console
$ export RMW_IMPLEMENTATION=rmw_gurumdds_cpp
```

## 测试安装

```console
$ source /opt/ros/jazzy/setup.bash
$ ros2 run demo_nodes_cpp talker
```

```console
$ source /opt/ros/jazzy/setup.bash
$ ros2 run demo_nodes_cpp listener
```

如果节点通信成功，说明安装正常工作。

---
[返回 DDS 实现](index.md)
