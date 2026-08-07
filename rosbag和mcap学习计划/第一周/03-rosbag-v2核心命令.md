# 第三篇：ROS 2 rosbag2 核心命令与 MCAP

> 本文以 ROS 2 Humble、Iron、Jazzy 中都常见的能力为主。rosbag2 的命令行选项会随发行版和补丁版本变化；遇到参数报错时，先执行 `ros2 bag <verb> --help`，不要把别的发行版的命令硬套过来。
>
> **与 ROS 1 rosbag 的主要区别**：
> - **不需要 `roscore`**：ROS 2 基于 DDS（分布式发现），没有中心节点，各节点自动互相发现。
> - **输出是目录，不是文件**：`ros2 bag record` 生成一个文件夹，里面包含 `metadata.yaml` + 数据库文件（`.db3` 或 `.mcap`）。
> - **存储后端可选**：默认后端由发行版和安装的插件决定。Humble 常见默认是 `sqlite3`；Iron 起官方默认切换为 `mcap`，但实际仍应以 `ros2 bag info` 的 `Storage id` 为准。
> - **消息类型格式不同**：`geometry_msgs/Twist`（v1）→ `geometry_msgs/msg/Twist`（v2，多了 `/msg/`）。
> - **序列化格式**：v1 使用 ROS 1 序列化；ROS 2 常见为 CDR（Common Data Representation），实际值以 bag 信息中的 serialization format 为准。

#### 前置条件：启动 ROS 2 容器

```bash
# ━━━ 方式一：用 Dockerfile（推荐，已预装所有依赖） ━━━
# 首次构建镜像（约 2-3 分钟，只需一次）
docker build -t ros2-lab -f docker/Dockerfile.ros2 .
# 启动容器（source、pip、opencv、mcap 插件全部就绪）
docker run -it  --name ros2_lab -v $(pwd):/data ros2-lab
# 容器内：source 已自动写入 .bashrc，直接用
ros2 bag --help

# ━━━ 方式二：手动（原始方式） ━━━
docker run -it --name ros2_lab -v $(pwd):/data ros:humble-ros-base bash
# 容器内手动安装
source /opt/ros/humble/setup.bash
apt-get update && apt-get install -y python3-pip ros-humble-rosbag2-storage-mcap
pip3 install opencv-python-headless numpy
ros2 bag --help
```

> **注意**：用 Dockerfile 方式，`source` 已写入 `.bashrc`，新终端自动生效。手动方式每次新终端都要 `source /opt/ros/humble/setup.bash`。

#### ROS 2 消息类型格式差异

ROS 2 的消息类型路径多了 `/msg/`，这是因为 ROS 2 把消息、服务、动作分成了不同的子命名空间：

| 维度 | ROS 1 (v1) | ROS 2 (v2) |
|------|-----------|----------|
| 消息类型 | `geometry_msgs/Twist` | `geometry_msgs/msg/Twist` |
| 服务类型 | `std_srvs/SetBool` | `std_srvs/srv/SetBool` |
| 动作类型 | `actionlib_tutorials/Fibonacci` | `action_tutorials_interfaces/action/Fibonacci` |
| 序列化 | ROS 1 序列化 | ROS 2 常见为 CDR（具体以 serialization format 为准） |

```bash
# 查看消息定义（用 ros2 interface 代替 rosmsg）
ros2 interface show geometry_msgs/msg/Twist
# 输出：
#   geometry_msgs/Vector3 linear
#     float64 x
#     float64 y
#     float64 z
#   geometry_msgs/Vector3 angular
#     float64 x
#     float64 y
#     float64 z

ros2 interface show sensor_msgs/msg/JointState
ros2 interface show nav_msgs/msg/Odometry

# 搜索包含 "force" 的所有接口
ros2 interface list | grep -i force
```

> **Header 结构相同**：ROS 2 的 `std_msgs/msg/Header` 仍然有 `stamp` + `frame_id`，但定义本身**没有 ROS 1 的 `seq` 字段**；不要把 DDS 的内部序号当成 Header 时间戳的替代品。

#### 用 publish_demo_ros2.py 制造练习数据

已提供 ROS 2 版本的 `publish_demo_ros2.py`，话题列表与 v1 完全一致（14 个话题）。主要改动：

