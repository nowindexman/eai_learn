# eai-learn — 具身智能数据工程学习仓库

从 ROS bag 到训练数据集，面向具身智能数据方向的系统学习资料。

涵盖数据采集格式（rosbag1/rosbag2/MCAP）、训练数据格式（LeRobot/HDF5/RLDS）、以及从采集到训练的完整数据工程链路。

---

## 适合谁

- （Embodied AI）数据方向的工程师
- 需要处理机器人录制数据（bag/MCAP）并转换为训练数据集的研究人员
- 想系统了解 ROS 数据生态的中文学习者

## 仓库内容

```
.
├── rosbag和mcap学习计划/       # 四周基础计划：概念命令 → 编程读写 → 清洗转换 → 流水线
├── 具身智能数据开发进阶计划/    # 进阶计划：训练格式 → ROS运行时 → 规模化处理
├── rosbags包中文文档/          # rosbags Python 库文档社区翻译（Apache-2.0）
├── ROS2_Jazzy中文文档/         # ROS 2 Jazzy 官方文档社区翻译（CC-BY-3.0）
├── publish_demo.py             # ROS 1 模拟数据发布（双足灵巧手机器人抓取任务）
├── publish_demo_ros2.py        # ROS 2 版本（rclpy）
├── homework/                   # 实战练习：bag 读取、话题过滤
├── docker/                     # ROS 1 Noetic + ROS 2 Humble Docker 环境
├── 具身智能数据架构与 ROS 生态演进知识总结 .md
├── 具身智能数据格式转换全景.md
├── 具身智能数据采集的格式演进.md
├── 常见误区.md                  # MCAP 与 ROS Bag 转换常见认知误区
├── 各种info.md                 # rosbag info 输出对比
└── 【无敌】词语速查表.md        # 采集→录制→转换→清洗→训练 全链路术语表
```

## 学习路径

### 第一步：rosbag 和 MCAP 基础（四周）

> 入口：[`rosbag和mcap学习计划/总体.md`](rosbag和mcap学习计划/总体.md)

| 周次 | 主题 | 产出 |
|------|------|------|
| 第一周 | 概念与命令行 | 能用 `rosbag`/`ros2 bag`/`mcap` CLI 完成录制、回放、检查 |
| 第二周 | Python 编程读写 | 用 `rosbags` 和 MCAP SDK 读取消息、解析类型 |
| 第三周 | 同步、清洗与数据集化 | 时间戳对齐、Parquet 输出、图像抽取、Foxglove 验收 |
| 第四周 | 数据流水线 | 批量处理、可恢复执行、元数据质量与版本管理 |

### 第二步：具身智能数据进阶

> 入口：[`具身智能数据开发进阶计划/总体.md`](具身智能数据开发进阶计划/总体.md)

| 阶段 | 主题 |
|------|------|
| 第零阶段 | 概念地基：给 Web 工程师的 ML 训练 / 机器人数据 / 坐标系入门 |
| 第一阶段 | 训练数据格式：LeRobot v3、HDF5、模型数据消费接口 |
| 第二阶段 | ROS 运行时：QoS、TF 树、传感器驱动、遥操作采集 |
| 第三阶段 | 规模化：Ray 分布式、云存储、数据版本管理 |

## 快速开始

### 方式一：Docker（推荐）

```bash
# 构建并启动 ROS 2 环境
docker compose -f docker/docker-compose.yml run --rm ros2

# 或 ROS 1 环境
docker compose -f docker/docker-compose.yml run --rm ros1
```

### 方式二：本地 Python

```bash
# 安装依赖
uv sync

# 运行示例（需要自备 bag/mcap 数据文件）
python homework/bag.py
```

## 致谢

- [ROS 2 官方文档](https://docs.ros.org/en/jazzy/) — 本仓库 `ROS2_Jazzy中文文档/` 的翻译来源
- [rosbags](https://ternaris.gitlab.io/rosbags/) by Ternaris GmbH — 本仓库 `rosbags包中文文档/` 的翻译来源
- [Foxglove](https://foxglove.dev/) — MCAP 格式的联合发起方及可视化工具

## License

- 仓库原创内容（学习计划、知识总结、示例代码）采用 **[MIT License](LICENSE)**
- `ROS2_Jazzy中文文档/` 为 ROS 2 官方文档的中文翻译，遵循原许可 [CC-BY-3.0](https://creativecommons.org/licenses/by/3.0/)
- `rosbags包中文文档/` 为 rosbags 库文档的中文翻译，遵循原许可 [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
