# 01：ROS 2 QoS 与实时通信

> 你在第一周学过 `ros2 bag record` 录制数据。但你有没有遇到过"话题明明在发布，录制后却发现消息数远少于预期"？这通常是 QoS（服务质量）配置不匹配导致的。理解 QoS 是诊断数据采集问题的第一道关。

## 1. 什么是 QoS

ROS 2 基于 DDS（Data Distribution Service）中间件。DDS 提供了 QoS 策略来控制消息传递的行为——可靠性、持久性、历史保留等。ROS 2 把这些策略暴露给了上层节点。

**核心问题**：发布者和订阅者各自有自己的 QoS 设置，**两者必须兼容**才能通信。不兼容时，DDS 会静默丢弃消息——你不会收到任何错误提示，只是消息数量变少或为零。

## 2. 五个核心 QoS 策略

### 2.1 Reliability（可靠性）

| 值 | 行为 | 适用场景 |
|---|---|---|
| `RELIABLE` | 保证消息到达，丢失会重传 | 控制命令、动作目标、关键状态 |
| `BEST_EFFORT` | 尽力而为，丢失不重传 | 传感器数据（图像、IMU、点云） |

**兼容性规则**：发布者 `RELIABLE` 可以匹配订阅者 `RELIABLE` 或 `BEST_EFFORT`；发布者 `BEST_EFFORT` 只能匹配订阅者 `BEST_EFFORT`。

```text
Publisher RELIABLE    + Subscriber RELIABLE     → ✅ 通信
Publisher RELIABLE    + Subscriber BEST_EFFORT  → ✅ 通信
Publisher BEST_EFFORT + Subscriber RELIABLE     → ❌ 不通信！
Publisher BEST_EFFORT + Subscriber BEST_EFFORT  → ✅ 通信
```

> 最常见的坑：相机驱动用 `BEST_EFFORT`（因为丢一帧无所谓），但 `ros2 bag record` 默认用 `RELIABLE`，导致录制时收不到图像。

### 2.2 Durability（持久性）

| 值 | 行为 | 适用场景 |
|---|---|---|
| `VOLATILE` | 只接收订阅之后发布的消息 | 大多数实时数据 |
| `TRANSIENT_LOCAL` | 接收订阅之前发布的"晚加入"消息 | 地图、TF 静态变换、配置 |

**兼容性规则**：与 Reliability 类似，订阅者的 Durability 不能比发布者"更持久"。

```text
Publisher VOLATILE          + Subscriber VOLATILE          → ✅
Publisher TRANSIENT_LOCAL   + Subscriber VOLATILE          → ✅
Publisher VOLATILE          + Subscriber TRANSIENT_LOCAL   → ❌ 不通信！
Publisher TRANSIENT_LOCAL   + Subscriber TRANSIENT_LOCAL   → ✅
```

> 典型场景：`/tf_static` 使用 `TRANSIENT_LOCAL`，这样新启动的节点也能立即收到静态变换。如果你的录制器用 `VOLATILE`，就会丢失之前的静态变换。

### 2.3 History（历史保留）

| 值 | 行为 |
|---|---|
| `KEEP_LAST(N)` | 保留最近 N 条消息，超出的丢弃 |
| `KEEP_ALL` | 保留所有消息（受限于缓冲区大小） |

传感器数据通常用 `KEEP_LAST(5)`——如果处理跟不上，丢掉旧的帧，保留最新的。控制命令通常用 `KEEP_LAST(10)`。

### 2.4 Deadline（截止时间）

指定两条消息之间的最大间隔。如果超时，DDS 会触发回调通知。适合检测传感器是否停止发布。

### 2.5 Liveliness（活跃性）

检测发布者节点是否还活着（即使没有发消息）。区分两种：
- `AUTOMATIC`：DDS 底层心跳，只要进程在就算活。
- `MANUAL_BY_TOPIC`：必须实际发布消息才算活。

## 3. ROS 2 预设 QoS Profile

ROS 2 提供了常用预设，避免每次都手动配置：

| Profile | Reliability | Durability | History | 适用场景 |
|---------|------------|------------|---------|---------|
| `default` | RELIABLE | VOLATILE | KEEP_LAST(10) | 通用通信 |
| `sensor_data` | BEST_EFFORT | VOLATILE | KEEP_LAST(5) | 传感器数据 |
| `parameters` | RELIABLE | TRANSIENT_LOCAL | KEEP_LAST(1000) | 参数服务 |
| `services` | RELIABLE | VOLATILE | KEEP_LAST(10) | 服务调用 |
| `parameter_events` | BEST_EFFORT | VOLATILE | KEEP_LAST(1000) | 参数事件 |

```python
# 发布者使用预设
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSReliabilityPolicy

sensor_qos = QoSProfile(
    reliability=QoSReliabilityPolicy.BEST_EFFORT,
    durability=QoSDurabilityPolicy.VOLATILE,
    depth=5,
)

publisher = node.create_publisher(
    sensor_msgs.msg.Image,
    '/camera/image',
    qos_profile=sensor_qos,
)
```

## 4. 录制与回放中的 QoS

### ros2 bag record 的 QoS

`ros2 bag record` 默认使用 `sensor_data` profile 订阅话题。这意味着：

