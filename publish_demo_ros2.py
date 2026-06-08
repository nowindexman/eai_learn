#!/usr/bin/env python3
"""
双足灵巧手机器人 —— ROS 2 (rclpy) 版本
模拟完整「走过去 → 拿东西 → 放回来」任务循环

与 ROS 1 版本 (publish_demo.py) 的对照：
  rospy           → rclpy + Node 类
  rospy.Publisher → self.create_publisher()
  latch=True      → QoSDurabilityPolicy.TRANSIENT_LOCAL
  rospy.Rate      → self.create_rate()
  rospy.Time.now()→ self.get_clock().now().to_msg()
  rospy.loginfo   → self.get_logger().info
  Header.seq      → 已移除（ROS 2 的 DDS 自带序列号）

话题列表（14 个，与 v1 完全一致）：
  /robot/odom                nav_msgs/msg/Odometry               躯干里程计
  /robot/imu                 sensor_msgs/msg/Imu                 躯干 IMU
  /robot/joint_states        sensor_msgs/msg/JointState          腿+臂关节
  /robot/hand_left/joints    sensor_msgs/msg/JointState          左手 15 关节
  /robot/hand_right/joints   sensor_msgs/msg/JointState          右手 15 关节
  /robot/foot_force_left     geometry_msgs/msg/WrenchStamped     左足底力
  /robot/foot_force_right    geometry_msgs/msg/WrenchStamped     右足底力
  /robot/finger_force        sensor_msgs/msg/JointState          指尖力
  /robot/cmd_vel             geometry_msgs/msg/Twist             行走速度指令
  /robot/task_state          std_msgs/msg/String                 任务阶段（latch）
  /camera/head/image         sensor_msgs/msg/CompressedImage     头部 RGB 相机（JPEG）
  /camera/head/camera_info   sensor_msgs/msg/CameraInfo          头部相机内参
  /camera/wrist/image        sensor_msgs/msg/CompressedImage     手腕深度相机（JPEG）
  /camera/wrist/camera_info  sensor_msgs/msg/CameraInfo          手腕相机内参
"""
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSDurabilityPolicy

import math
import random
import time
import array
import numpy as np
import cv2

from std_msgs.msg import String
from nav_msgs.msg import Odometry
from sensor_msgs.msg import JointState, Imu, CompressedImage, CameraInfo
from geometry_msgs.msg import (
    Twist, Wrench, WrenchStamped, Vector3, Quaternion, Point
)

# ═══════════════════════════════════════════════════════════
# 关节定义（与 v1 完全相同）
# ═══════════════════════════════════════════════════════════

# 左腿 / 右腿（各 6 个）
LEG_JOINTS_L = ["l_hip_yaw", "l_hip_pitch", "l_hip_roll", "l_knee", "l_ankle_pitch", "l_ankle_roll"]
LEG_JOINTS_R = ["r_hip_yaw", "r_hip_pitch", "r_hip_roll", "r_knee", "r_ankle_pitch", "r_ankle_roll"]

# 左臂 / 右臂（各 7 个）
ARM_JOINTS_L = ["l_shoulder_yaw", "l_shoulder_pitch", "l_shoulder_roll", "l_elbow_pitch",
                "l_wrist_yaw", "l_wrist_pitch", "l_wrist_roll"]
ARM_JOINTS_R = ["r_shoulder_yaw", "r_shoulder_pitch", "r_shoulder_roll", "r_elbow_pitch",
                "r_wrist_yaw", "r_wrist_pitch", "r_wrist_roll"]

# 灵巧手：每手 5 指 × 3 关节 = 15
FINGER_NAMES = ["thumb", "index", "middle", "ring", "pinky"]
JOINT_SUFFIX = ["_mcp", "_pip", "_dip"]

def hand_joints(prefix="l"):
    return [f"{prefix}_{f}{s}" for f in FINGER_NAMES for s in JOINT_SUFFIX]

HAND_JOINTS_L = hand_joints("l")  # 15 个
HAND_JOINTS_R = hand_joints("r")  # 15 个

ALL_BODY_JOINTS = LEG_JOINTS_L + LEG_JOINTS_R + ARM_JOINTS_L + ARM_JOINTS_R

# ═══════════════════════════════════════════════════════════
# 任务状态机
# ═══════════════════════════════════════════════════════════

