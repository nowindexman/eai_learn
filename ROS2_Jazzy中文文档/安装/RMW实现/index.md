> 原文地址：https://docs.ros.org/en/jazzy/Installation/RMW-Implementations.html

# RMW 实现

默认情况下，ROS 2 使用 DDS 作为其 `中间件 <https://design.ros2.org/articles/ros_on_dds.html>`__。它兼容多种 DDS 或 RTPS（DDS 线协议）供应商。目前支持 eProsima 的 Fast DDS、RTI 的 Connext DDS、Eclipse Cyclone DDS 和 GurumNetworks GurumDDS。

还支持非 DDS 的 RMW 实现，如 Zenoh。

请参阅 `REP-2000 <https://reps.openrobotics.org/rep-2000/>`__ 了解各发行版支持的 RMW 供应商。

默认的 RMW 供应商是 eProsima 的 Fast DDS。

查看所有可用选项：

- :doc:`DDS 实现 <RMW实现/DDS实现/index>` 介绍如何使用 DDS。
- :doc:`非 DDS 实现 <RMW实现/非DDS实现/index>` 介绍如何使用非 DDS 实现。

---
[返回安装首页](index.md)

## 子页面

- [DDS 实现](DDS实现/index.md)
- [非 DDS 实现](非DDS实现/index.md)

