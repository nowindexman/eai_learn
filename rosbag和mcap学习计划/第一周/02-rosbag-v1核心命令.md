### 2. rosbag v1 核心命令

> **前置条件**：rosbag v1 的所有命令都依赖 `roscore`（ROS 主节点）。先启动容器，后台运行 roscore，再执行后续操作。
> 否则会报 `Failed to contact master at [localhost:11311]`。

```bash
# ━━━ 方式一：用 Dockerfile（推荐，已预装所有依赖） ━━━
# 首次构建镜像（约 2-3 分钟，只需一次）
docker build -t ros1-lab -f docker/Dockerfile.ros1 .
# 启动容器（source、pip、opencv 全部就绪）
docker run -it  --name ros1_lab -v $(pwd):/data ros1-lab
# 容器内：source 已自动写入 .bashrc，直接启动 roscore
roscore &
sleep 2

# ━━━ 方式二：手动（原始方式） ━━━
docker run -it --name ros1_lab -v $(pwd):/data ros:noetic-ros-base bash
# 容器内手动安装依赖
apt-get update && apt-get install -y python3-pip && pip3 install opencv-python-headless numpy
source /opt/ros/noetic/setup.bash
roscore &
sleep 2
```

#### ROS 消息通用结构（用 `rosmsg show` 查看）

用 `rosmsg show` 可以查看任何消息类型的完整字段定义：
```bash
rosmsg show sensor_msgs/JointState
rosmsg show sensor_msgs/CompressedImage
rosmsg show nav_msgs/Odometry
```

##### 基本数据类型

| ROS 类型 | 对应 Python | 对应 C++ | 说明 |
|---------|-----------|---------|------|
| `bool` | `bool` | `bool` | 真/假 |
| `int8` / `uint8` | `int` | `int8_t` / `uint8_t` | 8 位整数，uint8 也用于表示字节数据 |
| `int16` / `uint16` | `int` | `int16_t` / `uint16_t` | 16 位整数 |
| `int32` / `uint32` | `int` | `int32_t` / `uint32_t` | 32 位整数 |
| `int64` / `uint64` | `int` | `int64_t` / `uint64_t` | 64 位整数 |
| `float32` | `float` | `float` | 单精度浮点 |
| `float64` | `float` | `double` | 双精度浮点（ROS 中角度/位置默认用这个） |
| `string` | `str` | `std::string` | 字符串 |
| `time` | `rospy.Time` | `ros::Time` | 时间戳（secs + nsecs） |
| `duration` | `rospy.Duration` | `ros::Duration` | 时间间隔（secs + nsecs） |

##### 数组类型

```bash
# 动态数组（长度可变）
float64[] position    # ← JointState 的关节角度，长度 = 关节数
string[] name         # ← 关节名称列表
uint8[] data          # ← CompressedImage 的图像字节

# 固定数组（长度写死）
float64[36] covariance  # ← Odometry 的协方差矩阵，6×6 展平 = 36 个元素
float64[9] K            # ← CameraInfo 的内参矩阵，3×3 展平 = 9 个元素
float64[12] P           # ← CameraInfo 的投影矩阵，3×4 展平 = 12 个元素
```

##### 通用结构：`std_msgs/Header`

几乎所有 ROS 消息都包含一个 `header` 字段，它是消息的“身份证”：

```bash
std_msgs/Header header
  uint32 seq          # 消息序号，自增（第几条消息）
  time stamp          # 时间戳（精确到纳秒）
  string frame_id     # 坐标系名称（数据是在哪个参考系下测量的）
```

**三个字段的作用：**

| 字段 | 作用 | 示例 |
|------|------|------|
| `seq` | 消息序号，用于检测丢包 | `0, 1, 2, ... 2465` |
| `stamp` | 时间戳，用于多传感器时间对齐 | `1780625604.850000000` |
| `frame_id` | 坐标系，用于 TF 坐标变换 | `"odom"`, `"base_link"`, `"head_camera_link"` |

**frame_id 详解 + TF 坐标变换：**

`frame_id` **不是随便写的**，它是传感器在机器人身上的坐标系名称，必须在整个系统里保持一致。

```
机器人身上每个传感器都有自己的“位置”：

  头部 ── 相机（frame_id: "head_camera_link"）
  躯干 ── IMU（frame_id: "torso_imu"）
  手腕 ── 相机（frame_id: "wrist_camera_link"）
  底盘 ── 激光雷达（frame_id: "base_laser"）
```