TASK_STATES = [
    ("IDLE",       2.0),   # 站立等待
    ("WALK_TO",    6.0),   # 走向目标
    ("REACH",      3.0),   # 右手伸向物体
    ("GRASP",      1.5),   # 右手闭合抓握
    ("LIFT",       2.0),   # 抬起物体
    ("WALK_BACK",  6.0),   # 走回原位
    ("PLACE",      2.5),   # 右手下放物体
    ("RELEASE",    1.5),   # 松开手指
]
TOTAL_CYCLE = sum(d for _, d in TASK_STATES)

HZ = 50       # 50 Hz，真实人形机器人常用频率
CAM_FPS = 10  # 相机 10 fps
CAM_W, CAM_H = 320, 240


# ─── 辅助函数 ─────────────────────────────────────────────

def get_state(t_in_cycle):
    """根据循环内时间返回当前状态名"""
    elapsed = 0
    for name, dur in TASK_STATES:
        if t_in_cycle < elapsed + dur:
            return name, (t_in_cycle - elapsed) / dur
        elapsed += dur
    return "IDLE", 0.0

def walking_gait(t, phase=0.0):
    """双足行走步态：简化正弦模型"""
    freq = 2.0
    amp_hip  = 0.4
    amp_knee = 0.6
    amp_ankle = 0.2
    s = math.sin(2 * math.pi * freq * t + phase)
    c = math.cos(2 * math.pi * freq * t + phase)
    left  = [0.0,  amp_hip * s,  0.02 * c,  amp_knee * max(s, 0),  -amp_hip * s * 0.5,  0.01 * c]
    right = [0.0, -amp_hip * s, -0.02 * c,  amp_knee * max(-s, 0), amp_hip * s * 0.5,  -0.01 * c]
    return left, right

def arm_reach(progress, side="right"):
    """手臂伸出"""
    sign = 1 if side == "right" else -1
    pitch = -1.2 * progress
    elbow = -0.8 * progress
    wrist_p = 0.5 * progress
    return [
        0.0,
        pitch + random.gauss(0, 0.01),
        sign * 0.15,
        elbow + random.gauss(0, 0.01),
        0.0,
        wrist_p,
        0.0,
    ]

def arm_natural(side="right"):
    """手臂自然下垂摆动"""
    sign = 1 if side == "right" else -1
    return [0.0, -0.05, sign * 0.1, -0.1, 0.0, 0.0, 0.0]

def hand_open():
    return [0.0] * 15

def hand_close(grasp_force=1.0):
    angles = []
    for i, f in enumerate(FINGER_NAMES):
        base = 1.0 if f != "thumb" else 0.8
        angles += [base * grasp_force * 0.5,
                   base * grasp_force * 0.7,
                   base * grasp_force * 0.9]
    return angles

def hand_pinch(progress):
    return [v * progress for v in hand_close()]

def make_camera_info(frame_id):
    """创建相机内参（ROS 2 版本字段名小写）"""
    ci = CameraInfo()
    ci.height = CAM_H
    ci.width  = CAM_W
    ci.distortion_model = "plumb_bob"
    ci.d = [0.0, 0.0, 0.0, 0.0, 0.0]           # ROS 2: D → d
    ci.k = [240.0, 0.0, CAM_W/2,  0.0, 240.0, CAM_H/2,  0.0, 0.0, 1.0]   # K → k
    ci.r = [1.0, 0.0, 0.0,  0.0, 1.0, 0.0,  0.0, 0.0, 1.0]               # R → r
    ci.p = [240.0, 0.0, CAM_W/2, 0.0,  0.0, 240.0, CAM_H/2, 0.0,  0.0, 0.0, 1.0, 0.0]  # P → p
    ci.header.frame_id = frame_id
    return ci


# ═══════════════════════════════════════════════════════════
# ROS 2 节点类
# ═══════════════════════════════════════════════════════════