| ROS 1 (publish_demo.py) | ROS 2 (publish_demo_ros2.py) | 说明 |
|---|---|---|
| `rospy.init_node()` | `rclpy.init()` + `Node` 类 | ROS 2 用类结构 |
| `rospy.Publisher()` | `self.create_publisher()` | 需要 QoS 配置 |
| `latch=True` | `QoSDurabilityPolicy.TRANSIENT_LOCAL` | QoS 持久性策略 |
| `rospy.Rate(50)` + `rate.sleep()` | `time.sleep(1.0 / HZ)` | 见下方踩坑说明 |
| `rospy.Time.now()` | `self.get_clock().now().to_msg()` | |
| `Header.seq` | 已移除 | DDS 自带序列号 |
| `CameraInfo.D/K/R/P` | `CameraInfo.d/k/r/p` | 字段名小写 |
| `ci.data = bytes` | `ci.data = array.array('B', ...)` | ROS 2 的 `uint8[]` 用 `array.array` |

> **关于 `Rate.sleep()` 的边界**：`rclpy.Rate.sleep()` 并不是“只要手动循环就必然永久阻塞”。但如果在回调中调用它，或者没有让执行器处理所需的回调，确实可能造成等待或表现异常。教学示例若采用手动发布循环，可用 `time.sleep(1.0 / HZ)` 控制节奏；采用定时器时则交给 `rclpy.spin(node)` 运行。

```bash
# 用 Dockerfile 方式启动的容器，依赖已预装，直接运行
python3 /data/publish_demo_ros2.py

# 如果是手动方式启动的容器，需先安装依赖
apt-get update && apt-get install -y python3-pip
pip3 install opencv-python-headless numpy
source /opt/ros/humble/setup.bash
python3 /data/publish_demo_ros2.py
```

实际验证输出：
```
# 启动后日志（每 0.5 秒一条）
[INFO] [humanoid_pick_place_publisher]: === Humanoid Pick-and-Place Publisher (ROS 2, 50 Hz) ===
[INFO] [humanoid_pick_place_publisher]:     Cycle: 24.5s | States: ['IDLE', 'WALK_TO', 'REACH', 'GRASP', 'LIFT', 'WALK_BACK', 'PLACE', 'RELEASE']
[INFO] [humanoid_pick_place_publisher]: [      IDLE 0%] t=0.0s | x=0.00m | knee_l=0.20rad | ...
[INFO] [humanoid_pick_place_publisher]: [   WALK_TO 50%] t=5.0s | x=2.40m | knee_l=0.00rad | ...
[INFO] [humanoid_pick_place_publisher]: [   WALK_TO 83%] t=7.0s | x=4.00m | knee_l=0.00rad | ...

# 话题列表（14 个，与 v1 一致）
$ ros2 topic list
/camera/head/camera_info     /robot/finger_force
/camera/head/image           /robot/foot_force_left
/camera/wrist/camera_info    /robot/foot_force_right
/camera/wrist/image          /robot/hand_left/joints
/robot/cmd_vel               /robot/hand_right/joints
/robot/imu                   /robot/task_state
/robot/joint_states          /robot/odom

# 状态机正常流转
$ ros2 topic echo --once /robot/task_state
data: WALK_TO|progress=0.33
data: REACH|progress=0.33

# 频率（因图像编码开销，实测约 42Hz，对练习足够）
$ ros2 topic hz /robot/joint_states --window 30
average rate: 42.081
```

#### 录制数据：`ros2 bag record`