消息里的 `frame_id` 就填它自己的名字：
```python
img_msg.header.frame_id = "head_camera_link"  # "这张图是从 head_camera_link 位置拍的"
imu_msg.header.frame_id = "torso_imu"          # "这个加速度是在 torso_imu 位置测的"
```

所有 `frame_id` 通过 **TF（Transform，坐标变换）树** 关联在一起：
```
TF 树：

  map                    ← 世界坐标系（地图原点）
   │
  odom                   ← 里程计（机器人起始位置）
   │
  base_link              ← 躯干中心
   ├── torso_imu         ← IMU（在 base_link 上方 0.5m）
   ├── head_link         ← 头部（在 base_link 上方 1.5m）
   │    └── head_camera_link  ← 头部相机（在 head 前方 0.1m）
   ├── r_arm_link        ← 右臂
   │    └── wrist_camera_link ← 手腕相机（在右臂末端前方 0.05m）
   └── base_laser        ← 激光雷达（在 base_link 前方 0.2m）
```

**TF 树解决什么问题？**——“头部相机看到的东西，在底盘坐标系下是哪个位置？”
```
相机说：“杯子在我前方 0.5m”（相对于 head_camera_link）
TF 换算：head_camera_link → head_link → base_link
结果：杯子在底盘前方 0.6m、上方 1.5m
```

**frame_id 可以随便写吗？**

| 场景 | 能不能随便写 | 后果 |
|------|------------|------|
| 只录 bag 不做坐标变换 | 可以 | bag 能正常回放 |
| 要给 rviz 可视化 | 不行 | TF 对不上，模型散架 |
| 要做多传感器融合 | 不行 | 坐标换算出错 |
| 训练 AI 模型 | 可以 | 训练不用 TF |

> 具身智能行业有标准命名约定：`base_link`、`odom`、`head_camera_link`、`wrist_camera_link` 等，大部分公司都这么叫。

**哪些消息有 Header，哪些没有：**

| 消息类型 | 有 Header | 原因 |
|---------|---------|------|
| `sensor_msgs/Imu` | ✅ | 传感器数据必须有时间戳 |
| `sensor_msgs/JointState` | ✅ | 关节状态必须有时间戳 |
| `sensor_msgs/CompressedImage` | ✅ | 图像必须有时间戳 |
| `nav_msgs/Odometry` | ✅ | 里程计需要时间戳 + 坐标系 |
| `geometry_msgs/Twist` | ❌ | 纯速度指令，不需要时间戳 |
| `std_msgs/String` | ❌ | 简单文本，不需要 |
| `std_msgs/Float64` | ❌ | 单个数值，不需要 |

> **规则**：带时间、空间属性的传感器数据都有 Header；简单的控制指令、状态文本通常没有。

##### 实际例子对比

```bash
# JointState（带 Header，有数组）
$ rosmsg show sensor_msgs/JointState
  std_msgs/Header header     ← 有 header
    uint32 seq
    time stamp
    string frame_id
  string[] name              ← 关节名称列表（动态数组）
  float64[] position         ← 关节角度（动态数组）
  float64[] velocity         ← 关节速度（动态数组）
  float64[] effort           ← 关节力矩（动态数组）

# CompressedImage（带 Header，有字节数组）
$ rosmsg show sensor_msgs/CompressedImage
  std_msgs/Header header     ← 有 header
    uint32 seq
    time stamp
    string frame_id
  string format              ← 压缩格式（"jpeg" / "png"）
  uint8[] data               ← 图片二进制数据（字节数组）

# Twist（无 Header，纯数据）
$ rosmsg show geometry_msgs/Twist
  geometry_msgs/Vector3 linear   ← 无 header，只有 x/y/z
    float64 x
    float64 y
    float64 z
  geometry_msgs/Vector3 angular  ← 角速度 x/y/z
    float64 x
    float64 y
    float64 z
```

##### 嵌套类型

消息可以嵌套其他消息类型，像俄罗斯套娃：

```
nav_msgs/Odometry
  └── geometry_msgs/PoseWithCovariance pose
        ├── geometry_msgs/Pose pose          ← 嵌套 Pose
        │     ├── Point position             ← 嵌套 Point
        │     └── Quaternion orientation     ← 嵌套 Quaternion
        └── float64[36] covariance
  └── geometry_msgs/TwistWithCovariance twist
        ├── geometry_msgs/Twist twist        ← 嵌套 Twist
        └── float64[36] covariance
```

