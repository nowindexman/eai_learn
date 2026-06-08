> 原文地址：https://docs.ros.org/en/jazzy/Installation.html

# 安装

ROS 2 Jazzy Jalisco 的安装选项：

## 二进制软件包

二进制包仅为 [REP-2000](https://reps.openrobotics.org/rep-2000/#rolling-ridley-june-2020---ongoing) 中列出的一级操作系统创建。如果您运行的不是以下操作系统，可能需要从源码构建或使用[容器方案](../How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.md)来在您的平台上运行 ROS 2。

我们提供以下平台的 ROS 2 二进制包：

- **Ubuntu Linux (amd64 / aarch64) - Noble Numbat (24.04)**
  - [deb 包](Ubuntu-deb包安装.md)（推荐）
  - [二进制归档](Ubuntu二进制归档.md)
- **Red Hat Enterprise Linux 9 (amd64)**
  - [RPM 包](RHEL-RPM包安装.md)（推荐）
  - [二进制归档](RHEL二进制归档.md)
- **Windows 10 (amd64)**
  - [Windows 二进制 (VS 2019)](Windows二进制安装.md)

## 从源码构建

我们支持在以下平台上从源码构建 ROS 2：

- Ubuntu Linux 24.04
- Windows 10
- RHEL-9/Fedora
- macOS

## 选择哪种安装方式？

从二进制包安装或从源码安装都能获得功能完整、可用的 ROS 2 安装。两种方式的区别取决于您计划如何使用 ROS 2。

**二进制包** 面向一般用户，提供已预构建的 ROS 2 安装。非常适合想要立即开始使用 ROS 2 的用户。

Linux 用户有两种安装二进制包的选择：
- **软件包**（deb 或 RPM，取决于平台）
- **二进制归档**

推荐使用软件包安装，因为它会自动安装必要的依赖项，并随系统更新一起更新。但是，安装 deb 包需要 root 权限。如果没有 root 权限，二进制归档是次优选择。

Windows 用户选择二进制包安装时只有二进制归档选项（deb 包仅适用于 Ubuntu/Debian）。

**从源码构建** 面向希望修改或选择性省略 ROS 2 基础部分的开发者。也推荐用于不支持二进制包的平台。从源码构建还可以让您安装最新版本的 ROS 2。

### 为 ROS 2 核心做贡献？

如果您计划直接为 ROS 2 核心包做贡献，可以安装[最新开发版源码](最新开发版安装.md)，它与 [Rolling 发行版](../发行版/index.md#rolling-发行版) 共享安装说明。

---

[下一页：Ubuntu deb 包安装](Ubuntu-deb包安装.md)
