> 原文地址：https://docs.ros.org/en/jazzy/How-To-Guides/Migrating-from-ROS1.html

# Migrating from ROS 1 to ROS 2

These guides show how to convert existing ROS 1 packages to ROS 2.
If you are new to porting between ROS 1 and ROS 2, it is recommended to read through the guides in order.

   :maxdepth: 1

   Migrating-from-ROS1/Migrating-Packages
   Migrating-from-ROS1/Migrating-Package-XML
   Migrating-from-ROS1/Migrating-Interfaces
   Migrating-from-ROS1/Migrating-CPP-Package-Example
   Migrating-from-ROS1/Migrating-CPP-Packages
   Migrating-from-ROS1/Migrating-Python-Package-Example
   Migrating-from-ROS1/Migrating-Python-Packages
   Migrating-from-ROS1/Migrating-Launch-Files
   Migrating-from-ROS1/Migrating-Parameters
   Migrating-from-ROS1/Migrating-Scripts

# Automatic tools

There are also some automatic conversion tools that exist, though they are not exhaustive:

* [Magical ROS 2 Conversion Tool ](https://github.com/DLu/roscompile/tree/main/magical_ros2_conversion_tool)
* Launch File migrator that converts a ROS 1 XML launch file to a ROS 2 Python launch file: https://github.com/aws-robotics/ros2-launch-file-migrator
* Amazon has made their tools for porting from ROS 1 to ROS 2 available at: https://github.com/awslabs/ros2-migration-tools/tree/master/porting\_tools
* [rospy2 ](https://github.com/dheera/rospy2) Python project to automatically convert rospy calls to rclpy calls


---
[返回](../index.md)

## 子页面

- [Migrating C++ Packages Reference](迁移C++包.md)
- [Migrating a C++ Package Example](迁移C++包示例.md)
- [Migrating Launch Files](迁移Launch文件.md)
- [Migrating your package.xml to format 2](迁移Package-XML.md)
- [Migrating Python Packages Reference](迁移Python包.md)
- [Migrating a Python Package Example](迁移Python包示例.md)
- [Migrating Packages](迁移包.md)
- [Migrating Parameters](迁移参数.md)
- [Migrating Interfaces](迁移接口.md)
- [Migrating Scripts](迁移脚本.md)