```bash

docker exec -it ros2_lab bash

# 录制所有话题（后端由发行版/插件决定，自动生成时间戳目录名）
ros2 bag record --all
# 生成目录：rosbag2_2026_06_05-02_13_11/
# 里面包含：metadata.yaml + rosbag2_2026_06_05-02_13_11_0.db3

# 指定输出目录名
ros2 bag record --all -o my_bag
# 生成目录：my_bag/
# 里面包含：metadata.yaml + my_bag_0.db3

# 指定 MCAP 格式存储（需要先安装 rosbag2 的 MCAP 存储插件）
ros2 bag record --all -s mcap -o my_bag_mcap
# 生成目录：my_bag_mcap/
# 里面包含：metadata.yaml + my_bag_mcap_0.mcap

# 只录指定话题
ros2 bag record /turtle1/cmd_vel /turtle1/pose -o turtle_bag

# 按大小切分（单位：字节，最小 86016 字节）
ros2 bag record --all -b 100000000 -o split_bag
# 每 100MB 自动切一个新文件：split_bag_0.db3, split_bag_1.db3, ...

# 按时间切分（单位：秒）
ros2 bag record --all -d 60 -o timed_bag
# 每 60 秒自动切一个新文件

# 边录边压缩（zstd 压缩）
ros2 bag record --all --compression-mode file --compression-format zstd -o compressed_bag
# 每个分片文件单独压缩为 .zstd

# 使用仿真时间（bag 内消息时间戳来自 /clock 话题而非系统时钟）
ros2 bag record --all --use-sim-time -o sim_bag
```

常用参数释义：
- `--all` / `-a`：录制所有话题（ROS 2 中 `-a` 和 `--all` 等价）。
- `-o`：指定输出**目录**名（不加则自动生成时间戳目录）。
- `-s` / `--storage`：指定存储后端，例如 `sqlite3` 或 `mcap`；能否使用取决于已安装插件。
- `-b`：按字节大小切分（单位字节，最小 86016）。
- `-d`：按秒数时间切分。
- `--compression-mode`：压缩模式，`file`（按文件）或 `message`（按消息）。
- `--compression-format`：压缩算法，目前只支持 `zstd`。
- `--use-sim-time`：使用 `/clock` 话题作为时间源。
- `--no-discovery`：禁止自动发现新话题（只录启动时已有的）。

> **与 v1 关键区别**：v1 用 `-O`（大写 O）指定文件名，v2 用 `-o`（小写 o）指定 bag URI。通常 v2 生成一个目录，目录中再放 `metadata.yaml` 和存储文件。

实际输出（录制过程）：
```
[INFO] [rosbag2_storage]: Opened database 'my_bag'.
[INFO] [rosbag2_transport]: Listening for topics...
[INFO] [rosbag2_transport]: Subscribed to topic '/turtle1/cmd_vel'
[INFO] [rosbag2_transport]: Subscribed to topic '/turtle1/pose'
[INFO] [rosbag2_transport]: Subscribed to topic '/parameter_events'
[INFO] [rosbag2_transport]: Subscribed to topic '/rosout'
[INFO] [rosbag2_transport]: All requested topics are subscribed. Stopping discovery...
# Ctrl+C 停止录制
[INFO] [rosbag2_cpp]: Writing remaining events to the bag. It may take a while...
```

#### 查看信息：`ros2 bag info`

```bash
ros2 bag info my_bag
```

示意输出（字段和进度显示随发行版、存储后端和版本变化）：
```
Files:             my_bag_0.db3
Bag size:          228.5 KiB
Storage id:        sqlite3
Duration:          48.47s
Start:             Jun 05 2026 02:13:24.85 (1780625604.85)
End:               Jun 05 2026 02:14:13.33 (1780625653.33)
Messages:          3013
Topic information: Topic: /turtle1/cmd_vel | Type: geometry_msgs/msg/Twist | Count: 9 | Serialization Format: cdr
                   Topic: /turtle1/pose | Type: turtlesim/msg/Pose | Count: 3004 | Serialization Format: cdr
```

#### 字段逐项解释

| 字段 | 示例值 | 含义 |
|------|--------|------|
| **Files** | `my_bag_0.db3` | 实际存储文件名。如果切分了会有多个：`_0.db3`, `_1.db3`, ... |
| **Bag size** | `228.5 KiB` | 所有存储文件的总大小 |
| **Storage id** | `sqlite3` | 实际存储后端；默认值随发行版和安装插件变化 |
| **Duration** | `48.47s` | 录制时长 = End - Start |
| **Start** | `Jun 05 2026 ... (1780625604.85)` | 第一条消息的时间戳 |
| **End** | `Jun 05 2026 ... (1780625653.33)` | 最后一条消息的时间戳 |
| **Messages** | `3013` | 所有话题消息总数 |
| **Topic** | `/turtle1/cmd_vel` | 话题名 |
| **Type** | `geometry_msgs/msg/Twist` | 消息类型（注意 v2 多了 `/msg/`） |
| **Count** | `9` | 该话题的消息条数 |
| **Serialization Format** | `cdr` | 该话题的序列化格式；ROS 2 中常见为 CDR，但不要把所有后端/版本都写死为一种格式 |