class HumanoidPublisher(Node):
    def __init__(self):
        super().__init__("humanoid_pick_place_publisher")

        # 普通话题 QoS（10 队列）
        qos_default = QoSProfile(depth=10)

        # latch 话题 QoS（TRANSIENT_LOCAL，相当于 v1 的 latch=True）
        qos_latched = QoSProfile(
            depth=5,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
        )

        # ── 创建 Publisher ───────────────────────────────
        self.pub_odom     = self.create_publisher(Odometry,      "/robot/odom",             qos_default)
        self.pub_imu      = self.create_publisher(Imu,           "/robot/imu",              qos_default)
        self.pub_joints   = self.create_publisher(JointState,    "/robot/joint_states",     qos_default)
        self.pub_hand_l   = self.create_publisher(JointState,    "/robot/hand_left/joints", qos_default)
        self.pub_hand_r   = self.create_publisher(JointState,    "/robot/hand_right/joints",qos_default)
        self.pub_foot_l   = self.create_publisher(WrenchStamped, "/robot/foot_force_left",  qos_default)
        self.pub_foot_r   = self.create_publisher(WrenchStamped, "/robot/foot_force_right", qos_default)
        self.pub_finger   = self.create_publisher(JointState,    "/robot/finger_force",     qos_default)
        self.pub_cmd_vel  = self.create_publisher(Twist,         "/robot/cmd_vel",          qos_default)
        self.pub_state    = self.create_publisher(String,        "/robot/task_state",       qos_latched)

        self.pub_cam_head      = self.create_publisher(CompressedImage, "/camera/head/image",      qos_default)
        self.pub_cam_head_info = self.create_publisher(CameraInfo,      "/camera/head/camera_info", qos_default)
        self.pub_cam_wrist      = self.create_publisher(CompressedImage, "/camera/wrist/image",     qos_default)
        self.pub_cam_wrist_info = self.create_publisher(CameraInfo,      "/camera/wrist/camera_info",qos_default)

        # 预创建相机内参
        self.cam_head_info  = make_camera_info("head_camera_link")
        self.cam_wrist_info = make_camera_info("wrist_camera_link")

        self.count = 0

        self.get_logger().info("=== Humanoid Pick-and-Place Publisher (ROS 2, 50 Hz) ===")
        self.get_logger().info(f"    Cycle: {TOTAL_CYCLE:.1f}s | States: {[s for s,_ in TASK_STATES]}")

    def run(self):
        """主循环"""
        while rclpy.ok():
            now = self.get_clock().now().to_msg()
            t = self.count / float(HZ)
            t_cycle = t % TOTAL_CYCLE
            state, progress = get_state(t_cycle)

            # ── 发布任务状态（每秒 1 次） ─────────────────────
            if self.count % HZ == 0:
                state_msg = String()
                state_msg.data = f"{state}|progress={progress:.2f}"
                self.pub_state.publish(state_msg)

            # ═══ 根据状态计算机器人各部位数据 ═══════════════

            # ── 里程计 & 速度 ──────────────────────────────
            odom = Odometry()
            odom.header.stamp = now
            odom.header.frame_id = "odom"
            odom.child_frame_id = "base_link"

            cmd = Twist()
            is_walking = state in ("WALK_TO", "WALK_BACK")
            walk_dir = 1.0 if state == "WALK_TO" else -1.0

            if is_walking:
                speed = 0.8
                odom.pose.pose.position.x = walk_dir * speed * (t_cycle - 2.0)
                cmd.linear.x = walk_dir * speed
                odom.pose.pose.position.z = 0.02 * abs(math.sin(2 * math.pi * 2.0 * t))
            else:
                odom.pose.pose.position.x = 4.8 if state in ("REACH","GRASP","LIFT") else (
                    4.8 - 0.8 * (t_cycle - 15.5) if state == "WALK_BACK" else 0.0
                )
                if state == "WALK_BACK":
                    cmd.linear.x = -0.8

            yaw = 0.02 * math.sin(t * 0.3)
            odom.pose.pose.orientation = Quaternion(x=0.0, y=0.0, z=math.sin(yaw/2), w=math.cos(yaw/2))
            cmd.angular.z = 0.02 * math.cos(t * 0.3)

            self.pub_odom.publish(odom)
            self.pub_cmd_vel.publish(cmd)

            # ── IMU ─────────────────────────────────────────
            imu = Imu()
            imu.header.stamp = now
            imu.header.frame_id = "torso_imu"
            imu.orientation = odom.pose.pose.orientation
            imu.angular_velocity = Vector3(
                x=random.gauss(0, 0.005), y=random.gauss(0, 0.005),
                z=cmd.angular.z + random.gauss(0, 0.002)
            )
            sway = 0.15 if is_walking else 0.03
            imu.linear_acceleration = Vector3(
                x=random.gauss(0, sway), y=random.gauss(0, sway),
                z=9.81 + random.gauss(0, 0.02)
            )
            self.pub_imu.publish(imu)

            # ── 腿关节 ─────────────────────────────────────
            if is_walking:
                leg_l, leg_r = walking_gait(t)
            else:
                leg_l = [random.gauss(0, 0.005)] * 6
                leg_r = [random.gauss(0, 0.005)] * 6
                leg_l[1] = -0.1; leg_r[1] = -0.1
                leg_l[3] = 0.2;  leg_r[3] = 0.2

            # ── 臂关节 ─────────────────────────────────────
            if state == "IDLE":
                arm_l = arm_natural("left")
                arm_r = arm_natural("right")
            elif state == "WALK_TO":
                swing = 0.2 * math.sin(2 * math.pi * 2.0 * t)
                arm_l = arm_natural("left");  arm_l[1] += swing
                arm_r = arm_natural("right"); arm_r[1] -= swing
            elif state in ("REACH", "LIFT"):
                arm_l = arm_natural("left")
                arm_r = arm_reach(progress if state == "REACH" else 1.0)
            elif state == "GRASP":
                arm_l = arm_natural("left")
                arm_r = arm_reach(1.0)
            elif state in ("WALK_BACK", "PLACE"):
                arm_l = arm_natural("left")
                arm_r = arm_reach(1.0 if state == "PLACE" else 0.8)
                arm_r[1] += 0.3
            elif state == "RELEASE":
                arm_l = arm_natural("left")
                arm_r = arm_reach(1.0 - progress)
            else:
                arm_l = arm_natural("left")
                arm_r = arm_natural("right")

            body_js = JointState()
            body_js.header.stamp = now
            body_js.name = ALL_BODY_JOINTS
            body_js.position = leg_l + leg_r + arm_l + arm_r
            body_js.velocity = [0.0] * len(ALL_BODY_JOINTS)
            body_js.effort   = [round(random.gauss(0, 3), 2)] * len(ALL_BODY_JOINTS)
            self.pub_joints.publish(body_js)

            # ── 灵巧手 ─────────────────────────────────────
            hand_l_js = JointState()
            hand_l_js.header.stamp = now
            hand_l_js.name = HAND_JOINTS_L
            hand_l_js.position = hand_open()
            hand_l_js.effort = [0.0] * 15
            self.pub_hand_l.publish(hand_l_js)

            hand_r_js = JointState()
            hand_r_js.header.stamp = now
            hand_r_js.name = HAND_JOINTS_R

            if state == "GRASP":
                hand_r_js.position = hand_pinch(progress)
                hand_r_js.effort = [progress * 5.0] * 15
            elif state in ("LIFT", "WALK_BACK", "PLACE"):
                hand_r_js.position = hand_close(1.0)
                hand_r_js.effort = [8.0 + random.gauss(0, 0.5)] * 15
            elif state == "RELEASE":
                hand_r_js.position = hand_pinch(1.0 - progress)
                hand_r_js.effort = [(1.0 - progress) * 5.0] * 15
            else:
                hand_r_js.position = hand_open()
                hand_r_js.effort = [0.0] * 15
            self.pub_hand_r.publish(hand_r_js)

            # ── 指尖力传感器 ────────────────────────────────
            ff = JointState()
            ff.header.stamp = now
            ff.name = [f"r_{f}_tip_force" for f in FINGER_NAMES]
            if state in ("GRASP", "LIFT", "WALK_BACK", "PLACE"):
                base_force = 3.0 if state == "GRASP" else 6.0
                ff.position = [round(base_force + random.gauss(0, 0.3), 2)] * 5
            else:
                ff.position = [0.0] * 5
            self.pub_finger.publish(ff)

            # ── 足底力传感器 ────────────────────────────────
            body_weight = 60.0
            for pub_foot, side_sign, foot_name in [
                (self.pub_foot_l, 1, "l_foot"),
                (self.pub_foot_r, -1, "r_foot"),
            ]:
                fs = WrenchStamped()
                fs.header.stamp = now
                fs.header.frame_id = foot_name
                if is_walking:
                    phase = math.sin(2 * math.pi * 2.0 * t + (0 if side_sign > 0 else math.pi))
                    fz = body_weight * 9.81 * max(0.1, (1 + phase) / 2)
                else:
                    fz = body_weight * 9.81 / 2
                    if state in ("LIFT", "PLACE"):
                        fz += 10.0
                fs.wrench.force = Vector3(
                    x=random.gauss(0, 2), y=random.gauss(0, 2), z=fz
                )
                fs.wrench.torque = Vector3(
                    x=random.gauss(0, 0.5), y=random.gauss(0, 0.5), z=random.gauss(0, 0.1)
                )
                pub_foot.publish(fs)

            # ── 相机图像（降频，10 fps） ─────────────────
            if self.count % (HZ // CAM_FPS) == 0:
                self._publish_cameras(now, state, progress, t, hand_r_js)

            # ── 日志（每秒 2 次） ─────────────────────────
            if self.count % (HZ // 2) == 0:
                grip_avg = sum(hand_r_js.effort) / len(hand_r_js.effort) if hand_r_js.effort else 0
                self.get_logger().info(
                    f"[{state:>10s} {progress:.0%}] t={t:.1f}s | "
                    f"x={odom.pose.pose.position.x:.2f}m | "
                    f"knee_l={leg_l[3]:.2f}rad | "
                    f"r_shoulder_pitch={arm_r[1]:.2f}rad | "
                    f"grip_force={grip_avg:.1f}N"
                )

            self.count += 1
            time.sleep(1.0 / HZ)

    def _publish_cameras(self, now, state, progress, t, hand_r_js):
        """发布头部和手腕相机图像"""

        # --- 头部相机 ---
        img_head = np.zeros((CAM_H, CAM_W, 3), dtype=np.uint8)
        img_head[CAM_H//2:, :] = [60, 60, 50]
        for row in range(CAM_H // 2):
            ratio = row / (CAM_H // 2)
            img_head[row, :] = [int(80 + 40 * ratio), int(60 + 30 * ratio), int(30 + 20 * ratio)]

        if state in ("WALK_TO", "REACH", "GRASP", "LIFT", "WALK_BACK"):
            obj_x = int(CAM_W * 0.5 + 30 * math.sin(t * 0.5))
            obj_y = int(CAM_H * 0.55)
            obj_size = 20 if state != "WALK_TO" else int(10 + 10 * progress)
            color = (0, 200, 50)
            if state in ("GRASP", "LIFT", "WALK_BACK"):
                obj_y = int(CAM_H * 0.55 - 40 * progress)
                color = (0, 200, 200)
            cv2.rectangle(img_head,
                          (obj_x - obj_size, obj_y - obj_size),
                          (obj_x + obj_size, obj_y + obj_size),
                          color, -1)
        cv2.putText(img_head, f"[{state}]", (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(img_head, f"t={t:.1f}s", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)

        _, buf_head = cv2.imencode('.jpg', img_head, [cv2.IMWRITE_JPEG_QUALITY, 70])
        ci_head = CompressedImage()
        ci_head.header.stamp = now
        ci_head.header.frame_id = "head_camera_link"
        ci_head.format = "jpeg"
        ci_head.data = array.array('B', buf_head.tobytes())  # ROS 2: uint8[] 用 array.array
        self.pub_cam_head.publish(ci_head)

        self.cam_head_info.header.stamp = now
        self.pub_cam_head_info.publish(self.cam_head_info)

        # --- 手腕相机 ---
        img_wrist = np.zeros((CAM_H, CAM_W, 3), dtype=np.uint8)
        img_wrist[:] = [20, 20, 25]

        grip_open = 1.0
        if state == "GRASP":
            grip_open = 1.0 - progress
        elif state in ("LIFT", "WALK_BACK", "PLACE"):
            grip_open = 0.0
        elif state == "RELEASE":
            grip_open = progress

        cx, cy = CAM_W // 2, CAM_H // 2 + 20
        for i in range(5):
            fx = cx - 60 + i * 30
            fy_top = cy - 50 + int(20 * (1 - grip_open))
            cv2.rectangle(img_wrist, (fx - 8, fy_top), (fx + 8, cy + 30),
                          (180, 150, 120), -1)

        if state in ("GRASP", "LIFT", "WALK_BACK", "PLACE") and grip_open < 0.5:
            cv2.circle(img_wrist, (cx, cy - 30), 15, (0, 200, 50), -1)

        grip_force = sum(hand_r_js.effort) / 15 if hand_r_js.effort else 0
        cv2.putText(img_wrist, f"grip={grip_force:.1f}N", (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

        _, buf_wrist = cv2.imencode('.jpg', img_wrist, [cv2.IMWRITE_JPEG_QUALITY, 70])
        ci_wrist = CompressedImage()
        ci_wrist.header.stamp = now
        ci_wrist.header.frame_id = "wrist_camera_link"
        ci_wrist.format = "jpeg"
        ci_wrist.data = array.array('B', buf_wrist.tobytes())
        self.pub_cam_wrist.publish(ci_wrist)

        self.cam_wrist_info.header.stamp = now
        self.pub_cam_wrist_info.publish(self.cam_wrist_info)


# ═══════════════════════════════════════════════════════════
# 入口
# ═══════════════════════════════════════════════════════════

def main():
    rclpy.init()
    node = HumanoidPublisher()
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        node.get_logger().info("=== Done ===")
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