> 在 Python 中访问：`msg.pose.pose.position.x`，就是层层点进去。

#### 制造练习数据：用 Python 发布话题

为了有东西可录，使用 `publish_demo.py`（放在挂载目录下）。这是一个完整的双足灵巧手机器人模拟器，包含 14 个话题：

| 话题 | 消息类型 | 频率 | 说明 |
|------|----------|------|------|
| `/robot/odom` | `Odometry` | 50Hz | 躯干里程计 |
| `/robot/imu` | `Imu` | 50Hz | 躯干 IMU |
| `/robot/joint_states` | `JointState` | 50Hz | 腿+臂 26 关节 |
| `/robot/hand_left/joints` | `JointState` | 50Hz | 左手 15 关节 |
| `/robot/hand_right/joints` | `JointState` | 50Hz | 右手 15 关节 |
| `/robot/foot_force_left` | `WrenchStamped` | 50Hz | 左足底力 |
| `/robot/foot_force_right` | `WrenchStamped` | 50Hz | 右足底力 |
| `/robot/finger_force` | `JointState` | 50Hz | 指尖力 |
| `/robot/cmd_vel` | `Twist` | 50Hz | 行走速度指令 |
| `/robot/task_state` | `String` | 1Hz | 任务阶段 |
| `/camera/head/image` | `CompressedImage` | 10Hz | 头部 RGB 相机（JPEG） |
| `/camera/head/camera_info` | `CameraInfo` | 10Hz | 头部相机内参 |
| `/camera/wrist/image` | `CompressedImage` | 10Hz | 手腕相机（JPEG） |
| `/camera/wrist/camera_info` | `CameraInfo` | 10Hz | 手腕相机内参 |

机器人会循环执行「走过去 → 伸手 → 抓握 → 抬起 → 走回来 → 放下 → 松手」完整任务。用 OpenCV 生成模拟图像：
- **头部相机**：前方场景，可见目标物体（绿色方块），抓起后变黄
- **手腕相机**：手部特写，可见 5 根手指开合、抓握力显示

> 完整代码见仓库中的 `publish_demo.py`，下面只展示关键片段。

#### 录制数据：`rosbag record`

```bash
# 先后台启动录制，再运行发布脚本
nohup rosbag record -a -O /data/demo.bag > /tmp/rosbag.log 2>&1 &
sleep 1
python3 /data/publish_demo.py
# Ctrl+C 停止发布，然后停掉录制
pkill -f 'rosbag record'
```

也可以手动分步操作：
```bash
# 进入容器
docker exec -it ros1_lab bash

# 录制所有话题 
# 没结束之前都是 zyw_2026-06-05-02-13-11.bag.active 这种形态的 
# 结束之后才会去掉active
rosbag record -a

# 录制指定话题，输出文件名由 -O 指定
rosbag record -O my_record.bag /sensor/status /sensor/temperature

# 录制时自动切分：每200MB或每10分钟切一个文件
rosbag record --split --size=200 --duration=10m /scan
```

常用参数释义：
- `-a`：录制所有正在发布的话题。
- `-O`：指定输出文件名（不加 .bag 会自动补上）。
- `--split`：按大小或时间切分，适合长时间采集。
- `--duration=10m`：录制10分钟后自动停止。
- `-j`：压缩（`bz2` 或 `lz4`），后面会提到。

#### 查看信息：`rosbag info`

```bash
# 先停掉录制进程
pkill -f 'rosbag record'

rosbag info /data/demo.bag
```

输出会显示：
- 文件路径、版本、持续时间、文件大小。
- 话题列表，每个话题的消息数量、类型、平均频率。
- 各话题的时间戳范围（起止时间）。