> **与 v1 的 `rosbag info` 对比**：
> - v1 输出 `path`（文件路径）、`version`（2.0）、`compression`（压缩方式）、`connections`
> - v2 输出 `Files`（目录内文件）、`Storage id`（存储后端）、`Serialization Format`
> - rosbag2 的信息展示通常不再以 ROS 1 的 `types`/MD5 区块为中心，而是展示话题类型、序列化格式和存储后端；具体字段随版本和后端变化。
> - rosbag2 的元数据模型通常按 topic/channel 展示，不要把它和 ROS 1 的 connection 统计直接等同。

#### 回放数据：`ros2 bag play`

```bash
# 正常回放（自动检测存储格式）
ros2 bag play my_bag
# 输出进度条：[rosbag2_play]: [========================] 100%

# 只回放指定话题
ros2 bag play my_bag --topics /turtle1/cmd_vel

# 排除某些话题（不同版本的选项名可能不同；此处使用较新的通用写法）
ros2 bag play my_bag --exclude '/rosout|/parameter_events'

# 用正则匹配话题（Iron/Jazzy 常见写法）
ros2 bag play my_bag --regex '/turtle1/.*'

# 排除正则匹配的话题
ros2 bag play my_bag --exclude '/rosout.*'

# 较新的发行版支持按输入 URI 合并回放；是否支持请先看本机 help
ros2 bag play -i bag1 -i bag2 -i bag3

# 通用写法是播放 bag URI 目录；部分较新的 rosbag2/存储插件也支持直接传入存储文件，
# 不要把下面写法当作所有发行版都支持的行为：
# ros2 bag play my_bag_mcap/my_bag_mcap_0.mcap
```

示意输出（字段随发行版和存储后端变化）：
```
[INFO] [rosbag2_storage]: Opened database 'my_bag'.
[rosbag2_play]: [======>                    ] 25%
```

> **与 v1 的 `rosbag play` 对比**：
> - v1 用 `--rate` 调速率，v2 也支持 `--rate`；播放过程中的暂停、恢复、下一条等控制还可通过播放器服务完成。
> - v1 用 `--start` / `--duration` 截取片段，rosbag2 常用 `ros2 bag convert` 的输入选项截取；具体参数名需按发行版确认。
> - 不同发行版的 rosbag2 播放器既可能提供键盘控制，也可能主要通过服务控制，不能把某一版本的交互方式当成全部版本的固定行为。
> - 较新的发行版支持 `-i` 传入多个 bag；这不是 Humble/Iron/Jazzy 所有补丁版本都应默认具备的能力。
> - rosbag2 也支持 `--loop` 的版本应以 `ros2 bag play --help` 为准。
> - v1 用 `--clock` 发布仿真时间，v2 用 `--clock` 参数（功能相同）
> - rosbag2 提供正则选择/排除能力，但选项名随版本变化；Iron/Jazzy 常见为 `--regex` 和 `--exclude`，应以本机帮助为准。

#### 过滤与转换：`ros2 bag convert`（v1 的 `rosbag filter` 替代方案）

Humble/Iron/Jazzy 等常见发行版没有独立的 `ros2 bag filter` 命令；过滤、切分、转换通常使用 `ros2 bag convert`，通过 YAML 配置文件控制：

##### 基本语法

```bash
# 不带高级选项时，先查看本机版本支持的参数
ros2 bag convert --help

# 使用 output_options.yaml 指定输出 URI、存储后端和 topic 选择
ros2 bag convert -i input_bag --output-options output_options.yaml
```

##### 按话题过滤（相当于 v1 的 `rosbag filter "topic == ..."`）

```bash
# 创建输出配置：只保留指定话题
cat << 'EOF' > filter_topics.yaml
output_bags:
- uri: filtered_bag
  storage_id: sqlite3
  topics: [/turtle1/cmd_vel, /turtle1/pose]
EOF

ros2 bag convert -i my_bag --output-options filter_topics.yaml
```

##### 排除话题

