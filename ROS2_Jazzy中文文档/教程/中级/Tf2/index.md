> 原文地址：https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html


    Tutorials/Tf2/Tf2-Main

.. _Tf2Main:

# ``tf2``

Many of the tf2 tutorials are available for both C++ and Python.
The tutorials are streamlined to complete either the C++ track or the Python track.
If you want to learn both C++ and Python, you should go through the tutorials once for C++ and once for Python.

   :depth: 2
   :local:

   :hidden:

   Introduction-To-Tf2
   Writing-A-Tf2-Static-Broadcaster-Py
   Writing-A-Tf2-Static-Broadcaster-Cpp
   Writing-A-Tf2-Broadcaster-Py
   Writing-A-Tf2-Broadcaster-Cpp
   Writing-A-Tf2-Listener-Py
   Writing-A-Tf2-Listener-Cpp
   Adding-A-Frame-Py
   Adding-A-Frame-Cpp
   Learning-About-Tf2-And-Time-Cpp
   Time-Travel-With-Tf2-Cpp
   Debugging-Tf2-Problems
   Quaternion-Fundamentals
   Using-Stamped-Datatypes-With-Tf2-Ros-MessageFilter

# Workspace setup

If you have not yet created a workspace in which to complete the tutorials, [follow this tutorial ](../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace).

# Learning tf2

#. [Introduction to tf2 ](./Introduction-To-Tf2).

   This tutorial will give you a good idea of what tf2 can do for you.
   It shows off some of the tf2 power in a multi-robot example using turtlesim.
   This also introduces using ``tf2_echo``, ``view_frames``, and ``rviz``.

#. Writing a static broadcaster [(Python) ](./Writing-A-Tf2-Static-Broadcaster-Py) [(C++) ](./Writing-A-Tf2-Static-Broadcaster-Cpp).

   This tutorial teaches you how to broadcast static coordinate frames to tf2.

#. Writing a broadcaster [(Python) ](./Writing-A-Tf2-Broadcaster-Py) [(C++) ](Writing-A-Tf2-Broadcaster-Cpp).

   This tutorial teaches you how to broadcast the state of a robot to tf2.

#. Writing a listener [(Python) ](./Writing-A-Tf2-Listener-Py) [(C++) ](./Writing-A-Tf2-Listener-Cpp).

   This tutorial teaches you how to use tf2 to get access to frame transformations.

#. Adding a frame [(Python) ](./Adding-A-Frame-Py) [(C++) ](Adding-A-Frame-Cpp).

   This tutorial teaches you how to add an extra fixed frame to tf2.

#. Using time [(C++) ](Learning-About-Tf2-And-Time-Cpp).

   This tutorial teaches you to use the timeout in ``lookup_transform`` function to
   wait for a transform to be available on the tf2 tree.

#. Traveling in time [(C++) ](./Time-Travel-With-Tf2-Cpp).

   This tutorial teaches you about advanced time travel features of tf2.

# Debugging tf2

#. [Quaternion fundamentals ](./Quaternion-Fundamentals).

   This tutorial teaches you basics of quaternion usage in ROS 2.

#. [Debugging tf2 problems ](./Debugging-Tf2-Problems).

   This tutorial teaches you about a systematic approach for debugging tf2 related problems.

# Using sensor messages with tf2

#. [Using stamped datatypes with tf2_ros::MessageFilter ](./Using-Stamped-Datatypes-With-Tf2-Ros-MessageFilter).

   This tutorial teaches you how to use ``tf2_ros::MessageFilter`` to process stamped datatypes.


---
[返回](../index.md)

## 子页面

- [Introducing ``tf2``](Tf2介绍.md)
- [Using time (C++)](Tf2和时间-Cpp.md)
- [Traveling in time (C++)](Tf2时间旅行-Cpp.md)
- [Using stamped datatypes with ``tf2_ros::MessageFilter``](使用带戳数据类型与消息过滤器.md)
- [Quaternion fundamentals](四元数基础.md)
- [Adding a frame (C++)](添加坐标系-Cpp.md)
- [Adding a frame (Python)](添加坐标系-Py.md)
- [Writing a broadcaster (C++)](编写广播器-Cpp.md)
- [Writing a broadcaster (Python)](编写广播器-Py.md)
- [Writing a listener (C++)](编写监听器-Cpp.md)
- [Writing a listener (Python)](编写监听器-Py.md)
- [Writing a static broadcaster (C++)](编写静态广播器-Cpp.md)
- [Writing a static broadcaster (Python)](编写静态广播器-Py.md)
- [Debugging](调试Tf2问题.md)