际输出（14 个话题完整录制）：
```
path:        zyw_2026-06-05-02-13-11.bag
version:     2.0
duration:    49.8s
start:       Jun 05 2026 02:13:24.85 (1780625604.85)
end:         Jun 05 2026 02:14:14.68 (1780625654.68)
size:        13.8 MB
messages:    24374
compression: none [18/18 chunks]
types:       geometry_msgs/Twist         [9f195f881246fdfa2798d1d3eebca84a]
             geometry_msgs/WrenchStamped [d78d3cb249ce23087ade7e7d0c40cfa7]
             nav_msgs/Odometry           [cd5e73d190d741a2f92e81eda573aca7]
             rosgraph_msgs/Log           [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/CameraInfo      [c9a58c1b0b154e0e6da7578cb991d214]
             sensor_msgs/CompressedImage [8f7a12909da2c9d3332d540a0977563f]
             sensor_msgs/Imu             [6a62c6daae103f4ff57a132d6f95cec2]
             sensor_msgs/JointState      [3066dcd76a6cfaef579bd0f34173e9fd]
             std_msgs/String             [992ce8a1687cec8c8bd883ec73ca41d1]
topics:      /camera/head/camera_info     483 msgs    : sensor_msgs/CameraInfo
             /camera/head/image           493 msgs    : sensor_msgs/CompressedImage
             /camera/wrist/camera_info    483 msgs    : sensor_msgs/CameraInfo
             /camera/wrist/image          493 msgs    : sensor_msgs/CompressedImage
             /robot/cmd_vel              2414 msgs    : geometry_msgs/Twist
             /robot/finger_force         2466 msgs    : sensor_msgs/JointState
             /robot/foot_force_left      2466 msgs    : geometry_msgs/WrenchStamped
             /robot/foot_force_right     2466 msgs    : geometry_msgs/WrenchStamped
             /robot/hand_left/joints     2467 msgs    : sensor_msgs/JointState
             /robot/hand_right/joints    2466 msgs    : sensor_msgs/JointState
             /robot/imu                  2467 msgs    : sensor_msgs/Imu
             /robot/joint_states         2466 msgs    : sensor_msgs/JointState
             /robot/odom                 2466 msgs    : nav_msgs/Odometry
             /robot/task_state             50 msgs    : std_msgs/String
             /rosout                      114 msgs    : rosgraph_msgs/Log  (2 connections)
             /rosout_agg                  114 msgs    : rosgraph_msgs/Log  (2 connections)
```

#### 字段逐项解释

| 字段 | 示例值 | 含义 |
|------|--------|------|
| **path** | `zyw_2026-06-05-...bag` | 文件路径。`zyw` 是 `-O` 指定的前缀，后自动加时间戳 |
| **version** | `2.0` | bag 格式版本。ROS 1 固定为 2.0（v1.0 是远古版本） |
| **duration** | `49.8s` | 录制时长 = end - start。约 2 个完整任务循环 |
| **start** | `Jun 05 2026 ... (1780625604.85)` | 第一条消息的时间戳：人类可读 + Unix 时间戳 |
| **end** | `Jun 05 2026 ... (1780625654.68)` | 最后一条消息的时间戳 |
| **size** | `13.8 MB` | 文件体积，包含消息数据 + 索引 + 消息定义 |
| **messages** | `24374` | 所有话题的消息条数之和 |
| **compression** | `none [18/18 chunks]` | 压缩方式。`none`=未压缩，`18/18`=共 18 个 chunk 全未压缩。chunk 是 bag 内部存储单元，默认约 768KB/个。用 `--lz4` 或 `--bz2` 可启用压缩 |
| **types** | `geometry_msgs/Twist [9f195f...]` | 用到的所有消息类型 + MD5 校验和。MD5 由消息定义文件计算，**同一版本 ROS 全球统一不变**，用于防止类型不匹配 |
| **topics** | 每行一个话题 | 话题名、消息数、消息类型 |
| **msgs** | `2466 msgs` | 该话题在录制期间收到的总消息数 |
| **(N connections)** | `(2 connections)` | 有多少个不同节点向该话题发布消息。没标注=默认 1 个。`/rosout` 有 2 个：publish_demo.py + rosbag 自身 |

#### 消息数反推频率

用 `消息数 ÷ 时长(49.8s)` 可验证实际发布频率：

| 话题 | 消息数 | 实际频率 | 预期 |
|------|--------|---------|------|
| /robot/odom | 2466 | 49.5 Hz | 50 Hz |
| /robot/joint_states | 2466 | 49.5 Hz | 50 Hz |
| /camera/head/image | 493 | 9.9 Hz | 10 Hz |
| /robot/task_state | 50 | 1.0 Hz | 1 Hz |
| /rosout | 114 | 2.3 Hz | ~2 Hz |

基本符合预期，略有波动是因为 Docker 容器不是实时系统。

