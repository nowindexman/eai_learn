#!/usr/bin/env python3
"""
双足灵巧手机器人 —— 模拟完整「走过去 → 拿东西 → 放回来」任务循环

机器人构型：
  - 双足：左右各 6 关节（hip_yaw/pitch/roll, knee, ankle_pitch/roll）
  - 双臂：左右各 7 关节（shoulder_yaw/pitch/roll, elbow_pitch, wrist_yaw/pitch/roll）
  - 灵巧手：左右各 5 指，每指 3 关节（MCP/PIP/DIP）
  - 躯干 IMU + 足底力传感器 + 指尖力传感器
  - 头部 RGB 相机 + 手腕深度相机

任务状态机：
  IDLE → WALK_TO → REACH → GRASP → LIFT → WALK_BACK → PLACE → RELEASE → IDLE

话题列表：
  /robot/odom                nav_msgs/Odometry               躯干里程计
  /robot/imu                 sensor_msgs/Imu                 躯干 IMU
  /robot/joint_states        sensor_msgs/JointState          腿+臂关节
  /robot/hand_left/joints    sensor_msgs/JointState          左手 15 关节
  /robot/hand_right/joints   sensor_msgs/JointState          右手 15 关节
  /robot/foot_force_left     geometry_msgs/WrenchStamped     左足底力
  /robot/foot_force_right    geometry_msgs/WrenchStamped     右足底力
  /robot/finger_force        sensor_msgs/JointState          指尖力
  /robot/cmd_vel             geometry_msgs/Twist             行走速度指令
  /robot/task_state          std_msgs/String                 任务阶段（latch）
  /camera/head/image         sensor_msgs/CompressedImage     头部 RGB 相机（JPEG）
  /camera/head/camera_info   sensor_msgs/CameraInfo          头部相机内参
  /camera/wrist/image        sensor_msgs/CompressedImage     手腕深度相机（JPEG）
  /camera/wrist/camera_info  sensor_msgs/CameraInfo          手腕相机内参
"""
import rospy
import math
import random
import numpy as np
import cv2

from std_msgs.msg import String, Float64
from nav_msgs.msg import Odometry
from sensor_msgs.msg import JointState, Imu, CompressedImage, CameraInfo
from geometry_msgs.msg import (
    Twist, Wrench, WrenchStamped, Vector3, Quaternion, Pose, Point
)

# ═══════════════════════════════════════════════════════════
# 关节定义
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

# ═══════════════════════════════════════════════════════════
# 初始化
# ═══════════════════════════════════════════════════════════

rospy.init_node("humanoid_pick_place_publisher")

pub_odom     = rospy.Publisher("/robot/odom",             Odometry,      queue_size=10)
pub_imu      = rospy.Publisher("/robot/imu",              Imu,           queue_size=10)
pub_joints   = rospy.Publisher("/robot/joint_states",     JointState,    queue_size=10)
pub_hand_l   = rospy.Publisher("/robot/hand_left/joints", JointState,    queue_size=10)
pub_hand_r   = rospy.Publisher("/robot/hand_right/joints",JointState,    queue_size=10)
pub_foot_l   = rospy.Publisher("/robot/foot_force_left",  WrenchStamped, queue_size=10)
pub_foot_r   = rospy.Publisher("/robot/foot_force_right", WrenchStamped, queue_size=10)
pub_finger_f = rospy.Publisher("/robot/finger_force",     JointState,    queue_size=10)
pub_cmd_vel  = rospy.Publisher("/robot/cmd_vel",          Twist,         queue_size=10)
pub_state    = rospy.Publisher("/robot/task_state",       String,        queue_size=5, latch=True)

# ── 相机话题 ─────────────────────────────────────────────
CAM_FPS = 10           # 相机 10 fps，比控制频率低
CAM_W, CAM_H = 320, 240  # 低分辨率，减小 bag 体积

pub_cam_head = rospy.Publisher("/camera/head/image",       CompressedImage, queue_size=5)
pub_cam_head_info = rospy.Publisher("/camera/head/camera_info", CameraInfo,  queue_size=5)
pub_cam_wrist = rospy.Publisher("/camera/wrist/image",      CompressedImage, queue_size=5)
pub_cam_wrist_info = rospy.Publisher("/camera/wrist/camera_info", CameraInfo, queue_size=5)

# 预创建相机内参（640×480 缩放到 320×240 的等效参数）
def make_camera_info(frame_id):
    ci = CameraInfo()
    ci.height = CAM_H
    ci.width  = CAM_W
    ci.distortion_model = "plumb_bob"
    ci.D = [0.0, 0.0, 0.0, 0.0, 0.0]           # 无畸变
    ci.K = [240.0, 0.0, CAM_W/2,  0.0, 240.0, CAM_H/2,  0.0, 0.0, 1.0]
    ci.R = [1,0,0, 0,1,0, 0,0,1]
    ci.P = [240.0, 0.0, CAM_W/2, 0.0,  0.0, 240.0, CAM_H/2, 0.0,  0.0, 0.0, 1.0, 0.0]
    ci.header.frame_id = frame_id
    return ci

