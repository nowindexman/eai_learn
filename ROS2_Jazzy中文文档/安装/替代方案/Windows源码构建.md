> 原文地址：https://docs.ros.org/en/jazzy/Installation/Alternatives/Windows-Development-Setup.html

# Windows（源码构建）

本页面介绍如何在 Windows 上设置 ROS 2 开发环境。

## 系统要求

### 语言支持

确保有支持 ``UTF-8`` 的区域设置。对于中文 Windows 安装，可能需要安装 `英语语言包 <https://support.microsoft.com/en-us/windows/language-packs-for-windows-a5094319-a92d-18de-5b53-1cfc697cfca8>`_。

### 创建 ROS 2 安装位置

启动管理员命令提示符，创建目录（路径应尽可能短）：

```console
$ mkdir C:\dev
```

### 增加 Windows 最大路径长度

Windows 默认最大路径长度限制为 260 个字符。ROS 2 构建会使用更长的路径：

```console
$ powershell New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

> 注意：需要以管理员身份执行。

## 安装前置条件

### 安装 MSVC

需要安装 MSVC 2022 编译器来编译 ROS 2 代码：

```console
$ powershell irm https://aka.ms/vs/17/release/vs_buildtools.exe -OutFile vs_buildtools_2022.exe
```

安装 MSVC 2022：

```console
$ .\vs_buildtools_2022.exe --quiet --wait --norestart --add Microsoft.Component.MSBuild --add Microsoft.Net.Component.4.6.1.TargetingPack --add Microsoft.Net.Component.4.8.SDK --add Microsoft.VisualStudio.Component.CoreBuildTools --add Microsoft.VisualStudio.Component.Roslyn.Compiler --add Microsoft.VisualStudio.Component.TextTemplating --add Microsoft.VisualStudio.Component.VC.CLI.Support --add Microsoft.VisualStudio.Component.VC.CoreBuildTools --add Microsoft.VisualStudio.Component.VC.CoreIde --add Microsoft.VisualStudio.Component.VC.Redist.14.Latest --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 --add Microsoft.VisualStudio.Component.Windows11SDK --add Microsoft.VisualStudio.Component.Windows11SDK.22621 --add Microsoft.VisualStudio.ComponentGroup.NativeDesktop.Core --add Microsoft.VisualStudio.Workload.MSBuildTools --add Microsoft.VisualStudio.Workload.VCTools
```

> 注意：MSVC 安装可能需要很长时间，且安装过程中没有反馈。

### 安装 pixi

ROS 2 使用 `conda-forge <https://conda-forge.org/>`__ 作为包后端，`pixi <https://pixi.sh/latest/>`__ 作为前端。

使用 https://pixi.sh/latest/ 上的说明安装 ``pixi``。安装后关闭命令提示符并重新启动。

### 安装依赖

```console
$ cd C:\dev
$ powershell irm https://raw.githubusercontent.com/ros2/ros2/refs/heads/jazzy/pixi.toml -OutFile pixi.toml
$ pixi install
```

## 构建 ROS 2

### 配置 MSVC 编译器

在用于编译的命令提示符中需要执行（运行时不需要）：

```console
$ call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x86_amd64
```

### 配置 pixi 环境

每个命令提示符都需要：

```console
$ cd C:\dev
$ pixi shell
```

### 获取 ROS 2 代码

```console
$ md C:\dev\jazzy\src
$ cd C:\dev\jazzy
$ vcs import --input https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos src
```

### 构建工作区代码

```console
$ colcon build --merge-install
```

> 注意：使用 ``--merge-install`` 避免构建后 ``PATH`` 变量过长。源码安装可能需要较长时间。

## 环境设置

启动新命令提示符：

```console
$ cd C:\dev
$ pixi shell
$ call C:\dev\jazzy\install\local_setup.bat
```

## 尝试示例

首次运行任何可执行文件时，需要允许通过 Windows 防火墙的网络访问。

运行测试：

```console
$ cd C:\dev\jazzy
$ colcon test --merge-install
$ colcon test-result
```

运行 C++ talker：

```console
$ call install\local_setup.bat
$ ros2 run demo_nodes_cpp talker
```

在另一个命令提示符中运行 Python listener：

```console
$ call install\local_setup.bat
$ ros2 run demo_nodes_py listener
```

> 注意：不建议在已 source ``local_setup.bat`` 的命令提示符中构建。

## 卸载

1. 打开新终端并不 source 工作区的 ``setup`` 文件即可。
2. 释放空间：``rmdir /s /q C:\dev\jazzy``

---
[返回替代方案](index.md)