```bash
cat << 'EOF' > exclude_rosout.yaml
output_bags:
- uri: no_rosout_bag
  storage_id: sqlite3
  all_topics: true
  all_services: true
  exclude_topics: [/rosout, /parameter_events]
EOF

ros2 bag convert -i my_bag --output-options exclude_rosout.yaml
```

##### 格式转换：sqlite3 → mcap

```bash
cat << 'EOF' > to_mcap.yaml
output_bags:
- uri: output_mcap
  storage_id: mcap
  all_topics: true
  all_services: true
EOF

ros2 bag convert -i my_bag --output-options to_mcap.yaml
# 生成 output_mcap/ 目录，里面是 .mcap 文件
```

对 mcap CLI 支持的 ROS bag，也可以尝试直接转换；ROS 2 CDR 通常仍需要对应的 ROS 类型定义路径：
```bash
mcap convert my_bag_0.db3 output.mcap --ament-prefix-path /opt/ros/humble
```

##### 按时间截取片段

```bash
# 某些较新发行版支持用 input options 指定时间范围（纳秒级精度）；先确认本机 help
cat << 'EOF' > input_time.yaml
input_bags:
- uri: my_bag
  storage_id: sqlite3
  start_time_ns: 1780625610000000000
  end_time_ns: 1780625620000000000
EOF

cat << 'EOF' > output_time.yaml
output_bags:
- uri: time_slice
  storage_id: sqlite3
  all_topics: true
  all_services: true
EOF

ros2 bag convert -i my_bag --input-options input_time.yaml \
  --output-options output_time.yaml
```

> `--input-options` 和时间截取字段不是所有 ROS 2 发行版都同时提供。Humble/Jazzy 环境若参数不存在，应以本机 `ros2 bag convert --help` 和对应发行版文档为准，不能直接复制上面的时间截取命令。

##### 合并多个 bag

```bash
cat << 'EOF' > merge.yaml
output_bags:
- uri: merged_bag
  all_topics: true
  all_services: true
EOF

ros2 bag convert -i bag1 -i bag2 --output-options merge.yaml
```

##### 压缩输出

```bash
cat << 'EOF' > compress.yaml
output_bags:
- uri: compressed_bag
  all_topics: true
  all_services: true
  compression_mode: file
  compression_format: zstd
EOF

ros2 bag convert -i my_bag --output-options compress.yaml
```

> **与 v1 的 `rosbag filter` 对比**：
> - v1 用一行 Python 表达式做过滤，v2 需要写 YAML 配置文件
> - v1 的 `filter` 更灵活（可以按消息内容过滤），v2 的 `convert` 更强大（支持合并、切分、压缩、格式转换）
> - v1 按消息内容过滤（如 `m.pose.pose.position.x > 2.0`），v2 暂时不支持（需要用 Python 代码手动处理）

#### 更多常用命令

##### 实时查看话题：`ros2 topic`

```bash
# 列出所有话题
ros2 topic list
# 输出：/turtle1/cmd_vel, /turtle1/pose, /rosout, /parameter_events

# 查看话题的消息类型
ros2 topic type /turtle1/cmd_vel
# 输出：geometry_msgs/msg/Twist

# 实时查看消息
ros2 topic echo /turtle1/pose

# 查看发布频率
ros2 topic hz /turtle1/pose
# 输出：average rate: 62.500  min: 0.015s  max: 0.017s

# 查看话题的 QoS 配置
ros2 topic info /turtle1/cmd_vel --verbose
```

##### 实时查看节点：`ros2 node`

```bash
# 列出所有节点
ros2 node list
# 输出：
#   /turtlesim           ← turtlesim 节点
#   /teleop_turtle       ← 键盘控制节点

# 查看节点详情
ros2 node info /turtlesim
# 输出该节点的发布/订阅话题、服务、动作等
```

##### 消息字段查看：`ros2 interface`（替代 v1 的 `rosmsg`）

```bash
# 查看消息定义
ros2 interface show geometry_msgs/msg/Twist
ros2 interface show sensor_msgs/msg/JointState
ros2 interface show nav_msgs/msg/Odometry

# 列出所有可用接口
ros2 interface list

# 搜索特定接口
ros2 interface list | grep -i image
```

##### 服务调用：`ros2 service`