cam_head_info  = make_camera_info("head_camera_link")
cam_wrist_info = make_camera_info("wrist_camera_link")

HZ = 50  # 50 Hz，真实人形机器人常用频率
rate = rospy.Rate(HZ)
count = 0

rospy.loginfo("=== Humanoid Pick-and-Place Publisher (50 Hz) ===")
rospy.loginfo(f"    Cycle: {TOTAL_CYCLE:.1f}s | States: {[s for s,_ in TASK_STATES]}")


# ─── 辅助函数 ─────────────────────────────────────────────

def get_state(t_in_cycle):
    """根据循环内时间返回当前状态名"""
    elapsed = 0
    for name, dur in TASK_STATES:
        if t_in_cycle < elapsed + dur:
            return name, (t_in_cycle - elapsed) / dur  # progress 0~1
        elapsed += dur
    return "IDLE", 0.0

def walking_gait(t, phase=0.0):
    """双足行走步态：简化正弦模型，返回 (左腿6关节, 右腿6关节)"""
    freq = 2.0  # 步频
    amp_hip  = 0.4
    amp_knee = 0.6
    amp_ankle = 0.2
    s = math.sin(2 * math.pi * freq * t + phase)
    c = math.cos(2 * math.pi * freq * t + phase)
    # 左腿：hip_pitch 前摆, knee 弯曲
    left  = [0.0,  amp_hip * s,  0.02 * c,  amp_knee * max(s, 0),  -amp_hip * s * 0.5,  0.01 * c]
    right = [0.0, -amp_hip * s, -0.02 * c,  amp_knee * max(-s, 0), amp_hip * s * 0.5,  -0.01 * c]
    return left, right

def arm_reach(progress, side="right"):
    """手臂伸出：从自然下垂到前方抓取位"""
    sign = 1 if side == "right" else -1
    pitch = -1.2 * progress          # shoulder_pitch 向前抬
    elbow = -0.8 * progress          # elbow 弯曲
    wrist_p = 0.5 * progress         # wrist 调整
    return [
        0.0,                         # shoulder_yaw
        pitch + random.gauss(0, 0.01),
        sign * 0.15,                 # shoulder_roll 略微外展
        elbow + random.gauss(0, 0.01),
        0.0,                         # wrist_yaw
        wrist_p,
        0.0,                         # wrist_roll
    ]

def arm_natural(side="right"):
    """手臂自然下垂摆动"""
    sign = 1 if side == "right" else -1
    return [0.0, -0.05, sign * 0.1, -0.1, 0.0, 0.0, 0.0]

def hand_open():
    """手指全张开：15 个关节角度"""
    return [0.0] * 15

def hand_close(grasp_force=1.0):
    """手指闭合抓握：MCP 大弯, PIP/DIP 跟随"""
    angles = []
    for i, f in enumerate(FINGER_NAMES):
        base = 1.0 if f != "thumb" else 0.8  # thumb 弯曲幅度略小
        angles += [base * grasp_force * 0.5,   # MCP
                   base * grasp_force * 0.7,   # PIP
                   base * grasp_force * 0.9]   # DIP
    return angles

def hand_pinch(progress):
    """渐进闭合"""
    return [v * progress for v in hand_close()]


# ═══════════════════════════════════════════════════════════
# 主循环
# ═══════════════════════════════════════════════════════════

