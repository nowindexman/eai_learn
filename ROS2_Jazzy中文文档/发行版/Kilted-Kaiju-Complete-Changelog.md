> 原文地址：https://docs.ros.org/en/jazzy/Releases/Kilted-Kaiju-Complete-Changelog.html

# ROS 2 Kilted Kaiju Complete Changelog

This page is a list of the complete changes in all ROS 2 core packages since the previous release.

   :local:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `action_msgs <https://github.com/ros2/rcl_interfaces/tree/kilted/action_msgs/CHANGELOG.rst>`__

* Add missing build_export_depend on rosidl_core_runtime ([#165 ](https://github.com/ros2/rcl_interfaces/issues/165)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `action_tutorials_cpp <https://github.com/ros2/demos/tree/kilted/action_tutorials/action_tutorials_cpp/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_) demo_nodes_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
* Update action cpp demos to support setting introspection ([#709 ](https://github.com/ros2/demos/issues/709)_) * Update action cpp demos to support setting introspection * Add the missing header file declaration ---------
* Remove action_tutorials_interfaces. ([#701 ](https://github.com/ros2/demos/issues/701)_)
* Removed outdated comment ([#699 ](https://github.com/ros2/demos/issues/699)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `action_tutorials_py <https://github.com/ros2/demos/tree/kilted/action_tutorials/action_tutorials_py/CHANGELOG.rst>`__

* Update action python demos to support setting introspection ([#708 ](https://github.com/ros2/demos/issues/708)_) * Update action python demos to support setting introspection * Correct the errors in the document ---------
* Add test_xmllint.py to all of the ament_python packages. ([#704 ](https://github.com/ros2/demos/issues/704)_)
* Remove action_tutorials_interfaces. ([#701 ](https://github.com/ros2/demos/issues/701)_)
* Change all of the demos to use the new rclpy context manager. ([#694 ](https://github.com/ros2/demos/issues/694)_)
* Contributors: Barry Xu, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_clang_format <https://github.com/ament/ament_lint/tree/kilted/ament_clang_format/CHANGELOG.rst>`__

* Add ament_xmllint testing for all packages that we can. ([#508 ](https://github.com/ament/ament_lint/issues/508)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_clang_tidy <https://github.com/ament/ament_lint/tree/kilted/ament_clang_tidy/CHANGELOG.rst>`__

* Add ament_xmllint testing for all packages that we can. ([#508 ](https://github.com/ament/ament_lint/issues/508)_)
* ament_clang_tidy - Fix Reporting when WarningsAsErrors is specified in config ([#397 ](https://github.com/ament/ament_lint/issues/397)_)
* Contributors: Chris Lalancette, Matt Condino


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_auto <https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_auto/CHANGELOG.rst>`__

* Fix headers destination installed by ament_auto_package ([#540 ](https://github.com/ament/ament_cmake/issues/540)_)
* Add ament_auto_depend_on_packages to replace ament_target_dependencies ([#571 ](https://github.com/ament/ament_cmake/issues/571)_)
* More specific prefix in some cmake_parse_argument calls ([#523 ](https://github.com/ament/ament_cmake/issues/523)_)
* Contributors: Kevin Egger, Kotaro Yoshimoto, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_core <https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_core/CHANGELOG.rst>`__

* Create destination directory during symlink install ([#569 ](https://github.com/ament/ament_cmake/issues/569)_)
* Support generator expressions when symlinking install(FILES) ([#560 ](https://github.com/ament/ament_cmake/issues/560)_)
* Always symlink TARGET\_{LINKER,SONAME}_FILE on libraries ([#535 ](https://github.com/ament/ament_cmake/issues/535)_)
* Fix symlink install of versioned libs on macOS ([#558 ](https://github.com/ament/ament_cmake/issues/558)_)
* More specific prefix in some cmake_parse_argument calls ([#523 ](https://github.com/ament/ament_cmake/issues/523)_)
* Contributors: Ezra Brooks, Kevin Egger, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_gen_version_h <https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_gen_version_h/CHANGELOG.rst>`__

* Add ALL target for ament_generate_version_header target. ([#526 ](https://github.com/ament/ament_cmake/issues/526)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_gtest <https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_gtest/CHANGELOG.rst>`__

* set search path args and then append ([#543 ](https://github.com/ament/ament_cmake/issues/543)_)
* Contributors: Will


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_pytest <https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_pytest/CHANGELOG.rst>`__

* Don't write Python bytecode when invoking pytest ([#533 ](https://github.com/ament/ament_cmake/issues/533)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_ros <https://github.com/ros2/ament_cmake_ros/tree/kilted/ament_cmake_ros/CHANGELOG.rst>`__

* Add ament_add_ros_isolated\_{gmock,gtest}_test macros ([#29 ](https://github.com/ros2/ament_cmake_ros/issues/29)_)
* Switch from 'domain_coordinator' to 'rmw_test_fixture' ([#28 ](https://github.com/ros2/ament_cmake_ros/issues/28)_)
* Add ament_add_ros_isolated_test function ([#27 ](https://github.com/ros2/ament_cmake_ros/issues/27)_)
* Split generic parts of ament_cmake_ros into _core package ([#20 ](https://github.com/ros2/ament_cmake_ros/issues/20)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_ros_core <https://github.com/ros2/ament_cmake_ros/tree/kilted/ament_cmake_ros_core/CHANGELOG.rst>`__

* Add missing build_export_depend on ament_cmake_libraries ([#37 ](https://github.com/ros2/ament_cmake_ros/issues/37)_)
* Split generic parts of ament_cmake_ros into _core package ([#20 ](https://github.com/ros2/ament_cmake_ros/issues/20)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_target_dependencies <https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_target_dependencies/CHANGELOG.rst>`__

* Deprecate ament_target_dependencies() ([#572 ](https://github.com/ament/ament_cmake/issues/572)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_vendor_package <https://github.com/ament/ament_cmake/tree/kilted/ament_cmake_vendor_package/CHANGELOG.rst>`__

* Add explicit git dependency from ament_cmake_vendor_package ([#554 ](https://github.com/ament/ament_cmake/issues/554)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_copyright <https://github.com/ament/ament_lint/tree/kilted/ament_copyright/CHANGELOG.rst>`__

* Improve ament_copyright performance drastically. ([#515 ](https://github.com/ament/ament_lint/issues/515)_)
* Fix error path for search_copyright_information. ([#491 ](https://github.com/ament/ament_lint/issues/491)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cppcheck <https://github.com/ament/ament_lint/tree/kilted/ament_cppcheck/CHANGELOG.rst>`__

* Add ament_xmllint testing for all packages that we can. ([#508 ](https://github.com/ament/ament_lint/issues/508)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cpplint <https://github.com/ament/ament_lint/tree/kilted/ament_cpplint/CHANGELOG.rst>`__

* Enable a quiet mode for cpplint ([#532 ](https://github.com/ament/ament_lint/issues/532)_)
* Add ament_xmllint testing for all packages that we can. ([#508 ](https://github.com/ament/ament_lint/issues/508)_)
* Contributors: Chris Lalancette, Nils-Christian Iseke


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_flake8 <https://github.com/ament/ament_lint/tree/kilted/ament_flake8/CHANGELOG.rst>`__

* Add the rest of the flake8 plugins as dependencies. ([#503 ](https://github.com/ament/ament_lint/issues/503)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_index_python <https://github.com/ament/ament_index/tree/kilted/ament_index_python/CHANGELOG.rst>`__

* Add py.typed to package_data ([#100 ](https://github.com/ament/ament_index/issues/100)_)
* Add test_xmllint to ament_index_python. ([#96 ](https://github.com/ament/ament_index/issues/96)_)
* Add ament_mypy unit test and export types ([#95 ](https://github.com/ament/ament_index/issues/95)_)
* Contributors: Chris Lalancette, Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_lint_auto <https://github.com/ament/ament_lint/tree/kilted/ament_lint_auto/CHANGELOG.rst>`__

* Add docu for AMENT_LINT_AUTO_EXCLUDE ([#524 ](https://github.com/ament/ament_lint/issues/524)_)
* Contributors: Alexander Reimann


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_lint_cmake <https://github.com/ament/ament_lint/tree/kilted/ament_lint_cmake/CHANGELOG.rst>`__

* Add ament_xmllint testing for all packages that we can. ([#508 ](https://github.com/ament/ament_lint/issues/508)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_mypy <https://github.com/ament/ament_lint/tree/kilted/ament_mypy/CHANGELOG.rst>`__

* Fix Windows Regression by removing removesuffix() ([#530 ](https://github.com/ament/ament_lint/issues/530)_)
* Export typing information ([#487 ](https://github.com/ament/ament_lint/issues/487)_)
* Add support for type stubs ([#516 ](https://github.com/ament/ament_lint/issues/516)_)
* Add ament_xmllint testing for all packages that we can. ([#508 ](https://github.com/ament/ament_lint/issues/508)_)
* Contributors: Chris Lalancette, Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_package <https://github.com/ament/ament_package/tree/kilted/CHANGELOG.rst>`__

* Simplify removing leading and trailing separators ([#152 ](https://github.com/ament/ament_package/issues/152)_)
* Remove CODEOWNERS and mirror-rolling-to-master. ([#149 ](https://github.com/ament/ament_package/issues/149)_)
* Always consider .dsv files, even when no shell specific script exists ([#147 ](https://github.com/ament/ament_package/issues/147)_)
* Contributors: Addisu Z. Taddese, Chris Lalancette, Rob Woolley


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_pclint <https://github.com/ament/ament_lint/tree/kilted/ament_pclint/CHANGELOG.rst>`__

* Add ament_xmllint testing for all packages that we can. ([#508 ](https://github.com/ament/ament_lint/issues/508)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_pycodestyle <https://github.com/ament/ament_lint/tree/kilted/ament_pycodestyle/CHANGELOG.rst>`__

* Add ament_xmllint testing for all packages that we can. ([#508 ](https://github.com/ament/ament_lint/issues/508)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_pyflakes <https://github.com/ament/ament_lint/tree/kilted/ament_pyflakes/CHANGELOG.rst>`__

* Add ament_xmllint testing for all packages that we can. ([#508 ](https://github.com/ament/ament_lint/issues/508)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_uncrustify <https://github.com/ament/ament_lint/tree/kilted/ament_uncrustify/CHANGELOG.rst>`__

* Add ament_xmllint testing for all packages that we can. ([#508 ](https://github.com/ament/ament_lint/issues/508)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_xmllint <https://github.com/ament/ament_lint/tree/kilted/ament_xmllint/CHANGELOG.rst>`__

* Add ament_xmllint testing for all packages that we can. ([#508 ](https://github.com/ament/ament_lint/issues/508)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `builtin_interfaces <https://github.com/ros2/rcl_interfaces/tree/kilted/builtin_interfaces/CHANGELOG.rst>`__

* Add missing build_export_depend on rosidl_core_runtime ([#165 ](https://github.com/ros2/rcl_interfaces/issues/165)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `camera_calibration_parsers <https://github.com/ros-perception/image_common/tree/kilted/camera_calibration_parsers/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#345 ](https://github.com/ros-perception/image_common/issues/345)_)
* Added common linters to camera_calibration_parsers ([#317 ](https://github.com/ros-perception/image_common/issues/317)_)
* Contributors: Alejandro Hernández Cordero, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `camera_info_manager <https://github.com/ros-perception/image_common/tree/kilted/camera_info_manager/CHANGELOG.rst>`__

* Add optional namespace to /set_camera_info service in CameraInfoManager ([#324 ](https://github.com/ros-perception/image_common/issues/324)_)
* Added common test to camera info manager ([#318 ](https://github.com/ros-perception/image_common/issues/318)_)
* Contributors: Alejandro Hernández Cordero, Jan Hernas


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `camera_info_manager_py <https://github.com/ros-perception/image_common/tree/kilted/camera_info_manager_py/CHANGELOG.rst>`__

* Cleanup of camera_info_manager_py. ([#340 ](https://github.com/ros-perception/image_common/issues/340)_)
* Add [`camera_info_manager_py`` (`#335 ](https://github.com/ros-perception/image_common/issues/335)_)
* Bump package version to synchronize with image_common
* Ros2 ([#2 ](https://github.com/clearpathrobotics/camera_info_manager_py/issues/2)_) * Run magic converter * Ament_python package * Fix some imports * Remove references to cpp camera info manager. Disable tests * Linting * Fully Remove old tests * Add lint tests * Final tests * Remove pep257 from depends
* changelog
* added CPR maintainer
* Release to Melodic and Noetic
* Only use rostest when testing enabled, thanks to Lukas Bulwahn.
* Move repository to ros-perception.
* Add namespace parameter to constructor, so a driver can handle multiple cameras. Enhancement thanks to Martin Llofriu.
* Make unit tests conditional on ``CATKIN_ENABLE_TESTING``.
* Release to Groovy and Hydro.
* Set null calibration even when URL invalid (#7).
* Release to Groovy and Hydro.
* Convert to catkin.
* Remove roslib dependency.
* Release to Groovy and Hydro.
* Initial Python camera_info_manager release to Fuerte.
* Contributors: Alejandro Hernández Cordero, Chris Iverach-Brereton, Chris Lalancette, Jack O'Quin, José Mastrangelo, Lucas Walter, Lukas Bulwahn, Martin Pecka, Michael Hosmar, mllofriu


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `composition <https://github.com/ros2/demos/tree/kilted/composition/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Fix typo in composition comment ([#703 ](https://github.com/ros2/demos/issues/703)_)
* Change references from "jazzy" to "rolling" on the rolling branch. ([#687 ](https://github.com/ros2/demos/issues/687)_)
* [composition] add launch action console output in the verify section ([#677 ](https://github.com/ros2/demos/issues/677)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Mikael Arguedas, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `demo_nodes_cpp <https://github.com/ros2/demos/tree/kilted/demo_nodes_cpp/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* [demo_nodes_cpp] some readme and executable name fixups ([#678 ](https://github.com/ros2/demos/issues/678)_)
* Fix gcc warnings when building with optimizations. ([#672 ](https://github.com/ros2/demos/issues/672)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Mikael Arguedas, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `demo_nodes_cpp_native <https://github.com/ros2/demos/tree/kilted/demo_nodes_cpp_native/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `demo_nodes_py <https://github.com/ros2/demos/tree/kilted/demo_nodes_py/CHANGELOG.rst>`__

* Revert "Revert "fix loading parameter behavior from yaml file. ([#656 ](https://github.com/ros2/demos/issues/656)_)" ([#660 ](https://github.com/ros2/demos/issues/660)_)" ([#661 ](https://github.com/ros2/demos/issues/661)_)
* Add test_xmllint.py to all of the ament_python packages. ([#704 ](https://github.com/ros2/demos/issues/704)_)
* Change all of the demos to use the new rclpy context manager. ([#694 ](https://github.com/ros2/demos/issues/694)_)
* Contributors: Chris Lalancette, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `domain_coordinator <https://github.com/ros2/ament_cmake_ros/tree/kilted/domain_coordinator/CHANGELOG.rst>`__

* Add test_xmllint to domain_coordinator. ([#17 ](https://github.com/ros2/ament_cmake_ros/issues/17)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `dummy_map_server <https://github.com/ros2/demos/tree/kilted/dummy_robot/dummy_map_server/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_) demo_nodes_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `dummy_robot_bringup <https://github.com/ros2/demos/tree/kilted/dummy_robot/dummy_robot_bringup/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_) demo_nodes_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `dummy_sensors <https://github.com/ros2/demos/tree/kilted/dummy_robot/dummy_sensors/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_) demo_nodes_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Update dummy_sensors readme to echo the correct topic ([#675 ](https://github.com/ros2/demos/issues/675)_)
* Contributors: Shane Loretz, jmackay2, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_async_client <https://github.com/ros2/examples/tree/kilted/rclcpp/services/async_client/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_cbg_executor <https://github.com/ros2/examples/tree/kilted/rclcpp/executors/cbg_executor/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_action_client <https://github.com/ros2/examples/tree/kilted/rclcpp/actions/minimal_action_client/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Removed outdated comment ([#388 ](https://github.com/ros2/examples/issues/388)_)
* Contributors: Alejandro Hernández Cordero, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_action_server <https://github.com/ros2/examples/tree/kilted/rclcpp/actions/minimal_action_server/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Removed outdated comment ([#388 ](https://github.com/ros2/examples/issues/388)_)
* Contributors: Alejandro Hernández Cordero, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_client <https://github.com/ros2/examples/tree/kilted/rclcpp/services/minimal_client/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_composition <https://github.com/ros2/examples/tree/kilted/rclcpp/composition/minimal_composition/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_publisher <https://github.com/ros2/examples/tree/kilted/rclcpp/topics/minimal_publisher/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_service <https://github.com/ros2/examples/tree/kilted/rclcpp/services/minimal_service/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_subscriber <https://github.com/ros2/examples/tree/kilted/rclcpp/topics/minimal_subscriber/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_timer <https://github.com/ros2/examples/tree/kilted/rclcpp/timers/minimal_timer/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_multithreaded_executor <https://github.com/ros2/examples/tree/kilted/rclcpp/executors/multithreaded_executor/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_wait_set <https://github.com/ros2/examples/tree/kilted/rclcpp/wait_set/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_executors <https://github.com/ros2/examples/tree/kilted/rclpy/executors/CHANGELOG.rst>`__

* Add in ament_xmllint for the ament_python packages. ([#397 ](https://github.com/ros2/examples/issues/397)_)
* Switch to using the rclpy context manager everywhere. ([#389 ](https://github.com/ros2/examples/issues/389)_)
* Update the shutdown handling in all of the Python examples. ([#379 ](https://github.com/ros2/examples/issues/379)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_guard_conditions <https://github.com/ros2/examples/tree/kilted/rclpy/guard_conditions/CHANGELOG.rst>`__

* Add in ament_xmllint for the ament_python packages. ([#397 ](https://github.com/ros2/examples/issues/397)_)
* Switch to using the rclpy context manager everywhere. ([#389 ](https://github.com/ros2/examples/issues/389)_)
* Update the shutdown handling in all of the Python examples. ([#379 ](https://github.com/ros2/examples/issues/379)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_action_client <https://github.com/ros2/examples/tree/kilted/rclpy/actions/minimal_action_client/CHANGELOG.rst>`__

* Add in ament_xmllint for the ament_python packages. ([#397 ](https://github.com/ros2/examples/issues/397)_)
* Switch to using the rclpy context manager everywhere. ([#389 ](https://github.com/ros2/examples/issues/389)_)
* Update the shutdown handling in all of the Python examples. ([#379 ](https://github.com/ros2/examples/issues/379)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_action_server <https://github.com/ros2/examples/tree/kilted/rclpy/actions/minimal_action_server/CHANGELOG.rst>`__

* Add in ament_xmllint for the ament_python packages. ([#397 ](https://github.com/ros2/examples/issues/397)_)
* Switch to using the rclpy context manager everywhere. ([#389 ](https://github.com/ros2/examples/issues/389)_)
* Add guard on Python single goal action server example ([#380 ](https://github.com/ros2/examples/issues/380)_)
* Update the shutdown handling in all of the Python examples. ([#379 ](https://github.com/ros2/examples/issues/379)_)
* Contributors: Chris Lalancette, Ruddick Lawrence


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_client <https://github.com/ros2/examples/tree/kilted/rclpy/services/minimal_client/CHANGELOG.rst>`__

* Add in ament_xmllint for the ament_python packages. ([#397 ](https://github.com/ros2/examples/issues/397)_)
* Switch to using the rclpy context manager everywhere. ([#389 ](https://github.com/ros2/examples/issues/389)_)
* Use a single executor instance for spinning in client_async_callback. ([#382 ](https://github.com/ros2/examples/issues/382)_)
* Update the shutdown handling in all of the Python examples. ([#379 ](https://github.com/ros2/examples/issues/379)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_publisher <https://github.com/ros2/examples/tree/kilted/rclpy/topics/minimal_publisher/CHANGELOG.rst>`__

* Address flake8 errors for examples_rclpy_minimal_publisher ([#410 ](https://github.com/ros2/examples/issues/410)_)
* Add publisher_member_function_with_wait_for_all_acked.py ([#407 ](https://github.com/ros2/examples/issues/407)_)
* Add in ament_xmllint for the ament_python packages. ([#397 ](https://github.com/ros2/examples/issues/397)_)
* Switch to using the rclpy context manager everywhere. ([#389 ](https://github.com/ros2/examples/issues/389)_)
* Update the shutdown handling in all of the Python examples. ([#379 ](https://github.com/ros2/examples/issues/379)_)
* Contributors: Chris Lalancette, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_service <https://github.com/ros2/examples/tree/kilted/rclpy/services/minimal_service/CHANGELOG.rst>`__

* Add in ament_xmllint for the ament_python packages. ([#397 ](https://github.com/ros2/examples/issues/397)_)
* Switch to using the rclpy context manager everywhere. ([#389 ](https://github.com/ros2/examples/issues/389)_)
* Update the shutdown handling in all of the Python examples. ([#379 ](https://github.com/ros2/examples/issues/379)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_subscriber <https://github.com/ros2/examples/tree/kilted/rclpy/topics/minimal_subscriber/CHANGELOG.rst>`__

* Add in ament_xmllint for the ament_python packages. ([#397 ](https://github.com/ros2/examples/issues/397)_)
* Switch to using the rclpy context manager everywhere. ([#389 ](https://github.com/ros2/examples/issues/389)_)
* Update the shutdown handling in all of the Python examples. ([#379 ](https://github.com/ros2/examples/issues/379)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_pointcloud_publisher <https://github.com/ros2/examples/tree/kilted/rclpy/topics/pointcloud_publisher/CHANGELOG.rst>`__

* Add in ament_xmllint for the ament_python packages. ([#397 ](https://github.com/ros2/examples/issues/397)_)
* Switch to using the rclpy context manager everywhere. ([#389 ](https://github.com/ros2/examples/issues/389)_)
* Update the shutdown handling in all of the Python examples. ([#379 ](https://github.com/ros2/examples/issues/379)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_tf2_py <https://github.com/ros2/geometry2/tree/kilted/examples_tf2_py/CHANGELOG.rst>`__

* Add in test_xmllint for geometry2 python packages. ([#725 ](https://github.com/ros2/geometry2/issues/725)_)
* Switch to using a context manager for the python examples. ([#700 ](https://github.com/ros2/geometry2/issues/700)_) That way we can be sure to always clean up, but use less code doing so.
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `foonathan_memory_vendor <https://github.com/eProsima/foonathan_memory_vendor/tree/master/CHANGELOG.rst>`__

* Improve mechanism to find an installation of foonathan_memory (#67)


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `geometry2 <https://github.com/ros2/geometry2/tree/kilted/geometry2/CHANGELOG.rst>`__

* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `geometry_msgs <https://github.com/ros2/common_interfaces/tree/kilted/geometry_msgs/CHANGELOG.rst>`__

* Complete Removal of PoseStampedArray ([#270 ](https://github.com/ros2/common_interfaces/issues/270)_)
* Move geometry_msgs/PoseStampedArray to nav_msgs/Goals ([#269 ](https://github.com/ros2/common_interfaces/issues/269)_)
* Add PoseStampedArray ([#262 ](https://github.com/ros2/common_interfaces/issues/262)_)
* Contributors: Tony Najjar, Tully Foote


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `gmock_vendor <https://github.com/ament/googletest/tree/kilted/googlemock/CHANGELOG.rst>`__

* Bump minimum CMake version to 3.15 ([#31 ](https://github.com/ament/googletest/issues/31)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `google_benchmark_vendor <https://github.com/ament/google_benchmark_vendor/tree/kilted/CHANGELOG.rst>`__

* Bump minimum CMake version to 3.10 ([#35 ](https://github.com/ament/google_benchmark_vendor/issues/35)_)
* Remove CODEOWNERS and mirror-rolling-to-main workflow. ([#31 ](https://github.com/ament/google_benchmark_vendor/issues/31)_)
* Contributors: Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `gtest_vendor <https://github.com/ament/googletest/tree/kilted/googletest/CHANGELOG.rst>`__

* Bump minimum CMake version to 3.15 ([#33 ](https://github.com/ament/googletest/issues/33)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `gz_cmake_vendor <https://github.com/gazebo-release/gz_cmake_vendor/tree/kilted/CHANGELOG.rst>`__

* Bump version to 4.1.1 ([#13 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/13)_)
* Bump version to 4.1.0 ([#11 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/11)_)
* Bump version to 4.0.0 ([#10 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/10)_)
* Fixes the cmake-config used during find_package ([#8 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/8)_) The provided cmake-config was not actually working if one did ``` find_package(gz_cmake_vendor) find_package(gz-cmake) ``` This because the config file tried to create aliases to targets that don't exist. For example, gz-cmake4::gz-cmake4 is not exported by gz-cmake.
* Remove the BUILD_DOCS cmake argument. ([#9 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/9)_) It is apparently deprecated in newer Gazebo.
* Apply prerelease suffix and remove patch ([#7 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/7)_)
* Upgrade to Ionic
* Contributors: Addisu Z. Taddese, Chris Lalancette, Steve Peters


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `gz_math_vendor <https://github.com/gazebo-release/gz_math_vendor/tree/kilted/CHANGELOG.rst>`__

* Bump version to 8.1.1 ([#10 ](https://github.com/gazebo-release/gz_math_vendor/issues/10)_)
* Bump version to 8.1.0 ([#8 ](https://github.com/gazebo-release/gz_math_vendor/issues/8)_) * This is a rerelease since #7 did not actually bump the version of the vendored package.
* Bump version to 8.1.0 ([#7 ](https://github.com/gazebo-release/gz_math_vendor/issues/7)_)
* Bump version to 8.0.0 ([#5 ](https://github.com/gazebo-release/gz_math_vendor/issues/5)_)
* Apply prerelease suffix ([#4 ](https://github.com/gazebo-release/gz_math_vendor/issues/4)_)
* Upgrade to Ionic
* Update vendored package version to 7.5.0
* Contributors: Addisu Z. Taddese, Carlos Agüero, Michael Carroll


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `gz_utils_vendor <https://github.com/gazebo-release/gz_utils_vendor/tree/kilted/CHANGELOG.rst>`__

* Bump version to 3.1.1 ([#10 ](https://github.com/gazebo-release/gz_utils_vendor/issues/10)_)
* Bump version to 3.1.0 ([#8 ](https://github.com/gazebo-release/gz_utils_vendor/issues/8)_)
* Bump version to 3.0.0 ([#7 ](https://github.com/gazebo-release/gz_utils_vendor/issues/7)_)
* Add in a dependency on spdlog_vendor. ([#6 ](https://github.com/gazebo-release/gz_utils_vendor/issues/6)_) * Add in a dependency on spdlog_vendor. That way when building on e.g. Windows, the paths to spdlog will be setup properly before trying to build this vendor package. * Also remove the spdlog dependency. That's because we will just depend on the vendor package to provide that dependency for us as necessary. ---------
* Remove the BUILD_DOCS cmake argument. ([#5 ](https://github.com/gazebo-release/gz_utils_vendor/issues/5)_) It is apparently deprecated in newer Gazebo.
* Apply prerelease suffix ([#4 ](https://github.com/gazebo-release/gz_utils_vendor/issues/4)_)
* Upgrade to Ionic
* Contributors: Addisu Z. Taddese, Carlos Agüero, Chris Lalancette, Michael Carroll


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `image_tools <https://github.com/ros2/demos/tree/kilted/image_tools/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Lint image_tools/CMakeLists.txt ([#712 ](https://github.com/ros2/demos/issues/712)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* Contributors: Alejandro Hernández Cordero, mosfet80, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `image_transport <https://github.com/ros-perception/image_common/tree/kilted/image_transport/CHANGELOG.rst>`__

* Remove windows warnings ([#350 ](https://github.com/ros-perception/image_common/issues/350)_)
* Add [`rclcpp::shutdown`` (`#347 ](https://github.com/ros-perception/image_common/issues/347)_)
* Use target_link_libraries instead of ament_target_dependencies ([#345 ](https://github.com/ros-perception/image_common/issues/345)_)
* feat: python bindings for image_transport and publish ([#323 ](https://github.com/ros-perception/image_common/issues/323)_) Co-authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>
* Apply remappings to base topic before creating transport-specific topics ([#326 ](https://github.com/ros-perception/image_common/issues/326)_)
* Add lazy subscription to republisher ([#325 ](https://github.com/ros-perception/image_common/issues/325)_)
* Fix node name ([#321 ](https://github.com/ros-perception/image_common/issues/321)_)
* Updated deprecated message filter headers ([#320 ](https://github.com/ros-perception/image_common/issues/320)_)
* Removed outdated comment ([#319 ](https://github.com/ros-perception/image_common/issues/319)_)
* Preparing for qos deprecation ([#315 ](https://github.com/ros-perception/image_common/issues/315)_)
* Removed warning ([#312 ](https://github.com/ros-perception/image_common/issues/312)_)
* Support zero-copy intra-process publishing ([#306 ](https://github.com/ros-perception/image_common/issues/306)_)
* Add missing sub and pub options ([#308 ](https://github.com/ros-perception/image_common/issues/308)_) Co-authored-by: Angsa Deployment Team <team@angsa-robotics.com>
* Contributors: Alejandro Hernández Cordero, Błażej Sowa, Földi Tamás, Lucas Wendland, Michal Sojka, Shane Loretz, Tony Najjar, Yuyuan Yuan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `image_transport_py <https://github.com/ros-perception/image_common/tree/kilted/image_transport_py/CHANGELOG.rst>`__

* Add in python3-dev build dependency ([#334 ](https://github.com/ros-perception/image_common/issues/334)_)
* feat: python bindings for image_transport and publish ([#323 ](https://github.com/ros-perception/image_common/issues/323)_) Co-authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>
* Contributors: Chris Lalancette, Földi Tamás


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `interactive_markers <https://github.com/ros-visualization/interactive_markers/tree/kilted/CHANGELOG.rst>`__

* Deprecating tf2 C Headers ([#109 ](https://github.com/ros-visualization/interactive_markers/issues/109)_)
* Remove CODEOWNERS and mirror-rolling-to-main workflow ([#110 ](https://github.com/ros-visualization/interactive_markers/issues/110)_)
* Use non deprecated API ([#108 ](https://github.com/ros-visualization/interactive_markers/issues/108)_)
* Contributors: Alejandro Hernández Cordero, Lucas Wendland


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `intra_process_demo <https://github.com/ros2/demos/tree/kilted/intra_process_demo/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* Removed pre-compiler check for opencv3 ([#695 ](https://github.com/ros2/demos/issues/695)_)
* [intra_process_demo] executable name in README.md fix-up ([#690 ](https://github.com/ros2/demos/issues/690)_)
* Contributors: Alejandro Hernández Cordero, Trushant Adeshara, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `kdl_parser <https://github.com/ros/kdl_parser/tree/kilted/kdl_parser/CHANGELOG.rst>`__

* update urdf model header ([#85 ](https://github.com/ros/kdl_parser/issues/85)_)
* Contributors: Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `laser_geometry <https://github.com/ros-perception/laser_geometry/tree/kilted/CHANGELOG.rst>`__

* Deprecating tf2 C Headers ([#98 ](https://github.com/ros-perception/laser_geometry/issues/98)_)
* Remove CODEOWNERS and mirror-rolling-to-main workflow ([#100 ](https://github.com/ros-perception/laser_geometry/issues/100)_)
* Stop using python_cmake_module. ([#93 ](https://github.com/ros-perception/laser_geometry/issues/93)_)
* Added common linters ([#96 ](https://github.com/ros-perception/laser_geometry/issues/96)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Lucas Wendland


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch <https://github.com/ros2/launch/tree/kilted/launch/CHANGELOG.rst>`__

* Provide copy of launch configs to TimerAction's entities ([#836 ](https://github.com/ros2/launch/issues/836)_)
* Allow concatenating each path component of PathJoinSubstitution ([#838 ](https://github.com/ros2/launch/issues/838)_)
* Add StringJoinSubstitution substitution ([#843 ](https://github.com/ros2/launch/issues/843)_)
* Add missing test_depend for launch ([#850 ](https://github.com/ros2/launch/issues/850)_)
* Document substitutions concatenation in architecture doc ([#845 ](https://github.com/ros2/launch/issues/845)_)
* Update docs to use proper RST literals ([#837 ](https://github.com/ros2/launch/issues/837)_)
* Fix function params indentation ([#833 ](https://github.com/ros2/launch/issues/833)_)
* Add ForEach action to repeat entities using iteration-specific values ([#802 ](https://github.com/ros2/launch/issues/802)_)
* Create py.typed ([#828 ](https://github.com/ros2/launch/issues/828)_)
* Improve error reporting by adding file locations to exceptions ([#823 ](https://github.com/ros2/launch/issues/823)_)
* add test coverage for substitution edgecases involving E notation ([#824 ](https://github.com/ros2/launch/issues/824)_)
* Cleanup the launch dependencies. ([#819 ](https://github.com/ros2/launch/issues/819)_)
* Fix 'set up' typo ([#813 ](https://github.com/ros2/launch/issues/813)_)
* Add test_xmllint to all of the ament_python packages. ([#804 ](https://github.com/ros2/launch/issues/804)_)
* Fix typo in comment ([#783 ](https://github.com/ros2/launch/issues/783)_)
* Contributors: Chris Lalancette, Christian Ruf, Christophe Bedard, Michael Carlstrom, Roland Arsenault, danielcranston


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_pytest <https://github.com/ros2/launch/tree/kilted/launch_pytest/CHANGELOG.rst>`__

* Cleanup the launch dependencies. ([#819 ](https://github.com/ros2/launch/issues/819)_)
* Add test_xmllint to all of the ament_python packages. ([#804 ](https://github.com/ros2/launch/issues/804)_)
* Switch to using an rclpy context manager. ([#787 ](https://github.com/ros2/launch/issues/787)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_ros <https://github.com/ros2/launch_ros/tree/kilted/launch_ros/CHANGELOG.rst>`__

* Remove the slash stripping since leading slash matters ([#456 ](https://github.com/ros2/launch_ros/issues/456)_)
* Fixing lifecycle node autostart issue [#445 ](https://github.com/ros2/launch_ros/issues/445)_ ([#449 ](https://github.com/ros2/launch_ros/issues/449)_)
* Change docstring markdown code blocks to RST ([#450 ](https://github.com/ros2/launch_ros/issues/450)_)
* Autostarting lifecycle nodes and example launch file demo ([#430 ](https://github.com/ros2/launch_ros/issues/430)_)
* Add YAML dumper representator for str type to keep quotes always. ([#436 ](https://github.com/ros2/launch_ros/issues/436)_)
* Mock launch components causing rosdoc2 to fail Python API ([#425 ](https://github.com/ros2/launch_ros/issues/425)_)
* Add ament_xmllint to the ament_python packages. ([#423 ](https://github.com/ros2/launch_ros/issues/423)_)
* Fix url in setup.py ([#413 ](https://github.com/ros2/launch_ros/issues/413)_)
* Contributors: Chris Lalancette, Christophe Bedard, Olivia/F.F., R Kent James, Steve Macenski, Tomoya Fujita, Wei HU


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing <https://github.com/ros2/launch/tree/kilted/launch_testing/CHANGELOG.rst>`__

* Fix function params indentation ([#833 ](https://github.com/ros2/launch/issues/833)_)
* Cleanup the launch dependencies. ([#819 ](https://github.com/ros2/launch/issues/819)_)
* Add test_xmllint to all of the ament_python packages. ([#804 ](https://github.com/ros2/launch/issues/804)_)
* Add mechanism to disable workaround for dependency groups ([#775 ](https://github.com/ros2/launch/issues/775)_)
* Contributors: Chris Lalancette, Christophe Bedard, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing_ament_cmake <https://github.com/ros2/launch/tree/kilted/launch_testing_ament_cmake/CHANGELOG.rst>`__

* Add CMake parameter to override launch_testing module ([#854 ](https://github.com/ros2/launch/issues/854)_)
* Stop using python_cmake_module. ([#760 ](https://github.com/ros2/launch/issues/760)_)
* Don't write Python bytecode when invoking launch tests ([#785 ](https://github.com/ros2/launch/issues/785)_)
* Contributors: Chris Lalancette, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing_examples <https://github.com/ros2/examples/tree/kilted/launch_testing/launch_testing_examples/CHANGELOG.rst>`__

* Add test_xmllint.py. ([#401 ](https://github.com/ros2/examples/issues/401)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing_ros <https://github.com/ros2/launch_ros/tree/kilted/launch_testing_ros/CHANGELOG.rst>`__

* [`WaitForTopics``: let the user inject a trigger function to be executed after starting the subscribers (`#356 ](https://github.com/ros2/launch_ros/issues/356)_)
* Add EnableRmwIsolation action for starting rmw_test_fixture ([#459 ](https://github.com/ros2/launch_ros/issues/459)_)
* Fix function params indentation ([#446 ](https://github.com/ros2/launch_ros/issues/446)_)
* Add ament_xmllint to the ament_python packages. ([#423 ](https://github.com/ros2/launch_ros/issues/423)_)
* Switch to use rclpy.init context manager. ([#402 ](https://github.com/ros2/launch_ros/issues/402)_)
* Contributors: Chris Lalancette, Christophe Bedard, Giorgio Pintaudi, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_xml <https://github.com/ros2/launch/tree/kilted/launch_xml/CHANGELOG.rst>`__

* Add ForEach action to repeat entities using iteration-specific values ([#802 ](https://github.com/ros2/launch/issues/802)_)
* Stop loading extensions during launch\_{xml,yaml} tests. ([#820 ](https://github.com/ros2/launch/issues/820)_)
* Cleanup the launch dependencies. ([#819 ](https://github.com/ros2/launch/issues/819)_)
* Add test_xmllint to all of the ament_python packages. ([#804 ](https://github.com/ros2/launch/issues/804)_)
* Contributors: Chris Lalancette, Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_yaml <https://github.com/ros2/launch/tree/kilted/launch_yaml/CHANGELOG.rst>`__

* Add ForEach action to repeat entities using iteration-specific values ([#802 ](https://github.com/ros2/launch/issues/802)_)
* Stop loading extensions during launch\_{xml,yaml} tests. ([#820 ](https://github.com/ros2/launch/issues/820)_)
* Cleanup the launch dependencies. ([#819 ](https://github.com/ros2/launch/issues/819)_)
* Add test_xmllint to all of the ament_python packages. ([#804 ](https://github.com/ros2/launch/issues/804)_)
* Contributors: Chris Lalancette, Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `libcurl_vendor <https://github.com/ros/resource_retriever/tree/kilted/libcurl_vendor/CHANGELOG.rst>`__

* uniform  MinCMakeVersion ([#108 ](https://github.com/ros/resource_retriever/issues/108)_)
* Add "lib" to the Windows curl search path. ([#96 ](https://github.com/ros/resource_retriever/issues/96)_) In CMake 3.3, a commit made it so that the find_package module in CMake had a compatibility mode where it would automatically search for packages in a <prefix>/lib subdirectory. In CMake 3.6, this compatibility mode was reverted for all platforms *except* Windows. That means that since CMake 3.3, we haven't actually been using the path as specified in ``curl_DIR``, but we have instead been inadvertently relying on that fallback behavior. In CMake 3.28, that compatibilty mode was also removed for Windows, meaning that we are now failing to find_package(curl) in downstream packages (like resource_retriever). Fix this by adding in the "lib" directory that always should have been there.  I'll note that this *only* affects our Windows builds, because this code is in a if(WIN32) block.
* Contributors: Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `liblz4_vendor <https://github.com/ros2/rosbag2/tree/kilted/liblz4_vendor/CHANGELOG.rst>`__

* Add in a library prefix for lz4 from conda on Windows. ([#1846 ](https://github.com/ros2/rosbag2/issues/1846)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `libstatistics_collector <https://github.com/ros-tooling/libstatistics_collector/tree/kilted/CHANGELOG.rst>`__

* Bump codecov/codecov-action from 4.5.0 to 4.6.0
* Fix MovingAverageStatistics::max\_ Default Value ([#201 ](https://github.com/ros-tooling/libstatistics_collector/issues/201)_)
* Removed deprecated classes ([#200 ](https://github.com/ros-tooling/libstatistics_collector/issues/200)_)
* fix: add void annotation ([#194 ](https://github.com/ros-tooling/libstatistics_collector/issues/194)_)
* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, Jeffery Hsu, dependabot[bot]


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `libyaml_vendor <https://github.com/ros2/libyaml_vendor/tree/kilted/CHANGELOG.rst>`__

* Only set CRT_SECURE_NO_WARNINGS if it hasn't already been set. ([#64 ](https://github.com/ros2/libyaml_vendor/issues/64)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `lifecycle <https://github.com/ros2/demos/tree/kilted/lifecycle/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `lifecycle_py <https://github.com/ros2/demos/tree/kilted/lifecycle_py/CHANGELOG.rst>`__

* Add test_xmllint.py to all of the ament_python packages. ([#704 ](https://github.com/ros2/demos/issues/704)_)
* Change all of the demos to use the new rclpy context manager. ([#694 ](https://github.com/ros2/demos/issues/694)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `logging_demo <https://github.com/ros2/demos/tree/kilted/logging_demo/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Alejandro Hernández Cordero, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `lttngpy <https://github.com/ros2/ros2_tracing/tree/kilted/lttngpy/CHANGELOG.rst>`__

* Remove SHARED from pybind11_add_module ([#154 ](https://github.com/ros2/ros2_tracing/issues/154)_)
* Add python3-dev build_depend to lttngpy. ([#146 ](https://github.com/ros2/ros2_tracing/issues/146)_)
* Don't try to build on BSD ([#142 ](https://github.com/ros2/ros2_tracing/issues/142)_)
* Allow enabling syscalls through [`ros2 trace`` or the Trace action (`#137 ](https://github.com/ros2/ros2_tracing/issues/137)_)
* Remove python_cmake_module use. ([#91 ](https://github.com/ros2/ros2_tracing/issues/91)_)
* Add missing dependency on pkg-config to lttngpy ([#130 ](https://github.com/ros2/ros2_tracing/issues/130)_)
* Contributors: Chris Lalancette, Christophe Bedard, Nathan Wiebe Neufeldt, Scott K Logan, Silvio Traversaro


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `mcap_vendor <https://github.com/ros2/rosbag2/tree/kilted/mcap_vendor/CHANGELOG.rst>`__

* Update mcap ([#1774 ](https://github.com/ros2/rosbag2/issues/1774)_) Update mcap cpp to last version
* Update mcap-releases-cpp- into CMakeLists.txt ([#1612 ](https://github.com/ros2/rosbag2/issues/1612)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `message_filters <https://github.com/ros2/message_filters/tree/kilted/CHANGELOG.rst>`__

* Removed windows warnings ([#171 ](https://github.com/ros2/message_filters/issues/171)_)
* More generic subscriber implementation using NodeInterfaces from rclcpp ([#113 ](https://github.com/ros2/message_filters/issues/113)_)
* Feature/time sequencer python ([#156 ](https://github.com/ros2/message_filters/issues/156)_)
* Add sync_arrival_time flag to ApproximateTimeSynchronizer ([#166 ](https://github.com/ros2/message_filters/issues/166)_)
* fix: add [`rclcpp::shutdown`` (`#167 ](https://github.com/ros2/message_filters/issues/167)_)
* fix typo: Cache.getLastestTime -> Cache.getLatestTime ([#165 ](https://github.com/ros2/message_filters//issues/165)_)
* Add temporal offset between topics between ApproximateTimeSynchronizer ([#154 ](https://github.com/ros2/message_filters/issues/154)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#158 ](https://github.com/ros2/message_filters/issues/158)_)
* Updated Python docs ([#150 ](https://github.com/ros2/message_filters/issues/150)_)
* Adds an input aligner filter ([#148 ](https://github.com/ros2/message_filters/issues/148)_)
* Stop using python_cmake_module. ([#114 ](https://github.com/ros2/message_filters/issues/114)_)
* Fix the wording in the deprecation messages. ([#144 ](https://github.com/ros2/message_filters/issues/144)_)
* Apply some simplifications and deduplications to ExactTime sync policy ([#142 ](https://github.com/ros2/message_filters/issues/142)_)
* Minor fixes for [#93 ](https://github.com/ros2/message_filters/issues/93)_ ([#143 ](https://github.com/ros2/message_filters/issues/143)_)
* Bugfix/segfault when getting surrounding interval of empty cache ([#116 ](https://github.com/ros2/message_filters/issues/116)_)
* Migrate to C++11 variadic templates ([#93 ](https://github.com/ros2/message_filters/issues/93)_)
* [LatestTimeSync] Fix crash when Synchronizeris started before the messges are available. ([#137 ](https://github.com/ros2/message_filters/issues/137)_)
* Fix cppcheck warning on Windwos ([#138 ](https://github.com/ros2/message_filters/issues/138)_)
* Adding ament_lint_common ([#120 ](https://github.com/ros2/message_filters/issues/120)_)
* Deprecating all C headers ([#135 ](https://github.com/ros2/message_filters/issues/135)_)
* Cleanups ([#134 ](https://github.com/ros2/message_filters/issues/134)_)
* fix link of index.rst in README.md ([#133 ](https://github.com/ros2/message_filters/issues/133)_)
* Revert "Adding explicit constructors ([#129 ](https://github.com/ros2/message_filters/issues/129)_)" ([#132 ](https://github.com/ros2/message_filters/issues/132)_)
* fix: fallback Time used incorrect clock ([#118 ](https://github.com/ros2/message_filters/issues/118)_)
* Adding explicit constructors ([#129 ](https://github.com/ros2/message_filters/issues/129)_)
* Deprecated qos_profile in Subscriber ([#127 ](https://github.com/ros2/message_filters/issues/127)_)
* Adding cpplint ([#125 ](https://github.com/ros2/message_filters/issues/125)_)
* Move Docs From Wiki ([#119 ](https://github.com/ros2/message_filters/issues/119)_)
* Adding lint_cmake ([#126 ](https://github.com/ros2/message_filters/issues/126)_)
* Adding Uncrustify Changes ([#124 ](https://github.com/ros2/message_filters/issues/124)_)
* Adding Copyright Linter ([#122 ](https://github.com/ros2/message_filters/issues/122)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christopher Wecht, Clément Chupin, Dominik, Dr. Denis, Iván López Broceño, Kalvik, Lucas Wendland, Matthias Holoch, Michal Staniaszek, Russ, Saif Sidhik, Sascha Arnold, Yuyuan Yuan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `mimick_vendor <https://github.com/ros2/mimick_vendor/tree/kilted/CHANGELOG.rst>`__

* Update hash to fix windows failures ([#39 ](https://github.com/ros2/mimick_vendor/issues/39)_)
* Update to the commit that includes DT_GNU_HASH. ([#37 ](https://github.com/ros2/mimick_vendor/issues/37)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `nav_msgs <https://github.com/ros2/common_interfaces/tree/kilted/nav_msgs/CHANGELOG.rst>`__

* Move geometry_msgs/PoseStampedArray to nav_msgs/Goals ([#269 ](https://github.com/ros2/common_interfaces/issues/269)_)
* Contributors: Tully Foote


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `orocos_kdl_vendor <https://github.com/ros2/orocos_kdl_vendor/tree/kilted/orocos_kdl_vendor/CHANGELOG.rst>`__

* Use the same cmake version ([#36 ](https://github.com/ros2/orocos_kdl_vendor/issues/36)_)
* Resolve compatibility issue with newer cmake ([#35 ](https://github.com/ros2/orocos_kdl_vendor/issues/35)_)
* fix: add cxx_standard to avoid c++ check error ([#30 ](https://github.com/ros2/orocos_kdl_vendor/issues/30)_)
* Ensure that orocos_kdl_vendor doesn't accidentally find itself. ([#27 ](https://github.com/ros2/orocos_kdl_vendor/issues/27)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Homalozoa X, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `osrf_pycommon <https://github.com/osrf/osrf_pycommon/tree/master/CHANGELOG.rst>`__

* Merge pull request [#103 ](https://github.com/osrf/osrf_pycommon/issues/103)_ from christophebedard/christophebedard/fix-typo-on-each-verb
* Align stdeb dependencies with setup.py ([#101 ](https://github.com/osrf/osrf_pycommon/issues/101)_) Follow-up to 4b2f3a8e4969f33dced1dc2db2296230e7a55b1d
* Add '+upstream' suffix to published deb version ([#102 ](https://github.com/osrf/osrf_pycommon/issues/102)_) Using a debian version suffix which falls late alphabetically appears to give our packages preference by apt. If a user enables a repository which distributes packages created by OSRF or ROS, it is likely that they wish to use these packages instead of the ones packaged by their platform.
* Upload coverage results to codecov ([#100 ](https://github.com/osrf/osrf_pycommon/issues/100)_)
* Update ci.yaml ([#96 ](https://github.com/osrf/osrf_pycommon/issues/96)_) fix node.js <20 deprecation Co-authored-by: Scott K Logan <logans@cottsay.net>
* Updated python version ([#97 ](https://github.com/osrf/osrf_pycommon/issues/97)_) Python version 3.7 is no longer supported as of June 27, 2023 Co-authored-by: Scott K Logan <logans@cottsay.net>
* Resolve outstanding resource warnings when running tests ([#99 ](https://github.com/osrf/osrf_pycommon/issues/99)_)
* Update deb platforms for release ([#95 ](https://github.com/osrf/osrf_pycommon/issues/95)_) Added: * Ubuntu Noble (24.04 LTS pre-release) * Debian Trixie (testing) Dropped: * Debian Bullseye (oldstable) Retained: * Debian Bookworm (stable) * Ubuntu Focal (20.04 LTS) * Ubuntu Jammy (22.04 LTS)
* Remove CODEOWNERS. ([#98 ](https://github.com/osrf/osrf_pycommon/issues/98)_) It is out of date and no longer serving its intended purpose.
* Contributors: Chris Lalancette, Christophe Bedard, Scott K Logan, Steven! Ragnarök, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `osrf_testing_tools_cpp <https://github.com/osrf/osrf_testing_tools_cpp/tree/kilted/osrf_testing_tools_cpp/CHANGELOG.rst>`__

* Update CMakeLists.txt ([#85 ](https://github.com/osrf/osrf_testing_tools_cpp/issues/85)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `pendulum_control <https://github.com/ros2/demos/tree/kilted/pendulum_control/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Alejandro Hernández Cordero, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `pendulum_msgs <https://github.com/ros2/demos/tree/kilted/pendulum_msgs/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `performance_test_fixture <https://github.com/ros2/performance_test_fixture/tree/kilted/CHANGELOG.rst>`__

* Fix a warning when building on Ubuntu Noble. ([#26 ](https://github.com/ros2/performance_test_fixture/issues/26)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `pluginlib <https://github.com/ros/pluginlib/tree/kilted/CHANGELOG.rst>`__

* Heavily cleanup pluginlib. ([#265 ](https://github.com/ros/pluginlib/issues/265)_)
* Remove CODEOWNERS and mirror-rolling-to-main workflow ([#268 ](https://github.com/ros/pluginlib/issues/268)_)
* Fix Minor Spelling Mistakes ([#260 ](https://github.com/ros/pluginlib/issues/260)_)
* Removed deprecated method ([#256 ](https://github.com/ros/pluginlib/issues/256)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, David V. Lu!!


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `point_cloud_transport <https://github.com/ros-perception/point_cloud_transport/tree/kilted/point_cloud_transport/CHANGELOG.rst>`__

* Add [`rclcpp::shutdown`` (`#110 ](https://github.com/ros-perception/point_cloud_transport/issues/110)_)
* Updated deprecated message filter headers ([#94 ](https://github.com/ros-perception/point_cloud_transport/issues/94)_)
* Removed warning ([#89 ](https://github.com/ros-perception/point_cloud_transport/issues/89)_)
* republisher: qos override pub and sub ([#88 ](https://github.com/ros-perception/point_cloud_transport/issues/88)_)
* Stop using ament_target_dependencies. ([#86 ](https://github.com/ros-perception/point_cloud_transport/issues/86)_) We are slowly moving away from its use, so stop using it here.  While we are in here, notice some things that makes this easier: 1. pluginlib is absolutely a public dependency of this package. Because of that, we can just rely on the PUBLIC export of it, and we don't need to link it into every test.  But that also means we don't need some of the forward-declarations that were in loader_fwds.hpp, as we can just get those through the header file. 2. republish.hpp doesn't really need to exist at all.  That's because it is only a header file, but the implementation is in an executable.  Thus, no downstream could ever use it.  So just remove the file and put the declaration straight into the cpp file.
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Yuyuan Yuan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `point_cloud_transport_py <https://github.com/ros-perception/point_cloud_transport/tree/kilted/point_cloud_transport_py/CHANGELOG.rst>`__

* Add in dependency on python3-dev. ([#103 ](https://github.com/ros-perception/point_cloud_transport/issues/103)_)
* Remove use of python_cmake_module. ([#63 ](https://github.com/ros-perception/point_cloud_transport/issues/63)_)
* remove extra semicolon ([#98 ](https://github.com/ros-perception/point_cloud_transport/issues/98)_)
* Contributors: Chris Lalancette, Manu


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `python_orocos_kdl_vendor <https://github.com/ros2/orocos_kdl_vendor/tree/kilted/python_orocos_kdl_vendor/CHANGELOG.rst>`__

* fix: use fetchcontent_makeavailable to fix CMP0169 ([#32 ](https://github.com/ros2/orocos_kdl_vendor/issues/32)_)
* Remove the use of python_cmake_module ([#26 ](https://github.com/ros2/orocos_kdl_vendor/issues/26)_)
* Contributors: Chris Lalancette, Homalozoa X


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `python_qt_binding <https://github.com/ros-visualization/python_qt_binding/tree/kilted/CHANGELOG.rst>`__

* Skip running the tests on Windows Debug. ([#142 ](https://github.com/ros-visualization/python_qt_binding/issues/142)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `qt_dotgraph <https://github.com/ros-visualization/qt_gui_core/tree/kilted/qt_dotgraph/CHANGELOG.rst>`__

* Convert qt_dotgraph to a pure Python package. ([#300 ](https://github.com/ros-visualization/qt_gui_core/issues/300)_)
* Cleanup qt_dotgraph and make the tests more robust. ([#296 ](https://github.com/ros-visualization/qt_gui_core/issues/296)_)
* Skip running the tests on Windows Debug. ([#292 ](https://github.com/ros-visualization/qt_gui_core/issues/292)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `qt_gui_cpp <https://github.com/ros-visualization/qt_gui_core/tree/kilted/qt_gui_cpp/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#302 ](https://github.com/ros-visualization/qt_gui_core/issues/302)_)
* Add common linters and make them happy to qt_gui_cpp ([#295 ](https://github.com/ros-visualization/qt_gui_core/issues/295)_)
* Deprecated h headers ([#294 ](https://github.com/ros-visualization/qt_gui_core/issues/294)_)
* Contributors: Alejandro Hernández Cordero, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `quality_of_service_demo_cpp <https://github.com/ros2/demos/tree/kilted/quality_of_service_demo/rclcpp/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_) demo_nodes_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `quality_of_service_demo_py <https://github.com/ros2/demos/tree/kilted/quality_of_service_demo/rclpy/CHANGELOG.rst>`__

* Add test_xmllint.py to all of the ament_python packages. ([#704 ](https://github.com/ros2/demos/issues/704)_)
* Change all of the demos to use the new rclpy context manager. ([#694 ](https://github.com/ros2/demos/issues/694)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl <https://github.com/ros2/rcl/tree/kilted/rcl/CHANGELOG.rst>`__

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#1218 ](https://github.com/ros2/rcl/issues/1218)_)
* Fix typo in message header include in doc ([#1219 ](https://github.com/ros2/rcl/issues/1219)_)
* use rmw_event_type_is_supported ([#1214 ](https://github.com/ros2/rcl/issues/1214)_)
* No need to add public symbol visibility macros in implementation. ([#1213 ](https://github.com/ros2/rcl/issues/1213)_)
* Add new interfaces to enable intropsection for action ([#1207 ](https://github.com/ros2/rcl/issues/1207)_)
* Use FASTDDS_DEFAULT_PROFILES_FILE instead. ([#1211 ](https://github.com/ros2/rcl/issues/1211)_)
* Relieve timer test period not to miss the cycle. ([#1209 ](https://github.com/ros2/rcl/issues/1209)_)
* fix(rcl_action): Allow to pass the timer to action during initialization ([#1201 ](https://github.com/ros2/rcl/issues/1201)_) * fix(timer): Use impl pointer in jump callback The interface description does not explicitly state that a rcl_timer_t may not be copied around. Therefore users may do this. By using a known never changing pointer in the callbacks, we avoid segfaults, even if the 'user' decides to copy the rcl_timer_t around.
* move qos_profile_rosout_default to rmw. ([#1195 ](https://github.com/ros2/rcl/issues/1195)_)
* Update example usage for rcl_wait_set_init to pass correct number of args ([#1204 ](https://github.com/ros2/rcl/issues/1204)_)
* Clean up error handling in many rcl{_action,_lifecycle} codepaths ([#1202 ](https://github.com/ros2/rcl/issues/1202)_) * Shorten the delay in test_action_server setup. Instead of waiting 250ms between setting up 10 goals (for at least 2.5 seconds), just wait 100ms which reduces this to 1 second. * Small style cleanups in test_action_server.cpp * Reset the error in rcl_node_type_cache_register_type(). That is, if rcutils_hash_map_set() fails, it sets its own error, so overriding it with our own will cause a warning to print.  Make sure to clear it before setting our own. * Only unregister a clock jump callback if we have installed it. This avoids a warning on cleanup in rcl_timer_init2. * Record the return value from rcl_node_type_cache_register_type. Otherwise, in a failure situation we set the error but we actually return RCL_RET_OK to the upper layers, which is odd. * Get rid of completely unnecessary return value translation. This generated code was translating an RCL error to an RCL error, which doesn't make much sense.  Just remove the duplicate code. * Use the rcl_timer_init2 functionality to start the timer disabled. Rather than starting it enabled, and then immediately canceling it. * Don't overwrite the error from rcl_action_goal_handle_get_info() It already sets the error, so rcl_action_server_goal_exists() should not set it again. * Reset errors before setting new ones when checking action validity That way we avoid an ugly warning in the error paths. * Move the copying of the options earlier in rcl_subscription_init. That way when we go to cleanup in the "fail" case, the options actually exist and are valid.  This avoids an ugly warning during cleanup. * Make sure to set the error on failure of rcl_action_get\_##_service_name This makes it match the generated code for the action_client. * Reset the errors during RCUTILS_FAULT_INJECTION testing. That way subsequent failures won't print out ugly error strings. * Make sure to return errors in _rcl_parse_resource_match . That is, if rcl_lexer_lookahead2_expect() returns an error, we should pass that along to higher layers rather than just ignoring it. * Don't overwrite error by rcl_validate_enclave_name. It leads to ugly warnings. * Add acomment that rmw_validate_namespace_with_size sets the error * Make sure to reset error in rcl_node_type_cache_init. Otherwise we get a warning about overwriting the error from rcutils_hash_map_init. * Conditionally set error message in rcl_publisher_is_valid. Only when rcl_context_is_valid doesn't set the error. * Don't overwrite error from rcl_node_get_logger_name. It already sets the error in the failure case. * Make sure to reset errors when testing network flow endpoints. That's because some of the RMW implementations may not support this feature, and thus set errors. * Make sure to reset errors in rcl_expand_topic_name. That way we can set more useful errors for the upper layers. * Cleanup wait.c error handling. In particular, make sure to not overwrite errors as we get into error-handling paths, which should clean up warnings we get. * Make sure to reset errors in rcl_lifecycle tests. That way we won't get ugly "overwritten" warnings on subsequent tests. ---------
* Make the event skipping more generic. ([#1197 ](https://github.com/ros2/rcl/issues/1197)_)
* Heavy cleanup of test_events.cpp. ([#1196 ](https://github.com/ros2/rcl/issues/1196)_)
* Cleanup test_graph.cpp. ([#1193 ](https://github.com/ros2/rcl/issues/1193)_)
* Expect a minimum of two nodes to be alive in test_graph ([#1192 ](https://github.com/ros2/rcl/issues/1192)_)
* escalate RCL_RET_ACTION_xxx to 40XX. ([#1191 ](https://github.com/ros2/rcl/issues/1191)_)
* Fix NULL allocator and racy condition. ([#1188 ](https://github.com/ros2/rcl/issues/1188)_)
* Properly initialize the char array used in type hash calculations. ([#1182 ](https://github.com/ros2/rcl/issues/1182)_)
* Increased timeouts ([#1181 ](https://github.com/ros2/rcl/issues/1181)_)
* Skip some event tests on rmw_zenoh ([#1180 ](https://github.com/ros2/rcl/issues/1180)_)
* doc: rcl_logging_spdlog is the default impl. ([#1177 ](https://github.com/ros2/rcl/issues/1177)_)
* Update wait.h documentation for rcl_wait ([#1176 ](https://github.com/ros2/rcl/issues/1176)_)
* Change the starting time of the goal expiration timeout ([#1121 ](https://github.com/ros2/rcl/issues/1121)_)
* Removed deprecated localhost_only ([#1169 ](https://github.com/ros2/rcl/issues/1169)_)
* Fix typo in rcl_validate_enclave_name_with_size() doc ([#1168 ](https://github.com/ros2/rcl/issues/1168)_)
* Removed deprecated rcl_init_timer() ([#1167 ](https://github.com/ros2/rcl/issues/1167)_)
* Cleanup test_count_matched test to handle non-DDS RMWs ([#1164 ](https://github.com/ros2/rcl/issues/1164)_) * Make check_state a class method in test_count_matched. This allows us to pass fewer parameters into each each invocation, and allows us to hide some more of the implementation inside the class. * Rename "ops" to "opts" in test_count_matched. It just better reflects what these structures are. * Cleanup pub/subs with a scope_exit in test_count_matched. This just ensures that they are always cleaned up, even if we exit early.  Note that we specifically do *not* use it for test_count_matched_functions, since the cleanup is intentionally interleaved with other tests. * Check with the RMW layer to see whether QoS is compatible. Some RMWs may have different compatibility than DDS, so check with the RMW layer to see what we should expect for the number of publishers and subscriptions.
* Add mechanism to disable workaround for dependency groups ([#1151 ](https://github.com/ros2/rcl/issues/1151)_)
* remap_impl: minor typo ([#1158 ](https://github.com/ros2/rcl/issues/1158)_)
* Fix up rmw_cyclonedds timestamp testing. ([#1156 ](https://github.com/ros2/rcl/issues/1156)_)
* Add 'mimick' label to tests which use Mimick ([#1152 ](https://github.com/ros2/rcl/issues/1152)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Christophe Bedard, Felix Penzlin, G.A. vd. Hoorn, Janosch Machowinski, Scott K Logan, Tomoya Fujita, Yadu, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_action <https://github.com/ros2/rcl/tree/kilted/rcl_action/CHANGELOG.rst>`__

* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#1218 ](https://github.com/ros2/rcl/issues/1218)_)
* No need to add public symbol visibility macros in implementation. ([#1213 ](https://github.com/ros2/rcl/issues/1213)_)
* fix 'rcl_action_server_configure_action_introspection': inconsistent dll linkage. ([#1212 ](https://github.com/ros2/rcl/issues/1212)_)
* Add new interfaces to enable intropsection for action ([#1207 ](https://github.com/ros2/rcl/issues/1207)_)
* fix(rcl_action): Allow to pass the timer to action during initialization ([#1201 ](https://github.com/ros2/rcl/issues/1201)_) * fix(timer): Use impl pointer in jump callback The interface description does not explicitly state that a rcl_timer_t may not be copied around. Therefore users may do this. By using a known never changing pointer in the callbacks, we avoid segfaults, even if the 'user' decides to copy the rcl_timer_t around.
* Added remapping resolution for action names ([#1170 ](https://github.com/ros2/rcl/issues/1170)_) * Added remapping resolution for action names * Fix cpplint/uncrustify * Simplified returned error codes in case name resolution failes. * Renamed action_name field to remapped_action_name. * Removed unnecessary resolved_action_name stack variable * Added tests for action name remapping. * Add tests for action name remapping using local arguments ---------
* Clean up error handling in many rcl{_action,_lifecycle} codepaths ([#1202 ](https://github.com/ros2/rcl/issues/1202)_) * Shorten the delay in test_action_server setup. Instead of waiting 250ms between setting up 10 goals (for at least 2.5 seconds), just wait 100ms which reduces this to 1 second. * Small style cleanups in test_action_server.cpp * Reset the error in rcl_node_type_cache_register_type(). That is, if rcutils_hash_map_set() fails, it sets its own error, so overriding it with our own will cause a warning to print.  Make sure to clear it before setting our own. * Only unregister a clock jump callback if we have installed it. This avoids a warning on cleanup in rcl_timer_init2. * Record the return value from rcl_node_type_cache_register_type. Otherwise, in a failure situation we set the error but we actually return RCL_RET_OK to the upper layers, which is odd. * Get rid of completely unnecessary return value translation. This generated code was translating an RCL error to an RCL error, which doesn't make much sense.  Just remove the duplicate code. * Use the rcl_timer_init2 functionality to start the timer disabled. Rather than starting it enabled, and then immediately canceling it. * Don't overwrite the error from rcl_action_goal_handle_get_info() It already sets the error, so rcl_action_server_goal_exists() should not set it again. * Reset errors before setting new ones when checking action validity That way we avoid an ugly warning in the error paths. * Move the copying of the options earlier in rcl_subscription_init. That way when we go to cleanup in the "fail" case, the options actually exist and are valid.  This avoids an ugly warning during cleanup. * Make sure to set the error on failure of rcl_action_get\_##_service_name This makes it match the generated code for the action_client. * Reset the errors during RCUTILS_FAULT_INJECTION testing. That way subsequent failures won't print out ugly error strings. * Make sure to return errors in _rcl_parse_resource_match . That is, if rcl_lexer_lookahead2_expect() returns an error, we should pass that along to higher layers rather than just ignoring it. * Don't overwrite error by rcl_validate_enclave_name. It leads to ugly warnings. * Add acomment that rmw_validate_namespace_with_size sets the error * Make sure to reset error in rcl_node_type_cache_init. Otherwise we get a warning about overwriting the error from rcutils_hash_map_init. * Conditionally set error message in rcl_publisher_is_valid. Only when rcl_context_is_valid doesn't set the error. * Don't overwrite error from rcl_node_get_logger_name. It already sets the error in the failure case. * Make sure to reset errors when testing network flow endpoints. That's because some of the RMW implementations may not support this feature, and thus set errors. * Make sure to reset errors in rcl_expand_topic_name. That way we can set more useful errors for the upper layers. * Cleanup wait.c error handling. In particular, make sure to not overwrite errors as we get into error-handling paths, which should clean up warnings we get. * Make sure to reset errors in rcl_lifecycle tests. That way we won't get ugly "overwritten" warnings on subsequent tests. ---------
* Cleanup test_graph.cpp. ([#1193 ](https://github.com/ros2/rcl/issues/1193)_)
* Expect a minimum of two nodes to be alive in test_graph ([#1192 ](https://github.com/ros2/rcl/issues/1192)_)
* escalate RCL_RET_ACTION_xxx to 40XX. ([#1191 ](https://github.com/ros2/rcl/issues/1191)_)
* Fix NULL allocator and racy condition. ([#1188 ](https://github.com/ros2/rcl/issues/1188)_)
* Increased timeouts ([#1181 ](https://github.com/ros2/rcl/issues/1181)_)
* Change the starting time of the goal expiration timeout ([#1121 ](https://github.com/ros2/rcl/issues/1121)_)
* Increase the test_action_interaction timeouts. ([#1172 ](https://github.com/ros2/rcl/issues/1172)_) While I can't reproduce the problem locally, I suspect that waiting only 1 second for the entities to become ready isn't enough in all cases, particularly on Windows, with Connext, and when we are running in parallel with other tests. Thus, increase the timeout for the rcl_wait() in all of the test_action_interaction tests, which should hopefully be enough to make this always pass.
* Stop compiling rcl_action tests multiple times. ([#1165 ](https://github.com/ros2/rcl/issues/1165)_) We don't need to compile the tests once for each RMW; we can just compile it once and then use the RMW_IMPLEMENTATION environment variable to run the tests on the different RMWs. This speeds up compilation.
* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Janosch Machowinski, Justus Braun, Tomoya Fujita, Yadu, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_lifecycle <https://github.com/ros2/rcl/tree/kilted/rcl_lifecycle/CHANGELOG.rst>`__

* add rcl_print_transition_map. ([#1217 ](https://github.com/ros2/rcl/issues/1217)_)
* Enable test isolation in rcl_lifecycle ([#1216 ](https://github.com/ros2/rcl/issues/1216)_)
* Clean up error handling in many rcl{_action,_lifecycle} codepaths ([#1202 ](https://github.com/ros2/rcl/issues/1202)_) * Shorten the delay in test_action_server setup. Instead of waiting 250ms between setting up 10 goals (for at least 2.5 seconds), just wait 100ms which reduces this to 1 second. * Small style cleanups in test_action_server.cpp * Reset the error in rcl_node_type_cache_register_type(). That is, if rcutils_hash_map_set() fails, it sets its own error, so overriding it with our own will cause a warning to print.  Make sure to clear it before setting our own. * Only unregister a clock jump callback if we have installed it. This avoids a warning on cleanup in rcl_timer_init2. * Record the return value from rcl_node_type_cache_register_type. Otherwise, in a failure situation we set the error but we actually return RCL_RET_OK to the upper layers, which is odd. * Get rid of completely unnecessary return value translation. This generated code was translating an RCL error to an RCL error, which doesn't make much sense.  Just remove the duplicate code. * Use the rcl_timer_init2 functionality to start the timer disabled. Rather than starting it enabled, and then immediately canceling it. * Don't overwrite the error from rcl_action_goal_handle_get_info() It already sets the error, so rcl_action_server_goal_exists() should not set it again. * Reset errors before setting new ones when checking action validity That way we avoid an ugly warning in the error paths. * Move the copying of the options earlier in rcl_subscription_init. That way when we go to cleanup in the "fail" case, the options actually exist and are valid.  This avoids an ugly warning during cleanup. * Make sure to set the error on failure of rcl_action_get\_##_service_name This makes it match the generated code for the action_client. * Reset the errors during RCUTILS_FAULT_INJECTION testing. That way subsequent failures won't print out ugly error strings. * Make sure to return errors in _rcl_parse_resource_match . That is, if rcl_lexer_lookahead2_expect() returns an error, we should pass that along to higher layers rather than just ignoring it. * Don't overwrite error by rcl_validate_enclave_name. It leads to ugly warnings. * Add acomment that rmw_validate_namespace_with_size sets the error * Make sure to reset error in rcl_node_type_cache_init. Otherwise we get a warning about overwriting the error from rcutils_hash_map_init. * Conditionally set error message in rcl_publisher_is_valid. Only when rcl_context_is_valid doesn't set the error. * Don't overwrite error from rcl_node_get_logger_name. It already sets the error in the failure case. * Make sure to reset errors when testing network flow endpoints. That's because some of the RMW implementations may not support this feature, and thus set errors. * Make sure to reset errors in rcl_expand_topic_name. That way we can set more useful errors for the upper layers. * Cleanup wait.c error handling. In particular, make sure to not overwrite errors as we get into error-handling paths, which should clean up warnings we get. * Make sure to reset errors in rcl_lifecycle tests. That way we won't get ugly "overwritten" warnings on subsequent tests. ---------
* Fix NULL allocator and racy condition. ([#1188 ](https://github.com/ros2/rcl/issues/1188)_)
* Fix typo in rcl_lifecycle_com_interface_t doc ([#1174 ](https://github.com/ros2/rcl/issues/1174)_)
* Fix a memory leak in test_rcl_lifecycle. ([#1173 ](https://github.com/ros2/rcl/issues/1173)_) This one came about probably as a result of a bad merge. But essentially we were forcing the srv_change_state com_interface to be nullptr, but forgetting to save off the old pointer early enough.  Thus, we could never restore the old one before we went to "fini", and the memory would be leaked.  Fix this by remembering the impl pointer earlier.
* Contributors: Chris Lalancette, Christophe Bedard, Scott K Logan, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_logging_noop <https://github.com/ros2/rcl_logging/tree/kilted/rcl_logging_noop/CHANGELOG.rst>`__

* rcl_logging_interface is only valid path with build environment. ([#122 ](https://github.com/ros2/rcl_logging/issues/122)_)
* README update and some cleanups. ([#120 ](https://github.com/ros2/rcl_logging/issues/120)_)
* Contributors: Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_logging_spdlog <https://github.com/ros2/rcl_logging/tree/kilted/rcl_logging_spdlog/CHANGELOG.rst>`__

* rcl_logging_interface is only valid path with build environment. ([#122 ](https://github.com/ros2/rcl_logging/issues/122)_)
* README update and some cleanups. ([#120 ](https://github.com/ros2/rcl_logging/issues/120)_)
* Updated deprecated API ([#117 ](https://github.com/ros2/rcl_logging/issues/117)_)
* Contributors: Alejandro Hernández Cordero, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_yaml_param_parser <https://github.com/ros2/rcl/tree/kilted/rcl_yaml_param_parser/CHANGELOG.rst>`__

* Cleanup errors after error paths in rcl_yaml_param_parser tests. ([#1203 ](https://github.com/ros2/rcl/issues/1203)_) This gets rid of ugly "overwritten" warnings in the tests.
* Add 'mimick' label to tests which use Mimick ([#1152 ](https://github.com/ros2/rcl/issues/1152)_)
* Contributors: Chris Lalancette, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp <https://github.com/ros2/rclcpp/tree/kilted/rclcpp/CHANGELOG.rst>`__

* Fix a race condition ([#2819 ](https://github.com/ros2/rclcpp/issues/2819)_)
* Remove redundant typesupport check in serialization module ([#2808 ](https://github.com/ros2/rclcpp/issues/2808)_)
* Remove get_typesupport_handle implementation. ([#2806 ](https://github.com/ros2/rclcpp/issues/2806)_)
* Use NodeParameterInterface instead of /parameter_event to update "use_sim_time" ([#2378 ](https://github.com/ros2/rclcpp/issues/2378)_)
* Remove cancel_clock_executor_promise\_. ([#2797 ](https://github.com/ros2/rclcpp/issues/2797)_)
* Enable parameter update recursively only when QoS override parameters. ([#2742 ](https://github.com/ros2/rclcpp/issues/2742)_)
* Removed trailing whitespace from the codebase. ([#2791 ](https://github.com/ros2/rclcpp/issues/2791)_)
* Expanded docstring of [`get_rmw_qos_profile()`` (`#2787 ](https://github.com/ros2/rclcpp/issues/2787)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#2776 ](https://github.com/ros2/rclcpp/issues/2776)_)
* fix: Compilefix for clang ([#2775 ](https://github.com/ros2/rclcpp/issues/2775)_)
* add exception doc for configure_introspection. ([#2773 ](https://github.com/ros2/rclcpp/issues/2773)_)
* feat: Add ClockWaiter and ClockConditionalVariable ([#2691 ](https://github.com/ros2/rclcpp/issues/2691)_)
* doc: Added warning to not instantiate Clock directly with RCL_ROS_TIME ([#2768 ](https://github.com/ros2/rclcpp/issues/2768)_)
* Use rmw_event_type_is_supported in test_qos_event ([#2761 ](https://github.com/ros2/rclcpp/issues/2761)_)
* Support action typesupport helper ([#2750 ](https://github.com/ros2/rclcpp/issues/2750)_)
* use maybe_unused attribute for the portability. ([#2758 ](https://github.com/ros2/rclcpp/issues/2758)_)
* Executor strong reference fix ([#2745 ](https://github.com/ros2/rclcpp/issues/2745)_)
* Cleanup of https://github.com/ros2/rclcpp/pull/2683 ([#2714 ](https://github.com/ros2/rclcpp/issues/2714)_)
* Fix typo in doc section for get_service_typesupport_handle ([#2751 ](https://github.com/ros2/rclcpp/issues/2751)_)
* Test case and fix for for https://github.com/ros2/rclcpp/issues/2652 ([#2713 ](https://github.com/ros2/rclcpp/issues/2713)_)
* fix(timer): Delete node, after executor thread terminated ([#2737 ](https://github.com/ros2/rclcpp/issues/2737)_)
* update doc section for spin_xxx methods. ([#2730 ](https://github.com/ros2/rclcpp/issues/2730)_)
* fix: Expose timers used by rclcpp::Waitables ([#2699 ](https://github.com/ros2/rclcpp/issues/2699)_)
* use rmw_qos_profile_rosout_default instead of rcl. ([#2663 ](https://github.com/ros2/rclcpp/issues/2663)_)
* fix(Executor): Fixed entities not beeing executed after just beeing added ([#2724 ](https://github.com/ros2/rclcpp/issues/2724)_)
* fix: make the loop condition align with the description ([#2726 ](https://github.com/ros2/rclcpp/issues/2726)_)
* Collect log messages from rcl, and reset. ([#2720 ](https://github.com/ros2/rclcpp/issues/2720)_)
* Fix transient local IPC publish  ([#2708 ](https://github.com/ros2/rclcpp/issues/2708)_)
* apply actual QoS from rmw to the IPC publisher. ([#2707 ](https://github.com/ros2/rclcpp/issues/2707)_)
* Adding in topic name to logging on IPC issues ([#2706 ](https://github.com/ros2/rclcpp/issues/2706)_)
* fix TestTimeSource.ROS_time_valid_attach_detach. ([#2700 ](https://github.com/ros2/rclcpp/issues/2700)_)
* Update docstring for [`rclcpp::Node::now()`` (`#2696 ](https://github.com/ros2/rclcpp/issues/2696)_)
* Re-enable executor test on rmw_connextdds. ([#2693 ](https://github.com/ros2/rclcpp/issues/2693)_)
* Fix warnings on Windows. ([#2692 ](https://github.com/ros2/rclcpp/issues/2692)_)
* Omnibus fixes for running tests with Connext. ([#2684 ](https://github.com/ros2/rclcpp/issues/2684)_)
* fix(Executor): Fix segfault if callback group is deleted during rmw_wait ([#2683 ](https://github.com/ros2/rclcpp/issues/2683)_)
* accept custom allocator for LoanedMessage. ([#2672 ](https://github.com/ros2/rclcpp/issues/2672)_)
* a couple of typo fixes in doc section for LoanedMessage. ([#2676 ](https://github.com/ros2/rclcpp/issues/2676)_)
* Make sure callback_end tracepoint is triggered in AnyServiceCallback ([#2670 ](https://github.com/ros2/rclcpp/issues/2670)_)
* Correct the incorrect comments in generic_client.hpp ([#2662 ](https://github.com/ros2/rclcpp/issues/2662)_)
* Fix NodeOptions assignment operator ([#2656 ](https://github.com/ros2/rclcpp/issues/2656)_)
* set QoS History KEEP_ALL explicitly for statistics publisher. ([#2650 ](https://github.com/ros2/rclcpp/issues/2650)_)
* Fix test_intra_process_manager.cpp with rmw_zenoh_cpp ([#2653 ](https://github.com/ros2/rclcpp/issues/2653)_)
* Fixed test_events_executors in zenoh ([#2643 ](https://github.com/ros2/rclcpp/issues/2643)_)
* rmw_fastrtps supports service event gid uniqueness test. ([#2638 ](https://github.com/ros2/rclcpp/issues/2638)_)
* print warning if event callback is not supported instead of passing exception. ([#2648 ](https://github.com/ros2/rclcpp/issues/2648)_)
* Implement callback support of async_send_request for service generic client ([#2614 ](https://github.com/ros2/rclcpp/issues/2614)_)
* Fixed test qos rmw zenoh ([#2639 ](https://github.com/ros2/rclcpp/issues/2639)_)
* verify client gid uniqueness for a single service event. ([#2636 ](https://github.com/ros2/rclcpp/issues/2636)_)
* Skip some tests in test_qos_event and run others with event types supported by rmw_zenoh ([#2626 ](https://github.com/ros2/rclcpp/issues/2626)_)
* Shutdown the context before context's destructor is invoked in tests ([#2633 ](https://github.com/ros2/rclcpp/issues/2633)_)
* Skip rmw zenoh content filtering tests ([#2627 ](https://github.com/ros2/rclcpp/issues/2627)_)
* Use InvalidServiceTypeError for unavailable service type in GenericClient ([#2629 ](https://github.com/ros2/rclcpp/issues/2629)_)
* Implement generic service ([#2617 ](https://github.com/ros2/rclcpp/issues/2617)_)
* fix events-executor warm-up bug and add unit-tests ([#2591 ](https://github.com/ros2/rclcpp/issues/2591)_)
* remove unnecessary gtest-skip in test_executors ([#2600 ](https://github.com/ros2/rclcpp/issues/2600)_)
* Correct node name in service test code ([#2615 ](https://github.com/ros2/rclcpp/issues/2615)_)
* Minor naming fixes for ParameterValue to_string() function ([#2609 ](https://github.com/ros2/rclcpp/issues/2609)_)
* Removed clang warnings ([#2605 ](https://github.com/ros2/rclcpp/issues/2605)_)
* Fix a couple of issues in the documentation. ([#2608 ](https://github.com/ros2/rclcpp/issues/2608)_)
* deprecate the static single threaded executor ([#2598 ](https://github.com/ros2/rclcpp/issues/2598)_)
* Fix name of ParameterEventHandler class in doc ([#2604 ](https://github.com/ros2/rclcpp/issues/2604)_)
* subscriber_statistics_collectors\_ should be protected by mutex. ([#2592 ](https://github.com/ros2/rclcpp/issues/2592)_)
* Fix bug in timers lifecycle for events executor ([#2586 ](https://github.com/ros2/rclcpp/issues/2586)_)
* fix rclcpp/test/rclcpp/CMakeLists.txt to check for the correct targets existance ([#2596 ](https://github.com/ros2/rclcpp/issues/2596)_)
* Shut down context during init if logging config fails ([#2594 ](https://github.com/ros2/rclcpp/issues/2594)_)
* Make more of the Waitable API abstract ([#2593 ](https://github.com/ros2/rclcpp/issues/2593)_)
* Only compile the tests once. ([#2590 ](https://github.com/ros2/rclcpp/issues/2590)_)
* Updated rcpputils path API ([#2579 ](https://github.com/ros2/rclcpp/issues/2579)_)
* Make the subscriber_triggered_to_receive_message test more reliable. ([#2584 ](https://github.com/ros2/rclcpp/issues/2584)_) * Make the subscriber_triggered_to_receive_message test more reliable. In the current code, inside of the timer we create the subscription and the publisher, publish immediately, and expect the subscription to get it immediately.  But it may be the case that discovery hasn't even happened between the publisher and the subscription by the time the publish call happens. To make this more reliable, create the subscription and publish *before* we ever create and spin on the timer.  This at least gives 100 milliseconds for discovery to happen.  That may not be quite enough to make this reliable on all platforms, but in my local testing this helps a lot.  Prior to this change I can make this fail one out of 10 times, and after the change I've run 100 times with no failures.
* Have the EventsExecutor use more common code  ([#2570 ](https://github.com/ros2/rclcpp/issues/2570)_) * move notify waitable setup to its own function * move mutex lock to retrieve_entity utility * use entities_need_rebuild\_ atomic bool in events-executors * remove duplicated set_on_ready_callback for notify_waitable * use mutex from base class rather than a new recursive mutex * use current_collection\_ member in events-executor * delay adding notify waitable to collection * postpone clearing the current collection * commonize notify waitable and collection * commonize add/remove node/cbg methods * fix linter errors ---------
* Removed deprecated methods and classes ([#2575 ](https://github.com/ros2/rclcpp/issues/2575)_)
* Release ownership of entities after spinning cancelled ([#2556 ](https://github.com/ros2/rclcpp/issues/2556)_) * Release ownership of entities after spinning cancelled * Move release action to every exit point in different spin functions * Move wait_result\_.reset() before setting spinning to false * Update test code * Move test code to test_executors.cpp ---------
* Split test_executors.cpp even further. ([#2572 ](https://github.com/ros2/rclcpp/issues/2572)_) That's because it is too large for Windows Debug to compile, so split into smaller bits. Even with this split, the file is too big; that's likely because we are using TYPED_TEST here, which generates multiple symbols per test case.  To deal with this, without further breaking up the file, also add in the /bigobj flag when compiling on Windows Debug.
* avoid adding notify waitable twice to events-executor collection ([#2564 ](https://github.com/ros2/rclcpp/issues/2564)_) * avoid adding notify waitable twice to events-executor entities collection * remove redundant mutex lock ---------
* Remove unnecessary msg includes in tests ([#2566 ](https://github.com/ros2/rclcpp/issues/2566)_)
* Fix copy-paste errors in function docs ([#2565 ](https://github.com/ros2/rclcpp/issues/2565)_)
* Fix typo in function doc ([#2563 ](https://github.com/ros2/rclcpp/issues/2563)_)
* Add test creating two content filter topics with the same topic name ([#2546 ](https://github.com/ros2/rclcpp/issues/2546)_) ([#2549 ](https://github.com/ros2/rclcpp/issues/2549)_)
* add impl pointer for ExecutorOptions ([#2523 ](https://github.com/ros2/rclcpp/issues/2523)_)
* Fixup Executor::spin_all() regression fix ([#2517 ](https://github.com/ros2/rclcpp/issues/2517)_)
* Add 'mimick' label to tests which use Mimick ([#2516 ](https://github.com/ros2/rclcpp/issues/2516)_)
* Contributors: Abhishek Kashyap, Alberto Soragna, Alejandro Hernández Cordero, Alexis Pojomovsky, Barry Xu, Chris Lalancette, Christophe Bedard, Hsin-Yi, Janosch Machowinski, Jeffery Hsu, Kang, Leander Stephen D'Souza, Patrick Roncagliolo, Pedro de Azeredo, Romain DESILLE, Scott K Logan, Steve Macenski, Tanishq Chaudhary, Tomoya Fujita, William Woodall, Yuyuan Yuan, jmachowinski


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp_action <https://github.com/ros2/rclcpp/tree/kilted/rclcpp_action/CHANGELOG.rst>`__

* Use std::recursive_mutex for action requests. ([#2798 ](https://github.com/ros2/rclcpp/issues/2798)_)
* Remove warning ([#2790 ](https://github.com/ros2/rclcpp/issues/2790)_)
* Harden rclcpp_action::convert(). ([#2786 ](https://github.com/ros2/rclcpp/issues/2786)_)
* Add new interfaces to enable introspection for action ([#2743 ](https://github.com/ros2/rclcpp/issues/2743)_)
* use maybe_unused attribute for the portability. ([#2758 ](https://github.com/ros2/rclcpp/issues/2758)_)
* fix: Expose timers used by rclcpp::Waitables ([#2699 ](https://github.com/ros2/rclcpp/issues/2699)_)
* Collect log messages from rcl, and reset. ([#2720 ](https://github.com/ros2/rclcpp/issues/2720)_)
* Make ament_cmake a buildtool dependency ([#2689 ](https://github.com/ros2/rclcpp/issues/2689)_)
* Fix documentation typo in server_goal_handle.hpp ([#2669 ](https://github.com/ros2/rclcpp/issues/2669)_)
* Increase the timeout for the cppcheck on rclcpp_action. ([#2640 ](https://github.com/ros2/rclcpp/issues/2640)_)
* add smart pointer macros definitions to action server and client base classes ([#2631 ](https://github.com/ros2/rclcpp/issues/2631)_)
* Fix typo in function doc ([#2563 ](https://github.com/ros2/rclcpp/issues/2563)_)
* Add 'mimick' label to tests which use Mimick ([#2516 ](https://github.com/ros2/rclcpp/issues/2516)_)
* Contributors: Alberto Soragna, Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Christophe Bedard, Janosch Machowinski, Nathan Wiebe Neufeldt, Scott K Logan, Tomoya Fujita, YR


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp_components <https://github.com/ros2/rclcpp/tree/kilted/rclcpp_components/CHANGELOG.rst>`__

* Removed trailing whitespace from the codebase. ([#2791 ](https://github.com/ros2/rclcpp/issues/2791)_)
* add NO_UNDEFINED_SYMBOLS to rclcpp_components_register_node cmake macro ([#2746 ](https://github.com/ros2/rclcpp/issues/2746)_) ([#2764 ](https://github.com/ros2/rclcpp/issues/2764)_)
* use maybe_unused attribute for the portability. ([#2758 ](https://github.com/ros2/rclcpp/issues/2758)_)
* ComponentManager should just ignore unknown extra argument in the bas… ([#2723 ](https://github.com/ros2/rclcpp/issues/2723)_)
* Add parsing for rest of obvious boolean extra arguments and throw for unsupported ones ([#2685 ](https://github.com/ros2/rclcpp/issues/2685)_)
* Shutdown the context before context's destructor is invoked in tests ([#2633 ](https://github.com/ros2/rclcpp/issues/2633)_)
* Fix typo in rclcpp_components benchmark_components ([#2602 ](https://github.com/ros2/rclcpp/issues/2602)_)
* Updated rcpputils path API ([#2579 ](https://github.com/ros2/rclcpp/issues/2579)_)
* remove deprecated APIs from component_manager.hpp ([#2585 ](https://github.com/ros2/rclcpp/issues/2585)_)
* Contributors: Alberto Soragna, Alejandro Hernández Cordero, Christophe Bedard, Jonas Otto, Leander Stephen D'Souza, Tomoya Fujita, rcp1


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp_lifecycle <https://github.com/ros2/rclcpp/tree/kilted/rclcpp_lifecycle/CHANGELOG.rst>`__

* should pull valid transition before trying to change the state. ([#2774 ](https://github.com/ros2/rclcpp/issues/2774)_)
* use maybe_unused attribute for the portability. ([#2758 ](https://github.com/ros2/rclcpp/issues/2758)_)
* Collect log messages from rcl, and reset. ([#2720 ](https://github.com/ros2/rclcpp/issues/2720)_)
* Update docstring for [`rclcpp::Node::now()`` (`#2696 ](https://github.com/ros2/rclcpp/issues/2696)_)
* Fix error message in rclcpp_lifecycle::State::reset() ([#2647 ](https://github.com/ros2/rclcpp/issues/2647)_)
* Shutdown the context before context's destructor is invoked in tests ([#2633 ](https://github.com/ros2/rclcpp/issues/2633)_)
* LifecycleNode bugfix and add test cases ([#2562 ](https://github.com/ros2/rclcpp/issues/2562)_)
* Properly test get_service_names_and_types_by_node in rclcpp_lifecycle ([#2599 ](https://github.com/ros2/rclcpp/issues/2599)_)
* Removed deprecated methods and classes ([#2575 ](https://github.com/ros2/rclcpp/issues/2575)_)
* Fix the lifecycle tests on RHEL-9. ([#2583 ](https://github.com/ros2/rclcpp/issues/2583)_) * Fix the lifecycle tests on RHEL-9. The full explanation is in the comment, but basically since RHEL doesn't support mocking_utils::inject_on_return, we have to split out certain tests to make sure resources within a process don't collide. Co-authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>
* revert call shutdown in LifecycleNode destructor ([#2557 ](https://github.com/ros2/rclcpp/issues/2557)_)
* LifecycleNode shutdown on dtor only with valid context. ([#2545 ](https://github.com/ros2/rclcpp/issues/2545)_)
* call shutdown in LifecycleNode dtor to avoid leaving the device in unknown state (2nd) ([#2528 ](https://github.com/ros2/rclcpp/issues/2528)_)
* rclcpp::shutdown should not be called before LifecycleNode dtor. ([#2527 ](https://github.com/ros2/rclcpp/issues/2527)_)
* Revert "call shutdown in LifecycleNode dtor to avoid leaving the device in un… ([#2450 ](https://github.com/ros2/rclcpp/issues/2450)_)" ([#2522 ](https://github.com/ros2/rclcpp/issues/2522)_)
* Add 'mimick' label to tests which use Mimick ([#2516 ](https://github.com/ros2/rclcpp/issues/2516)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Patrick Roncagliolo, Scott K Logan, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclpy <https://github.com/ros2/rclpy/tree/kilted/rclpy/CHANGELOG.rst>`__

* Update parameter types ([#1441 ](https://github.com/ros2/rclpy/issues/1441)_)
* Add TypeError string arg for better clarity ([#1442 ](https://github.com/ros2/rclpy/issues/1442)_)
* Fix loading parameter behavior from yaml file. ([#1193 ](https://github.com/ros2/rclpy/issues/1193)_)
* Update [`lifecycle`` types (`#1440 ](https://github.com/ros2/rclpy/issues/1440)_)
* Update _rclpy_pybind11.pyi order and add EventsExecutor ([#1436 ](https://github.com/ros2/rclpy/issues/1436)_)
* Update Clock Types ([#1433 ](https://github.com/ros2/rclpy/issues/1433)_)
* Introduce EventsExecutor implementation ([#1391 ](https://github.com/ros2/rclpy/issues/1391)_)
* Fix Duration, Clock, and QoS Docs ([#1428 ](https://github.com/ros2/rclpy/issues/1428)_)
* Add exception doc for configure_introspection. ([#1434 ](https://github.com/ros2/rclpy/issues/1434)_)
* Fix Task constructor type bug ([#1431 ](https://github.com/ros2/rclpy/issues/1431)_)
* Add new interfaces to enable intropsection for action ([#1413 ](https://github.com/ros2/rclpy/issues/1413)_)
* Check parameter callback signature during registration. ([#1425 ](https://github.com/ros2/rclpy/issues/1425)_)
* Fix function params indentation ([#1426 ](https://github.com/ros2/rclpy/issues/1426)_)
* Update Service and Action Protocols ([#1409 ](https://github.com/ros2/rclpy/issues/1409)_)
* Remove [`SHARED`` from ``pybind11_add_module`` (`#1305 ](https://github.com/ros2/rclpy/issues/1305)_)
* Publish action goal status once accepted before execution. ([#1228 ](https://github.com/ros2/rclpy/issues/1228)_)
* Add missing dependencies so that rosdoc2 shows Node ([#1408 ](https://github.com/ros2/rclpy/issues/1408)_)
* add QoS Profile/Depth support to Node. ([#1376 ](https://github.com/ros2/rclpy/issues/1376)_)
* Various typing fixes ([#1402 ](https://github.com/ros2/rclpy/issues/1402)_)
* Add types to Action with rhel roscli fix ([#1361 ](https://github.com/ros2/rclpy/issues/1361)_)
* Check if Task(Future) is canceled. ([#1377 ](https://github.com/ros2/rclpy/issues/1377)_)
* Executors types ([#1370 ](https://github.com/ros2/rclpy/issues/1370)_)
* event_handler.py types ([#1340 ](https://github.com/ros2/rclpy/issues/1340)_)
* Add support for operator overloading of [`Duration`` (`#1387 ](https://github.com/ros2/rclpy/issues/1387)_)
* Service/Client Implementation types ([#1384 ](https://github.com/ros2/rclpy/issues/1384)_)
* avoid lifecycle node transition exception ([#1319 ](https://github.com/ros2/rclpy/issues/1319)_)
* Client:call generates TimeoutError exception when it is timed out. ([#1271 ](https://github.com/ros2/rclpy/issues/1271)_)
* Add in python3-dev build dependency. ([#1380 ](https://github.com/ros2/rclpy/issues/1380)_)
* Fix the race condition while calling rcl_shutdown ([#1353 ](https://github.com/ros2/rclpy/issues/1353)_)
* Use @deprecated to mark deprecated APIs for type checkers. ([#1350 ](https://github.com/ros2/rclpy/issues/1350)_)
* init ([#1358 ](https://github.com/ros2/rclpy/issues/1358)_)
* Avoid redundant done callbacks of the future while repeatedly calling spin_until_future_complete ([#1374 ](https://github.com/ros2/rclpy/issues/1374)_)
* Clean qos zenoh tests ([#1369 ](https://github.com/ros2/rclpy/issues/1369)_)
* adjust warn message that requested goal is already expired. ([#1363 ](https://github.com/ros2/rclpy/issues/1363)_)
* Adds types to Lifecycle Objects ([#1338 ](https://github.com/ros2/rclpy/issues/1338)_)
* Remove python_cmake_module use ([#1220 ](https://github.com/ros2/rclpy/issues/1220)_)
* TestClient.test_service_timestamps failing consistently. ([#1364 ](https://github.com/ros2/rclpy/issues/1364)_)
* Revert "Add types to Action Server and Action Client ([#1349 ](https://github.com/ros2/rclpy/issues/1349)_)" ([#1359 ](https://github.com/ros2/rclpy/issues/1359)_)
* Revert "Executors types ([#1345 ](https://github.com/ros2/rclpy/issues/1345)_)" ([#1360 ](https://github.com/ros2/rclpy/issues/1360)_)
* remove mock_compat ([#1357 ](https://github.com/ros2/rclpy/issues/1357)_)
* Executors types ([#1345 ](https://github.com/ros2/rclpy/issues/1345)_)
* Add types to Action Server and Action Client ([#1349 ](https://github.com/ros2/rclpy/issues/1349)_)
* Remove TODO for OpenSplice DDS issue. ([#1354 ](https://github.com/ros2/rclpy/issues/1354)_)
* Add types to parameter_client.py ([#1348 ](https://github.com/ros2/rclpy/issues/1348)_)
* Add types to Node.py ([#1346 ](https://github.com/ros2/rclpy/issues/1346)_)
* Add types to signals.py ([#1344 ](https://github.com/ros2/rclpy/issues/1344)_)
* Fixes spin_until_future_complete inside callback ([#1316 ](https://github.com/ros2/rclpy/issues/1316)_)
* add types ([#1339 ](https://github.com/ros2/rclpy/issues/1339)_)
* Add types to wait_for_message.py and moves Handles into type stubs ([#1325 ](https://github.com/ros2/rclpy/issues/1325)_)
* Add types to waitable.py ([#1328 ](https://github.com/ros2/rclpy/issues/1328)_)
* Replace rclpyHandle with type stubs ([#1326 ](https://github.com/ros2/rclpy/issues/1326)_)
* Fix time subtraction ([#1312 ](https://github.com/ros2/rclpy/issues/1312)_)
* Adds types to TypeDescriptionService. ([#1329 ](https://github.com/ros2/rclpy/issues/1329)_)
* Import DurationHandle not DurationType ([#1332 ](https://github.com/ros2/rclpy/issues/1332)_)
* Creates PublisherHandle and updates publisher.py ([#1310 ](https://github.com/ros2/rclpy/issues/1310)_)
* Subscription types ([#1281 ](https://github.com/ros2/rclpy/issues/1281)_)
* Add types to qos.py ([#1255 ](https://github.com/ros2/rclpy/issues/1255)_)
* minor improvements ([#1330 ](https://github.com/ros2/rclpy/issues/1330)_)
* Initialize signal handlers after context ([#1331 ](https://github.com/ros2/rclpy/issues/1331)_)
* shutdown ThreadPoolExecutor in MultiThreadedExecutor. ([#1309 ](https://github.com/ros2/rclpy/issues/1309)_)
* Generics Services and Clients ([#1275 ](https://github.com/ros2/rclpy/issues/1275)_)
* Add types to ParameterService ([#1262 ](https://github.com/ros2/rclpy/issues/1262)_)
* Add types to timer.py ([#1260 ](https://github.com/ros2/rclpy/issues/1260)_)
* Add types to rcutils_logger.py ([#1249 ](https://github.com/ros2/rclpy/issues/1249)_)
* Add types to topic_endpoint_info.oy ([#1253 ](https://github.com/ros2/rclpy/issues/1253)_)
* Add types to parameter.py. ([#1246 ](https://github.com/ros2/rclpy/issues/1246)_)
* Guard condition types. ([#1252 ](https://github.com/ros2/rclpy/issues/1252)_)
* Add types to callback_groups.py ([#1251 ](https://github.com/ros2/rclpy/issues/1251)_)
* Utilities.py types. ([#1250 ](https://github.com/ros2/rclpy/issues/1250)_)
* reduce result_timeout to 10 secs from 15 mins. ([#1171 ](https://github.com/ros2/rclpy/issues/1171)_)
* Add TimerInfo to timer callback. ([#1292 ](https://github.com/ros2/rclpy/issues/1292)_)
* Add types to task.py ([#1254 ](https://github.com/ros2/rclpy/issues/1254)_)
* Fix a bad bug in fetching the lifecycle transitions. ([#1321 ](https://github.com/ros2/rclpy/issues/1321)_)
* Fix a bug when using multiple rclpy.init context managers. ([#1314 ](https://github.com/ros2/rclpy/issues/1314)_)
* Executor executes the tasks in FIFO order. ([#1304 ](https://github.com/ros2/rclpy/issues/1304)_)
* Add top-level try_shutdown method. ([#1302 ](https://github.com/ros2/rclpy/issues/1302)_)
* Make rclpy initialization context-manager aware. ([#1298 ](https://github.com/ros2/rclpy/issues/1298)_)
* Docstring specifying proper destruction and creation of Rate, Timer and GuardCondition ([#1286 ](https://github.com/ros2/rclpy/issues/1286)_)
* Make timers context-aware. ([#1296 ](https://github.com/ros2/rclpy/issues/1296)_)
* Make service lients context-aware. ([#1295 ](https://github.com/ros2/rclpy/issues/1295)_)
* Make service servers context-manager aware. ([#1294 ](https://github.com/ros2/rclpy/issues/1294)_)
* Make nodes context-manager aware. ([#1293 ](https://github.com/ros2/rclpy/issues/1293)_)
* Make subscriptions context-manager aware. ([#1291 ](https://github.com/ros2/rclpy/issues/1291)_)
* Make publishers context-manager aware. ([#1289 ](https://github.com/ros2/rclpy/issues/1289)_)
* (NumberOfEntities) improve performance ([#1285 ](https://github.com/ros2/rclpy/issues/1285)_)
* Using Generics for messages ([#1239 ](https://github.com/ros2/rclpy/issues/1239)_)
* Contributors: Alejandro Hernández Cordero, Arjo Chakravarty, Barry Xu, Brad Martin, Chris Lalancette, Christophe Bedard, Elian NEPPEL, Jonathan, Matthijs van der Burgh, Michael Carlstrom, Nadav Elkabets, R Kent James, Shane Loretz, Tomoya Fujita, Wolf Vollprecht, Zahi Kakish


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcpputils <https://github.com/ros2/rcpputils/tree/kilted/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#211 ](https://github.com/ros2/rcpputils/issues/211)_)
* Added marco to disable deprecation warnings ([#210 ](https://github.com/ros2/rcpputils/issues/210)_)
* Added missing include ([#207 ](https://github.com/ros2/rcpputils/issues/207)_)
* Clear the rcutils error when throwing an exception. ([#206 ](https://github.com/ros2/rcpputils/issues/206)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#204 ](https://github.com/ros2/rcpputils/issues/204)_)
* fix memory leak for remove_all(). ([#201 ](https://github.com/ros2/rcpputils/issues/201)_)
* Suppress clang error because of deprecation ([#199 ](https://github.com/ros2/rcpputils/issues/199)_)
* Deprecated path class ([#196 ](https://github.com/ros2/rcpputils/issues/196)_)
* Replace create_temp_directory with the new create_temporary_directory ([#198 ](https://github.com/ros2/rcpputils/issues/198)_) * Replace create_temp_directory with the new create_temporary_directory - The newly added ``create_temporary_directory(..)`` uses std::filesystem::path and doesn't have platform-specific code. - Also deprecated ``create_temp_directory(..)`` and ``temp_directory_path``
* Removed deprecated header get_env.hpp ([#195 ](https://github.com/ros2/rcpputils/issues/195)_)
* Removed rolling mean accumulator deprecated header ([#194 ](https://github.com/ros2/rcpputils/issues/194)_)
* Removed deprecated clamp methods ([#193 ](https://github.com/ros2/rcpputils/issues/193)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Janosch Machowinski, Michael Carroll, Michael Orlov, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcutils <https://github.com/ros2/rcutils/tree/kilted/CHANGELOG.rst>`__

* Handle spaces in start_process arguments on Windows ([#494 ](https://github.com/ros2/rcutils/issues/494)_)
* Add utility functions for invoking a subprocess ([#491 ](https://github.com/ros2/rcutils/issues/491)_) ([#492 ](https://github.com/ros2/rcutils/issues/492)_)
* Add rcutils_join function for concatenating strings ([#490 ](https://github.com/ros2/rcutils/issues/490)_)
* Switch to ament_cmake_ros_core package ([#489 ](https://github.com/ros2/rcutils/issues/489)_)
* Cleanup error handling in rcutils. ([#485 ](https://github.com/ros2/rcutils/issues/485)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#483 ](https://github.com/ros2/rcutils/issues/483)_)
* Fix setting allocator to NULL. ([#478 ](https://github.com/ros2/rcutils/issues/478)_)
* Add new API to set envar while specifying overwrite ([#473 ](https://github.com/ros2/rcutils/issues/473)_)
* Remove completely unnecessary use of CLASSNAME. ([#471 ](https://github.com/ros2/rcutils/issues/471)_)
* load dll built by MINGW with lib prefix ([#470 ](https://github.com/ros2/rcutils/issues/470)_)
* add mingw support ([#468 ](https://github.com/ros2/rcutils/issues/468)_)
* Fix filesystem iteration on Windows ([#469 ](https://github.com/ros2/rcutils/issues/469)_)
* Add 'mimick' label to tests which use Mimick ([#466 ](https://github.com/ros2/rcutils/issues/466)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Felix F Xu, Michael Carroll, Scott K Logan, Yadu


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `resource_retriever <https://github.com/ros/resource_retriever/tree/kilted/resource_retriever/CHANGELOG.rst>`__

* Fixed clang compile error ([#112 ](https://github.com/ros/resource_retriever/issues/112)_)
* Removed windows warnings ([#111 ](https://github.com/ros/resource_retriever/issues/111)_)
* Add a plugin mechanism to resource_retriever ([#103 ](https://github.com/ros/resource_retriever/issues/103)_)
* uniform  MinCMakeVersion ([#108 ](https://github.com/ros/resource_retriever/issues/108)_)
* Stop using python_cmake_module. ([#94 ](https://github.com/ros/resource_retriever/issues/94)_)
* Allow spaces ([#100 ](https://github.com/ros/resource_retriever/issues/100)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michael Carroll, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw <https://github.com/ros2/rmw/tree/kilted/rmw/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#397 ](https://github.com/ros2/rmw/issues/397)_)
* Added rmw_event_type_is_supported ([#395 ](https://github.com/ros2/rmw/issues/395)_)
* add enclave option functions. ([#393 ](https://github.com/ros2/rmw/issues/393)_)
* a couple of typo fixes for doc section. ([#391 ](https://github.com/ros2/rmw/issues/391)_)
* update cmake version ([#389 ](https://github.com/ros2/rmw/issues/389)_)
* get_zero_initialized_xxx functions return zero initialized structure. ([#380 ](https://github.com/ros2/rmw/issues/380)_) * get_zero_initialized_xxx functions return zero initialized structure. * introduce RMW_EVENT_TYPE_MAX in rmw_event_type_t. * add a comment and more tests for rmw_event_type. ---------
* move qos_profile_rosout_default from rcl. ([#381 ](https://github.com/ros2/rmw/issues/381)_)
* Fix ugly overwritten warning messages on error paths. ([#387 ](https://github.com/ros2/rmw/issues/387)_) This mostly has to do with calling rmw_reset_error() in the proper time in the tests, but we also change one test for an allocator to properly check for a valid allocator.
* Fix rmw_validate_namespace{_with_size} error handling. ([#386 ](https://github.com/ros2/rmw/issues/386)_) * Fix rmw_validate_namespace{_with_size} error handling. It should always set an error, even on invalid arguments.
* Fix arg name in rmw_take_response() doc ([#384 ](https://github.com/ros2/rmw/issues/384)_)
* Initialize the NULL strucutre with static value. ([#378 ](https://github.com/ros2/rmw/issues/378)_)
* remove rmw_localhost_only_t. ([#376 ](https://github.com/ros2/rmw/issues/376)_)
* Fix typo with RMW_DURATION_UNSPECIFIED ([#375 ](https://github.com/ros2/rmw/issues/375)_)
* Fix typo in rmw_validate\_*_with_size() doc ([#374 ](https://github.com/ros2/rmw/issues/374)_)
* removed deprecated rmw_node_assert_liveliness() ([#373 ](https://github.com/ros2/rmw/issues/373)_)
* add mingw support ([#370 ](https://github.com/ros2/rmw/issues/370)_)
* Minor typo fix ([#368 ](https://github.com/ros2/rmw/issues/368)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Felix F Xu, G.A. vd. Hoorn, Michael Carroll, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_connextdds <https://github.com/ros2/rmw_connextdds/tree/kilted/rmw_connextdds/CHANGELOG.rst>`__

* Switch buildtool to ament_cmake package ([#183 ](https://github.com/ros2/rmw_connextdds/issues/183)_)
* Export a modern CMake target ([#179 ](https://github.com/ros2/rmw_connextdds/issues/179)_)
* Added rmw_event_type_is_supported ([#173 ](https://github.com/ros2/rmw_connextdds/issues/173)_)
* Contributors: Alejandro Hernández Cordero, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_connextdds_common <https://github.com/ros2/rmw_connextdds/tree/kilted/rmw_connextdds_common/CHANGELOG.rst>`__

* Address cpplit and gcc warnings. ([#184 ](https://github.com/ros2/rmw_connextdds/issues/184)_)
* Support topic instances ([#178 ](https://github.com/ros2/rmw_connextdds/issues/178)_)
* Switch buildtool to ament_cmake package ([#183 ](https://github.com/ros2/rmw_connextdds/issues/183)_)
* Discovery race condition mitigation ([#174 ](https://github.com/ros2/rmw_connextdds/issues/174)_)
* Added rmw_event_type_is_supported ([#173 ](https://github.com/ros2/rmw_connextdds/issues/173)_)
* use rmw_enclave_options_xxx APIs instead. ([#172 ](https://github.com/ros2/rmw_connextdds/issues/172)_)
* fix security certificate error message format. ([#171 ](https://github.com/ros2/rmw_connextdds/issues/171)_)
* Use rmw_security_common ([#167 ](https://github.com/ros2/rmw_connextdds/issues/167)_)
* Use target_link_libraries instead of ament_target_dependencies ([#169 ](https://github.com/ros2/rmw_connextdds/issues/169)_)
* introduce RMW_EVENT_TYPE_MAX in rmw_event_type_t. ([#162 ](https://github.com/ros2/rmw_connextdds/issues/162)_)
* Instrument client/service for end-to-end request/response tracking ([#163 ](https://github.com/ros2/rmw_connextdds/issues/163)_)
* fix: "Failed to parse type hash" message was overly spammy (ros2-50) ([#149 ](https://github.com/ros2/rmw_connextdds/issues/149)_)
* remove rmw_localhost_only_t. ([#156 ](https://github.com/ros2/rmw_connextdds/issues/156)_)
* Make rmw_service_server_is_available return RMW_RET_INVALID_ARGUMENT ([#150 ](https://github.com/ros2/rmw_connextdds/issues/150)_)
* Use rmw_namespace_validation_result_string() in rmw_create_node ([#151 ](https://github.com/ros2/rmw_connextdds/issues/151)_)
* Make rmw_destroy_wait_set return RMW_RET_INVALID_ARGUMENT ([#152 ](https://github.com/ros2/rmw_connextdds/issues/152)_)
* Contributors: Alejandro Hernández Cordero, Christophe Bedard, Francisco Gallego Salido, Scott K Logan, Shane Loretz, Taxo Rubio RTI, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_connextddsmicro <https://github.com/ros2/rmw_connextdds/tree/kilted/rmw_connextddsmicro/CHANGELOG.rst>`__

* Mark the package rmw_connextddsmicro as deprecated ([#182 ](https://github.com/ros2/rmw_connextdds/issues/182)_)
* Switch buildtool to ament_cmake package ([#183 ](https://github.com/ros2/rmw_connextdds/issues/183)_)
* Added rmw_event_type_is_supported ([#173 ](https://github.com/ros2/rmw_connextdds/issues/173)_)
* Contributors: Alejandro Hernández Cordero, Francisco Gallego Salido, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_cyclonedds_cpp <https://github.com/ros2/rmw_cyclonedds/tree/kilted/rmw_cyclonedds_cpp/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#538 ](https://github.com/ros2/rmw_cyclonedds/issues/538)_)
* Added rmw_event_type_is_supported ([#532 ](https://github.com/ros2/rmw_cyclonedds/issues/532)_)
* use rmw_enclave_options_xxx APIs instead. ([#531 ](https://github.com/ros2/rmw_cyclonedds/issues/531)_)
* use rmw_security_common ([#529 ](https://github.com/ros2/rmw_cyclonedds/issues/529)_)
* introduce RMW_EVENT_TYPE_MAX in rmw_event_type_t. ([#518 ](https://github.com/ros2/rmw_cyclonedds/issues/518)_)
* Reset the error before setting a new one. ([#526 ](https://github.com/ros2/rmw_cyclonedds/issues/526)_)
* Instrument client/service for end-to-end request/response tracking ([#521 ](https://github.com/ros2/rmw_cyclonedds/issues/521)_)
* Drop support for float128. ([#522 ](https://github.com/ros2/rmw_cyclonedds/issues/522)_)
* use RMW_GID_STORAGE_SIZE to client_service_id_t. ([#515 ](https://github.com/ros2/rmw_cyclonedds/issues/515)_)
* remove rmw_localhost_only_t. ([#508 ](https://github.com/ros2/rmw_cyclonedds/issues/508)_)
* Fix the triggering of guard conditions. ([#504 ](https://github.com/ros2/rmw_cyclonedds/issues/504)_) When a guard condition goes active, we have to remember to increase the trig_idx so we look at the next trigger. Otherwise, we can get into situations where we skip a triggered member.
* Make rmw_service_server_is_available return RMW_RET_INVALID_ARGUMENT ([#496 ](https://github.com/ros2/rmw_cyclonedds/issues/496)_)
* Use rmw_namespace_validation_result_string() in rmw_create_node ([#497 ](https://github.com/ros2/rmw_cyclonedds/issues/497)_)
* Make rmw_destroy_wait_set return RMW_RET_INVALID_ARGUMENT ([#498 ](https://github.com/ros2/rmw_cyclonedds/issues/498)_)
* Set received_timestamp to system_clock::now() in message_info ([#491 ](https://github.com/ros2/rmw_cyclonedds/issues/491)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Erik Boasson, Joe Speed, Jose Tomas Lorente, Michael Orlov, Scott K Logan, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_dds_common <https://github.com/ros2/rmw_dds_common/tree/kilted/rmw_dds_common/CHANGELOG.rst>`__

* Deprecated security methods ([#77 ](https://github.com/ros2/rmw_dds_common/issues/77)_)
* Contributors: Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_fastrtps_cpp <https://github.com/ros2/rmw_fastrtps/tree/kilted/rmw_fastrtps_cpp/CHANGELOG.rst>`__

* Address RHEL warnings and missing includes. ([#819 ](https://github.com/ros2/rmw_fastrtps/issues/819)_)
* Support topic instances ([#753 ](https://github.com/ros2/rmw_fastrtps/issues/753)_)
* Switch to ament_cmake_ros_core package ([#818 ](https://github.com/ros2/rmw_fastrtps/issues/818)_)
* Added rmw_event_type_is_supported ([#809 ](https://github.com/ros2/rmw_fastrtps/issues/809)_)
* use rmw_enclave_options_xxx APIs instead. ([#808 ](https://github.com/ros2/rmw_fastrtps/issues/808)_)
* Add deprecation warning for FASTRTPS_DEFAULT_PROFILES_FILE ([#806 ](https://github.com/ros2/rmw_fastrtps/issues/806)_)
* Export a modern CMake target ([#805 ](https://github.com/ros2/rmw_fastrtps/issues/805)_)
* Changes to build against Fast DDS 3.0 ([#776 ](https://github.com/ros2/rmw_fastrtps/issues/776)_)
* Fix some overwritten errors in rmw_fastrtps. ([#799 ](https://github.com/ros2/rmw_fastrtps/issues/799)_)
* Instrument client/service for end-to-end request/response tracking ([#787 ](https://github.com/ros2/rmw_fastrtps/issues/787)_)
* Contributors: Alejandro Hernández Cordero, Carlos Espinoza Curto, Chris Lalancette, Christophe Bedard, Miguel Company, Scott K Logan, Shane Loretz, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_fastrtps_dynamic_cpp <https://github.com/ros2/rmw_fastrtps/tree/kilted/rmw_fastrtps_dynamic_cpp/CHANGELOG.rst>`__

* Address RHEL warnings and missing includes. ([#819 ](https://github.com/ros2/rmw_fastrtps/issues/819)_)
* Support topic instances ([#753 ](https://github.com/ros2/rmw_fastrtps/issues/753)_)
* Switch to ament_cmake_ros_core package ([#818 ](https://github.com/ros2/rmw_fastrtps/issues/818)_)
* Make rmw_fastrtps_dynamic_cpp export a modern CMake target ([#814 ](https://github.com/ros2/rmw_fastrtps/issues/814)_)
* Added rmw_event_type_is_supported ([#809 ](https://github.com/ros2/rmw_fastrtps/issues/809)_)
* use rmw_enclave_options_xxx APIs instead. ([#808 ](https://github.com/ros2/rmw_fastrtps/issues/808)_)
* Add deprecation warning for FASTRTPS_DEFAULT_PROFILES_FILE ([#806 ](https://github.com/ros2/rmw_fastrtps/issues/806)_)
* Changes to build against Fast DDS 3.0 ([#776 ](https://github.com/ros2/rmw_fastrtps/issues/776)_)
* Fix some overwritten errors in rmw_fastrtps. ([#799 ](https://github.com/ros2/rmw_fastrtps/issues/799)_)
* Instrument client/service for end-to-end request/response tracking ([#787 ](https://github.com/ros2/rmw_fastrtps/issues/787)_)
* Add tracing instrumentation to rmw_fastrtps_dynamic_cpp ([#772 ](https://github.com/ros2/rmw_fastrtps/issues/772)_)
* Contributors: Alejandro Hernández Cordero, Carlos Espinoza Curto, Chris Lalancette, Christophe Bedard, Miguel Company, Scott K Logan, Shane Loretz, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_fastrtps_shared_cpp <https://github.com/ros2/rmw_fastrtps/tree/kilted/rmw_fastrtps_shared_cpp/CHANGELOG.rst>`__

* Address RHEL warnings and missing includes. ([#819 ](https://github.com/ros2/rmw_fastrtps/issues/819)_)
* Support topic instances ([#753 ](https://github.com/ros2/rmw_fastrtps/issues/753)_)
* Switch to ament_cmake_ros_core package ([#818 ](https://github.com/ros2/rmw_fastrtps/issues/818)_)
* Added rmw_event_type_is_supported ([#809 ](https://github.com/ros2/rmw_fastrtps/issues/809)_)
* use rmw_enclave_options_xxx APIs instead. ([#808 ](https://github.com/ros2/rmw_fastrtps/issues/808)_)
* Add deprecation warning for FASTRTPS_DEFAULT_PROFILES_FILE ([#806 ](https://github.com/ros2/rmw_fastrtps/issues/806)_)
* Use rmw_security_common ([#803 ](https://github.com/ros2/rmw_fastrtps/issues/803)_)
* introduce RMW_EVENT_TYPE_MAX in rmw_event_type_t. ([#785 ](https://github.com/ros2/rmw_fastrtps/issues/785)_)
* Changes to build against Fast DDS 3.0 ([#776 ](https://github.com/ros2/rmw_fastrtps/issues/776)_)
* Cleanup one test in rmw_fastrtps_shared_cpp. ([#794 ](https://github.com/ros2/rmw_fastrtps/issues/794)_)
* Instrument client/service for end-to-end request/response tracking ([#787 ](https://github.com/ros2/rmw_fastrtps/issues/787)_)
* Drop support for float128. ([#788 ](https://github.com/ros2/rmw_fastrtps/issues/788)_)
* Keep reference to [`DomainParticipantFactory`` (`#770 ](https://github.com/ros2/rmw_fastrtps/issues/770)_)
* Use client's reader guid for service introspection event gid ([#781 ](https://github.com/ros2/rmw_fastrtps/issues/781)_)
* Revert "Unique Client GID for Service Introspectino Event. ([#779 ](https://github.com/ros2/rmw_fastrtps/issues/779)_)" ([#780 ](https://github.com/ros2/rmw_fastrtps/issues/780)_)
* Unique Client GID for Service Introspectino Event. ([#779 ](https://github.com/ros2/rmw_fastrtps/issues/779)_)
* remove rmw_localhost_only_t. ([#773 ](https://github.com/ros2/rmw_fastrtps/issues/773)_)
* Make rmw_service_server_is_available return RMW_RET_INVALID_ARGUMENT ([#763 ](https://github.com/ros2/rmw_fastrtps/issues/763)_)
* Use rmw_namespace_validation_result_string() in rmw_create_node ([#765 ](https://github.com/ros2/rmw_fastrtps/issues/765)_)
* Make rmw_destroy_wait_set return RMW_RET_INVALID_ARGUMENT ([#766 ](https://github.com/ros2/rmw_fastrtps/issues/766)_)
* Use unique mangled names when creating Content Filter Topics ([#762 ](https://github.com/ros2/rmw_fastrtps/issues/762)_)
* Add support for data representation ([#756 ](https://github.com/ros2/rmw_fastrtps/issues/756)_)
* Contributors: Alejandro Hernández Cordero, Carlos Espinoza Curto, Chris Lalancette, Christophe Bedard, Jorge J. Perez, Mario Domínguez López, Miguel Company, Scott K Logan, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_implementation <https://github.com/ros2/rmw_implementation/tree/kilted/rmw_implementation/CHANGELOG.rst>`__

* Added rmw_event_type_is_supported ([#250 ](https://github.com/ros2/rmw_implementation/issues/250)_)
* Make sure to find_package(rmw) in rmw_implementation. ([#242 ](https://github.com/ros2/rmw_implementation/issues/242)_)
* Add mechanism to disable workaround for dependency groups ([#229 ](https://github.com/ros2/rmw_implementation/issues/229)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_implementation_cmake <https://github.com/ros2/rmw/tree/kilted/rmw_implementation_cmake/CHANGELOG.rst>`__

* update cmake version ([#389 ](https://github.com/ros2/rmw/issues/389)_)
* Contributors: Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_security_common <https://github.com/ros2/rmw/tree/kilted/rmw_security_common/CHANGELOG.rst>`__

* Export rmw dependency ([#400 ](https://github.com/ros2/rmw/issues/400)_)
* Added rmw_security_common ([#388 ](https://github.com/ros2/rmw/issues/388)_)
* Contributors: Alejandro Hernández Cordero, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_test_fixture <https://github.com/ros2/ament_cmake_ros/tree/kilted/rmw_test_fixture/CHANGELOG.rst>`__

* Resolve windows warnings in rmw_test_fixture ([#22 ](https://github.com/ros2/ament_cmake_ros/issues/22)_)
* Add rmw_test_fixture for supporting RMW-isolated testing ([#21 ](https://github.com/ros2/ament_cmake_ros/issues/21)_)
* Contributors: Alejandro Hernández Cordero, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_test_fixture_implementation <https://github.com/ros2/ament_cmake_ros/tree/kilted/rmw_test_fixture_implementation/CHANGELOG.rst>`__

* Don't set ROS_AUTOMATIC_DISCOVERY_RANGE in rmw_test_fixture ([#33 ](https://github.com/ros2/ament_cmake_ros/issues/33)_)
* Fix rmw_test_fixture DLL import on Windows ([#32 ](https://github.com/ros2/ament_cmake_ros/issues/32)_)
* Fix range for rmw_test_fixture_default port locking ([#31 ](https://github.com/ros2/ament_cmake_ros/issues/31)_)
* Stop loading RMW to load the test fixture ([#30 ](https://github.com/ros2/ament_cmake_ros/issues/30)_)
* Add 'default' rmw_test_fixture based on domain_coordinator ([#26 ](https://github.com/ros2/ament_cmake_ros/issues/26)_)
* Install run_rmw_isolated executable to lib subdirectory ([#25 ](https://github.com/ros2/ament_cmake_ros/issues/25)_)
* Ignore Ctrl-C in run_rmw_isolated on Windows ([#24 ](https://github.com/ros2/ament_cmake_ros/issues/24)_)
* Resolve windows warnings in rmw_test_fixture ([#22 ](https://github.com/ros2/ament_cmake_ros/issues/22)_)
* Add rmw_test_fixture for supporting RMW-isolated testing ([#21 ](https://github.com/ros2/ament_cmake_ros/issues/21)_)
* Contributors: Alejandro Hernández Cordero, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_zenoh_cpp <https://github.com/ros2/rmw_zenoh/tree/kilted/rmw_zenoh_cpp/CHANGELOG.rst>`__

* Change serialization format in attachment_helpers.cpp ([#601 ](https://github.com/ros2/rmw_zenoh/issues/601)_)
* Bump Zenoh to v1.3.2 and improve e2e reliability with HeartbeatSporadic ([#591 ](https://github.com/ros2/rmw_zenoh/issues/591)_)
* Implement rmw_test_fixture to start the Zenoh router ([#583 ](https://github.com/ros2/rmw_zenoh/issues/583)_)
* Add quality declaration ([#483 ](https://github.com/ros2/rmw_zenoh/issues/483)_)
* Trigger qos event callback if there are changes before registration  ([#587 ](https://github.com/ros2/rmw_zenoh/issues/587)_)
* Set wait_set->triggered flag to false ([#575 ](https://github.com/ros2/rmw_zenoh/issues/575)_)
* Add space after [`id`` token in ``rmw_zenohd`` log string (`#576 ](https://github.com/ros2/rmw_zenoh/issues/576)_)
* Use [`std::unique_lock`` to unlock correctly on Windows (`#570 ](https://github.com/ros2/rmw_zenoh/issues/570)_)
* Switch to std::map for TopicTypeMap ([#546 ](https://github.com/ros2/rmw_zenoh/issues/546)_)
* Support zenoh config override ([#551 ](https://github.com/ros2/rmw_zenoh/issues/551)_)
* Align the config with the latest Zenoh. ([#556 ](https://github.com/ros2/rmw_zenoh/issues/556)_)
* Added documentation note in the code ([#540 ](https://github.com/ros2/rmw_zenoh/issues/540)_)
* fix: unlock the mutex before making get ([#537 ](https://github.com/ros2/rmw_zenoh/issues/537)_)
* Take wait_set_lock before condition_variable notification for subscriptions ([#528 ](https://github.com/ros2/rmw_zenoh/issues/528)_)
* Switch default durability to volatile ([#521 ](https://github.com/ros2/rmw_zenoh/issues/521)_)
* Added rmw_event_type_is_supported ([#502 ](https://github.com/ros2/rmw_zenoh/issues/502)_)
* Fixed windows warning ([#500 ](https://github.com/ros2/rmw_zenoh/issues/500)_)
* Config: tune some values for ROS use case, especially with large number of Nodes (>200) ([#509 ](https://github.com/ros2/rmw_zenoh/issues/509)_)
* Honor ignore_local_publications in subscription options ([#508 ](https://github.com/ros2/rmw_zenoh/issues/508)_)
* Bump zenoh-cpp to 2a127bb, zenoh-c to 3540a3c, and zenoh to f735bf5 ([#503 ](https://github.com/ros2/rmw_zenoh/issues/503)_)
* Fix calculation of current_count_change when event status is updated ([#504 ](https://github.com/ros2/rmw_zenoh/issues/504)_)
* Fix checks for invalid arguments ([#497 ](https://github.com/ros2/rmw_zenoh/issues/497)_)
* Fail creation of entities if qos contains unknown settings ([#494 ](https://github.com/ros2/rmw_zenoh/issues/494)_)
* use rmw_enclave_options_xxx APIs instead. ([#491 ](https://github.com/ros2/rmw_zenoh/issues/491)_)
* Enable Zenoh UDP transport ([#486 ](https://github.com/ros2/rmw_zenoh/issues/486)_)
* fix: use the default destructor that automatically drops the zenoh reply/query and hence sends the final signal ([#473 ](https://github.com/ros2/rmw_zenoh/issues/473)_)
* Introduce the advanced publisher and subscriber ([#368 ](https://github.com/ros2/rmw_zenoh/issues/368)_)
* Switch to debug log if topic_name not in topic_map ([#454 ](https://github.com/ros2/rmw_zenoh/issues/454)_)
* Bump Zenoh to commit id 3bbf6af (1.2.1 + few commits) ([#456 ](https://github.com/ros2/rmw_zenoh/issues/456)_)
* Bump Zenoh to commit id e4ea6f0 (1.2.0 + few commits) ([#446 ](https://github.com/ros2/rmw_zenoh/issues/446)_)
* Inform users that peers will not discover and communicate with one another until the router is started ([#440 ](https://github.com/ros2/rmw_zenoh/issues/440)_)
* Clear the error after rmw_serialized_message_resize() ([#435 ](https://github.com/ros2/rmw_zenoh/issues/435)_)
* Fix [`ZENOH_ROUTER_CHECK_ATTEMPTS`` which was not respected (`#427 ](https://github.com/ros2/rmw_zenoh/issues/427)_)
* fix: use the default destructor to drop the member [`Payload`` (`#419 ](https://github.com/ros2/rmw_zenoh/issues/419)_)
* Remove [`gid_hash\_`` from ``AttachmentData`` (`#416 ](https://github.com/ros2/rmw_zenoh/issues/416)_)
* Sync the config with the default config in Zenoh. ([#396 ](https://github.com/ros2/rmw_zenoh/issues/396)_)
* fix: check the context validity before accessing the session ([#403 ](https://github.com/ros2/rmw_zenoh/issues/403)_)
* Fix wan't typo ([#400 ](https://github.com/ros2/rmw_zenoh/issues/400)_)
* An alternative middleware for ROS 2 based on Zenoh.
* Contributors: Alejandro Hernández Cordero, Alex Day, Bernd Pfrommer, ChenYing Kuo (CY), Chris Lalancette, Christophe Bedard, CihatAltiparmak, Esteve Fernandez, Franco Cipollone, Geoffrey Biggs, Hans-Martin, Hugal31, James Mount, Julien Enoch, Luca Cominardi, Mahmoud Mazouz, Morgan Quigley, Nate Koenig, Patrick Roncagliolo, Scott K Logan, Shivang Vijay, Tim Clephas, Tomoya Fujita, Yadunund, Yuyuan Yuan, methylDragon, yadunund, yellowhatter


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `robot_state_publisher <https://github.com/ros/robot_state_publisher/tree/kilted/CHANGELOG.rst>`__

* Use [`emplace()`` with ``std::map`` (`#231 ](https://github.com/ros/robot_state_publisher/issues/231)_)
* Remove CODEOWNERS and mirror-rolling-to-main workflow ([#229 ](https://github.com/ros/robot_state_publisher/issues/229)_)
* update urdf model header ([#223 ](https://github.com/ros/robot_state_publisher/issues/223)_)
* Contributors: Alejandro Hernández Cordero, Patrick Roncagliolo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2action <https://github.com/ros2/ros2cli/tree/kilted/ros2action/CHANGELOG.rst>`__

* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Support 'ros2 action echo' ([#978 ](https://github.com/ros2/ros2cli/issues/978)_)
* Correct the license content ([#979 ](https://github.com/ros2/ros2cli/issues/979)_)
* Maintaining consistency of automatically putting time stamps in the service and action calls similiar to publishing in rostopics. ([#961 ](https://github.com/ros2/ros2cli/issues/961)_)
* ros2action: add SIGINT handler to manage cancel request. ([#956 ](https://github.com/ros2/ros2cli/issues/956)_)
* node name print bug fix with ros2 action info. ([#926 ](https://github.com/ros2/ros2cli/issues/926)_)
* Switch to using rclpy.init context manager. ([#918 ](https://github.com/ros2/ros2cli/issues/918)_)
* support 'ros2 action find'. ([#917 ](https://github.com/ros2/ros2cli/issues/917)_)
* Contributors: Barry Xu, Chris Lalancette, Michael Carroll, Sukhvansh Jain, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2bag <https://github.com/ros2/rosbag2/tree/kilted/ros2bag/CHANGELOG.rst>`__

* Add actions replay feature ([#1955 ](https://github.com/ros2/rosbag2/issues/1955)_)
* Implement actions recording and displaying information about recorded actions features ([#1939 ](https://github.com/ros2/rosbag2/issues/1939)_)
* Fix for failing test_record_qos_profiles on Windows ([#1949 ](https://github.com/ros2/rosbag2/issues/1949)_)
* Progress bar for ros2 bag play ([#1836 ](https://github.com/ros2/rosbag2/issues/1836)_)
* Update CLI play verb metavar ([#1906 ](https://github.com/ros2/rosbag2/issues/1906)_)
* Add test_xmllint.py to python packages. ([#1879 ](https://github.com/ros2/rosbag2/issues/1879)_)
* Add support for replaying based on publication timestamp ([#1876 ](https://github.com/ros2/rosbag2/issues/1876)_)
* Publish clock after delay is over and disable delay on next loops ([#1861 ](https://github.com/ros2/rosbag2/issues/1861)_)
* Support replaying multiple bags ([#1848 ](https://github.com/ros2/rosbag2/issues/1848)_)
* Rename rclpy.qos.QoS*Policy to rclpy.qos.*Policy ([#1832 ](https://github.com/ros2/rosbag2/issues/1832)_)
* Add "--sort" CLI option to the "ros2 bag info" command ([#1804 ](https://github.com/ros2/rosbag2/issues/1804)_)
* Add cli option compression-threads-priority ([#1768 ](https://github.com/ros2/rosbag2/issues/1768)_)
* Add computation of size contribution to info verb ([#1726 ](https://github.com/ros2/rosbag2/issues/1726)_)
* fix(start-offset): allow specifying a start offset of 0 ([#1682 ](https://github.com/ros2/rosbag2/issues/1682)_)
* Exclude recorded /clock topic when --clock option is specified ([#1646 ](https://github.com/ros2/rosbag2/issues/1646)_)
* Sweep cleanup in rosbag2 recorder CLI args verification code ([#1633 ](https://github.com/ros2/rosbag2/issues/1633)_)
* Add --log-level to ros2 bag play and record ([#1625 ](https://github.com/ros2/rosbag2/issues/1625)_)
* Add optional  '--topics' CLI argument for 'ros2 bag record' ([#1632 ](https://github.com/ros2/rosbag2/issues/1632)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Christophe Bedard, Kosuke Takeuchi, Michael Orlov, Nicola Loi, Patrick Roncagliolo, Rein Appeldoorn, Roman, Sanoronas


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2cli <https://github.com/ros2/ros2cli/tree/kilted/ros2cli/CHANGELOG.rst>`__

* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Rename the test\_{daemon,direct}.py tests. ([#959 ](https://github.com/ros2/ros2cli/issues/959)_)
* replace removeprefix with string slicing. ([#953 ](https://github.com/ros2/ros2cli/issues/953)_)
* Fix instability in the ros2 daemon. ([#947 ](https://github.com/ros2/ros2cli/issues/947)_)
* Drop dependency on python3-pkg-resources ([#946 ](https://github.com/ros2/ros2cli/issues/946)_)
* NodeStrategy supports node name argument. ([#941 ](https://github.com/ros2/ros2cli/issues/941)_)
* Switch to using the rclpy.init context manager. ([#920 ](https://github.com/ros2/ros2cli/issues/920)_)
* Contributors: Chris Lalancette, Michael Carroll, Scott K Logan, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2doctor <https://github.com/ros2/ros2cli/tree/kilted/ros2doctor/CHANGELOG.rst>`__

* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Skip QoS compatibility test on Zenoh ([#985 ](https://github.com/ros2/ros2cli/issues/985)_)
* New flag and code update for its use ([#942 ](https://github.com/ros2/ros2cli/issues/942)_)
* Switch to using rclpy.init context manager. ([#918 ](https://github.com/ros2/ros2cli/issues/918)_)
* Revamp how we get network information in ros2doctor. ([#910 ](https://github.com/ros2/ros2cli/issues/910)_)
* Contributors: Alejandro Hernández Cordero, Angel LoGa, Chris Lalancette, Michael Carroll


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2launch <https://github.com/ros2/launch_ros/tree/kilted/ros2launch/CHANGELOG.rst>`__

* Add ament_xmllint to the ament_python packages. ([#423 ](https://github.com/ros2/launch_ros/issues/423)_)
* Fix url in setup.py ([#413 ](https://github.com/ros2/launch_ros/issues/413)_)
* Add mechanism to disable workaround for dependency groups ([#397 ](https://github.com/ros2/launch_ros/issues/397)_)
* Contributors: Chris Lalancette, Scott K Logan, Wei HU


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2lifecycle <https://github.com/ros2/ros2cli/tree/kilted/ros2lifecycle/CHANGELOG.rst>`__

* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Contributors: Michael Carroll


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2lifecycle_test_fixtures <https://github.com/ros2/ros2cli/tree/kilted/ros2lifecycle_test_fixtures/CHANGELOG.rst>`__

* Use target_link_libraries instead of ament_target_dependencies ([#973 ](https://github.com/ros2/ros2cli/issues/973)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2node <https://github.com/ros2/ros2cli/tree/kilted/ros2node/CHANGELOG.rst>`__

* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* ros2node requires fully qualified node name. ([#923 ](https://github.com/ros2/ros2cli/issues/923)_)
* Switch to using rclpy.init context manager. ([#918 ](https://github.com/ros2/ros2cli/issues/918)_)
* Contributors: Chris Lalancette, Michael Carroll, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2param <https://github.com/ros2/ros2cli/tree/kilted/ros2param/CHANGELOG.rst>`__

* Fix loading parameter behavior from yaml file ([#864 ](https://github.com/ros2/ros2cli/issues/864)_)
* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* cosmetic fixes for ros2param dump command. ([#933 ](https://github.com/ros2/ros2cli/issues/933)_)
* Switch to using rclpy.init context manager. ([#918 ](https://github.com/ros2/ros2cli/issues/918)_)
* Contributors: Chris Lalancette, Michael Carroll, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2pkg <https://github.com/ros2/ros2cli/tree/kilted/ros2pkg/CHANGELOG.rst>`__

* Use modern C++17 syntax. ([#982 ](https://github.com/ros2/ros2cli/issues/982)_)
* Use target_link_libraries instead of ament_target_dependencies ([#973 ](https://github.com/ros2/ros2cli/issues/973)_)
* Try to use the git global user.name for maintainer-name ([#968 ](https://github.com/ros2/ros2cli/issues/968)_)
* Update minimum CMake version CMakeLists.txt.em ([#969 ](https://github.com/ros2/ros2cli/issues/969)_)
* Add ament_xmllint test by default to ament_python packages. ([#957 ](https://github.com/ros2/ros2cli/issues/957)_)
* Drop dependency on python3-pkg-resources ([#946 ](https://github.com/ros2/ros2cli/issues/946)_)
* Support empy4 and empy3 ([#921 ](https://github.com/ros2/ros2cli/issues/921)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Larry Gezelius, Scott K Logan, Sebastian Castro, Shane Loretz, Shynur


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2run <https://github.com/ros2/ros2cli/tree/kilted/ros2run/CHANGELOG.rst>`__

* Add signal handler SIGIN/SIGTERM to ros2run ([#899 ](https://github.com/ros2/ros2cli/issues/899)_)
* Contributors: Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2service <https://github.com/ros2/ros2cli/tree/kilted/ros2service/CHANGELOG.rst>`__

* Use [`get_service`` in ``ros2service call`` (`#994 ](https://github.com/ros2/ros2cli/issues/994)_)
* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Support QoS options for [`ros2 service call`` (`#966 ](https://github.com/ros2/ros2cli/issues/966)_)
* Maintaining consistency of automatically putting time stamps in the service and action calls similiar to publishing in rostopics. ([#961 ](https://github.com/ros2/ros2cli/issues/961)_)
* Switch to using the rclpy.init context manager. ([#920 ](https://github.com/ros2/ros2cli/issues/920)_)
* Switch to using rclpy.init context manager. ([#918 ](https://github.com/ros2/ros2cli/issues/918)_)
* Contributors: Chris Lalancette, Michael Carlstrom, Michael Carroll, Sukhvansh Jain, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2test <https://github.com/ros2/ros_testing/tree/kilted/ros2test/CHANGELOG.rst>`__

* Add in test_xmllint to ros2test. ([#13 ](https://github.com/ros2/ros_testing/issues/13)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2topic <https://github.com/ros2/ros2cli/tree/kilted/ros2topic/CHANGELOG.rst>`__

* Custom Completion Finder for fetching topic prototype ([#995 ](https://github.com/ros2/ros2cli/issues/995)_)
* Documented now and auto keywords ([#1008 ](https://github.com/ros2/ros2cli/issues/1008)_)
* Conditional deserialization of message for [`ros2 topic hz`` (`#1005 ](https://github.com/ros2/ros2cli/issues/1005)_)
* Enable [`ros2 topic echo`` with entries of array fields (`#996 ](https://github.com/ros2/ros2cli/issues/996)_)
* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Adapt tests to Zenoh ([#988 ](https://github.com/ros2/ros2cli/issues/988)_)
* Adjust topic hz and bw command description ([#987 ](https://github.com/ros2/ros2cli/issues/987)_)
* Add support for topic QOS for ros2topic bw, delay and hz ([#935 ](https://github.com/ros2/ros2cli/issues/935)_)
* Start the simulation from 1 second for the test ([#975 ](https://github.com/ros2/ros2cli/issues/975)_)
* Support QoS options for [`ros2 service call`` (`#966 ](https://github.com/ros2/ros2cli/issues/966)_)
* Support ros2 topic pub yaml file input ([#925 ](https://github.com/ros2/ros2cli/issues/925)_)
* support multiple fields in ros2topic echo ([#964 ](https://github.com/ros2/ros2cli/issues/964)_)
* NodeStrategy supports node name argument. ([#941 ](https://github.com/ros2/ros2cli/issues/941)_)
* feat(echo --clear): add --clear option to echo ([#819 ](https://github.com/ros2/ros2cli/issues/819)_)
* Support multiple topics via ros2 topic hz. ([#929 ](https://github.com/ros2/ros2cli/issues/929)_)
* Remove TODO for OpenSplice DDS issue. ([#928 ](https://github.com/ros2/ros2cli/issues/928)_)
* Switch to using rclpy.init context manager. ([#918 ](https://github.com/ros2/ros2cli/issues/918)_)
* Contributors: Alejandro Hernández Cordero, Anthony Welte, Chris Lalancette, Fabian Thomsen, Florencia, Guillaume Beuzeboc, Kostubh Khandelwal, Leander Stephen D'Souza, Martin Pecka, Michael Carroll, SangtaekLee, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2trace <https://github.com/ros2/ros2_tracing/tree/kilted/ros2trace/CHANGELOG.rst>`__

* Expose types for tracing tools ([#153 ](https://github.com/ros2/ros2_tracing/issues/153)_)
* Contributors: Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros_environment <https://github.com/ros/ros_environment/tree/kilted/CHANGELOG.rst>`__

* Update ROS_DISTRO for Kilted Kaiju ([#41 ](https://github.com/ros/ros_environment/issues/41)_)
* Remove CODEOWNERS. ([#40 ](https://github.com/ros/ros_environment/issues/40)_)
* Contributors: Chris Lalancette, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2 <https://github.com/ros2/rosbag2/tree/kilted/rosbag2/CHANGELOG.rst>`__

* Support replaying multiple bags ([#1848 ](https://github.com/ros2/rosbag2/issues/1848)_)
* Contributors: Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_compression <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_compression/CHANGELOG.rst>`__

* Bugfix: Update metadata with new file_info before saving it first time ([#1843 ](https://github.com/ros2/rosbag2/issues/1843)_)
* Make snapshot writing into a new file each time it is triggered ([#1842 ](https://github.com/ros2/rosbag2/issues/1842)_)
* Add cli option compression-threads-priority ([#1768 ](https://github.com/ros2/rosbag2/issues/1768)_)
* Bugfix for bag_split event callbacks called to early with file compression ([#1643 ](https://github.com/ros2/rosbag2/issues/1643)_)
* Fix for regression in [`open_succeeds_twice`` and ``minimal_writer_example`` tests (`#1667 ](https://github.com/ros2/rosbag2/issues/1667)_)
* Bugfix for writer not being able to open again after closing ([#1599 ](https://github.com/ros2/rosbag2/issues/1599)_)
* Contributors: Alejandro Hernández Cordero, Michael Orlov, Roman, yschulz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_cpp <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_cpp/CHANGELOG.rst>`__

* Add support for finding action types message definitions in the [`LocalMessageDefinitionSource`` class to be able to store actions message definitions during recording. (`#1965 ](https://github.com/ros2/rosbag2/issues/1965)_)
* Add message sequence number to the messages write API ([#1961 ](https://github.com/ros2/rosbag2/issues/1961)_)
* Implement actions recording and displaying information about recorded actions features ([#1939 ](https://github.com/ros2/rosbag2/issues/1939)_)
* Set environment variables to run tests with [`rmw_zenoh_cpp`` with multicast discovery (`#1946 ](https://github.com/ros2/rosbag2/issues/1946)_)
* Add more logging info to storage and reader/writer open operations ([#1881 ](https://github.com/ros2/rosbag2/issues/1881)_)
* Add PlayerClock::wakeup() to interrupt sleeping ([#1869 ](https://github.com/ros2/rosbag2/issues/1869)_)
* Support replaying multiple bags ([#1848 ](https://github.com/ros2/rosbag2/issues/1848)_)
* Bugfix: Update metadata with new file_info before saving it first time ([#1843 ](https://github.com/ros2/rosbag2/issues/1843)_)
* Make snapshot writing into a new file each time it is triggered ([#1842 ](https://github.com/ros2/rosbag2/issues/1842)_)
* Bugfix for rosbag2_cpp serialization converter ([#1814 ](https://github.com/ros2/rosbag2/issues/1814)_)
* Allow unknown types in bag rewrite ([#1812 ](https://github.com/ros2/rosbag2/issues/1812)_)
* Add computation of size contribution to info verb ([#1726 ](https://github.com/ros2/rosbag2/issues/1726)_)
* [WIP] Remove rcpputils::fs dependencies in rosbag2 packages ([#1740 ](https://github.com/ros2/rosbag2/issues/1740)_)
* Removed deprecated write method ([#1738 ](https://github.com/ros2/rosbag2/issues/1738)_)
* Bugfix for bag_split event callbacks called to early with file compression ([#1643 ](https://github.com/ros2/rosbag2/issues/1643)_)
* Add topics with zero message counts to the SQLiteStorage::get_metadata(). ([#1725 ](https://github.com/ros2/rosbag2/issues/1725)_)
* Propagate "custom_data" and "ros_distro" in to the metadata.yaml file during re-indexing ([#1700 ](https://github.com/ros2/rosbag2/issues/1700)_)
* Bugfix for writer not being able to open again after closing ([#1599 ](https://github.com/ros2/rosbag2/issues/1599)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe Bedard, Cole Tucker, Michael Orlov, Nicola Loi, Tomoya Fujita, Yadunund, yschulz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_examples_cpp <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_examples/rosbag2_examples_cpp/CHANGELOG.rst>`__

* Add rosbag2_examples_cpp/simple_bag_reader.cpp. ([#1683 ](https://github.com/ros2/rosbag2/issues/1683)_)
* Contributors: Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_examples_py <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_examples/rosbag2_examples_py/CHANGELOG.rst>`__

* avoid using internal modules for examples. ([#1905 ](https://github.com/ros2/rosbag2/issues/1905)_)
* Add test_xmllint.py to python packages. ([#1879 ](https://github.com/ros2/rosbag2/issues/1879)_)
* simple_bag_reader.py should publish the data for each timer callback. ([#1767 ](https://github.com/ros2/rosbag2/issues/1767)_)
* Change the python examples to use the rclpy context manager. ([#1758 ](https://github.com/ros2/rosbag2/issues/1758)_)
* Add rosbag2_examples_cpp/simple_bag_reader.cpp. ([#1683 ](https://github.com/ros2/rosbag2/issues/1683)_)
* Contributors: Chris Lalancette, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_py <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_py/CHANGELOG.rst>`__

* Add message sequence number to the messages write API ([#1961 ](https://github.com/ros2/rosbag2/issues/1961)_)
* Add actions replay feature ([#1955 ](https://github.com/ros2/rosbag2/issues/1955)_)
* Implement actions recording and displaying information about recorded actions features ([#1939 ](https://github.com/ros2/rosbag2/issues/1939)_)
* Add bindings to close method in PyReader and PyCompressionReader ([#1935 ](https://github.com/ros2/rosbag2/issues/1935)_)
* Remove SHARED from pybind11_add_module ([#1929 ](https://github.com/ros2/rosbag2/issues/1929)_)
* Progress bar for ros2 bag play ([#1836 ](https://github.com/ros2/rosbag2/issues/1836)_)
* Upstream quality changes from Apex.AI part 1 ([#1903 ](https://github.com/ros2/rosbag2/issues/1903)_)
* Add support for replaying based on publication timestamp ([#1876 ](https://github.com/ros2/rosbag2/issues/1876)_)
* Support replaying multiple bags ([#1848 ](https://github.com/ros2/rosbag2/issues/1848)_)
* Add in python3-dev build dependency. ([#1863 ](https://github.com/ros2/rosbag2/issues/1863)_)
* Add "--sort" CLI option to the "ros2 bag info" command ([#1804 ](https://github.com/ros2/rosbag2/issues/1804)_)
* Remove use of python_cmake_module ([#1570 ](https://github.com/ros2/rosbag2/issues/1570)_)
* Added method to introspect QoS in Python ([#1648 ](https://github.com/ros2/rosbag2/issues/1648)_)
* Update CI scripts to use Ubuntu Noble distros and bump action scripts to latest versions ([#1709 ](https://github.com/ros2/rosbag2/issues/1709)_)
* Add cli option compression-threads-priority ([#1768 ](https://github.com/ros2/rosbag2/issues/1768)_)
* Add computation of size contribution to info verb ([#1726 ](https://github.com/ros2/rosbag2/issues/1726)_)
* Bugfix for wrong timestamps in ros2 bag info ([#1745 ](https://github.com/ros2/rosbag2/issues/1745)_)
* Add bindings for LocalMessageDefinitionSource ([#1697 ](https://github.com/ros2/rosbag2/issues/1697)_)
* Add --log-level to ros2 bag play and record ([#1625 ](https://github.com/ros2/rosbag2/issues/1625)_)
* Included to_rclcpp_qos_vector to Python wrappers ([#1642 ](https://github.com/ros2/rosbag2/issues/1642)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Christophe Bedard, Michael Orlov, Nicola Loi, Roman, Sanoronas, Silvio Traversaro, methylDragon, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_storage <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_storage/CHANGELOG.rst>`__

* Add message sequence number to the messages write API ([#1961 ](https://github.com/ros2/rosbag2/issues/1961)_)
* Add actions replay feature ([#1955 ](https://github.com/ros2/rosbag2/issues/1955)_)
* Add more logging info to storage and reader/writer open operations ([#1881 ](https://github.com/ros2/rosbag2/issues/1881)_)
* Contributors: Barry Xu, Michael Orlov


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_storage_mcap <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_storage_mcap/CHANGELOG.rst>`__

* Add message sequence number to the messages write API ([#1961 ](https://github.com/ros2/rosbag2/issues/1961)_)
* Add actions replay feature ([#1955 ](https://github.com/ros2/rosbag2/issues/1955)_)
* Upstream quality changes from Apex.AI part 1 ([#1903 ](https://github.com/ros2/rosbag2/issues/1903)_)
* Add vscode gitignore rule and remove vscode folder ([#1698 ](https://github.com/ros2/rosbag2/issues/1698)_)
* Contributors: Barry Xu, Michael Orlov, methylDragon


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_storage_sqlite3 <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_storage_sqlite3/CHANGELOG.rst>`__

* Add actions replay feature ([#1955 ](https://github.com/ros2/rosbag2/issues/1955)_)
* Fix incorrect zero size for sqlite storage ([#1759 ](https://github.com/ros2/rosbag2/issues/1759)_)
* Fix for failing throws_on_invalid_pragma_in_config_file on Windows ([#1742 ](https://github.com/ros2/rosbag2/issues/1742)_)
* Add topics with zero message counts to the SQLiteStorage::get_metadata(). ([#1725 ](https://github.com/ros2/rosbag2/issues/1725)_)
* Contributors: Barry Xu, Michael Orlov, Roman, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_test_common <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_test_common/CHANGELOG.rst>`__

* Add actions replay feature ([#1955 ](https://github.com/ros2/rosbag2/issues/1955)_)
* Implement actions recording and displaying information about recorded actions features ([#1939 ](https://github.com/ros2/rosbag2/issues/1939)_)
* Upstream quality changes from Apex.AI part 1 ([#1903 ](https://github.com/ros2/rosbag2/issues/1903)_)
* Use tmpfs in rosbag2 temporary_directory_fixture ([#1901 ](https://github.com/ros2/rosbag2/issues/1901)_)
* Add debug information for flaky can_record_again_after_stop test ([#1871 ](https://github.com/ros2/rosbag2/issues/1871)_)
* Remove use of python_cmake_module ([#1570 ](https://github.com/ros2/rosbag2/issues/1570)_)
* Improve the reliability of rosbag2 tests ([#1796 ](https://github.com/ros2/rosbag2/issues/1796)_)
* Small cleanups to the rosbag2 tests. ([#1792 ](https://github.com/ros2/rosbag2/issues/1792)_)
* [WIP] Remove rcpputils::fs dependencies in rosbag2 packages ([#1740 ](https://github.com/ros2/rosbag2/issues/1740)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Michael Orlov


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_test_msgdefs <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_test_msgdefs/CHANGELOG.rst>`__

* Add support for finding action types message definitions in the [`LocalMessageDefinitionSource`` class to be able to store actions message definitions during recording. (`#1965 ](https://github.com/ros2/rosbag2/issues/1965)_)
* Contributors: Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_tests <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_tests/CHANGELOG.rst>`__

* Implement actions recording and displaying information about recorded actions features ([#1939 ](https://github.com/ros2/rosbag2/issues/1939)_)
* Upstream quality changes from Apex.AI part 1 ([#1903 ](https://github.com/ros2/rosbag2/issues/1903)_)
* Increase timeout to 180s for test_rosbag2_record_end_to_end ([#1889 ](https://github.com/ros2/rosbag2/issues/1889)_)
* Add "--sort" CLI option to the "ros2 bag info" command ([#1804 ](https://github.com/ros2/rosbag2/issues/1804)_)
* Improve the reliability of rosbag2 tests ([#1796 ](https://github.com/ros2/rosbag2/issues/1796)_)
* Small cleanups to the rosbag2 tests. ([#1792 ](https://github.com/ros2/rosbag2/issues/1792)_)
* Add computation of size contribution to info verb ([#1726 ](https://github.com/ros2/rosbag2/issues/1726)_)
* Bugfix for wrong timestamps in ros2 bag info ([#1745 ](https://github.com/ros2/rosbag2/issues/1745)_)
* Fix for a false negative integration test with bag split in recorder ([#1743 ](https://github.com/ros2/rosbag2/issues/1743)_)
* Propagate "custom_data" and "ros_distro" in to the metadata.yaml file during re-indexing ([#1700 ](https://github.com/ros2/rosbag2/issues/1700)_)
* Sweep cleanup in rosbag2 recorder CLI args verification code ([#1633 ](https://github.com/ros2/rosbag2/issues/1633)_)
* Fix for regression in [`open_succeeds_twice`` and ``minimal_writer_example`` tests (`#1667 ](https://github.com/ros2/rosbag2/issues/1667)_)
* Add optional  '--topics' CLI argument for 'ros2 bag record' ([#1632 ](https://github.com/ros2/rosbag2/issues/1632)_)
* Bugfix for writer not being able to open again after closing ([#1599 ](https://github.com/ros2/rosbag2/issues/1599)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Cole Tucker, Michael Orlov, Nicola Loi, Sanoronas, yadunund, yschulz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_transport <https://github.com/ros2/rosbag2/tree/kilted/rosbag2_transport/CHANGELOG.rst>`__

* Add actions replay feature ([#1955 ](https://github.com/ros2/rosbag2/issues/1955)_)
* Implement actions recording and displaying information about recorded actions features ([#1939 ](https://github.com/ros2/rosbag2/issues/1939)_)
* Set environment variables to run tests with [`rmw_zenoh_cpp`` with multicast discovery (`#1946 ](https://github.com/ros2/rosbag2/issues/1946)_)
* Initialize filter with namespaced updated topics and services.  (rolling) ([#1944 ](https://github.com/ros2/rosbag2/issues/1944)_)
* Fix: QoS incompatibilities are not expected with rmw_zenoh_cpp ([#1936 ](https://github.com/ros2/rosbag2/issues/1936)_)
* Address windows warnings in the progress bar class ([#1927 ](https://github.com/ros2/rosbag2/issues/1927)_)
* Don't delete existing subscription if failed to create a new one ([#1923 ](https://github.com/ros2/rosbag2/issues/1923)_)
* Progress bar for ros2 bag play ([#1836 ](https://github.com/ros2/rosbag2/issues/1836)_)
* Upstream quality changes from Apex.AI part 1 ([#1903 ](https://github.com/ros2/rosbag2/issues/1903)_)
* Use tmpfs in rosbag2 temporary_directory_fixture ([#1901 ](https://github.com/ros2/rosbag2/issues/1901)_)
* Bugfix: Recorder discovery does not restart after being stopped ([#1894 ](https://github.com/ros2/rosbag2/issues/1894)_)
* Bugfix. Event publisher not starting for second run after stop ([#1888 ](https://github.com/ros2/rosbag2/issues/1888)_)
* Add support for replaying based on publication timestamp ([#1876 ](https://github.com/ros2/rosbag2/issues/1876)_)
* Publish clock after delay is over and disable delay on next loops ([#1861 ](https://github.com/ros2/rosbag2/issues/1861)_)
* Add PlayerClock::wakeup() to interrupt sleeping ([#1869 ](https://github.com/ros2/rosbag2/issues/1869)_)
* Add debug information for flaky can_record_again_after_stop test ([#1871 ](https://github.com/ros2/rosbag2/issues/1871)_)
* Support replaying multiple bags ([#1848 ](https://github.com/ros2/rosbag2/issues/1848)_)
* Reintroduce [`Don't warn for unknown types if topics are not selected`` (`#1825 ](https://github.com/ros2/rosbag2/issues/1825)_)
* Allow unknown types in bag rewrite ([#1812 ](https://github.com/ros2/rosbag2/issues/1812)_)
* Improve the reliability of rosbag2 tests ([#1796 ](https://github.com/ros2/rosbag2/issues/1796)_)
* Removed warnings ([#1794 ](https://github.com/ros2/rosbag2/issues/1794)_)
* Small cleanups to the rosbag2 tests. ([#1792 ](https://github.com/ros2/rosbag2/issues/1792)_)
* Add cli option compression-threads-priority ([#1768 ](https://github.com/ros2/rosbag2/issues/1768)_)
* [WIP] Remove rcpputils::fs dependencies in rosbag2 packages ([#1740 ](https://github.com/ros2/rosbag2/issues/1740)_)
* Bugfix for bag_split event callbacks called to early with file compression ([#1643 ](https://github.com/ros2/rosbag2/issues/1643)_)
* Bugfix for issue where unable to create composable nodes with compression ([#1679 ](https://github.com/ros2/rosbag2/issues/1679)_)
* Add support for "all" and "exclude" in RecordOptions YAML decoder ([#1664 ](https://github.com/ros2/rosbag2/issues/1664)_)
* Add unit tests to cover message's send and received timestamps during recording ([#1641 ](https://github.com/ros2/rosbag2/issues/1641)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Christophe Bedard, Michael Orlov, Nicola Loi, Ramon Wijnands, Roderick Taylor, Roman, Yuyuan Yuan, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_adapter <https://github.com/ros2/rosidl/tree/kilted/rosidl_adapter/CHANGELOG.rst>`__

* Types for rosidl_adapter ([#828 ](https://github.com/ros2/rosidl/issues/828)_)
* Support empy3 and empy4 ([#821 ](https://github.com/ros2/rosidl/issues/821)_)
* Contributors: Alejandro Hernández Cordero, Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_cli <https://github.com/ros2/rosidl/tree/kilted/rosidl_cli/CHANGELOG.rst>`__

* Rosidl cli types with [`specs_set`` fix (`#831 ](https://github.com/ros2/rosidl/issues/831)_)
* Contributors: Chris Lalancette, Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_core_generators <https://github.com/ros2/rosidl_core/tree/kilted/rosidl_core_generators/CHANGELOG.rst>`__

* Add mechanism to disable workaround for dependency groups ([#3 ](https://github.com/ros2/rosidl_core/issues/3)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_core_runtime <https://github.com/ros2/rosidl_core/tree/kilted/rosidl_core_runtime/CHANGELOG.rst>`__

* Add mechanism to disable workaround for dependency groups ([#3 ](https://github.com/ros2/rosidl_core/issues/3)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_default_runtime <https://github.com/ros2/rosidl_defaults/tree/kilted/rosidl_default_runtime/CHANGELOG.rst>`__

* Minor update to quality declaration ([#27 ](https://github.com/ros2/rosidl_defaults/issues/27)_)
* Contributors: Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_dynamic_typesupport <https://github.com/ros2/rosidl_dynamic_typesupport/tree/kilted/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#15 ](https://github.com/ros2/rosidl_dynamic_typesupport/issues/15)_)
* Bump minimum CMake version to 3.20 ([#14 ](https://github.com/ros2/rosidl_dynamic_typesupport/issues/14)_)
* Drop support for long double/float128. ([#12 ](https://github.com/ros2/rosidl_dynamic_typesupport/issues/12)_)
* Contributors: Chris Lalancette, Michael Carroll, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_dynamic_typesupport_fastrtps <https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/tree/kilted/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#8 ](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/8)_)
* Changes to build against Fast DDS 3.0 ([#5 ](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/5)_)
* Drop support for long double/float128. ([#6 ](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/6)_)
* Contributors: Chris Lalancette, Miguel Company, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_c <https://github.com/ros2/rosidl/tree/kilted/rosidl_generator_c/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#856 ](https://github.com/ros2/rosidl/issues/856)_)
* Deterministic iteration order for reproducible codegen ([#846 ](https://github.com/ros2/rosidl/issues/846)_)
* Add types [`rosidl_pycommon`` (`#824 ](https://github.com/ros2/rosidl/issues/824)_)
* Contributors: Harry Sarson, Michael Carlstrom, Michael Carroll


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_cpp <https://github.com/ros2/rosidl/tree/kilted/rosidl_generator_cpp/CHANGELOG.rst>`__

* Add name and data_type traits for actions ([#848 ](https://github.com/ros2/rosidl/issues/848)_)
* Add types [`rosidl_pycommon`` (`#824 ](https://github.com/ros2/rosidl/issues/824)_)
* Contributors: Michael Carlstrom, Nathan Wiebe Neufeldt


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_dds_idl <https://github.com/ros2/rosidl_dds/tree/kilted/rosidl_generator_dds_idl/CHANGELOG.rst>`__

* Update cmake version requirements ([#64 ](https://github.com/ros2/rosidl_dds/issues/64)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_py <https://github.com/ros2/rosidl_python/tree/kilted/rosidl_generator_py/CHANGELOG.rst>`__

* Fix [`__eq__`` for Array fields (`#224 ](https://github.com/ros2/rosidl_python/issues/224)_)
* Remove use of ament_target_dependencies ([#222 ](https://github.com/ros2/rosidl_python/issues/222)_)
* Revamp how we check for the correct class. ([#218 ](https://github.com/ros2/rosidl_python/issues/218)_)
* Remove python_cmake_module and set hints ([#204 ](https://github.com/ros2/rosidl_python/issues/204)_)
* Add rosidl_generator_py to the rosidl_runtime_packages group ([#212 ](https://github.com/ros2/rosidl_python/issues/212)_)
* Contributors: Chris Lalancette, Michael Carlstrom, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_tests <https://github.com/ros2/rosidl/tree/kilted/rosidl_generator_tests/CHANGELOG.rst>`__

* Add name and data_type traits for actions ([#848 ](https://github.com/ros2/rosidl/issues/848)_)
* Silence one more gcc false-positive. ([#814 ](https://github.com/ros2/rosidl/issues/814)_)
* Switch to using fastjsonschema for schema validation. ([#809 ](https://github.com/ros2/rosidl/issues/809)_)
* Contributors: Chris Lalancette, Nathan Wiebe Neufeldt


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_type_description <https://github.com/ros2/rosidl/tree/kilted/rosidl_generator_type_description/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#856 ](https://github.com/ros2/rosidl/issues/856)_)
* Contributors: Michael Carroll


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_parser <https://github.com/ros2/rosidl/tree/kilted/rosidl_parser/CHANGELOG.rst>`__

* Finish adding types to [`rosidl_parser`` (`#832 ](https://github.com/ros2/rosidl/issues/832)_)
* Add types to definition.py in [`rosidl_parser`` (`#791 ](https://github.com/ros2/rosidl/issues/791)_)
* Contributors: Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_pycommon <https://github.com/ros2/rosidl/tree/kilted/rosidl_pycommon/CHANGELOG.rst>`__

* Add test_xmllint to rosidl_pycommon. ([#833 ](https://github.com/ros2/rosidl/issues/833)_)
* Add types [`rosidl_pycommon`` (`#824 ](https://github.com/ros2/rosidl/issues/824)_)
* Support empy3 and empy4 ([#821 ](https://github.com/ros2/rosidl/issues/821)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_runtime_c <https://github.com/ros2/rosidl/tree/kilted/rosidl_runtime_c/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#856 ](https://github.com/ros2/rosidl/issues/856)_)
* Implement [`resize`` function for String (`#806 ](https://github.com/ros2/rosidl/issues/806)_)
* Fix u16 docs and improve docs formatting ([#805 ](https://github.com/ros2/rosidl/issues/805)_)
* Contributors: Christophe Bedard, Michael Carroll, WATANABE Aoi


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_runtime_cpp <https://github.com/ros2/rosidl/tree/kilted/rosidl_runtime_cpp/CHANGELOG.rst>`__

* Suppress warnings in the benchmarks for upstream GCC false positives. ([#810 ](https://github.com/ros2/rosidl/issues/810)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_runtime_py <https://github.com/ros2/rosidl_runtime_py/tree/kilted/CHANGELOG.rst>`__

* Use deepcopy in set_message_fields for safety. ([#34 ](https://github.com/ros2/rosidl_runtime_py/issues/34)_)
* Remove CODEOWNERS and mirror-rolling-to-master. ([#31 ](https://github.com/ros2/rosidl_runtime_py/issues/31)_)
* Contributors: Chris Lalancette, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_c <https://github.com/ros2/rosidl_typesupport/tree/kilted/rosidl_typesupport_c/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#166 ](https://github.com/ros2/rosidl_typesupport/issues/166)_)
* Uniform cmake requirement ([#163 ](https://github.com/ros2/rosidl_typesupport/issues/163)_)
* Cleanup warning message in rosidl_typesupport_c tests. ([#161 ](https://github.com/ros2/rosidl_typesupport/issues/161)_)
* Add mechanism to disable workaround for dependency groups ([#157 ](https://github.com/ros2/rosidl_typesupport/issues/157)_)
* Add 'mimick' label to tests which use Mimick ([#158 ](https://github.com/ros2/rosidl_typesupport/issues/158)_)
* Contributors: Chris Lalancette, Scott K Logan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_cpp <https://github.com/ros2/rosidl_typesupport/tree/kilted/rosidl_typesupport_cpp/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#166 ](https://github.com/ros2/rosidl_typesupport/issues/166)_)
* Uniform cmake requirement ([#163 ](https://github.com/ros2/rosidl_typesupport/issues/163)_)
* Add mechanism to disable workaround for dependency groups ([#157 ](https://github.com/ros2/rosidl_typesupport/issues/157)_)
* Contributors: Scott K Logan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_fastrtps_c <https://github.com/ros2/rosidl_typesupport_fastrtps/tree/kilted/rosidl_typesupport_fastrtps_c/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#127 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/127)_)
* Remove dependency on fastrtps_cmake_module ([#120 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/120)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow ([#124 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/124)_)
* Remove deprecated functions benchmark tests ([#122 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/122)_)
* Contributors: Chris Lalancette, Miguel Company, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_fastrtps_cpp <https://github.com/ros2/rosidl_typesupport_fastrtps/tree/kilted/rosidl_typesupport_fastrtps_cpp/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#127 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/127)_)
* Remove dependency on fastrtps_cmake_module ([#120 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/120)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow ([#124 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/124)_)
* Remove deprecated functions benchmark tests ([#122 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/122)_)
* Contributors: Chris Lalancette, Miguel Company, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_introspection_c <https://github.com/ros2/rosidl/tree/kilted/rosidl_typesupport_introspection_c/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#860 ](https://github.com/ros2/rosidl/issues/860)_)
* Add types [`rosidl_pycommon`` (`#824 ](https://github.com/ros2/rosidl/issues/824)_)
* Contributors: Michael Carlstrom, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_introspection_cpp <https://github.com/ros2/rosidl/tree/kilted/rosidl_typesupport_introspection_cpp/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#860 ](https://github.com/ros2/rosidl/issues/860)_)
* Add types [`rosidl_pycommon`` (`#824 ](https://github.com/ros2/rosidl/issues/824)_)
* Contributors: Michael Carlstrom, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_introspection_tests <https://github.com/ros2/rosidl/tree/kilted/rosidl_typesupport_introspection_tests/CHANGELOG.rst>`__

* Suppress false positive warnings from gcc. ([#811 ](https://github.com/ros2/rosidl/issues/811)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_tests <https://github.com/ros2/rosidl_typesupport/tree/kilted/rosidl_typesupport_tests/CHANGELOG.rst>`__

* Uniform cmake requirement ([#163 ](https://github.com/ros2/rosidl_typesupport/issues/163)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rpyutils <https://github.com/ros2/rpyutils/tree/kilted/CHANGELOG.rst>`__

* Add py.typed to Package Data ([#16 ](https://github.com/ros2/rpyutils/issues/16)_)
* Add Create py.typed ([#15 ](https://github.com/ros2/rpyutils/issues/15)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#13 ](https://github.com/ros2/rpyutils/issues/13)_)
* Add types and ament_mypy to rpyutils. ([#12 ](https://github.com/ros2/rpyutils/issues/12)_)
* Contributors: Chris Lalancette, Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_bag <https://github.com/ros-visualization/rqt_bag/tree/kilted/rqt_bag/CHANGELOG.rst>`__

* Add standard tests for rqt_bag and rqt_bag_plugins ([#171 ](https://github.com/ros-visualization/rqt_bag/issues/171)_)
* Updated player QoS ([#164 ](https://github.com/ros-visualization/rqt_bag/issues/164)_)
* Adapted to rosbag2_py ([#156 ](https://github.com/ros-visualization/rqt_bag/issues/156)_)
* Fixed button icons ([#159 ](https://github.com/ros-visualization/rqt_bag/issues/159)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_bag_plugins <https://github.com/ros-visualization/rqt_bag/tree/kilted/rqt_bag_plugins/CHANGELOG.rst>`__

* Add standard tests for rqt_bag and rqt_bag_plugins ([#171 ](https://github.com/ros-visualization/rqt_bag/issues/171)_)
* Adapted to rosbag2_py ([#156 ](https://github.com/ros-visualization/rqt_bag/issues/156)_)
* Fixed image timeline renderer ([#158 ](https://github.com/ros-visualization/rqt_bag/issues/158)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_console <https://github.com/ros-visualization/rqt_console/tree/kilted/CHANGELOG.rst>`__

* Add in standard tests. ([#48 ](https://github.com/ros-visualization/rqt_console/issues/48)_)
* Remove CODEOWNERS and mirror-rolling-to-main workflow ([#46 ](https://github.com/ros-visualization/rqt_console/issues/46)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_graph <https://github.com/ros-visualization/rqt_graph/tree/kilted/CHANGELOG.rst>`__

* Add in standard tests. ([#104 ](https://github.com/ros-visualization/rqt_graph/issues/104)_)
* Remove CODEOWNERS ([#102 ](https://github.com/ros-visualization/rqt_graph/issues/102)_)
* Fixed fit_in_view icon button ([#95 ](https://github.com/ros-visualization/rqt_graph/issues/95)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_gui <https://github.com/ros-visualization/rqt/tree/kilted/rqt_gui/CHANGELOG.rst>`__

* Add in standard tests for rqt_gui and rqt_gui_py ([#318 ](https://github.com/ros-visualization/rqt/issues/318)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_gui_cpp <https://github.com/ros-visualization/rqt/tree/kilted/rqt_gui_cpp/CHANGELOG.rst>`__

* Added common test to rqt_gui_cpp and deprecate h headers ([#311 ](https://github.com/ros-visualization/rqt/issues/311)_)
* Updated deprecated qt_gui_cpp headers ([#309 ](https://github.com/ros-visualization/rqt/issues/309)_)
* Contributors: Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_gui_py <https://github.com/ros-visualization/rqt/tree/kilted/rqt_gui_py/CHANGELOG.rst>`__

* Add in standard tests for rqt_gui and rqt_gui_py ([#318 ](https://github.com/ros-visualization/rqt/issues/318)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_plot <https://github.com/ros-visualization/rqt_plot/tree/kilted/CHANGELOG.rst>`__

* Add unit tests for topic name validation & field expansion ([#108 ](https://github.com/ros-visualization/rqt_plot/issues/108)_)
* Fix double slash when plotting all sub-fields with trailing slash ([#107 ](https://github.com/ros-visualization/rqt_plot/issues/107)_)
* Fix listing of nested basic type fields ([#101 ](https://github.com/ros-visualization/rqt_plot/issues/101)_)
* Fix f-string and add single quote around field name ([#100 ](https://github.com/ros-visualization/rqt_plot/issues/100)_)
* Add single quotes around topic in validation msg for consistency ([#99 ](https://github.com/ros-visualization/rqt_plot/issues/99)_) This is more consistent with the other messages below.
* Add in the rest of the standard ament_python tests. ([#98 ](https://github.com/ros-visualization/rqt_plot/issues/98)_)
* Remove CODEOWNERS ([#96 ](https://github.com/ros-visualization/rqt_plot/issues/96)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_publisher <https://github.com/ros-visualization/rqt_publisher/tree/kilted/CHANGELOG.rst>`__

* Add in the remaining standard ament_python tests. ([#49 ](https://github.com/ros-visualization/rqt_publisher/issues/49)_)
* Add in LICENSE. ([#46 ](https://github.com/ros-visualization/rqt_publisher/issues/46)_)
* Remove CODEOWNERS ([#47 ](https://github.com/ros-visualization/rqt_publisher/issues/47)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_py_common <https://github.com/ros-visualization/rqt/tree/kilted/rqt_py_common/CHANGELOG.rst>`__

* Stop using python_cmake_module. ([#304 ](https://github.com/ros-visualization/rqt/issues/304)_)
* Use an rclpy context manager. ([#312 ](https://github.com/ros-visualization/rqt/issues/312)_)
* Added common test to rqt_py_common ([#310 ](https://github.com/ros-visualization/rqt/issues/310)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_py_console <https://github.com/ros-visualization/rqt_py_console/tree/kilted/CHANGELOG.rst>`__

* Add the standard tests to rqt_py_console. ([#19 ](https://github.com/ros-visualization/rqt_py_console/issues/19)_)
* Remove CODEOWNERS ([#17 ](https://github.com/ros-visualization/rqt_py_console/issues/17)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_service_caller <https://github.com/ros-visualization/rqt_service_caller/tree/kilted/CHANGELOG.rst>`__

* Update rqt_service_caller to our standard policies. ([#31 ](https://github.com/ros-visualization/rqt_service_caller/issues/31)_)
* Remove CODEOWNERS ([#29 ](https://github.com/ros-visualization/rqt_service_caller/issues/29)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_shell <https://github.com/ros-visualization/rqt_shell/tree/kilted/CHANGELOG.rst>`__

* Add in standard tests to rqt_shell. ([#24 ](https://github.com/ros-visualization/rqt_shell/issues/24)_) That way we know it conforms to our standards.
* Remove CODEOWNERS ([#22 ](https://github.com/ros-visualization/rqt_shell/issues/22)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_topic <https://github.com/ros-visualization/rqt_topic/tree/kilted/CHANGELOG.rst>`__

* Override subscriber qos ([#51 ](https://github.com/ros-visualization/rqt_topic//issues/51)_)
* Remove CODEOWNERS ([#52 ](https://github.com/ros-visualization/rqt_topic//issues/52)_)
* Contributors: Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rti_connext_dds_cmake_module <https://github.com/ros2/rmw_connextdds/tree/kilted/rti_connext_dds_cmake_module/CHANGELOG.rst>`__

* Update Connext to 7.3.0 ([#181 ](https://github.com/ros2/rmw_connextdds/issues/181)_)
* Quiet a warning when CONNEXTDDS_DIR or NDDSHOME is not found. ([#158 ](https://github.com/ros2/rmw_connextdds/issues/158)_)
* Contributors: Chris Lalancette, lobolanja


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rttest <https://github.com/ros2/realtime_support/tree/kilted/rttest/CHANGELOG.rst>`__

* Don't try to build on BSD ([#126 ](https://github.com/ros2/realtime_support/issues/126)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz2 <https://github.com/ros2/rviz/tree/kilted/rviz2/CHANGELOG.rst>`__

* Expose the possibility to create ROS node with custom [`NodeOptions`` (`#1347 ](https://github.com/ros2/rviz/issues/1347)_)
* uniform CMAKE requirement ([#1335 ](https://github.com/ros2/rviz/issues/1335)_)
* Detect wayland and make sure X rendering is used. ([#1253 ](https://github.com/ros2/rviz/issues/1253)_)
* Fixed RViz2 linters ([#1231 ](https://github.com/ros2/rviz/issues/1231)_)
* Contributors: Alejandro Hernández Cordero, Matthew Elwin, Patrick Roncagliolo, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_assimp_vendor <https://github.com/ros2/rviz/tree/kilted/rviz_assimp_vendor/CHANGELOG.rst>`__

* Revert "Update ASSIMP_VENDOR CMakeLists.txt ([#1226 ](https://github.com/ros2/rviz/issues/1226)_)" ([#1249 ](https://github.com/ros2/rviz/issues/1249)_)
* Update ASSIMP_VENDOR CMakeLists.txt ([#1226 ](https://github.com/ros2/rviz/issues/1226)_) CLEAN UNUSED CHECK SE MIN ASSIMP VERSION TO 5.3.1 SET C++ VERSION TO 17
* Contributors: Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_common <https://github.com/ros2/rviz/tree/kilted/rviz_common/CHANGELOG.rst>`__

* Work in progress using the new resource retriever apis ([#1262 ](https://github.com/ros2/rviz/issues/1262)_)
* addTrackedObject Function Fails to Handle Null Pointer, Causing Crash When nullptr is Passed ([#1375 ](https://github.com/ros2/rviz/issues/1375)_)
* Add test to check mapGetString when key is missing ([#1361 ](https://github.com/ros2/rviz/issues/1361)_)
* UniformStringStream::parseFloat Fails to Handle Invalid Float Formats Correctly ([#1360 ](https://github.com/ros2/rviz/issues/1360)_)
* Fix Potential Null Pointer Dereference in VisualizerApp::getRenderWindow() to Prevent Crashes ([#1359 ](https://github.com/ros2/rviz/issues/1359)_)
* Extend support for type adaptation (REP 2007) in rviz_common for TF-filtered displays ([#1346 ](https://github.com/ros2/rviz/issues/1346)_)
* Expose the possibility to create ROS node with custom [`NodeOptions`` (`#1347 ](https://github.com/ros2/rviz/issues/1347)_)
* uniform CMAKE requirement ([#1335 ](https://github.com/ros2/rviz/issues/1335)_)
* Add basic support for type adaptation (REP 2007) in [`rviz_common`` for displays (`#1331 ](https://github.com/ros2/rviz/issues/1331)_)
* Fix preferred tools loading names ([#1321 ](https://github.com/ros2/rviz/issues/1321)_)
* Add RVIZ_COMMON_PUBLIC macro to ToolManager ([#1323 ](https://github.com/ros2/rviz/issues/1323)_)
* Clean visualization_manager.cpp ([#1317 ](https://github.com/ros2/rviz/issues/1317)_)
* Fix Deprecated tf2 headers ([#1289 ](https://github.com/ros2/rviz/issues/1289)_)
* include QString ([#1298 ](https://github.com/ros2/rviz/issues/1298)_)
* Handle time source exception ([#1285 ](https://github.com/ros2/rviz/issues/1285)_)
* Fully handle [`Tool::processKeyEvent`` return value (`#1270 ](https://github.com/ros2/rviz/issues/1270)_)
* Handle [`Tool::Finished`` returned by ``processKeyEvent`` (`#1257 ](https://github.com/ros2/rviz/issues/1257)_)
* Added more time to copyright on Windwos ([#1252 ](https://github.com/ros2/rviz/issues/1252)_)
* Added common test for rviz_common ([#1232 ](https://github.com/ros2/rviz/issues/1232)_)
* Set ContentsMargins for RenderPanel to 0 to avoid borders in fullscreen mode. Fixes [#1024 ](https://github.com/ros2/rviz/issues/1024)_ ([#1228 ](https://github.com/ros2/rviz/issues/1228)_)
* Updated deprecated message filter headers ([#1239 ](https://github.com/ros2/rviz/issues/1239)_)
* Correclty load icons of panels with whitespaces in their name ([#1241 ](https://github.com/ros2/rviz/issues/1241)_)
* Prepping for qos deprecation ([#1214 ](https://github.com/ros2/rviz/issues/1214)_)
* Replace ESC shortcut for exiting full screen with solution from https://github.com/ros-visualization/rviz/pull/1416 ([#1205 ](https://github.com/ros2/rviz/issues/1205)_)
* Contributors: Alejandro Hernández Cordero, Bo Chen, Lucas Wendland, Matthew Foran, Michael Carroll, Michael Ripperger, Patrick Roncagliolo, RaduPopescu, Silvio Traversaro, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_default_plugins <https://github.com/ros2/rviz/tree/kilted/rviz_default_plugins/CHANGELOG.rst>`__

* PointCloudDisplay: Fix decay time 0 keeping more than the last message ([#1400 ](https://github.com/ros2/rviz/issues/1400)_)
* Work in progress using the new resource retriever apis ([#1262 ](https://github.com/ros2/rviz/issues/1262)_)
* Include chrono ([#1353 ](https://github.com/ros2/rviz/issues/1353)_)
* fix: add rclcpp::shutdown ([#1343 ](https://github.com/ros2/rviz/issues/1343)_)
* Nv12 color format ([#1318 ](https://github.com/ros2/rviz/issues/1318)_) Co-authored-by: zycczy <zycczyby@gmail.com>
* uniform CMAKE requirement ([#1335 ](https://github.com/ros2/rviz/issues/1335)_)
* Initialize lookup table only once at compile time ([#1330 ](https://github.com/ros2/rviz/issues/1330)_) Co-authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>
* Fixed the XY Orbit controller move ([#1327 ](https://github.com/ros2/rviz/issues/1327)_) Co-authored-by: Terry Scott <tscott@seegrid.com>
* Fix Deprecated tf2 headers ([#1289 ](https://github.com/ros2/rviz/issues/1289)_)
* Change EffortDisplay superclass from MessageFilterDisplay to RosTopicDisplay to avoid dropping messages with empty frame_id. ([#1312 ](https://github.com/ros2/rviz/issues/1312)_)
* Fix access control for Accel, Effort and Twist displays ([#1311 ](https://github.com/ros2/rviz/issues/1311)_)
* remove unused variable ([#1301 ](https://github.com/ros2/rviz/issues/1301)_)
* include QString ([#1298 ](https://github.com/ros2/rviz/issues/1298)_)
* Clean code for Image display ([#1271 ](https://github.com/ros2/rviz/issues/1271)_)
* Handle time source exception ([#1285 ](https://github.com/ros2/rviz/issues/1285)_)
* replace deprecated encodings 'yuv422' and 'yuv422_yuy2' ([#1276 ](https://github.com/ros2/rviz/issues/1276)_)
* Update urdf model.h deprecation ([#1266 ](https://github.com/ros2/rviz/issues/1266)_)
* Enabling manual space width for TextViewFacingMarker ([#1261 ](https://github.com/ros2/rviz/issues/1261)_)
* Added more time to copyright on Windwos ([#1252 ](https://github.com/ros2/rviz/issues/1252)_)
* Updated deprecated message filter headers ([#1239 ](https://github.com/ros2/rviz/issues/1239)_)
* Fixed RViz default plugin license linter ([#1230 ](https://github.com/ros2/rviz/issues/1230)_)
* Contributors: Alejandro Hernández Cordero, Christian Rauch, Lucas Wendland, Matthew Foran, Michael Carroll, Patrick Roncagliolo, Peng Wang, Stefan Fabian, Terry Scott, Tom Moore, Yuyuan Yuan, disRecord, mosfet80, quic-zhaoyuan, suchetanrs


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_ogre_vendor <https://github.com/ros2/rviz/tree/kilted/rviz_ogre_vendor/CHANGELOG.rst>`__

* Add missing glew dependency for ogre vendor package ([#1350 ](https://github.com/ros2/rviz/issues/1350)_)
* Use official freetype github mirror instead of savannah ([#1348 ](https://github.com/ros2/rviz/issues/1348)_)
* Fix flags for both clang and gcc. ([#1219 ](https://github.com/ros2/rviz/issues/1219)_)
* Update freetype lib ([#1216 ](https://github.com/ros2/rviz/issues/1216)_)
* Update zlib into CMakeLists.txt ([#1128 ](https://github.com/ros2/rviz/issues/1128)_) Changes in 1.3 (18 Aug 2023) - Remove K&R function definitions and zlib2ansi - Fix bug in deflateBound() for level 0 and memLevel 9 - Fix bug when gzungetc() is used immediately after gzopen() - Fix bug when using gzflush() with a very small buffer - Fix crash when gzsetparams() attempted for transparent write - Fix test/example.c to work with FORCE_STORED - Rewrite of zran in examples (see zran.c version history) - Fix minizip to allow it to open an empty zip file - Fix reading disk number start on zip64 files in minizip - Fix logic error in minizip argument processing - Add minizip testing to Makefile - Read multiple bytes instead of byte-by-byte in minizip unzip.c - Add memory sanitizer to configure (--memory) - Various portability improvements - Various documentation improvements - Various spelling and typo corrections Co-authored-by: Chris Lalancette <clalancette@gmail.com>
* Contributors: Chris Lalancette, Silvio Traversaro, Stefan Fabian, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_rendering <https://github.com/ros2/rviz/tree/kilted/rviz_rendering/CHANGELOG.rst>`__

* BillboardLine::addPoint() does not throw an exception when exceeding max_points_per_line limit ([#1436 ](https://github.com/ros2/rviz/issues/1436)_)
* Constructor ScrewVisual::ScrewVisual does not handle null pointers, leading to crashes ([#1435 ](https://github.com/ros2/rviz/issues/1435)_)
* Removed Windows warnings ([#1413 ](https://github.com/ros2/rviz/issues/1413)_)
* Memory Access Error When Handling Empty Strings in splitStringIntoTrimmedItems Function ([#1412 ](https://github.com/ros2/rviz/issues/1412)_)
* Crash due to Unhandled Null Pointer in ParameterEventsFilter Constructor ([#1411 ](https://github.com/ros2/rviz/issues/1411)_)
* MovableText constructor does not validate invalid character height, default fallback missing ([#1398 ](https://github.com/ros2/rviz/issues/1398)_)
* Invalid Parameter Handling in CovarianceVisual::CovarianceVisual Constructor ([#1396 ](https://github.com/ros2/rviz/issues/1396)_)
* Lack of Validity Check for Invalid Parameters in EffortVisual::EffortVisual Constructor ([#1395 ](https://github.com/ros2/rviz/issues/1395)_)
* Grid Class Constructor Does Not Handle Null Pointer, Leading to Program Crash ([#1394 ](https://github.com/ros2/rviz/issues/1394)_)
* Crash in MovableText::update() when caption is an empty string due to uninitialized resource usage ([#1393 ](https://github.com/ros2/rviz/issues/1393)_)
* Work in progress using the new resource retriever apis ([#1262 ](https://github.com/ros2/rviz/issues/1262)_)
* uniform CMAKE requirement ([#1335 ](https://github.com/ros2/rviz/issues/1335)_)
* Clean ogre_render_window_impl.cpp ([#1334 ](https://github.com/ros2/rviz/issues/1334)_)
* include QString ([#1298 ](https://github.com/ros2/rviz/issues/1298)_)
* Use consistent conditionals in render_system.hpp ([#1294 ](https://github.com/ros2/rviz/issues/1294)_)
* Avoid redefinition of default color materials ([#1281 ](https://github.com/ros2/rviz/issues/1281)_)
* Added more time to copyright on Windwos ([#1252 ](https://github.com/ros2/rviz/issues/1252)_)
* Fix: issue [#1220 ](https://github.com/ros2/rviz/issues/1220)_. ([#1237 ](https://github.com/ros2/rviz/issues/1237)_) Co-authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>
* Added common test: rviz_rendering ([#1233 ](https://github.com/ros2/rviz/issues/1233)_)
* Contributors: Alejandro Hernández Cordero, Masayoshi Dohi, Matthew Foran, Michael Carroll, Scott K Logan, chama1176, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_rendering_tests <https://github.com/ros2/rviz/tree/kilted/rviz_rendering_tests/CHANGELOG.rst>`__

* Work in progress using the new resource retriever apis ([#1262 ](https://github.com/ros2/rviz/issues/1262)_)
* uniform CMAKE requirement ([#1335 ](https://github.com/ros2/rviz/issues/1335)_)
* Added common test to rviz_rendering_tests ([#1234 ](https://github.com/ros2/rviz/issues/1234)_)
* Contributors: Alejandro Hernández Cordero, Michael Carroll, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_resource_interfaces <https://github.com/ros2/rviz/tree/kilted/rviz_resource_interfaces/CHANGELOG.rst>`__

* Work in progress using the new resource retriever apis ([#1262 ](https://github.com/ros2/rviz/issues/1262)_)
* Contributors: Michael Carroll


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_visual_testing_framework <https://github.com/ros2/rviz/tree/kilted/rviz_visual_testing_framework/CHANGELOG.rst>`__

* uniform CMAKE requirement ([#1335 ](https://github.com/ros2/rviz/issues/1335)_)
* Fix Deprecated tf2 headers ([#1289 ](https://github.com/ros2/rviz/issues/1289)_)
* include QString ([#1298 ](https://github.com/ros2/rviz/issues/1298)_)
* Added common test to rviz_visual_testing_framework ([#1235 ](https://github.com/ros2/rviz/issues/1235)_)
* Contributors: Alejandro Hernández Cordero, Lucas Wendland, Matthew Foran, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sensor_msgs <https://github.com/ros2/common_interfaces/tree/kilted/sensor_msgs/CHANGELOG.rst>`__

* Add NV12 to color formats ([#253 ](https://github.com/ros2/common_interfaces/issues/253)_)
* Contributors: Lukas Schäper


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sensor_msgs_py <https://github.com/ros2/common_interfaces/tree/kilted/sensor_msgs_py/CHANGELOG.rst>`__

* Add ament_xmllint to sensor_msgs_py. ([#259 ](https://github.com/ros2/common_interfaces/issues/259)_)
* Fix formatting in sensor_msgs_py ([#248 ](https://github.com/ros2/common_interfaces/issues/248)_)
* Contributors: Chris Lalancette, Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `service_msgs <https://github.com/ros2/rcl_interfaces/tree/kilted/service_msgs/CHANGELOG.rst>`__

* Add missing build_export_depend on rosidl_core_runtime ([#165 ](https://github.com/ros2/rcl_interfaces/issues/165)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sqlite3_vendor <https://github.com/ros2/rosbag2/tree/kilted/sqlite3_vendor/CHANGELOG.rst>`__

* Bump sqlite3 to 3.45.1 ([#1737 ](https://github.com/ros2/rosbag2/issues/1737)_)
* Contributors: Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sros2 <https://github.com/ros2/sros2/tree/kilted/sros2/CHANGELOG.rst>`__

* Switch to get_rmw_additional_env ([#339 ](https://github.com/ros2/sros2/issues/339)_)
* Fix github-workflow mypy error ([#336 ](https://github.com/ros2/sros2/issues/336)_)
* Give more time to generate policies in tests ([#323 ](https://github.com/ros2/sros2/issues/323)_)
* Switch to context manager for rclpy tests. ([#322 ](https://github.com/ros2/sros2/issues/322)_)
* [FIX] remove dangerous mutable default arguments in generate_artifacts ([#318 ](https://github.com/ros2/sros2/issues/318)_)
* Fix sros2 tests on Windows Debug. ([#317 ](https://github.com/ros2/sros2/issues/317)_)
* [TESTS] Update tests and add test for generate_artifacts ([#311 ](https://github.com/ros2/sros2/issues/311)_)
* remove deprecated create_key and list_keys verbs ([#302 ](https://github.com/ros2/sros2/issues/302)_)
* Fix linux tutorial: cloning example policies and set of default policies for a node ([#295 ](https://github.com/ros2/sros2/issues/295)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Mikael Arguedas, Tomoya Fujita, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_cli <https://github.com/ros2/system_tests/tree/kilted/test_cli/CHANGELOG.rst>`__

* Stop using python_cmake_module. ([#536 ](https://github.com/ros2/system_tests/issues/536)_)
* Use rclpy.init context manager where we can. ([#547 ](https://github.com/ros2/system_tests/issues/547)_) This allows us to cleanup, while using a lot less code to try and track it.
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_cli_remapping <https://github.com/ros2/system_tests/tree/kilted/test_cli_remapping/CHANGELOG.rst>`__

* Stop using python_cmake_module. ([#536 ](https://github.com/ros2/system_tests/issues/536)_)
* Use rclpy.init context manager where we can. ([#547 ](https://github.com/ros2/system_tests/issues/547)_) This allows us to cleanup, while using a lot less code to try and track it.
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_communication <https://github.com/ros2/system_tests/tree/kilted/test_communication/CHANGELOG.rst>`__

* Use EnableRmwIsolation in launch tests ([#571 ](https://github.com/ros2/system_tests/issues/571)_)
* Switch to isolated test fixture macros ([#571 ](https://github.com/ros2/system_tests/issues/571)_)
* Add tests for Keyed types ([#568 ](https://github.com/ros2/system_tests/issues/568)_)
* Remove use of ament_target_dependencies ([#566 ](https://github.com/ros2/system_tests/issues/566)_)
* Skip all multi-vendor pub/sub tests with zenoh ([#560 ](https://github.com/ros2/system_tests/issues/560)_)
* Stop using python_cmake_module. ([#536 ](https://github.com/ros2/system_tests/issues/536)_)
* Use rclpy.init context manager where we can. ([#547 ](https://github.com/ros2/system_tests/issues/547)_) This allows us to cleanup, while using a lot less code to try and track it.
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Francisco Gallego Salido, Scott K Logan, Shane Loretz, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_interface_files <https://github.com/ros2/test_interface_files/tree/kilted/CHANGELOG.rst>`__

* Drop long double from the IDL. ([#22 ](https://github.com/ros2/test_interface_files/issues/22)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_launch_ros <https://github.com/ros2/launch_ros/tree/kilted/test_launch_ros/CHANGELOG.rst>`__

* Add python3-pytest-timeout to test_launch_ros. ([#454 ](https://github.com/ros2/launch_ros/issues/454)_)
* Autostarting lifecycle nodes and example launch file demo ([#430 ](https://github.com/ros2/launch_ros/issues/430)_)
* Add ament_xmllint to the ament_python packages. ([#423 ](https://github.com/ros2/launch_ros/issues/423)_)
* Add in a timeout for test_launch_ros. ([#417 ](https://github.com/ros2/launch_ros/issues/417)_)
* Fix url in setup.py ([#413 ](https://github.com/ros2/launch_ros/issues/413)_)
* Revamp the test_load_composable_nodes test. ([#403 ](https://github.com/ros2/launch_ros/issues/403)_)
* Switch to use rclpy.init context manager. ([#402 ](https://github.com/ros2/launch_ros/issues/402)_)
* Contributors: Chris Lalancette, Steve Macenski, Tomoya Fujita, Wei HU


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_msgs <https://github.com/ros2/rcl_interfaces/tree/kilted/test_msgs/CHANGELOG.rst>`__

* Added test messages with keys ([#173 ](https://github.com/ros2/rcl_interfaces/issues/173)_)
* Contributors: Francisco Gallego Salido


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_osrf_testing_tools_cpp <https://github.com/osrf/osrf_testing_tools_cpp/tree/kilted/test_osrf_testing_tools_cpp/CHANGELOG.rst>`__

* Update CMakeLists.txt ([#85 ](https://github.com/osrf/osrf_testing_tools_cpp/issues/85)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_quality_of_service <https://github.com/ros2/system_tests/tree/kilted/test_quality_of_service/CHANGELOG.rst>`__

* Switch to isolated test fixture macros ([#571 ](https://github.com/ros2/system_tests/issues/571)_)
* Use rmw_event_type_is_supported to skip tests ([#563 ](https://github.com/ros2/system_tests/issues/563)_)
* Fixed some qos test related with Zenoh ([#551 ](https://github.com/ros2/system_tests/issues/551)_)
* Contributors: Alejandro Hernández Cordero, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_rclcpp <https://github.com/ros2/system_tests/tree/kilted/test_rclcpp/CHANGELOG.rst>`__

* Use EnableRmwIsolation in launch tests ([#571 ](https://github.com/ros2/system_tests/issues/571)_)
* Ensure test verifies the existence of all spawning nodes ([#558 ](https://github.com/ros2/system_tests/issues/558)_)
* chore: Adopted to API changes in rclcpp ([#556 ](https://github.com/ros2/system_tests/issues/556)_)
* Implement the pure-virtual functions in the Waitable class. ([#548 ](https://github.com/ros2/system_tests/issues/548)_)
* Update deprecated methods ([#546 ](https://github.com/ros2/system_tests/issues/546)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Janosch Machowinski, Scott K Logan, Yuyuan Yuan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_rmw_implementation <https://github.com/ros2/rmw_implementation/tree/kilted/test_rmw_implementation/CHANGELOG.rst>`__

* Added rmw_event_type_is_supported ([#250 ](https://github.com/ros2/rmw_implementation/issues/250)_) * Added rmw_event_check_compatible * fix return typoe * updated name and use in wait_set test ---------
* Update expectations of tests to remain compatible with non-DDS middlewares ([#248 ](https://github.com/ros2/rmw_implementation/issues/248)_)
* use rmw_enclave_options_xxx APIs instead. ([#247 ](https://github.com/ros2/rmw_implementation/issues/247)_)
* Fix up some overwritten errors. ([#246 ](https://github.com/ros2/rmw_implementation/issues/246)_) That is, make sure to clear out errors where we should. We also slightly rewrite some of the testing around unsupported APIs, so that they make more sense.
* Do not deref msg ptr for rmw\_{publish,return}_loaned_message*() ([#240 ](https://github.com/ros2/rmw_implementation/issues/240)_)
* remove rmw_localhost_only_t. ([#239 ](https://github.com/ros2/rmw_implementation/issues/239)_)
* Expect rmw_service_server_is_available to ret RMW_RET_INVALID_ARGUMENT ([#231 ](https://github.com/ros2/rmw_implementation/issues/231)_)
* Expect rmw_destroy_wait_set to ret RMW_RET_INVALID_ARGUMENT ([#234 ](https://github.com/ros2/rmw_implementation/issues/234)_)
* Add test creating two content filter topics with the same topic name ([#230 ](https://github.com/ros2/rmw_implementation/issues/230)_) ([#233 ](https://github.com/ros2/rmw_implementation/issues/233)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Tomoya Fujita, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_ros2trace <https://github.com/ros2/ros2_tracing/tree/kilted/test_ros2trace/CHANGELOG.rst>`__

* Add timeout to test_ros2trace tests that wait on stdout ([#167 ](https://github.com/ros2/ros2_tracing/issues/167)_)
* Allow enabling syscalls through [`ros2 trace`` or the Trace action (`#137 ](https://github.com/ros2/ros2_tracing/issues/137)_)
* Contributors: Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_tf2 <https://github.com/ros2/geometry2/tree/kilted/test_tf2/CHANGELOG.rst>`__

* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Add [`rclcpp::shutdown`` (`#762 ](https://github.com/ros2/geometry2/issues/762)_)
* Remove many extra conversions from Matrix3x3 to Quaternion ([#741 ](https://github.com/ros2/geometry2/issues/741)_) Co-authored-by: jmachowinski <jmachowinski@users.noreply.github.com> Co-authored-by: Katherine Scott <katherineAScott@gmail.com>
* Deprecate C Headers ([#720 ](https://github.com/ros2/geometry2/issues/720)_)
* Switch to using a context manager for the python examples. ([#700 ](https://github.com/ros2/geometry2/issues/700)_) That way we can be sure to always clean up, but use less code doing so.
* Contributors: Chris Lalancette, Lucas Wendland, Yuyuan Yuan, kyle-basis, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_tracetools <https://github.com/ros2/ros2_tracing/tree/kilted/test_tracetools/CHANGELOG.rst>`__

* Run test_tracetools tests against rmw_zenoh_cpp ([#140 ](https://github.com/ros2/ros2_tracing/issues/140)_)
* Use ament_add_ros_isolated\_* in test_tracetools ([#159 ](https://github.com/ros2/ros2_tracing/issues/159)_)
* Instrument client/service for end-to-end request/response tracking ([#145 ](https://github.com/ros2/ros2_tracing/issues/145)_)
* Don't try to build on BSD ([#142 ](https://github.com/ros2/ros2_tracing/issues/142)_) The 'BSD' variable was added in CMake 3.25. Note that variables which are not defined will evaluate to 'False', so this shouldn't regress platforms using CMake versions older than 3.25.
* Refactor and split test_service into test\_{service,client} ([#144 ](https://github.com/ros2/ros2_tracing/issues/144)_)
* Change expected rmw GID array size to 16 bytes ([#138 ](https://github.com/ros2/ros2_tracing/issues/138)_)
* Run test_tracetools tests against rmw_fastrtps_dynamic_cpp too ([#127 ](https://github.com/ros2/ros2_tracing/issues/127)_)
* Make test_tracetools ping pubs/subs transient_local ([#125 ](https://github.com/ros2/ros2_tracing/issues/125)_)
* Run relevant test_tracetools tests with all instrumented rmw impls ([#116 ](https://github.com/ros2/ros2_tracing/issues/116)_)
* Contributors: Christophe Bedard, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_tracetools_launch <https://github.com/ros2/ros2_tracing/tree/kilted/test_tracetools_launch/CHANGELOG.rst>`__

* Fix or ignore new mypy issues ([#161 ](https://github.com/ros2/ros2_tracing/issues/161)_)
* Allow enabling syscalls through [`ros2 trace`` or the Trace action (`#137 ](https://github.com/ros2/ros2_tracing/issues/137)_)
* Contributors: Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2 <https://github.com/ros2/geometry2/tree/kilted/tf2/CHANGELOG.rst>`__

* Add isnan support ([#780 ](https://github.com/ros2/geometry2/issues/780)_)
* Overflow Issue in durationFromSec() Function when Handling Extremely Large or Small Values ([#785 ](https://github.com/ros2/geometry2/issues/785)_)
* Do not clobber callback handles when cancelling pending transformable requests ([#779 ](https://github.com/ros2/geometry2/issues/779)_)
* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Remove many extra conversions from Matrix3x3 to Quaternion ([#741 ](https://github.com/ros2/geometry2/issues/741)_) Co-authored-by: jmachowinski <jmachowinski@users.noreply.github.com> Co-authored-by: Katherine Scott <katherineAScott@gmail.com>
* Cleanup deprecation warnings. ([#744 ](https://github.com/ros2/geometry2/issues/744)_) The deprecation warnings were not printing out properly on GCC, at least; it would warn that #warning was not standard, and it would also not print out the actual warning.  Also "deprecated" was spelled wrong.  Fix all of these issues here.
* Deprecate C Headers ([#720 ](https://github.com/ros2/geometry2/issues/720)_)
* Removed unused var in tf2 ([#735 ](https://github.com/ros2/geometry2/issues/735)_)
* Error String Filled ([#715 ](https://github.com/ros2/geometry2//issues/715)_)
* Removed deprecated enuns ([#699 ](https://github.com/ros2/geometry2//issues/699)_)
* [TimeCache] Improve performance for insertData() and pruneList() ([#680 ](https://github.com/ros2/geometry2/issues/680)_) Co-authored-by: Chris Lalancette <clalancette@gmail.com>
* Removed warning ([#682 ](https://github.com/ros2/geometry2/issues/682)_)
* Add cache_benchmark ([#679 ](https://github.com/ros2/geometry2/issues/679)_) * Add cache_benchmark Co-authored-by: Chris Lalancette <clalancette@gmail.com>
* [cache_unittest] Add direct implementation testing on ordering, pruning ([#678 ](https://github.com/ros2/geometry2/issues/678)_) * [cache_unittest] Add direct implementation testing on ordering, pruning * do getAllItems() approach * Return a reference instead. * mark getAllItems as internal * Fix warning on Windows. Co-authored-by: Chris Lalancette <clalancette@gmail.com>
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Eric Cousineau, Lucas Wendland, Michael Carlstrom, Timo Röhling, cramke, kyle-basis, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_bullet <https://github.com/ros2/geometry2/tree/kilted/tf2_bullet/CHANGELOG.rst>`__

* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Deprecate C Headers ([#720 ](https://github.com/ros2/geometry2/issues/720)_)
* Contributors: Lucas Wendland, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_eigen <https://github.com/ros2/geometry2/tree/kilted/tf2_eigen/CHANGELOG.rst>`__

* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Deprecate C Headers ([#720 ](https://github.com/ros2/geometry2/issues/720)_)
* Contributors: Lucas Wendland, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_eigen_kdl <https://github.com/ros2/geometry2/tree/kilted/tf2_eigen_kdl/CHANGELOG.rst>`__

* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Deprecate C Headers ([#720 ](https://github.com/ros2/geometry2/issues/720)_)
* Contributors: Lucas Wendland, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_geometry_msgs <https://github.com/ros2/geometry2/tree/kilted/tf2_geometry_msgs/CHANGELOG.rst>`__

* Remove many extra conversions from Matrix3x3 to Quaternion ([#741 ](https://github.com/ros2/geometry2/issues/741)_) Co-authored-by: jmachowinski <jmachowinski@users.noreply.github.com> Co-authored-by: Katherine Scott <katherineAScott@gmail.com>
* Deprecate C Headers ([#720 ](https://github.com/ros2/geometry2/issues/720)_)
* Add a python3-dev dependency to tf2_py. ([#733 ](https://github.com/ros2/geometry2/issues/733)_)
* Fix tf2_geometry_msgs_INCLUDE_DIRS. ([#729 ](https://github.com/ros2/geometry2/issues/729)_)
* Remove use of python_cmake_module ([#651 ](https://github.com/ros2/geometry2//issues/651)_)
* Contributors: Chris Lalancette, Lucas Wendland, kyle-basis, rkeating-planted


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_kdl <https://github.com/ros2/geometry2/tree/kilted/tf2_kdl/CHANGELOG.rst>`__

* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Fix external docs mappings ([#757 ](https://github.com/ros2/geometry2/issues/757)_)
* tf2_kdl: add python_orocos_kdl_vendor dependency ([#745 ](https://github.com/ros2/geometry2/issues/745)_) * tf2_kdl: add python_orocos_kdl_vendor dependency The tf2_kdl Python API depends on PyKDL, which is provided by python_orocos_kdl_vendor. * tf2_kdl: remove tf2_msgs test dependency This dependency is not needed.
* Deprecate C Headers ([#720 ](https://github.com/ros2/geometry2/issues/720)_)
* Contributors: Ben Wolsieffer, Emmanuel, Lucas Wendland, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_msgs <https://github.com/ros2/geometry2/tree/kilted/tf2_msgs/CHANGELOG.rst>`__

* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_py <https://github.com/ros2/geometry2/tree/kilted/tf2_py/CHANGELOG.rst>`__

* Deprecate C Headers ([#720 ](https://github.com/ros2/geometry2/issues/720)_)
* Add a python3-dev dependency to tf2_py. ([#733 ](https://github.com/ros2/geometry2/issues/733)_)
* Remove use of python_cmake_module ([#651 ](https://github.com/ros2/geometry2//issues/651)_)
* Contributors: Chris Lalancette, Lucas Wendland


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_ros <https://github.com/ros2/geometry2/tree/kilted/tf2_ros/CHANGELOG.rst>`__

* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Add [`rclcpp::shutdown`` (`#762 ](https://github.com/ros2/geometry2/issues/762)_)
* Fix external docs mappings ([#757 ](https://github.com/ros2/geometry2/issues/757)_)
* Deprecate C Headers ([#720 ](https://github.com/ros2/geometry2/issues/720)_)
* specified quaternion order to be xyzw ([#718 ](https://github.com/ros2/geometry2/issues/718)_)
* Add configurable TF topics ([#709 ](https://github.com/ros2/geometry2//issues/709)_)
* Adding static transform listener ([#673 ](https://github.com/ros2/geometry2/issues/673)_)
* Updated deprecated message filter headers ([#702 ](https://github.com/ros2/geometry2/issues/702)_)
* Update qos for deprecation ([#695 ](https://github.com/ros2/geometry2/issues/695)_)
* Cli tools documentation ([#653 ](https://github.com/ros2/geometry2/issues/653)_)
* Contributors: Abhishek Kashyap, Alejandro Hernández Cordero, Emmanuel, Lucas Wendland, Ryan, Tom Moore, Yuyuan Yuan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_ros_py <https://github.com/ros2/geometry2/tree/kilted/tf2_ros_py/CHANGELOG.rst>`__

* Fix external docs mappings ([#757 ](https://github.com/ros2/geometry2/issues/757)_)
* Add in the linters for tf2_ros_py. ([#740 ](https://github.com/ros2/geometry2/issues/740)_)
* Adding StaticTransformListener in Python ([#719 ](https://github.com/ros2/geometry2/issues/719)_)
* Add in test_xmllint for geometry2 python packages. ([#725 ](https://github.com/ros2/geometry2/issues/725)_)
* Add configurable TF topics ([#709 ](https://github.com/ros2/geometry2//issues/709)_)
* Fix the time_jump_callback signature. ([#711 ](https://github.com/ros2/geometry2//issues/711)_)
* Switch to using a context manager for the python examples. ([#700 ](https://github.com/ros2/geometry2/issues/700)_) That way we can be sure to always clean up, but use less code doing so.
* Contributors: Chris Lalancette, Emmanuel, Lucas Wendland, Ryan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_sensor_msgs <https://github.com/ros2/geometry2/tree/kilted/tf2_sensor_msgs/CHANGELOG.rst>`__

* Deprecate C Headers ([#720 ](https://github.com/ros2/geometry2/issues/720)_)
* Add a python3-dev dependency to tf2_py. ([#733 ](https://github.com/ros2/geometry2/issues/733)_)
* Remove use of python_cmake_module ([#651 ](https://github.com/ros2/geometry2//issues/651)_)
* Contributors: Chris Lalancette, Lucas Wendland


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_tools <https://github.com/ros2/geometry2/tree/kilted/tf2_tools/CHANGELOG.rst>`__

* Add in test_xmllint for geometry2 python packages. ([#725 ](https://github.com/ros2/geometry2/issues/725)_)
* Add configurable TF topics ([#709 ](https://github.com/ros2/geometry2//issues/709)_)
* [view_frames] log filenames after it's been determined ([#674 ](https://github.com/ros2/geometry2/issues/674)_)
* Contributors: Chris Lalancette, Mikael Arguedas, Ryan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tlsf <https://github.com/ros2/tlsf/tree/kilted/tlsf/CHANGELOG.rst>`__

* Fixed link ([#15 ](https://github.com/ros2/tlsf/issues/15)_)
* Contributors: Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tlsf_cpp <https://github.com/ros2/realtime_support/tree/kilted/tlsf_cpp/CHANGELOG.rst>`__

* Explicitly shutdown context before test exits ([#129 ](https://github.com/ros2/realtime_support/issues/129)_)
* Reduce the number of files we compile. ([#125 ](https://github.com/ros2/realtime_support/issues/125)_)
* Contributors: Chris Lalancette, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `topic_monitor <https://github.com/ros2/demos/tree/kilted/topic_monitor/CHANGELOG.rst>`__

* Add test_xmllint.py to all of the ament_python packages. ([#704 ](https://github.com/ros2/demos/issues/704)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `topic_statistics_demo <https://github.com/ros2/demos/tree/kilted/topic_statistics_demo/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools <https://github.com/ros2/ros2_tracing/tree/kilted/tracetools/CHANGELOG.rst>`__

* Switch to ament_cmake_ros_core package ([#162 ](https://github.com/ros2/ros2_tracing/issues/162)_)
* Instrument client/service for end-to-end request/response tracking ([#145 ](https://github.com/ros2/ros2_tracing/issues/145)_)
* Don't try to build on BSD ([#142 ](https://github.com/ros2/ros2_tracing/issues/142)_)
* Change expected rmw GID array size to 16 bytes ([#138 ](https://github.com/ros2/ros2_tracing/issues/138)_)
* Fix up two different C problems. ([#129 ](https://github.com/ros2/ros2_tracing/issues/129)_)
* Ignore zero-variadic-macro-arguments warnings from lttng-ust macros ([#126 ](https://github.com/ros2/ros2_tracing/issues/126)_)
* Remove deprecated TRACEPOINT macros ([#123 ](https://github.com/ros2/ros2_tracing/issues/123)_)
* Fix type for buffer index argument in tracepoint event declaration. ([#117 ](https://github.com/ros2/ros2_tracing/issues/117)_)
* Contributors: Chris Lalancette, Christophe Bedard, Mattis Kieffer, Michael Carroll, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools_launch <https://github.com/ros2/ros2_tracing/tree/kilted/tracetools_launch/CHANGELOG.rst>`__

* Fix or ignore new mypy issues ([#161 ](https://github.com/ros2/ros2_tracing/issues/161)_)
* Improve Python typing annotations ([#152 ](https://github.com/ros2/ros2_tracing/issues/152)_)
* Expose types for tracing tools ([#153 ](https://github.com/ros2/ros2_tracing/issues/153)_)
* Allow enabling syscalls through [`ros2 trace`` or the Trace action (`#137 ](https://github.com/ros2/ros2_tracing/issues/137)_)
* Contributors: Christophe Bedard, Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools_read <https://github.com/ros2/ros2_tracing/tree/kilted/tracetools_read/CHANGELOG.rst>`__

* Improve Python typing annotations ([#152 ](https://github.com/ros2/ros2_tracing/issues/152)_)
* Expose types for tracing tools ([#153 ](https://github.com/ros2/ros2_tracing/issues/153)_)
* Contributors: Christophe Bedard, Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools_test <https://github.com/ros2/ros2_tracing/tree/kilted/tracetools_test/CHANGELOG.rst>`__

* Fix or ignore new mypy issues ([#161 ](https://github.com/ros2/ros2_tracing/issues/161)_)
* Improve Python typing annotations ([#152 ](https://github.com/ros2/ros2_tracing/issues/152)_)
* Expose types for tracing tools ([#153 ](https://github.com/ros2/ros2_tracing/issues/153)_)
* Run relevant test_tracetools tests with all instrumented rmw impls ([#116 ](https://github.com/ros2/ros2_tracing/issues/116)_)
* Contributors: Christophe Bedard, Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools_trace <https://github.com/ros2/ros2_tracing/tree/kilted/tracetools_trace/CHANGELOG.rst>`__

* Improve Python typing annotations ([#152 ](https://github.com/ros2/ros2_tracing/issues/152)_)
* Expose types for tracing tools ([#153 ](https://github.com/ros2/ros2_tracing/issues/153)_)
* Remove unnecessary 'type: ignore' comments in tracetools_trace ([#151 ](https://github.com/ros2/ros2_tracing/issues/151)_)
* Instrument client/service for end-to-end request/response tracking ([#145 ](https://github.com/ros2/ros2_tracing/issues/145)_)
* Allow enabling syscalls through [`ros2 trace`` or the Trace action (`#137 ](https://github.com/ros2/ros2_tracing/issues/137)_)
* Contributors: Christophe Bedard, Michael Carlstrom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `turtlesim <https://github.com/ros/ros_tutorials/tree/kilted/turtlesim/CHANGELOG.rst>`__

* Create turtlesim_msgs ([#169 ](https://github.com/ros/ros_tutorials/issues/169)_)
* Add icon for Jazzy. ([#167 ](https://github.com/ros/ros_tutorials/issues/167)_)
* [teleop_turtle_key] update usage string to match keys captured by keyboard ([#165 ](https://github.com/ros/ros_tutorials/issues/165)_)
* Contributors: Alejandro Hernández Cordero, Marco A. Gutierrez, Mikael Arguedas


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `turtlesim_msgs <https://github.com/ros/ros_tutorials/tree/kilted/turtlesim_msgs/CHANGELOG.rst>`__

* Create turtlesim_msgs ([#169 ](https://github.com/ros/ros_tutorials/issues/169)_)
* Contributors: Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `type_description_interfaces <https://github.com/ros2/rcl_interfaces/tree/kilted/type_description_interfaces/CHANGELOG.rst>`__

* Add missing build_export_depend on rosidl_core_runtime ([#165 ](https://github.com/ros2/rcl_interfaces/issues/165)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `unique_identifier_msgs <https://github.com/ros2/unique_identifier_msgs/tree/kilted/CHANGELOG.rst>`__

* Add missing build_export_depend on rosidl_core_runtime ([#30 ](https://github.com/ros2/unique_identifier_msgs/issues/30)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `urdf <https://github.com/ros2/urdf/tree/kilted/urdf/CHANGELOG.rst>`__

* make linters happy ([#45 ](https://github.com/ros2/urdf/issues/45)_)
* Added documentation with rosdoc2 ([#40 ](https://github.com/ros2/urdf/issues/40)_)
* Added commom linters ([#39 ](https://github.com/ros2/urdf/issues/39)_)
* Use rcutils to log ([#37 ](https://github.com/ros2/urdf/issues/37)_)
* Enable test_robot_model_parser test ([#38 ](https://github.com/ros2/urdf/issues/38)_)
* Contributors: Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `urdf_parser_plugin <https://github.com/ros2/urdf/tree/kilted/urdf_parser_plugin/CHANGELOG.rst>`__

* Added commom linters ([#39 ](https://github.com/ros2/urdf/issues/39)_)
* Contributors: Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `zenoh_cpp_vendor <https://github.com/ros2/rmw_zenoh/tree/kilted/zenoh_cpp_vendor/CHANGELOG.rst>`__

* Bump Zenoh to v1.3.2 and improve e2e reliability with HeartbeatSporadic ([#591 ](https://github.com/ros2/rmw_zenoh/issues/591)_)
* Add quality declaration ([#483 ](https://github.com/ros2/rmw_zenoh/issues/483)_)
* Fix liveliness crash in debug mode ([#544 ](https://github.com/ros2/rmw_zenoh/issues/544)_)
* Bump zenoh-cpp to 2a127bb, zenoh-c to 3540a3c, and zenoh to f735bf5 ([#503 ](https://github.com/ros2/rmw_zenoh/issues/503)_)
* Enable Zenoh UDP transport ([#486 ](https://github.com/ros2/rmw_zenoh/issues/486)_)
* Bump zenoh-c to 261493 and zenoh-cpp to 5dfb68c ([#463 ](https://github.com/ros2/rmw_zenoh/issues/463)_)
* Bump Zenoh to commit id 3bbf6af (1.2.1 + few commits) ([#456 ](https://github.com/ros2/rmw_zenoh/issues/456)_)
* Bump Zenoh to commit id e4ea6f0 (1.2.0 + few commits) ([#446 ](https://github.com/ros2/rmw_zenoh/issues/446)_)
* Bump zenoh-c and zenoh-cpp to 1.1.1 ([#424 ](https://github.com/ros2/rmw_zenoh/issues/424)_)
* Update Zenoh version ([#405 ](https://github.com/ros2/rmw_zenoh/issues/405)_)
* Vendors zenoh-cpp for rmw_zenoh.
* Contributors: Alejandro Hernández Cordero, ChenYing Kuo (CY), Chris Lalancette, Franco Cipollone, Hugal31, Julien Enoch, Luca Cominardi, Yadunund, Yuyuan Yuan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `zenoh_security_tools <https://github.com/ros2/rmw_zenoh/tree/kilted/zenoh_security_tools/CHANGELOG.rst>`__

* Add zenoh_security_tools ([#595 ](https://github.com/ros2/rmw_zenoh/issues/595)_)
* Contributors: yadunund





---
[返回](../index.md)