> **注意**：`/rosout` 和 `/rosout_agg` 是 ROS 系统自动产生的日志话题，每个节点的 `rospy.loginfo()` 都会发到 `/rosout`，`/rosout_agg` 是其聚合版本。

#### 回放数据：`rosbag play` 就是在后台发布消息

```bash
# 正常速度回放
rosbag play /data/demo.bag

# 5倍速回放，只发布传感器话题
rosbag play /data/demo.bag --rate=5 --topics /sensor/status /sensor/temperature

# 从第30秒开始，播放5秒内容
rosbag play my_record.bag --start=30 --duration=5
```

实际输出：
```
[INFO] Opening /data/demo.bag
Waiting 0.2 seconds after advertising topics... done.
Hit space to toggle paused, or 's' to step.
 [RUNNING]  Bag Time: 1780563043.094985   Duration: 7.025778 / 7.999795
Done.
```

回放时，消息会按录制时的相对时间间隔重新发布到 ROS 网络中，就像时光倒流一样。

#### 过滤：`rosbag filter`

按条件从已有 bag 中生成新文件。条件是一个 **Python 表达式**，可用的变量：

| 变量 | 类型 | 含义 |
|------|------|------|
| `topic` | `str` | 话题名，如 `'/robot/odom'` |
| `t` | `genpy.Time` | 消息时间戳，`t.secs` + `t.nsecs` |
| `m` | `ROS 消息` | 消息本身，可访问 `m.data`、`m.position` 等字段 |

##### 按话题过滤

```bash
# 只保留单个话题
rosbag filter demo.bag odom_only.bag "topic == '/robot/odom'"

# 保留多个话题
rosbag filter demo.bag sensors.bag "topic in ['/robot/imu', '/robot/joint_states']"

# 排除某些话题（用 not）
rosbag filter demo.bag no_rosout.bag "not topic.startswith('/rosout')"

# 只保留相机相关话题
rosbag filter demo.bag cameras.bag "topic.startswith('/camera/')"

# 只保留机器人相关话题
rosbag filter demo.bag robot_only.bag "topic.startswith('/robot/')"
```

##### 按时间过滤

```bash
# 只保留前 10 秒的数据
rosbag filter demo.bag first_10s.bag "t.secs - 1780625604 < 10"
# 注意：1780625604 是 bag 的 start 时间戳，用 rosbag info 查看

# 保留第 10 秒到第 30 秒
rosbag filter demo.bag middle.bag "10 <= (t.secs - 1780625604) <= 30"

# 保留偶数秒的数据（降采样）
rosbag filter demo.bag even_secs.bag "t.secs % 2 == 0"
```

##### 按消息内容过滤

```bash
# 只保留任务状态为 WALK_TO 的消息
rosbag filter demo.bag walking.bag "topic == '/robot/task_state' and 'WALK_TO' in m.data"

# 只保留里程计 x > 2.0 的消息（机器人走到 2m 以后）
rosbag filter demo.bag far.bag "topic == '/robot/odom' and m.pose.pose.position.x > 2.0"

# 只保留有抓握力的指尖力消息
rosbag filter demo.bag gripping.bag "topic == '/robot/finger_force' and any(e > 5.0 for e in m.effort)"
```

##### 组合条件

```bash
# 只保留行走阶段的关节数据（按时间 + 话题组合）
rosbag filter demo.bag walk_joints.bag \
  "topic.startswith('/robot/') and 2 <= (t.secs - 1780625604) <= 8"

# 保留传感器数据但排除日志（多条件）
rosbag filter demo.bag clean.bag \
  "not topic.startswith('/rosout') and topic.startswith('/robot/')"

# 抽取抓取阶段所有数据（精确时间窗口）
rosbag filter demo.bag grasp_phase.bag \
  "8 <= (t.secs - 1780625604) <= 13 and topic.startswith('/robot/')"
```

##### 实际例子——过滤效果对比

```bash
# 原始 bag：13.8 MB，24374 条消息，14 个话题
rosbag info demo.bag

# 只保留关节数据：约 2 MB，~7400 条消息，3 个话题
rosbag filter demo.bag joints_only.bag "topic in ['/robot/joint_states', '/robot/hand_left/joints', '/robot/hand_right/joints']"

# 只保留相机图像：约 10 MB，~986 条消息，2 个话题
rosbag filter demo.bag images_only.bag "topic.endswith('/image')"

# 去掉图像后：约 3 MB，~23000 条消息，12 个话题
rosbag filter demo.bag no_images.bag "not '/image' in topic and not '/camera_info' in topic"
```