```bash
# 列出所有服务
ros2 service list

# 查看服务类型
ros2 service type /spawn

# 调用服务
ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.0, y: 5.0, theta: 0.0, name: ''}"

# 没有字段的服务也要显式传空请求
# ros2 service call /some_empty_service example_interfaces/srv/Trigger "{}"
```

##### 参数查看：`ros2 param`

```bash
# 列出所有参数
ros2 param list

# 查看某节点参数
ros2 param get /turtlesim background_r
```

##### 修复索引：`ros2 bag reindex`

```bash
# 尝试重建缺失或不完整的 metadata.yaml
ros2 bag reindex my_bag
```

> `reindex` 主要是恢复/重建元数据，不等于修复已经丢失或被截断的消息。执行前先复制原始目录，并用 `ros2 bag info` 验证结果。

##### 远程控制录制（rosbag2 能力；服务名称和可用版本需确认）

v2 的录制器是一个 ROS 2 节点，可以通过服务调用远程控制：

```bash
# 暂停录制
ros2 service call /rosbag2_recorder/pause rosbag2_interfaces/srv/Pause "{}"

# 恢复录制
ros2 service call /rosbag2_recorder/resume rosbag2_interfaces/srv/Resume "{}"

# 触发分片
ros2 service call /rosbag2_recorder/split_bagfile rosbag2_interfaces/srv/SplitBagfile "{}"

# 触发快照（需要先 --snapshot-mode 启动）
ros2 service call /rosbag2_recorder/snapshot rosbag2_interfaces/srv/Snapshot "{}"

# 停止录制
ros2 service call /rosbag2_recorder/stop rosbag2_interfaces/srv/Stop "{}"
```

##### 快照模式（rosbag2 能力；参数和版本需确认）

“环形缓冲区”模式，只在需要时保存最近 N 秒的数据：

```bash
# 启用快照模式；缓存大小以字节计。达到容量后保留最近写入的缓存
ros2 bag record --all --snapshot-mode --max-cache-size 104857600 -o snapshot_bag

# 需要时触发保存（另一个终端）
ros2 service call /rosbag2_recorder/snapshot rosbag2_interfaces/srv/Snapshot "{}"
# 保存当前缓存中的数据到文件
```

> **典型场景**：机器人正常运行时先把消息保存在缓存中，检测到异常/碰撞时触发保存。上面的 `--max-cache-size` 是容量上限，不保证精确对应 30 秒；较新的发行版若提供 `--max-cache-duration`，才可用时间上限表达。请先查看 `ros2 bag record --help`。

##### QoS 覆盖（ROS 2 能力；录制/回放选项需按版本确认）

ROS 2 有 QoS（服务质量）策略，录制和回放时可以覆盖：

```bash
# 创建 QoS 配置
cat << 'EOF' > qos.yaml
/turtle1/cmd_vel:
  reliability: reliable
  durability: transient_local
  depth: 10
EOF

# 录制时使用自定义 QoS
ros2 bag record --all -o qos_bag --qos-profile-overrides-path qos.yaml
```

> 当回放数据时下游节点收不到消息，通常是 QoS 不匹配导致的，需要用这个参数调整。

#### 完整命令速查表

