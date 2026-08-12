> 原文地址：https://ternaris.gitlab.io/rosbags/api/rosbags.html

# Rosbags 命名空间

本页面为 Rosbags 库的完整 API 参考索引，涵盖所有子模块、类、方法和函数。

---

## rosbags.convert

消息格式转换模块，支持 ROS1 和 ROS2 之间的消息转换。

- [`ConverterError`](rosbags.convert.html#rosbags.convert.ConverterError) — 转换错误异常类
- [`convert()`](rosbags.convert.html#rosbags.convert.convert) — 消息格式转换函数

## rosbags.highlevel

高层读写接口，提供统一的 bag 文件读取方式。

- [`AnyReader`](rosbags.highlevel.html#rosbags.highlevel.AnyReader) — 通用 Reader，可自动识别并读取 ROS1 或 ROS2 bag 文件
  - [`AnyReader.close()`](rosbags.highlevel.html#rosbags.highlevel.AnyReader.close) — 关闭 Reader
  - [`AnyReader.deserialize()`](rosbags.highlevel.html#rosbags.highlevel.AnyReader.deserialize) — 反序列化消息
  - [`AnyReader.duration`](rosbags.highlevel.html#rosbags.highlevel.AnyReader.duration) — bag 文件时长（duration）
  - [`AnyReader.end_time`](rosbags.highlevel.html#rosbags.highlevel.AnyReader.end_time) — 结束时间戳
  - [`AnyReader.message_count`](rosbags.highlevel.html#rosbags.highlevel.AnyReader.message_count) — 消息总数
  - [`AnyReader.messages()`](rosbags.highlevel.html#rosbags.highlevel.AnyReader.messages) — 迭代读取消息
  - [`AnyReader.open()`](rosbags.highlevel.html#rosbags.highlevel.AnyReader.open) — 打开 Reader
  - [`AnyReader.start_time`](rosbags.highlevel.html#rosbags.highlevel.AnyReader.start_time) — 起始时间戳
  - [`AnyReader.topics`](rosbags.highlevel.html#rosbags.highlevel.AnyReader.topics) — 话题信息
- [`AnyReaderError`](rosbags.highlevel.html#rosbags.highlevel.AnyReaderError) — AnyReader 错误异常类

## rosbags.rosbag1

ROS1 bag 文件（`.bag`）的读写模块。

- [`Reader`](rosbags.rosbag1.html#rosbags.rosbag1.Reader) — ROS1 bag 文件 Reader
  - [`Reader.close()`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.close) — 关闭 Reader
  - [`Reader.duration`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.duration) — bag 文件时长（duration）
  - [`Reader.end_time`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.end_time) — 结束时间戳
  - [`Reader.message_count`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.message_count) — 消息总数
  - [`Reader.messages()`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.messages) — 迭代读取消息
  - [`Reader.open()`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.open) — 打开 Reader
  - [`Reader.read_chunk()`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.read_chunk) — 读取数据块（chunk）
  - [`Reader.read_chunk_info()`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.read_chunk_info) — 读取数据块信息
  - [`Reader.read_connection()`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.read_connection) — 读取连接信息
  - [`Reader.read_index_data()`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.read_index_data) — 读取索引数据
  - [`Reader.start_time`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.start_time) — 起始时间戳
  - [`Reader.topics`](rosbags.rosbag1.html#rosbags.rosbag1.Reader.topics) — 话题信息
- [`ReaderError`](rosbags.rosbag1.html#rosbags.rosbag1.ReaderError) — Reader 错误异常类
- [`Writer`](rosbags.rosbag1.html#rosbags.rosbag1.Writer) — ROS1 bag 文件 Writer
  - [`Writer.CompressionFormat`](rosbags.rosbag1.html#rosbags.rosbag1.Writer.CompressionFormat) — 压缩格式枚举
  - [`Writer.add_connection()`](rosbags.rosbag1.html#rosbags.rosbag1.Writer.add_connection) — 添加连接
  - [`Writer.close()`](rosbags.rosbag1.html#rosbags.rosbag1.Writer.close) — 关闭 Writer
  - [`Writer.open()`](rosbags.rosbag1.html#rosbags.rosbag1.Writer.open) — 打开 Writer
  - [`Writer.set_compression()`](rosbags.rosbag1.html#rosbags.rosbag1.Writer.set_compression) — 设置压缩方式
  - [`Writer.write()`](rosbags.rosbag1.html#rosbags.rosbag1.Writer.write) — 写入消息
  - [`Writer.write_chunk()`](rosbags.rosbag1.html#rosbags.rosbag1.Writer.write_chunk) — 写入数据块（chunk）
  - [`Writer.write_connection()`](rosbags.rosbag1.html#rosbags.rosbag1.Writer.write_connection) — 写入连接信息
- [`WriterError`](rosbags.rosbag1.html#rosbags.rosbag1.WriterError) — Writer 错误异常类

## rosbags.rosbag2

ROS2 bag 文件的读写模块。

- [`CompressionFormat`](rosbags.rosbag2.html#rosbags.rosbag2.CompressionFormat) — 压缩格式枚举
- [`CompressionMode`](rosbags.rosbag2.html#rosbags.rosbag2.CompressionMode) — 压缩模式枚举
- [`Reader`](rosbags.rosbag2.html#rosbags.rosbag2.Reader) — ROS2 bag 文件 Reader
  - [`Reader.close()`](rosbags.rosbag2.html#rosbags.rosbag2.Reader.close) — 关闭 Reader
  - [`Reader.compression_format`](rosbags.rosbag2.html#rosbags.rosbag2.Reader.compression_format) — 压缩格式
  - [`Reader.compression_mode`](rosbags.rosbag2.html#rosbags.rosbag2.Reader.compression_mode) — 压缩模式
  - [`Reader.duration`](rosbags.rosbag2.html#rosbags.rosbag2.Reader.duration) — bag 文件时长（duration）
  - [`Reader.end_time`](rosbags.rosbag2.html#rosbags.rosbag2.Reader.end_time) — 结束时间戳
  - [`Reader.message_count`](rosbags.rosbag2.html#rosbags.rosbag2.Reader.message_count) — 消息总数
  - [`Reader.messages()`](rosbags.rosbag2.html#rosbags.rosbag2.Reader.messages) — 迭代读取消息
  - [`Reader.open()`](rosbags.rosbag2.html#rosbags.rosbag2.Reader.open) — 打开 Reader
  - [`Reader.ros_distro`](rosbags.rosbag2.html#rosbags.rosbag2.Reader.ros_distro) — ROS 发行版信息
  - [`Reader.start_time`](rosbags.rosbag2.html#rosbags.rosbag2.Reader.start_time) — 起始时间戳
  - [`Reader.topics`](rosbags.rosbag2.html#rosbags.rosbag2.Reader.topics) — 话题信息
- [`ReaderError`](rosbags.rosbag2.html#rosbags.rosbag2.ReaderError) — Reader 错误异常类
- [`StoragePlugin`](rosbags.rosbag2.html#rosbags.rosbag2.StoragePlugin) — 存储插件枚举
- [`Writer`](rosbags.rosbag2.html#rosbags.rosbag2.Writer) — ROS2 bag 文件 Writer
  - [`Writer.add_connection()`](rosbags.rosbag2.html#rosbags.rosbag2.Writer.add_connection) — 添加连接
  - [`Writer.close()`](rosbags.rosbag2.html#rosbags.rosbag2.Writer.close) — 关闭 Writer
  - [`Writer.open()`](rosbags.rosbag2.html#rosbags.rosbag2.Writer.open) — 打开 Writer
  - [`Writer.set_compression()`](rosbags.rosbag2.html#rosbags.rosbag2.Writer.set_compression) — 设置压缩方式
  - [`Writer.set_custom_data()`](rosbags.rosbag2.html#rosbags.rosbag2.Writer.set_custom_data) — 设置自定义元数据
  - [`Writer.write()`](rosbags.rosbag2.html#rosbags.rosbag2.Writer.write) — 写入消息
- [`WriterError`](rosbags.rosbag2.html#rosbags.rosbag2.WriterError) — Writer 错误异常类

## rosbags.serde

序列化与反序列化模块，支持 ROS1 和 CDR（Common Data Representation）格式。

- [`SerdeError`](rosbags.serde.html#rosbags.serde.SerdeError) — 序列化错误异常类
- [`cdr_to_ros1()`](rosbags.serde.html#rosbags.serde.cdr_to_ros1) — 将 CDR 格式转换为 ROS1 格式
- [`deserialize_cdr()`](rosbags.serde.html#rosbags.serde.deserialize_cdr) — 反序列化 CDR 格式数据
- [`deserialize_ros1()`](rosbags.serde.html#rosbags.serde.deserialize_ros1) — 反序列化 ROS1 格式数据
- [`ros1_to_cdr()`](rosbags.serde.html#rosbags.serde.ros1_to_cdr) — 将 ROS1 格式转换为 CDR 格式
- [`serialize_cdr()`](rosbags.serde.html#rosbags.serde.serialize_cdr) — 序列化为 CDR 格式
- [`serialize_ros1()`](rosbags.serde.html#rosbags.serde.serialize_ros1) — 序列化为 ROS1 格式

## rosbags.typesys

类型系统模块，管理 ROS 消息类型的注册、加载和存储。

- [`Stores`](rosbags.typesys.html#rosbags.typesys.Stores) — 支持的 ROS 发行版（Store）枚举
  - [`Stores.EMPTY`](rosbags.typesys.html#rosbags.typesys.Stores.EMPTY) — 空存储
  - [`Stores.LATEST`](rosbags.typesys.html#rosbags.typesys.Stores.LATEST) — 最新版本存储
  - [`Stores.ROS1_NOETIC`](rosbags.typesys.html#rosbags.typesys.Stores.ROS1_NOETIC) — ROS1 Noetic
  - [`Stores.ROS2_DASHING`](rosbags.typesys.html#rosbags.typesys.Stores.ROS2_DASHING) — ROS2 Dashing
  - [`Stores.ROS2_ELOQUENT`](rosbags.typesys.html#rosbags.typesys.Stores.ROS2_ELOQUENT) — ROS2 Eloquent
  - [`Stores.ROS2_FOXY`](rosbags.typesys.html#rosbags.typesys.Stores.ROS2_FOXY) — ROS2 Foxy
  - [`Stores.ROS2_GALACTIC`](rosbags.typesys.html#rosbags.typesys.Stores.ROS2_GALACTIC) — ROS2 Galactic
  - [`Stores.ROS2_HUMBLE`](rosbags.typesys.html#rosbags.typesys.Stores.ROS2_HUMBLE) — ROS2 Humble
  - [`Stores.ROS2_IRON`](rosbags.typesys.html#rosbags.typesys.Stores.ROS2_IRON) — ROS2 Iron
  - [`Stores.ROS2_JAZZY`](rosbags.typesys.html#rosbags.typesys.Stores.ROS2_JAZZY) — ROS2 Jazzy
  - [`Stores.ROS2_KILTED`](rosbags.typesys.html#rosbags.typesys.Stores.ROS2_KILTED) — ROS2 Kilted
- [`TypesysError`](rosbags.typesys.html#rosbags.typesys.TypesysError) — 类型系统错误异常类
- [`get_types_from_idl()`](rosbags.typesys.html#rosbags.typesys.get_types_from_idl) — 从 IDL 文件解析消息类型
- [`get_types_from_msg()`](rosbags.typesys.html#rosbags.typesys.get_types_from_msg) — 从 msg 文件解析消息类型
- [`get_typestore()`](rosbags.typesys.html#rosbags.typesys.get_typestore) — 获取指定 Store 的类型存储（TypeStore）
- [`register_types()`](rosbags.typesys.html#rosbags.typesys.register_types) — 注册自定义消息类型

## rosbags.typesys.stores

各 ROS 发行版的预定义消息类型存储。每个 Store 包含对应 ROS 发行版的所有标准消息类型。

- [`Stores`](rosbags.typesys.stores.html#rosbags.typesys.stores.Stores) — 支持的 ROS 发行版枚举（同 rosbags.typesys.Stores）
  - `Stores.EMPTY`
  - `Stores.LATEST`
  - `Stores.ROS1_NOETIC`
  - `Stores.ROS2_DASHING`
  - `Stores.ROS2_ELOQUENT`
  - `Stores.ROS2_FOXY`
  - `Stores.ROS2_GALACTIC`
  - `Stores.ROS2_HUMBLE`
  - `Stores.ROS2_IRON`
  - `Stores.ROS2_JAZZY`
  - `Stores.ROS2_KILTED`
- [`get_typestore()`](rosbags.typesys.stores.html#rosbags.typesys.stores.get_typestore) — 获取指定 Store 的 TypeStore 实例

### rosbags.typesys.stores.empty

空存储，仅包含基础时间类型。

- `builtin_interfaces__msg__Duration`
- `builtin_interfaces__msg__Time`

### rosbags.typesys.stores.ros1_noetic

ROS1 Noetic 发行版的标准消息类型。

**actionlib 消息：**

- `actionlib__msg__TestAction`
- `actionlib__msg__TestActionFeedback`
- `actionlib__msg__TestActionGoal`
- `actionlib__msg__TestActionResult`
- `actionlib__msg__TestFeedback`
- `actionlib__msg__TestGoal`
- `actionlib__msg__TestRequestAction`
- `actionlib__msg__TestRequestActionFeedback`
- `actionlib__msg__TestRequestActionGoal`
- `actionlib__msg__TestRequestActionResult`
- `actionlib__msg__TestRequestFeedback`
- `actionlib__msg__TestRequestGoal`
- `actionlib__msg__TestRequestResult`
- `actionlib__msg__TestResult`
- `actionlib__msg__TwoIntsAction`
- `actionlib__msg__TwoIntsActionFeedback`
- `actionlib__msg__TwoIntsActionGoal`
- `actionlib__msg__TwoIntsActionResult`
- `actionlib__msg__TwoIntsFeedback`
- `actionlib__msg__TwoIntsGoal`
- `actionlib__msg__TwoIntsResult`

**actionlib_msgs 消息：**

- `actionlib_msgs__msg__GoalID`
- `actionlib_msgs__msg__GoalStatus`
- `actionlib_msgs__msg__GoalStatusArray`

**bond 消息：**

- `bond__msg__Constants`
- `bond__msg__Status`

**diagnostic_msgs 消息：**

- `diagnostic_msgs__msg__DiagnosticArray`
- `diagnostic_msgs__msg__DiagnosticStatus`
- `diagnostic_msgs__msg__KeyValue`

**dynamic_reconfigure 消息：**

- `dynamic_reconfigure__msg__BoolParameter`
- `dynamic_reconfigure__msg__Config`
- `dynamic_reconfigure__msg__ConfigDescription`
- `dynamic_reconfigure__msg__DoubleParameter`
- `dynamic_reconfigure__msg__Group`
- `dynamic_reconfigure__msg__GroupState`
- `dynamic_reconfigure__msg__IntParameter`
- `dynamic_reconfigure__msg__ParamDescription`
- `dynamic_reconfigure__msg__SensorLevels`
- `dynamic_reconfigure__msg__StrParameter`

**geometry_msgs 消息：**

- `geometry_msgs__msg__Accel`
- `geometry_msgs__msg__AccelStamped`
- `geometry_msgs__msg__AccelWithCovariance`
- `geometry_msgs__msg__AccelWithCovarianceStamped`
- `geometry_msgs__msg__Inertia`
- `geometry_msgs__msg__InertiaStamped`
- `geometry_msgs__msg__Point`
- `geometry_msgs__msg__Point32`
- `geometry_msgs__msg__PointStamped`
- `geometry_msgs__msg__Polygon`
- `geometry_msgs__msg__PolygonStamped`
- `geometry_msgs__msg__Pose`
- `geometry_msgs__msg__Pose2D`
- `geometry_msgs__msg__PoseArray`
- `geometry_msgs__msg__PoseStamped`
- `geometry_msgs__msg__PoseWithCovariance`
- `geometry_msgs__msg__PoseWithCovarianceStamped`
- `geometry_msgs__msg__Quaternion`
- `geometry_msgs__msg__QuaternionStamped`
- `geometry_msgs__msg__Transform`
- `geometry_msgs__msg__TransformStamped`
- `geometry_msgs__msg__Twist`
- `geometry_msgs__msg__TwistStamped`
- `geometry_msgs__msg__TwistWithCovariance`
- `geometry_msgs__msg__TwistWithCovarianceStamped`
- `geometry_msgs__msg__Vector3`
- `geometry_msgs__msg__Vector3Stamped`
- `geometry_msgs__msg__Wrench`
- `geometry_msgs__msg__WrenchStamped`

**nav_msgs 消息：**

- `nav_msgs__msg__GetMapAction`
- `nav_msgs__msg__GetMapActionFeedback`
- `nav_msgs__msg__GetMapActionGoal`
- `nav_msgs__msg__GetMapActionResult`
- `nav_msgs__msg__GetMapFeedback`
- `nav_msgs__msg__GetMapGoal`
- `nav_msgs__msg__GetMapResult`
- `nav_msgs__msg__GridCells`
- `nav_msgs__msg__MapMetaData`
- `nav_msgs__msg__OccupancyGrid`
- `nav_msgs__msg__Odometry`
- `nav_msgs__msg__Path`

**roscpp 消息：**

- `roscpp__msg__Logger`

**rosgraph_msgs 消息：**

- `rosgraph_msgs__msg__Clock`
- `rosgraph_msgs__msg__Log`
- `rosgraph_msgs__msg__TopicStatistics`

**sensor_msgs 消息：**

- `sensor_msgs__msg__BatteryState`
- `sensor_msgs__msg__CameraInfo`
- `sensor_msgs__msg__ChannelFloat32`
- `sensor_msgs__msg__CompressedImage`
- `sensor_msgs__msg__FluidPressure`
- `sensor_msgs__msg__Illuminance`
- `sensor_msgs__msg__Image`
- `sensor_msgs__msg__Imu`
- `sensor_msgs__msg__JointState`
- `sensor_msgs__msg__Joy`
- `sensor_msgs__msg__JoyFeedback`
- `sensor_msgs__msg__JoyFeedbackArray`
- `sensor_msgs__msg__LaserEcho`
- `sensor_msgs__msg__LaserScan`
- `sensor_msgs__msg__MagneticField`
- `sensor_msgs__msg__MultiDOFJointState`
- `sensor_msgs__msg__MultiEchoLaserScan`
- `sensor_msgs__msg__NavSatFix`
- `sensor_msgs__msg__NavSatStatus`
- `sensor_msgs__msg__PointCloud`
- `sensor_msgs__msg__PointCloud2`
- `sensor_msgs__msg__PointField`
- `sensor_msgs__msg__Range`
- `sensor_msgs__msg__RegionOfInterest`
- `sensor_msgs__msg__RelativeHumidity`
- `sensor_msgs__msg__Temperature`
- `sensor_msgs__msg__TimeReference`

**shape_msgs 消息：**

- `shape_msgs__msg__Mesh`
- `shape_msgs__msg__MeshTriangle`
- `shape_msgs__msg__Plane`
- `shape_msgs__msg__SolidPrimitive`

**std_msgs 消息：**

- `std_msgs__msg__Bool`
- `std_msgs__msg__Byte`
- `std_msgs__msg__ByteMultiArray`
- `std_msgs__msg__Char`
- `std_msgs__msg__ColorRGBA`
- `std_msgs__msg__Duration`
- `std_msgs__msg__Empty`
- `std_msgs__msg__Float32`
- `std_msgs__msg__Float32MultiArray`
- `std_msgs__msg__Float64`
- `std_msgs__msg__Float64MultiArray`
- `std_msgs__msg__Header`
- `std_msgs__msg__Int16`
- `std_msgs__msg__Int16MultiArray`
- `std_msgs__msg__Int32`
- `std_msgs__msg__Int32MultiArray`
- `std_msgs__msg__Int64`
- `std_msgs__msg__Int64MultiArray`
- `std_msgs__msg__Int8`
- `std_msgs__msg__Int8MultiArray`
- `std_msgs__msg__MultiArrayDimension`
- `std_msgs__msg__MultiArrayLayout`
- `std_msgs__msg__String`
- `std_msgs__msg__Time`
- `std_msgs__msg__UInt16`
- `std_msgs__msg__UInt16MultiArray`
- `std_msgs__msg__UInt32`
- `std_msgs__msg__UInt32MultiArray`
- `std_msgs__msg__UInt64`
- `std_msgs__msg__UInt64MultiArray`
- `std_msgs__msg__UInt8`
- `std_msgs__msg__UInt8MultiArray`

**stereo_msgs 消息：**

- `stereo_msgs__msg__DisparityImage`

**trajectory_msgs 消息：**

- `trajectory_msgs__msg__JointTrajectory`
- `trajectory_msgs__msg__JointTrajectoryPoint`
- `trajectory_msgs__msg__MultiDOFJointTrajectory`
- `trajectory_msgs__msg__MultiDOFJointTrajectoryPoint`

**visualization_msgs 消息：**

- `visualization_msgs__msg__ImageMarker`
- `visualization_msgs__msg__InteractiveMarker`
- `visualization_msgs__msg__InteractiveMarkerControl`
- `visualization_msgs__msg__InteractiveMarkerFeedback`
- `visualization_msgs__msg__InteractiveMarkerInit`
- `visualization_msgs__msg__InteractiveMarkerPose`
- `visualization_msgs__msg__InteractiveMarkerUpdate`
- `visualization_msgs__msg__Marker`
- `visualization_msgs__msg__MarkerArray`
- `visualization_msgs__msg__MenuEntry`

### rosbags.typesys.stores.ros2_dashing

ROS2 Dashing 发行版的标准消息类型。

**action_msgs 消息：**

- `action_msgs__msg__GoalInfo`
- `action_msgs__msg__GoalStatus`
- `action_msgs__msg__GoalStatusArray`

**actionlib_msgs 消息：**

- `actionlib_msgs__msg__GoalID`
- `actionlib_msgs__msg__GoalStatus`
- `actionlib_msgs__msg__GoalStatusArray`

**diagnostic_msgs 消息：**

- `diagnostic_msgs__msg__DiagnosticArray`
- `diagnostic_msgs__msg__DiagnosticStatus`
- `diagnostic_msgs__msg__KeyValue`

**geometry_msgs 消息：**

- `geometry_msgs__msg__Accel`
- `geometry_msgs__msg__AccelStamped`
- `geometry_msgs__msg__AccelWithCovariance`
- `geometry_msgs__msg__AccelWithCovarianceStamped`
- `geometry_msgs__msg__Inertia`
- `geometry_msgs__msg__InertiaStamped`
- `geometry_msgs__msg__Point`
- `geometry_msgs__msg__Point32`
- `geometry_msgs__msg__PointStamped`
- `geometry_msgs__msg__Polygon`
- `geometry_msgs__msg__PolygonStamped`
- `geometry_msgs__msg__Pose`
- `geometry_msgs__msg__Pose2D`
- `geometry_msgs__msg__PoseArray`
- `geometry_msgs__msg__PoseStamped`
- `geometry_msgs__msg__PoseWithCovariance`
- `geometry_msgs__msg__PoseWithCovarianceStamped`
- `geometry_msgs__msg__Quaternion`
- `geometry_msgs__msg__QuaternionStamped`
- `geometry_msgs__msg__Transform`
- `geometry_msgs__msg__TransformStamped`
- `geometry_msgs__msg__Twist`
- `geometry_msgs__msg__TwistStamped`
- `geometry_msgs__msg__TwistWithCovariance`
- `geometry_msgs__msg__TwistWithCovarianceStamped`
- `geometry_msgs__msg__Vector3`
- `geometry_msgs__msg__Vector3Stamped`
- `geometry_msgs__msg__Wrench`
- `geometry_msgs__msg__WrenchStamped`

**lifecycle_msgs 消息：**

- `lifecycle_msgs__msg__State`
- `lifecycle_msgs__msg__Transition`
- `lifecycle_msgs__msg__TransitionDescription`
- `lifecycle_msgs__msg__TransitionEvent`

**nav_msgs 消息：**

- `nav_msgs__msg__GridCells`
- `nav_msgs__msg__MapMetaData`
- `nav_msgs__msg__OccupancyGrid`
- `nav_msgs__msg__Odometry`
- `nav_msgs__msg__Path`

**rcl_interfaces 消息：**

- `rcl_interfaces__msg__FloatingPointRange`
- `rcl_interfaces__msg__IntegerRange`
- `rcl_interfaces__msg__IntraProcessMessage`
- `rcl_interfaces__msg__ListParametersResult`
- `rcl_interfaces__msg__Log`
- `rcl_interfaces__msg__Parameter`
- `rcl_interfaces__msg__ParameterDescriptor`
- `rcl_interfaces__msg__ParameterEvent`
- `rcl_interfaces__msg__ParameterEventDescriptors`
- `rcl_interfaces__msg__ParameterType`
- `rcl_interfaces__msg__ParameterValue`
- `rcl_interfaces__msg__SetParametersResult`

**rosgraph_msgs 消息：**

- `rosgraph_msgs__msg__Clock`

**sensor_msgs 消息：**

- `sensor_msgs__msg__BatteryState`
- `sensor_msgs__msg__CameraInfo`
- `sensor_msgs__msg__ChannelFloat32`
- `sensor_msgs__msg__CompressedImage`
- `sensor_msgs__msg__FluidPressure`
- `sensor_msgs__msg__Illuminance`
- `sensor_msgs__msg__Image`
- `sensor_msgs__msg__Imu`
- `sensor_msgs__msg__JointState`
- `sensor_msgs__msg__Joy`
- `sensor_msgs__msg__JoyFeedback`
- `sensor_msgs__msg__JoyFeedbackArray`
- `sensor_msgs__msg__LaserEcho`
- `sensor_msgs__msg__LaserScan`
- `sensor_msgs__msg__MagneticField`
- `sensor_msgs__msg__MultiDOFJointState`
- `sensor_msgs__msg__MultiEchoLaserScan`
- `sensor_msgs__msg__NavSatFix`
- `sensor_msgs__msg__NavSatStatus`
- `sensor_msgs__msg__PointCloud`
- `sensor_msgs__msg__PointCloud2`
- `sensor_msgs__msg__PointField`
- `sensor_msgs__msg__Range`
- `sensor_msgs__msg__RegionOfInterest`
- `sensor_msgs__msg__RelativeHumidity`
- `sensor_msgs__msg__Temperature`
- `sensor_msgs__msg__TimeReference`

**shape_msgs 消息：**

- `shape_msgs__msg__Mesh`
- `shape_msgs__msg__MeshTriangle`
- `shape_msgs__msg__Plane`
- `shape_msgs__msg__SolidPrimitive`

**std_msgs 消息：**

- `std_msgs__msg__Bool`
- `std_msgs__msg__Byte`
- `std_msgs__msg__ByteMultiArray`
- `std_msgs__msg__Char`
- `std_msgs__msg__ColorRGBA`
- `std_msgs__msg__Empty`
- `std_msgs__msg__Float32`
- `std_msgs__msg__Float32MultiArray`
- `std_msgs__msg__Float64`
- `std_msgs__msg__Float64MultiArray`
- `std_msgs__msg__Header`
- `std_msgs__msg__Int16`
- `std_msgs__msg__Int16MultiArray`
- `std_msgs__msg__Int32`
- `std_msgs__msg__Int32MultiArray`
- `std_msgs__msg__Int64`
- `std_msgs__msg__Int64MultiArray`
- `std_msgs__msg__Int8`
- `std_msgs__msg__Int8MultiArray`
- `std_msgs__msg__MultiArrayDimension`
- `std_msgs__msg__MultiArrayLayout`
- `std_msgs__msg__String`
- `std_msgs__msg__UInt16`
- `std_msgs__msg__UInt16MultiArray`
- `std_msgs__msg__UInt32`
- `std_msgs__msg__UInt32MultiArray`
- `std_msgs__msg__UInt64`
- `std_msgs__msg__UInt64MultiArray`
- `std_msgs__msg__UInt8`
- `std_msgs__msg__UInt8MultiArray`

**stereo_msgs 消息：**

- `stereo_msgs__msg__DisparityImage`

**tf2_msgs 消息：**

- `tf2_msgs__msg__TF2Error`
- `tf2_msgs__msg__TFMessage`

**trajectory_msgs 消息：**

- `trajectory_msgs__msg__JointTrajectory`
- `trajectory_msgs__msg__JointTrajectoryPoint`
- `trajectory_msgs__msg__MultiDOFJointTrajectory`
- `trajectory_msgs__msg__MultiDOFJointTrajectoryPoint`

**unique_identifier_msgs 消息：**

- `unique_identifier_msgs__msg__UUID`

**visualization_msgs 消息：**

- `visualization_msgs__msg__ImageMarker`
- `visualization_msgs__msg__InteractiveMarker`
- `visualization_msgs__msg__InteractiveMarkerControl`
- `visualization_msgs__msg__InteractiveMarkerFeedback`
- `visualization_msgs__msg__InteractiveMarkerInit`
- `visualization_msgs__msg__InteractiveMarkerPose`
- `visualization_msgs__msg__InteractiveMarkerUpdate`
- `visualization_msgs__msg__Marker`
- `visualization_msgs__msg__MarkerArray`
- `visualization_msgs__msg__MenuEntry`

### rosbags.typesys.stores.ros2_eloquent

ROS2 Eloquent 发行版的标准消息类型（继承自 Dashing，无额外独占类型）。

### rosbags.typesys.stores.ros2_foxy

ROS2 Foxy 发行版的标准消息类型。在继承 Dashing/Eloquent 基础上新增：

**libstatistics_collector 消息：**

- `libstatistics_collector__msg__DummyMessage`

**rmw_dds_common 消息：**

- `rmw_dds_common__msg__Gid`
- `rmw_dds_common__msg__NodeEntitiesInfo`
- `rmw_dds_common__msg__ParticipantEntitiesInfo`

**statistics_msgs 消息：**

- `statistics_msgs__msg__MetricsMessage`
- `statistics_msgs__msg__StatisticDataPoint`
- `statistics_msgs__msg__StatisticDataType`

**visualization_msgs 消息（新增）：**

- `visualization_msgs__msg__ImageMarker`
- `visualization_msgs__msg__Marker`

### rosbags.typesys.stores.ros2_galactic

ROS2 Galactic 发行版的标准消息类型。在继承 Foxy 基础上新增：

**rcl_interfaces 消息（新增）：**

- `rcl_interfaces__msg__ParameterDescriptor`

### rosbags.typesys.stores.ros2_humble

ROS2 Humble 发行版的标准消息类型。在继承 Galactic 基础上新增：

- `rosbag2_interfaces__msg__ReadSplitEvent`
- `rosbag2_interfaces__msg__WriteSplitEvent`
- `shape_msgs__msg__SolidPrimitive`
- `visualization_msgs__msg__Marker`
- `visualization_msgs__msg__MeshFile`
- `visualization_msgs__msg__UVCoordinate`

### rosbags.typesys.stores.ros2_iron

ROS2 Iron 发行版的标准消息类型。在继承 Humble 基础上新增：

- `rcl_interfaces__msg__LoggerLevel`
- `rcl_interfaces__msg__SetLoggerLevelsResult`
- `rmw_dds_common__msg__Gid`
- `sensor_msgs__msg__BatteryState`
- `sensor_msgs__msg__Range`
- `service_msgs__msg__ServiceEventInfo`
- `type_description_interfaces__msg__Field`
- `type_description_interfaces__msg__FieldType`
- `type_description_interfaces__msg__IndividualTypeDescription`
- `type_description_interfaces__msg__KeyValue`
- `type_description_interfaces__msg__TypeDescription`
- `type_description_interfaces__msg__TypeSource`

### rosbags.typesys.stores.ros2_jazzy

ROS2 Jazzy 发行版的标准消息类型。在继承 Iron 基础上新增：

- `geometry_msgs__msg__PolygonInstance`
- `geometry_msgs__msg__PolygonInstanceStamped`
- `geometry_msgs__msg__VelocityStamped`
- `rcl_interfaces__msg__Log`
- `rosbag2_interfaces__msg__ReadSplitEvent`
- `rosbag2_interfaces__msg__WriteSplitEvent`
- `sensor_msgs__msg__NavSatStatus`
- `visualization_msgs__msg__Marker`

### rosbags.typesys.stores.ros2_kilted

ROS2 Kilted 发行版的标准消息类型。在继承 Jazzy 基础上新增：

- `nav_msgs__msg__Goals`

---

[← 与原生 ROS 配合使用](../examples/与%20Native%20ROS%20栈配合使用.md)