> **经验**：图像话题占 bag 体积的 70-90%，但消息数只占 2-5%。做数据分析时通常先 filter 掉图像减小体积，需要时再单独提取。

#### 更多常用命令

##### 文件检查：`rosbag check`

检查 bag 文件是否与当前 ROS 版本兼容（消息类型定义是否需要迁移）：
```bash
rosbag check demo.bag
```
输出示例（正常，不需要迁移）：
```
Bag file does not need any migrations.
```
输出示例（有问题，消息定义发生了变化）：
```
The following migrations need to occur:
  from: sensor_msgs/JointState  [old_md5]
  to:   sensor_msgs/JointState  [new_md5]
```
> 通常在 ROS 版本升级后消息定义变了才会出现。日常采集不会遇到。

##### 压缩与解压：`rosbag compress` / `decompress`

```bash
# 压缩为 lz4（推荐，速度快，压缩率约 40-60%）
rosbag compress --lz4 demo.bag
# 压缩后的文件覆盖原文件名 demo.bag
# 压缩前的原始文件被重命名为 demo.orig.bag（orig = original）

# 压缩为 bz2（压缩率更高，但慢）
rosbag compress --bz2 demo.bag

# 不保留原始文件（省空间，直接覆盖）
rosbag compress --lz4 --force demo.bag
# 不生成 .orig.bag，压缩后直接覆盖原文件

# 解压（play 也能自动解压，一般不需要手动解压） 解压也会生成新的 .bag 文件和orig文件
rosbag decompress demo.bag.lz4.bag
```
> **`.orig.bag` 是什么？** `orig` = **original**（原始的）。`rosbag compress` 默认会把压缩前的文件重命名为 `.orig.bag` 作为备份，压缩后的文件使用原文件名。这是 Unix/Linux 世界的常见惯例（`patch`、`sed -i` 等工具也用 `.orig` 表示原始版本）。
>
> **实际经验**：50Hz 的 56 关节 + 双相机，1 分钟原始数据约 20-30 MB，lz4 压缩后约 8-12 MB。

##### 修复索引：`rosbag reindex`

录制过程中容器崩溃或 `kill -9` 强杀，bag 索引可能没写完：
```bash
# 修复损坏的 bag 文件
rosbag reindex broken.bag
# 生成 broken.bag.reindex.bag，原文件保留

# 修复后验证
rosbag info broken.bag.reindex.bag
```

##### 实时查看话题：`rostopic`

录制过程中实时监控：
```bash
# 查看某话题的实时消息（每秒刷新）
rostopic echo /robot/task_state

# 查看某话题的实际发布频率
rostopic hz /robot/joint_states
# 输出：average rate: 49.987  min: 0.019s  max: 0.021s

# 列出所有正在发布的话题
rostopic list

# 查看某话题的消息类型
rostopic type /robot/odom
# 输出：nav_msgs/Odometry

# 查看某话题一条消息的完整字段
rostopic echo /robot/odom --noarr  # --noarr 省略数组，输出更简洁
```

##### 实时查看节点：`rosnode`

```bash
# 列出所有运行中的节点
rosnode list
# 输出：
#   /humanoid_pick_place_publisher   ← 你的 publish_demo.py
#   /rosout                           ← roscore 自带的

# 查看某节点的详细信息
rosnode info /humanoid_pick_place_publisher
```

##### 查看参数服务器：`rosparam`

```bash
# 列出所有参数
rosparam list

# 读取某参数
rosparam get /run_id
```

##### 消息字段查看：`rosmsg`

不用打开源码就能看任何消息类型的完整定义：
```bash
# 查看 Odometry 的全部字段
rosmsg show nav_msgs/Odometry

# 查看 Imu 的全部字段
rosmsg show sensor_msgs/Imu

# 搜索包含 "force" 的所有消息类型
rosmsg packages | grep -i force
```

##### 服务调用：`rosservice`

```bash
# 列出所有可用的服务
rosservice list

# 调用某服务（例如清空参数）
rosservice call /service_name "args"
```

##### 时间相关（通过 `rosparam`）

> 注意：ROS 1 没有独立的 `rostime` 命令，时间相关操作通过 `rosparam` 完成。

