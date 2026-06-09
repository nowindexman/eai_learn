> 原文地址：https://docs.ros.org/en/jazzy/Installation/Alternatives/macOS-Development-Setup.html

# macOS（源码构建）

## 系统要求

目前支持 macOS Mojave (10.14)。

## 系统设置

### 安装前置条件

1. **Xcode**：如未安装，从 App Store 安装 `Xcode <https://apps.apple.com/app/xcode/id497799835>`_。安装命令行工具：

```console
$ xcode-select --install
$ sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

> 注意：如果手动安装了 Xcode.app，需要接受许可证：``sudo xcodebuild -license``

2. **brew**：从 http://brew.sh/ 安装。可选检查：``brew doctor``

3. 使用 ``brew`` 安装依赖：

```console
$ brew install asio assimp bison bullet cmake console_bridge cppcheck \
  cunit eigen freetype graphviz opencv openssl orocos-kdl pcre poco \
  pyqt@5 python qt@5 sip spdlog tinyxml2
```

4. 设置环境变量：

```console
# 添加 openssl 目录用于 DDS-Security
$ echo "export OPENSSL_ROOT_DIR=$(brew --prefix openssl)" >> ~/.zshrc

# 添加 Qt 目录到 PATH 和 CMAKE_PREFIX_PATH
$ export CMAKE_PREFIX_PATH=$CMAKE_PREFIX_PATH:$(brew --prefix qt@5)
$ export PATH=$PATH:$(brew --prefix qt@5)/bin
```

5. 使用 pip 安装更多依赖：

```console
$ python3 -m pip install --upgrade pip

$ python3 -m pip install -U \
  --config-settings="--global-option=build_ext" \
  --config-settings="--global-option=-I$(brew --prefix graphviz)/include/" \
  --config-settings="--global-option=-L$(brew --prefix graphviz)/lib/" \
  argcomplete catkin_pkg colcon-common-extensions coverage \
  cryptography empy flake8 flake8-blind-except==0.1.1 flake8-builtins \
  flake8-class-newline flake8-comprehensions flake8-deprecated \
  flake8-import-order flake8-quotes \
  importlib-metadata jsonschema lark==1.1.1 lxml matplotlib mock mypy==0.931 netifaces \
  psutil pydot pygraphviz pyparsing==2.4.7 \
  pytest-mock rosdep rosdistro setuptools==59.6.0 vcstool
```

### 禁用系统完整性保护（SIP）

macOS/OS X >=10.11 默认启用系统完整性保护。SIP 会阻止进程继承动态链接器环境变量（如 ``DYLD_LIBRARY_PATH``），需要 `按照这些说明 <https://developer.apple.com/library/content/documentation/Security/Conceptual/System_Integrity_Protection_Guide/ConfiguringSystemIntegrityProtection/ConfiguringSystemIntegrityProtection.html>`__ 禁用它。

## 构建 ROS 2

### 获取 ROS 2 代码

```console
$ mkdir -p ~/ros2_jazzy/src
$ cd ~/ros2_jazzy
$ vcs import --input https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos src
```

### 构建工作区代码

```console
$ cd ~/ros2_jazzy/
$ colcon build --symlink-install --packages-skip-by-dep python_qt_binding
```

> 注意：由于 SIP、Qt@5 和 PyQt5 的未解决问题，需要禁用 ``python_qt_binding`` 才能构建成功。

## 环境设置

```console
$ . ~/ros2_jazzy/install/setup.zsh
```

## 尝试示例

```console
$ ros2 run demo_nodes_cpp talker
```

```console
$ ros2 run demo_nodes_py listener
```

## 卸载

1. 打开新终端并不 source 工作区的 ``setup`` 文件即可。
2. 释放空间：``rm -rf ~/ros2_jazzy``

---
[返回替代方案](index.md)
