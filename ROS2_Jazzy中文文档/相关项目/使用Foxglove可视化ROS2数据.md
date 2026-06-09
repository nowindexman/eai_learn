> 原文地址：https://docs.ros.org/en/jazzy/Related-Projects/Visualizing-ROS-2-Data-With-Foxglove.html

# 使用 Foxglove 可视化 ROS 2 数据

[Foxglove](https://foxglove.dev/) 是一个面向机器人开发者的可视化和可观测性工具。它可在浏览器中使用，也可作为独立桌面应用，对个人、小团队和学术用途免费。

## 安装

使用 Foxglove 需要[创建账户](https://app.foxglove.dev/signup)，这是免费的，只需要一个有效的邮箱地址。

创建账户后，可以通过打开 Google Chrome 并导航到 [app.foxglove.dev](https://app.foxglove.dev) 在网页上使用 Foxglove。

要使用 Linux、macOS 或 Windows 的桌面应用，可以直接从 [Foxglove 网站](https://foxglove.dev/download)下载。

> **注意：** Foxglove 使用了 Google Chrome 的特定功能。虽然部分功能可能在其他浏览器上可用，但不受官方支持。为获得最佳体验，建议使用 Chrome 或桌面应用。

## 连接实时数据源

要连接到实时 ROS 2 协议栈，需要[安装 Foxglove ROS 2 bridge](https://docs.foxglove.dev/docs/connecting-to-data/ros-foxglove-bridge)：

```console
$ sudo apt install ros-$ROS_DISTRO-foxglove-bridge
```

安装好 bridge 后，启动它：

```console
$ ros2 launch foxglove_bridge foxglove_bridge_launch.xml
```

在机器人上运行 bridge 后，就可以在 Foxglove 中连接查看数据了。确保与机器人在同一网络中，打开 Foxglove（网页或桌面版）并点击"Open connection"。

选择"Foxglove WebSocket"选项并输入机器人的 WebSocket URL。默认为 `ws://localhost:8765`，可以在[这里](https://docs.foxglove.dev/docs/connecting-to-data/ros-foxglove-bridge#configuration-1)了解 ROS Foxglove bridge 的配置选项。

> **注意：** Foxglove 也可以使用 rosbridge 连接，但出于性能和稳定性考虑，推荐使用 Foxglove bridge。

## 查看和回放录制数据

如果要可视化录制的数据，可以使用 Foxglove 回放 ROS 2 的 `.mcap` 文件以及旧版 ROS 2 的 `.db3` 文件和 ROS 1 的 `.bag` 文件。Foxglove 查看录制数据特别方便，因为它不需要 ROS 2 运行即可查看数据。

使用 [ros2 bag 命令行工具](../../教程/入门-CLI工具/录制和回放数据/录制和回放数据.md) 从机器人录制数据到 `.mcap` 文件：

```console
$ ros2 bag record -a
```

在 Foxglove 面板或菜单中，选择"Open local file"并导航到录制的 `.mcap` 文件。

更多信息请参阅 [Foxglove 文档关于可用数据源类型的说明](https://docs.foxglove.dev/docs/connecting-to-data/introduction/)。

## 使用面板构建布局

[面板](https://docs.foxglove.dev/docs/visualization/panels/introduction) 允许你可视化不同类型的数据，如日志、地图、绘图和 3D 信息。你可以通过拖放面板到 Foxglove [布局](https://foxglove.dev/docs/visualization/layouts) 中来同时查看多种类型的数据。

你还可以保存布局以备将来使用或与团队共享。

点击菜单栏左上角的"Add panel"图标可以找到所有可用面板的完整列表。

下面重点介绍一些特别有用的面板：

### 3D 面板：查看 3D 数据和可视化标记

通过点击右上角的齿轮图标打开面板设置。通过左侧的话题选择器选择要显示的话题，并在"Edit topic settings"菜单中配置每个话题的可视化设置。

发布 marker 消息可以向 3D 面板场景添加基本形状（箭头、球体等）和更复杂的可视化（占用网格、点云等）。

参考[文档](https://foxglove.dev/docs/visualization/panels/3d)获取[支持的消息类型](https://foxglove.dev/docs/visualization/panels/3d#supported-messages)和[用户交互](https://foxglove.dev/docs/visualization/panels/3d#user-interactions)的完整列表。

### 诊断面板：查看和过滤诊断消息

在运行中的数据流中，以 `diagnostic_msgs/msg/DiagnosticArray` 数据类型显示已见节点的状态（即 stale、error、warn 或 OK），并显示给定 `diagnostic_name/hardware_id` 的诊断数据。

参考[文档](https://foxglove.dev/docs/visualization/panels/diagnostics)获取更多详情。

### 图像面板：查看相机图像

显示原始和压缩图像以及压缩视频，支持 2D 标注如文本标签、圆形和点。可以叠加 3D 标记以提供额外上下文。

参考[文档](https://foxglove.dev/docs/visualization/panels/image)获取更多详情。

### 日志面板：查看日志消息

要实时查看 `rcl_interfaces/msg/Log` 消息，使用桌面应用[连接](https://docs.foxglove.dev/docs/connecting-to-data/frameworks/ros2)到运行中的 ROS 协议栈。要查看预录制数据文件中的 `rcl_interfaces/msg/Log` 消息，可以将文件拖放到[网页版](https://app.foxglove.dev)或桌面应用中。

接下来，添加一个 [Log](https://foxglove.dev/docs/visualization/panels/log) 面板到布局中。如果连接正确，你应该能看到日志消息列表，并可以按节点名或严重级别进行过滤。

参考[文档](https://foxglove.dev/docs/visualization/panels/log)获取更多详情。

### 绘图面板：随时间绘制任意值

从话题[消息路径](https://docs.foxglove.dev/docs/visualization/message-path-syntax)绘制任意数值。

回放本地或远程数据文件时，该面板将预加载指定话题消息路径在整个回放时间线上的数据。当前回放时间由垂直灰色条表示。

参考[文档](https://foxglove.dev/docs/visualization/panels/plot)获取更多详情。

### 原始消息面板：查看接收到的话题消息

检查数据源中的特定[消息路径](https://docs.foxglove.dev/docs/visualization/message-path-syntax)。

当收到指定路径的新消息时，可折叠树将只显示最新消息。你可以展开和折叠键，这些状态会在回放过程中保持。

参考[文档](https://foxglove.dev/docs/visualization/panels/raw-messages)获取更多详情。

### 遥操作面板：遥操作你的机器人

通过在给定话题上发布 `geometry_msgs/msg/Twist` 消息回你的实时 ROS 协议栈来遥操作物理机器人。

参考[文档](https://foxglove.dev/docs/visualization/panels/teleop)获取更多详情。

### 可视化 URDF：查看和操控你的 URDF 模型

Foxglove 的 [3D 面板支持显示统一机器人描述格式（URDF）模型](https://docs.foxglove.dev/docs/visualization/panels/3d/#custom-layers)，在你的机器人世界上下文中展示。

要在 Foxglove 中可视化和控制你的机器人模型，打开网页或桌面应用并添加一个 3D 面板到布局中。

使用 HTTP/HTTPS URL（网页和桌面版）或 `file://` 和 `package://` 前缀 URL（仅桌面版）添加任意数量的 URDF 模型作为 3D 面板的自定义层。

除这些 URL 外，3D 面板还可以从 `/robot_description` 话题显示 URDF。

添加到 3D 面板后，URDF 文件将根据模型的连杆和关节填充变换树，包含帧和变换。

需要注意的是，Foxglove 使用与 RViz 不同的默认设置——如果你的网格显示不正确，可能需要调整面板设置'Scene'部分中的"Ignore COLLADA <up_axis>"（用于 DAE 网格）和"Mesh up axis"（用于 STL 和 OBJ 网格）选项。

你可以通过发布变换消息来更新这棵树以移动 URDF 模型的关节位置——如果之前使用过 JointState 消息，可以使用 robot_state_publisher 节点在运行时将它们转换为 TF 消息。

你还可以通过面板设置界面手动控制模型的关节。

参考[文档](https://foxglove.dev/docs/visualization/panels/urdf-viewer)获取更多详情。

## 其他基本操作

### 查看 ROS 话题图

[使用桌面应用](https://foxglove.dev/download)，[连接](https://docs.foxglove.dev/docs/connecting-to-data/frameworks/ros2)到运行中的 ROS 协议栈。接下来，添加一个 [Topic Graph](https://foxglove.dev/docs/visualization/panels/topic-graph) 面板到布局中。如果连接正确，你应该能在该面板中看到 ROS 节点、话题和服务的计算图。使用面板右侧的控件选择要显示的话题或切换服务。

### 查看和编辑 ROS 参数

[使用桌面应用](https://foxglove.dev/download)，[连接](https://docs.foxglove.dev/docs/connecting-to-data/frameworks/ros2)到运行中的 ROS 协议栈。接下来，添加一个 [Parameters](https://foxglove.dev/docs/visualization/panels/parameters) 面板到布局中。如果连接正确，你应该能看到当前 `rosparams` 的实时视图。你可以编辑这些参数值以将 `rosparam` 更新发布回 ROS 协议栈。

### 向实时 ROS 协议栈发布消息

[使用桌面应用](https://foxglove.dev/download)，[连接](https://docs.foxglove.dev/docs/connecting-to-data/frameworks/ros2)到运行中的 ROS 协议栈。接下来，添加一个 [Publish](https://foxglove.dev/docs/visualization/panels/publish) 面板到布局中。

指定要发布的话题以推断其数据类型并用 JSON 消息模板填充文本字段。

在常用 ROS 数据类型的下拉列表中选择数据类型也会用 JSON 消息模板填充文本字段。

在点击"Publish"之前编辑模板以自定义消息。

---
[返回相关项目](../相关项目.md)