```bash
# 查看是否使用仿真时间（默认 false，使用系统时间）
rosparam get /use_sim_time

# 查看当前系统时间（Linux 自带命令）
date

# rosbag play 时发布仿真时间
rosbag play demo.bag --clock
# 此时 rostopic echo /clock 会输出 bag 内的时间，而非系统时间
```
> `--clock` 在回放数据给其他节点处理时非常有用，让下游算法以为在真实运行。

##### 话题录制高级技巧

```bash
# 排除某些话题（不录 /rosout）
rosbag record -a -x '/rosout.*' -O clean_demo.bag

# 只录指定话题
rosbag record /robot/joint_states /camera/head/image -O joints_cam.bag

# 延迟 5 秒后开始录（等待系统稳定）
rosbag record -a --pause -O delayed.bag
# 然后另一个终端：rosservice call /record/start

# 限制最大录制时长
rosbag record -a --duration=30 -O short_demo.bag

# 录制时启用 lz4 压缩（边录边压）
rosbag record -a -j --lz4 -O compressed_demo.bag
```

##### 回放高级技巧

```bash
# 只回放指定话题
rosbag play demo.bag --topics /robot/joint_states /robot/imu

# 从第 10 秒开始，播放 5 秒
rosbag play demo.bag --start=10 --duration=5

# 慢速回放（0.5 倍速，方便观察）
rosbag play demo.bag --rate=0.5

# 循环回放
rosbag play demo.bag --loop

# 使用仿真时间（让下游节点以为在真实运行）
rosbag play demo.bag --clock

# 交互式回放（空格暂停，s 单步）
rosbag play demo.bag
# 输出：Hit space to toggle paused, or 's' to step.
```

#### 完整命令速查表

| 命令 | 用途 | 常用参数 |
|------|------|----------|
| **录制** | | |
| `rosbag record -a` | 录所有话题 | `-O name` 指定文件名 |
| `rosbag record /topic1 /topic2` | 只录指定话题 | `-O name` 指定文件名 |
| `rosbag record -a -x '/rosout.*'` | 录所有但排除某些 | `-x` 正则排除 |
| `rosbag record -a --split --size=200` | 按大小切分 | 每 200MB 一个新文件 |
| `rosbag record -a --duration=30` | 限时录制 | 30 秒后自动停止 |
| `rosbag record -a -j --lz4` | 边录边压缩 | 节省磁盘空间 |
| **查看** | | |
| `rosbag info demo.bag` | 查看 bag 元数据 | 时长/话题/消息数/大小 |
| `rosbag check demo.bag` | 检查文件完整性 | 验证 MD5 是否匹配 |
| **回放** | | |
| `rosbag play demo.bag` | 正常回放 | 空格暂停，s 单步 |
| `rosbag play demo.bag --rate=5` | 5 倍速回放 | |
| `rosbag play demo.bag --start=10 --duration=5` | 片段回放 | 从第 10 秒开始，放 5 秒 |
| `rosbag play demo.bag --topics /t1 /t2` | 只回放指定话题 | |
| `rosbag play demo.bag --loop` | 循环回放 | |
| `rosbag play demo.bag --clock` | 发布仿真时间 | 让下游用 bag 内时间 |
| **过滤** | | |
| `rosbag filter in.bag out.bag "条件"` | 按条件过滤 | 条件是 Python 表达式 |
| 常用条件 | `"topic == '/robot/odom'"` | 只保留某话题 |
| | `"t.secs > 10 and t.secs < 20"` | 只保留时间段 |
| | `"topic in ['/t1', '/t2']"` | 保留多个话题 |
| **维护** | | |
| `rosbag compress --lz4 demo.bag` | 压缩文件 | 生成 .lz4.bag |
| `rosbag decompress demo.bag` | 解压文件 | |
| `rosbag reindex broken.bag` | 修复索引 | 处理崩溃中断的 bag |
| **实时监控** | | |
| `rostopic list` | 列出所有话题 | |
| `rostopic echo /topic` | 实时查看消息 | `--noarr` 省略数组 |
| `rostopic hz /topic` | 查看发布频率 | |
| `rostopic type /topic` | 查看消息类型 | |
| `rosnode list` | 列出所有节点 | |
| `rosnode info /node` | 查看节点详情 | |
| `rosmsg show pkg/Msg` | 查看消息字段定义 | |