- 如果发布者用 `RELIABLE`，匹配成功（RELIABLE + BEST_EFFORT 可通信）。
- 如果发布者用 `BEST_EFFORT`，匹配成功（BEST_EFFORT + BEST_EFFORT 可通信）。

看起来没问题？但要注意 `depth` 只有 5——如果录制器的写入速度跟不上消息速率，消息会在 DDS 缓冲区被丢弃。

```bash
# 查看录制器的实际 QoS（需确认发行版是否支持该选项）
ros2 bag record --all --qos-profile-overrides-path qos_override.yaml -o my_bag
```

```yaml
# qos_override.yaml：为特定话题覆盖 QoS
/camera/head/image:
  reliability: best_effort
  durability: volatile
  depth: 30      # 增大缓冲区，减少高速相机丢帧
```

### ros2 bag play 的 QoS

回放时同样有 QoS 匹配问题。如果下游算法节点用 `RELIABLE`，而回放发布器用 `BEST_EFFORT`，可能丢失消息。

## 5. 诊断 QoS 问题

### 命令行诊断

```bash
# 查看某话题所有端点的 QoS（发布者和订阅者）
ros2 topic info /camera/head/image --verbose

# 输出示例：
# Publishing nodes:
#   /camera_driver:
#     QoS profile:
#       Reliability: BEST_EFFORT
#       Durability: VOLATILE
#       History: KEEP_LAST depth: 5
#
# Subscription nodes:
#   /rosbag2_recorder:
#     QoS profile:
#       Reliability: RELIABLE      ← 不匹配！
#       Durability: VOLATILE
#       History: KEEP_LAST depth: 5
```

上面这个例子就是经典的 QoS 不匹配：发布者 `BEST_EFFORT`，订阅者 `RELIABLE`——DDS 不会建立连接，消息直接收不到。

### Python 诊断脚本

```python
"""检查一个 bag 中每个话题的 QoS 和消息数，发现可能的 QoS 不匹配。"""
import sys
from pathlib import Path

from rosbags.highlevel import AnyReader
from collections import Counter


def diagnose_qos(bag_path: Path) -> None:
    with AnyReader([bag_path]) as reader:
        counts: Counter[str] = Counter()
        for connection, _, _ in reader.messages():
            counts[connection.topic] += 1

        print(f"Bag: {bag_path}")
        print(f"Duration: {reader.duration / 1e9:.1f}s")
        print(f"Total messages: {reader.message_count}")
        print()
        print("Topic | Count | Approx Hz")
        print("------|-------|-----------")
        for topic, count in sorted(counts.items()):
            hz = count / (reader.duration / 1e9) if reader.duration > 0 else 0
            flag = " ⚠️" if count == 0 else ""
            print(f"{topic} | {count} | {hz:.1f}{flag}")


diagnose_qos(Path(sys.argv[1]))
```

如果一个话题的计数远低于预期（比如相机应该是 30Hz × 60s = 1800 条，但只有 200 条），很可能就是 QoS 不匹配。

## 6. DDS 底层概念

ROS 2 的 DDS 中间件有几个配置会影响数据采集：

| 概念 | 作用 | 常见问题 |
|------|------|---------|
| Domain ID | 隔离不同 ROS 网络的"频道" | 两个不同 Domain ID 的节点互相看不到 |
| Discovery | 节点自动发现机制 | 网络不支持组播时，发现失败 |
| Transport | 传输协议（UDP/Shared Memory/TCP） | 大消息（点云）可能超过 UDP 最大包大小 |

```bash
# 设置 Domain ID（不同项目的机器人不要混在一起）
export ROS_DOMAIN_ID=42

# 使用 Shared Memory 传输（同机大幅提速，大消息必需）
# 需要安装 Cyclone DDS 或 Fast DDS 的 SHM 插件
```

## 7. QoS 与数据工程的交集

作为数据工程师，你需要关注的 QoS 场景：

| 场景 | QoS 关注点 | 数据质量影响 |
|------|----------|------------|
| 录制相机数据 | 发布者 BEST_EFFORT + 录制器 RELIABLE | 图像帧丢失，但不报错 |
| 录制 TF 静态变换 | TRANSIENT_LOCAL 未正确配置 | 录制后 TF 树断裂 |
| 录制高频 IMU | depth 太小 | 处理跟不上时丢数据 |
| 回放给算法节点 | 回放 QoS 与算法节点不匹配 | 算法收不到消息 |

**建议**：在你的 inspect pipeline（前置计划第二周）中增加 QoS 检查步骤——在采集前确认每个话题的发布者和录制器 QoS 兼容。

## 8. 本篇练习

1. 用 `ros2 topic info --verbose` 检查你容器中 `publish_demo_ros2.py` 各话题的 QoS，看哪些用 `BEST_EFFORT`、哪些用 `RELIABLE`。
2. 故意把录制器的 QoS 设成与发布者不兼容，录制一段数据后对比消息数量。
3. 运行上面的诊断脚本，检查你的 bag 中是否有帧数异常低的话题。
4. 思考：你的 `数据采集样本/` 中的 Orbbec 数据，是在 ROS 2 之外采集的——它的"QoS"等价物是什么？（提示：看 manifest 中的 `paired_frame_sets_observed` 和 `synchronization` 字段。）

下一篇将进入 TF 坐标变换系统——理解 `frame_id` 的真正含义。
