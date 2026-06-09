> 原文地址：https://docs.ros.org/en/jazzy/Installation/ROS-2-Mirrors.html

# 镜像

## 文档镜像

ROS 文档镜像在主站 `http://docs.ros.org <http://docs.ros.org>`_ 不可用时作为备份，并为地理位置更近的用户提供更快访问。

## Debian/Ubuntu（APT）仓库镜像

要使用这些镜像，请在 APT 配置中将官方 ROS 仓库 URL 替换为下面的镜像地址。

### 亚洲

| 镜像 | 国家 | URL |
|------|------|-----|
| 清华大学（TUNA） | 中国 | https://mirrors.tuna.tsinghua.edu.cn/ros2/ubuntu/ |
| 中国科学技术大学（USTC） | 中国 | https://mirrors.ustc.edu.cn/ros2/ubuntu/ |
| 阿里云（Aliyun） | 中国 | https://mirrors.aliyun.com/ros2/ubuntu/ |
| 齐鲁工业大学（QLU） | 中国 | https://mirrors.qlu.edu.cn/ros2/ubuntu/ |
| 重庆大学（CQU） | 中国 | https://mirrors.cqu.edu.cn/ros2/ubuntu/ |

### 欧洲

| 镜像 | 国家 | URL |
|------|------|-----|
| 代尔夫特理工大学 | 荷兰 | http://ftp.tudelft.nl/ros2/ubuntu/ |

### 北美

| 镜像 | 国家 | URL |
|------|------|-----|
| 马里兰大学（UMD） | 美国 | http://mirror.umd.edu/packages.ros.org/ros2/ubuntu/ |

### 大洋洲

| 镜像 | 国家 | URL |
|------|------|-----|
| AARNet | 澳大利亚 | https://mirror.aarnet.edu.au/pub/ros2-packages/ubuntu/ |

### 南美和非洲

目前这些地区没有官方验证的 ROS 2 镜像。

## 使用镜像

在 ``ros2-latest.list`` 文件中将 ``packages.ros.org`` 替换为镜像 URL：

```bash
# 以清华镜像为例
sudo sed -i 's|http://packages.ros.org/ros2/ubuntu|https://mirrors.tuna.tsinghua.edu.cn/ros2/ubuntu|g' /etc/apt/sources.list.d/ros2-latest.list
sudo apt update
```

## 建立镜像

ROS 基础设施使用 ``rsync`` 分发包。创建 ROS 2 仓库的本地镜像：

1. **存储要求**：确保至少有 500GB 可用磁盘空间。
2. **同步命令**：

```bash
# 同步主 ROS 2 仓库
rsync -azv rsync.osuosl.org::ros2-main /your/local/path --delete
```

3. **维护**：设置 ``cron`` 任务每 6-12 小时同步一次。

### 将镜像添加到列表

要被官方列出，镜像必须满足：
- 支持 **HTTPS**
- 至少每 24 小时同步一次
- 提供基础设施通知的联系邮箱

## 镜像 docs.ros.org

镜像文档站点需要特定配置以防止搜索引擎碎片化。如要托管文档的区域镜像，请先通过 Discourse **联系基础设施团队**。

---
[返回安装首页](index.md)