while not rospy.is_shutdown():
    now = rospy.Time.now()
    t = count / float(HZ)
    t_cycle = t % TOTAL_CYCLE
    state, progress = get_state(t_cycle)

    # ── 发布任务状态 ────────────────────────────────────────
    if count % HZ == 0:  # 每秒发一次
        state_msg = String()
        state_msg.data = f"{state}|progress={progress:.2f}"
        pub_state.publish(state_msg)

    # ═══ 根据状态计算机器人各部位数据 ═══════════════════════

    # ── 里程计 & 速度 ──────────────────────────────────────
    odom = Odometry()
    odom.header.stamp = now
    odom.header.frame_id = "odom"
    odom.child_frame_id = "base_link"

    cmd = Twist()
    is_walking = state in ("WALK_TO", "WALK_BACK")
    walk_dir = 1.0 if state == "WALK_TO" else -1.0

    if is_walking:
        speed = 0.8  # m/s
        odom.pose.pose.position.x = walk_dir * speed * (t_cycle - 2.0)  # 简化
        cmd.linear.x = walk_dir * speed
        # 躯干行走起伏
        odom.pose.pose.position.z = 0.02 * abs(math.sin(2 * math.pi * 2.0 * t))
    else:
        odom.pose.pose.position.x = 4.8 if state in ("REACH","GRASP","LIFT") else (
            4.8 - 0.8 * (t_cycle - 15.5) if state == "WALK_BACK" else 0.0
        )
        if state == "WALK_BACK":
            cmd.linear.x = -0.8

    # 偏航
    yaw = 0.02 * math.sin(t * 0.3)
    odom.pose.pose.orientation = Quaternion(x=0, y=0, z=math.sin(yaw/2), w=math.cos(yaw/2))
    cmd.angular.z = 0.02 * math.cos(t * 0.3)

    pub_odom.publish(odom)
    pub_cmd_vel.publish(cmd)

    # ── IMU ─────────────────────────────────────────────────
    imu = Imu()
    imu.header.stamp = now
    imu.header.frame_id = "torso_imu"
    imu.orientation = odom.pose.pose.orientation
    imu.angular_velocity = Vector3(
        x=random.gauss(0, 0.005), y=random.gauss(0, 0.005),
        z=cmd.angular.z + random.gauss(0, 0.002)
    )
    # 行走时躯干晃动更大
    sway = 0.15 if is_walking else 0.03
    imu.linear_acceleration = Vector3(
        x=random.gauss(0, sway), y=random.gauss(0, sway),
        z=9.81 + random.gauss(0, 0.02)
    )
    pub_imu.publish(imu)

    # ── 腿关节 ─────────────────────────────────────────────
    if is_walking:
        leg_l, leg_r = walking_gait(t)
    else:
        # 站立微动
        leg_l = [random.gauss(0, 0.005)] * 6
        leg_r = [random.gauss(0, 0.005)] * 6
        leg_l[1] = -0.1  # 微屈膝
        leg_r[1] = -0.1
        leg_l[3] = 0.2
        leg_r[3] = 0.2

    # ── 臂关节 ─────────────────────────────────────────────
    if state == "IDLE":
        arm_l = arm_natural("left")
        arm_r = arm_natural("right")
    elif state == "WALK_TO":
        # 行走摆臂
        swing = 0.2 * math.sin(2 * math.pi * 2.0 * t)
        arm_l = arm_natural("left")
        arm_l[1] += swing
        arm_r = arm_natural("right")
        arm_r[1] -= swing
    elif state in ("REACH", "LIFT"):
        arm_l = arm_natural("left")
        arm_r = arm_reach(progress if state == "REACH" else 1.0)
    elif state == "GRASP":
        arm_l = arm_natural("left")
        arm_r = arm_reach(1.0)
    elif state in ("WALK_BACK", "PLACE"):
        arm_l = arm_natural("left")
        arm_r = arm_reach(1.0 if state == "PLACE" else 0.8)  # 拿着东西走
        arm_r[1] += 0.3  # 抬起一些
    elif state == "RELEASE":
        arm_l = arm_natural("left")
        arm_r = arm_reach(1.0 - progress)  # 手收回
    else:
        arm_l = arm_natural("left")
        arm_r = arm_natural("right")

    # 合并发布
    body_js = JointState()
    body_js.header.stamp = now
    body_js.name = ALL_BODY_JOINTS
    body_js.position = leg_l + leg_r + arm_l + arm_r
    body_js.velocity = [0.0] * len(ALL_BODY_JOINTS)
    body_js.effort   = [round(random.gauss(0, 3), 2)] * len(ALL_BODY_JOINTS)
    pub_joints.publish(body_js)

    # ── 灵巧手 ─────────────────────────────────────────────
    hand_l_js = JointState()
    hand_l_js.header.stamp = now
    hand_l_js.name = HAND_JOINTS_L
    hand_l_js.position = hand_open()  # 左手始终张开
    hand_l_js.effort = [0.0] * 15
    pub_hand_l.publish(hand_l_js)

    hand_r_js = JointState()
    hand_r_js.header.stamp = now
    hand_r_js.name = HAND_JOINTS_R

    if state == "GRASP":
        hand_r_js.position = hand_pinch(progress)
        hand_r_js.effort = [progress * 5.0] * 15  # 抓握力渐增
    elif state in ("LIFT", "WALK_BACK", "PLACE"):
        hand_r_js.position = hand_close(1.0)
        hand_r_js.effort = [8.0 + random.gauss(0, 0.5)] * 15  # 持续夹持力
    elif state == "RELEASE":
        hand_r_js.position = hand_pinch(1.0 - progress)
        hand_r_js.effort = [(1.0 - progress) * 5.0] * 15
    else:
        hand_r_js.position = hand_open()
        hand_r_js.effort = [0.0] * 15
    pub_hand_r.publish(hand_r_js)

    # ── 指尖力传感器 ────────────────────────────────────────
    finger_force = JointState()
    finger_force.header.stamp = now
    finger_force.name = [f"r_{f}_tip_force" for f in FINGER_NAMES]
    if state in ("GRASP", "LIFT", "WALK_BACK", "PLACE"):
        base_force = 3.0 if state == "GRASP" else 6.0
        finger_force.position = [round(base_force + random.gauss(0, 0.3), 2)] * 5
    else:
        finger_force.position = [0.0] * 5
    pub_finger_force.publish(finger_force)

    # ── 足底力传感器 ────────────────────────────────────────
    body_weight = 60.0  # kg → ~588 N
    for pub_foot, side_sign in [(pub_foot_l, 1), (pub_foot_r, -1)]:
        fs = WrenchStamped()
        fs.header.stamp = now
        fs.header.frame_id = f"{'l' if side_sign > 0 else 'r'}_foot"
        if is_walking:
            # 行走时交替承重
            phase = math.sin(2 * math.pi * 2.0 * t + (0 if side_sign > 0 else math.pi))
            fz = body_weight * 9.81 * max(0.1, (1 + phase) / 2)
        else:
            fz = body_weight * 9.81 / 2  # 双脚均分
            if state in ("LIFT", "PLACE"):
                fz += 10.0  # 物体重量传递
        fs.wrench.force = Vector3(
            x=random.gauss(0, 2), y=random.gauss(0, 2), z=fz
        )
        fs.wrench.torque = Vector3(
            x=random.gauss(0, 0.5), y=random.gauss(0, 0.5), z=random.gauss(0, 0.1)
        )
        pub_foot.publish(fs)

    # ── 相机图像（降频发布，10 fps） ─────────────────────
    if count % (HZ // CAM_FPS) == 0:
        # --- 头部相机：模拟前方场景 ---
        img_head = np.zeros((CAM_H, CAM_W, 3), dtype=np.uint8)
        # 地面：下半部分灰褐色
        img_head[CAM_H//2:, :] = [60, 60, 50]
        # 天空：上半部分渐变蓝
        for row in range(CAM_H // 2):
            ratio = row / (CAM_H // 2)
            img_head[row, :] = [int(80 + 40 * ratio), int(60 + 30 * ratio), int(30 + 20 * ratio)]
        # 目标物体：一个移动的彩色方块
        if state in ("WALK_TO", "REACH", "GRASP", "LIFT", "WALK_BACK"):
            obj_x = int(CAM_W * 0.5 + 30 * math.sin(t * 0.5))
            obj_y = int(CAM_H * 0.55)
            obj_size = 20 if state != "WALK_TO" else int(10 + 10 * progress)
            color = (0, 200, 50)  # 绿色物体
            if state in ("GRASP", "LIFT", "WALK_BACK"):
                obj_y = int(CAM_H * 0.55 - 40 * progress)
                color = (0, 200, 200)  # 变黄表示已被抓取
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
        ci_head.data = buf_head.tobytes()
        pub_cam_head.publish(ci_head)

        cam_head_info.header.stamp = now
        pub_cam_head_info.publish(cam_head_info)

        # --- 手腕相机：模拟近距离手部视角 ---
        img_wrist = np.zeros((CAM_H, CAM_W, 3), dtype=np.uint8)
        img_wrist[:] = [20, 20, 25]
        # 手指开合状态
        grip_open = 1.0
        if state == "GRASP":
            grip_open = 1.0 - progress
        elif state in ("LIFT", "WALK_BACK", "PLACE"):
            grip_open = 0.0
        elif state == "RELEASE":
            grip_open = progress
        # 画 5 根手指
        cx, cy = CAM_W // 2, CAM_H // 2 + 20
        for i in range(5):
            fx = cx - 60 + i * 30
            fy_top = cy - 50 + int(20 * (1 - grip_open))
            cv2.rectangle(img_wrist, (fx - 8, fy_top), (fx + 8, cy + 30),
                          (180, 150, 120), -1)
        # 抓到的物体
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
        ci_wrist.data = buf_wrist.tobytes()
        pub_cam_wrist.publish(ci_wrist)

        cam_wrist_info.header.stamp = now
        pub_cam_wrist_info.publish(cam_wrist_info)

    # ── 日志（每 2 秒一次） ─────────────────────────────────
    if count % (HZ * 2) == 0:
        grip_avg = sum(hand_r_js.effort) / len(hand_r_js.effort) if hand_r_js.effort else 0
        rospy.loginfo(
            f"[{state:>10s} {progress:.0%}] t={t:.1f}s | "
            f"x={odom.pose.pose.position.x:.2f}m | "
            f"knee_l={leg_l[3]:.2f}rad | "
            f"r_shoulder_pitch={arm_r[1]:.2f}rad | "
            f"grip_force={grip_avg:.1f}N"
        )

    count += 1
    rate.sleep()

rospy.loginfo("=== Done ===")
