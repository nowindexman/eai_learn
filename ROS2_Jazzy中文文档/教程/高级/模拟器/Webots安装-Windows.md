> 原文地址：https://docs.ros.org/en/jazzy/Tutorials/Advanced/Simulators/Webots/Installation-Windows.html

# Installation (Windows)

**Goal:** Install the ``webots_ros2`` package and run simulation examples on Windows.

**Tutorial level:** Advanced

**Time:** 10 minutes

   :depth: 2
   :local:

# Background

The ``webots_ros2`` package provides an interface between ROS 2 and Webots.
It includes several sub-packages, including ``webots_ros2_driver``, which allows ROS nodes to communicate with Webots.
Other sub-packages are mainly examples that show multiple possible implementations using the interface.
In this tutorial, you are going to install the package and learn how to run one of these examples.

# Prerequisites

It is recommended to understand basic ROS principles covered in the beginner :doc:`../../../../Tutorials`.
In particular, :doc:`../../../Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace` and :doc:`../../../Beginner-Client-Libraries/Creating-Your-First-ROS2-Package` are useful prerequisites.

Webots is a prerequisite to use the ``webots_ros2`` package.
You can follow the [installation procedure ](https://cyberbotics.com/doc/guide/installation-procedure) or [build it from sources ](https://github.com/cyberbotics/webots/wiki/Windows-installation/).

Alternatively, you can also let ``webots_ros2`` download Webots automatically.
This option appears when you launch an example of the package and no Webots installation is found.

# Multiple Installations of Webots

If you have more than one installation of Webots, ROS 2 will look for Webots at the following locations (in this order):

1. If the ``ROS2_WEBOTS_HOME`` environment variable is set, ROS 2 will use the Webots in this folder, regardless of its version.
2. If the ``WEBOTS_HOME`` environment variable is set, ROS 2 will use the Webots in this folder, regardless of its version.
3. If none of the previous points is set/installed ROS 2 will look for Webots in the default installation paths for a compatible version: ``C:\Program Files\Webots``.
4. If Webots couldn't be found, ``webots_ros2`` will show a window and offer automatic Webots installation of the last compatible version.

# Tasks

# 1 Install WSL2

On Windows, WSL (Windows Subsystem for Linux) improves the user experience with ROS 2 compared to native Windows installation, as it runs on a Linux platform.
Install WSL with an Ubuntu version which is compatible with your ROS distribution and upgrade to WSL2 following the [official Microsoft tutorial ](https://learn.microsoft.com/en-us/windows/wsl/install).

# 2 Install ROS 2 in WSL

Install ROS 2 inside Ubuntu WSL, following :doc:`../../../../Installation/Ubuntu-Install-Debs`.

# 3 Install ``webots_ros2``

The following commands must be run inside the WSL environment.



        Run the following command in a terminal.

```bash

         $ sudo apt-get install ros-{DISTRO}-webots-ros2

 .. group-tab:: Install ``webots_ros2`` from sources

     Create a ROS 2 workspace with its ``src`` directory.

```bash

         $ mkdir -p ~/ros2_ws/src

     Source the ROS 2 environment.

```bash

         $ source /opt/ros/{DISTRO}/setup.bash

     Retrieve the sources from Github.

```bash

         $ cd ~/ros2_ws
         $ git clone --recurse-submodules https://github.com/cyberbotics/webots_ros2.git src/webots_ros2

     Install the package dependencies.

```bash

         $ sudo apt install python3-pip python3-rosdep python3-colcon-common-extensions
         $ sudo rosdep init && rosdep update
         $ rosdep install --from-paths src --ignore-src --rosdistro {DISTRO}

     Build the package using ``colcon``.

```bash

         $ colcon build

     Source this workspace.

```bash

         $ source install/local_setup.bash
```

# 4 Launch the ``webots_ros2_universal_robot`` example

WSL doesn't support hardware acceleration (yet).
Therefore, Webots should be started on Windows, while the ROS part is running inside WSL.
To do so, the following commands must be run inside the WSL environment.

First source the ROS 2 environment, if not done already.

```bash

     $ source /opt/ros/{DISTRO}/setup.bash
```
Setting the ``WEBOTS_HOME`` environment variable allows you to start a specific Webots installation (e.g. ``C:\Program Files\Webots``).
Use the mount point "/mnt" to refer to a path on native Windows.

```bash

     $ export WEBOTS_HOME=/mnt/c/Program\ Files/Webots
```
If installed from sources, source your ROS 2 workspace, if not done already.

```bash

     $ cd ~/ros2_ws
     $ source install/local_setup.bash
```
Use the ROS 2 launch command to start demo packages (e.g. ``webots_ros2_universal_robot``).

```bash

     $ ros2 launch webots_ros2_universal_robot multirobot_launch.py
```

# 5 RViz troubleshooting

With recent versions of WSL2, RViz should work out of the box.

You can check if it works correctly by running any example that uses RViz, for example:

```bash

     $ sudo apt install ros-{DISTRO}-slam-toolbox
     $ ros2 launch webots_ros2_tiago robot_launch.py rviz:=true slam:=true
```
The Tiago robot can be controlled using:

```bash

     $ ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
With older WSL versions, RViz2 may not work directly, as no display is available.
To use RViz, you can either upgrade WSL or enable X11 forwarding.


        In a Windows shell:

```bash

         $ wsl --update

 .. group-tab:: Enable X11 forwarding

     For older versions of WSL, the following steps can be followed:

     1. Install `VcXsrv <https://sourceforge.net/projects/vcxsrv/>`_.
     2. Launch VcXsrv.
        You can leave most of the parameters default, except the ``Extra settings`` page, where you must set ``Clipboard``, ``Primary Selection`` and ``Disable access control`` and unset ``Native opengl``.
     3. You can save the configuration for future launches.
     4. Click on ``Finish``, you will see that the X11 server is running in the icon tray.
     5. In your WSL environment, export the ``DISPLAY`` variable.

```bash

             $ export DISPLAY=$(ip route list default | awk '{print }'):0

         You can add this to your ``.bashrc``, so that it is set for every future WSL environment.

```bash

             $ echo "export DISPLAY=$(ip route list default | awk '{print }'):0" >> ~/.bashrc

```

---
[返回](../../index.md)
