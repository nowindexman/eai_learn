# 各种 info 输出对比

## 1. rosbag info (ROS 1)

```
root@ac58550d290b:/data# rosbag info 1c6umkjmum.bag
path:        1c6umkjmum.bag
version:     2.0
duration:    4:07s (247s)
start:       Jan 25 2011 14:29:26.43 (1295965766.43)
end:         Jan 25 2011 14:33:34.21 (1295966014.21)
size:        340.6 MB
messages:    81069
compression: none [414/414 chunks]
types:       geometry_msgs/PoseWithCovarianceStamped     [953b798c0f514ff060a53a3498ce6246]
             nav_msgs/Odometry                           [cd5e73d190d741a2f92e81eda573aca7]
             pr2_mechanism_controllers/BaseOdometryState [8a483e137ebc37abafa4c26549091dd6]
             pr2_mechanism_controllers/Odometer          [1f1d53743f4592ee455aa3eaf9019457]
             sensor_msgs/CameraInfo                      [c9a58c1b0b154e0e6da7578cb991d214]
             sensor_msgs/Image                           [060021388200f6f0f447d0fcd9c64743]
             sensor_msgs/Imu                             [6a62c6daae103f4ff57a132d6f95cec2]
             sensor_msgs/LaserScan                       [90c7ef2dc6895d81024acba2ac42f369]
             std_msgs/Bool                               [8b94c1b53db61fb6aed406028ad6332a]
             tf/tfMessage                                [94810edda583a504dfda3829e70d7eec]
topics:      /base_odometry/odom                       23451 msgs    : nav_msgs/Odometry
             /base_odometry/odometer                     248 msgs    : pr2_mechanism_controllers/Odometer
             /base_odometry/state                        248 msgs    : pr2_mechanism_controllers/BaseOdometryState
             /base_scan                                 4951 msgs    : sensor_msgs/LaserScan
             /robot_pose_ekf/odom_combined              7117 msgs    : geometry_msgs/PoseWithCovarianceStamped
             /tf                                       14124 msgs    : tf/tfMessage
             /tilt_scan                                 4936 msgs    : sensor_msgs/LaserScan
             /torso_lift_imu/data                      24778 msgs    : sensor_msgs/Imu
             /torso_lift_imu/is_calibrated                 1 msg     : std_msgs/Bool
             /wide_stereo/left/camera_info_throttle      243 msgs    : sensor_msgs/CameraInfo
             /wide_stereo/left/image_rect_throttle       486 msgs    : sensor_msgs/Image
             /wide_stereo/right/camera_info_throttle     243 msgs    : sensor_msgs/CameraInfo
             /wide_stereo/right/image_rect_throttle      243 msgs    : sensor_msgs/Image
```

## 2. ros2 bag info (ROS 2)

```
root@20097a57ff82:/data# ros2 bag info rosbags_v2.mcap

closing.

Files:             rosbags_v2.mcap
Bag size:          340.9 MiB
Storage id:        mcap
Duration:          247.783239926s
Start:             Jan 25 2011 14:29:26.427620748 (1295965766.427620748)
End:               Jan 25 2011 14:33:34.210860674 (1295966014.210860674)
Messages:          81069
Topic information: Topic: /wide_stereo/right/camera_info_throttle | Type: sensor_msgs/msg/CameraInfo | Count: 243 | Serialization Format: cdr
                   Topic: /wide_stereo/left/camera_info_throttle | Type: sensor_msgs/msg/CameraInfo | Count: 243 | Serialization Format: cdr
                   Topic: /wide_stereo/right/image_rect_throttle | Type: sensor_msgs/msg/Image | Count: 243 | Serialization Format: cdr
                   Topic: /wide_stereo/left/image_rect_throttle | Type: sensor_msgs/msg/Image | Count: 486 | Serialization Format: cdr
                   Topic: /base_odometry/state | Type: pr2_mechanism_controllers/msg/BaseOdometryState | Count: 248 | Serialization Format: cdr
                   Topic: /base_odometry/odometer | Type: pr2_mechanism_controllers/msg/Odometer | Count: 248 | Serialization Format: cdr
                   Topic: /base_scan | Type: sensor_msgs/msg/LaserScan | Count: 4951 | Serialization Format: cdr
                   Topic: /robot_pose_ekf/odom_combined | Type: geometry_msgs/msg/PoseWithCovarianceStamped | Count: 7117 | Serialization Format: cdr
                   Topic: /torso_lift_imu/data | Type: sensor_msgs/msg/Imu | Count: 24778 | Serialization Format: cdr
                   Topic: /torso_lift_imu/is_calibrated | Type: std_msgs/msg/Bool | Count: 1 | Serialization Format: cdr
                   Topic: /base_odometry/odom | Type: nav_msgs/msg/Odometry | Count: 23451 | Serialization Format: cdr
                   Topic: /tilt_scan | Type: sensor_msgs/msg/LaserScan | Count: 4936 | Serialization Format: cdr
                   Topic: /tf | Type: tf2_msgs/msg/TFMessage | Count: 14124 | Serialization Format: cdr
```

## 3. mcap info

```
❯ mcap info rosbags_v2.mcap
library:   rosbags-0.11.1
profile:   ros2
messages:  81069
duration:  4m7.783239926s
start:     2011-01-25T22:29:26.427620748+08:00 (1295965766.427620748)
end:       2011-01-25T22:33:34.210860674+08:00 (1295966014.210860674)
compression:
        : [312/312 chunks] [339.49 MiB/339.49 MiB (0.00%)] [1.37 MiB/sec]
chunks:
        max uncompressed size: 1.29 MiB
        max compressed size: 1.29 MiB
        overlaps: no
channels:
        (1)  /tf                                      14124 msgs (57.00Hz)    : tf2_msgs/msg/TFMessage [ros2msg]
        (2)  /tilt_scan                                4936 msgs (19.92Hz)    : sensor_msgs/msg/LaserScan [ros2msg]
        (3)  /base_odometry/odom                      23451 msgs (94.64Hz)    : nav_msgs/msg/Odometry [ros2msg]
        (4)  /torso_lift_imu/is_calibrated                1 msgs              : std_msgs/msg/Bool [ros2msg]
        (5)  /torso_lift_imu/data                     24778 msgs (100.00Hz)   : sensor_msgs/msg/Imu [ros2msg]
        (6)  /robot_pose_ekf/odom_combined             7117 msgs (28.72Hz)    : geometry_msgs/msg/PoseWithCovarianceStamped [ros2msg]
        (7)  /base_scan                                4951 msgs (19.98Hz)    : sensor_msgs/msg/LaserScan [ros2msg]
        (8)  /base_odometry/odometer                    248 msgs (1.00Hz)     : pr2_mechanism_controllers/msg/Odometer [ros2msg]
        (9)  /base_odometry/state                       248 msgs (1.00Hz)     : pr2_mechanism_controllers/msg/BaseOdometryState [ros2msg]
        (10) /wide_stereo/left/image_rect_throttle      486 msgs (1.96Hz)     : sensor_msgs/msg/Image [ros2msg]
        (11) /wide_stereo/right/image_rect_throttle     243 msgs (0.98Hz)     : sensor_msgs/msg/Image [ros2msg]
        (12) /wide_stereo/left/camera_info_throttle     243 msgs (0.98Hz)     : sensor_msgs/msg/CameraInfo [ros2msg]
        (13) /wide_stereo/right/camera_info_throttle    243 msgs (0.98Hz)     : sensor_msgs/msg/CameraInfo [ros2msg]
channels: 13
attachments: 0
metadata: 1
```
