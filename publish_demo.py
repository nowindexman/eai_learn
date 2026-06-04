#!/usr/bin/env python3
"""
具身智能多话题发布器 —— 模拟一台移动机械臂的核心传感器数据
话题列表：
  /robot/odom          nav_msgs/Odometry           里程计（底盘位移+速度）
  /robot/joint_states  sensor_msgs/JointState      关节状态（6轴机械臂角度）
  /robot/imu           sensor_msgs/Imu             IMU惯性传感器
  /robot/cmd_vel       geometry_msgs/Twist         底盘速度指令
  /robot/force_torque  geometry_msgs/Wrench        末端力/力矩传感器
  /robot/gripper       std_msgs/Float64            夹爪开合度
  /robot/status        std_msgs/String             系统状态文本
"""
import rospy
import math
import random

from std_msgs.msg import String, Float64
from nav_msgs.msg import Odometry
from sensor_msgs.msg import JointState, Imu
from geometry_msgs.msg import Twist, Wrench, Vector3, Quaternion

# ── 初始化节点 ──────────────────────────────────────────────
rospy.init_node("embodied_demo_publisher")

# ── 创建发布者 ──────────────────────────────────────────────
pub_odom   = rospy.Publisher("/robot/odom",         Odometry,    queue_size=10)
pub_joint  = rospy.Publisher("/robot/joint_states",  JointState,  queue_size=10)
pub_imu    = rospy.Publisher("/robot/imu",           Imu,         queue_size=10)
pub_cmd    = rospy.Publisher("/robot/cmd_vel",       Twist,       queue_size=10)
pub_ft     = rospy.Publisher("/robot/force_torque",  Wrench,      queue_size=10)
pub_grip   = rospy.Publisher("/robot/gripper",       Float64,     queue_size=10)
pub_status = rospy.Publisher("/robot/status",        String,      queue_size=10, latch=True)

# ── 机械臂关节名定义 ────────────────────────────────────────
JOINT_NAMES = [
    "shoulder_pan_joint",
    "shoulder_lift_joint",
    "elbow_joint",
    "wrist_1_joint",
    "wrist_2_joint",
    "wrist_3_joint",
]

FRAME_ID = "base_link"
rate = rospy.Rate(20)  # 20 Hz，接近真实机器人发布频率
count = 0

rospy.loginfo("=== Embodied Demo Publisher started (20 Hz) ===")

while not rospy.is_shutdown():
    now = rospy.Time.now()
    t = count / 20.0  # 秒

    # ── 1. 里程计：模拟沿 X 轴匀速前进 + 小幅转向 ──────────
    odom = Odometry()
    odom.header.stamp = now
    odom.header.frame_id = "odom"
    odom.child_frame_id = FRAME_ID
    odom.pose.pose.position.x = 0.5 * t                          # 0.5 m/s 前进
    odom.pose.pose.position.y = 0.1 * math.sin(t * 0.5)          # 小幅蛇形
    odom.pose.pose.orientation = Quaternion(
        x=0, y=0,
        z=math.sin(0.05 * math.cos(t * 0.5)),  # 偏航角
        w=math.cos(0.05 * math.cos(t * 0.5))
    )
    odom.twist.twist.linear.x = 0.5
    odom.twist.twist.angular.z = 0.05 * math.cos(t * 0.5)
    pub_odom.publish(odom)

    # ── 2. 关节状态：6 轴机械臂做正弦往复运动 ───────────────
    js = JointState()
    js.header.stamp = now
    js.name = JOINT_NAMES
    js.position = [
        math.sin(t * 0.3) * 1.0,       # shoulder_pan  ±1.0 rad
        math.sin(t * 0.5) * 0.8 - 0.5, # shoulder_lift
        math.sin(t * 0.4) * 1.2,       # elbow
        math.sin(t * 0.6) * 0.5,       # wrist_1
        math.cos(t * 0.3) * 0.3,       # wrist_2
        math.sin(t * 0.8) * 0.2,       # wrist_3
    ]
    js.velocity = [0.0] * 6  # 简化：速度为 0
    js.effort   = [round(random.uniform(-5, 5), 2)] * 6  # 模拟力矩噪声
    pub_joint.publish(js)

    # ── 3. IMU：加速度 + 角速度 + 方向 ──────────────────────
    imu = Imu()
    imu.header.stamp = now
    imu.header.frame_id = "imu_link"
    imu.orientation = odom.pose.pose.orientation  # 复用里程计方向
    imu.angular_velocity = Vector3(
        x=random.gauss(0, 0.01),
        y=random.gauss(0, 0.01),
        z=odom.twist.twist.angular.z + random.gauss(0, 0.005)
    )
    imu.linear_acceleration = Vector3(
        x=random.gauss(0, 0.05),
        y=random.gauss(0, 0.05),
        z=9.81 + random.gauss(0, 0.02)   # 重力 9.81 m/s²
    )
    pub_imu.publish(imu)

    # ── 4. 速度指令：模拟导航控制器输出 ────────────────────
    cmd = Twist()
    cmd.linear.x  = 0.5 + 0.1 * math.sin(t * 0.2)
    cmd.angular.z = 0.05 * math.cos(t * 0.5)
    pub_cmd.publish(cmd)

    # ── 5. 力/力矩传感器：模拟末端接触力 ────────────────────
    ft = Wrench()
    ft.force = Vector3(
        x=random.gauss(0, 0.5),
        y=random.gauss(0, 0.5),
        z=-2.0 + random.gauss(0, 0.3)   # 模拟向下按压力
    )
    ft.torque = Vector3(
        x=random.gauss(0, 0.02),
        y=random.gauss(0, 0.02),
        z=random.gauss(0, 0.01)
    )
    pub_ft.publish(ft)

    # ── 6. 夹爪开合度：周期性开合 ──────────────────────────
    gripper = Float64()
    gripper.data = round(0.04 * (math.sin(t * 0.2) + 1) / 2, 4)  # 0~0.04 m
    pub_grip.publish(gripper)

    # ── 7. 系统状态（仅发布一次，latch=True 锁存） ──────────
    if count == 0:
        status = String()
        status.data = "system_ok: all sensors initialized"
        pub_status.publish(status)

    # ── 日志（降频打印，避免刷屏） ──────────────────────────
    if count % 100 == 0:
        rospy.loginfo(
            f"t={t:.1f}s | odom_x={odom.pose.pose.position.x:.2f}m | "
            f"joint0={js.position[0]:.2f}rad | grip={gripper.data:.3f}m | "
            f"fz={ft.force.z:.2f}N"
        )

    count += 1
    rate.sleep()

rospy.loginfo("=== Done ===")