| 命令 | 用途 | 常用参数 |
|------|------|----------|
| **录制** | | |
| `ros2 bag record --all` | 录所有话题 | `-o name` 指定目录名 |
| `ros2 bag record /topic1 /topic2` | 只录指定话题 | `-o name` 指定目录名 |
| `ros2 bag record --all -s mcap` | 用 MCAP 格式录制 | 需先装 mcap 插件 |
| `ros2 bag record --all -b 100000000` | 按大小切分 | 每 100MB 一个新文件 |
| `ros2 bag record --all -d 60` | 按时间切分 | 每 60 秒一个新文件 |
| `ros2 bag record --all --compression-mode file --compression-format zstd` | 边录边压缩 | zstd 压缩 |
| `ros2 bag record --all --use-sim-time` | 使用仿真时间 | 时间戳来自 /clock |
| `ros2 bag record --all --snapshot-mode --max-cache-size 104857600` | 快照模式 | 缓存容量以字节计；时间上限参数需看发行版 |
| **查看** | | |
| `ros2 bag info my_bag` | 查看 bag 元数据 | 时长/话题/消息数/存储后端 |
| **回放** | | |
| `ros2 bag play my_bag` | 正常回放 | 带进度条 |
| `ros2 bag play my_bag --topics /t1 /t2` | 只回放指定话题 | |
| `ros2 bag play my_bag --exclude '/rosout.*'` | 排除匹配话题 | 选项名随发行版变化 |
| `ros2 bag play my_bag --regex '/turtle1/.*'` | 正则匹配话题 | Iron/Jazzy 常见写法 |
| `ros2 bag play -i bag1 -i bag2` | 合并回放多个 bag | 较新发行版；以本机 help 为准 |
| `ros2 bag play my_bag --clock` | 发布仿真时间 | 让下游用 bag 内时间 |
| **转换** | | |
| `ros2 bag convert -i in --output-options out.yaml` | 过滤/转换/合并 | 通过 YAML 配置；参数以本机 help 为准 |
| `mcap convert in.db3 out.mcap` | 支持的 bag → MCAP | ROS 2 数据通常仍需类型支持/ament 路径 |
| **实时监控** | | |
| `ros2 topic list` | 列出所有话题 | |
| `ros2 topic echo /topic` | 实时查看消息 | |
| `ros2 topic hz /topic` | 查看发布频率 | |
| `ros2 topic type /topic` | 查看消息类型 | |
| `ros2 node list` | 列出所有节点 | |
| `ros2 node info /node` | 查看节点详情 | |
| `ros2 interface show pkg/msg/Msg` | 查看消息字段定义 | |
| **维护** | | |
| `ros2 bag reindex my_bag` | 重建 metadata.yaml | 不能恢复已丢失消息 |
| **远程控制** | | |
| `ros2 service call /rosbag2_recorder/pause ...` | 暂停录制 | |
| `ros2 service call /rosbag2_recorder/resume ...` | 恢复录制 | |
| `ros2 service call /rosbag2_recorder/snapshot ...` | 触发快照 | 需 --snapshot-mode |


---

## 第二部分：MCAP 概念与命令行深入

### 1. MCAP 是什么？为什么重要？

MCAP 是一种开放式、多模态日志容器格式，最初由 Foxglove 推动并开源。它从设计上支持机器人日志常见的 schema、channel、消息、附件和元数据记录，但“能否无 ROS 解码”仍取决于消息的编码和读取端是否有对应解码器。

- **可携带 schema**：写入端可以把类型定义一起写入文件；也允许不写 schema，所以不能看到 `.mcap` 就断言定义一定完整。
- **可索引、可定位读取**：文件可以写入摘要和索引记录，读取端可据此快速定位；没有完整索引时仍可顺序扫描，速度和随机访问能力会不同。
- **多编码支持**：同一个容器可以承载 JSON、Protobuf、FlatBuffers、ROS 1、ROS 2 CDR 等编码；编码不同，解码方式也不同。
- **流式友好**：可以边写边读，适合机器人采集、复制和上传；尚未正常 `finish` 的文件可能缺少完整摘要，需要检查或恢复。
- **分块与压缩**：支持 chunk 和压缩算法，具体压缩方式由写入端和工具参数决定。
- **跨语言**：有多种语言的实现和工具，但跨语言只解决容器读取，不自动解决 ROS CDR、Protobuf 等消息体的解码。

文件结构大致为：
```
[Magic][Header][Data records/chunks][DataEnd][Summary?][SummaryOffset][Footer][Magic]
```
其中 Summary/索引相关记录可能不存在或不完整。这样的布局允许工具对部分尾部记录缺失的文件尝试检查或恢复，但不保证崩溃后所有消息、索引和元数据都完整；恢复前应保留原始文件。

### 2. MCAP 命令行工具 `mcap`

安装后直接使用 `mcap` 命令，主要子命令：

#### `mcap info` – 查看元数据
```bash
mcap info sample.mcap
```
输出示例：
```
library: mcap
profile: x
messages: 1234
channels: 2
  (1) /odom 1000 msgs (1000.0 Hz)
  (2) /scan 234 msgs (10.0 Hz)
...
file size: 2.3 MB
```
会看到每个通道（相当于话题）的消息数量、平均频率、消息编码等。这对于数据处理系统在读取前快速判断文件内容非常有价值。

##### `profile` 字段（3 种 well-known 值）

