> 原文地址：https://docs.ros.org/en/jazzy/Installation/RMW-Implementations/Non-DDS-Implementations/Working-with-Zenoh.html

# Zenoh

Zenoh 是一个开源通信协议和中间件，旨在促进异构系统之间的高效数据分发。它提供了高性能发布/订阅和分布式查询的位置透明抽象。
详见：https://zenoh.io/docs/getting-started/first-app/

## 前置条件

需已安装 rosdep。

## 安装包

Zenoh 的 RMW 实现可以通过二进制包安装（推荐用于稳定开发）。各受支持的 ROS 2 发行版的二进制包可在相应的 Tier-1 平台上获取。

```bash
sudo apt install ros-jazzy-rmw-zenoh-cpp
```

## 从源码构建

仅在需要最新功能时推荐从源码构建。

默认情况下，我们 vendor 并使用 zenoh 功能的子集编译 ``zenoh-cpp``。

1. 克隆仓库：

```bash
mkdir ~/ws_rmw_zenoh/src -p && cd ~/ws_rmw_zenoh/src
git clone https://github.com/ros2/rmw_zenoh.git -b jazzy
```

2. 安装依赖：

```bash
cd ~/ws_rmw_zenoh
rosdep install --from-paths src --ignore-src --rosdistro jazzy -y
```

3. 构建工作区：

```bash
source /opt/ros/jazzy/setup.bash
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release
```

## 切换到 rmw_zenoh_cpp

通过环境变量切换：

```bash
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
```

## 运行 talker 和 listener

首先启动 Zenoh 路由器：

```bash
# 终端 1
source /opt/ros/jazzy/setup.bash
ros2 run rmw_zenoh_cpp rmw_zenohd
```

> 注意：没有 Zenoh 路由器，节点将无法相互发现，因为默认情况下节点的会话配置中禁用了多播发现。节点将通过 Zenoh 路由器的 gossip 功能接收其他对等方的发现信息。

```bash
# 终端 2
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
source /opt/ros/jazzy/setup.bash
ros2 run demo_nodes_cpp talker
```

```bash
# 终端 3
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
source /opt/ros/jazzy/setup.bash
ros2 run demo_nodes_cpp listener
```

---
[返回非 DDS 实现](index.md)
