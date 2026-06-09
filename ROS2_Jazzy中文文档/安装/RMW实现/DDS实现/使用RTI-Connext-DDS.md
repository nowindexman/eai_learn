> 原文地址：https://docs.ros.org/en/jazzy/Installation/RMW-Implementations/DDS-Implementations/Working-with-RTI-Connext-DDS.html

# RTI Connext DDS

RTI Connext DDS 在全球 2000 多个最苛刻的系统设计中得到信赖，以最高水平的性能、可靠性和安全性分发关键实时数据。它对于原型设计、研究、非商业和学术用途是免费的。
访问 `RTI 网站 <https://www.rti.com/ros>`__ 了解更多信息。

## 前置条件

### 安装 RTI Connext DDS

构建和使用 ``rmw_connextdds`` 需要与 ROS 2 发行版兼容的 Connext DDS 版本：

| ROS 2 发行版 | apt 安装版本 | 源码构建版本 |
|-------------|------------|------------|
| jazzy | ``6.0.1`` | ``6.0.1`` |
| humble | ``6.0.1`` | ``6.0.1`` |
| kilted | ``7.3.0`` | ``7.3.0`` |
| lyrical | ``7.7.0`` | ``7.7.0`` |

**从 ROS 2 apt 仓库安装**：

```console
$ sudo apt update && sudo apt install -q -y rti-connext-dds-6.0.1
```

此包仅包含 RTI Connext 核心 DDS 库，不包含完整的 Connext Professional 工具套件。

**其他安装选项**：`Connext Robotics Toolkit <https://www.rti.com/developers/connext-robotics-toolkit>`__ 包含完整的 Connext 工具套件，对于原型开发、研究、非商业和学术用途免费。

## 安装 rmw_connextdds 二进制包

```console
$ sudo apt update && sudo apt install -q -y ros-jazzy-rmw-connextdds
```

## 从源码构建 rmw_connextdds

克隆仓库并选择匹配的分支：

```console
$ mkdir -p ros2_ws/src
$ cd ros2_ws
$ git clone -b jazzy https://github.com/ros2/rmw_connextdds src/rmw_connextdds
```

安装必要的包：

```console
$ cd ..
$ rosdep install --from src -i
```

设置环境以帮助 colcon 找到 RTI Connext 的安装位置：

```console
$ source /opt/rti.com/rti_connext_dds-6.0.1/resource/scripts/rtisetenv_x64Linux4gcc8.5.0.bash
```

设置 ROS 2 环境并构建：

```console
$ source /opt/ros/jazzy/setup.bash
$ colcon build --symlink-install
$ source install/setup.bash
```

## 使用 rmw_connextdds

```console
$ export RMW_IMPLEMENTATION=rmw_connextdds
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