`profile` 是 MCAP 文件 Header 中的字段，用来提示文件采用的记录约定，并不代替每个 channel 的 schema。官方注册表定义了 **3 种 well-known profile**：

| profile 值 | 说明 | message_encoding | schema encoding |
|---|---|---|---|
| `""` (空字符串) | 通用/不指定 | 无限制 | 无限制 |
| `ros1` | ROS 1 规范 | 通常为 `ros1` | 通常为 `ros1msg` |
| `ros2` | ROS 2 规范 | 通常为 `cdr` | 常见为 `ros2msg` / `ros2idl` / `omgidl` |

规范也允许填入自定义值（非 well-known），但读取端可能不认识。

##### `library` 字段（自由格式，无固定枚举）

`library` 是一个**自由格式字符串**，由写入 MCAP 文件的库自行填写，用于调试目的。官方规范没有固定枚举，但主要有以下官方/常见实现：

| 语言 | 库名示例 |
|---|---|
| C++ | `mcap-cpp-x.x.x` |
| Python（官方） | `mcap-x.x.x` |
| Go | `mcap-go-x.x.x` |
| TypeScript | `@mcap/core-x.x.x` |
| Swift | `mcap-swift-x.x.x` |
| Rust | `mcap-x.x.x` |
| Python（第三方） | `rosbags-x.x.x` |

> 例如 `mcap info` 输出 `library: rosbags-0.11.1`，说明该文件是用第三方 Python `rosbags` 库写入的，而非 Foxglove 官方的 `mcap` Python 库。

#### `mcap cat` – 输出消息内容
```bash
# 只输出某个或多个通道；当前 CLI 使用复数参数，值为逗号分隔列表
mcap cat sample.mcap --topics /odom

# 对支持 JSON 输出的编码打印 JSON Lines，并限制行数
mcap cat sample.mcap --topics /odom --json | head -n 5
```
`--json` 不是任意编码的通用反序列化器。当前 CLI 只对部分编码（例如 `ros1`、`protobuf`、`json`）提供 JSON 输出；ROS 2 常见的 `cdr` 不能直接靠这个选项变成可读 JSON，应使用 ROS 类型支持、`rosbags` 或其他对应解码器。

#### `mcap filter` – 按条件切出新文件
```bash
# 只保留 /odom 通道，生成 new.mcap；-y 的值是话题正则表达式
mcap filter sample.mcap -o new.mcap -y '^/odom$'

# 保留多个通道，并限定时间范围；--start/--end 可使用纳秒时间戳
mcap filter big.mcap -o slice.mcap -y '^/odom$' -y '^/tf$' \
    --start 1600000000000000000 --end 1600000010000000000
```
`mcap filter` 主要按话题正则和日志时间过滤，不是按消息字段内容过滤；输出是否保留附件、metadata 也受版本和选项影响。它会生成新文件，不修改输入文件。

#### `mcap compress` / `decompress` – 压缩与解压
```bash
mcap compress uncompressed.mcap -o compressed.mcap --compression zstd
mcap decompress compressed.mcap -o original.mcap
```

#### `mcap list schemas` – 查看文件中注册的 schema
```bash
mcap list schemas sample.mcap
```
这对理解数据格式、转换成其他系统（如 Parquet）时很有帮助。

#### `mcap doctor` 与 `mcap recover`：结构检查和尽力恢复

```bash
# 检查 MCAP 记录结构；它不是业务语义质量检查
mcap doctor sample.mcap

# 对疑似未正常收尾的文件尝试恢复，输出到新文件
mcap recover broken.mcap -o recovered.mcap
```

恢复成功只表示工具能重新组织可读记录，不表示损坏前的所有消息一定都找回来了；恢复后的文件仍需用 `mcap info`、`mcap doctor` 和实际解码验证。

### 3. 如何获取 MCAP 文件进行练习？

Foxglove 提供了许多示例 MCAP 文件，可以直接下载：
```bash
# 下载一个包含传感器数据的 MCAP
wget https://github.com/foxglove/mcap/raw/main/tests/conformance/data/OneMessage/OneMessage.mcap

# 查看信息
mcap info OneMessage.mcap
mcap cat OneMessage.mcap
```
也可以在 Foxglove Studio 中直接拖放查看，直观地看到里面的图像、点云等。
