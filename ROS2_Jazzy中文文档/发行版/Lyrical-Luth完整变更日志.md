> 原文地址：https://docs.ros.org/en/jazzy/Releases/Lyrical-Luth-Complete-Changelog.html

# ROS 2 Lyrical Luth Complete Changelog

This page is a list of the complete changes in all ROS 2 core packages since the previous release.

   :local:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `action_msgs <https://github.com/ros2/rcl_interfaces/tree/lyrical/action_msgs/CHANGELOG.rst>`__

* Fix cmake deprecation ([#180 ](https://github.com/ros2/rcl_interfaces/issues/180)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `action_tutorials_cpp <https://github.com/ros2/demos/tree/lyrical/action_tutorials/action_tutorials_cpp/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_) demo_nodes_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
* Update action cpp demos to support setting introspection ([#709 ](https://github.com/ros2/demos/issues/709)_) * Update action cpp demos to support setting introspection * Add the missing header file declaration ---------
* Contributors: Barry Xu, Emerson Knapp, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `action_tutorials_py <https://github.com/ros2/demos/tree/lyrical/action_tutorials/action_tutorials_py/CHANGELOG.rst>`__

* action_tutorials_py: add ament_mypy support ([#775 ](https://github.com/ros2/demos//issues/775)_)
* fix setuptools deprecations ([#733 ](https://github.com/ros2/demos/issues/733)_)
* support cancel handler in action_tutorials_py action server. ([#727 ](https://github.com/ros2/demos/issues/727)_)
* Update action python demos to support setting introspection ([#708 ](https://github.com/ros2/demos/issues/708)_) * Update action python demos to support setting introspection * Correct the errors in the document ---------
* Contributors: Barry Xu, Tomoya Fujita, mohit, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_clang_format <https://github.com/ament/ament_lint/tree/lyrical/ament_clang_format/CHANGELOG.rst>`__

* [ament_mypy] Fix config for ament_cmake packages and type entrypoints ([#574 ](https://github.com/ament/ament_lint/issues/574)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_clang_tidy <https://github.com/ament/ament_lint/tree/lyrical/ament_clang_tidy/CHANGELOG.rst>`__

* [ament_mypy] Fix config for ament_cmake packages and type entrypoints ([#574 ](https://github.com/ament/ament_lint/issues/574)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake/CHANGELOG.rst>`__

* Removed deprecated ament_cmake_export_interfaces package ([#581 ](https://github.com/ament/ament_cmake/issues/581)_)
* Contributors: Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_auto <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_auto/CHANGELOG.rst>`__

* Do not error on USE_SCOPED_HEADER_INSTALL_DIR ([#596 ](https://github.com/ament/ament_cmake/issues/596)_)
* Contributors: Tim Clephas


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_clang_format <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_clang_format/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Allow overriding clang-format version via CMake ([#536 ](https://github.com/ament/ament_lint/issues/536)_)
* Contributors: Nathan Wiebe Neufeldt, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_clang_tidy <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_clang_tidy/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_copyright <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_copyright/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_core <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_core/CHANGELOG.rst>`__

* Remove unused AMENT_CMAKE_ENVIRONMENT_GENERATION option ([#354 ](https://github.com/ament/ament_cmake/issues/354)_)
* Address ament_lint_cmake regressions ([#604 ](https://github.com/ament/ament_cmake/issues/604)_)
* Respect find_package(QUIET) in chains from ament_cmake_core ([#603 ](https://github.com/ament/ament_cmake/issues/603)_)
* perf: faster normalize_path implementation using cmake_path ([#586 ](https://github.com/ament/ament_cmake/issues/586)_)
* Contributors: Nathan Boisard, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_cppcheck <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_cppcheck/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_cpplint <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_cpplint/CHANGELOG.rst>`__

* Fixing EXCLUDE consistency ([#481 ](https://github.com/ament/ament_lint/issues/481)_)
* cpplint: update link to upstream cpplint repo ([#538 ](https://github.com/ament/ament_lint/issues/538)_)
* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: Romain Reignier, Tom Moore, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_export_targets <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_export_targets/CHANGELOG.rst>`__

* Address ament_lint_cmake regressions ([#604 ](https://github.com/ament/ament_cmake/issues/604)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_flake8 <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_flake8/CHANGELOG.rst>`__

* Fixing EXCLUDE consistency ([#481 ](https://github.com/ament/ament_lint/issues/481)_)
* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: Tom Moore, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_gen_version_h <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_gen_version_h/CHANGELOG.rst>`__

* Address ament_lint_cmake regressions ([#604 ](https://github.com/ament/ament_cmake/issues/604)_)
* Update CMake requirement ([#589 ](https://github.com/ament/ament_cmake/issues/589)_)
* Removed deprecated function ament_cmake_gen_version_h ([#582 ](https://github.com/ament/ament_cmake/issues/582)_)
* Contributors: Alejandro Hernández Cordero, Scott K Logan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_gmock <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_gmock/CHANGELOG.rst>`__

* Use libgtest-dev and libgmock-dev ([#622 ](https://github.com/ament/ament_cmake//issues/622)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_gtest <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_gtest/CHANGELOG.rst>`__

* Use libgtest-dev and libgmock-dev ([#622 ](https://github.com/ament/ament_cmake//issues/622)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_libraries <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_libraries/CHANGELOG.rst>`__

* Address ament_lint_cmake regressions ([#604 ](https://github.com/ament/ament_cmake/issues/604)_)
* Contributors: Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_lint_cmake <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_lint_cmake/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_mypy <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_mypy/CHANGELOG.rst>`__

* [ament_mypy] Add [`--ament-strict`` flag for more strict type checking. (`#573 ](https://github.com/ament/ament_lint/issues/573)_)
* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_pclint <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_pclint/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_pep257 <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_pep257/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_pycodestyle <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_pycodestyle/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_pyflakes <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_pyflakes/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_python <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_python/CHANGELOG.rst>`__

* feature: allow extending a python package in [`ament_python_install_package`` (`#587 ](https://github.com/ament/ament_cmake//issues/587)_)
* Add missing dependency ([#617 ](https://github.com/ament/ament_cmake/issues/617)_)
* Contributors: Nadav Elkabets, Robert Haschke


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_python_test <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_python_test/CHANGELOG.rst>`__

* feature: allow extending a python package in [`ament_python_install_package`` (`#587 ](https://github.com/ament/ament_cmake//issues/587)_)
* Contributors: Nadav Elkabets


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_ros <https://github.com/ros2/ament_cmake_ros/tree/lyrical/ament_cmake_ros/CHANGELOG.rst>`__

* fix cmake deprecation ([#47 ](https://github.com/ros2/ament_cmake_ros/issues/47)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_ros_core <https://github.com/ros2/ament_cmake_ros/tree/lyrical/ament_cmake_ros_core/CHANGELOG.rst>`__

* Add [`ament_ros_defaults`` target (`#62 ](https://github.com/ros2/ament_cmake_ros/issues/62)_)
* fix cmake deprecation ([#47 ](https://github.com/ros2/ament_cmake_ros/issues/47)_)
* Contributors: Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_target_dependencies <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_target_dependencies/CHANGELOG.rst>`__

* Revert "Revert "Removed deprecated function ament_cmake_target_dependencies (…" ([#614 ](https://github.com/ament/ament_cmake/issues/614)_)
* Revert "Removed deprecated function ament_cmake_target_dependencies" ([#585 ](https://github.com/ament/ament_cmake/issues/585)_)
* Removed deprecated function ament_cmake_target_dependencies ([#583 ](https://github.com/ament/ament_cmake/issues/583)_)
* Contributors: Alejandro Hernández Cordero, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_uncrustify <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_uncrustify/CHANGELOG.rst>`__

* [ament_cmake_uncrustify] Add ament_cmake_uncrustify_LANGUAGE variable ([#384 ](https://github.com/ament/ament_lint/issues/384)_)
* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: Abrar Rahman Protyasha, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_vendor_package <https://github.com/ament/ament_cmake/tree/lyrical/ament_cmake_vendor_package/CHANGELOG.rst>`__

* ament_vendor: Propagate additional variables to ExternalProject ([#593 ](https://github.com/ament/ament_cmake/issues/593)_)
* Contributors: Silvio Traversaro


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_xmllint <https://github.com/ament/ament_lint/tree/lyrical/ament_cmake_xmllint/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_copyright <https://github.com/ament/ament_lint/tree/lyrical/ament_copyright/CHANGELOG.rst>`__

* [ament_mypy] Fix config for ament_cmake packages and type entrypoints ([#574 ](https://github.com/ament/ament_lint/issues/574)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Remove [`importlib_metadata`` (`#564 ](https://github.com/ament/ament_lint/issues/564)_)
* Remove invalid license template. ([#209 ](https://github.com/ament/ament_lint/issues/209)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, Tully Foote, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cppcheck <https://github.com/ament/ament_lint/tree/lyrical/ament_cppcheck/CHANGELOG.rst>`__

* [ament_mypy] Fix config for ament_cmake packages and type entrypoints ([#574 ](https://github.com/ament/ament_lint/issues/574)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cpplint <https://github.com/ament/ament_lint/tree/lyrical/ament_cpplint/CHANGELOG.rst>`__

* [ament_mypy] Fix config for ament_cmake packages and type entrypoints ([#574 ](https://github.com/ament/ament_lint/issues/574)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* cpplint: update link to upstream cpplint repo ([#538 ](https://github.com/ament/ament_lint/issues/538)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, Romain Reignier, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_flake8 <https://github.com/ament/ament_lint/tree/lyrical/ament_flake8/CHANGELOG.rst>`__

* [ament_mypy] Add [`--ament-strict`` flag for more strict type checking. (`#573 ](https://github.com/ament/ament_lint/issues/573)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Drop dependency on python3-flake8-docstrings ([#513 ](https://github.com/ament/ament_lint/issues/513)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, Scott K Logan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_index_cpp <https://github.com/ament/ament_index/tree/lyrical/ament_index_cpp/CHANGELOG.rst>`__

* Cleanups ([#114 ](https://github.com/ament/ament_index/issues/114)_)
* Use get_package_share_path just as python ([#112 ](https://github.com/ament/ament_index//issues/112)_)
* Add autogenerated version header ([#105 ](https://github.com/ament/ament_index/issues/105)_)
* Extend API to use std::filesystem ([#104 ](https://github.com/ament/ament_index/issues/104)_)
* Fix CMake deprecation ([#102 ](https://github.com/ament/ament_index/issues/102)_)
* Contributors: Alejandro Hernández Cordero, Eric Lujan, Tim Clephas, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_index_python <https://github.com/ament/ament_index/tree/lyrical/ament_index_python/CHANGELOG.rst>`__

* Cleanups ament_index_python ([#115 ](https://github.com/ament/ament_index/issues/115)_)
* fix setuptools deprecations ([#101 ](https://github.com/ament/ament_index/issues/101)_)
* Contributors: Alejandro Hernández Cordero, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_lint <https://github.com/ament/ament_lint/tree/lyrical/ament_lint/CHANGELOG.rst>`__

* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_lint_auto <https://github.com/ament/ament_lint/tree/lyrical/ament_lint_auto/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_lint_cmake <https://github.com/ament/ament_lint/tree/lyrical/ament_lint_cmake/CHANGELOG.rst>`__

* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_lint_common <https://github.com/ament/ament_lint/tree/lyrical/ament_lint_common/CHANGELOG.rst>`__

* Fix cmake deprecation ([#539 ](https://github.com/ament/ament_lint/issues/539)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_mypy <https://github.com/ament/ament_lint/tree/lyrical/ament_mypy/CHANGELOG.rst>`__

* Allow unused ignores ([#575 ](https://github.com/ament/ament_lint/issues/575)_)
* [ament_mypy] Fix config for ament_cmake packages and type entrypoints ([#574 ](https://github.com/ament/ament_lint/issues/574)_)
* [ament_mypy] Add [`--ament-strict`` flag for more strict type checking. (`#573 ](https://github.com/ament/ament_lint/issues/573)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_package <https://github.com/ament/ament_package/tree/lyrical/CHANGELOG.rst>`__

* feat: add support for fish ([#164 ](https://github.com/ament/ament_package/issues/164)_)
* Fix flake8 ([#163 ](https://github.com/ament/ament_package/issues/163)_)
* Remove unneeded deps ([#161 ](https://github.com/ament/ament_package/issues/161)_)
* fix setuptools deprecations ([#156 ](https://github.com/ament/ament_package/issues/156)_)
* Contributors: Michael Carlstrom, SPeak, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_pclint <https://github.com/ament/ament_lint/tree/lyrical/ament_pclint/CHANGELOG.rst>`__

* [ament_mypy] Fix config for ament_cmake packages and type entrypoints ([#574 ](https://github.com/ament/ament_lint/issues/574)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* clean setup.py ([#552 ](https://github.com/ament/ament_lint/issues/552)_)
* fix setuptools deprecation ([#551 ](https://github.com/ament/ament_lint/issues/551)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_pep257 <https://github.com/ament/ament_lint/tree/lyrical/ament_pep257/CHANGELOG.rst>`__

* Skip pydocstyle tests if it can't be imported ([#579 ](https://github.com/ament/ament_lint/issues/579)_)
* [ament_mypy] Fix config for ament_cmake packages and type entrypoints ([#574 ](https://github.com/ament/ament_lint/issues/574)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, Scott K Logan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_pycodestyle <https://github.com/ament/ament_lint/tree/lyrical/ament_pycodestyle/CHANGELOG.rst>`__

* [ament_mypy] Fix config for ament_cmake packages and type entrypoints ([#574 ](https://github.com/ament/ament_lint/issues/574)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_pyflakes <https://github.com/ament/ament_lint/tree/lyrical/ament_pyflakes/CHANGELOG.rst>`__

* [ament_mypy] Fix config for ament_cmake packages and type entrypoints ([#574 ](https://github.com/ament/ament_lint/issues/574)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_uncrustify <https://github.com/ament/ament_lint/tree/lyrical/ament_uncrustify/CHANGELOG.rst>`__

* [ament_mypy] Fix config for ament_cmake packages and type entrypoints ([#574 ](https://github.com/ament/ament_lint/issues/574)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Revert "Removed uncrustify_vendor ([#556 ](https://github.com/ament/ament_lint/issues/556)_)" ([#561 ](https://github.com/ament/ament_lint/issues/561)_)
* Removed uncrustify_vendor ([#556 ](https://github.com/ament/ament_lint/issues/556)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Alejandro Hernández Cordero, Jochen Sprickerhof, Michael Carlstrom, Michael Orlov, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_xmllint <https://github.com/ament/ament_lint/tree/lyrical/ament_xmllint/CHANGELOG.rst>`__

* [ament_mypy] Add [`--ament-strict`` flag for more strict type checking. (`#573 ](https://github.com/ament/ament_lint/issues/573)_)
* xmllint: fetch external schemas via Python ([#570 ](https://github.com/ament/ament_lint/issues/570)_)
* Drop setuptools from install_requires ([#566 ](https://github.com/ament/ament_lint/issues/566)_)
* Export typing information for ament linters ([#553 ](https://github.com/ament/ament_lint/issues/553)_)
* fix setuptools deprecations ([#547 ](https://github.com/ament/ament_lint/issues/547)_)
* Contributors: Jochen Sprickerhof, Michael Carlstrom, Michael Carroll, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `builtin_interfaces <https://github.com/ros2/rcl_interfaces/tree/lyrical/builtin_interfaces/CHANGELOG.rst>`__

* Fix cmake deprecation ([#180 ](https://github.com/ros2/rcl_interfaces/issues/180)_)
* Add info to duration message and time message comments ([#176 ](https://github.com/ros2/rcl_interfaces/issues/176)_)
* Contributors: Jimmy McElwain, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `camera_calibration_parsers <https://github.com/ros-perception/image_common/tree/lyrical/camera_calibration_parsers/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#396 ](https://github.com/ros-perception/image_common/issues/396)_)
* Delete camera_calibration_parsers/setup.py ([#393 ](https://github.com/ros-perception/image_common/issues/393)_)
* Update BSD licenses to SPDX identifier ([#389 ](https://github.com/ros-perception/image_common/issues/389)_) Co-authored-by: Alejandro Hernandez Cordero <ahcorde@gmail.com>
* Fix cmake deprecation ([#367 ](https://github.com/ros-perception/image_common/issues/367)_)
* Use target_link_libraries instead of ament_target_dependencies ([#345 ](https://github.com/ros-perception/image_common/issues/345)_)
* Contributors: Emerson Knapp, Garrett Brown, Michael Carlstrom, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `camera_info_manager <https://github.com/ros-perception/image_common/tree/lyrical/camera_info_manager/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#396 ](https://github.com/ros-perception/image_common/issues/396)_)
* Added camera info manager unit test ([#358 ](https://github.com/ros-perception/image_common/issues/358)_)
* Use get_package_share_path ([#391 ](https://github.com/ros-perception/image_common/issues/391)_)
* Update BSD licenses to SPDX identifier ([#389 ](https://github.com/ros-perception/image_common/issues/389)_) Co-authored-by: Alejandro Hernandez Cordero <ahcorde@gmail.com>
* Updated deprecated ament_index_cpp API ([#388 ](https://github.com/ros-perception/image_common/issues/388)_)
* Fix compilation error with clang ([#372 ](https://github.com/ros-perception/image_common/issues/372)_)
* Support lifecycle node - NodeInterfaces ([#352 ](https://github.com/ros-perception/image_common/issues/352)_)
* Deprecated rmw_qos_profile_t in favour of rclcpp::QoS ([#364 ](https://github.com/ros-perception/image_common/issues/364)_)
* Fix cmake deprecation ([#367 ](https://github.com/ros-perception/image_common/issues/367)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Garrett Brown, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `camera_info_manager_py <https://github.com/ros-perception/image_common/tree/lyrical/camera_info_manager_py/CHANGELOG.rst>`__

* Update BSD licenses to SPDX identifier ([#389 ](https://github.com/ros-perception/image_common/issues/389)_) Co-authored-by: Alejandro Hernandez Cordero <ahcorde@gmail.com>
* Cleanup mislabeled BSD license ([#382 ](https://github.com/ros-perception/image_common/issues/382)_)
* fix setuptools deprecation ([#366 ](https://github.com/ros-perception/image_common/issues/366)_)
* Fix CameraInfo distortion coefficients and logger ([#360 ](https://github.com/ros-perception/image_common/issues/360)_)
* Contributors: Alejandro Hernández Cordero, Garrett Brown, Rick-v-E, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `class_loader <https://github.com/ros/class_loader/tree/lyrical/CHANGELOG.rst>`__

* Fix compiler error with clang ([#227 ](https://github.com/ros/class_loader/issues/227)_)
* Remove ament_cmake_ros dependency ([#226 ](https://github.com/ros/class_loader/issues/226)_) The dependent ament_cmake_ros package transitively pulls in RMW-layer packages which is unnecessarily heavy to class_loader that is supposed to be an independent plugin loading library. This commit removes the ament_cmake_ros dependency and replaces with a plain ament_cmake with an explicit SHARED library type to keep the dependency minimal.
* Improvements ([#225 ](https://github.com/ros/class_loader/issues/225)_)
* Clean up tests ([#224 ](https://github.com/ros/class_loader/issues/224)_)
* Add support for passing arguments to constructors ([#223 ](https://github.com/ros/class_loader//issues/223)_)
* Thread and Address Sanitizer CI ([#198 ](https://github.com/ros/class_loader/issues/198)_)
* Update cmake requirement
* Remove CODEOWNERS and mirror-rolling-to-main workflow ([#215 ](https://github.com/ros/class_loader/issues/215)_)
* Contributors: Alejandro Hernández Cordero, CY Chen, Tyler Weaver, mosfet80, pum1k


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `common_interfaces <https://github.com/ros2/common_interfaces/tree/lyrical/common_interfaces/CHANGELOG.rst>`__

* Fix CMAKE deprecation ([#288 ](https://github.com/ros2/common_interfaces/issues/288)_)
* Removed deprecated actionlib_msgs ([#280 ](https://github.com/ros2/common_interfaces/issues/280)_)
* Contributors: Alejandro Hernández Cordero, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `composition <https://github.com/ros2/demos/tree/lyrical/composition/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* Add tests isolation in test_dlopen_composition.py.in and test_linktime_composition.py.in ([#764 ](https://github.com/ros2/demos//issues/764)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* Log message for linktime composition on Windows ([#640 ](https://github.com/ros2/demos/issues/640)_)
* correct name of shared libraries and their location ([#722 ](https://github.com/ros2/demos/issues/722)_) ([#726 ](https://github.com/ros2/demos/issues/726)_)
* Use EnableRmwIsolation in launch tests ([#724 ](https://github.com/ros2/demos/issues/724)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Julien Enoch, Lucas Wendland, Scott K Logan, Shane Loretz, mergify[bot], mosfet80, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `composition_interfaces <https://github.com/ros2/rcl_interfaces/tree/lyrical/composition_interfaces/CHANGELOG.rst>`__

* Fix cmake deprecation ([#180 ](https://github.com/ros2/rcl_interfaces/issues/180)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `console_bridge_vendor <https://github.com/ros2/console_bridge_vendor/tree/lyrical/CHANGELOG.rst>`__

* Update CMake version here and console_bridge ([#44 ](https://github.com/ros2/console_bridge_vendor/issues/44)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#42 ](https://github.com/ros2/console_bridge_vendor/issues/42)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `demo_nodes_cpp <https://github.com/ros2/demos/tree/lyrical/demo_nodes_cpp/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* add child logger under parent node, with different log levels. ([#772 ](https://github.com/ros2/demos//issues/772)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* Update subscription callback signatures ([#754 ](https://github.com/ros2/demos/issues/754)_)
* Use EnableRmwIsolation in launch tests ([#724 ](https://github.com/ros2/demos/issues/724)_)
* fix typo in docs demo_nodes_cpp ([#715 ](https://github.com/ros2/demos/issues/715)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Khaled Gabr, Lucas Wendland, Scott K Logan, Tomoya Fujita, mini-1235, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `demo_nodes_cpp_native <https://github.com/ros2/demos/tree/lyrical/demo_nodes_cpp_native/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* Removed outdated TODO ([#723 ](https://github.com/ros2/demos/issues/723)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas Wendland, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `demo_nodes_py <https://github.com/ros2/demos/tree/lyrical/demo_nodes_py/CHANGELOG.rst>`__

* add child logger under parent node, with different log levels. ([#772 ](https://github.com/ros2/demos//issues/772)_)
* Fix deprecated RcutilsLogger::warn() usage in LoggerServiceNode ([#773 ](https://github.com/ros2/demos//issues/773)_)
* Ignore A005 ([#771 ](https://github.com/ros2/demos//issues/771)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* fix setuptools deprecations ([#733 ](https://github.com/ros2/demos/issues/733)_)
* Revert "Revert "fix loading parameter behavior from yaml file. ([#656 ](https://github.com/ros2/demos/issues/656)_)" ([#660 ](https://github.com/ros2/demos/issues/660)_)" ([#661 ](https://github.com/ros2/demos/issues/661)_)
* Contributors: Barry Xu, Lucas Wendland, Michael Carlstrom, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `diagnostic_msgs <https://github.com/ros2/common_interfaces/tree/lyrical/diagnostic_msgs/CHANGELOG.rst>`__

* Fix CMAKE deprecation ([#288 ](https://github.com/ros2/common_interfaces/issues/288)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `domain_coordinator <https://github.com/ros2/ament_cmake_ros/tree/lyrical/domain_coordinator/CHANGELOG.rst>`__

* fix setuptools deprecations ([#49 ](https://github.com/ros2/ament_cmake_ros/issues/49)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `dummy_map_server <https://github.com/ros2/demos/tree/lyrical/dummy_robot/dummy_map_server/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* get rid of deprecated rclcpp::spin_some(). ([#734 ](https://github.com/ros2/demos/issues/734)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_) demo_nodes_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `dummy_robot_bringup <https://github.com/ros2/demos/tree/lyrical/dummy_robot/dummy_robot_bringup/CHANGELOG.rst>`__

* Fixed launch file ([#759 ](https://github.com/ros2/demos/issues/759)_)
* Added README.md for dummy_robot_bringup. ([#574 ](https://github.com/ros2/demos/issues/574)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_) demo_nodes_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
* Contributors: Alejandro Hernández Cordero, Gary Bey, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `dummy_sensors <https://github.com/ros2/demos/tree/lyrical/dummy_robot/dummy_sensors/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* get rid of deprecated rclcpp::spin_some(). ([#734 ](https://github.com/ros2/demos/issues/734)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_) demo_nodes_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `eigen3_cmake_module <https://github.com/ros2/eigen3_cmake_module/tree/lyrical/CHANGELOG.rst>`__

* fix cmake deprecation ([#10 ](https://github.com/ros2/eigen3_cmake_module/issues/10)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#8 ](https://github.com/ros2/eigen3_cmake_module/issues/8)_)
* Contributors: Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `example_interfaces <https://github.com/ros2/example_interfaces/tree/lyrical/CHANGELOG.rst>`__

* fix cmake deprecation ([#23 ](https://github.com/ros2/example_interfaces/issues/23)_)
* Remove .github/ISSUE_TEMPLATE.md (old version of templates) ([#21 ](https://github.com/ros2/example_interfaces/issues/21)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#19 ](https://github.com/ros2/example_interfaces/issues/19)_)
* Contributors: Chris Lalancette, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_async_client <https://github.com/ros2/examples/tree/lyrical/rclcpp/services/async_client/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#444 ](https://github.com/ros2/examples/issues/444)_)
* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Emerson Knapp, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_cbg_executor <https://github.com/ros2/examples/tree/lyrical/rclcpp/executors/cbg_executor/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#444 ](https://github.com/ros2/examples/issues/444)_)
* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Emerson Knapp, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_action_client <https://github.com/ros2/examples/tree/lyrical/rclcpp/actions/minimal_action_client/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#444 ](https://github.com/ros2/examples/issues/444)_)
* get rid of deprecated rclcpp::spin_some(). ([#422 ](https://github.com/ros2/examples//issues/422)_)
* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_action_server <https://github.com/ros2/examples/tree/lyrical/rclcpp/actions/minimal_action_server/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#444 ](https://github.com/ros2/examples/issues/444)_)
* Add rclcpp single goal action server example ([#429 ](https://github.com/ros2/examples/issues/429)_)
* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Emerson Knapp, Shane Loretz, Taiga Arai, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_client <https://github.com/ros2/examples/tree/lyrical/rclcpp/services/minimal_client/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#444 ](https://github.com/ros2/examples/issues/444)_)
* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Emerson Knapp, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_composition <https://github.com/ros2/examples/tree/lyrical/rclcpp/composition/minimal_composition/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#444 ](https://github.com/ros2/examples/issues/444)_)
* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Emerson Knapp, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_publisher <https://github.com/ros2/examples/tree/lyrical/rclcpp/topics/minimal_publisher/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#444 ](https://github.com/ros2/examples/issues/444)_)
* Improve minimal_publisher README with clearer structure and usage guidance ([#434 ](https://github.com/ros2/examples/issues/434)_)
* get rid of deprecated rclcpp::spin_some(). ([#422 ](https://github.com/ros2/examples//issues/422)_)
* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* wait 5 secs until all subscriptions acknowledge the messages. ([#414 ](https://github.com/ros2/examples/issues/414)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Emerson Knapp, Shane Loretz, Tomoya Fujita, Yadnyeshwar Amol Sakhare, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_service <https://github.com/ros2/examples/tree/lyrical/rclcpp/services/minimal_service/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#444 ](https://github.com/ros2/examples/issues/444)_)
* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Emerson Knapp, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_subscriber <https://github.com/ros2/examples/tree/lyrical/rclcpp/topics/minimal_subscriber/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#444 ](https://github.com/ros2/examples/issues/444)_)
* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Emerson Knapp, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_timer <https://github.com/ros2/examples/tree/lyrical/rclcpp/timers/minimal_timer/CHANGELOG.rst>`__

* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_multithreaded_executor <https://github.com/ros2/examples/tree/lyrical/rclcpp/executors/multithreaded_executor/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#444 ](https://github.com/ros2/examples/issues/444)_)
* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* Improve readibility of reported thread ids in the multithreaded executor example ([#415 ](https://github.com/ros2/examples/issues/415)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Emerson Knapp, José Faria, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_wait_set <https://github.com/ros2/examples/tree/lyrical/rclcpp/wait_set/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#444 ](https://github.com/ros2/examples/issues/444)_)
* Fix CMAKE deprecation ([#419 ](https://github.com/ros2/examples/issues/419)_)
* Use target_link_libraries instead of ament_target_dependencies ([#404 ](https://github.com/ros2/examples/issues/404)_)
* Contributors: Emerson Knapp, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_executors <https://github.com/ros2/examples/tree/lyrical/rclpy/executors/CHANGELOG.rst>`__

* Fix setuptools deprecations ([#421 ](https://github.com/ros2/examples/issues/421)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_guard_conditions <https://github.com/ros2/examples/tree/lyrical/rclpy/guard_conditions/CHANGELOG.rst>`__

* Fix setuptools deprecations ([#421 ](https://github.com/ros2/examples/issues/421)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_action_client <https://github.com/ros2/examples/tree/lyrical/rclpy/actions/minimal_action_client/CHANGELOG.rst>`__

* Fix setuptools deprecations ([#421 ](https://github.com/ros2/examples/issues/421)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_action_server <https://github.com/ros2/examples/tree/lyrical/rclpy/actions/minimal_action_server/CHANGELOG.rst>`__

* Fix setuptools deprecations ([#421 ](https://github.com/ros2/examples/issues/421)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_client <https://github.com/ros2/examples/tree/lyrical/rclpy/services/minimal_client/CHANGELOG.rst>`__

* flake8 fixes ([#445 ](https://github.com/ros2/examples/issues/445)_)
* Fix setuptools deprecations ([#421 ](https://github.com/ros2/examples/issues/421)_)
* Contributors: Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_publisher <https://github.com/ros2/examples/tree/lyrical/rclpy/topics/minimal_publisher/CHANGELOG.rst>`__

* Fix setuptools deprecations ([#421 ](https://github.com/ros2/examples/issues/421)_)
* Address flake8 errors for examples_rclpy_minimal_publisher ([#410 ](https://github.com/ros2/examples/issues/410)_)
* Add publisher_member_function_with_wait_for_all_acked.py ([#407 ](https://github.com/ros2/examples/issues/407)_)
* Contributors: Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_service <https://github.com/ros2/examples/tree/lyrical/rclpy/services/minimal_service/CHANGELOG.rst>`__

* flake8 fixes ([#445 ](https://github.com/ros2/examples/issues/445)_)
* Fix setuptools deprecations ([#421 ](https://github.com/ros2/examples/issues/421)_)
* Contributors: Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_subscriber <https://github.com/ros2/examples/tree/lyrical/rclpy/topics/minimal_subscriber/CHANGELOG.rst>`__

* flake8 fixes ([#445 ](https://github.com/ros2/examples/issues/445)_)
* Fix setuptools deprecations ([#421 ](https://github.com/ros2/examples/issues/421)_)
* Contributors: Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_pointcloud_publisher <https://github.com/ros2/examples/tree/lyrical/rclpy/topics/pointcloud_publisher/CHANGELOG.rst>`__

* Fix setuptools deprecations ([#421 ](https://github.com/ros2/examples/issues/421)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_tf2_py <https://github.com/ros2/geometry2/tree/lyrical/examples_tf2_py/CHANGELOG.rst>`__

* fix typos ([#921 ](https://github.com/ros2/geometry2/issues/921)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Fix Setuptools deprecations ([#809 ](https://github.com/ros2/geometry2/issues/809)_)
* Contributors: Auguste Lalande, R Kent James, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `foonathan_memory_vendor <https://github.com/eProsima/foonathan_memory_vendor/tree/master/CHANGELOG.rst>`__

* Change upstream to fix build with clang (#80)
* Change upstream to eProsima fork to avoid patch command (#80)
* Update upstream to release 0.7-4 (#75)
* Remove installer CMake patches (#75)
* Improve mechanism to find an installation of foonathan_memory (#67)
* Fix ament_lint_cmake errors (#68)
* Add FORCE_BUILD option to cmake (#69)
* Shorten new option description (#70)


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `geometry2 <https://github.com/ros2/geometry2/tree/lyrical/geometry2/CHANGELOG.rst>`__

* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `geometry_msgs <https://github.com/ros2/common_interfaces/tree/lyrical/geometry_msgs/CHANGELOG.rst>`__

* Clarify [`Inertia.msg`` expresses inertia about the center of mass (`#313 ](https://github.com/ros2/common_interfaces/issues/313)_)
* Fix CMAKE deprecation ([#288 ](https://github.com/ros2/common_interfaces/issues/288)_)
* Removed deprecated geometry_msgs/Pose2d ([#283 ](https://github.com/ros2/common_interfaces/issues/283)_)
* Contributors: Alejandro Hernández Cordero, Andrew Symington, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `gmock_vendor <https://github.com/ament/googletest/tree/lyrical/googlemock/CHANGELOG.rst>`__

* Deprecate gtest_vendor and gmock_vendor ([#41 ](https://github.com/ament/googletest/issues/41)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `gtest_vendor <https://github.com/ament/googletest/tree/lyrical/googletest/CHANGELOG.rst>`__

* Deprecate gtest_vendor and gmock_vendor ([#41 ](https://github.com/ament/googletest/issues/41)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `gz_cmake_vendor <https://github.com/gazebo-release/gz_cmake_vendor/tree/lyrical/CHANGELOG.rst>`__

* Bump version to 5.1.0 ([#24 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/24)_)
* Merge pull request [#23 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/23)_ Bump version to 5.0.2  ---------
* Bump version to 5.0.1 ([#20 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/20)_)
* Bump version to 5.0.0 ([#19 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/19)_)
* Jetty support: bump to 5.0.0, fix package names ([#16 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/16)_) * Jetty support: bump to 5.0.0, fix package names Major version numbers have been removed from package names in Gazebo Jetty, so extra cmake config files are no longer needed. * Add option VENDOR_FROM_LIB_VCS_REF This allows vendoring from a specified vcs ref instead of the hard-coded tag. When this option is set to true, a branch, tag, or commit can be specified in the LIB_VCS_REF variable. If LIB_VCS_REF is unspecified, vendoring will use main. * remove unused cmake config template * use lowercase to fix linter complaint * 5.0.0~pre1 ---------
* Bump version to 4.2.0 ([#15 ](https://github.com/gazebo-release/gz_cmake_vendor/issues/15)_)
* Contributors: Addisu Z. Taddese, Jose Luis Rivero, Steve Peters


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `gz_math_vendor <https://github.com/gazebo-release/gz_math_vendor/tree/lyrical/CHANGELOG.rst>`__

* Bump version to 9.1.0 ([#20 ](https://github.com/gazebo-release/gz_math_vendor/issues/20)_)
* Bump version to 9.0.0 ([#17 ](https://github.com/gazebo-release/gz_math_vendor/issues/17)_)
* Set PYTHONPATH for Jetty packages ([#14 ](https://github.com/gazebo-release/gz_math_vendor/issues/14)_) * Set PYTHONPATH for unversioned packages * Bump to 9.0.0-pre2 * Set PYTHONPATH in separate dsv file ---------
* Bump to 9.0.0-pre2 ([#16 ](https://github.com/gazebo-release/gz_math_vendor/issues/16)_)
* Jetty support: bump to 9.0.0, fix package names ([#12 ](https://github.com/gazebo-release/gz_math_vendor/issues/12)_) * Jetty support: bump to 9.0.0, fix package names Major version numbers have been removed from package names in Gazebo Jetty, so extra cmake config files are no longer needed. * Add option VENDOR_FROM_LIB_VCS_REF This allows vendoring from a specified vcs ref instead of the hard-coded tag. When this option is set to true, a branch, tag, or commit can be specified in the LIB_VCS_REF variable. If LIB_VCS_REF is unspecified, vendoring will use main. * remove unused cmake config file * use lowercase to fix linter complaint * build python bindings * 9.0.0~pre1 ---------
* Bump version to 8.2.0 ([#11 ](https://github.com/gazebo-release/gz_math_vendor/issues/11)_)
* Contributors: Addisu Z. Taddese, Ian Chen, Jose Luis Rivero, Steve Peters


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `gz_utils_vendor <https://github.com/gazebo-release/gz_utils_vendor/tree/lyrical/CHANGELOG.rst>`__

* Bump version to 4.0.0 ([#12 ](https://github.com/gazebo-release/gz_utils_vendor/issues/12)_)
* Add dsv for PYTHONPATH for Jetty packages ([#13 ](https://github.com/gazebo-release/gz_utils_vendor/issues/13)_)
* Jetty support: bump to 4.0.0, fix package names ([#11 ](https://github.com/gazebo-release/gz_utils_vendor/issues/11)_) * Jetty support: bump to 4.0.0, fix package names Major version numbers have been removed from package names in Gazebo Jetty, so extra cmake config files are no longer needed. * Add option VENDOR_FROM_LIB_VCS_REF This allows vendoring from a specified vcs ref instead of the hard-coded tag. When this option is set to true, a branch, tag, or commit can be specified in the LIB_VCS_REF variable. If LIB_VCS_REF is unspecified, vendoring will use main. * remove unused cmake config file * use lowercase to fix linter complaint * Add dependency on cli11 * 4.0.0~pre1 * Use vendored version of CLI11 --------- Co-authored-by: Addisu Z. Taddese <addisu@openrobotics.org>
* Contributors: Addisu Z. Taddese, Steve Peters


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `image_common <https://github.com/ros-perception/image_common/tree/lyrical/image_common/CHANGELOG.rst>`__

* Update BSD licenses to SPDX identifier ([#389 ](https://github.com/ros-perception/image_common/issues/389)_) Co-authored-by: Alejandro Hernandez Cordero <ahcorde@gmail.com>
* Fix cmake deprecation ([#367 ](https://github.com/ros-perception/image_common/issues/367)_)
* Contributors: Garrett Brown, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `image_tools <https://github.com/ros2/demos/tree/lyrical/image_tools/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* Don't use [`libopencv-dev`` for exec (`#760 ](https://github.com/ros2/demos//issues/760)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* Use EnableRmwIsolation in launch tests ([#724 ](https://github.com/ros2/demos/issues/724)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Lint image_tools/CMakeLists.txt ([#712 ](https://github.com/ros2/demos/issues/712)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas Wendland, Michael Carlstrom, Scott K Logan, mosfet80, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `image_transport <https://github.com/ros-perception/image_common/tree/lyrical/image_transport/CHANGELOG.rst>`__

* Removed clang warning ([#399 ](https://github.com/ros-perception/image_common/issues/399)_)
* Include message type ([#394 ](https://github.com/ros-perception/image_common/issues/394)_)
* Use new ROSIDL aggregate CMake target ([#396 ](https://github.com/ros-perception/image_common/issues/396)_)
* Update BSD licenses to SPDX identifier ([#389 ](https://github.com/ros-perception/image_common/issues/389)_) Co-authored-by: Alejandro Hernandez Cordero <ahcorde@gmail.com>
* properly shut down rclcpp after all tests complete. ([#384 ](https://github.com/ros-perception/image_common/issues/384)_)
* Fix QoS override tests ([#376 ](https://github.com/ros-perception/image_common/issues/376)_)
* Fix rclcpp_lifecycle dependency ([#373 ](https://github.com/ros-perception/image_common/issues/373)_)
* Fix compilation error with clang ([#372 ](https://github.com/ros-perception/image_common/issues/372)_)
* Support lifecycle node - NodeInterfaces ([#352 ](https://github.com/ros-perception/image_common/issues/352)_)
* Fixed clang build ([#371 ](https://github.com/ros-perception/image_common/issues/371)_)
* fixed build ([#369 ](https://github.com/ros-perception/image_common/issues/369)_)
* Deprecated rmw_qos_profile_t in favour of rclcpp::QoS ([#364 ](https://github.com/ros-perception/image_common/issues/364)_)
* Removed deprecated code ([#356 ](https://github.com/ros-perception/image_common/issues/356)_)
* Fix cmake deprecation ([#367 ](https://github.com/ros-perception/image_common/issues/367)_)
* Fix topic resolution for plugins ([#365 ](https://github.com/ros-perception/image_common/issues/365)_)
* Remove windows warnings ([#350 ](https://github.com/ros-perception/image_common/issues/350)_)
* Add [`rclcpp::shutdown`` (`#347 ](https://github.com/ros-perception/image_common/issues/347)_)
* Use target_link_libraries instead of ament_target_dependencies ([#345 ](https://github.com/ros-perception/image_common/issues/345)_)
* Contributors: Alejandro Hernández Cordero, Alex Tyshka, Emerson Knapp, Garrett Brown, Shane Loretz, Tomoya Fujita, Yuyuan Yuan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `image_transport_py <https://github.com/ros-perception/image_common/tree/lyrical/image_transport_py/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#396 ](https://github.com/ros-perception/image_common/issues/396)_)
* Update BSD licenses to SPDX identifier ([#389 ](https://github.com/ros-perception/image_common/issues/389)_) Co-authored-by: Alejandro Hernandez Cordero <ahcorde@gmail.com>
* Use pybind11 from deb or pixi ([#374 ](https://github.com/ros-perception/image_common/issues/374)_)
* Support lifecycle node - NodeInterfaces ([#352 ](https://github.com/ros-perception/image_common/issues/352)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Garrett Brown


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `interactive_markers <https://github.com/ros-visualization/interactive_markers/tree/lyrical/CHANGELOG.rst>`__

* fix: Fix compilation on MSVC 2022 ([#120 ](https://github.com/ros-visualization/interactive_markers/issues/120)_)
* Use new ROSIDL aggregate CMake target ([#119 ](https://github.com/ros-visualization/interactive_markers/issues/119)_)
* Cleanup mislabeled BSD license ([#118 ](https://github.com/ros-visualization/interactive_markers/issues/118)_)
* Explicit Time comparissons ([#105 ](https://github.com/ros-visualization/interactive_markers/issues/105)_)
* fix cmake deprecation ([#113 ](https://github.com/ros-visualization/interactive_markers/issues/113)_)
* Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Emerson Knapp, Janosch Machowinski, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `intra_process_demo <https://github.com/ros2/demos/tree/lyrical/intra_process_demo/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* Don't use [`libopencv-dev`` for exec (`#760 ](https://github.com/ros2/demos//issues/760)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* fixup image_pipeline_demo ([#755 ](https://github.com/ros2/demos/issues/755)_)
* Use EnableRmwIsolation in launch tests ([#724 ](https://github.com/ros2/demos/issues/724)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas Wendland, Michael Carlstrom, Scott K Logan, William Woodall, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `kdl_parser <https://github.com/ros/kdl_parser/tree/lyrical/CHANGELOG.rst>`__

* Removed kdl vendor dependency ([#90 ](https://github.com/ros/kdl_parser//issues/90)_)
* Cmake requirement ([#88 ](https://github.com/ros/kdl_parser/issues/88)_)
* Remove kdl_parser_py. ([#89 ](https://github.com/ros/kdl_parser/issues/89)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `keyboard_handler <https://github.com/ros-tooling/keyboard_handler/tree/lyrical/keyboard_handler/CHANGELOG.rst>`__

* fix cmake deprecation ([#55 ](https://github.com/ros-tooling/keyboard_handler/issues/55)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `laser_geometry <https://github.com/ros-perception/laser_geometry/tree/lyrical/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#115 ](https://github.com/ros-perception/laser_geometry/issues/115)_)
* Use seconds in sensor_msgs::msg::LaserScan msg inside the test ([#107 ](https://github.com/ros-perception/laser_geometry/issues/107)_)
* Use constructor of rclcpp::Time instead of conversion. ([#91 ](https://github.com/ros-perception/laser_geometry/issues/91)_)
* fix cmake deprecation ([#105 ](https://github.com/ros-perception/laser_geometry/issues/105)_)
* Remove hard-coded eigen3 header path for linux hosts ([#95 ](https://github.com/ros-perception/laser_geometry/issues/95)_) Co-authored-by: Alejandro Hernandez Cordero <ahcorde@gmail.com>
* Contributors: AiVerisimilitude, Alejandro Hernández Cordero, Emerson Knapp, Lukas Schäper, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch <https://github.com/ros2/launch/tree/lyrical/launch/CHANGELOG.rst>`__

* Correct typos ([#961 ](https://github.com/ros2/launch/issues/961)_)
* hotfix ([#950 ](https://github.com/ros2/launch/issues/950)_)
* Declare Boolean Launch Argument ([#944 ](https://github.com/ros2/launch/issues/944)_)
* Support frontends for PathJoinSubstitution ([#943 ](https://github.com/ros2/launch/issues/943)_)
* test python substitution with submodules ([#688 ](https://github.com/ros2/launch/issues/688)_)
* Scope launch file dir/path locals to included launch file ([#862 ](https://github.com/ros2/launch/issues/862)_)
* Capture the environment variables in TimerAction ([#728 ](https://github.com/ros2/launch/issues/728)_)
* Remove importlib metadata ([#932 ](https://github.com/ros2/launch/issues/932)_)
* Fix intersphinx_mapping format ([#921 ](https://github.com/ros2/launch/issues/921)_)
* Make the directory-finding substitutions into a PathSubstitution for / operator ([#914 ](https://github.com/ros2/launch//issues/914)_)
* Expose StringJoinSubstitution to frontend ([#857 ](https://github.com/ros2/launch//issues/857)_)
* Shared logic for substitutions ([#769 ](https://github.com/ros2/launch/issues/769)_)
* Use yaml types ([#781 ](https://github.com/ros2/launch/issues/781)_)
* Switch osrf_pycommon dependency to system package ([#817 ](https://github.com/ros2/launch/issues/817)_)
* Fix all/any in xml and yaml launch files ([#906 ](https://github.com/ros2/launch/issues/906)_)
* Allow providing launch args to include using let in frontends ([#848 ](https://github.com/ros2/launch//issues/848)_)
* Fix Setuptoolsdeprecations ([#898 ](https://github.com/ros2/launch/issues/898)_)
* Remove LaunchDescriptionArgument ([#891 ](https://github.com/ros2/launch/issues/891)_)
* Make sure to install py.typed files ([#886 ](https://github.com/ros2/launch/issues/886)_)
* use custom log_file name as per the user setting ([#861 ](https://github.com/ros2/launch/issues/861)_)
* Using [`TimerAction`` with ``SetParameter`` from launch_ros causes crash (`#879 ](https://github.com/ros2/launch/issues/879)_)
* Fix [`log\_*`` warnings (`#883 ](https://github.com/ros2/launch/issues/883)_)
* Updated [`launch`` typings (`#831 ](https://github.com/ros2/launch/issues/831)_)
* Allow Path in substitutions, instead of requiring cast to str ([#873 ](https://github.com/ros2/launch/issues/873)_)
* Add a [`/`` path join operator for ``PathJoinSubstitution`` (`#868 ](https://github.com/ros2/launch/issues/868)_)
* Other Logging Implementations with [`getLevelNamesMapping`` fix (`#866 ](https://github.com/ros2/launch/issues/866)_)
* Revert "Add Other Logging Implementations ([#858 ](https://github.com/ros2/launch/issues/858)_)" ([#865 ](https://github.com/ros2/launch/issues/865)_) This reverts commit b7b31c45b0eb350deedd282b88398d1ca0d5faf4.
* Add Other Logging Implementations ([#858 ](https://github.com/ros2/launch/issues/858)_)
* Contributors: Auguste Lalande, Christian Ruf, Christophe Bedard, David V. Lu!!, Emerson Knapp, Harrison Chen, Jonas Otto, Kenji Brameld (TRACLabs), Matthijs van der Burgh, Michael Carlstrom, Scott K Logan, Sebastian Javier D'Alessandro Szymanowski, Tanishq Chaudhary, Will, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_pytest <https://github.com/ros2/launch/tree/lyrical/launch_pytest/CHANGELOG.rst>`__

* fix regressions ([#959 ](https://github.com/ros2/launch/issues/959)_)
* fix: add get_launch_test_fixture_scope for pytest compatibility ([#949 ](https://github.com/ros2/launch/issues/949)_)
* Switch osrf_pycommon dependency to system package ([#817 ](https://github.com/ros2/launch/issues/817)_)
* Fix Setuptoolsdeprecations ([#898 ](https://github.com/ros2/launch/issues/898)_)
* Make sure to install py.typed files ([#886 ](https://github.com/ros2/launch/issues/886)_)
* Add remaining [`py.typed`` (`#884 ](https://github.com/ros2/launch/issues/884)_)
* Allow Path in substitutions, instead of requiring cast to str ([#873 ](https://github.com/ros2/launch/issues/873)_)
* fix(launch_pytest): prevent re-wrapping test funtions on re-run ([#855 ](https://github.com/ros2/launch/issues/855)_)
* Contributors: Christophe Bedard, Daisuke Nishimatsu, David Revay, Emerson Knapp, Michael Carlstrom, Scott K Logan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_ros <https://github.com/ros2/launch_ros/tree/lyrical/launch_ros/CHANGELOG.rst>`__

* Fix flake8 ([#529 ](https://github.com/ros2/launch_ros//issues/529)_)
* correct typos ([#524 ](https://github.com/ros2/launch_ros//issues/524)_)
* Fix regression ([#521 ](https://github.com/ros2/launch_ros//issues/521)_)
* Fix rhel10 flake8 error ([#515 ](https://github.com/ros2/launch_ros//issues/515)_)
* Compatiblity with 'Populate Transitions' [ros2/rcl#1269 ](https://github.com/ros2/rcl/issues/1269)_ ([#495 ](https://github.com/ros2/launch_ros/issues/495)_)
* remove importlib ([#508 ](https://github.com/ros2/launch_ros/issues/508)_)
* Make FindPackage substitutions a Path to get operator / ([#494 ](https://github.com/ros2/launch_ros/issues/494)_)
* Expose lifecycle_node ([#327 ](https://github.com/ros2/launch_ros/issues/327)_) (with test) ([#482 ](https://github.com/ros2/launch_ros/issues/482)_)
* Expose composable_lifecycle_node in front-end ([#480 ](https://github.com/ros2/launch_ros/issues/480)_)
* Switch osrf_pycommon dependency to system package ([#431 ](https://github.com/ros2/launch_ros/issues/431)_)
* Fix SetUseSimTime for launch frontends ([#488 ](https://github.com/ros2/launch_ros/issues/488)_)
* fix setuptools deprecations ([#475 ](https://github.com/ros2/launch_ros/issues/475)_)
* improve type readability in errors ([#469 ](https://github.com/ros2/launch_ros/issues/469)_)
* Fix: LoadComposableNodes fails to parse wildcard param files correctly ([#460 ](https://github.com/ros2/launch_ros/issues/460)_) ([#465 ](https://github.com/ros2/launch_ros/issues/465)_)
* Contributors: Auguste Lalande, Christophe Bedard, Emerson Knapp, Emre Kuru, Jasper van Brakel, Kenji Brameld, Michael Carlstrom, Scott K Logan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing <https://github.com/ros2/launch/tree/lyrical/launch_testing/CHANGELOG.rst>`__

* Correct typos ([#961 ](https://github.com/ros2/launch/issues/961)_)
* Fix test_io_tests for Ubuntu26 ([#960 ](https://github.com/ros2/launch/issues/960)_)
* Fix flake8 ([#952 ](https://github.com/ros2/launch/issues/952)_)
* Switch osrf_pycommon dependency to system package ([#817 ](https://github.com/ros2/launch/issues/817)_)
* Fix Setuptoolsdeprecations ([#898 ](https://github.com/ros2/launch/issues/898)_)
* Make sure to install py.typed files ([#886 ](https://github.com/ros2/launch/issues/886)_)
* Add remaining [`py.typed`` (`#884 ](https://github.com/ros2/launch/issues/884)_)
* Updated [`launch`` typings (`#831 ](https://github.com/ros2/launch/issues/831)_)
* Contributors: Auguste Lalande, Christophe Bedard, Michael Carlstrom, Scott K Logan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing_ament_cmake <https://github.com/ros2/launch/tree/lyrical/launch_testing_ament_cmake/CHANGELOG.rst>`__

* Fix CMake deprecation ([#899 ](https://github.com/ros2/launch/issues/899)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing_examples <https://github.com/ros2/examples/tree/lyrical/launch_testing/launch_testing_examples/CHANGELOG.rst>`__

* improve test integrity with rmw_cyclonedds_cpp. ([#440 ](https://github.com/ros2/examples/issues/440)_)
* Fix setuptools deprecations ([#421 ](https://github.com/ros2/examples/issues/421)_)
* Contributors: Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing_ros <https://github.com/ros2/launch_ros/tree/lyrical/launch_testing_ros/CHANGELOG.rst>`__

* Add tests isolation in launch_testing_ros ([#528 ](https://github.com/ros2/launch_ros//issues/528)_)
* Surpressing multi-threaded process warning from flake8. ([#520 ](https://github.com/ros2/launch_ros//issues/520)_)
* correct typos ([#524 ](https://github.com/ros2/launch_ros//issues/524)_)
* Fix launch_ros_testing shutdown race in WaitForTopics ([#511 ](https://github.com/ros2/launch_ros/issues/511)_)
* Give the option to inject a quality of service profile ([#493 ](https://github.com/ros2/launch_ros/issues/493)_)
* fix setuptools deprecations ([#475 ](https://github.com/ros2/launch_ros/issues/475)_)
* [`WaitForTopics``: wait for publisher-subscriber connection to be established (`#474 ](https://github.com/ros2/launch_ros/issues/474)_)
* Contributors: Auguste Lalande, Giorgio Pintaudi, Julien Enoch, Michael Carroll, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_xml <https://github.com/ros2/launch/tree/lyrical/launch_xml/CHANGELOG.rst>`__

* Correct typos ([#961 ](https://github.com/ros2/launch/issues/961)_)
* Support frontends for PathJoinSubstitution ([#943 ](https://github.com/ros2/launch/issues/943)_)
* Capture the environment variables in TimerAction ([#728 ](https://github.com/ros2/launch/issues/728)_)
* Expose StringJoinSubstitution to frontend ([#857 ](https://github.com/ros2/launch//issues/857)_)
* Fix all/any in xml and yaml launch files ([#906 ](https://github.com/ros2/launch/issues/906)_)
* Allow providing launch args to include using let in frontends ([#848 ](https://github.com/ros2/launch//issues/848)_)
* Fix Setuptoolsdeprecations ([#898 ](https://github.com/ros2/launch/issues/898)_)
* Make sure to install py.typed files ([#886 ](https://github.com/ros2/launch/issues/886)_)
* Add remaining [`py.typed`` (`#884 ](https://github.com/ros2/launch/issues/884)_)
* Fix [`log\_*`` warnings (`#883 ](https://github.com/ros2/launch/issues/883)_)
* Allow Path in substitutions, instead of requiring cast to str ([#873 ](https://github.com/ros2/launch/issues/873)_)
* Other Logging Implementations with [`getLevelNamesMapping`` fix (`#866 ](https://github.com/ros2/launch/issues/866)_)
* Revert "Add Other Logging Implementations ([#858 ](https://github.com/ros2/launch/issues/858)_)" ([#865 ](https://github.com/ros2/launch/issues/865)_) This reverts commit b7b31c45b0eb350deedd282b88398d1ca0d5faf4.
* Add Other Logging Implementations ([#858 ](https://github.com/ros2/launch/issues/858)_)
* Contributors: Auguste Lalande, Christian Ruf, Christophe Bedard, Emerson Knapp, Matthijs van der Burgh, Michael Carlstrom, Sebastian Javier D'Alessandro Szymanowski, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_yaml <https://github.com/ros2/launch/tree/lyrical/launch_yaml/CHANGELOG.rst>`__

* Correct typos ([#961 ](https://github.com/ros2/launch/issues/961)_)
* Support frontends for PathJoinSubstitution ([#943 ](https://github.com/ros2/launch/issues/943)_)
* Capture the environment variables in TimerAction ([#728 ](https://github.com/ros2/launch/issues/728)_)
* Expose StringJoinSubstitution to frontend ([#857 ](https://github.com/ros2/launch//issues/857)_)
* Fix all/any in xml and yaml launch files ([#906 ](https://github.com/ros2/launch/issues/906)_)
* Allow providing launch args to include using let in frontends ([#848 ](https://github.com/ros2/launch//issues/848)_)
* Fix Setuptoolsdeprecations ([#898 ](https://github.com/ros2/launch/issues/898)_)
* Make sure to install py.typed files ([#886 ](https://github.com/ros2/launch/issues/886)_)
* Add remaining [`py.typed`` (`#884 ](https://github.com/ros2/launch/issues/884)_)
* Fix [`log\_*`` warnings (`#883 ](https://github.com/ros2/launch/issues/883)_)
* Other Logging Implementations with [`getLevelNamesMapping`` fix (`#866 ](https://github.com/ros2/launch/issues/866)_)
* Revert "Add Other Logging Implementations ([#858 ](https://github.com/ros2/launch/issues/858)_)" ([#865 ](https://github.com/ros2/launch/issues/865)_) This reverts commit b7b31c45b0eb350deedd282b88398d1ca0d5faf4.
* Add Other Logging Implementations ([#858 ](https://github.com/ros2/launch/issues/858)_)
* Contributors: Auguste Lalande, Christian Ruf, Christophe Bedard, Matthijs van der Burgh, Michael Carlstrom, Sebastian Javier D'Alessandro Szymanowski, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `libstatistics_collector <https://github.com/ros-tooling/libstatistics_collector/tree/lyrical/CHANGELOG.rst>`__

* Use new aggregate rosidl target instead of _TARGETS ([#222 ](https://github.com/ros-tooling/libstatistics_collector/issues/222)_)
* fix cmake deprecation ([#214 ](https://github.com/ros-tooling/libstatistics_collector/issues/214)_)
* Bump ros-tooling/action-ros-ci from 0.3 to 0.4
* Bump codecov/codecov-action from 5.3.1 to 5.4.0
* Bump codecov/codecov-action from 5.1.2 to 5.3.1
* Bump codecov/codecov-action from 5.0.7 to 5.1.2
* Bump codecov/codecov-action from 4.6.0 to 5.0.7
* Contributors: Alexis Tsogias, dependabot[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `libyaml_vendor <https://github.com/ros2/libyaml_vendor/tree/lyrical/CHANGELOG.rst>`__

* Replace ament_vendor with cmake module ([#67 ](https://github.com/ros2/libyaml_vendor/issues/67)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#65 ](https://github.com/ros2/libyaml_vendor/issues/65)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `lifecycle <https://github.com/ros2/demos/tree/lyrical/lifecycle/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* r-simonelli/demos-lifecycle ([#750 ](https://github.com/ros2/demos/issues/750)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Emerson Knapp, Lucas Wendland, Shane Loretz, mosfet80, r-simonelli


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `lifecycle_msgs <https://github.com/ros2/rcl_interfaces/tree/lyrical/lifecycle_msgs/CHANGELOG.rst>`__

* Use builtin_interfaces/Time for TransitionEvent stamp ([#185 ](https://github.com/ros2/rcl_interfaces/issues/185)_)
* Fix cmake deprecation ([#180 ](https://github.com/ros2/rcl_interfaces/issues/180)_)
* Contributors: Jasper van Brakel, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `lifecycle_py <https://github.com/ros2/demos/tree/lyrical/lifecycle_py/CHANGELOG.rst>`__

* Add [`ament_mypy`` support and type hints to ``lifecycle_py`` (`#778 ](https://github.com/ros2/demos/issues/778)_)
* Revert lifecycle_py accidental merge - ament_mypy ([#777 ](https://github.com/ros2/demos//issues/777)_)
* action_tutorials_py: add ament_mypy support ([#775 ](https://github.com/ros2/demos//issues/775)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* fix setuptools deprecations ([#733 ](https://github.com/ros2/demos/issues/733)_)
* Contributors: Lucas Wendland, Mohit Kumaresan, mohit, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `logging_demo <https://github.com/ros2/demos/tree/lyrical/logging_demo/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* Use EnableRmwIsolation in launch tests ([#724 ](https://github.com/ros2/demos/issues/724)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Lucas Wendland, Scott K Logan, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `lttngpy <https://github.com/ros2/ros2_tracing/tree/lyrical/lttngpy/CHANGELOG.rst>`__

* Use <lttng/lttng.h> in lttngpy and clean up includes ([#222 ](https://github.com/ros2/ros2_tracing/issues/222)_)
* Allow creating snapshot sessions ([#195 ](https://github.com/ros2/ros2_tracing/issues/195)_)
* [Fix] compile fail ([#194 ](https://github.com/ros2/ros2_tracing/issues/194)_)
* Use pybind11 from deb or pixi ([#197 ](https://github.com/ros2/ros2_tracing/issues/197)_)
* Add support for starting tracing at runtime ([#191 ](https://github.com/ros2/ros2_tracing/issues/191)_)
* Contributors: Alejandro Hernández Cordero, RHolland, Shravan Deva, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `map_msgs <https://github.com/ros-planning/navigation_msgs/tree/lyrical/map_msgs/CHANGELOG.rst>`__

* Change email address associated with maintainer
* fix cmake deprecation
* Contributors: David V. Lu, Steve Macenski, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `mcap_vendor <https://github.com/ros2/rosbag2/tree/lyrical/mcap_vendor/CHANGELOG.rst>`__

* Update mcap dependency to version 2.1.3 ([#2355 ](https://github.com/ros2/rosbag2/issues/2355)_)
* Remove lz4 vendor package ([#2165 ](https://github.com/ros2/rosbag2/issues/2165)_)
* Replace [`zstd_vendor`` with ``zstd_cmake_module`` (`#2166 ](https://github.com/ros2/rosbag2/issues/2166)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Backport missing [`cstdint`` include (`#2008 ](https://github.com/ros2/rosbag2/issues/2008)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, David Anthony, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `message_filters <https://github.com/ros2/message_filters/tree/lyrical/CHANGELOG.rst>`__

* Avoid vector assignment in message_filters signal callback ([#292 ](https://github.com/ros2/message_filters/issues/292)_) ([#293 ](https://github.com/ros2/message_filters/issues/293)_)
* Cleanup headers and removed deadcode ([#284 ](https://github.com/ros2/message_filters/issues/284)_) ([#291 ](https://github.com/ros2/message_filters/issues/291)_)
* feat(python): add python implementation of InputAligner  (backport [#283 ](https://github.com/ros2/message_filters/issues/283)_) ([#286 ](https://github.com/ros2/message_filters/issues/286)_)
* C++20 style ([#272 ](https://github.com/ros2/message_filters/issues/272)_)
* ([#221 ](https://github.com/ros2/message_filters/issues/221)_) Tutorials: Add DeltaFilter Python tutorial ([#277 ](https://github.com/ros2/message_filters/issues/277)_)
* DeltaFilter(C++): Add DeltaFilter class. Add tests ([#273 ](https://github.com/ros2/message_filters/issues/273)_) ([#273 ](https://github.com/ros2/message_filters/issues/273)_)
* Removed dead code
* Improvements and more test coverage
* Use new ROSIDL aggregate CMake target
* Tutorials minor fixers: Replace the TODOs with the actual links to other tutorials as required. Rename Approximate-Tyme tutorial to Approximate-Time ([#266 ](https://github.com/ros2/message_filters/issues/266)_)
* Tutorials: Add LatestTime synchronization policy tutorial ([#266 ](https://github.com/ros2/message_filters/issues/266)_)
* Tutorials: Approximate-Synchronizer: Label CMake code blocks with the right language markings
* Tutorials: Add C++ tutorial for Approximate Epsilon Time Sync policy
* DeltaFilter(Python): Add DeltaFilter for Python. Add tests. Add docstring to filters and comparison handlers ([#252 ](https://github.com/ros2/message_filters/issues/252)_)
* remove setup.py ([#257 ](https://github.com/ros2/message_filters/issues/257)_)
* ([#246 ](https://github.com/ros2/message_filters/issues/246)_, [#186 ](https://github.com/ros2/message_filters/issues/186)_) Subscriber(Python): Add callback_group, event_callbacks, qos_overriding_options, raw and content_filter_options arguments to __init_\_. ([#251 ](https://github.com/ros2/message_filters/issues/251)_)
* Add kwargs passing from Subscriber to node.create_subscription ([#247 ](https://github.com/ros2/message_filters/issues/247)_) Fixes callers that use callback_group
* Get topic name from base class to propagate remaps ([#68 ](https://github.com/ros2/message_filters/issues/68)_)
* [#130 ](https://github.com/ros2/message_filters/issues/130)_ add simple filter tutorial for cpp ([#239 ](https://github.com/ros2/message_filters/issues/239)_)
* [#200 ](https://github.com/ros2/message_filters/issues/200)_ fix inconsistensy between cpp and python exact time synchronizer impl ([#238 ](https://github.com/ros2/message_filters/issues/238)_)
* Add simple filter tutorials ([#226 ](https://github.com/ros2/message_filters/issues/226)_)
* Update subscription callback signatures ([#222 ](https://github.com/ros2/message_filters/issues/222)_)
* Add chain tutorial python ([#219 ](https://github.com/ros2/message_filters/issues/219)_)
* Change function signature for Python Subscriber class ([#220 ](https://github.com/ros2/message_filters/issues/220)_)
* Add Python implementation for a Chain filter ([#213 ](https://github.com/ros2/message_filters/issues/213)_)
* Fix comparison of different time sources in C++ TimeSequencer ([#202 ](https://github.com/ros2/message_filters/issues/202)_)
* Some fixes to documentation ([#208 ](https://github.com/ros2/message_filters/issues/208)_)
* Create a Chain class tutorial for C++ ([#203 ](https://github.com/ros2/message_filters/issues/203)_)
* get rid of deprecated rclcpp::spin_some(). ([#201 ](https://github.com/ros2/message_filters/issues/201)_)
* Add 'Cache (C++)' tutorial ([#196 ](https://github.com/ros2/message_filters/issues/196)_)
* cache.hpp: Add allow_headerless ([#195 ](https://github.com/ros2/message_filters/issues/195)_)
* Simplify method call ([#194 ](https://github.com/ros2/message_filters/issues/194)_)
* Fix cache tutorial: added tab extension ([#190 ](https://github.com/ros2/message_filters/issues/190)_)
* Add tutorial for Cache filter for Python ([#185 ](https://github.com/ros2/message_filters/issues/185)_)
* fix cmake deprecation ([#182 ](https://github.com/ros2/message_filters/issues/182)_)
* update documentation ([#180 ](https://github.com/ros2/message_filters/issues/180)_)
* Removed missing pragma ([#179 ](https://github.com/ros2/message_filters/issues/179)_)
* Removed Subscriber deprecation ([#177 ](https://github.com/ros2/message_filters/issues/177)_)
* Removed deprecated headers ([#176 ](https://github.com/ros2/message_filters/issues/176)_)
* Use warning instead of warn ([#178 ](https://github.com/ros2/message_filters/issues/178)_)
* Docs - Remove C++ implementation limit of 9 channels ([#174 ](https://github.com/ros2/message_filters/issues/174)_)
* Contributors: Alejandro Hernandez Cordero, Alejandro Hernández Cordero, Alex Spitzer, Emerson Knapp, Erwin L., EsipovPA, Johannes Böhm, Michael Carlstrom, Patrick Roncagliolo, Pavel Esipov, Samuel Foo Enze, Tomoya Fujita, mergify[bot], mini-1235, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `mimick_vendor <https://github.com/ros2/mimick_vendor/tree/lyrical/CHANGELOG.rst>`__

* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#40 ](https://github.com/ros2/mimick_vendor/issues/40)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `nav_msgs <https://github.com/ros2/common_interfaces/tree/lyrical/nav_msgs/CHANGELOG.rst>`__

* Adding the Trajectory and trajectoryPoint messages ([#296 ](https://github.com/ros2/common_interfaces/issues/296)_)
* Fix CMAKE deprecation ([#288 ](https://github.com/ros2/common_interfaces/issues/288)_)
* Contributors: Steve Macenski, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `osrf_testing_tools_cpp <https://github.com/osrf/osrf_testing_tools_cpp/tree/lyrical/osrf_testing_tools_cpp/CHANGELOG.rst>`__

* fix cmake min version ([#96 ](https://github.com/osrf/osrf_testing_tools_cpp/issues/96)_)
* fix cmake deprecation  ([#94 ](https://github.com/osrf/osrf_testing_tools_cpp/issues/94)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `pendulum_control <https://github.com/ros2/demos/tree/lyrical/pendulum_control/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* Update subscription callback signatures ([#754 ](https://github.com/ros2/demos/issues/754)_)
* get rid of deprecated rclcpp::spin_some(). ([#734 ](https://github.com/ros2/demos/issues/734)_)
* Use EnableRmwIsolation in launch tests ([#724 ](https://github.com/ros2/demos/issues/724)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Set envars to run tests with rmw_zenoh_cpp with multicast discovery ([#711 ](https://github.com/ros2/demos/issues/711)_)
* Use target_link_libraries instead of ament_target_dependencies ([#707 ](https://github.com/ros2/demos/issues/707)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Scott K Logan, Shane Loretz, Tomoya Fujita, mini-1235, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `pendulum_msgs <https://github.com/ros2/demos/tree/lyrical/pendulum_msgs/CHANGELOG.rst>`__

* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `performance_test_fixture <https://github.com/ros2/performance_test_fixture/tree/lyrical/CHANGELOG.rst>`__

* fix cmake deprecation ([#31 ](https://github.com/ros2/performance_test_fixture/issues/31)_)
* Remove CODEOWNERS and mirror-rolling-to-main workflow. ([#28 ](https://github.com/ros2/performance_test_fixture/issues/28)_)
* Contributors: Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `pluginlib <https://github.com/ros/pluginlib/tree/lyrical/pluginlib/CHANGELOG.rst>`__

* Fix some minor issues ([#292 ](https://github.com/ros/pluginlib/issues/292)_)
* Add support for passing arguments to constructors ([#291 ](https://github.com/ros/pluginlib/issues/291)_)
* Export includes ([#290 ](https://github.com/ros/pluginlib/issues/290)_)
* Updated deprecated ament_index_cpp API ([#289 ](https://github.com/ros/pluginlib/issues/289)_)
* refactor: replace regex with find_last_of to split plugin name ([#271 ](https://github.com/ros/pluginlib/issues/271)_)
* Removed tinyxml2_vendor dependency ([#274 ](https://github.com/ros/pluginlib/issues/274)_)
* Add ros2plugin ([#165 ](https://github.com/ros/pluginlib/issues/165)_)
* Contributors: Alejandro Hernández Cordero, Jeremie Deray, ipa-fez, pum1k


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `point_cloud_transport <https://github.com/ros-perception/point_cloud_transport/tree/lyrical/point_cloud_transport/CHANGELOG.rst>`__

* Fix exit crash on aarch64 by using leaky singleton for global loader ([#157 ](https://github.com/ros-perception/point_cloud_transport/issues/157)_)
* Include message type ([#152 ](https://github.com/ros-perception/point_cloud_transport/issues/152)_)
* Use new aggregate rosidl target instead of _TARGETS ([#153 ](https://github.com/ros-perception/point_cloud_transport/issues/153)_) Co-authored-by: Alexis Tsogias <a.tsogias@cellumation.com>
* Improvements ([#150 ](https://github.com/ros-perception/point_cloud_transport/issues/150)_)
* Expose original ROS Publishers and Subscription ([#146 ](https://github.com/ros-perception/point_cloud_transport/issues/146)_) ([#148 ](https://github.com/ros-perception/point_cloud_transport/issues/148)_)
* Fix duplicate component registration for Republisher ([#142 ](https://github.com/ros-perception/point_cloud_transport/issues/142)_)
* Removed outdated comment ([#138 ](https://github.com/ros-perception/point_cloud_transport/issues/138)_)
* Use standard unsigned int in place of uint for Windows compatibility ([#134 ](https://github.com/ros-perception/point_cloud_transport/issues/134)_)
* Update subscriber filter ([#126 ](https://github.com/ros-perception/point_cloud_transport/issues/126)_)
* Simplify NodeInterface API mehotd call ([#129 ](https://github.com/ros-perception/point_cloud_transport/issues/129)_)
* Fixed QOS override tests ([#128 ](https://github.com/ros-perception/point_cloud_transport/issues/128)_)
* Deprecated rmw_qos_profile_t ([#125 ](https://github.com/ros-perception/point_cloud_transport/issues/125)_)
* Feat/Add LifecycleNode Support ([#109 ](https://github.com/ros-perception/point_cloud_transport/issues/109)_)
* Add [`rclcpp::shutdown`` (`#110 ](https://github.com/ros-perception/point_cloud_transport/issues/110)_)
* Contributors: Alejandro Hernández Cordero, Alexis Tsogias, ElSayed ElSheikh, Michael Carroll, Silvio Traversaro, Yuyuan Yuan, mergify[bot], mini-1235


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `point_cloud_transport_py <https://github.com/ros-perception/point_cloud_transport/tree/lyrical/point_cloud_transport_py/CHANGELOG.rst>`__

* Use new aggregate rosidl target instead of _TARGETS ([#153 ](https://github.com/ros-perception/point_cloud_transport/issues/153)_)
* Python improvements ([#151 ](https://github.com/ros-perception/point_cloud_transport/issues/151)_)
* Use pybind11 from deb or pixi ([#131 ](https://github.com/ros-perception/point_cloud_transport/issues/131)_)
* Simplify NodeInterface API mehotd call ([#129 ](https://github.com/ros-perception/point_cloud_transport/issues/129)_)
* Feat/Add LifecycleNode Support ([#109 ](https://github.com/ros-perception/point_cloud_transport/issues/109)_)
* Contributors: Alejandro Hernández Cordero, Alexis Tsogias, ElSayed ElSheikh


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `python_qt_binding <https://github.com/ros-visualization/python_qt_binding/tree/lyrical/CHANGELOG.rst>`__

* Pick Qt version at build time, not install time ([#161 ](https://github.com/ros-visualization/python_qt_binding/issues/161)_)
* Re-add exec depend on python3 qt bindings rosdep key ([#160 ](https://github.com/ros-visualization/python_qt_binding/issues/160)_)
* Remove qt6-base-dev from package.xml ([#159 ](https://github.com/ros-visualization/python_qt_binding/issues/159)_)
* Depend on python3-dev ([#158 ](https://github.com/ros-visualization/python_qt_binding/issues/158)_)
* Use sip-build and python3_add_library for Qt5/Qt6 ([#157 ](https://github.com/ros-visualization/python_qt_binding/issues/157)_)
* fix setuptools deprecation ([#151 ](https://github.com/ros-visualization/python_qt_binding/issues/151)_)
* fix cmake deprecation ([#150 ](https://github.com/ros-visualization/python_qt_binding/issues/150)_)
* Remove the mirror-rolling-to-main workflow ([#145 ](https://github.com/ros-visualization/python_qt_binding/issues/145)_)
* Remove CODEOWNERS ([#144 ](https://github.com/ros-visualization/python_qt_binding/issues/144)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `qt_dotgraph <https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_dotgraph/CHANGELOG.rst>`__

* More qt6 fixes ([#334 ](https://github.com/ros-visualization/qt_gui_core/issues/334)_) ([#335 ](https://github.com/ros-visualization/qt_gui_core/issues/335)_) (cherry picked from commit 62f29544c4061006f9c09c3dfa4bf2895e8126e0) Co-authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>
* Support qt6 ([#293 ](https://github.com/ros-visualization/qt_gui_core/issues/293)_)
* Ignore case when asserting snippet presence in tests ([#314 ](https://github.com/ros-visualization/qt_gui_core/issues/314)_)
* Fix setupTools deprecations ([#308 ](https://github.com/ros-visualization/qt_gui_core/issues/308)_)
* Contributors: Alejandro Hernández Cordero, Scott K Logan, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `qt_gui <https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_gui/CHANGELOG.rst>`__

* More qt6 fixes ([#334 ](https://github.com/ros-visualization/qt_gui_core/issues/334)_) ([#335 ](https://github.com/ros-visualization/qt_gui_core/issues/335)_) (cherry picked from commit 62f29544c4061006f9c09c3dfa4bf2895e8126e0) Co-authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>
* Support qt6 ([#293 ](https://github.com/ros-visualization/qt_gui_core/issues/293)_)
* fix(qt_gui): __builtin_\_ -> builtins ([#315 ](https://github.com/ros-visualization/qt_gui_core/issues/315)_)
* Fix cmake deprecations ([#307 ](https://github.com/ros-visualization/qt_gui_core/issues/307)_)
* Contributors: Alejandro Hernández Cordero, Matthijs van der Burgh, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `qt_gui_app <https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_gui_app/CHANGELOG.rst>`__

* Fix cmake deprecations ([#307 ](https://github.com/ros-visualization/qt_gui_core/issues/307)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `qt_gui_core <https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_gui_core/CHANGELOG.rst>`__

* Update qt_gui_core to package.xml version 2. ([#319 ](https://github.com/ros-visualization/qt_gui_core/issues/319)_)
* Fix cmake deprecations ([#307 ](https://github.com/ros-visualization/qt_gui_core/issues/307)_)
* Contributors: Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `qt_gui_cpp <https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_gui_cpp/CHANGELOG.rst>`__

* More qt6 fixes ([#334 ](https://github.com/ros-visualization/qt_gui_core/issues/334)_) ([#335 ](https://github.com/ros-visualization/qt_gui_core/issues/335)_) (cherry picked from commit 62f29544c4061006f9c09c3dfa4bf2895e8126e0) Co-authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>
* find_package(Qt...) in downstream packages ([#332 ](https://github.com/ros-visualization/qt_gui_core/issues/332)_)
* Export qt dependencies in package.xml ([#331 ](https://github.com/ros-visualization/qt_gui_core/issues/331)_)
* Use qt-base-dev / libqtwidgets ([#330 ](https://github.com/ros-visualization/qt_gui_core/issues/330)_)
* Support qt6 ([#293 ](https://github.com/ros-visualization/qt_gui_core/issues/293)_)
* Use new aggregate rosidl target instead of _TARGETS ([#325 ](https://github.com/ros-visualization/qt_gui_core/issues/325)_)
* remove unsued setup.py ([#323 ](https://github.com/ros-visualization/qt_gui_core/issues/323)_)
* Removed tinyxml2_vendor dependency ([#309 ](https://github.com/ros-visualization/qt_gui_core/issues/309)_)
* Fix cmake deprecations ([#307 ](https://github.com/ros-visualization/qt_gui_core/issues/307)_)
* Removed deprecated headers ([#305 ](https://github.com/ros-visualization/qt_gui_core/issues/305)_)
* Use target_link_libraries instead of ament_target_dependencies ([#302 ](https://github.com/ros-visualization/qt_gui_core/issues/302)_)
* Contributors: Alejandro Hernández Cordero, Alexis Tsogias, Michael Carlstrom, Shane Loretz, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `qt_gui_py_common <https://github.com/ros-visualization/qt_gui_core/tree/lyrical/qt_gui_py_common/CHANGELOG.rst>`__

* More qt6 fixes ([#334 ](https://github.com/ros-visualization/qt_gui_core/issues/334)_) ([#335 ](https://github.com/ros-visualization/qt_gui_core/issues/335)_)
* Support qt6 ([#293 ](https://github.com/ros-visualization/qt_gui_core/issues/293)_)
* remove unsued setup.py ([#323 ](https://github.com/ros-visualization/qt_gui_core/issues/323)_)
* Fix cmake deprecations ([#307 ](https://github.com/ros-visualization/qt_gui_core/issues/307)_)
* Contributors: Alejandro Hernández Cordero, Michael Carlstrom, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `quality_of_service_demo_cpp <https://github.com/ros2/demos/tree/lyrical/quality_of_service_demo/rclcpp/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_) demo_nodes_cpp/CMakeLists.txt require cmake min version 3.12 other modules cmake 3.5. It is proposed to standardize with version 3.12. This also fixes cmake <3.10 deprecation warnings
* Contributors: Emerson Knapp, Lucas Wendland, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `quality_of_service_demo_py <https://github.com/ros2/demos/tree/lyrical/quality_of_service_demo/rclpy/CHANGELOG.rst>`__

* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* fix setuptools deprecations ([#731 ](https://github.com/ros2/demos/issues/731)_)
* Contributors: Lucas Wendland, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl <https://github.com/ros2/rcl/tree/lyrical/rcl/CHANGELOG.rst>`__

* feat: Added check for double usage of entities in rcl_waitset ([#1206 ](https://github.com/ros2/rcl/issues/1206)_)
* Preserve [`rmw_create_node`` error state in ``rcl_node_init`` by using ``RCL_EXPECT_ERROR_IS_SET`` (`#1313 ](https://github.com/ros2/rcl/issues/1313)_)
* Remove clang warnings ([#1315 ](https://github.com/ros2/rcl/issues/1315)_)
* Add RCL_EXPECT_ERROR_IS_SET macro ([#1312 ](https://github.com/ros2/rcl/issues/1312)_)
* Improved documentation of rcl_XYZ_set_on_new_XYZ_callback ([#1289 ](https://github.com/ros2/rcl/issues/1289)_)
* Add rcl_subscription_options_set_acceptable_buffer_backends with proper lifetime management ([#1308 ](https://github.com/ros2/rcl/issues/1308)_)
* Added tracepoint to rcl_take_loaned_message ([#1300 ](https://github.com/ros2/rcl/issues/1300)_)
* Apply change from "Use new aggregate rosidl target instead of _TARGETS ([#1302 ](https://github.com/ros2/rcl/issues/1302)_)" on some leftovers ([#1309 ](https://github.com/ros2/rcl/issues/1309)_)
* Remove the check for content filter support at the RCL layer ([#1304 ](https://github.com/ros2/rcl/issues/1304)_)
* Use new aggregate rosidl target instead of _TARGETS ([#1302 ](https://github.com/ros2/rcl/issues/1302)_)
* Add API for client libraries to set action server goal expiration callbacks ([#1295 ](https://github.com/ros2/rcl/issues/1295)_)
* Fujitatomoya/improve rcl test graph ([#1296 ](https://github.com/ros2/rcl/issues/1296)_)
* Add content filtering support check for subscriptions ([#1293 ](https://github.com/ros2/rcl/issues/1293)_)
* rcl_logging_implementation package support. ([#1276 ](https://github.com/ros2/rcl/issues/1276)_)
* Remove default from switch with enum, so that compiler warns. ([#1278 ](https://github.com/ros2/rcl/issues/1278)_)
* Add clients servers info ([#1161 ](https://github.com/ros2/rcl/issues/1161)_)
* Fix REP url locations ([#1271 ](https://github.com/ros2/rcl/issues/1271)_)
* rcl_logging_allocator_initialize() support. ([#1049 ](https://github.com/ros2/rcl/issues/1049)_)
* Fix typos: occurrs->occurs, successfull->successful ([#1259 ](https://github.com/ros2/rcl/issues/1259)_)
* Refer to 'the middleware' and not 'the DDS implementation' in doc ([#1260 ](https://github.com/ros2/rcl/issues/1260)_)
* Switch to isolated testing via rmw_test_fixture ([#1251 ](https://github.com/ros2/rcl/issues/1251)_)
* Fix Cmake deprecation ([#1249 ](https://github.com/ros2/rcl/issues/1249)_)
* Assert HistoryQoS in test_info_by_topic ([#1242 ](https://github.com/ros2/rcl//issues/1242)_)
* Add a test for the subscription option 'ignore_local_publications' ([#1239 ](https://github.com/ros2/rcl//issues/1239)_)
* remove unnecessary test_with_localhost_only. ([#1238 ](https://github.com/ros2/rcl/issues/1238)_)
* Address memory leaks in rcl test_timer_init_state ([#1236 ](https://github.com/ros2/rcl/issues/1236)_)
* Removed unused nondefault_qos_profile ([#1233 ](https://github.com/ros2/rcl/issues/1233)_)
* Removed unused functions ([#1230 ](https://github.com/ros2/rcl/issues/1230)_)
* remove rcl_qos_profile_rosout_default. ([#1225 ](https://github.com/ros2/rcl/issues/1225)_)
* remove rmw_connext from test. ([#1226 ](https://github.com/ros2/rcl/issues/1226)_)
* Fix a dangling pointer discovered by a fresh Clang ([#1222 ](https://github.com/ros2/rcl/issues/1222)_)
* Contributors: Akihiko Komada, Alejandro Hernández Cordero, Alexander Kornienko, Alexis Tsogias, Barry Xu, CY Chen, Christophe Bedard, Emerson Knapp, Janosch Machowinski, Lee, Mario Domínguez López, Michael Orlov, Minju, Oren Bell PhD, Rushhaank Sahay, Sai Kishor Kothakota, Shane Loretz, Skyler Medeiros, Tim Clephas, Tomoya Fujita, mosfet80, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_action <https://github.com/ros2/rcl/tree/lyrical/rcl_action/CHANGELOG.rst>`__

* fix(rcl_action): use RMW isolation for cross-node tests ([#1311 ](https://github.com/ros2/rcl/issues/1311)_)
* Add 2 interfaces for configuring action client feedback subscription contents filter ([#1287 ](https://github.com/ros2/rcl/issues/1287)_)
* Apply change from "Use new aggregate rosidl target instead of _TARGETS ([#1302 ](https://github.com/ros2/rcl/issues/1302)_)" on some leftovers ([#1309 ](https://github.com/ros2/rcl/issues/1309)_)
* simplify error logging for timer cancellation ([#1307 ](https://github.com/ros2/rcl/issues/1307)_)
* fix: Prevent short time endless loop in expire_timer ([#1303 ](https://github.com/ros2/rcl/issues/1303)_)
* Add API for client libraries to set action server goal expiration callbacks ([#1295 ](https://github.com/ros2/rcl/issues/1295)_)
* support rcl_action_count_clients and rcl_action_count_servers. ([#1294 ](https://github.com/ros2/rcl/issues/1294)_)
* Fix REP url locations ([#1271 ](https://github.com/ros2/rcl/issues/1271)_)
* add rcl_action_goal_handle_is_abortable(). ([#1257 ](https://github.com/ros2/rcl/issues/1257)_)
* Fix Cmake deprecation ([#1249 ](https://github.com/ros2/rcl/issues/1249)_)
* Contributors: Alexis Tsogias, Barry Xu, Janosch Machowinski, Skyler Medeiros, Tim Clephas, Tomoya Fujita, William Woodall, Yuyuan Yuan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_interfaces <https://github.com/ros2/rcl_interfaces/tree/lyrical/rcl_interfaces/CHANGELOG.rst>`__

* Fix cmake deprecation ([#180 ](https://github.com/ros2/rcl_interfaces/issues/180)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_lifecycle <https://github.com/ros2/rcl/tree/lyrical/rcl_lifecycle/CHANGELOG.rst>`__

* Apply change from "Use new aggregate rosidl target instead of _TARGETS ([#1302 ](https://github.com/ros2/rcl/issues/1302)_)" on some leftovers ([#1309 ](https://github.com/ros2/rcl/issues/1309)_)
* Populate Transitions in Transition Events (continuation) ([#1269 ](https://github.com/ros2/rcl/issues/1269)_)
* Fix REP url locations ([#1271 ](https://github.com/ros2/rcl/issues/1271)_)
* Fix Cmake deprecation ([#1249 ](https://github.com/ros2/rcl/issues/1249)_)
* introduce rcl_lifecycle_get_transition_label_by_id(). ([#1229 ](https://github.com/ros2/rcl/issues/1229)_)
* Contributors: Alexis Tsogias, Jasper van Brakel, Tim Clephas, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_logging_implementation <https://github.com/ros2/rcl_logging/tree/lyrical/rcl_logging_implementation/CHANGELOG.rst>`__

* update rcl_logging_implementation architecture diagram. ([#137 ](https://github.com/ros2/rcl_logging/issues/137)_)
* rcl logging implementation ([#135 ](https://github.com/ros2/rcl_logging/issues/135)_) * 1st draft bring-up for rcl_logging_implementation package. * add test_logging_implementation to check dynamic loading. * address Copilot review comments. * fix: correct visibility macro for DLL export in CMakeLists.txt * add visibility control with RCL_LOGGING_IMPLEMENTATION_DEFAULT_VISIBILITY. * load the all symbols at the initialization. * Use goto pattern to eliminate the cleanup duplication. * Add basic design doc of rmw_logging_implementation. * use RCPPUTILS_SCOPE_EXIT instead of goto statement. * logging visibility macro was incorrect. * logging symbols stay until the peocess actually exits. --------- Co-authored-by: Barry Xu <barry.xu@sony.com>
* Contributors: Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_logging_interface <https://github.com/ros2/rcl_logging/tree/lyrical/rcl_logging_interface/CHANGELOG.rst>`__

* Fix cmake deprecation ([#133 ](https://github.com/ros2/rcl_logging/issues/133)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_logging_noop <https://github.com/ros2/rcl_logging/tree/lyrical/rcl_logging_noop/CHANGELOG.rst>`__

* Fix cmake deprecation ([#133 ](https://github.com/ros2/rcl_logging/issues/133)_)
* Cleanup rcl_logging_noop dependencies. ([#132 ](https://github.com/ros2/rcl_logging/issues/132)_) It shouldn't build_export_depend anything (as nothing downstream should link against it), and all of its dependencies can be private.
* Contributors: Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_logging_spdlog <https://github.com/ros2/rcl_logging/tree/lyrical/rcl_logging_spdlog/CHANGELOG.rst>`__

* feat: add env variable to configure flushing interval ([#139 ](https://github.com/ros2/rcl_logging/issues/139)_)
* Fix cmake deprecation ([#133 ](https://github.com/ros2/rcl_logging/issues/133)_)
* Cleanup overwritten warning messages on error. ([#128 ](https://github.com/ros2/rcl_logging/issues/128)_)
* Contributors: Achille Verheye, Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_yaml_param_parser <https://github.com/ros2/rcl/tree/lyrical/rcl_yaml_param_parser/CHANGELOG.rst>`__

* Remove clang warnings ([#1315 ](https://github.com/ros2/rcl/issues/1315)_)
* fix ([#1310 ](https://github.com/ros2/rcl/issues/1310)_)
* Use the POSIX locale to parse YAML double ([#1292 ](https://github.com/ros2/rcl/issues/1292)_)
* rcl_yaml_node_struct_print print loop interation fix. ([#1290 ](https://github.com/ros2/rcl//issues/1290)_)
* rcl_yaml_param_parser: add support for binary tag to load byte arrays parameters ([#1256 ](https://github.com/ros2/rcl//issues/1256)_)
* Validate name input in add_name_to_ns function ([#1281 ](https://github.com/ros2/rcl/issues/1281)_)
* parse_key() should use yaml_map_lvl_t instead of uint_32. ([#1279 ](https://github.com/ros2/rcl/issues/1279)_)
* Remove default from switch with enum, so that compiler warns. ([#1278 ](https://github.com/ros2/rcl/issues/1278)_)
* Add yaml tags support ([#1275 ](https://github.com/ros2/rcl/issues/1275)_) Co-authored-by: Lei Liu <Lei.Liu.AP@sony.com>
* Fix REP url locations ([#1271 ](https://github.com/ros2/rcl/issues/1271)_)
* Fix param file parsing failure with wildcards due to ordering ([#1253 ](https://github.com/ros2/rcl/issues/1253)_)
* Fix Cmake deprecation ([#1249 ](https://github.com/ros2/rcl/issues/1249)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Hugal31, Michael Carlstrom, Romain Reignier, Tim Clephas, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp <https://github.com/ros2/rclcpp/tree/lyrical/rclcpp/CHANGELOG.rst>`__

* Include EventsCBGExecutor ([#3137 ](https://github.com/ros2/rclcpp/issues/3137)_)
* Fix topic statistics for IPC subscriptions ([#3130 ](https://github.com/ros2/rclcpp/issues/3130)_)
* fix: Fixed MSVC compile errors ([#3135 ](https://github.com/ros2/rclcpp/issues/3135)_)
* feat: Added callback group events executor ([#3097 ](https://github.com/ros2/rclcpp/issues/3097)_)
* Fix wrong dependency ([#3133 ](https://github.com/ros2/rclcpp/issues/3133)_)
* feat: Switch to c++20 and remove resulting compile warnings ([#3124 ](https://github.com/ros2/rclcpp/issues/3124)_)
* fix: Compile fix for MSVC 2022 ([#3131 ](https://github.com/ros2/rclcpp/issues/3131)_)
* Remove warnings on tests ([#3125 ](https://github.com/ros2/rclcpp/issues/3125)_)
* feat: Add per-node log level support via NodeOptions ([#3092 ](https://github.com/ros2/rclcpp/issues/3092)_)
* Improve error message when parameter value is missing ([#3093 ](https://github.com/ros2/rclcpp/issues/3093)_)
* Fix incorrect internal clear inside [`RingBufferImplementation`` (`#3116 ](https://github.com/ros2/rclcpp/issues/3116)_)
* Add acceptable_buffer_backends field in SubscriptionOptionsBase ([#3098 ](https://github.com/ros2/rclcpp/issues/3098)_)
* Remove comment about removed StaticSingleThreadedExecutor ([#3121 ](https://github.com/ros2/rclcpp/issues/3121)_)
* Added tracepoint ([#3103 ](https://github.com/ros2/rclcpp/issues/3103)_)
* Add ConstRefCallback in take_shared_method ([#3066 ](https://github.com/ros2/rclcpp/issues/3066)_)
* Replace mispelled "${rcl_interfaces_TARGES}" by rcl_interfaces::rcl_interfaces ([#3112 ](https://github.com/ros2/rclcpp/issues/3112)_)
* Use new ROSIDL aggregate CMake target ([#3105 ](https://github.com/ros2/rclcpp/issues/3105)_)
* remove duplicate test cases in TestAnySubscriptionCallback::is_serialized_message_callback ([#3104 ](https://github.com/ros2/rclcpp/issues/3104)_)
* keep the event alive throught the assertion, preveiting the race. ([#3099 ](https://github.com/ros2/rclcpp/issues/3099)_)
* Add support check for content filter feature in subscription ([#3089 ](https://github.com/ros2/rclcpp/issues/3089)_)
* Expose ServiceType in Service public API ([#3088 ](https://github.com/ros2/rclcpp/issues/3088)_)
* perf: Optimized out shared_ptr copies ([#3079 ](https://github.com/ros2/rclcpp/issues/3079)_)
* avoid stale parameter events in content filter tests. ([#3085 ](https://github.com/ros2/rclcpp/issues/3085)_)
* improve lookup time for matches_any_publishers() ([#3084 ](https://github.com/ros2/rclcpp/issues/3084)_)
* Add tests isolation ([#3081 ](https://github.com/ros2/rclcpp/issues/3081)_)
* Revert "improve lookup time for matches_any_publishers(). ([#3068 ](https://github.com/ros2/rclcpp/issues/3068)_)" ([#3077 ](https://github.com/ros2/rclcpp/issues/3077)_)
* improve lookup time for matches_any_publishers(). ([#3068 ](https://github.com/ros2/rclcpp/issues/3068)_)
* fix: Use default rcl allocator if allocator is std::allocator ([#3058 ](https://github.com/ros2/rclcpp/issues/3058)_)
* fix: Various data races in test cases ([#3057 ](https://github.com/ros2/rclcpp/issues/3057)_)
* fix: Fix data race in CallbackGroup::size() ([#3056 ](https://github.com/ros2/rclcpp/issues/3056)_)
* remove default: so that compiler can detect the missing case. ([#3048 ](https://github.com/ros2/rclcpp/issues/3048)_)
* use weak_ptr for rcl entities in the memory strategy. ([#2988 ](https://github.com/ros2/rclcpp/issues/2988)_)
* remove test_static_executor_entities_collector.cpp ([#3041 ](https://github.com/ros2/rclcpp/issues/3041)_)
* include the 1st spin that might throw the exception. ([#3042 ](https://github.com/ros2/rclcpp/issues/3042)_)
* print warning message on owner node if the parameter operation fails. ([#3037 ](https://github.com/ros2/rclcpp/issues/3037)_)
* fix context in wait for message wait set ([#3030 ](https://github.com/ros2/rclcpp/issues/3030)_)
* Revert "construct wait set with passed in context ([#3021 ](https://github.com/ros2/rclcpp/issues/3021)_)" ([#3028 ](https://github.com/ros2/rclcpp/issues/3028)_)
* construct wait set with passed in context ([#3021 ](https://github.com/ros2/rclcpp/issues/3021)_)
* Improve the robustness of the TopicEndpointInfo constructor ([#3013 ](https://github.com/ros2/rclcpp/issues/3013)_)
* Deprecate the shared_ptr<MessageT> subscription callback signatures ([#2975 ](https://github.com/ros2/rclcpp/issues/2975)_)
* Updated deprecated ament_index_cpp API ([#3011 ](https://github.com/ros2/rclcpp/issues/3011)_)
* Unified Node Interfaces: Add const version of get_node_x_interface() ([#3006 ](https://github.com/ros2/rclcpp/issues/3006)_)
* Parameter Descriptor Simplification  ([#2179 ](https://github.com/ros2/rclcpp/issues/2179)_)
* ParameterEventHandler support ContentFiltering ([#2971 ](https://github.com/ros2/rclcpp/issues/2971)_)
* update policy_name_from_kind && test_qos ([#2156 ](https://github.com/ros2/rclcpp/issues/2156)_)
* Add ability to disable and enable subscription's callbacks ([#2985 ](https://github.com/ros2/rclcpp/issues/2985)_)
* Switch to isolated testing via rmw_test_fixture ([#2929 ](https://github.com/ros2/rclcpp/issues/2929)_)
* remove I/O from signal handler. ([#2986 ](https://github.com/ros2/rclcpp/issues/2986)_)
* correct test function descriptions ([#2970 ](https://github.com/ros2/rclcpp/issues/2970)_)
* add : get clients, servers info ([#2569 ](https://github.com/ros2/rclcpp/issues/2569)_)
* Fix REP url locations ([#2987 ](https://github.com/ros2/rclcpp/issues/2987)_)
* clear handles before node destruction in test_memory_strategy. ([#2969 ](https://github.com/ros2/rclcpp/issues/2969)_)
* Added static assert asserting custom types have no overloaded operator new ([#2954 ](https://github.com/ros2/rclcpp/issues/2954)_)
* Store graph listener inside the context instead of the node graph ([#2952 ](https://github.com/ros2/rclcpp/issues/2952)_)
* Reapply "Catch the exception from rate.sleep() if the context is invalid. ([#2956 ](https://github.com/ros2/rclcpp/issues/2956)_)" ([#2963 ](https://github.com/ros2/rclcpp/issues/2963)_) ([#2964 ](https://github.com/ros2/rclcpp/issues/2964)_)
* Revert "Catch the exception from rate.sleep() if the context is invalid. ([#2956 ](https://github.com/ros2/rclcpp/issues/2956)_)" ([#2963 ](https://github.com/ros2/rclcpp/issues/2963)_)
* Catch the exception from rate.sleep() if the context is invalid. ([#2956 ](https://github.com/ros2/rclcpp/issues/2956)_)
* update Time documentation ([#2955 ](https://github.com/ros2/rclcpp/issues/2955)_)
* Removed warning ([#2949 ](https://github.com/ros2/rclcpp/issues/2949)_)
* add note about problems with spin_until_future_complete ([#2849 ](https://github.com/ros2/rclcpp/issues/2849)_)
* deprecate rclcpp::spin_some and rclcpp::spin_all ([#2848 ](https://github.com/ros2/rclcpp/issues/2848)_)
* Improve the function extract_type_identifier ([#2923 ](https://github.com/ros2/rclcpp/issues/2923)_)
* Allow for implicitly convertable loggers as well ([#2922 ](https://github.com/ros2/rclcpp/issues/2922)_)
* Fix: improve exception context for parameter_value_from ([#2917 ](https://github.com/ros2/rclcpp/issues/2917)_)
* Fix [`start_type_description_service`` param handling (`#2897 ](https://github.com/ros2/rclcpp/issues/2897)_)
* Add qos parameter for wait_for_message function ([#2903 ](https://github.com/ros2/rclcpp/issues/2903)_)
* Fujitatomoya/test append parameter override ([#2896 ](https://github.com/ros2/rclcpp/issues/2896)_)
* Expose [`typesupport_helpers`` API needed for the Rosbag2 (`#2858 ](https://github.com/ros2/rclcpp/issues/2858)_)
* Remove comment about now-removed StaticSingleThreadedExecutor ([#2893 ](https://github.com/ros2/rclcpp/issues/2893)_)
* Add overload of [`append_parameter_override`` (`#2891 ](https://github.com/ros2/rclcpp/issues/2891)_)
* fix: Don't deadlock if removing shutdown callbacks in a shutdown callback ([#2886 ](https://github.com/ros2/rclcpp/issues/2886)_)
* Hand-code logging.hpp ([#2870 ](https://github.com/ros2/rclcpp/issues/2870)_)
* Adressed TODO in node_graph ([#2877 ](https://github.com/ros2/rclcpp/issues/2877)_)
* fix test_publisher_with_system_default_qos. ([#2881 ](https://github.com/ros2/rclcpp/issues/2881)_)
* Fix for memory leaks in rclcpp::SerializedMessage ([#2861 ](https://github.com/ros2/rclcpp/issues/2861)_)
* Removed warning test_qos ([#2859 ](https://github.com/ros2/rclcpp/issues/2859)_)
* Added missing chrono includes ([#2854 ](https://github.com/ros2/rclcpp/issues/2854)_)
* get_all_data_impl() does not handle null pointers properly, causing segmentation fault ([#2840 ](https://github.com/ros2/rclcpp/issues/2840)_)
* QoSInitialization::from_rmw does not validate invalid history policy values, leading to silent failures ([#2841 ](https://github.com/ros2/rclcpp/issues/2841)_)
* remove get_notify_guard_condition from NodeBaseInterface. ([#2839 ](https://github.com/ros2/rclcpp/issues/2839)_)
* Removed deprecated StaticSingleThreadedExecutor ([#2835 ](https://github.com/ros2/rclcpp/issues/2835)_)
* Removed deprecated rcpputils Path ([#2834 ](https://github.com/ros2/rclcpp/issues/2834)_)
* Add range constraints for applicable array parameters ([#2828 ](https://github.com/ros2/rclcpp/issues/2828)_)
* Update RingBufferImplementation to clear internal data. ([#2837 ](https://github.com/ros2/rclcpp/issues/2837)_)
* Removed deprecated cancel_sleep_or_wait ([#2836 ](https://github.com/ros2/rclcpp/issues/2836)_)
* Add missing 's' to 'NodeParametersInterface' in doc/comment ([#2831 ](https://github.com/ros2/rclcpp/issues/2831)_)
* subordinate node consistent behavior and update docstring. ([#2822 ](https://github.com/ros2/rclcpp/issues/2822)_)
* throws std::invalid_argument if ParameterEvent is NULL. ([#2814 ](https://github.com/ros2/rclcpp/issues/2814)_)
* Removed clang warnings ([#2823 ](https://github.com/ros2/rclcpp/issues/2823)_)
* Contributors: Alberto Soragna, Alejandro Hernández Cordero, Alex Youngs, Alexis Tsogias, Andrianov Roman, Barry Xu, CY Chen, Chris Lalancette, Christophe Bedard, Danil, Emerson Knapp, Ilario A. Azzollini, Ivo Ivanov, Janosch Machowinski, Julien Enoch, Lee, Lucas Wendland, Maurice Alexander Purnawan, Michael Carlstrom, Michael Carroll, Michael Orlov, Michiel Leegwater, Minju, Oren Bell, Patrick Roncagliolo, Peng Wang, Rahat Dhande, Skyler Medeiros, Sriharsha Ghanta, Tim Clephas, Tomoya Fujita, Yadnyeshwar Amol Sakhare, Yuchen966, fabianhirmann, jay, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp_action <https://github.com/ros2/rclcpp/tree/lyrical/rclcpp_action/CHANGELOG.rst>`__

* publish_feedback should effect only on executing state. ([#3118 ](https://github.com/ros2/rclcpp/issues/3118)_)
* Support to configure feedback subscription content filter for action client ([#3034 ](https://github.com/ros2/rclcpp/issues/3034)_)
* Use new ROSIDL aggregate CMake target ([#3105 ](https://github.com/ros2/rclcpp/issues/3105)_)
* Fix expiration of action goals when EventsExecutors are used ([#3018 ](https://github.com/ros2/rclcpp/issues/3018)_)
* perf: Optimized out shared_ptr copies ([#3079 ](https://github.com/ros2/rclcpp/issues/3079)_)
* remove default: so that compiler can detect the missing case. ([#3048 ](https://github.com/ros2/rclcpp/issues/3048)_)
* Update exception documentation for goal cancellation in ServerGoalHandle ([#3019 ](https://github.com/ros2/rclcpp/issues/3019)_)
* Fix REP url locations ([#2987 ](https://github.com/ros2/rclcpp/issues/2987)_)
* it misses the iterator second to lock the weakptr. ([#2958 ](https://github.com/ros2/rclcpp/issues/2958)_)
* try aborting before canceling 1st on dtor of ServerGoalHandle. ([#2953 ](https://github.com/ros2/rclcpp/issues/2953)_)
* deprecate rclcpp::spin_some and rclcpp::spin_all ([#2848 ](https://github.com/ros2/rclcpp/issues/2848)_)
* fix cmake deprecation ([#2914 ](https://github.com/ros2/rclcpp/issues/2914)_)
* Replace std::default_random_engine with std::mt19937 (rolling) ([#2843 ](https://github.com/ros2/rclcpp/issues/2843)_)
* Added missing chrono includes ([#2854 ](https://github.com/ros2/rclcpp/issues/2854)_)
* Contributors: Alberto Soragna, Alejandro Hernández Cordero, Andrei Costinescu, Barry Xu, Emerson Knapp, Janosch Machowinski, Skyler Medeiros, Tim Clephas, Tomoya Fujita, keeponoiro, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp_components <https://github.com/ros2/rclcpp/tree/lyrical/rclcpp_components/CHANGELOG.rst>`__

* Refactor component containers + Add option for CBG Executor ([#3134 ](https://github.com/ros2/rclcpp/issues/3134)_)
* feat: Add per-node log level support via NodeOptions ([#3092 ](https://github.com/ros2/rclcpp/issues/3092)_)
* Use new ROSIDL aggregate CMake target ([#3105 ](https://github.com/ros2/rclcpp/issues/3105)_)
* Avoid unecessary creation of MultiThreadedExecutor ([#3090 ](https://github.com/ros2/rclcpp/issues/3090)_)
* Fix component registering in subdirectories ([#3064 ](https://github.com/ros2/rclcpp/issues/3064)_)
* Add library dependency to node executable in rclcpp_components_register_node ([#3047 ](https://github.com/ros2/rclcpp/issues/3047)_)
* Updated deprecated ament_index_cpp API ([#3011 ](https://github.com/ros2/rclcpp/issues/3011)_)
* Fix REP url locations ([#2987 ](https://github.com/ros2/rclcpp/issues/2987)_)
* Cleanup the dependencies in rclcpp_components. ([#2918 ](https://github.com/ros2/rclcpp/issues/2918)_)
* fix cmake deprecation ([#2914 ](https://github.com/ros2/rclcpp/issues/2914)_)
* NEW PR: Add component_container for EventsExecutor ([#2885 ](https://github.com/ros2/rclcpp/issues/2885)_)
* make sure that plugin arg includes the double colon. ([#2878 ](https://github.com/ros2/rclcpp/issues/2878)_)
* set thread names by node in component container isolated ([#2871 ](https://github.com/ros2/rclcpp/issues/2871)_)
* Added missing chrono includes ([#2854 ](https://github.com/ros2/rclcpp/issues/2854)_)
* Contributors: Adam Aposhian, Alejandro Hernández Cordero, Chris Lalancette, Emerson Knapp, Mihir Rao, Peng Wang, Skyler Medeiros, Tim Clephas, Tomoya Fujita, YuJin Hong, mosfet80, pum1k, solo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp_lifecycle <https://github.com/ros2/rclcpp/tree/lyrical/rclcpp_lifecycle/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#3105 ](https://github.com/ros2/rclcpp/issues/3105)_)
* Compatiblity with 'Populate Transitions' [ros2/rcl#1269 ](https://github.com/ros2/rcl/issues/1269)_ ([#2967 ](https://github.com/ros2/rclcpp/issues/2967)_)
* add : get clients, servers info ([#2569 ](https://github.com/ros2/rclcpp/issues/2569)_)
* Fix REP url locations ([#2987 ](https://github.com/ros2/rclcpp/issues/2987)_)
* Add get_parameter_or overload returning value or alternative ([#2973 ](https://github.com/ros2/rclcpp/issues/2973)_)
* deprecate rclcpp::spin_some and rclcpp::spin_all ([#2848 ](https://github.com/ros2/rclcpp/issues/2848)_)
* Clearer warning message, the old one lacked information and was perhaps misleading ([#2927 ](https://github.com/ros2/rclcpp/issues/2927)_)
* fix cmake deprecation ([#2914 ](https://github.com/ros2/rclcpp/issues/2914)_) cmake version < then 3.10 is deprecated
* Added missing chrono includes ([#2854 ](https://github.com/ros2/rclcpp/issues/2854)_)
* introduce rcl_lifecycle_get_transition_label_by_id(). ([#2827 ](https://github.com/ros2/rclcpp/issues/2827)_)
* Contributors: Alberto Soragna, Alejandro Hernández Cordero, Emerson Knapp, Jasper van Brakel, Lee, Minju, Peter Mitrano (AR), Tim Clephas, Tomoya Fujita, Zheng Qu, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclpy <https://github.com/ros2/rclpy/tree/lyrical/rclpy/CHANGELOG.rst>`__

* Feature: async node ([#1620 ](https://github.com/ros2/rclpy/issues/1620)_)
* Refactor: moved TypeDescriptionService, LoggingService, ParameterService to BaseNode ([#1645 ](https://github.com/ros2/rclpy/issues/1645)_)
* Refactor: base node ([#1637 ](https://github.com/ros2/rclpy/issues/1637)_)
* Bugfix: executor doesn't propagate exception from task that awaited a future ([#1643 ](https://github.com/ros2/rclpy/issues/1643)_)
* Fix: disable flaky executor test ([#1648 ](https://github.com/ros2/rclpy/issues/1648)_) ([#1649 ](https://github.com/ros2/rclpy/issues/1649)_)
* Streamline entity destroy ([#1629 ](https://github.com/ros2/rclpy/issues/1629)_)
* Add acceptable_buffer_backends as subscription option in rclpy ([#1628 ](https://github.com/ros2/rclpy/issues/1628)_)
* publish_feedback should effect only on executing state. ([#1639 ](https://github.com/ros2/rclpy/issues/1639)_)
* Support to configure feedback subscription content filter for action client ([#1633 ](https://github.com/ros2/rclpy/issues/1633)_)
* fix flaky test_multi_threaded_executor_closes_threads. ([#1636 ](https://github.com/ros2/rclpy/issues/1636)_)
* Fix violation ([#1635 ](https://github.com/ros2/rclpy/issues/1635)_)
* Fix test_executor types ([#1632 ](https://github.com/ros2/rclpy/issues/1632)_)
* Refactor: base clock ([#1627 ](https://github.com/ros2/rclpy/issues/1627)_)
* Fix future flake8 ([#1634 ](https://github.com/ros2/rclpy/issues/1634)_)
* Use new ROSIDL aggregate CMake target ([#1630 ](https://github.com/ros2/rclpy/issues/1630)_)
* Update type hints for parameters ([#1631 ](https://github.com/ros2/rclpy/issues/1631)_)
* Add support check for content filter feature in subscription ([#1618 ](https://github.com/ros2/rclpy/issues/1618)_)
* Refactor: base entity classes ([#1624 ](https://github.com/ros2/rclpy/issues/1624)_)
* Fix more test typings and remove unused type aliases ([#1626 ](https://github.com/ros2/rclpy/issues/1626)_)
* Add types to test_waitable ([#1625 ](https://github.com/ros2/rclpy/issues/1625)_)
* Correct typos ([#1619 ](https://github.com/ros2/rclpy/issues/1619)_)
* Fix incorrect action client/server callback type hints ([#1616 ](https://github.com/ros2/rclpy/issues/1616)_)
* avoid stale parameter events in content filter tests. ([#1615 ](https://github.com/ros2/rclpy/issues/1615)_)
* fix violations ([#1614 ](https://github.com/ros2/rclpy/issues/1614)_)
* Typing Regression Fixes ([#1612 ](https://github.com/ros2/rclpy/issues/1612)_)
* CFT is only supported rmw_fastrtps and rmw_connextdds. ([#1611 ](https://github.com/ros2/rclpy/issues/1611)_)
* Prevents the Future result from being set twice. ([#1599 ](https://github.com/ros2/rclpy/issues/1599)_)
* Wrap up ActionClient construction before spining ([#1591 ](https://github.com/ros2/rclpy/issues/1591)_)
* Compatiblity with 'Populate Transitions' [ros2/rcl#1269 ](https://github.com/ros2/rcl/issues/1269)_ ([#1528 ](https://github.com/ros2/rclpy/issues/1528)_)
* Drop invalid waitables from wait set ([#1590 ](https://github.com/ros2/rclpy/issues/1590)_)
* give some time for the discovery for test_on_new_message_callback. ([#1585 ](https://github.com/ros2/rclpy/issues/1585)_)
* print warning message on owner node if the parameter operation fails. ([#1584 ](https://github.com/ros2/rclpy/issues/1584)_)
* Update release version to 10.0.4 ([#1583 ](https://github.com/ros2/rclpy/issues/1583)_)
* Update [`type_support.py`` to use new message abstract base classes  (`#1509 ](https://github.com/ros2/rclpy/issues/1509)_)
* Fix performance bug in MultiThreadedExecutor (hopefully) ([#1547 ](https://github.com/ros2/rclpy/issues/1547)_)
* Expose action graph functions as Node class methods. ([#1574 ](https://github.com/ros2/rclpy/issues/1574)_)
* Improve wildcard parsing and optimize the logic for parsing YAML para… ([#1571 ](https://github.com/ros2/rclpy/issues/1571)_)
* Improve the compatibility of processing YAML parameter files ([#1548 ](https://github.com/ros2/rclpy/issues/1548)_)
* Fix parameter parsing for unspecified target nodes ([#1552 ](https://github.com/ros2/rclpy/issues/1552)_)
* Remove default from switch with enum, so that compiler warns. ([#1566 ](https://github.com/ros2/rclpy/issues/1566)_)
* Use unconditional wait when possible. ([#1563 ](https://github.com/ros2/rclpy/issues/1563)_)
* Increase clock accuracy ([#1564 ](https://github.com/ros2/rclpy/issues/1564)_)
* Fix issues with resuming async tasks awaiting a future ([#1469 ](https://github.com/ros2/rclpy/issues/1469)_)
* ParameterEventHandler support ContentFiltering ([#1531 ](https://github.com/ros2/rclpy/issues/1531)_)
* add : get clients, servers info ([#1307 ](https://github.com/ros2/rclpy/issues/1307)_)
* Allow action servers without execute callback ([#1219 ](https://github.com/ros2/rclpy/issues/1219)_)
* Remove accidental tuple ([#1542 ](https://github.com/ros2/rclpy/issues/1542)_)
* fix(test_events_executor): destroy all nodes before shutdown ([#1538 ](https://github.com/ros2/rclpy/issues/1538)_)
* Remove duplicate future handling from send_goal_async ([#1532 ](https://github.com/ros2/rclpy/issues/1532)_)
* remove unused 'param_type' ([#1524 ](https://github.com/ros2/rclpy/issues/1524)_)
* Fixes Action.*_async futures never complete ([#1308 ](https://github.com/ros2/rclpy/issues/1308)_)
* add spinning state for the Executor classes. ([#1510 ](https://github.com/ros2/rclpy/issues/1510)_)
* EventsExecutor: Handle async callbacks for services and subscriptions ([#1478 ](https://github.com/ros2/rclpy/issues/1478)_)
* Added lock to protect futures for multithreaded executor ([#1477 ](https://github.com/ros2/rclpy/issues/1477)_)
* Add content-filtered-topic interfaces ([#1506 ](https://github.com/ros2/rclpy/issues/1506)_)
* Fix warnings from gcc. ([#1501 ](https://github.com/ros2/rclpy/issues/1501)_)
* Feature: expose event callback setter in subscription, service, client and timer ([#1496 ](https://github.com/ros2/rclpy/issues/1496)_)
* Feature: add executor.create_future() ([#1495 ](https://github.com/ros2/rclpy/issues/1495)_)
* Add More Test Typings ([#1472 ](https://github.com/ros2/rclpy/issues/1472)_)
* Use pybind11 from deb or pixi ([#1497 ](https://github.com/ros2/rclpy/issues/1497)_)
* Do not execute the timer if call_timer_with_info() fails ([#1488 ](https://github.com/ros2/rclpy/issues/1488)_)
* Fix msbuild warnings on [`operator==`` deprecation for pybind11 >=2.2 (`#1483 ](https://github.com/ros2/rclpy/issues/1483)_)
* Cleanup the rclpy dependencies. ([#1482 ](https://github.com/ros2/rclpy/issues/1482)_)
* Feature: add logger_name property to subscription, publisher, service and client ([#1471 ](https://github.com/ros2/rclpy/issues/1471)_)
* Update [`test_node`` Types (`#1464 ](https://github.com/ros2/rclpy/issues/1464)_)
* Add method that get datetime.datetime from Time ([#1443 ](https://github.com/ros2/rclpy/issues/1443)_)
* add [`MessageInfo.publisher_gid`` (`#1466 ](https://github.com/ros2/rclpy/issues/1466)_)
* Add types to [`test_action\_\*.py`` (`#1444 ](https://github.com/ros2/rclpy/issues/1444)_)
* Revert "Fix Duration, Clock, and QoS Docs ([#1428 ](https://github.com/ros2/rclpy/issues/1428)_)" ([#1447 ](https://github.com/ros2/rclpy/issues/1447)_)
* remove all deprecated classes and methods ([#1456 ](https://github.com/ros2/rclpy/issues/1456)_)
* [rclpy] Fix spin() incorrectly removing node from executor if already attached ([#1446 ](https://github.com/ros2/rclpy/issues/1446)_)
* Contributors: Alejandro Hernández Cordero, Alon Borenshtein, Auguste Lalande, Barry Xu, Brad Martin, Brennan Miller-Klugman, Błażej Sowa, CY Chen, Chris Lalancette, Christian Rauch, Clara Berendsen, Emerson Knapp, Florian Vahl, Jasper van Brakel, Jean Paul, Jonathan, Lee, Michael Carlstrom, Michael Tandy, Minju, Nadav Elkabets, Nathan Wiebe Neufeldt, Tim Clephas, Tomoya Fujita, Yuyuan Yuan, mhidalgo-rai


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcpputils <https://github.com/ros2/rcpputils/tree/lyrical/CHANGELOG.rst>`__

* Updated note related with tl_expected ([#229 ](https://github.com/ros2/rcpputils/issues/229)_)
* Increase test coverage ([#222 ](https://github.com/ros2/rcpputils/issues/222)_)
* Append copies of BSD and CC0 licenses from the works ([#223 ](https://github.com/ros2/rcpputils/issues/223)_)
* Use std::filesystem in find_library and add more test ([#221 ](https://github.com/ros2/rcpputils/issues/221)_)
* Remove -Werror from Clang compile options ([#220 ](https://github.com/ros2/rcpputils/issues/220)_)
* Remove unnecessary dependencies from rcpputils. ([#216 ](https://github.com/ros2/rcpputils/issues/216)_) It doesn't need to have dependencies on python tests.
* fix cmake deprecation ([#214 ](https://github.com/ros2/rcpputils/issues/214)_)
* add thread naming utilities ([#213 ](https://github.com/ros2/rcpputils/issues/213)_)
* Removed deprecated path ([#212 ](https://github.com/ros2/rcpputils/issues/212)_)
* Contributors: Adam Aposhian, Alejandro Hernández Cordero, Chris Lalancette, Tully Foote, William Woodall, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcutils <https://github.com/ros2/rcutils/tree/lyrical/CHANGELOG.rst>`__

* Add buildtool_export_depend on ament_cmake_ros_core ([#558 ](https://github.com/ros2/rcutils/issues/558)_)
* fix: typo in parameter documentation for overwrite ([#557 ](https://github.com/ros2/rcutils/issues/557)_)
* Remove ATOMIC_VAR_INIT ([#556 ](https://github.com/ros2/rcutils/issues/556)_)
* Use [`ament_set_default_language_standards`` from ``ament_cmake_core`` (`#548 ](https://github.com/ros2/rcutils/issues/548)_)
* Use uncommon variable name in macro to avoid being overwritten ([#551 ](https://github.com/ros2/rcutils/issues/551)_)
* Remove [`ament_export_link_flags()`` for atomic operations (`#528 ](https://github.com/ros2/rcutils/issues/528)_)
* Use less common variable name in macro ([#550 ](https://github.com/ros2/rcutils/issues/550)_)
* Fix missing include for std::get_time ([#549 ](https://github.com/ros2/rcutils/issues/549)_)
* Fix gcc 15.2.1 warning for discarding 'const' qualifier ([#547 ](https://github.com/ros2/rcutils/issues/547)_)
* Disable warning C5105 for older Windows SDKs in base64.c ([#544 ](https://github.com/ros2/rcutils/issues/544)_)
* Add {short_file_name} as log format option ([#541 ](https://github.com/ros2/rcutils/issues/541)_)
* Add base64 encoding and decoding functions with tests ([#533 ](https://github.com/ros2/rcutils/issues/533)_)
* remove default: so that compiler can detect the missing case. ([#534 ](https://github.com/ros2/rcutils/issues/534)_)
* Check SIZE_MAX for array initialization. ([#527 ](https://github.com/ros2/rcutils/issues/527)_)
* Do not export dl in rcutils_LIBRARIES ([#522 ](https://github.com/ros2/rcutils/issues/522)_)
* rcutils_logging_allocator_initialize() support. ([#419 ](https://github.com/ros2/rcutils/issues/419)_)
* Export -latomic even if BUILD_TESTING is disabled. ([#516 ](https://github.com/ros2/rcutils/issues/516)_)
* Add rcutils_raw_steady_time_now method for slew-free clock ([#507 ](https://github.com/ros2/rcutils/issues/507)_)
* Revert "use getenv_s instead of getenv for Windows. ([#499 ](https://github.com/ros2/rcutils/issues/499)_)" ([#504 ](https://github.com/ros2/rcutils/issues/504)_) This reverts commit 46ab4d4eeb555a2e9e880157b97f0a867d3a256c.
* Hand-code logging_macros.h ([#502 ](https://github.com/ros2/rcutils/issues/502)_)
* Implement rcutils_strnlen. ([#430 ](https://github.com/ros2/rcutils/issues/430)_)
* use getenv_s instead of getenv for Windows. ([#499 ](https://github.com/ros2/rcutils/issues/499)_)
* Make linters happy
* Clean memory in test_process.cpp ([#495 ](https://github.com/ros2/rcutils/issues/495)_)
* Contributors: Alejandro Hernández Cordero, Andrei Kholodnyi, Barry Xu, Chris Lalancette, EddyGharib, Miguel Company, Sai Kishor Kothakota, Shane Loretz, Tomoya Fujita, Tony Najjar


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `resource_retriever <https://github.com/ros/resource_retriever/tree/lyrical/resource_retriever/CHANGELOG.rst>`__

* Removed python2 code ([#121 ](https://github.com/ros/resource_retriever/issues/121)_)
* Delete resource_retriever/setup.py ([#120 ](https://github.com/ros/resource_retriever/issues/120)_)
* Use get_package_share_path ([#119 ](https://github.com/ros/resource_retriever/issues/119)_)
* Updated deprecated ament_index_cpp API ([#118 ](https://github.com/ros/resource_retriever/issues/118)_)
* removed libcurl_vendor package ([#116 ](https://github.com/ros/resource_retriever/issues/116)_)
* Removed deprecated code ([#113 ](https://github.com/ros/resource_retriever/issues/113)_)
* Fixed clang compile error ([#112 ](https://github.com/ros/resource_retriever/issues/112)_)
* Removed windows warnings ([#111 ](https://github.com/ros/resource_retriever/issues/111)_)
* Add a plugin mechanism to resource_retriever ([#103 ](https://github.com/ros/resource_retriever/issues/103)_)
* uniform  MinCMakeVersion ([#108 ](https://github.com/ros/resource_retriever/issues/108)_)
* Contributors: Alejandro Hernández Cordero, Michael Carlstrom, Michael Carroll, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `resource_retriever_interfaces <https://github.com/ros2/resource_retriever_service/tree/lyrical/resource_retriever_interfaces/CHANGELOG.rst>`__

* Update the plugin license ([#17 ](https://github.com/ros2/resource_retriever_service/issues/17)_)
* Contributors: Stoyan Gaydarov


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `resource_retriever_service <https://github.com/ros2/resource_retriever_service/tree/lyrical/resource_retriever_service/CHANGELOG.rst>`__

* Update the plugin license ([#17 ](https://github.com/ros2/resource_retriever_service/issues/17)_)
* Contributors: Stoyan Gaydarov


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `resource_retriever_service_plugin <https://github.com/ros2/resource_retriever_service/tree/lyrical/resource_retriever_service_plugin/CHANGELOG.rst>`__

* Update the plugin license ([#17 ](https://github.com/ros2/resource_retriever_service/issues/17)_)
* Contributors: Stoyan Gaydarov


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw <https://github.com/ros2/rmw/tree/lyrical/rmw/CHANGELOG.rst>`__

* find_package ament_cmake_gtest ([#417 ](https://github.com/ros2/rmw/issues/417)_)
* Add acceptable_buffer_backends field in rmw_subscription_options_s ([#416 ](https://github.com/ros2/rmw/issues/416)_)
* Add is_cft_supported field to rmw_subscription_t for content filtering support ([#415 ](https://github.com/ros2/rmw/issues/415)_)
* Remove default from switch with enum, so that compiler warns. ([#414 ](https://github.com/ros2/rmw/issues/414)_)
* add: get clients, servers info ([#371 ](https://github.com/ros2/rmw//issues/371)_)
* Fix REP url locations ([#406 ](https://github.com/ros2/rmw//issues/406)_)
* Update link to rmw API docs ([#405 ](https://github.com/ros2/rmw//issues/405)_)
* Don't assume a DDS-based implementation in function docs ([#402 ](https://github.com/ros2/rmw//issues/402)_)
* Contributors: Barry Xu, CY Chen, Christophe Bedard, Lee, Minju, Shane Loretz, Tim Clephas, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_connextdds <https://github.com/ros2/rmw_connextdds/tree/lyrical/rmw_connextdds/CHANGELOG.rst>`__

* fix: Fixed compilation on MSVC 2022 ([#225 ](https://github.com/ros2/rmw_connextdds/issues/225)_)
* Remove default from switch with enum to enable compiler warnings ([#216 ](https://github.com/ros2/rmw_connextdds/issues/216)_)
* add : get clients,servers info ([#154 ](https://github.com/ros2/rmw_connextdds/issues/154)_)
* fix: remove superflous [`buildtool_export_depend`` (`#206 ](https://github.com/ros2/rmw_connextdds/issues/206)_)
* Fix cmake deprecation ([#198 ](https://github.com/ros2/rmw_connextdds/issues/198)_)
* Contributors: Bas Zalmstra, Janosch Machowinski, Lee, Minju, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_connextdds_common <https://github.com/ros2/rmw_connextdds/tree/lyrical/rmw_connextdds_common/CHANGELOG.rst>`__

* Fix content filtering on Windows with modern Connext DDS ([#226 ](https://github.com/ros2/rmw_connextdds/issues/226)_) ([#230 ](https://github.com/ros2/rmw_connextdds/issues/230)_)
* fix: Fixed compilation on MSVC 2022 ([#225 ](https://github.com/ros2/rmw_connextdds/issues/225)_)
* Add variable [`RMW_CONNEXT_USER_TOPICS_PUBLISH_MODE`` and deprecate ``RMW_CONNEXT_USE_DEFAULT_PUBLISH_MODE`` (`#224 ](https://github.com/ros2/rmw_connextdds/issues/224)_)
* Update Connext from 7.3.0 to 7.7.0, disable monitoring library by default, and use synchronous publishing mode ([#219 ](https://github.com/ros2/rmw_connextdds/issues/219)_)
* Enable property [`dds.ros.demangle_topic_and_type_names`` to announce demangled topic name as topic alias (`#221 ](https://github.com/ros2/rmw_connextdds/issues/221)_)
* Enable content filtering flag ([#223 ](https://github.com/ros2/rmw_connextdds/issues/223)_)
* Remove deprecated security properties and use new ones ([#217 ](https://github.com/ros2/rmw_connextdds/issues/217)_)
* Remove default from switch with enum to enable compiler warnings ([#216 ](https://github.com/ros2/rmw_connextdds/issues/216)_)
* Replace [`DDS_ContentFilter_register_filter`` with ``DDS_DomainParticipant_register_contentfilterI`` (`#215 ](https://github.com/ros2/rmw_connextdds/issues/215)_)
* Remove superfluous [`buildtool_export_depend`` (`#210 ](https://github.com/ros2/rmw_connextdds/issues/210)_)
* add : get clients,servers info ([#154 ](https://github.com/ros2/rmw_connextdds/issues/154)_)
* [rmw_connextdds_common]: Remove <member_of_group>rosidl_interface_packages ([#202 ](https://github.com/ros2/rmw_connextdds/issues/202)_)
* Correctly calculate the size of a serialized key ([#200 ](https://github.com/ros2/rmw_connextdds/issues/200)_)
* Fix cmake deprecation ([#198 ](https://github.com/ros2/rmw_connextdds/issues/198)_)
* Fixed serialized minimum sample size callback ([#196 ](https://github.com/ros2/rmw_connextdds/issues/196)_)
* Removed warning ([#187 ](https://github.com/ros2/rmw_connextdds/issues/187)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Chris Lalancette, Francisco Gallego Salido, Janosch Machowinski, Lee, Minju, Tomoya Fujita, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_connextddsmicro <https://github.com/ros2/rmw_connextdds/tree/lyrical/rmw_connextddsmicro/CHANGELOG.rst>`__

* fix: Fixed compilation on MSVC 2022 ([#225 ](https://github.com/ros2/rmw_connextdds/issues/225)_)
* Remove default from switch with enum to enable compiler warnings ([#216 ](https://github.com/ros2/rmw_connextdds/issues/216)_)
* Remove superfluous [`buildtool_export_depend`` (`#210 ](https://github.com/ros2/rmw_connextdds/issues/210)_)
* add : get clients,servers info ([#154 ](https://github.com/ros2/rmw_connextdds/issues/154)_)
* Fix cmake deprecation ([#198 ](https://github.com/ros2/rmw_connextdds/issues/198)_)
* Contributors: Janosch Machowinski, Lee, Minju, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_cyclonedds_cpp <https://github.com/ros2/rmw_cyclonedds/tree/lyrical/rmw_cyclonedds_cpp/CHANGELOG.rst>`__

* Silence unused variable warning in Release builds ([#580 ](https://github.com/ros2/rmw_cyclonedds/issues/580)_)
* Add key support and update Cyclone DDS compatibility ([#575 ](https://github.com/ros2/rmw_cyclonedds/issues/575)_)
* Explicitly disable content filtering support ([#574 ](https://github.com/ros2/rmw_cyclonedds/issues/574)_)
* Add tracepoint to [`rmw_take_loan_int`` (`#566 ](https://github.com/ros2/rmw_cyclonedds/issues/566)_)
* Fix warnings about [`may be used uninitialized`` (`#573 ](https://github.com/ros2/rmw_cyclonedds/issues/573)_)
* Improve MessageTypeSupport performance ([#562 ](https://github.com/ros2/rmw_cyclonedds/issues/562)_)
* Improve serialization performance by optimizing [`dynamic_cast`` usage and replacing virtual functions with templates (`#553 ](https://github.com/ros2/rmw_cyclonedds/issues/553)_)
* Remove defaults to trigger proper warnings ([#549 ](https://github.com/ros2/rmw_cyclonedds/issues/549)_)
* add : get clients, servers info ([#499 ](https://github.com/ros2/rmw_cyclonedds/issues/499)_)
* Do not include rosidl_typesupport\_{c,cpp} in rmw impl typesupport list ([#544 ](https://github.com/ros2/rmw_cyclonedds/issues/544)_)
* Update CMake requirement ([#539 ](https://github.com/ros2/rmw_cyclonedds/issues/539)_)
* Contributors: Brandon Simoncic, Christophe Bedard, Janosch Machowinski, Lee, Minju, Oren Bell PhD, Shane Loretz, Tomoya Fujita, eboasson, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_dds_common <https://github.com/ros2/rmw_dds_common/tree/lyrical/rmw_dds_common/CHANGELOG.rst>`__

* If no publishers discovered, make the best available QoS for subscription. ([#84 ](https://github.com/ros2/rmw_dds_common/issues/84)_)
* Add get_clients_info_by_service and get_servers_info_by_service; introduce ServiceEntityInfo to handle service type hash in graph cache ([#82 ](https://github.com/ros2/rmw_dds_common/issues/82)_)
* Remove deprecated GraphCache methods without type hash ([#83 ](https://github.com/ros2/rmw_dds_common/issues/83)_)
* Update cmake requirements ([#80 ](https://github.com/ros2/rmw_dds_common/issues/80)_)
* Remove deprecated security utilities ([#79 ](https://github.com/ros2/rmw_dds_common/issues/79)_)
* Contributors: Alejandro Hernández Cordero, Christophe Bedard, Lee, Minju, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_fastrtps_cpp <https://github.com/ros2/rmw_fastrtps/tree/lyrical/rmw_fastrtps_cpp/CHANGELOG.rst>`__

* Clean up logs for the rosidl::Buffer path ([#886 ](https://github.com/ros2/rmw_fastrtps//issues/886)_) ([#887 ](https://github.com/ros2/rmw_fastrtps//issues/887)_)
* Change the buffer-aware BUFBE: -> bufbe. (backport [#880 ](https://github.com/ros2/rmw_fastrtps//issues/880)_) ([#884 ](https://github.com/ros2/rmw_fastrtps//issues/884)_)
* Fix UB in accessing the keys ([#879 ](https://github.com/ros2/rmw_fastrtps//issues/879)_) ([#882 ](https://github.com/ros2/rmw_fastrtps//issues/882)_)
* Remove warning when compiling with [`lcang`` (`#876 ](https://github.com/ros2/rmw_fastrtps/issues/876)_)
* Add support for rosidl::Buffer-aware per-endpoint pub/sub ([#867 ](https://github.com/ros2/rmw_fastrtps/issues/867)_)
* Use new aggregate rosidl target instead of _TARGETS ([#870 ](https://github.com/ros2/rmw_fastrtps/issues/870)_)
* Enable content filtering flag ([#869 ](https://github.com/ros2/rmw_fastrtps/issues/869)_)
* fix: remove superflous buildtool_export_depend. ([#852 ](https://github.com/ros2/rmw_fastrtps/issues/852)_)
* add : get clients, servers info ([#771 ](https://github.com/ros2/rmw_fastrtps/issues/771)_)
* Do not include rosidl_typesupport\_{c,cpp} in rmw impl typesupport list ([#843 ](https://github.com/ros2/rmw_fastrtps/issues/843)_)
* fix cmake deprecation ([#831 ](https://github.com/ros2/rmw_fastrtps/issues/831)_)
* Contributors: Alejandro Hernández Cordero, Alexis Tsogias, Barry Xu, CY Chen, Christophe Bedard, Lee, Minju, Tomoya Fujita, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_fastrtps_dynamic_cpp <https://github.com/ros2/rmw_fastrtps/tree/lyrical/rmw_fastrtps_dynamic_cpp/CHANGELOG.rst>`__

* Fix UB in accessing the keys ([#879 ](https://github.com/ros2/rmw_fastrtps//issues/879)_) ([#882 ](https://github.com/ros2/rmw_fastrtps//issues/882)_)
* Add support for rosidl::Buffer-aware per-endpoint pub/sub ([#867 ](https://github.com/ros2/rmw_fastrtps/issues/867)_)
* Use new aggregate rosidl target instead of _TARGETS ([#870 ](https://github.com/ros2/rmw_fastrtps/issues/870)_)
* fix: remove superflous buildtool_export_depend. ([#852 ](https://github.com/ros2/rmw_fastrtps/issues/852)_)
* add : get clients, servers info ([#771 ](https://github.com/ros2/rmw_fastrtps/issues/771)_)
* Do not include rosidl_typesupport\_{c,cpp} in rmw impl typesupport list ([#843 ](https://github.com/ros2/rmw_fastrtps/issues/843)_)
* Check remaining size before resizing sequences ([#827 ](https://github.com/ros2/rmw_fastrtps/issues/827)_)
* fix cmake deprecation ([#831 ](https://github.com/ros2/rmw_fastrtps/issues/831)_)
* Contributors: Alexis Tsogias, CY Chen, Christophe Bedard, Lee, Miguel Company, Minju, Tomoya Fujita, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_fastrtps_shared_cpp <https://github.com/ros2/rmw_fastrtps/tree/lyrical/rmw_fastrtps_shared_cpp/CHANGELOG.rst>`__

* Change the buffer-aware BUFBE: -> bufbe. (backport [#880 ](https://github.com/ros2/rmw_fastrtps//issues/880)_) ([#884 ](https://github.com/ros2/rmw_fastrtps//issues/884)_)
* feat: set collection header element_flags TryConstructFailAction::DISCARD instead of 0 ([#875 ](https://github.com/ros2/rmw_fastrtps/issues/875)_)
* Add support for rosidl::Buffer-aware per-endpoint pub/sub ([#867 ](https://github.com/ros2/rmw_fastrtps/issues/867)_)
* Added rmw_take tracepoint, because it wasn't being triggered for successful takes ([#871 ](https://github.com/ros2/rmw_fastrtps/issues/871)_)
* Added tracepoint to loaned take ([#868 ](https://github.com/ros2/rmw_fastrtps/issues/868)_)
* fix: remove superflous buildtool_export_depend. ([#852 ](https://github.com/ros2/rmw_fastrtps/issues/852)_)
* add : get clients, servers info ([#771 ](https://github.com/ros2/rmw_fastrtps/issues/771)_)
* Refs [#23861 ](https://github.com/ros2/rmw_fastrtps/issues/23861)_. Use key annotation in TypeObject build ([#849 ](https://github.com/ros2/rmw_fastrtps/issues/849)_)
* fix cmake deprecation ([#831 ](https://github.com/ros2/rmw_fastrtps/issues/831)_)
* Retrieve [`HistoryQoS`` in discovery when available (`#829 ](https://github.com/ros2/rmw_fastrtps/issues/829)_)
* check a local publication to ignore with serialized message. ([#823 ](https://github.com/ros2/rmw_fastrtps/issues/823)_)
* Contributors: CY Chen, Daisuke Nishimatsu, Lee, Mario Domínguez López, Miguel Company, Minju, Oren Bell, Oren Bell PhD, Tomoya Fujita, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_implementation <https://github.com/ros2/rmw_implementation/tree/lyrical/rmw_implementation/CHANGELOG.rst>`__

* Add rmw_zenoh_cpp as a build dependency ([#273 ](https://github.com/ros2/rmw_implementation/issues/273)_)
* Updated deprecated ament_index_cpp API ([#272 ](https://github.com/ros2/rmw_implementation/issues/272)_)
* Add rmw_get_clients_info_by_service , rmw_servers_clients_info_by_service ([#238 ](https://github.com/ros2/rmw_implementation/issues/238)_)
* fix cmake deprecation ([#267 ](https://github.com/ros2/rmw_implementation/issues/267)_)
* Explain rosidl_typesupport\_{c,cpp} in rmw impl typesupport list ([#265 ](https://github.com/ros2/rmw_implementation/issues/265)_)
* Fixed windows warning ([#254 ](https://github.com/ros2/rmw_implementation/issues/254)_)
* Contributors: Alejandro Hernández Cordero, Christophe Bedard, Lee, Minju, Tony Najjar, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_test_fixture <https://github.com/ros2/ament_cmake_ros/tree/lyrical/rmw_test_fixture/CHANGELOG.rst>`__

* Add missing dependency from rmw_test_fixture to rmw ([#53 ](https://github.com/ros2/ament_cmake_ros/issues/53)_)
* add find_package call ([#50 ](https://github.com/ros2/ament_cmake_ros/issues/50)_)
* fix cmake deprecation ([#47 ](https://github.com/ros2/ament_cmake_ros/issues/47)_)
* Contributors: Matt Condino, Scott K Logan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_test_fixture_implementation <https://github.com/ros2/ament_cmake_ros/tree/lyrical/rmw_test_fixture_implementation/CHANGELOG.rst>`__

* Block signals during Python environment reload in rmw_test_fixture_implementation ([#64 ](https://github.com/ros2/ament_cmake_ros/issues/64)_)
* Add [`ament_ros_defaults`` target (`#62 ](https://github.com/ros2/ament_cmake_ros/issues/62)_)
* Drop dependency group dependency on test fixtures ([#60 ](https://github.com/ros2/ament_cmake_ros/issues/60)_)
* Restore ROS_DOMAIN_ID after isolation is finished ([#58 ](https://github.com/ros2/ament_cmake_ros/issues/58)_)
* default to c++17 due to use of newer methods on std::map ([#55 ](https://github.com/ros2/ament_cmake_ros/issues/55)_)
* fix cmake deprecation ([#47 ](https://github.com/ros2/ament_cmake_ros/issues/47)_)
* On start-after-stop, re-check RMW_IMPLEMENTATION for changes ([#46 ](https://github.com/ros2/ament_cmake_ros/issues/46)_)
* Choose random domain IDs during default RMW isolation ([#39 ](https://github.com/ros2/ament_cmake_ros/issues/39)_)
* Ignore SIGINT *after* child process has been spawned ([#45 ](https://github.com/ros2/ament_cmake_ros/issues/45)_)
* Add some smoke tests for rmw_test_fixture_implementation ([#42 ](https://github.com/ros2/ament_cmake_ros/issues/42)_)
* Copy all environment variables explicitly ([#43 ](https://github.com/ros2/ament_cmake_ros/issues/43)_)
* Split the generator expression for each library ([#36 ](https://github.com/ros2/ament_cmake_ros/issues/36)_)
* Removed clang warnings ([#34 ](https://github.com/ros2/ament_cmake_ros/issues/34)_)
* Contributors: Alejandro Hernández Cordero, Michael Carlstrom, Michael Carroll, Scott K Logan, Tanishq Chaudhary, William Woodall, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_zenoh_cpp <https://github.com/ros2/rmw_zenoh/tree/lyrical/rmw_zenoh_cpp/CHANGELOG.rst>`__

* Bump Zenoh to 1.8.0, fix Windows shutdown hang, and resolve synchronization with [`undeclare`` (`#964 ](https://github.com/ros2/rmw_zenoh/issues/964)_)
* Revert changes to build against rust >= 1.75 and bump zenoh to 1.8.0 ([#960 ](https://github.com/ros2/rmw_zenoh/issues/960)_)
* Prevent deadlock by not holding both locks when processing event data ([#937 ](https://github.com/ros2/rmw_zenoh/issues/937)_)
* Bump zenoh to 1.8.0 ([#935 ](https://github.com/ros2/rmw_zenoh/issues/935)_)
* Explicitly set [`false`` for the content filtering feature (`#938 ](https://github.com/ros2/rmw_zenoh/issues/938)_)
* Add deadline/liveliness QoS events to [`rmw_zenoh_cpp`` (`#934 ](https://github.com/ros2/rmw_zenoh/issues/934)_)
* Catch [`PackageNotFoundError`` during default config URI loading to prevent crash (`#915 ](https://github.com/ros2/rmw_zenoh/issues/915)_)
* Populate [`reception_sequence_number`` and ``advertise_sequence_number`` features (`#920 ](https://github.com/ros2/rmw_zenoh/issues/920)_)
* Use [`get_package_share_path`` (`#913 ](https://github.com/ros2/rmw_zenoh/issues/913)_)
* Address outstanding TODO items ([#896 ](https://github.com/ros2/rmw_zenoh/issues/896)_)
* Expose zenoh session ([#865 ](https://github.com/ros2/rmw_zenoh/issues/865)_)
* Fix config loading with incorrect path variable ([#898 ](https://github.com/ros2/rmw_zenoh/issues/898)_)
* Fix build binary workflow ([#895 ](https://github.com/ros2/rmw_zenoh/issues/895)_)
* Fix line ending in session open error message ([#888 ](https://github.com/ros2/rmw_zenoh/issues/888)_)
* Update deprecated [`ament_index_cpp`` API (`#879 ](https://github.com/ros2/rmw_zenoh/issues/879)_)
* Remove [`default`` from switch with enum to enable compiler warnings (`#871 ](https://github.com/ros2/rmw_zenoh/issues/871)_)
* Use shared SHM transport provider instead of creating a new instance ([#857 ](https://github.com/ros2/rmw_zenoh/issues/857)_)
* Bump [`zenoh`` to 1.7.1 (`#870 ](https://github.com/ros2/rmw_zenoh/issues/870)_)
* Add rmw_get_clients_info_by_service and rmw_get_servers_info_by_service ([#679 ](https://github.com/ros2/rmw_zenoh/issues/679)_)
* Fix REP url locations ([#858 ](https://github.com/ros2/rmw_zenoh/issues/858)_)
* Restore ZENOH_CONFIG_OVERRIDE after isolation is finished ([#855 ](https://github.com/ros2/rmw_zenoh/issues/855)_)
* Fix typo in 'triggered' ([#844 ](https://github.com/ros2/rmw_zenoh/issues/844)_)
* Log details at SHM creation (alloc and threashold sizes) ([#835 ](https://github.com/ros2/rmw_zenoh/issues/835)_)
* Change default value of ZENOH_SHM_ALLOC_SIZE to 48 MiB ([#830 ](https://github.com/ros2/rmw_zenoh/issues/830)_)
* config: increase queries_default_timeout to 10min ([#820 ](https://github.com/ros2/rmw_zenoh/issues/820)_)
* Fix compile with clang ([#819 ](https://github.com/ros2/rmw_zenoh/issues/819)_)
* feat(logging): add contextual information to log messages ([#809 ](https://github.com/ros2/rmw_zenoh/issues/809)_)
* Align the config with upstream Zenoh. ([#785 ](https://github.com/ros2/rmw_zenoh/issues/785)_)
* fix: resolve memory leak when publishing with the default allocator ([#797 ](https://github.com/ros2/rmw_zenoh/issues/797)_)
* Recycle serialization buffers on transmission ([#342 ](https://github.com/ros2/rmw_zenoh/issues/342)_)
* refactor: avoid redundant key expression creation when replying ([#732 ](https://github.com/ros2/rmw_zenoh/issues/732)_)
* Do not include rosidl_typesupport\_{c,cpp} in rmw impl typesupport list ([#748 ](https://github.com/ros2/rmw_zenoh/issues/748)_)
* fixing typo flow to flows in config files ([#740 ](https://github.com/ros2/rmw_zenoh/issues/740)_)
* Shared Memory on C++ API ([#363 ](https://github.com/ros2/rmw_zenoh/issues/363)_)
* Bump Zenoh to v1.5.0 ([#728 ](https://github.com/ros2/rmw_zenoh/issues/728)_)
* rmw_zenoh_cpp: Include algorithm for std::find_if ([#723 ](https://github.com/ros2/rmw_zenoh/issues/723)_)
* Use rfind to avoid issues with service types ending in Request or Response ([#719 ](https://github.com/ros2/rmw_zenoh/issues/719)_)
* Remove the extra copy on the publisher side ([#711 ](https://github.com/ros2/rmw_zenoh/issues/711)_)
* Avoid ambiguity with variable shadowing ([#706 ](https://github.com/ros2/rmw_zenoh/issues/706)_)
* Only configure the timeout of the action-related service [`get_result`` to maximum value. (`#685 ](https://github.com/ros2/rmw_zenoh/issues/685)_)
* Use Zenoh Querier to replace Session.get ([#694 ](https://github.com/ros2/rmw_zenoh/issues/694)_)
* Use data() to avoid potentially dereferencing an empty vector ([#667 ](https://github.com/ros2/rmw_zenoh/issues/667)_)
* Bump Zenoh to 1.4.0 ([#652 ](https://github.com/ros2/rmw_zenoh/issues/652)_)
* fix(comment): correct the QoS incompatibilities ([#644 ](https://github.com/ros2/rmw_zenoh/issues/644)_)
* fix rmw_take_serialized_message. ([#638 ](https://github.com/ros2/rmw_zenoh/issues/638)_)
* Update CMakeLists.txt ([#617 ](https://github.com/ros2/rmw_zenoh/issues/617)_)
* Contributors: Alejandro Hernandez Cordero, Alejandro Hernández Cordero, ChenYing Kuo (CY), Chris Lalancette, Christophe Bedard, Faseel Chemmadan, Filip, Hervé Audren, Jan Vermaete, Julien Enoch, Lee, Mahmoud Mazouz, Minju, Nikola Banović, Scott K Logan, Shane Loretz, Skyler Medeiros, Steven Palma, Tim Clephas, Tomoya Fujita, Yadunund, Yuyuan Yuan, jordanburklund, milidam, mosfet80, yadunund, yellowhatter, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `robot_state_publisher <https://github.com/ros/robot_state_publisher/tree/lyrical/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#246 ](https://github.com/ros/robot_state_publisher/issues/246)_)
* Improvements ([#245 ](https://github.com/ros/robot_state_publisher/issues/245)_)
* Update subscription callback signatures ([#241 ](https://github.com/ros/robot_state_publisher/issues/241)_)
* Add functionality to read description from a topic instead of a parameter ([#234 ](https://github.com/ros/robot_state_publisher/issues/234)_)
* Removed tf2_ros warning ([#239 ](https://github.com/ros/robot_state_publisher/issues/239)_)
* fix cmake deprecation ([#232 ](https://github.com/ros/robot_state_publisher/issues/232)_)
* Removed tf2_ros warning ([#238 ](https://github.com/ros/robot_state_publisher/issues/238)_)
* Removed orocos kdl vendor dependency ([#237 ](https://github.com/ros/robot_state_publisher/issues/237)_)
* Removed warnings in geometry2 ([#236 ](https://github.com/ros/robot_state_publisher/issues/236)_)
* Replace deprecated tf2_ros headers ([#235 ](https://github.com/ros/robot_state_publisher/issues/235)_)
* Removed deprecated command-line argument ([#233 ](https://github.com/ros/robot_state_publisher/issues/233)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Kenji Brameld (TRACLabs), Maurice Alexander Purnawan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2action <https://github.com/ros2/ros2cli/tree/lyrical/ros2action/CHANGELOG.rst>`__

* Fix [`flake8`` (`#1215 ](https://github.com/ros2/ros2cli/issues/1215)_)
* Add timeout arguments to [`ros2 service call``, ``ros2 action send_goal``, ``ros2 component``, ``ros2 lifecycle``, and ``ros2 param`` (`#1185 ](https://github.com/ros2/ros2cli/issues/1185)_)
* add osrf_pycommon depend for test_exec. ([#1120 ](https://github.com/ros2/ros2cli/issues/1120)_)
* Fujitatomoya/clearup isolated ros2daemon ([#1098 ](https://github.com/ros2/ros2cli/issues/1098)_)
* Restore environment variables after launch tests ([#1086 ](https://github.com/ros2/ros2cli/issues/1086)_)
* Use rmw_test_fixture to isolate ros2cli tests ([#1062 ](https://github.com/ros2/ros2cli/issues/1062)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* fix ros2action send_goal signal handling. ([#1072 ](https://github.com/ros2/ros2cli/issues/1072)_)
* Fujitatomoya/ros2 action send goal timeout ([#1067 ](https://github.com/ros2/ros2cli/issues/1067)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Relax the check from exact to partial match. ([#1055 ](https://github.com/ros2/ros2cli/issues/1055)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* move QoS methods from ros2topic.api to ros2cli.qos. ([#1053 ](https://github.com/ros2/ros2cli/issues/1053)_)
* remove unnecessary '/' from ros2 action info. ([#1049 ](https://github.com/ros2/ros2cli/issues/1049)_)
* add QoS option to ros2service/ros2action echo commands. ([#1036 ](https://github.com/ros2/ros2cli/issues/1036)_)
* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Support 'ros2 action echo' ([#978 ](https://github.com/ros2/ros2cli/issues/978)_)
* Correct the license content ([#979 ](https://github.com/ros2/ros2cli/issues/979)_)
* Contributors: Barry Xu, Christophe Bedard, Michael Carlstrom, Michael Carroll, Scott K Logan, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2bag <https://github.com/ros2/rosbag2/tree/lyrical/ros2bag/CHANGELOG.rst>`__

* Add [`--repeat-all-transient-local`` flag for automatic transient-local topic detection (`#2391 ](https://github.com/ros2/rosbag2/issues/2391)_)
* Repeat transient-local topics: Recorder, CLI, and Python bindings ([#2387 ](https://github.com/ros2/rosbag2/issues/2387)_)
* Suppress multi-threaded process warning from rosbag2 flake8 ([#2329 ](https://github.com/ros2/rosbag2/issues/2329)_)
* Remove deprecated arguments and options from [`ros2bag`` (`#2328 ](https://github.com/ros2/rosbag2/issues/2328)_)
* Implement circular logging by split count ([`--max-bag-files``) (`#2218 ](https://github.com/ros2/rosbag2/issues/2218)_)
* Improve [`ros2 bag convert`` performance for fragment cutting and add ``--input-options`` (`#2325 ](https://github.com/ros2/rosbag2/issues/2325)_)
* Add static topics feature for recorder ([#2319 ](https://github.com/ros2/rosbag2/issues/2319)_)
* Add [`--max-cache-duration`` option for time-bounded snapshots (`#2289 ](https://github.com/ros2/rosbag2/issues/2289)_)
* Add [`rosbag2_storage_default_plugins`` to ``exec_depend`` of ``ros2bag`` (`#2227 ](https://github.com/ros2/rosbag2/issues/2227)_)
* Add [`input_serialization_format`` and ``output_serialization_format`` to ``RecordOptions``, deprecating ``rmw_serialization_format`` (`#2215 ](https://github.com/ros2/rosbag2/issues/2215)_)
* Publish messages lost statistics to 'events/messages_lost' topic ([#2150 ](https://github.com/ros2/rosbag2/issues/2150)_)
* Expose more of the player and recorder API to Python, and improve signal handling ([#2062 ](https://github.com/ros2/rosbag2/issues/2062)_)
* Fix setuptools deprecations ([#2087 ](https://github.com/ros2/rosbag2/issues/2087)_)
* Refactor Python player and recorder APIs into classes ([#2047 ](https://github.com/ros2/rosbag2/issues/2047)_)
* Upstream quality changes from Apex.AI part-2 ([#1924 ](https://github.com/ros2/rosbag2/issues/1924)_)
* Contributors: Christophe Bedard, Luke Sy, Michael Orlov, Tomoya Fujita, Tony Najjar, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2cli <https://github.com/ros2/ros2cli/tree/lyrical/ros2cli/CHANGELOG.rst>`__

* Add RMW isolation fixture to enable discovery for [`rmw_zenoh_cpp`` tests (`#1216 ](https://github.com/ros2/ros2cli/issues/1216)_)
* Add support for fish ([#1211 ](https://github.com/ros2/ros2cli/issues/1211)_)
* Fix [`flake8`` (`#1215 ](https://github.com/ros2/ros2cli/issues/1215)_)
* Fix future flake8 regressions ([#1196 ](https://github.com/ros2/ros2cli//issues/1196)_)
* fix deprecated warning for action graph APIs. ([#1188 ](https://github.com/ros2/ros2cli//issues/1188)_)
* Enable always complete ([#1190 ](https://github.com/ros2/ros2cli//issues/1190)_)
* Add fzf-based interactive selection to ros2cli commands ([#1151 ](https://github.com/ros2/ros2cli//issues/1151)_)
* check for invalid ROS discovery configuration and print warning if ne… ([#1178 ](https://github.com/ros2/ros2cli//issues/1178)_)
* skip history and depth check for rmw_connextdds. ([#1064 ](https://github.com/ros2/ros2cli/issues/1064)_)
* Remove importlib packages ([#1117 ](https://github.com/ros2/ros2cli/issues/1117)_)
* add verbose in service-info verb ([#916 ](https://github.com/ros2/ros2cli//issues/916)_)
* Fix handling of empty ROS_DOMAIN_ID in ros2cli ([#1112 ](https://github.com/ros2/ros2cli//issues/1112)_)
* fix: Also catch a TimeoutError ([#1092 ](https://github.com/ros2/ros2cli/issues/1092)_)
* [ros2doctor] Add Action Report ([#1076 ](https://github.com/ros2/ros2cli/issues/1076)_)
* Use rmw_test_fixture to isolate ros2cli tests ([#1062 ](https://github.com/ros2/ros2cli/issues/1062)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Add Service report similar to topic report ([#1059 ](https://github.com/ros2/ros2cli/issues/1059)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* move QoS methods from ros2topic.api to ros2cli.qos. ([#1053 ](https://github.com/ros2/ros2cli/issues/1053)_)
* Assert HistoryQoS in test_ros2cli_daemon ([#1040 ](https://github.com/ros2/ros2cli/issues/1040)_)
* remove add_subparsers from ros2cli. ([#1032 ](https://github.com/ros2/ros2cli/issues/1032)_)
* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Contributors: Christophe Bedard, David V. Lu!!, Kaju-Bubanja, Lee, Mario Domínguez López, Michael Carlstrom, Michael Carroll, Minju, SPeak, Scott K Logan, Tomoya Fujita, Tony Najjar, Yuyuan Yuan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2cli_common_extensions <https://github.com/ros2/ros2cli_common_extensions/tree/lyrical/ros2cli_common_extensions/CHANGELOG.rst>`__

* Add dependency on ros2plugin in package.xml ([#13 ](https://github.com/ros2/ros2cli_common_extensions/issues/13)_)
* Update CMakeLists.txt ([#11 ](https://github.com/ros2/ros2cli_common_extensions/issues/11)_)
* Contributors: Maurice Alexander Purnawan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2cli_test_interfaces <https://github.com/ros2/ros2cli/tree/lyrical/ros2cli_test_interfaces/CHANGELOG.rst>`__

* fix cmake deprecation ([#1082 ](https://github.com/ros2/ros2cli/issues/1082)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2component <https://github.com/ros2/ros2cli/tree/lyrical/ros2component/CHANGELOG.rst>`__

* Fix [`flake8`` (`#1215 ](https://github.com/ros2/ros2cli/issues/1215)_)
* Add timeout arguments to [`ros2 service call``, ``ros2 action send_goal``, ``ros2 component``, ``ros2 lifecycle``, and ``ros2 param`` (`#1185 ](https://github.com/ros2/ros2cli/issues/1185)_)
* Fix future flake8 regressions ([#1196 ](https://github.com/ros2/ros2cli//issues/1196)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* Contributors: Christophe Bedard, Michael Carlstrom, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2doctor <https://github.com/ros2/ros2cli/tree/lyrical/ros2doctor/CHANGELOG.rst>`__

* Fix future flake8 regressions ([#1196 ](https://github.com/ros2/ros2cli//issues/1196)_)
* Remove importlib packages ([#1117 ](https://github.com/ros2/ros2cli/issues/1117)_)
* Harden ros2doctor system calls. ([#1118 ](https://github.com/ros2/ros2cli/issues/1118)_)
* Add error handling when parsing package locally ([#1108 ](https://github.com/ros2/ros2cli//issues/1108)_)
* Fujitatomoya/clearup isolated ros2daemon ([#1098 ](https://github.com/ros2/ros2cli/issues/1098)_)
* [ros2doctor] Environment Report ([#1045 ](https://github.com/ros2/ros2cli/issues/1045)_)
* Restore environment variables after launch tests ([#1086 ](https://github.com/ros2/ros2cli/issues/1086)_)
* add warning notice for ros2 doctor --report. ([#1079 ](https://github.com/ros2/ros2cli/issues/1079)_)
* [ros2doctor] Add Action Report ([#1076 ](https://github.com/ros2/ros2cli/issues/1076)_)
* Use rmw_test_fixture to isolate ros2cli tests ([#1062 ](https://github.com/ros2/ros2cli/issues/1062)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Add Service report similar to topic report ([#1059 ](https://github.com/ros2/ros2cli/issues/1059)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* Fix stringifying InterfaceFlags when the flags are empty. ([#1026 ](https://github.com/ros2/ros2cli/issues/1026)_)
* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Skip QoS compatibility test on Zenoh ([#985 ](https://github.com/ros2/ros2cli/issues/985)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Christophe Bedard, Michael Carlstrom, Michael Carroll, Scott K Logan, Tomoya Fujita, mini-1235, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2interface <https://github.com/ros2/ros2cli/tree/lyrical/ros2interface/CHANGELOG.rst>`__

* Add fzf-based interactive selection to ros2cli commands ([#1151 ](https://github.com/ros2/ros2cli//issues/1151)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* Contributors: Christophe Bedard, Michael Carlstrom, Tony Najjar, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2launch <https://github.com/ros2/launch_ros/tree/lyrical/ros2launch/CHANGELOG.rst>`__

* correct typos ([#524 ](https://github.com/ros2/launch_ros//issues/524)_)
* fix setuptools deprecations ([#475 ](https://github.com/ros2/launch_ros/issues/475)_)
* user control of log file base names, in ros2 launch ([#461 ](https://github.com/ros2/launch_ros/issues/461)_) Co-authored-by: Katherine Scott <katherineAScott@gmail.com>
* Contributors: Auguste Lalande, Tanishq Chaudhary, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2lifecycle <https://github.com/ros2/ros2cli/tree/lyrical/ros2lifecycle/CHANGELOG.rst>`__

* Add timeout arguments to [`ros2 service call``, ``ros2 action send_goal``, ``ros2 component``, ``ros2 lifecycle``, and ``ros2 param`` (`#1185 ](https://github.com/ros2/ros2cli/issues/1185)_)
* ros2interface output the contents for each node. ([#1163 ](https://github.com/ros2/ros2cli//issues/1163)_)
* Fujitatomoya/clearup isolated ros2daemon ([#1098 ](https://github.com/ros2/ros2cli/issues/1098)_)
* Restore environment variables after launch tests ([#1086 ](https://github.com/ros2/ros2cli/issues/1086)_)
* Use rmw_test_fixture to isolate ros2cli tests ([#1062 ](https://github.com/ros2/ros2cli/issues/1062)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Relax the check from exact to partial match. ([#1055 ](https://github.com/ros2/ros2cli/issues/1055)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Contributors: Christophe Bedard, Michael Carlstrom, Michael Carroll, Scott K Logan, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2lifecycle_test_fixtures <https://github.com/ros2/ros2cli/tree/lyrical/ros2lifecycle_test_fixtures/CHANGELOG.rst>`__

* fix cmake deprecation ([#1082 ](https://github.com/ros2/ros2cli/issues/1082)_)
* Use target_link_libraries instead of ament_target_dependencies ([#973 ](https://github.com/ros2/ros2cli/issues/973)_)
* Contributors: Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2multicast <https://github.com/ros2/ros2cli/tree/lyrical/ros2multicast/CHANGELOG.rst>`__

* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* Contributors: Christophe Bedard, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2node <https://github.com/ros2/ros2cli/tree/lyrical/ros2node/CHANGELOG.rst>`__

* Add fzf-based interactive selection to ros2cli commands ([#1151 ](https://github.com/ros2/ros2cli//issues/1151)_)
* Fujitatomoya/clearup isolated ros2daemon ([#1098 ](https://github.com/ros2/ros2cli/issues/1098)_)
* Restore environment variables after launch tests ([#1086 ](https://github.com/ros2/ros2cli/issues/1086)_)
* Use rmw_test_fixture to isolate ros2cli tests ([#1062 ](https://github.com/ros2/ros2cli/issues/1062)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Contributors: Christophe Bedard, Michael Carlstrom, Michael Carroll, Scott K Logan, Tomoya Fujita, Tony Najjar, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2param <https://github.com/ros2/ros2cli/tree/lyrical/ros2param/CHANGELOG.rst>`__

* Add timeout arguments to [`ros2 service call``, ``ros2 action send_goal``, ``ros2 component``, ``ros2 lifecycle``, and ``ros2 param`` (`#1185 ](https://github.com/ros2/ros2cli/issues/1185)_)
* ros2 param set /node_name <param1 value1 param2 value2...> support. ([#1204 ](https://github.com/ros2/ros2cli//issues/1204)_)
* ros2 param get /node_name <param1 param2 param3...> support. ([#1203 ](https://github.com/ros2/ros2cli//issues/1203)_)
* Add per-node timeout option to ros2 param list ([#1170 ](https://github.com/ros2/ros2cli//issues/1170)_)
* Fix Bash completion ([#1182 ](https://github.com/ros2/ros2cli//issues/1182)_)
* Add fzf-based interactive selection to ros2cli commands ([#1151 ](https://github.com/ros2/ros2cli//issues/1151)_)
* Support "ros2 param get <parameter>" across all nodes. ([#1174 ](https://github.com/ros2/ros2cli//issues/1174)_)
* Fix ParameterNameCompleter. ([#1172 ](https://github.com/ros2/ros2cli//issues/1172)_)
* Output node parameters upon each receipt ([#1162 ](https://github.com/ros2/ros2cli//issues/1162)_)
* skip test_verb_load_wildcard for rmw_connextdds. ([#1150 ](https://github.com/ros2/ros2cli/issues/1150)_)
* Fujitatomoya/clearup isolated ros2daemon ([#1098 ](https://github.com/ros2/ros2cli/issues/1098)_)
* Restore environment variables after launch tests ([#1086 ](https://github.com/ros2/ros2cli/issues/1086)_)
* Use rmw_test_fixture to isolate ros2cli tests ([#1062 ](https://github.com/ros2/ros2cli/issues/1062)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Relax the check from exact to partial match. ([#1055 ](https://github.com/ros2/ros2cli/issues/1055)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* fix misspelling. ([#1035 ](https://github.com/ros2/ros2cli/issues/1035)_)
* catch ConnectionRefusedError, so that it can fall back to DirectNode. ([#1014 ](https://github.com/ros2/ros2cli/issues/1014)_)
* fails the test properly to avoid TypeError exception. ([#1016 ](https://github.com/ros2/ros2cli/issues/1016)_)
* Fix loading parameter behavior from yaml file ([#864 ](https://github.com/ros2/ros2cli/issues/864)_)
* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Contributors: Barry Xu, Christophe Bedard, Michael Carlstrom, Michael Carroll, Scott K Logan, Taiga Arai, Tomoya Fujita, Tony Najjar, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2pkg <https://github.com/ros2/ros2cli/tree/lyrical/ros2pkg/CHANGELOG.rst>`__

* Remove "rclrs" duplicate dependency ([#1197 ](https://github.com/ros2/ros2cli//issues/1197)_)
* Fix future flake8 regressions ([#1196 ](https://github.com/ros2/ros2cli//issues/1196)_)
* Add Native ROS2 Rust Package Create Capability ([#1107 ](https://github.com/ros2/ros2cli/issues/1107)_)
* Remove importlib packages ([#1117 ](https://github.com/ros2/ros2cli/issues/1117)_)
* add mypy ([#1109 ](https://github.com/ros2/ros2cli//issues/1109)_)
* fix cmake deprecation ([#1082 ](https://github.com/ros2/ros2cli/issues/1082)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Reduce boilerplate in install(TARGETS for library ([#1056 ](https://github.com/ros2/ros2cli/issues/1056)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* Use modern C++17 syntax. ([#982 ](https://github.com/ros2/ros2cli/issues/982)_)
* Use target_link_libraries instead of ament_target_dependencies ([#973 ](https://github.com/ros2/ros2cli/issues/973)_)
* Try to use the git global user.name for maintainer-name ([#968 ](https://github.com/ros2/ros2cli/issues/968)_)
* Update minimum CMake version CMakeLists.txt.em ([#969 ](https://github.com/ros2/ros2cli/issues/969)_)
* Contributors: Bartlomiej Styczen, Christophe Bedard, Larry Gezelius, Michael Carlstrom, Parth Patel, Sebastian Castro, Shane Loretz, Shynur, Silvio Traversaro, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2plugin <https://github.com/ros/pluginlib/tree/lyrical/ros2plugin/CHANGELOG.rst>`__

* Implement package option ([#293 ](https://github.com/ros/pluginlib/issues/293)_)
* Improve logging when unable to parse the plugin ([#285 ](https://github.com/ros/pluginlib/issues/285)_)
* Add ros2plugin ([#165 ](https://github.com/ros/pluginlib/issues/165)_)
* Contributors: Alejandro Hernández Cordero, Jeremie Deray, mini-1235


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2run <https://github.com/ros2/ros2cli/tree/lyrical/ros2run/CHANGELOG.rst>`__

* Fix Bash completion ([#1182 ](https://github.com/ros2/ros2cli//issues/1182)_)
* Add fzf-based interactive selection to ros2cli commands ([#1151 ](https://github.com/ros2/ros2cli//issues/1151)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* Add signal handler SIGIN/SIGTERM to ros2run ([#899 ](https://github.com/ros2/ros2cli/issues/899)_)
* Contributors: Christophe Bedard, Michael Carlstrom, Tomoya Fujita, Tony Najjar, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2service <https://github.com/ros2/ros2cli/tree/lyrical/ros2service/CHANGELOG.rst>`__

* Add timeout arguments to [`ros2 service call``, ``ros2 action send_goal``, ``ros2 component``, ``ros2 lifecycle``, and ``ros2 param`` (`#1185 ](https://github.com/ros2/ros2cli/issues/1185)_)
* Fix Bash completion ([#1182 ](https://github.com/ros2/ros2cli//issues/1182)_)
* Add fzf-based interactive selection to ros2cli commands ([#1151 ](https://github.com/ros2/ros2cli//issues/1151)_)
* add verbose in service-info verb ([#916 ](https://github.com/ros2/ros2cli//issues/916)_)
* Fujitatomoya/clearup isolated ros2daemon ([#1098 ](https://github.com/ros2/ros2cli/issues/1098)_)
* Restore environment variables after launch tests ([#1086 ](https://github.com/ros2/ros2cli/issues/1086)_)
* Use rmw_test_fixture to isolate ros2cli tests ([#1062 ](https://github.com/ros2/ros2cli/issues/1062)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Relax the check from exact to partial match. ([#1055 ](https://github.com/ros2/ros2cli/issues/1055)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* move QoS methods from ros2topic.api to ros2cli.qos. ([#1053 ](https://github.com/ros2/ros2cli/issues/1053)_)
* add QoS option to ros2service/ros2action echo commands. ([#1036 ](https://github.com/ros2/ros2cli/issues/1036)_)
* Use [`get_service`` in ``ros2service call`` (`#994 ](https://github.com/ros2/ros2cli/issues/994)_)
* Allow zenoh tests to run with multicast ([#992 ](https://github.com/ros2/ros2cli/issues/992)_)
* Support QoS options for [`ros2 service call`` (`#966 ](https://github.com/ros2/ros2cli/issues/966)_)
* Contributors: Christophe Bedard, Lee, Michael Carlstrom, Michael Carroll, Minju, Scott K Logan, Tomoya Fujita, Tony Najjar, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2test <https://github.com/ros2/ros_testing/tree/lyrical/ros2test/CHANGELOG.rst>`__

* fix setuptools deprecations ([#16 ](https://github.com/ros2/ros_testing/issues/16)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2topic <https://github.com/ros2/ros2cli/tree/lyrical/ros2topic/CHANGELOG.rst>`__

* Improve test isolation and suppress Connext license noise ([#1225 ](https://github.com/ros2/ros2cli/issues/1225)_)
* Add fzf-based interactive selection to ros2cli commands ([#1151 ](https://github.com/ros2/ros2cli//issues/1151)_)
* add "--all/-a" option to "ros2 topic bw" with screen refresh. ([#1130 ](https://github.com/ros2/ros2cli/issues/1130)_)
* return explicitly from internal functions. ([#1128 ](https://github.com/ros2/ros2cli/issues/1128)_)
* support multiple topics for "ros2 topic bw". ([#1124 ](https://github.com/ros2/ros2cli/issues/1124)_)
* add "--all/-a" option to "ros2 topic hz" with screen refresh. ([#1122 ](https://github.com/ros2/ros2cli/issues/1122)_)
* Fujitatomoya/clearup isolated ros2daemon ([#1098 ](https://github.com/ros2/ros2cli/issues/1098)_)
* wait for the publisher before test command is executed. ([#1094 ](https://github.com/ros2/ros2cli/issues/1094)_)
* Enable test isolation on a few remaining ros2topic tests ([#1087 ](https://github.com/ros2/ros2cli/issues/1087)_)
* Restore environment variables after launch tests ([#1086 ](https://github.com/ros2/ros2cli/issues/1086)_)
* Use rmw_test_fixture to isolate ros2cli tests ([#1062 ](https://github.com/ros2/ros2cli/issues/1062)_)
* fix setuptools deprecations ([#1066 ](https://github.com/ros2/ros2cli/issues/1066)_)
* Make sure to install py.typed files ([#1058 ](https://github.com/ros2/ros2cli/issues/1058)_)
* Export Typing information ([#1041 ](https://github.com/ros2/ros2cli/issues/1041)_)
* move QoS methods from ros2topic.api to ros2cli.qos. ([#1053 ](https://github.com/ros2/ros2cli/issues/1053)_)
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
* Contributors: Alejandro Hernández Cordero, Anthony Welte, Christophe Bedard, Fabian Thomsen, Florencia, Kostubh Khandelwal, Leander Stephen D'Souza, Martin Pecka, Michael Carlstrom, Michael Carroll, Scott K Logan, Tomoya Fujita, Tony Najjar, mosfet80, nomumu


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2trace <https://github.com/ros2/ros2_tracing/tree/lyrical/ros2trace/CHANGELOG.rst>`__

* Ignore A0005 ([#237 ](https://github.com/ros2/ros2_tracing/issues/237)_)
* Update trace command's doc-string ([#213 ](https://github.com/ros2/ros2_tracing/issues/213)_)
* Allow creating snapshot sessions ([#195 ](https://github.com/ros2/ros2_tracing/issues/195)_)
* Add support for starting tracing at runtime ([#191 ](https://github.com/ros2/ros2_tracing/issues/191)_)
* fix setuptools deprecation ([#189 ](https://github.com/ros2/ros2_tracing/issues/189)_)
* Address typing issues reported by mypy in tracetools_launch ([#184 ](https://github.com/ros2/ros2_tracing/issues/184)_)
* Contributors: Christophe Bedard, Michael Carlstrom, Shravan Deva, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros_environment <https://github.com/ros/ros_environment/tree/lyrical/CHANGELOG.rst>`__

* Change default ROS_DISTRO from 'rolling' to 'lyrical'
* fix cmake deprecation ([#42 ](https://github.com/ros/ros_environment/issues/42)_)
* Remove CODEOWNERS. ([#40 ](https://github.com/ros/ros_environment/issues/40)_)
* Contributors: Chris Lalancette, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros_testing <https://github.com/ros2/ros_testing/tree/lyrical/ros_testing/CHANGELOG.rst>`__

* fix cmake deprecation ([#17 ](https://github.com/ros2/ros_testing/issues/17)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2 <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2/CHANGELOG.rst>`__

* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_compression <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_compression/CHANGELOG.rst>`__

* Add validation for empty file path in compression process ([#2398 ](https://github.com/ros2/rosbag2/issues/2398)_)
* Fix a possible race condition in compression writer on close ([#2362 ](https://github.com/ros2/rosbag2/issues/2362)_)
* Update Rosbag2 filename format to [`index+name+timestamp`` (`#2265 ](https://github.com/ros2/rosbag2/issues/2265)_)
* Implement circular logging by split count ([`--max-bag-files``) (`#2218 ](https://github.com/ros2/rosbag2/issues/2218)_)
* Make topics persistent between writer's close() and open() API calls ([#2229 ](https://github.com/ros2/rosbag2/issues/2229)_)
* Address recorder test flakiness by increasing cache size ([#2203 ](https://github.com/ros2/rosbag2/issues/2203)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Add message loss statistics callbacks and logging ([#2039 ](https://github.com/ros2/rosbag2/issues/2039)_)
* Introduce new [`BaseWriteInterface`` methods ``write_messages`` and ``write_message`` to provide operation status, deprecating old write APIs (`#2030 ](https://github.com/ros2/rosbag2/issues/2030)_)
* Bugfix: [`ros2 bag convert`` dropping messages with compression mode message (`#1975 ](https://github.com/ros2/rosbag2/issues/1975)_)
* Contributors: Daisuke Sato, DangitBen, Luke Sy, Michael Orlov, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_compression_zstd <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_compression_zstd/CHANGELOG.rst>`__

* Replace [`zstd_vendor`` with ``zstd_cmake_module`` (`#2166 ](https://github.com/ros2/rosbag2/issues/2166)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Contributors: Alejandro Hernández Cordero, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_cpp <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_cpp/CHANGELOG.rst>`__

* Removed clang warning ([#2404 ](https://github.com/ros2/rosbag2/issues/2404)_)
* Implement [`transient-local topic`` repetition for Writer API and split/snapshot integration (`#2386 ](https://github.com/ros2/rosbag2/issues/2386)_)
* Add [`TransientLocalMessagesCache`` and ``RecordOptions`` for repeating transient-local topics (`#2385 ](https://github.com/ros2/rosbag2/issues/2385)_)
* Use new ROSIDL aggregate CMake target ([#2384 ](https://github.com/ros2/rosbag2/issues/2384)_)
* Fix a possible race condition in compression writer on close ([#2362 ](https://github.com/ros2/rosbag2/issues/2362)_)
* Fix incorrect serialization format in metadata ([#2372 ](https://github.com/ros2/rosbag2/issues/2372)_)
* Update Rosbag2 filename format to [`index+name+timestamp`` (`#2265 ](https://github.com/ros2/rosbag2/issues/2265)_)
* Support relative includes for IDL in local message definition ([#2241 ](https://github.com/ros2/rosbag2/issues/2241)_)
* Implement circular logging by split count ([`--max-bag-files``) (`#2218 ](https://github.com/ros2/rosbag2/issues/2218)_)
* Add [`--max-cache-duration`` option for time-bounded snapshots (`#2289 ](https://github.com/ros2/rosbag2/issues/2289)_)
* Workaround flaky [`bagsize_split_is_at_least_specified_size`` test (`#2311 ](https://github.com/ros2/rosbag2/issues/2311)_)
* Incorporate upstream minor fixes from Apex.AI ([#2240 ](https://github.com/ros2/rosbag2/issues/2240)_)
* Update deprecated ament_index_cpp API ([#2268 ](https://github.com/ros2/rosbag2/issues/2268)_)
* Make topics persistent between writer's close() and open() API calls ([#2229 ](https://github.com/ros2/rosbag2/issues/2229)_)
* Add nullptr check when pushing new messages to the message cache ([#2219 ](https://github.com/ros2/rosbag2/issues/2219)_)
* Address recorder test flakiness by increasing cache size ([#2203 ](https://github.com/ros2/rosbag2/issues/2203)_)
* Log reasoning for not found message definition only in debug log ([#2183 ](https://github.com/ros2/rosbag2/issues/2183)_)
* Improve error handling in rosbag2_cpp with null checks and exception throwing ([#2127 ](https://github.com/ros2/rosbag2/issues/2127)_)
* Add null pointer checks in [`Reader`` constructor and ``open()`` method (`#2135 ](https://github.com/ros2/rosbag2/issues/2135)_)
* Use [`rclcpp typesupport helpers`` in ``rosbag2_cpp`` (`#2017 ](https://github.com/ros2/rosbag2/issues/2017)_)
* Fix callback not called for MESSAGES_LOST event ([#2105 ](https://github.com/ros2/rosbag2/issues/2105)_)
* Improve recorder's MessageCache performance ([#2104 ](https://github.com/ros2/rosbag2/issues/2104)_)
* Fix reindex duration bug when bag file durations overlap ([#2036 ](https://github.com/ros2/rosbag2/issues/2036)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Add support for searching message definitions in nested subdirectories ([#2055 ](https://github.com/ros2/rosbag2/issues/2055)_)
* Add message loss statistics callbacks and logging ([#2039 ](https://github.com/ros2/rosbag2/issues/2039)_)
* Use cache to determine action interface inner types ([#2052 ](https://github.com/ros2/rosbag2/issues/2052)_)
* Fix service/action message definition issue ([#2041 ](https://github.com/ros2/rosbag2/issues/2041)_)
* Introduce new [`BaseWriteInterface`` methods ``write_messages`` and ``write_message`` to provide operation status, deprecating old write APIs (`#2030 ](https://github.com/ros2/rosbag2/issues/2030)_)
* Improve message publishing timing by avoiding sporadic wakeups and fixing incorrect intervals on player start ([#2025 ](https://github.com/ros2/rosbag2/issues/2025)_)
* Upstream quality changes from Apex.AI part-2 ([#1924 ](https://github.com/ros2/rosbag2/issues/1924)_)
* Address clang warning in the [`TimeControllerClock::wakeup()`` (`#1962 ](https://github.com/ros2/rosbag2/issues/1962)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe Bedard, Chui Vanfleet, Daisuke Sato, Emerson Knapp, Hunter L. Allen, José Faria, Luke Sy, Michael Orlov, Tomoya Fujita, Tony Najjar, YuJin Hong, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_examples_cpp <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_examples/rosbag2_examples_cpp/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#2384 ](https://github.com/ros2/rosbag2/issues/2384)_)
* Update subscription callback signatures ([#2225 ](https://github.com/ros2/rosbag2/issues/2225)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Add examples for compressing bag files ([#1956 ](https://github.com/ros2/rosbag2/issues/1956)_)
* Contributors: Emerson Knapp, Maxime Fleury, mini-1235, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_examples_py <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_examples/rosbag2_examples_py/CHANGELOG.rst>`__

* Fix setuptools deprecation by removing [`tests_require`` (`#2092 ](https://github.com/ros2/rosbag2/issues/2092)_)
* Add examples for compressing bag files ([#1956 ](https://github.com/ros2/rosbag2/issues/1956)_)
* Upstream quality changes from Apex.AI part-2 ([#1924 ](https://github.com/ros2/rosbag2/issues/1924)_)
* Add a simple example showing how to convert bags to the csv file ([#1974 ](https://github.com/ros2/rosbag2/issues/1974)_)
* Contributors: Christophe Bedard, Maxime Fleury, Michael Orlov, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_interfaces <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_interfaces/CHANGELOG.rst>`__

* Add support for time based Resume service ([#2357 ](https://github.com/ros2/rosbag2/issues/2357)_)
* Allow pause/resume service calls while not in recording ([#2349 ](https://github.com/ros2/rosbag2/issues/2349)_)
* Implement delayed and time-based recorder and player services, adding new bag split modes ([#2330 ](https://github.com/ros2/rosbag2/issues/2330)_)
* Add error return code to the [`~/stop`` service request (`#2312 ](https://github.com/ros2/rosbag2/issues/2312)_)
* Add Record, Stop, StartDiscovery, StopDiscovery, and IsDiscoveryRunning services for Recorder ([#2248 ](https://github.com/ros2/rosbag2/issues/2248)_)
* Publish messages lost statistics to 'events/messages_lost' topic ([#2150 ](https://github.com/ros2/rosbag2/issues/2150)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Contributors: Michael Orlov, carlos-apex, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_performance_benchmarking <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_performance/rosbag2_performance_benchmarking/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#2384 ](https://github.com/ros2/rosbag2/issues/2384)_)
* Remove unnecessary dependencies on [`yaml_cpp_vendor`` (`#2353 ](https://github.com/ros2/rosbag2/issues/2353)_)
* Fix warning by initializing [`number_of_threads`` (`#2121 ](https://github.com/ros2/rosbag2/issues/2121)_)
* Enable [`rosbag2_performance_benchmarking`` package to be built by default (`#2093 ](https://github.com/ros2/rosbag2/issues/2093)_)
* Fix performance benchmarking data generation and environment variable handling ([#2078 ](https://github.com/ros2/rosbag2/issues/2078)_)
* Fix failure in [`benchmark_launch`` when calling ``Process.wait()`` twice (`#2076 ](https://github.com/ros2/rosbag2/issues/2076)_)
* Fix incorrect results from [`prosbag2_performance_benchmarking`` for high-frequency topics (`#2077 ](https://github.com/ros2/rosbag2/issues/2077)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Upstream quality changes from Apex.AI part-2 ([#1924 ](https://github.com/ros2/rosbag2/issues/1924)_)
* Contributors: Chris Lalancette, Christophe Bedard, Cristóbal Arroyo, Emerson Knapp, Michael Orlov, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_performance_benchmarking_msgs <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_performance/rosbag2_performance_benchmarking_msgs/CHANGELOG.rst>`__

* Enable [`rosbag2_performance_benchmarking`` package to be built by default (`#2093 ](https://github.com/ros2/rosbag2/issues/2093)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Contributors: Michael Orlov, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_py <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_py/CHANGELOG.rst>`__

* Add [`--repeat-all-transient-local`` flag for automatic transient-local topic detection (`#2391 ](https://github.com/ros2/rosbag2/issues/2391)_)
* Repeat transient-local topics: Recorder, CLI, and Python bindings ([#2387 ](https://github.com/ros2/rosbag2/issues/2387)_)
* Implement circular logging by split count ([`--max-bag-files``) (`#2218 ](https://github.com/ros2/rosbag2/issues/2218)_)
* Move to [`build_depend`` (`#2332 ](https://github.com/ros2/rosbag2/issues/2332)_)
* Improve [`ros2 bag convert`` performance for fragment cutting and add ``--input-options`` (`#2325 ](https://github.com/ros2/rosbag2/issues/2325)_)
* Add static topics feature for recorder ([#2319 ](https://github.com/ros2/rosbag2/issues/2319)_)
* Add [`--max-cache-duration`` option for time-bounded snapshots (`#2289 ](https://github.com/ros2/rosbag2/issues/2289)_)
* Incorporate upstream minor fixes from Apex.AI ([#2240 ](https://github.com/ros2/rosbag2/issues/2240)_)
* Add [`input_serialization_format`` and ``output_serialization_format`` to ``RecordOptions``, deprecating ``rmw_serialization_format`` (`#2215 ](https://github.com/ros2/rosbag2/issues/2215)_)
* Use pybind11 from deb or pixi ([#2154 ](https://github.com/ros2/rosbag2/issues/2154)_)
* Publish messages lost statistics to 'events/messages_lost' topic ([#2150 ](https://github.com/ros2/rosbag2/issues/2150)_)
* Ensure test topic discovery by recorder in [`rosbag2_py`` test (`#2132 ](https://github.com/ros2/rosbag2/issues/2132)_)
* Fix CMake list append for env vars in rosbag2_py with clang ([#2116 ](https://github.com/ros2/rosbag2/issues/2116)_)
* Add public API for player's starting time and playback duration ([#2095 ](https://github.com/ros2/rosbag2/issues/2095)_)
* Expose more of the player and recorder API to Python, and improve signal handling ([#2062 ](https://github.com/ros2/rosbag2/issues/2062)_)
* Add [`send_timestamp`` to Python interface for reading serialized messages (`#2061 ](https://github.com/ros2/rosbag2/issues/2061)_)
* Refactor Python player and recorder APIs into classes ([#2047 ](https://github.com/ros2/rosbag2/issues/2047)_)
* Fix service/action message definition issue ([#2041 ](https://github.com/ros2/rosbag2/issues/2041)_)
* Upstream quality changes from Apex.AI part-2 ([#1924 ](https://github.com/ros2/rosbag2/issues/1924)_)
* Bugfix: [`ros2 bag convert`` dropping messages with compression mode message (`#1975 ](https://github.com/ros2/rosbag2/issues/1975)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe Bedard, DangitBen, Luke Sy, Michael Carlstrom, Michael Orlov, Om Shivam Verma, Tony Najjar


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_storage <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_storage/CHANGELOG.rst>`__

* Add [`TransientLocalMessagesCache`` and ``RecordOptions`` for repeating transient-local topics (`#2385 ](https://github.com/ros2/rosbag2/issues/2385)_)
* Implement delayed and time-based recorder and player services, adding new bag split modes ([#2330 ](https://github.com/ros2/rosbag2/issues/2330)_)
* Implement circular logging by split count ([`--max-bag-files``) (`#2218 ](https://github.com/ros2/rosbag2/issues/2218)_)
* Improve [`ros2 bag convert`` performance for fragment cutting and add ``--input-options`` (`#2325 ](https://github.com/ros2/rosbag2/issues/2325)_)
* Add [`--max-cache-duration`` option for time-bounded snapshots (`#2289 ](https://github.com/ros2/rosbag2/issues/2289)_)
* Throw [`YAML::Exception`` during conversion if the data type mismatches (`#2262 ](https://github.com/ros2/rosbag2/issues/2262)_)
* Fix decoder and encode mismatch in YAML deserialization ([#2277 ](https://github.com/ros2/rosbag2/issues/2277)_)
* Incorporate upstream minor fixes from Apex.AI ([#2240 ](https://github.com/ros2/rosbag2/issues/2240)_)
* Fix memory leak on [`make_empty_serialized_message()`` (`#2253 ](https://github.com/ros2/rosbag2/issues/2253)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Introduce new [`BaseWriteInterface`` methods ``write_messages`` and ``write_message`` to provide operation status, deprecating old write APIs (`#2030 ](https://github.com/ros2/rosbag2/issues/2030)_)
* Fix undefined behavior in the [`rosbag2_storage`` and ``rosbag2_storage_sqlite3`` packages (`#1997 ](https://github.com/ros2/rosbag2/issues/1997)_)
* Use DDS queue depth for subscriptions as a maximum value across publishers ([#1960 ](https://github.com/ros2/rosbag2/issues/1960)_)
* Contributors: Luke Sy, Michael Orlov, Tomoya Fujita, Tony Najjar, carlos-apex, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_storage_default_plugins <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_storage_default_plugins/CHANGELOG.rst>`__

* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_storage_mcap <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_storage_mcap/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#2384 ](https://github.com/ros2/rosbag2/issues/2384)_)
* Remove unnecessary dependencies on [`yaml_cpp_vendor`` (`#2353 ](https://github.com/ros2/rosbag2/issues/2353)_)
* Fix MCAPStorage::seek(time) to advance when timestamp matches current time ([#2157 ](https://github.com/ros2/rosbag2/issues/2157)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Introduce new [`BaseWriteInterface`` methods ``write_messages`` and ``write_message`` to provide operation status, deprecating old write APIs (`#2030 ](https://github.com/ros2/rosbag2/issues/2030)_)
* Update [`index.ros.org/p/`` links for ``rosbag2_storage_mcap`` (`#2034 ](https://github.com/ros2/rosbag2/issues/2034)_)
* Contributors: Chris Lalancette, Christophe Bedard, Emerson Knapp, Michael Orlov, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_storage_sqlite3 <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_storage_sqlite3/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#2384 ](https://github.com/ros2/rosbag2/issues/2384)_)
* Implement circular logging by split count ([`--max-bag-files``) (`#2218 ](https://github.com/ros2/rosbag2/issues/2218)_)
* Add [`--max-cache-duration`` option for time-bounded snapshots (`#2289 ](https://github.com/ros2/rosbag2/issues/2289)_)
* Fix vulnerable string concatenation by using parameterized queries ([#2290 ](https://github.com/ros2/rosbag2/issues/2290)_)
* Remove sqlite3_vendor ([#2164 ](https://github.com/ros2/rosbag2/issues/2164)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Introduce new [`BaseWriteInterface`` methods ``write_messages`` and ``write_message`` to provide operation status, deprecating old write APIs (`#2030 ](https://github.com/ros2/rosbag2/issues/2030)_)
* Fix undefined behavior in the [`rosbag2_storage`` and ``rosbag2_storage_sqlite3`` packages (`#1997 ](https://github.com/ros2/rosbag2/issues/1997)_)
* Upstream quality changes from Apex.AI part-2 ([#1924 ](https://github.com/ros2/rosbag2/issues/1924)_)
* Contributors: Alejandro Hernández Cordero, Christophe Bedard, Emerson Knapp, Luke Sy, Michael Orlov, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_test_common <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_test_common/CHANGELOG.rst>`__

* Reduce flakiness in rosbag2 recorder end-to-end tests ([#2370 ](https://github.com/ros2/rosbag2/issues/2370)_)
* Use new ROSIDL aggregate CMake target ([#2384 ](https://github.com/ros2/rosbag2/issues/2384)_)
* Update Rosbag2 filename format to [`index+name+timestamp`` (`#2265 ](https://github.com/ros2/rosbag2/issues/2265)_)
* Update subscription callback signatures ([#2225 ](https://github.com/ros2/rosbag2/issues/2225)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Address test flakiness by waiting for executor spin ([#2001 ](https://github.com/ros2/rosbag2/issues/2001)_)
* Upstream quality changes from Apex.AI part-2 ([#1924 ](https://github.com/ros2/rosbag2/issues/1924)_)
* Use DDS queue depth for subscriptions as a maximum value across publishers ([#1960 ](https://github.com/ros2/rosbag2/issues/1960)_)
* Contributors: Christophe Bedard, Daisuke Sato, Emerson Knapp, Michael Orlov, mini-1235, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_test_msgdefs <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_test_msgdefs/CHANGELOG.rst>`__

* Support relative includes for IDL in local message definition ([#2241 ](https://github.com/ros2/rosbag2/issues/2241)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Add support for searching message definitions in nested subdirectories ([#2055 ](https://github.com/ros2/rosbag2/issues/2055)_)
* Contributors: Hunter L. Allen, Michael Orlov, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_tests <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_tests/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#2384 ](https://github.com/ros2/rosbag2/issues/2384)_)
* Update Rosbag2 filename format to [`index+name+timestamp`` (`#2265 ](https://github.com/ros2/rosbag2/issues/2265)_)
* Add static topics feature for recorder ([#2319 ](https://github.com/ros2/rosbag2/issues/2319)_)
* Add [`--max-cache-duration`` option for time-bounded snapshots (`#2289 ](https://github.com/ros2/rosbag2/issues/2289)_)
* Workaround flaky [`bagsize_split_is_at_least_specified_size`` test (`#2311 ](https://github.com/ros2/rosbag2/issues/2311)_)
* Add [`input_serialization_format`` and ``output_serialization_format`` to ``RecordOptions``, deprecating ``rmw_serialization_format`` (`#2215 ](https://github.com/ros2/rosbag2/issues/2215)_)
* Address recorder test flakiness by increasing cache size ([#2203 ](https://github.com/ros2/rosbag2/issues/2203)_)
* Use [`rclcpp typesupport helpers`` in ``rosbag2_cpp`` (`#2017 ](https://github.com/ros2/rosbag2/issues/2017)_)
* Expose more of the player and recorder API to Python, and improve signal handling ([#2062 ](https://github.com/ros2/rosbag2/issues/2062)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Fix deadlocks in Rosbag2 player when calling stop API ([#2057 ](https://github.com/ros2/rosbag2/issues/2057)_)
* Introduce new [`BaseWriteInterface`` methods ``write_messages`` and ``write_message`` to provide operation status, deprecating old write APIs (`#2030 ](https://github.com/ros2/rosbag2/issues/2030)_)
* Address test flakiness by waiting for executor spin ([#2001 ](https://github.com/ros2/rosbag2/issues/2001)_)
* Upstream quality changes from Apex.AI part-2 ([#1924 ](https://github.com/ros2/rosbag2/issues/1924)_)
* Contributors: Christophe Bedard, Daisuke Sato, Emerson Knapp, Michael Orlov, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_transport <https://github.com/ros2/rosbag2/tree/lyrical/rosbag2_transport/CHANGELOG.rst>`__

* Apply /bigobj to all MSVC builds in rosbag2_transport ([#2424 ](https://github.com/ros2/rosbag2/issues/2424)_) ([#2428 ](https://github.com/ros2/rosbag2/issues/2428)_)
* fix: Fixed compile errors in rosbag2_transport for MSVC 2022 and C++20 ([#2407 ](https://github.com/ros2/rosbag2/issues/2407)_)
* Fix QoS overrides ignored when topic name has no leading slash ([#2394 ](https://github.com/ros2/rosbag2/issues/2394)_)
* Refactor transient-local topic detection and logging in RecorderImpl ([#2395 ](https://github.com/ros2/rosbag2/issues/2395)_)
* Fix race condition in [`RecordSrvsSimTimeTest`` by waiting for clock subscriber (`#2396 ](https://github.com/ros2/rosbag2/issues/2396)_)
* Add [`--repeat-all-transient-local`` flag for automatic transient-local topic detection (`#2391 ](https://github.com/ros2/rosbag2/issues/2391)_)
* Repeat transient-local topics: Recorder, CLI, and Python bindings ([#2387 ](https://github.com/ros2/rosbag2/issues/2387)_)
* Implement [`transient-local topic`` repetition for Writer API and split/snapshot integration (`#2386 ](https://github.com/ros2/rosbag2/issues/2386)_)
* Add [`TransientLocalMessagesCache`` and ``RecordOptions`` for repeating transient-local topics (`#2385 ](https://github.com/ros2/rosbag2/issues/2385)_)
* Use new ROSIDL aggregate CMake target ([#2384 ](https://github.com/ros2/rosbag2/issues/2384)_)
* Address flakiness in the [`rosbag2_transport::test_record_services`` tests (`#2368 ](https://github.com/ros2/rosbag2/issues/2368)_)
* Add support for time based Resume service ([#2357 ](https://github.com/ros2/rosbag2/issues/2357)_)
* Address race condition in the [`wait_for_playback_to_start()`` function (`#2344 ](https://github.com/ros2/rosbag2/issues/2344)_)
* Add [`set_on_start_recording_callback()`` to set the callback for when recording starts (`#2340 ](https://github.com/ros2/rosbag2/issues/2340)_)
* Remove unnecessary dependencies on [`yaml_cpp_vendor`` (`#2353 ](https://github.com/ros2/rosbag2/issues/2353)_)
* Allow pause/resume service calls while not in recording ([#2349 ](https://github.com/ros2/rosbag2/issues/2349)_)
* Implement delayed and time-based recorder and player services, adding new bag split modes ([#2330 ](https://github.com/ros2/rosbag2/issues/2330)_)
* Update Rosbag2 filename format to [`index+name+timestamp`` (`#2265 ](https://github.com/ros2/rosbag2/issues/2265)_)
* Address a possible deadlock in [`seek(timestamp)`` (`#2345 ](https://github.com/ros2/rosbag2/issues/2345)_)
* Add missing fields to [`RecordOptions`` YAML encode/decode functions and include a compile-time safeguard (`#2334 ](https://github.com/ros2/rosbag2/issues/2334)_)
* Implement circular logging by split count ([`--max-bag-files``) (`#2218 ](https://github.com/ros2/rosbag2/issues/2218)_)
* Improve [`ros2 bag convert`` performance for fragment cutting and add ``--input-options`` (`#2325 ](https://github.com/ros2/rosbag2/issues/2325)_)
* Add static topics feature for recorder ([#2319 ](https://github.com/ros2/rosbag2/issues/2319)_)
* Add [`--max-cache-duration`` option for time-bounded snapshots (`#2289 ](https://github.com/ros2/rosbag2/issues/2289)_)
* Fix the flaky [`can_record_again_after_stop`` test (`#2313 ](https://github.com/ros2/rosbag2/issues/2313)_)
* Add error return code to the [`~/stop`` service request (`#2312 ](https://github.com/ros2/rosbag2/issues/2312)_)
* Add Record, Stop, StartDiscovery, StopDiscovery, and IsDiscoveryRunning services for Recorder ([#2248 ](https://github.com/ros2/rosbag2/issues/2248)_)
* Use QoS override settings for inner Rosbag2 publishing topics ([#2286 ](https://github.com/ros2/rosbag2/issues/2286)_)
* Fix decoder and encode mismatch in YAML deserialization ([#2277 ](https://github.com/ros2/rosbag2/issues/2277)_)
* Incorporate upstream minor fixes from Apex.AI ([#2240 ](https://github.com/ros2/rosbag2/issues/2240)_)
* Fix macOS build: Disable thread-safety annotations in [`locked_priority_queue.hpp`` (`#2245 ](https://github.com/ros2/rosbag2/issues/2245)_)
* Fix C++ Recorder failure when stop() then record() are called with the same bag name ([#2224 ](https://github.com/ros2/rosbag2/issues/2224)_)
* Add a direct API for [`rosbag2_transport::Recorder`` (`#2221 ](https://github.com/ros2/rosbag2/issues/2221)_)
* Add [`input_serialization_format`` and ``output_serialization_format`` to ``RecordOptions``, deprecating ``rmw_serialization_format`` (`#2215 ](https://github.com/ros2/rosbag2/issues/2215)_)
* Enable RMW communication isolation in rosbag2_transport tests ([#2190 ](https://github.com/ros2/rosbag2/issues/2190)_)
* Add topic name and type delimiter for hash map keys to avoid collisions ([#2210 ](https://github.com/ros2/rosbag2/issues/2210)_)
* Add cache for [`TopicFilter`` to avoid performance burden on discovery (`#1486 ](https://github.com/ros2/rosbag2/issues/1486)_)
* Address recorder test flakiness by increasing cache size ([#2203 ](https://github.com/ros2/rosbag2/issues/2203)_)
* Reduce CPU overhead in Rosbag2 recorder discovery by improving discovery logic ([#2201 ](https://github.com/ros2/rosbag2/issues/2201)_)
* Fix data races in [`PlayerProgressBar`` using atomic variables (`#2194 ](https://github.com/ros2/rosbag2/issues/2194)_)
* Fix data races in tests with [`MockSequentialWriter`` (`#2192 ](https://github.com/ros2/rosbag2/issues/2192)_)
* Player now respects original message order for same timestamps ([#2172 ](https://github.com/ros2/rosbag2/issues/2172)_)
* Return player storage options by value in [`get_storage_options()`` to avoid dangling reference (`#2181 ](https://github.com/ros2/rosbag2/issues/2181)_)
* Fix player not playing when [`read_ahead_queue_size`` equals 1 (`#2174 ](https://github.com/ros2/rosbag2/issues/2174)_)
* Fix multiple race conditions and a deadlock in the player ([#2171 ](https://github.com/ros2/rosbag2/issues/2171)_)
* Fix multibag replay stagnation and improve playback performance by managing chronological message order with [`ReadersManager`` (`#2158 ](https://github.com/ros2/rosbag2/issues/2158)_)
* Fix MCAPStorage::seek(time) to advance when timestamp matches current time ([#2157 ](https://github.com/ros2/rosbag2/issues/2157)_)
* Publish messages lost statistics to 'events/messages_lost' topic ([#2150 ](https://github.com/ros2/rosbag2/issues/2150)_)
* Add [`RecorderEventNotifier`` class (`#2144 ](https://github.com/ros2/rosbag2/issues/2144)_)
* Resolve deadlock during multibag replay and update [`wait_for_playback_to_start`` (`#2143 ](https://github.com/ros2/rosbag2/issues/2143)_)
* Use [`rclcpp typesupport helpers`` in ``rosbag2_cpp`` (`#2017 ](https://github.com/ros2/rosbag2/issues/2017)_)
* Fix callback not called for MESSAGES_LOST event ([#2105 ](https://github.com/ros2/rosbag2/issues/2105)_)
* Add public API for player's starting time and playback duration ([#2095 ](https://github.com/ros2/rosbag2/issues/2095)_)
* Fix CMAKE deprecation ([#2067 ](https://github.com/ros2/rosbag2/issues/2067)_)
* Fix deadlocks in Rosbag2 player when calling stop API ([#2057 ](https://github.com/ros2/rosbag2/issues/2057)_)
* Add message loss statistics callbacks and logging ([#2039 ](https://github.com/ros2/rosbag2/issues/2039)_)
* Skip flaky [`can_record_again_after_stop`` test (`#2031 ](https://github.com/ros2/rosbag2/issues/2031)_)
* Fix [`cout`` output when progress bar is disabled (`#2024 ](https://github.com/ros2/rosbag2/issues/2024)_)
* Improve message publishing timing by avoiding sporadic wakeups and fixing incorrect intervals on player start ([#2025 ](https://github.com/ros2/rosbag2/issues/2025)_)
* Fix [`playing_respects_delay`` test flakiness (`#2016 ](https://github.com/ros2/rosbag2/issues/2016)_)
* Address test flakiness by waiting for executor spin ([#2001 ](https://github.com/ros2/rosbag2/issues/2001)_)
* Avoid sending non-existent cancel requests ([#2005 ](https://github.com/ros2/rosbag2/issues/2005)_)
* Fix a maybe-uninitialized warning in player_action_client.cpp ([#1969 ](https://github.com/ros2/rosbag2/issues/1969)_)
* Upstream quality changes from Apex.AI part-2 ([#1924 ](https://github.com/ros2/rosbag2/issues/1924)_)
* Bugfix: [`ros2 bag convert`` dropping messages with compression mode message (`#1975 ](https://github.com/ros2/rosbag2/issues/1975)_)
* Use DDS queue depth for subscriptions as a maximum value across publishers ([#1960 ](https://github.com/ros2/rosbag2/issues/1960)_)
* Contributors: Barry Xu, Chris Lalancette, Christophe Bedard, Daisuke Sato, DangitBen, Dhruv Patel, Emerson Knapp, Janosch Machowinski, Luke Sy, Michael Carroll, Michael Orlov, Sahil Lakhmani, Scott K Logan, Shane Loretz, Tomoya Fujita, Tony Najjar, baranbologur, carlos-apex, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosgraph_msgs <https://github.com/ros2/rcl_interfaces/tree/lyrical/rosgraph_msgs/CHANGELOG.rst>`__

* Actually build the new graph description messages ([#192 ](https://github.com/ros2/rcl_interfaces/issues/192)_) ([#198 ](https://github.com/ros2/rcl_interfaces/issues/198)_)
* Add Graph description messages to [`rosgraph_msgs`` (`#188 ](https://github.com/ros2/rcl_interfaces/issues/188)_)
* Fix cmake deprecation ([#180 ](https://github.com/ros2/rcl_interfaces/issues/180)_)
* Contributors: Emerson Knapp, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_adapter <https://github.com/ros2/rosidl/tree/lyrical/rosidl_adapter/CHANGELOG.rst>`__

* Fix future regressions on flake8 ([#936 ](https://github.com/ros2/rosidl//issues/936)_)
* Fix @optional for string literals ([#905 ](https://github.com/ros2/rosidl/issues/905)_)
* Export typing Information ([#903 ](https://github.com/ros2/rosidl/issues/903)_)
* Add Optional Parsing ([#883 ](https://github.com/ros2/rosidl/issues/883)_)
* Uniform cmake minVersion ([#849 ](https://github.com/ros2/rosidl/issues/849)_)
* Contributors: Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_buffer <https://github.com/ros2/rosidl/tree/lyrical/rosidl_buffer/CHANGELOG.rst>`__

* Add missing std::vector compatible APIs to rosidl::Buffer ([#959 ](https://github.com/ros2/rosidl/issues/959)_)
* Bump rosidl_buffer min CMake version ([#956 ](https://github.com/ros2/rosidl/issues/956)_)
* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942 ](https://github.com/ros2/rosidl/issues/942)_)
* Add cstdint include to c_helpers.cpp ([#953 ](https://github.com/ros2/rosidl/issues/953)_)
* Add rosidl_buffer and rosidl_buffer_backend for native Buffer type support ([#941 ](https://github.com/ros2/rosidl/issues/941)_)
* Contributors: CY Chen, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_buffer_backend <https://github.com/ros2/rosidl/tree/lyrical/rosidl_buffer_backend/CHANGELOG.rst>`__

* Clarify return of get_descriptor_type_support() ([#958 ](https://github.com/ros2/rosidl/issues/958)_)
* Bump rosidl_buffer min CMake version ([#956 ](https://github.com/ros2/rosidl/issues/956)_)
* Add rosidl_buffer and rosidl_buffer_backend for native Buffer type support ([#941 ](https://github.com/ros2/rosidl/issues/941)_)
* Contributors: CY Chen, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_buffer_backend_registry <https://github.com/ros2/rosidl/tree/lyrical/rosidl_buffer_backend_registry/CHANGELOG.rst>`__

* Add missing ament_cmake_gtest dep ([#960 ](https://github.com/ros2/rosidl/issues/960)_)
* Bump rosidl_buffer min CMake version ([#956 ](https://github.com/ros2/rosidl/issues/956)_)
* Add rosidl_buffer_backend_registry ([#944 ](https://github.com/ros2/rosidl/issues/944)_)
* Contributors: CY Chen, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_buffer_py <https://github.com/ros2/rosidl/tree/lyrical/rosidl_buffer_py/CHANGELOG.rst>`__

* Bump rosidl_buffer min CMake version ([#956 ](https://github.com/ros2/rosidl/issues/956)_)
* Fix pybind11 rosdep key ([#955 ](https://github.com/ros2/rosidl/issues/955)_)
* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942 ](https://github.com/ros2/rosidl/issues/942)_)
* Contributors: CY Chen, Christoph Fröhlich, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_cli <https://github.com/ros2/rosidl/tree/lyrical/rosidl_cli/CHANGELOG.rst>`__

* Fix future regressions on flake8 ([#936 ](https://github.com/ros2/rosidl//issues/936)_)
* remove importlib-metadata ([#917 ](https://github.com/ros2/rosidl/issues/917)_)
* Export typing Information ([#903 ](https://github.com/ros2/rosidl/issues/903)_)
* fix setuptools deprecations ([#877 ](https://github.com/ros2/rosidl/issues/877)_)
* rosidl_cli: Add type description support ([#857 ](https://github.com/ros2/rosidl/issues/857)_)
* Contributors: Francisco Rossi, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_cmake <https://github.com/ros2/rosidl/tree/lyrical/rosidl_cmake/CHANGELOG.rst>`__

* Install interface files to same folder as idl ([#935 ](https://github.com/ros2/rosidl/issues/935)_)
* Create an aggregate target for rosidl generated interfaces targets ([#947 ](https://github.com/ros2/rosidl//issues/947)_)
* Add [`rosidl_auto_generate_interfaces`` function (`#918 ](https://github.com/ros2/rosidl/issues/918)_)
* Export typing Information ([#903 ](https://github.com/ros2/rosidl/issues/903)_)
* remove deprecated rosidl_target_interfaces. ([#898 ](https://github.com/ros2/rosidl/issues/898)_)
* fix cmake <3.10 deprecation ([#875 ](https://github.com/ros2/rosidl/issues/875)_)
* Contributors: Emerson Knapp, Kotaro Yoshimoto, Michael Carlstrom, Tim Wendt, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_core_generators <https://github.com/ros2/rosidl_core/tree/lyrical/rosidl_core_generators/CHANGELOG.rst>`__

* Revert "Revert "Added rosidl_generator_rs ([#7 ](https://github.com/ros2/rosidl_core/issues/7)_)" ([#8 ](https://github.com/ros2/rosidl_core/issues/8)_)" ([#9 ](https://github.com/ros2/rosidl_core/issues/9)_)
* fix cmake deprecation ([#10 ](https://github.com/ros2/rosidl_core/issues/10)_)
* Contributors: Esteve Fernandez, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_core_runtime <https://github.com/ros2/rosidl_core/tree/lyrical/rosidl_core_runtime/CHANGELOG.rst>`__

* Add rosidl_buffer_py as build_export_depend with explicit group resolution ([#14 ](https://github.com/ros2/rosidl_core/issues/14)_)
* fix cmake deprecation ([#10 ](https://github.com/ros2/rosidl_core/issues/10)_)
* Contributors: CY Chen, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_default_generators <https://github.com/ros2/rosidl_defaults/tree/lyrical/rosidl_default_generators/CHANGELOG.rst>`__

* fix cmake deprecation ([#31 ](https://github.com/ros2/rosidl_defaults/issues/31)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_default_runtime <https://github.com/ros2/rosidl_defaults/tree/lyrical/rosidl_default_runtime/CHANGELOG.rst>`__

* fix cmake deprecation ([#31 ](https://github.com/ros2/rosidl_defaults/issues/31)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_dynamic_typesupport <https://github.com/ros2/rosidl_dynamic_typesupport/tree/lyrical/CHANGELOG.rst>`__

* Don't automatically enable verbose makefiles ([#17 ](https://github.com/ros2/rosidl_dynamic_typesupport/issues/17)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_dynamic_typesupport_fastrtps <https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/tree/lyrical/CHANGELOG.rst>`__

* Merge pull request [#11 ](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/11)_ from mosfet80/patch-1
* Don't automatically enable verbose makefiles. ([#9 ](https://github.com/ros2/rosidl_dynamic_typesupport_fastrtps/issues/9)_)
* Contributors: Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_c <https://github.com/ros2/rosidl/tree/lyrical/rosidl_generator_c/CHANGELOG.rst>`__

* Export typing Information ([#903 ](https://github.com/ros2/rosidl/issues/903)_)
* Uniform cmake minVersion ([#849 ](https://github.com/ros2/rosidl/issues/849)_)
* rosidl_cli: Add type description support ([#857 ](https://github.com/ros2/rosidl/issues/857)_)
* Contributors: Francisco Rossi, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_cpp <https://github.com/ros2/rosidl/tree/lyrical/rosidl_generator_cpp/CHANGELOG.rst>`__

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942 ](https://github.com/ros2/rosidl/issues/942)_)
* Use IWYU pragma export to avoid clangd warnings for generated headers ([#902 ](https://github.com/ros2/rosidl//issues/902)_)
* rosidl_generator_cpp: constexpr message traits and to_tuple_ref for generated structs ([#928 ](https://github.com/ros2/rosidl//issues/928)_)
* Make [`data_type`` and ``name`` traits constexpr (`#929 ](https://github.com/ros2/rosidl//issues/929)_)
* Export typing Information ([#903 ](https://github.com/ros2/rosidl/issues/903)_)
* Add static_cast ([#884 ](https://github.com/ros2/rosidl/issues/884)_)
* Uniform cmake minVersion ([#849 ](https://github.com/ros2/rosidl/issues/849)_)
* rosidl_cli: Add type description support ([#857 ](https://github.com/ros2/rosidl/issues/857)_)
* Add missing cstdint include ([#864 ](https://github.com/ros2/rosidl/issues/864)_)
* Removed deprecated methods ([#863 ](https://github.com/ros2/rosidl/issues/863)_)
* Contributors: Adam Leeper, Alejandro Hernández Cordero, CY Chen, Francisco Rossi, Michael Carlstrom, mosfet80, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_dds_idl <https://github.com/ros2/rosidl_dds/tree/lyrical/rosidl_generator_dds_idl/CHANGELOG.rst>`__

* Update cmake version requirements ([#64 ](https://github.com/ros2/rosidl_dds/issues/64)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_py <https://github.com/ros2/rosidl_python/tree/lyrical/rosidl_generator_py/CHANGELOG.rst>`__

* Use absolute names for type hints ([#258 ](https://github.com/ros2/rosidl_python/issues/258)_)
* Feature: add depends flag for ament_python_install_package ([#254 ](https://github.com/ros2/rosidl_python/issues/254)_)
* Add support for rosidl::Buffer in rosidl Python path for rclpy ([#250 ](https://github.com/ros2/rosidl_python/issues/250)_)
* Cast Sequence to list on assignment (with templates) ([#249 ](https://github.com/ros2/rosidl_python/issues/249)_)
* Fix linter violations with flake8-import-order 0.19.0 ([#248 ](https://github.com/ros2/rosidl_python/issues/248)_)
* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies ([#238 ](https://github.com/ros2/rosidl_python/issues/238)_)
* Deprecate using set for container based input ([#243 ](https://github.com/ros2/rosidl_python//issues/243)_)
* Update to use new BaseImpl ([#241 ](https://github.com/ros2/rosidl_python/issues/241)_)
* remove second call ([#232 ](https://github.com/ros2/rosidl_python/issues/232)_)
* Derive Messages from Base Classes ([#230 ](https://github.com/ros2/rosidl_python/issues/230)_)
* Remove NoReturn for now ([#229 ](https://github.com/ros2/rosidl_python/issues/229)_)
* Static typing for Message, Services, and Actions ([#206 ](https://github.com/ros2/rosidl_python/issues/206)_)
* Contributors: Anthony Welte, CY Chen, Michael Carlstrom, Nadav Elkabets


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_rs <https://github.com/ros2-rust/rosidl_rust/tree/main/rosidl_generator_rs/CHANGELOG.rst>`__

* fix(rosidl_generator_rs_generate_interfaces): Remove poisoning of global CMAKE_SHARED_LINKER_FLAGS variable (#22)
* Change the package metadata to point to the new ros-env crate (#21)
* Fix TransientParseError on Ubuntu Resolute (#20)
* fix: do not monkey-patch _removesuffix into str ([#18 ](https://github.com/ros2-rust/rosidl_rust/issues/18)_)
* fix: add str.removesuffix() backport for Python < 3.9 (RHEL 8) ([#17 ](https://github.com/ros2-rust/rosidl_rust/issues/17)_)
* feat: relative Module Path Resolution ([#12 ](https://github.com/ros2-rust/rosidl_rust/issues/12)_) * Changed all generated code to use relative symbols instead of ``crate::`` ones. Reworked the rosidl_generator_rs slightly to be a bit simpler. Separate actual templates from the files that reuse them. * WIP For adding documentation to all structs, members, and constants generated from idl's. * Clean up all the surfaced warnings from generated code.
* build: update rosidl_runtime_rs dependency version to 0.6 ([#14 ](https://github.com/ros2-rust/rosidl_rust/issues/14)_)
* fix: update rosidl_runtime_rs dependency version to 0.5 ([#11 ](https://github.com/ros2-rust/rosidl_rust/issues/11)_)
* Fix use of serde ([#9 ](https://github.com/ros2-rust/rosidl_rust/issues/9)_) * Fix use of serde * Include serde for services ---------
* Update to the latest version of Action trait ([#7 ](https://github.com/ros2-rust/rosidl_rust/issues/7)_) * Update to the latest version of Action trait * Fix use of serde ---------
* fix cmake deprecation ([#6 ](https://github.com/ros2-rust/rosidl_rust/issues/6)_) * fix cmake deprecation cmake version < then 3.10 is deprecated * Update CMakeLists.txt
* fix: clean up dependencies ([#5 ](https://github.com/ros2-rust/rosidl_rust/issues/5)_)
* fix: added missing dependency
* clean up changelog. Removed rosidl_runtime_rs as a dependency
* set python executable var to custom cmake commands ([#3 ](https://github.com/ros2-rust/rosidl_rust/issues/3)_)
* Contributors: Esteve Fernandez, Grey, Kimberly N. McGuire, Sam Privett, Shane Loretz, Silvio Traversaro, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_tests <https://github.com/ros2/rosidl/tree/lyrical/rosidl_generator_tests/CHANGELOG.rst>`__

* Use new aggregate rosidl target instead of _TARGETS ([#952 ](https://github.com/ros2/rosidl/issues/952)_)
* rosidl_generator_cpp: constexpr message traits and to_tuple_ref for generated structs ([#928 ](https://github.com/ros2/rosidl//issues/928)_)
* Make [`data_type`` and ``name`` traits constexpr (`#929 ](https://github.com/ros2/rosidl//issues/929)_)
* fix cmake <3.10 deprecation ([#875 ](https://github.com/ros2/rosidl/issues/875)_)
* Contributors: Alexis Tsogias, Michael Carlstrom, mosfet80, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_type_description <https://github.com/ros2/rosidl/tree/lyrical/rosidl_generator_type_description/CHANGELOG.rst>`__

* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies ([#910 ](https://github.com/ros2/rosidl//issues/910)_)
* Add missing dependency on ament_cmake_pytest ([#914 ](https://github.com/ros2/rosidl/issues/914)_)
* Export typing Information ([#903 ](https://github.com/ros2/rosidl/issues/903)_)
* Uniform cmake minVersion ([#849 ](https://github.com/ros2/rosidl/issues/849)_)
* rosidl_cli: Add type description support ([#857 ](https://github.com/ros2/rosidl/issues/857)_)
* Contributors: Anthony Welte, Francisco Rossi, Michael Carlstrom, Scott K Logan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_parser <https://github.com/ros2/rosidl/tree/lyrical/rosidl_parser/CHANGELOG.rst>`__

* Fix future regressions on flake8 ([#936 ](https://github.com/ros2/rosidl//issues/936)_)
* Add Optional Parsing ([#883 ](https://github.com/ros2/rosidl/issues/883)_)
* fix cmake <3.10 deprecation ([#875 ](https://github.com/ros2/rosidl/issues/875)_)
* Contributors: Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_pycommon <https://github.com/ros2/rosidl/tree/lyrical/rosidl_pycommon/CHANGELOG.rst>`__

* fix regressions ([#951 ](https://github.com/ros2/rosidl/issues/951)_)
* Fix future regressions on flake8 ([#936 ](https://github.com/ros2/rosidl//issues/936)_)
* Add BaseImpl ([#912 ](https://github.com/ros2/rosidl/issues/912)_)
* Export typing Information ([#903 ](https://github.com/ros2/rosidl/issues/903)_)
* Provide base classes in [`rosidl_pycommon`` (`#887 ](https://github.com/ros2/rosidl/issues/887)_)
* fix setuptools deprecation ([#880 ](https://github.com/ros2/rosidl/issues/880)_)
* Contributors: Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_runtime_c <https://github.com/ros2/rosidl/tree/lyrical/rosidl_runtime_c/CHANGELOG.rst>`__

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942 ](https://github.com/ros2/rosidl/issues/942)_)
* Fix copy/paste errors in type support docs ([#906 ](https://github.com/ros2/rosidl/issues/906)_)
* fix cmake <3.10 deprecation ([#875 ](https://github.com/ros2/rosidl/issues/875)_)
* Add an ament_cmake_gtest dependency to rosidl_runtime_c. ([#865 ](https://github.com/ros2/rosidl/issues/865)_)
* Contributors: CY Chen, Chris Lalancette, Christophe Bedard, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_runtime_cpp <https://github.com/ros2/rosidl/tree/lyrical/rosidl_runtime_cpp/CHANGELOG.rst>`__

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942 ](https://github.com/ros2/rosidl/issues/942)_)
* rosidl_generator_cpp: constexpr message traits and to_tuple_ref for generated structs ([#928 ](https://github.com/ros2/rosidl//issues/928)_)
* Make [`data_type`` and ``name`` traits constexpr (`#929 ](https://github.com/ros2/rosidl//issues/929)_)
* fix cmake <3.10 deprecation ([#875 ](https://github.com/ros2/rosidl/issues/875)_)
* Add missing cstdint include ([#864 ](https://github.com/ros2/rosidl/issues/864)_)
* Contributors: CY Chen, Michael Carlstrom, mosfet80, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_runtime_py <https://github.com/ros2/rosidl_runtime_py/tree/lyrical/CHANGELOG.rst>`__

* Add support for rosidl::Buffer in rosidl Python path for rclpy ([#39 ](https://github.com/ros2/rosidl_runtime_py/issues/39)_)
* Fix flake8 ([#40 ](https://github.com/ros2/rosidl_runtime_py/issues/40)_)
* Add py.typed to the package ([#37 ](https://github.com/ros2/rosidl_runtime_py/issues/37)_)
* fix setuptools deprecations ([#35 ](https://github.com/ros2/rosidl_runtime_py/issues/35)_)
* Contributors: CY Chen, Michael Carlstrom, Vladimir Gerts, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_c <https://github.com/ros2/rosidl_typesupport/tree/lyrical/rosidl_typesupport_c/CHANGELOG.rst>`__

* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies ([#168 ](https://github.com/ros2/rosidl_typesupport/issues/168)_)
* Contributors: Anthony Welte


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_cpp <https://github.com/ros2/rosidl_typesupport/tree/lyrical/rosidl_typesupport_cpp/CHANGELOG.rst>`__

* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies ([#168 ](https://github.com/ros2/rosidl_typesupport/issues/168)_)
* Remove deprecated rosidl_typesupport_cpp/type_support_map.h ([#167 ](https://github.com/ros2/rosidl_typesupport/issues/167)_)
* De-duplicate type_support_map.h header ([#81 ](https://github.com/ros2/rosidl_typesupport/issues/81)_)
* Contributors: Anthony Welte, Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_fastrtps_c <https://github.com/ros2/rosidl_typesupport_fastrtps/tree/lyrical/rosidl_typesupport_fastrtps_c/CHANGELOG.rst>`__

* Update rosidl typesupport to support rosidl::Buffer in nested uint8[] ([#151 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/151)_) ([#152 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/152)_)
* Add support for rosidl::Buffer type serialization ([#144 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/144)_)
* use variable to control shared/static build type ([#138 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/138)_)
* Switch ament_index_python and rosidl_cli to exec_depend. ([#137 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/137)_)
* Removed deprecated code ([#135 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/135)_)
* fix cmake deprecation ([#134 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/134)_)
* Check remaining size before resizing sequences ([#130 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/130)_)
* Contributors: Alejandro Hernández Cordero, Anthony Welte, CY Chen, Chris Lalancette, Jay Sridharan, Miguel Company, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_fastrtps_cpp <https://github.com/ros2/rosidl_typesupport_fastrtps/tree/lyrical/rosidl_typesupport_fastrtps_cpp/CHANGELOG.rst>`__

* Clean up logs in buffer serialization functions ([#153 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/153)_) ([#154 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/154)_)
* Update rosidl typesupport to support rosidl::Buffer in nested uint8[] ([#151 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/151)_) ([#152 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/152)_)
* Add missing build dependencies for exported dependencies ([#149 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/149)_)
* Add support for rosidl::Buffer type serialization ([#144 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/144)_)
* use variable to control shared/static build type ([#138 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/138)_)
* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies ([#136 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/136)_)
* Switch ament_index_python and rosidl_cli to exec_depend. ([#137 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/137)_)
* Removed deprecated code ([#135 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/135)_)
* fix cmake deprecation ([#134 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/134)_)
* Check remaining size before resizing sequences ([#130 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/130)_)
* Contributors: Alejandro Hernández Cordero, Anthony Welte, CY Chen, Chris Lalancette, Jay Sridharan, Miguel Company, Scott K Logan, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_interface <https://github.com/ros2/rosidl/tree/lyrical/rosidl_typesupport_interface/CHANGELOG.rst>`__

* fix cmake <3.10 deprecation ([#875 ](https://github.com/ros2/rosidl/issues/875)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_introspection_c <https://github.com/ros2/rosidl/tree/lyrical/rosidl_typesupport_introspection_c/CHANGELOG.rst>`__

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942 ](https://github.com/ros2/rosidl/issues/942)_)
* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies ([#910 ](https://github.com/ros2/rosidl//issues/910)_)
* Export typing Information ([#903 ](https://github.com/ros2/rosidl/issues/903)_)
* Uniform cmake minVersion ([#849 ](https://github.com/ros2/rosidl/issues/849)_)
* rosidl_cli: Add type description support ([#857 ](https://github.com/ros2/rosidl/issues/857)_)
* Contributors: Anthony Welte, CY Chen, Francisco Rossi, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_introspection_cpp <https://github.com/ros2/rosidl/tree/lyrical/rosidl_typesupport_introspection_cpp/CHANGELOG.rst>`__

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942 ](https://github.com/ros2/rosidl/issues/942)_)
* Add DEPENDS_EXPLICIT_ONLY to remove implicit dependencies ([#910 ](https://github.com/ros2/rosidl//issues/910)_)
* Export typing Information ([#903 ](https://github.com/ros2/rosidl/issues/903)_)
* Uniform cmake minVersion ([#849 ](https://github.com/ros2/rosidl/issues/849)_)
* rosidl_cli: Add type description support ([#857 ](https://github.com/ros2/rosidl/issues/857)_)
* Contributors: Anthony Welte, CY Chen, Francisco Rossi, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_introspection_tests <https://github.com/ros2/rosidl/tree/lyrical/rosidl_typesupport_introspection_tests/CHANGELOG.rst>`__

* Update rosidl cpp path to emit rosidl::Buffer for uint8[] type ([#942 ](https://github.com/ros2/rosidl/issues/942)_)
* fix cmake <3.10 deprecation ([#875 ](https://github.com/ros2/rosidl/issues/875)_)
* Disable test failing in coverage jobs, see [#812 ](https://github.com/ros2/rosidl/issues/812)_ ([#853 ](https://github.com/ros2/rosidl/issues/853)_)
* Contributors: CY Chen, Jorge J. Perez, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_tests <https://github.com/ros2/rosidl_typesupport/tree/lyrical/rosidl_typesupport_tests/CHANGELOG.rst>`__

* pass all tests for rmw_cyclonedds_cpp. ([#171 ](https://github.com/ros2/rosidl_typesupport/issues/171)_)
* Contributors: Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rpyutils <https://github.com/ros2/rpyutils/tree/lyrical/CHANGELOG.rst>`__

* Enforce ament_mypy --ament-strict ([#22 ](https://github.com/ros2/rpyutils/issues/22)_)
* fix setuptools deprecations ([#17 ](https://github.com/ros2/rpyutils/issues/17)_)
* Contributors: Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt <https://github.com/ros-visualization/rqt/tree/lyrical/rqt/CHANGELOG.rst>`__

* fix setuptools deprecations ([#334 ](https://github.com/ros-visualization/rqt/issues/334)_)
* fix setuptools deprecations ([#329 ](https://github.com/ros-visualization/rqt/issues/329)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_action <https://github.com/ros-visualization/rqt_action/tree/lyrical/CHANGELOG.rst>`__

* fix setuptools deprecations ([#19 ](https://github.com/ros-visualization/rqt_action/issues/19)_)
* Remove CODEOWNERS and mirror-rolling-to-main workflow ([#16 ](https://github.com/ros-visualization/rqt_action/issues/16)_)
* Contributors: Alejandro Hernández Cordero, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_bag <https://github.com/ros-visualization/rqt_bag/tree/lyrical/rqt_bag/CHANGELOG.rst>`__

* Fix Qt6 issues (backport [#207 ](https://github.com/ros-visualization/rqt_bag/issues/207)_) ([#208 ](https://github.com/ros-visualization/rqt_bag/issues/208)_)
* Support Qt6 ([#206 ](https://github.com/ros-visualization/rqt_bag/issues/206)_)
* Cleanup mislabeled BSD license ([#205 ](https://github.com/ros-visualization/rqt_bag/issues/205)_)
* Better handling of large bag files ([#178 ](https://github.com/ros-visualization/rqt_bag/issues/178)_)
* Display roll, pitch, yaw values for quaternions ([#179 ](https://github.com/ros-visualization/rqt_bag/issues/179)_)
* Fix flake8 error in setup.py ([#192 ](https://github.com/ros-visualization/rqt_bag/issues/192)_)
* Improved raw view to better handle arrays and time objects ([#173 ](https://github.com/ros-visualization/rqt_bag/issues/173)_)
* plot_view: Fixed display of initial message ([#180 ](https://github.com/ros-visualization/rqt_bag/issues/180)_)
* fix setuptools deprecations ([#185 ](https://github.com/ros-visualization/rqt_bag/issues/185)_)
* Fixed timeline resolution ([#175 ](https://github.com/ros-visualization/rqt_bag/issues/175)_)
* Contributors: Alejandro Hernández Cordero, Martin Pecka, Michael Carlstrom, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_bag_plugins <https://github.com/ros-visualization/rqt_bag/tree/lyrical/rqt_bag_plugins/CHANGELOG.rst>`__

* Support Qt6 ([#206 ](https://github.com/ros-visualization/rqt_bag/issues/206)_)
* Display roll, pitch, yaw values for quaternions ([#179 ](https://github.com/ros-visualization/rqt_bag/issues/179)_)
* Fix flake8 error in setup.py ([#192 ](https://github.com/ros-visualization/rqt_bag/issues/192)_)
* Fixed image helper and added support for PNG-coded compressedDepth ([#176 ](https://github.com/ros-visualization/rqt_bag/issues/176)_)
* Improve plot view ([#174 ](https://github.com/ros-visualization/rqt_bag/issues/174)_)
* plot_view: Fixed display of initial message ([#180 ](https://github.com/ros-visualization/rqt_bag/issues/180)_)
* fix setuptools deprecations ([#185 ](https://github.com/ros-visualization/rqt_bag/issues/185)_)
* Contributors: Alejandro Hernández Cordero, Martin Pecka, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_console <https://github.com/ros-visualization/rqt_console/tree/lyrical/CHANGELOG.rst>`__

* Support Qt6 ([#58 ](https://github.com/ros-visualization/rqt_console/issues/58)_)
* fixed copyright test ([#57 ](https://github.com/ros-visualization/rqt_console/issues/57)_)
* added copyright header
* fixed flake8 ([#56 ](https://github.com/ros-visualization/rqt_console/issues/56)_)
* fixed flake8
* remove residual imports in colored output test-file ([#55 ](https://github.com/ros-visualization/rqt_console/issues/55)_)
* remove residual imports
* basic support for colors and bold/bright using ANSI escape codes ([#54 ](https://github.com/ros-visualization/rqt_console/issues/54)_)
* replace colorama dependency with manual ansi codes
* add checkbox in the settings
* support more color codes
* basic support for colors and bold/bright
* fix setuptools deprecations ([#50 ](https://github.com/ros-visualization/rqt_console/issues/50)_)
* Contributors: Alejandro Hernández Cordero, Arne Hitzmann, Peter, mosfet80, peter


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_graph <https://github.com/ros-visualization/rqt_graph/tree/lyrical/CHANGELOG.rst>`__

* Support Wheel event in qt6 (backport [#116 ](https://github.com/ros-visualization/rqt_graph/issues/116)_) ([#117 ](https://github.com/ros-visualization/rqt_graph/issues/117)_)
* Fix: broken dependency ([#115 ](https://github.com/ros-visualization/rqt_graph//issues/115)_)
* Support Qt6 ([#114 ](https://github.com/ros-visualization/rqt_graph//issues/114)_)
* add warning for type incompatibilities ([#105 ](https://github.com/ros-visualization/rqt_graph/issues/105)_)
* Remove rqt_graph script. ([#66 ](https://github.com/ros-visualization/rqt_graph/issues/66)_)
* fix setuptools deprecations ([#107 ](https://github.com/ros-visualization/rqt_graph/issues/107)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jonas Otto, Matthew Foran, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_gui <https://github.com/ros-visualization/rqt/tree/lyrical/rqt_gui/CHANGELOG.rst>`__

* Fix setupTools deprecations ([#322 ](https://github.com/ros-visualization/rqt/issues/322)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_gui_cpp <https://github.com/ros-visualization/rqt/tree/lyrical/rqt_gui_cpp/CHANGELOG.rst>`__

* Cleanup headers ([#347 ](https://github.com/ros-visualization/rqt/issues/347)_) ([#350 ](https://github.com/ros-visualization/rqt/issues/350)_)
* Use qt-base-dev / libqtwidgets ([#345 ](https://github.com/ros-visualization/rqt/issues/345)_)
* fix: include unistd.h for getpid ([#341 ](https://github.com/ros-visualization/rqt/issues/341)_)
* Support Qt6 ([#339 ](https://github.com/ros-visualization/rqt/issues/339)_)
* Removed deprecated header ([#340 ](https://github.com/ros-visualization/rqt/issues/340)_)
* Use qt6 as the default dependency from rosdep ([#337 ](https://github.com/ros-visualization/rqt/issues/337)_)
* fix compile with qt6 ([#321 ](https://github.com/ros-visualization/rqt/issues/321)_)
* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, Shane Loretz, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_gui_py <https://github.com/ros-visualization/rqt/tree/lyrical/rqt_gui_py/CHANGELOG.rst>`__

* Support Qt6 ([#339 ](https://github.com/ros-visualization/rqt/issues/339)_)
* Fix setupTools deprecations ([#322 ](https://github.com/ros-visualization/rqt/issues/322)_)
* Contributors: Alejandro Hernández Cordero, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_msg <https://github.com/ros-visualization/rqt_msg/tree/lyrical/CHANGELOG.rst>`__

* Support Qt6 ([#27 ](https://github.com/ros-visualization/rqt_msg/issues/27)_)
* fix setuptools deprecations ([#23 ](https://github.com/ros-visualization/rqt_msg/issues/23)_)
* Remove CODEOWNERS ([#20 ](https://github.com/ros-visualization/rqt_msg/issues/20)_)
* Contributors: Alejandro Hernández Cordero, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_plot <https://github.com/ros-visualization/rqt_plot/tree/lyrical/CHANGELOG.rst>`__

* Use qt-base-dev / libqtwidgets ([#128 ](https://github.com/ros-visualization/rqt_plot/issues/128)_)
* Support Qt6 ([#127 ](https://github.com/ros-visualization/rqt_plot/issues/127)_)
* fix setuptools deprecations ([#123 ](https://github.com/ros-visualization/rqt_plot/issues/123)_)
* Added missing test dependency ([#118 ](https://github.com/ros-visualization/rqt_plot/issues/118)_)
* Fix for displaying constant curves ([#114 ](https://github.com/ros-visualization/rqt_plot/issues/114)_)
* Contributors: Alejandro Hernández Cordero, Martin Pecka, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_publisher <https://github.com/ros-visualization/rqt_publisher/tree/lyrical/CHANGELOG.rst>`__

* fix flake8 (backport [#57 ](https://github.com/ros-visualization/rqt_publisher/issues/57)_) ([#58 ](https://github.com/ros-visualization/rqt_publisher/issues/58)_)
* Support Qt6 ([#56 ](https://github.com/ros-visualization/rqt_publisher/issues/56)_)
* fix setuptools deprecations ([#52 ](https://github.com/ros-visualization/rqt_publisher/issues/52)_)
* Contributors: Alejandro Hernández Cordero, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_py_common <https://github.com/ros-visualization/rqt/tree/lyrical/rqt_py_common/CHANGELOG.rst>`__

* Cleanup headers ([#347 ](https://github.com/ros-visualization/rqt/issues/347)_) ([#350 ](https://github.com/ros-visualization/rqt/issues/350)_)
* Use qt-base-dev / libqtwidgets ([#345 ](https://github.com/ros-visualization/rqt/issues/345)_)
* Support Qt6 ([#339 ](https://github.com/ros-visualization/rqt/issues/339)_)
* fix compile with qt6 ([#321 ](https://github.com/ros-visualization/rqt/issues/321)_)
* Contributors: Alejandro Hernández Cordero, Shane Loretz, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_py_console <https://github.com/ros-visualization/rqt_py_console/tree/lyrical/CHANGELOG.rst>`__

* Add Qt6 compatibility ([#25 ](https://github.com/ros-visualization/rqt_py_console/issues/25)_) Co-authored-by: Alejandro Hernandez Cordero <ahcorde@gmail.com>
* fix setuptools deprecations ([#21 ](https://github.com/ros-visualization/rqt_py_console/issues/21)_)
* Contributors: Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_reconfigure <https://github.com/ros-visualization/rqt_reconfigure/tree/lyrical/CHANGELOG.rst>`__

* Support Qt6 ([#158 ](https://github.com/ros-visualization/rqt_reconfigure/issues/158)_)
* Harden behavior if double value or limit is Infinity ([#161 ](https://github.com/ros-visualization/rqt_reconfigure/issues/161)_)
* Scale IntegerEditor if range exceeds int32 ([#160 ](https://github.com/ros-visualization/rqt_reconfigure/issues/160)_)
* Ignore A005 for future flake8 ([#159 ](https://github.com/ros-visualization/rqt_reconfigure/issues/159)_)
* Cleanup mislabeled BSD license ([#157 ](https://github.com/ros-visualization/rqt_reconfigure/issues/157)_)
* fix setuptools deprecation ([#153 ](https://github.com/ros-visualization/rqt_reconfigure/issues/153)_)
* If updating remote fails, reflect the failure locally ([#144 ](https://github.com/ros-visualization/rqt_reconfigure/issues/144)_)
* Remove CODEOWNERS ([#147 ](https://github.com/ros-visualization/rqt_reconfigure/issues/147)_)
* Contributors: Alejandro Hernández Cordero, Christoph Fröhlich, Jonathan Selling, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_service_caller <https://github.com/ros-visualization/rqt_service_caller/tree/lyrical/CHANGELOG.rst>`__

* Support Qt6 ([#38 ](https://github.com/ros-visualization/rqt_service_caller/issues/38)_)
* fix setuptools deprecations ([#33 ](https://github.com/ros-visualization/rqt_service_caller/issues/33)_)
* Contributors: Alejandro Hernández Cordero, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_shell <https://github.com/ros-visualization/rqt_shell/tree/lyrical/CHANGELOG.rst>`__

* make linters happy
* Fix setuptools deprecation ([#26 ](https://github.com/ros-visualization/rqt_shell/issues/26)_)
* Contributors: Alejandro Hernandez Cordero, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_srv <https://github.com/ros-visualization/rqt_srv/tree/lyrical/CHANGELOG.rst>`__

* fix setuptools deprecations ([#16 ](https://github.com/ros-visualization/rqt_srv/issues/16)_)
* Remove CODEOWNERS ([#13 ](https://github.com/ros-visualization/rqt_srv/issues/13)_)
* Contributors: Alejandro Hernández Cordero, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_topic <https://github.com/ros-visualization/rqt_topic/tree/lyrical/CHANGELOG.rst>`__

* Support Qt6 ([#67 ](https://github.com/ros-visualization/rqt_topic/issues/67)_)
* Add Qt6 compatibility ([#66 ](https://github.com/ros-visualization/rqt_topic/issues/66)_)
* Tweak expected error in test for Pydantic v2 compat ([#65 ](https://github.com/ros-visualization/rqt_topic/issues/65)_)
* Use choose_qos() from ros2 topic echo ([#55 ](https://github.com/ros-visualization/rqt_topic/issues/55)_)
* Enable flake8 ([#58 ](https://github.com/ros-visualization/rqt_topic/issues/58)_)
* Open source rewrite of rqt_topic ([#47 ](https://github.com/ros-visualization/rqt_topic/issues/47)_) Co-authored-by: Evan Flynn <evan.flynn@apex.ai> Co-authored-by: Alejandro Hernandez Cordero <ahcorde@gmail.com>
* fix setuptools deprecations ([#57 ](https://github.com/ros-visualization/rqt_topic/issues/57)_)
* Contributors: Alejandro Hernández Cordero, Evan Flynn, Romain Reignier, Scott K Logan, Shane Loretz, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rti_connext_dds_cmake_module <https://github.com/ros2/rmw_connextdds/tree/lyrical/rti_connext_dds_cmake_module/CHANGELOG.rst>`__

* Update Connext from 7.3.0 to 7.7.0, disable monitoring library by default, and use synchronous publishing mode ([#219 ](https://github.com/ros2/rmw_connextdds/issues/219)_)
* Fix cmake deprecation ([#198 ](https://github.com/ros2/rmw_connextdds/issues/198)_)
* Contributors: Francisco Gallego Salido, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rttest <https://github.com/ros2/realtime_support/tree/lyrical/rttest/CHANGELOG.rst>`__

* cleanups and removed dead code ([#141 ](https://github.com/ros2/realtime_support/issues/141)_) ([#144 ](https://github.com/ros2/realtime_support/issues/144)_)
* Fix cmake deprecation ([#134 ](https://github.com/ros2/realtime_support/issues/134)_)
* Contributors: mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz2 <https://github.com/ros2/rviz/tree/lyrical/rviz2/CHANGELOG.rst>`__

* Use rosdep keys that select Qt5 or Qt6 by platform ([#1720 ](https://github.com/ros2/rviz/issues/1720)_)
* Use new ROSIDL aggregate CMake target ([#1688 ](https://github.com/ros2/rviz/issues/1688)_)
* Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689 ](https://github.com/ros2/rviz/issues/1689)_)
* Use qt6 as the default dependency from rosdep ([#1635 ](https://github.com/ros2/rviz/issues/1635)_)
* get rid of deprecated rclcpp::spin_some() ([#1567 ](https://github.com/ros2/rviz/issues/1567)_)
* feat: support both qt5 and qt6 ([#1187 ](https://github.com/ros2/rviz/issues/1187)_)
* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, Emerson Knapp, Nathan Brooks, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_common <https://github.com/ros2/rviz/tree/lyrical/rviz_common/CHANGELOG.rst>`__

* Use rosdep keys that select Qt5 or Qt6 by platform ([#1720 ](https://github.com/ros2/rviz/issues/1720)_)
* Compressed Image Display ([#1288 ](https://github.com/ros2/rviz//issues/1288)_)
* fix: Fixed compilation on MSVC 2022 ([#1706 ](https://github.com/ros2/rviz//issues/1706)_)
* Removed Qt6 warnings ([#1704 ](https://github.com/ros2/rviz/issues/1704)_)
* Fixed regresion is RHEL ([#1703 ](https://github.com/ros2/rviz/issues/1703)_)
* Remove warnings ([#1693 ](https://github.com/ros2/rviz/issues/1693)_)
* Link against [`GTest::gmock`` target (`#1699 ](https://github.com/ros2/rviz/issues/1699)_)
* Reduce [`QFile`` dependency (`#1652 ](https://github.com/ros2/rviz/issues/1652)_)
* Use new ROSIDL aggregate CMake target ([#1688 ](https://github.com/ros2/rviz/issues/1688)_)
* Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689 ](https://github.com/ros2/rviz/issues/1689)_)
* Cleanups in rviz_common ([#1686 ](https://github.com/ros2/rviz/issues/1686)_)
* Add tests for shallow and deep copy in Config ([#1682 ](https://github.com/ros2/rviz/issues/1682)_)
* Build performance optimizations for rviz_common ([#1677 ](https://github.com/ros2/rviz/issues/1677)_)
* Use get_package_share_path ([#1671 ](https://github.com/ros2/rviz/issues/1671)_)
* Fix setHidden regression in PropertyTreeWidget ([#1667 ](https://github.com/ros2/rviz/issues/1667)_)
* Add topic name filtering when adding new visualizations ([#1662 ](https://github.com/ros2/rviz/issues/1662)_)
* use QPointer in QTimer::singleShot to prevent use-after-free ([#1657 ](https://github.com/ros2/rviz/issues/1657)_)
* Fix Not loading plugins due to incorrect package path ([#1651 ](https://github.com/ros2/rviz/issues/1651)_)
* Updated deprecated ament_index_cpp API ([#1647 ](https://github.com/ros2/rviz/issues/1647)_)
* Fix crash with no tools ([#1639 ](https://github.com/ros2/rviz/issues/1639)_)
* Use qt6 as the default dependency from rosdep ([#1635 ](https://github.com/ros2/rviz/issues/1635)_)
* Pointcloud2 display set QoS to best effort ([#1621 ](https://github.com/ros2/rviz/issues/1621)_)
* Cleanup deprecated code ([#1619 ](https://github.com/ros2/rviz//issues/1619)_)
* Removed support for yaml-cpp lower than 0.5 ([#1605 ](https://github.com/ros2/rviz//issues/1605)_)
* Removed duplicated forward class declaration ([#1602 ](https://github.com/ros2/rviz//issues/1602)_)
* resolved TODO in visualization manager ([#1603 ](https://github.com/ros2/rviz//issues/1603)_)
* Fix incorrect Qt signal connection in combo box ([#1596 ](https://github.com/ros2/rviz/issues/1596)_)
* Removed tinyxml2_vendor dependency ([#1591 ](https://github.com/ros2/rviz/issues/1591)_)
* Replace QRegExp with QRegularExpression to support Qt6 ([#1592 ](https://github.com/ros2/rviz/issues/1592)_)
* fix crash ([#1587 ](https://github.com/ros2/rviz/issues/1587)_)
* added option to change filemode ([#1537 ](https://github.com/ros2/rviz/issues/1537)_)
* Removed deprecation warning in tf2 ([#1585 ](https://github.com/ros2/rviz/issues/1585)_)
* Std chrono update in default plugins ([#1579 ](https://github.com/ros2/rviz/issues/1579)_)
* Removed deprecations ([#1556 ](https://github.com/ros2/rviz/issues/1556)_)
* rviz common ros service property ([#1548 ](https://github.com/ros2/rviz/issues/1548)_)
* add ros action property ([#1549 ](https://github.com/ros2/rviz/issues/1549)_)
* Deprecates update(float, float) methods and provides update(std::chrono::duration, std::chrono::duration) replacements. ([#1533 ](https://github.com/ros2/rviz//issues/1533)_)
* Replace deprecated tf2_ros headers ([#1529 ](https://github.com/ros2/rviz/issues/1529)_)
* Postpone hiding of properties until insertion into model is finished ([#1508 ](https://github.com/ros2/rviz/issues/1508)_)
* Don't hide rows of properties not within the model ([#1507 ](https://github.com/ros2/rviz/issues/1507)_)
* Remove redundant check ([#1506 ](https://github.com/ros2/rviz/issues/1506)_)
* Fix panel deletion ([#1037 ](https://github.com/ros2/rviz/issues/1037)_)
* Config::mapGetBool causes segmentation fault when value_out is nullptr ([#1471 ](https://github.com/ros2/rviz/issues/1471)_)
* feat: support both qt5 and qt6 ([#1187 ](https://github.com/ros2/rviz/issues/1187)_)
* Fixed crash when a resource is not available ([#1455 ](https://github.com/ros2/rviz/issues/1455)_)
* Work in progress using the new resource retriever apis ([#1262 ](https://github.com/ros2/rviz/issues/1262)_)
* addTrackedObject Function Fails to Handle Null Pointer, Causing Crash When nullptr is Passed ([#1375 ](https://github.com/ros2/rviz/issues/1375)_)
* Add test to check mapGetString when key is missing ([#1361 ](https://github.com/ros2/rviz/issues/1361)_)
* UniformStringStream::parseFloat Fails to Handle Invalid Float Formats Correctly ([#1360 ](https://github.com/ros2/rviz/issues/1360)_)
* Fix Potential Null Pointer Dereference in VisualizerApp::getRenderWindow() to Prevent Crashes ([#1359 ](https://github.com/ros2/rviz/issues/1359)_)
* Extend support for type adaptation (REP 2007) in rviz_common for TF-filtered displays ([#1346 ](https://github.com/ros2/rviz/issues/1346)_)
* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, David V. Lu!!, Emerson Knapp, Janosch Machowinski, Joshua Supratman, Mark Johnson, Mateusz Żak, Matteo Princisgh, Matthew Foran, Michael Carroll, Nathan Brooks, Oscmoar07, Patrick Roncagliolo, Shane Loretz, mini-1235, nelson, t0k0shi


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_default_plugins <https://github.com/ros2/rviz/tree/lyrical/rviz_default_plugins/CHANGELOG.rst>`__

* Use rosdep keys that select Qt5 or Qt6 by platform ([#1720 ](https://github.com/ros2/rviz/issues/1720)_)
* Compressed Image Display ([#1288 ](https://github.com/ros2/rviz//issues/1288)_)
* Removed Qt6 warnings ([#1704 ](https://github.com/ros2/rviz/issues/1704)_)
* Switch rviz service resource retriever to use new repo's code ([#1698 ](https://github.com/ros2/rviz/issues/1698)_)
* Link against [`GTest::gmock`` target (`#1699 ](https://github.com/ros2/rviz/issues/1699)_)
* Improve marker common ([#1687 ](https://github.com/ros2/rviz/issues/1687)_)
* Reduce [`QFile`` dependency (`#1652 ](https://github.com/ros2/rviz/issues/1652)_)
* Use new ROSIDL aggregate CMake target ([#1688 ](https://github.com/ros2/rviz/issues/1688)_)
* Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689 ](https://github.com/ros2/rviz/issues/1689)_)
* Remove redundant compilation of test fixtures ([#1673 ](https://github.com/ros2/rviz/issues/1673)_)
* Updated deprecated ament_index_cpp API ([#1647 ](https://github.com/ros2/rviz/issues/1647)_)
* Add CameraInfo topic property to DepthCloudDisplay ([#1643 ](https://github.com/ros2/rviz/issues/1643)_)
* Use qt6 as the default dependency from rosdep ([#1635 ](https://github.com/ros2/rviz/issues/1635)_)
* Pointcloud2 display set QoS to best effort ([#1621 ](https://github.com/ros2/rviz/issues/1621)_)
* Fix Translation Issue in XYOrbitViewController ([#1630 ](https://github.com/ros2/rviz/issues/1630)_)
* Overcome 16384 size limit ([#1622 ](https://github.com/ros2/rviz/issues/1622)_)
* Removed already done TODO ([#1604 ](https://github.com/ros2/rviz//issues/1604)_)
* Fixed issue 1593 ([#1598 ](https://github.com/ros2/rviz/issues/1598)_)
* Removed tf2 warning ([#1586 ](https://github.com/ros2/rviz/issues/1586)_)
* Removed deprecation warning in tf2 ([#1585 ](https://github.com/ros2/rviz/issues/1585)_)
* Std chrono update in default plugins ([#1579 ](https://github.com/ros2/rviz/issues/1579)_)
* Fix pointcloud2 display divide by 0 ([#1581 ](https://github.com/ros2/rviz/issues/1581)_)
* add support for ffmpeg_image_transport and point_cloud_transport ([#1568 ](https://github.com/ros2/rviz/issues/1568)_)
* Extend the message filter display for point cloud 2 display ([#1566 ](https://github.com/ros2/rviz/issues/1566)_)
* Support image transport lifecycle ([#1472 ](https://github.com/ros2/rviz//issues/1472)_)
* Fix QoS profile loading for InitialPoseTool from rviz config files ([#1544 ](https://github.com/ros2/rviz//issues/1544)_)
* Replace rmw_qos_profile_t with rclcpp::QoS ([#1525 ](https://github.com/ros2/rviz/issues/1525)_)
* Replace deprecated tf2_ros headers ([#1529 ](https://github.com/ros2/rviz/issues/1529)_)
* fix deprecated include ([#1530 ](https://github.com/ros2/rviz/issues/1530)_)
* point_cloud_transport update API call ([#1526 ](https://github.com/ros2/rviz/issues/1526)_)
* Better handling of missing transport plugins ([#1488 ](https://github.com/ros2/rviz/issues/1488)_)
* Fixed deprecation warning on point_cloud_transport: rmw_qos_profile_t ([#1491 ](https://github.com/ros2/rviz/issues/1491)_)
* Add symbol visibility macros to make*Palette public functions ([#1492 ](https://github.com/ros2/rviz/issues/1492)_)
* Fix /rviz/get_resource ([#1487 ](https://github.com/ros2/rviz/issues/1487)_)
* Removed point_cloud_transport deprecation ([#1474 ](https://github.com/ros2/rviz/issues/1474)_)
* Frame view controller: Removed warnings ([#1470 ](https://github.com/ros2/rviz/issues/1470)_)
* Fix compile with qt6 ([#1475 ](https://github.com/ros2/rviz/issues/1475)_)
* Fix Issue with Quaternion Angular Distance ([#1473 ](https://github.com/ros2/rviz/issues/1473)_)
* PointStampedDisplay: Ignore incoming messages if disabled ([#1036 ](https://github.com/ros2/rviz/issues/1036)_)
* Removed unused headers from resouce retriever ([#1463 ](https://github.com/ros2/rviz/issues/1463)_)
* feat: support both qt5 and qt6 ([#1187 ](https://github.com/ros2/rviz/issues/1187)_)
* [rviz_default_plugins] Add missing export dependencies ([#1461 ](https://github.com/ros2/rviz/issues/1461)_)
* Backported FrameAligned camera ([#1453 ](https://github.com/ros2/rviz/issues/1453)_)
* Changed Marker Displays to allow toggling visibility of namespaces ([#1402 ](https://github.com/ros2/rviz/issues/1402)_)
* Do not use ${Qt5Widgets_INCLUDE_DIRS} to avoid creating non-relocatable CMake config files ([#1450 ](https://github.com/ros2/rviz/issues/1450)_)
* PointCloudDisplay: Fix decay time 0 keeping more than the last message ([#1400 ](https://github.com/ros2/rviz/issues/1400)_)
* Work in progress using the new resource retriever apis ([#1262 ](https://github.com/ros2/rviz/issues/1262)_)
* Include chrono ([#1353 ](https://github.com/ros2/rviz/issues/1353)_)
* Contributors: Alejandro Hernández Cordero, Alexis Tsogias, Antonio Brandi, Daisuke Nishimatsu, Eesha Kumar, Emerson Knapp, Felix Exner (fexner), Georg Flick, Guillaume Doisy, Harrison Chen, Kenji Brameld (TRACLabs), Kosuke Takeuchi, Lennart Reiher, Mark Johnson, Matthew Foran, Michael Carroll, Nathan Brooks, Shane Loretz, Silvio Traversaro, Stefan Fabian, Stoyan Gaydarov, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_ogre_vendor <https://github.com/ros2/rviz/tree/lyrical/rviz_ogre_vendor/CHANGELOG.rst>`__

* Add patch to remove [`binary_function`` (`#1691 ](https://github.com/ros2/rviz/issues/1691)_)
* Bump cmake version and suppress warning for rviz_ogre_vendor ([#1684 ](https://github.com/ros2/rviz/issues/1684)_)
* Remove vendoring freetype and zlib on Windows ([#1636 ](https://github.com/ros2/rviz/issues/1636)_)
* Add RVIZ_OGRE_VENDOR_MANGLE_NAME_OF_LIBRARIES_USED_BY_RVIZ option to further mangle ogre libraries used by rviz ([#1493 ](https://github.com/ros2/rviz/issues/1493)_)
* Add missing glew dependency for ogre vendor package ([#1350 ](https://github.com/ros2/rviz/issues/1350)_)
* Contributors: Dhruv Patel, Michael Carroll, Shane Loretz, Silvio Traversaro, Stefan Fabian


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_rendering <https://github.com/ros2/rviz/tree/lyrical/rviz_rendering/CHANGELOG.rst>`__

* Use rosdep keys that select Qt5 or Qt6 by platform ([#1720 ](https://github.com/ros2/rviz/issues/1720)_)
* Fix build for Ubuntu 26 ([#1694 ](https://github.com/ros2/rviz/issues/1694)_)
* Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689 ](https://github.com/ros2/rviz/issues/1689)_)
* Updated deprecated ament_index_cpp API ([#1647 ](https://github.com/ros2/rviz/issues/1647)_)
* Use qt6 as the default dependency from rosdep ([#1635 ](https://github.com/ros2/rviz/issues/1635)_)
* Removed unused files ([#1600 ](https://github.com/ros2/rviz//issues/1600)_)
* Removed assimp vendor package ([#1574 ](https://github.com/ros2/rviz/issues/1574)_)
* Update OGRE mesh files from ROS1 RViz ([#1536 ](https://github.com/ros2/rviz//issues/1536)_) ([#1559 ](https://github.com/ros2/rviz//issues/1559)_)
* add resourceExists check to loadEmbeddedTexture before loading texture ([#1542 ](https://github.com/ros2/rviz//issues/1542)_)
* Assign the geometry to the resource group "rviz_rendering" ([#1502 ](https://github.com/ros2/rviz/issues/1502)_)
* Removed windows warning ([#1486 ](https://github.com/ros2/rviz/issues/1486)_)
* Handle glTF Y-Up frame convention on mesh load ([#1482 ](https://github.com/ros2/rviz/issues/1482)_)
* Removed unused headers from resouce retriever ([#1463 ](https://github.com/ros2/rviz/issues/1463)_)
* feat: support both qt5 and qt6 ([#1187 ](https://github.com/ros2/rviz/issues/1187)_)
* WrenchVisual::setForceColor and setTorqueColor clamp values ([#1437 ](https://github.com/ros2/rviz/issues/1437)_)
* Missing Null Pointer Check in TrianglePolygon Constructor Leads to Crash ([#1434 ](https://github.com/ros2/rviz/issues/1434)_)
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
* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, John TGZ, Michael Carlstrom, Michael Carroll, Michel Hidalgo, Nathan Brooks, Shane Loretz, matthias88, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_rendering_tests <https://github.com/ros2/rviz/tree/lyrical/rviz_rendering_tests/CHANGELOG.rst>`__

* Use rosdep keys that select Qt5 or Qt6 by platform ([#1720 ](https://github.com/ros2/rviz/issues/1720)_)
* Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689 ](https://github.com/ros2/rviz/issues/1689)_)
* Updated deprecated ament_index_cpp API ([#1647 ](https://github.com/ros2/rviz/issues/1647)_)
* Use qt6 as the default dependency from rosdep ([#1635 ](https://github.com/ros2/rviz/issues/1635)_)
* feat: support both qt5 and qt6 ([#1187 ](https://github.com/ros2/rviz/issues/1187)_)
* Work in progress using the new resource retriever apis ([#1262 ](https://github.com/ros2/rviz/issues/1262)_)
* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, Michael Carroll, Nathan Brooks, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_visual_testing_framework <https://github.com/ros2/rviz/tree/lyrical/rviz_visual_testing_framework/CHANGELOG.rst>`__

* Use rosdep keys that select Qt5 or Qt6 by platform ([#1720 ](https://github.com/ros2/rviz/issues/1720)_)
* Use new ROSIDL aggregate CMake target ([#1688 ](https://github.com/ros2/rviz/issues/1688)_)
* Fix Qt version resolution when both Qt5 and Qt6 are installed - CMake defaults to ascending resolution and Qt5 will be found when Qt6 is desired (Rolling, L-Turtle, and beyond). ([#1689 ](https://github.com/ros2/rviz/issues/1689)_)
* Use get_package_share_path ([#1671 ](https://github.com/ros2/rviz/issues/1671)_)
* Update ament_index_cpp API ([#1649 ](https://github.com/ros2/rviz/issues/1649)_)
* Use qt6 as the default dependency from rosdep ([#1635 ](https://github.com/ros2/rviz/issues/1635)_)
* Removed deprecation warning in tf2 ([#1585 ](https://github.com/ros2/rviz/issues/1585)_)
* Replace deprecated tf2_ros headers ([#1529 ](https://github.com/ros2/rviz/issues/1529)_)
* feat: support both qt5 and qt6 ([#1187 ](https://github.com/ros2/rviz/issues/1187)_)
* Contributors: Alejandro Hernández Cordero, Daisuke Nishimatsu, Emerson Knapp, Nathan Brooks, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sensor_msgs <https://github.com/ros2/common_interfaces/tree/lyrical/sensor_msgs/CHANGELOG.rst>`__

* [ADD] missing PointField type entries ([#301 ](https://github.com/ros2/common_interfaces/issues/301)_)
* Update point_cloud2_iterator.hpp ([#298 ](https://github.com/ros2/common_interfaces/issues/298)_)
* Fix CMAKE deprecation ([#288 ](https://github.com/ros2/common_interfaces/issues/288)_)
* Enhance NV12 and NV21 Support in sensor_msgs::image_encodings ([#264 ](https://github.com/ros2/common_interfaces/issues/264)_)
* Contributors: Adam Leeper, Zhaoyuan Cheng, mosfet80, wodtko


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sensor_msgs_py <https://github.com/ros2/common_interfaces/tree/lyrical/sensor_msgs_py/CHANGELOG.rst>`__

* Use structured NumPy points.dtype.itemsize as default point_step in create_cloud ([#295 ](https://github.com/ros2/common_interfaces/issues/295)_)
* fix setuptools deprecation ([#293 ](https://github.com/ros2/common_interfaces/issues/293)_)
* Contributors: mosfet80, xndcn


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `service_msgs <https://github.com/ros2/rcl_interfaces/tree/lyrical/service_msgs/CHANGELOG.rst>`__

* Fix cmake deprecation ([#180 ](https://github.com/ros2/rcl_interfaces/issues/180)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `shape_msgs <https://github.com/ros2/common_interfaces/tree/lyrical/shape_msgs/CHANGELOG.rst>`__

* Fix CMAKE deprecation ([#288 ](https://github.com/ros2/common_interfaces/issues/288)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `spdlog_vendor <https://github.com/ros2/spdlog_vendor/tree/lyrical/CHANGELOG.rst>`__

* Remove CODEOWNERS and mirror-rolling-to-master. ([#38 ](https://github.com/ros2/spdlog_vendor/issues/38)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sros2 <https://github.com/ros2/sros2/tree/lyrical/sros2/CHANGELOG.rst>`__

* Fix [`load_file_into_BIO: File could not be found, opened or is empty`` error on Windows (`#386 ](https://github.com/ros2/sros2/issues/386)_) ([#387 ](https://github.com/ros2/sros2/issues/387)_)
* python3-pytest-timeout is missing for test dependency. ([#377 ](https://github.com/ros2/sros2/issues/377)_)
* Clean up isolated ros2 daemon process for tests. ([#375 ](https://github.com/ros2/sros2/issues/375)_)
* Remove importlib ([#368 ](https://github.com/ros2/sros2/issues/368)_)
* Timezone aware datetimes + remove hack from [#209 ](https://github.com/ros2/sros2/issues/209)_ ([#300 ](https://github.com/ros2/sros2/issues/300)_)
* fix setuptools deprecations ([#357 ](https://github.com/ros2/sros2/issues/357)_)
* Use rmw_test_fixture to isolate ros2cli tests ([#356 ](https://github.com/ros2/sros2/issues/356)_)
* update utilities to pass instance not class of ec.SECP256R1 ([#352 ](https://github.com/ros2/sros2/issues/352)_)
* suppress multi-threaded warnings. ([#346 ](https://github.com/ros2/sros2/issues/346)_)
* Switch to get_rmw_additional_env ([#339 ](https://github.com/ros2/sros2/issues/339)_)
* Fix github-workflow mypy error ([#336 ](https://github.com/ros2/sros2/issues/336)_)
* Contributors: Michael Carlstrom, Mikael Arguedas, Scott K Logan, Tomoya Fujita, cdisco, mergify[bot], mosfet80, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sros2_cmake <https://github.com/ros2/sros2/tree/lyrical/sros2_cmake/CHANGELOG.rst>`__

* Update CMakeLists.txt ([#344 ](https://github.com/ros2/sros2/issues/344)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `statistics_msgs <https://github.com/ros2/rcl_interfaces/tree/lyrical/statistics_msgs/CHANGELOG.rst>`__

* Fix cmake deprecation ([#180 ](https://github.com/ros2/rcl_interfaces/issues/180)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `std_msgs <https://github.com/ros2/common_interfaces/tree/lyrical/std_msgs/CHANGELOG.rst>`__

* Fix CMAKE deprecation ([#288 ](https://github.com/ros2/common_interfaces/issues/288)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `std_srvs <https://github.com/ros2/common_interfaces/tree/lyrical/std_srvs/CHANGELOG.rst>`__

* Fix CMAKE deprecation ([#288 ](https://github.com/ros2/common_interfaces/issues/288)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `stereo_msgs <https://github.com/ros2/common_interfaces/tree/lyrical/stereo_msgs/CHANGELOG.rst>`__

* Fix CMAKE deprecation ([#288 ](https://github.com/ros2/common_interfaces/issues/288)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tango_icons_vendor <https://github.com/ros-visualization/tango_icons_vendor/tree/lyrical/CHANGELOG.rst>`__

* fix cmake deprecation ([#15 ](https://github.com/ros-visualization/tango_icons_vendor/issues/15)_)
* Remove the mirror-rolling-to-master workflow ([#12 ](https://github.com/ros-visualization/tango_icons_vendor/issues/12)_)
* Remove CODEOWNERS ([#11 ](https://github.com/ros-visualization/tango_icons_vendor/issues/11)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_cli <https://github.com/ros2/system_tests/tree/lyrical/test_cli/CHANGELOG.rst>`__

* fix CMAKE deprecation ([#572 ](https://github.com/ros2/system_tests/issues/572)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_cli_remapping <https://github.com/ros2/system_tests/tree/lyrical/test_cli_remapping/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#587 ](https://github.com/ros2/system_tests/issues/587)_)
* fix CMAKE deprecation ([#572 ](https://github.com/ros2/system_tests/issues/572)_)
* Contributors: Emerson Knapp, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_communication <https://github.com/ros2/system_tests/tree/lyrical/test_communication/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#587 ](https://github.com/ros2/system_tests/issues/587)_)
* disable interoperability check for CycloneDDS and FastRTPS for WString ([#586 ](https://github.com/ros2/system_tests/issues/586)_)
* Fix index ([#585 ](https://github.com/ros2/system_tests/issues/585)_)
* Update subscription callback signatures ([#575 ](https://github.com/ros2/system_tests/issues/575)_)
* get rid of deprecated rclcpp::spin_some(). ([#574 ](https://github.com/ros2/system_tests//issues/574)_)
* fix CMAKE deprecation ([#572 ](https://github.com/ros2/system_tests/issues/572)_)
* Use EnableRmwIsolation in launch tests ([#571 ](https://github.com/ros2/system_tests/issues/571)_)
* Switch to isolated test fixture macros ([#571 ](https://github.com/ros2/system_tests/issues/571)_)
* Add tests for Keyed types ([#568 ](https://github.com/ros2/system_tests/issues/568)_)
* Remove use of ament_target_dependencies ([#566 ](https://github.com/ros2/system_tests/issues/566)_)
* Skip all multi-vendor pub/sub tests with zenoh ([#560 ](https://github.com/ros2/system_tests/issues/560)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Francisco Gallego Salido, Janosch Machowinski, Michael Carlstrom, Scott K Logan, Shane Loretz, Tomoya Fujita, mini-1235, mosfet80, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_interface_files <https://github.com/ros2/test_interface_files/tree/lyrical/CHANGELOG.rst>`__

* Update CMakeLists.txt ([#26 ](https://github.com/ros2/test_interface_files/issues/26)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#23 ](https://github.com/ros2/test_interface_files/issues/23)_)
* Contributors: Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_launch_ros <https://github.com/ros2/launch_ros/tree/lyrical/test_launch_ros/CHANGELOG.rst>`__

* Add tests for new component container refactor ([#536 ](https://github.com/ros2/launch_ros/issues/536)_)
* Surpressing multi-threaded process warning from flake8. ([#520 ](https://github.com/ros2/launch_ros//issues/520)_)
* correct typos ([#524 ](https://github.com/ros2/launch_ros//issues/524)_)
* set PYTHONUNBUFFERED to 1 to avoid hangs due to lost buffers ([#519 ](https://github.com/ros2/launch_ros//issues/519)_)
* Make FindPackage substitutions a Path to get operator / ([#494 ](https://github.com/ros2/launch_ros/issues/494)_)
* Expose lifecycle_node ([#327 ](https://github.com/ros2/launch_ros/issues/327)_) (with test) ([#482 ](https://github.com/ros2/launch_ros/issues/482)_)
* Switch osrf_pycommon dependency to system package ([#431 ](https://github.com/ros2/launch_ros/issues/431)_)
* Fix SetUseSimTime for launch frontends ([#488 ](https://github.com/ros2/launch_ros/issues/488)_)
* fix setuptools deprecations ([#475 ](https://github.com/ros2/launch_ros/issues/475)_)
* Fix: LoadComposableNodes fails to parse wildcard param files correctly ([#460 ](https://github.com/ros2/launch_ros/issues/460)_) ([#465 ](https://github.com/ros2/launch_ros/issues/465)_)
* Contributors: Auguste Lalande, Christophe Bedard, Clara Berendsen, Emerson Knapp, Emre Kuru, Jasper van Brakel, Scott K Logan, Skyler Medeiros, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_launch_testing <https://github.com/ros2/launch/tree/lyrical/test_launch_testing/CHANGELOG.rst>`__

* Fix CMake deprecation ([#899 ](https://github.com/ros2/launch/issues/899)_)
* Allow Path in substitutions, instead of requiring cast to str ([#873 ](https://github.com/ros2/launch/issues/873)_)
* Contributors: Emerson Knapp, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_msgs <https://github.com/ros2/rcl_interfaces/tree/lyrical/test_msgs/CHANGELOG.rst>`__

* Add [`ament_cmake_mypy`` to ``test_msgs`` (`#187 ](https://github.com/ros2/rcl_interfaces/issues/187)_)
* Fix cmake deprecation ([#180 ](https://github.com/ros2/rcl_interfaces/issues/180)_)
* Contributors: Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_osrf_testing_tools_cpp <https://github.com/osrf/osrf_testing_tools_cpp/tree/lyrical/test_osrf_testing_tools_cpp/CHANGELOG.rst>`__

* fix cmake deprecation  ([#94 ](https://github.com/osrf/osrf_testing_tools_cpp/issues/94)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_quality_of_service <https://github.com/ros2/system_tests/tree/lyrical/test_quality_of_service/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#587 ](https://github.com/ros2/system_tests/issues/587)_)
* fix CMAKE deprecation ([#572 ](https://github.com/ros2/system_tests/issues/572)_)
* Switch to isolated test fixture macros ([#571 ](https://github.com/ros2/system_tests/issues/571)_)
* Use rmw_event_type_is_supported to skip tests ([#563 ](https://github.com/ros2/system_tests/issues/563)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Scott K Logan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_rclcpp <https://github.com/ros2/system_tests/tree/lyrical/test_rclcpp/CHANGELOG.rst>`__

* Add tests isolation in test_rclcpp ([#583 ](https://github.com/ros2/system_tests/issues/583)_)
* info message comes from deferred signal handler with another thread. ([#576 ](https://github.com/ros2/system_tests/issues/576)_)
* get rid of deprecated rclcpp::spin_some(). ([#574 ](https://github.com/ros2/system_tests//issues/574)_)
* fix CMAKE deprecation ([#572 ](https://github.com/ros2/system_tests/issues/572)_)
* Use EnableRmwIsolation in launch tests ([#571 ](https://github.com/ros2/system_tests/issues/571)_)
* Ensure test verifies the existence of all spawning nodes ([#558 ](https://github.com/ros2/system_tests/issues/558)_)
* Contributors: Alejandro Hernández Cordero, Julien Enoch, Scott K Logan, Tomoya Fujita, Yuyuan Yuan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_rmw_implementation <https://github.com/ros2/rmw_implementation/tree/lyrical/test_rmw_implementation/CHANGELOG.rst>`__

* Use new aggregate rosidl target instead of _TARGETS ([#276 ](https://github.com/ros2/rmw_implementation/issues/276)_)
* test_rmw_implementation: add test isolation ([#275 ](https://github.com/ros2/rmw_implementation/issues/275)_)
* Add rmw_get_clients_info_by_service , rmw_servers_clients_info_by_service ([#238 ](https://github.com/ros2/rmw_implementation/issues/238)_)
* fix cmake deprecation ([#267 ](https://github.com/ros2/rmw_implementation/issues/267)_)
* Test failing deserialization of invalid sequence length ([#261 ](https://github.com/ros2/rmw_implementation/issues/261)_)
* add ignore_local_publications_serialized test. ([#255 ](https://github.com/ros2/rmw_implementation/issues/255)_)
* Contributors: Alexis Tsogias, Julien Enoch, Lee, Miguel Company, Minju, Tomoya Fujita, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_ros2trace <https://github.com/ros2/ros2_tracing/tree/lyrical/test_ros2trace/CHANGELOG.rst>`__

* Skip test_ros2trace's tracing tests for now ([#218 ](https://github.com/ros2/ros2_tracing/issues/218)_)
* Allow creating snapshot sessions ([#195 ](https://github.com/ros2/ros2_tracing/issues/195)_)
* Only check test process events in test_runtime_disable ([#193 ](https://github.com/ros2/ros2_tracing/issues/193)_)
* Add runtime tracing opt-out mechanism ([#185 ](https://github.com/ros2/ros2_tracing/issues/185)_)
* fix setuptools deprecation ([#189 ](https://github.com/ros2/ros2_tracing/issues/189)_)
* Use timeout for everything in test_ros2trace tests ([#174 ](https://github.com/ros2/ros2_tracing/issues/174)_)
* Contributors: Christophe Bedard, Michel Hidalgo, Shravan Deva, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_security <https://github.com/ros2/system_tests/tree/lyrical/test_security/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#587 ](https://github.com/ros2/system_tests/issues/587)_)
* fix CMAKE deprecation ([#572 ](https://github.com/ros2/system_tests/issues/572)_)
* Contributors: Emerson Knapp, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_tf2 <https://github.com/ros2/geometry2/tree/lyrical/test_tf2/CHANGELOG.rst>`__

* fix typos ([#921 ](https://github.com/ros2/geometry2/issues/921)_)
* Use new ROSIDL aggregate CMake target ([#907 ](https://github.com/ros2/geometry2/issues/907)_)
* added toMsg for eigen-accel as well as its tests ([#887 ](https://github.com/ros2/geometry2/issues/887)_)
* Move \author tags to \file \brief ([#870 ](https://github.com/ros2/geometry2/issues/870)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Adding NodeInterfaces API Design ([#714 ](https://github.com/ros2/geometry2/issues/714)_)
* Change tf2_ros C to C++ headers ([#805 ](https://github.com/ros2/geometry2/issues/805)_)
* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Add [`rclcpp::shutdown`` (`#762 ](https://github.com/ros2/geometry2/issues/762)_)
* Contributors: Alireza Moayyedi, Auguste Lalande, Emerson Knapp, Gary Servin, Lucas Wendland, R Kent James, Yuyuan Yuan, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_tracetools <https://github.com/ros2/ros2_tracing/tree/lyrical/test_tracetools/CHANGELOG.rst>`__

* fix: Fixed compiation on MSVC 2022 ([#243 ](https://github.com/ros2/ros2_tracing/issues/243)_)
* Use new ROSIDL aggregate CMake target ([#238 ](https://github.com/ros2/ros2_tracing/issues/238)_)
* Support tracepoints for complex message flow annotation used by ROS 2 plugin of Eclipse Trace Compass ([#233 ](https://github.com/ros2/ros2_tracing/issues/233)_)
* Update subscription callback signatures ([#217 ](https://github.com/ros2/ros2_tracing/issues/217)_)
* Add runtime tracing opt-out mechanism ([#185 ](https://github.com/ros2/ros2_tracing/issues/185)_)
* Update CMakeLists.txt ([#176 ](https://github.com/ros2/ros2_tracing/issues/176)_)
* Contributors: Emerson Knapp, Janosch Machowinski, Michel Hidalgo, Raphael van Kempen, mini-1235, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_tracetools_launch <https://github.com/ros2/ros2_tracing/tree/lyrical/test_tracetools_launch/CHANGELOG.rst>`__

* Allow creating snapshot sessions ([#195 ](https://github.com/ros2/ros2_tracing/issues/195)_)
* fix setuptools deprecation ([#189 ](https://github.com/ros2/ros2_tracing/issues/189)_)
* Make trace action parameters substitutable for xml and yaml launch files ([#188 ](https://github.com/ros2/ros2_tracing/issues/188)_)
* Make trace action parameters substitutable ([#187 ](https://github.com/ros2/ros2_tracing/issues/187)_)
* Address typing issues reported by mypy in tracetools_launch ([#184 ](https://github.com/ros2/ros2_tracing/issues/184)_)
* Contributors: Christophe Bedard, Shravan Deva, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2 <https://github.com/ros2/geometry2/tree/lyrical/tf2/CHANGELOG.rst>`__

* Added tests for static cache ([#920 ](https://github.com/ros2/geometry2/issues/920)_)
* Replacing with clean index-based iteration and avoid division by zero ([#901 ](https://github.com/ros2/geometry2/issues/901)_)
* fix typos ([#921 ](https://github.com/ros2/geometry2/issues/921)_)
* Fix StaticCache::getData() returning true on empty cache ([#908 ](https://github.com/ros2/geometry2/issues/908)_)
* Use new ROSIDL aggregate CMake target ([#907 ](https://github.com/ros2/geometry2/issues/907)_)
* Fix CPP style in tf2 ([#902 ](https://github.com/ros2/geometry2/issues/902)_)
* local variable tf2 no longer shadows the tf2:: ([#903 ](https://github.com/ros2/geometry2/issues/903)_)
* Replaced char* with std::string ([#904 ](https://github.com/ros2/geometry2/issues/904)_)
* Fix misleading extrapolation time in buffer_core ([#832 ](https://github.com/ros2/geometry2/issues/832)_) ([#896 ](https://github.com/ros2/geometry2/issues/896)_)
* static function to crate quaternions directly from rotation added ([#881 ](https://github.com/ros2/geometry2/issues/881)_)
* Expose Doxygen output in tf2, showing former Doxygen front page also as README.md ([#871 ](https://github.com/ros2/geometry2/issues/871)_)
* Move \author tags to \file \brief ([#870 ](https://github.com/ros2/geometry2/issues/870)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Fix various documentation errors in tf2 ([#857 ](https://github.com/ros2/geometry2/issues/857)_)
* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856 ](https://github.com/ros2/geometry2/issues/856)_)
* Fix REP url locations ([#847 ](https://github.com/ros2/geometry2/issues/847)_)
* Adding explicit handling for normalization of zero-quaternions ([#839 ](https://github.com/ros2/geometry2/issues/839)_)
* Cleanup TF2 dependencies ([#843 ](https://github.com/ros2/geometry2/issues/843)_)
* Added tf2 documentation to docs.ros.org ([#671 ](https://github.com/ros2/geometry2/issues/671)_)
* Add RPY quaternion constructor ([#806 ](https://github.com/ros2/geometry2/issues/806)_)
* Default initialize TransformStorage's frame_id\_ and child_frame_id\_ with UINT32_MAX ([#783 ](https://github.com/ros2/geometry2/issues/783)_)
* Removed deprecated headers tf2 ([#789 ](https://github.com/ros2/geometry2/issues/789)_)
* Add isnan support ([#780 ](https://github.com/ros2/geometry2/issues/780)_)
* Overflow Issue in durationFromSec() Function when Handling Extremely Large or Small Values ([#785 ](https://github.com/ros2/geometry2/issues/785)_)
* Do not clobber callback handles when cancelling pending transformable requests ([#779 ](https://github.com/ros2/geometry2/issues/779)_)
* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Contributors: Alejandro Hernández Cordero, Alireza Moayyedi, Andreas, Auguste Lalande, Chris Lalancette, Emerson Knapp, Markus Bader, Michael Carlstrom, Pavel Guzenfeld, R Kent James, Selim Ağırman, Simon Jusner, Tim Clephas, Timo Röhling, cramke, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_bullet <https://github.com/ros2/geometry2/tree/lyrical/tf2_bullet/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#907 ](https://github.com/ros2/geometry2/issues/907)_)
* Move \author tags to \file \brief ([#870 ](https://github.com/ros2/geometry2/issues/870)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856 ](https://github.com/ros2/geometry2/issues/856)_)
* Set Cmake Policy CMP0144 ([#819 ](https://github.com/ros2/geometry2/issues/819)_)
* Change tf2_ros C to C++ headers ([#805 ](https://github.com/ros2/geometry2/issues/805)_)
* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Contributors: Cristóbal Arroyo, Emerson Knapp, Gary Servin, R Kent James, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_eigen <https://github.com/ros2/geometry2/tree/lyrical/tf2_eigen/CHANGELOG.rst>`__

* fix typos ([#921 ](https://github.com/ros2/geometry2/issues/921)_)
* Use new ROSIDL aggregate CMake target ([#907 ](https://github.com/ros2/geometry2/issues/907)_)
* added toMsg for eigen-accel as well as its tests ([#887 ](https://github.com/ros2/geometry2/issues/887)_)
* Move \author tags to \file \brief ([#870 ](https://github.com/ros2/geometry2/issues/870)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Add fromMsg for converting from Accel to Eigen ([#844 ](https://github.com/ros2/geometry2/issues/844)_)
* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856 ](https://github.com/ros2/geometry2/issues/856)_)
* Change tf2_ros C to C++ headers ([#805 ](https://github.com/ros2/geometry2/issues/805)_)
* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Contributors: Alireza Moayyedi, Auguste Lalande, Emerson Knapp, Gary Servin, R Kent James, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_eigen_kdl <https://github.com/ros2/geometry2/tree/lyrical/tf2_eigen_kdl/CHANGELOG.rst>`__

* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856 ](https://github.com/ros2/geometry2/issues/856)_)
* Cleanup mislabeled BSD license ([#855 ](https://github.com/ros2/geometry2/issues/855)_)
* Removed orocos kdl vendor dependency ([#826 ](https://github.com/ros2/geometry2/issues/826)_)
* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Contributors: Alejandro Hernández Cordero, R Kent James, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_geometry_msgs <https://github.com/ros2/geometry2/tree/lyrical/tf2_geometry_msgs/CHANGELOG.rst>`__

* fix typos ([#921 ](https://github.com/ros2/geometry2/issues/921)_)
* fix: doTransform of VelocityStamped added input vector after transform ([#909 ](https://github.com/ros2/geometry2/issues/909)_)
* Use new ROSIDL aggregate CMake target ([#907 ](https://github.com/ros2/geometry2/issues/907)_)
* Copy child_frame_id from input ([#889 ](https://github.com/ros2/geometry2/issues/889)_)
* Move \author tags to \file \brief ([#870 ](https://github.com/ros2/geometry2/issues/870)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Removed orocos kdl vendor dependency ([#826 ](https://github.com/ros2/geometry2/issues/826)_)
* Change tf2_ros C to C++ headers ([#805 ](https://github.com/ros2/geometry2/issues/805)_)
* Contributors: Alejandro Hernández Cordero, Auguste Lalande, Emerson Knapp, Gary Servin, R Kent James, Yannik Meinken, cramke


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_kdl <https://github.com/ros2/geometry2/tree/lyrical/tf2_kdl/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#907 ](https://github.com/ros2/geometry2/issues/907)_)
* Move \author tags to \file \brief ([#870 ](https://github.com/ros2/geometry2/issues/870)_)
* Documentation fixes for tf2_kdl ([#869 ](https://github.com/ros2/geometry2/issues/869)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856 ](https://github.com/ros2/geometry2/issues/856)_)
* Removed orocos kdl vendor dependency ([#826 ](https://github.com/ros2/geometry2/issues/826)_)
* Change tf2_ros C to C++ headers ([#805 ](https://github.com/ros2/geometry2/issues/805)_)
* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Fix external docs mappings ([#757 ](https://github.com/ros2/geometry2/issues/757)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Emmanuel, Gary Servin, R Kent James, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_msgs <https://github.com/ros2/geometry2/tree/lyrical/tf2_msgs/CHANGELOG.rst>`__

* fix typos ([#921 ](https://github.com/ros2/geometry2/issues/921)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Contributors: Auguste Lalande, R Kent James, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_py <https://github.com/ros2/geometry2/tree/lyrical/tf2_py/CHANGELOG.rst>`__

* fix typos ([#921 ](https://github.com/ros2/geometry2/issues/921)_)
* Use new ROSIDL aggregate CMake target ([#907 ](https://github.com/ros2/geometry2/issues/907)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Cleanup TF2 dependencies ([#843 ](https://github.com/ros2/geometry2/issues/843)_)
* Contributors: Auguste Lalande, Chris Lalancette, Emerson Knapp, R Kent James


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_ros <https://github.com/ros2/geometry2/tree/lyrical/tf2_ros/CHANGELOG.rst>`__

* fix typos ([#921 ](https://github.com/ros2/geometry2/issues/921)_)
* Use new ROSIDL aggregate CMake target ([#907 ](https://github.com/ros2/geometry2/issues/907)_)
* Move \author tags to \file \brief ([#870 ](https://github.com/ros2/geometry2/issues/870)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856 ](https://github.com/ros2/geometry2/issues/856)_)
* Prevent log spam from tf2_ros message_filter ([#851 ](https://github.com/ros2/geometry2/issues/851)_)
* Updated tf2_echo with some other features ([#802 ](https://github.com/ros2/geometry2/issues/802)_) ([#840 ](https://github.com/ros2/geometry2/issues/840)_)
* Replace std::sleep_for with rclcpp::clock::sleep_for ([#835 ](https://github.com/ros2/geometry2/issues/835)_)
* Removed deprecation rclcpp::spin_some(node) ([#824 ](https://github.com/ros2/geometry2/issues/824)_)
* Adding NodeInterfaces API Design ([#714 ](https://github.com/ros2/geometry2/issues/714)_)
* ger rid of deprecated rclcpp::spin_some(). ([#821 ](https://github.com/ros2/geometry2/issues/821)_)
* Ensure variable is considered volatile in message_filter_test ([#812 ](https://github.com/ros2/geometry2/issues/812)_)
* Change tf2_ros C to C++ headers ([#805 ](https://github.com/ros2/geometry2/issues/805)_)
* Fix message filter target frames string ([#803 ](https://github.com/ros2/geometry2/issues/803)_)
* Remove deprecation warnings ([#790 ](https://github.com/ros2/geometry2/issues/790)_)
* Uniform cmake min version ([#764 ](https://github.com/ros2/geometry2/issues/764)_)
* Add [`rclcpp::shutdown`` (`#762 ](https://github.com/ros2/geometry2/issues/762)_)
* Fix external docs mappings ([#757 ](https://github.com/ros2/geometry2/issues/757)_)
* Contributors: Alejandro Hernández Cordero, Auguste Lalande, Emerson Knapp, Emmanuel, Gary Servin, Lucas Wendland, Mirko Ferrati, R Kent James, Sergei Zobov, Tomoya Fujita, Yuyuan Yuan, mergify[bot], mini-1235, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_ros_py <https://github.com/ros2/geometry2/tree/lyrical/tf2_ros_py/CHANGELOG.rst>`__

* fix typos ([#921 ](https://github.com/ros2/geometry2/issues/921)_)
* flake8 fixes ([#919 ](https://github.com/ros2/geometry2/issues/919)_)
* prevent AttributeError when static_only=true ([#906 ](https://github.com/ros2/geometry2/issues/906)_)
* fixed typoe in buffer.py ([#905 ](https://github.com/ros2/geometry2/issues/905)_)
* Increase robustness of listener and broadcaster test ([#894 ](https://github.com/ros2/geometry2/issues/894)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Disable TAGFILES in rosdoc2 to separate namespace tf2 documentation into packages ([#856 ](https://github.com/ros2/geometry2/issues/856)_)
* Cleanup TF2 dependencies ([#843 ](https://github.com/ros2/geometry2/issues/843)_)
* Fixed inconsistency of C++ and Python implementations of StaticTransformPublisher ([#820 ](https://github.com/ros2/geometry2/issues/820)_)
* Fix deprecation warning ([#804 ](https://github.com/ros2/geometry2/issues/804)_)
* Remove deprecation warnings ([#790 ](https://github.com/ros2/geometry2/issues/790)_)
* Fix external docs mappings ([#757 ](https://github.com/ros2/geometry2/issues/757)_)
* Contributors: Alejandro Hernández Cordero, Auguste Lalande, Chris Lalancette, Dominik, Emmanuel, Michael Carlstrom, Michael Carroll, R Kent James, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_sensor_msgs <https://github.com/ros2/geometry2/tree/lyrical/tf2_sensor_msgs/CHANGELOG.rst>`__

* fix typos ([#921 ](https://github.com/ros2/geometry2/issues/921)_)
* Use new ROSIDL aggregate CMake target ([#907 ](https://github.com/ros2/geometry2/issues/907)_)
* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Solved TODO with copyright in tf2_sensor_msgs ([#836 ](https://github.com/ros2/geometry2/issues/836)_)
* Removed orocos kdl vendor dependency ([#826 ](https://github.com/ros2/geometry2/issues/826)_)
* Add imu & mag support in [`tf2_sensor_msgs`` (`#800 ](https://github.com/ros2/geometry2/issues/800)_) ([#813 ](https://github.com/ros2/geometry2/issues/813)_)
* Change tf2_ros C to C++ headers ([#805 ](https://github.com/ros2/geometry2/issues/805)_)
* Add normals rotation in [`PointCloud2`` ``doTransform`` (`#792 ](https://github.com/ros2/geometry2/issues/792)_)
* Contributors: Alejandro Hernández Cordero, Auguste Lalande, Emerson Knapp, Gary Servin, Patrick Roncagliolo, R Kent James


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_tools <https://github.com/ros2/geometry2/tree/lyrical/tf2_tools/CHANGELOG.rst>`__

* Modernize conf.py files to only include modified Copyright, eliminati… ([#865 ](https://github.com/ros2/geometry2/issues/865)_)
* Fix Setuptools deprecations ([#809 ](https://github.com/ros2/geometry2/issues/809)_)
* Contributors: R Kent James, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tlsf <https://github.com/ros2/tlsf/tree/lyrical/tlsf/CHANGELOG.rst>`__

* update cmake requirements ([#18 ](https://github.com/ros2/tlsf/issues/18)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tlsf_cpp <https://github.com/ros2/realtime_support/tree/lyrical/tlsf_cpp/CHANGELOG.rst>`__

* cleanups and removed dead code ([#141 ](https://github.com/ros2/realtime_support/issues/141)_) ([#144 ](https://github.com/ros2/realtime_support/issues/144)_)
* fix: Removed AllocatorMemoryStrategy (backport [#140 ](https://github.com/ros2/realtime_support/issues/140)_) ([#142 ](https://github.com/ros2/realtime_support/issues/142)_)
* Remove deprecation warnings ([#139 ](https://github.com/ros2/realtime_support/issues/139)_)
* Use new ROSIDL aggregate CMake target ([#137 ](https://github.com/ros2/realtime_support/issues/137)_)
* tlsf_cpp: add test isolation ([#136 ](https://github.com/ros2/realtime_support/issues/136)_)
* Update subscription callback signatures ([#135 ](https://github.com/ros2/realtime_support/issues/135)_)
* Fix cmake deprecation ([#134 ](https://github.com/ros2/realtime_support/issues/134)_)
* Explicitly shutdown context before test exits ([#129 ](https://github.com/ros2/realtime_support/issues/129)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Julien Enoch, mergify[bot], mini-1235, mosfet80, yadunund


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `topic_monitor <https://github.com/ros2/demos/tree/lyrical/topic_monitor/CHANGELOG.rst>`__

* Add mypy config ([#776 ](https://github.com/ros2/demos//issues/776)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* fix setuptools deprecations ([#733 ](https://github.com/ros2/demos/issues/733)_)
* Update README.md ([#718 ](https://github.com/ros2/demos/issues/718)_) ([#719 ](https://github.com/ros2/demos/issues/719)_)
* Contributors: Dan Mascarenhas, Lucas Wendland, mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `topic_statistics_demo <https://github.com/ros2/demos/tree/lyrical/topic_statistics_demo/CHANGELOG.rst>`__

* Use new ROSIDL aggregate CMake target ([#781 ](https://github.com/ros2/demos//issues/781)_)
* Switching to example_interfaces ([#674 ](https://github.com/ros2/demos/issues/674)_)
* Uniform CMAKE min VERSION ([#714 ](https://github.com/ros2/demos/issues/714)_)
* Contributors: Emerson Knapp, Lucas Wendland, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools <https://github.com/ros2/ros2_tracing/tree/lyrical/tracetools/CHANGELOG.rst>`__

* Support tracepoints for complex message flow annotation used by ROS 2 plugin of Eclipse Trace Compass ([#233 ](https://github.com/ros2/ros2_tracing/issues/233)_)
* Removed warning ([#225 ](https://github.com/ros2/ros2_tracing/issues/225)_)
* Add runtime tracing opt-out mechanism ([#185 ](https://github.com/ros2/ros2_tracing/issues/185)_)
* Fix Clang warnings by using proper function prototypes in macros ([#179 ](https://github.com/ros2/ros2_tracing/issues/179)_)
* Update CMakeLists.txt ([#176 ](https://github.com/ros2/ros2_tracing/issues/176)_)
* Removed clang warning ([#168 ](https://github.com/ros2/ros2_tracing/issues/168)_)
* Contributors: Alejandro Hernández Cordero, Michel Hidalgo, Raphael van Kempen, Shravan Deva, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools_launch <https://github.com/ros2/ros2_tracing/tree/lyrical/tracetools_launch/CHANGELOG.rst>`__

* tracetools_launch: use parse_if_substitutions for non-string action params ([#234 ](https://github.com/ros2/ros2_tracing/issues/234)_)
* Add example launch files for snapshot mode ([#206 ](https://github.com/ros2/ros2_tracing/issues/206)_)
* Allow creating snapshot sessions ([#195 ](https://github.com/ros2/ros2_tracing/issues/195)_)
* Add launch files with preconfigured dual session ([#196 ](https://github.com/ros2/ros2_tracing/issues/196)_)
* Add support for starting tracing at runtime ([#191 ](https://github.com/ros2/ros2_tracing/issues/191)_)
* fix setuptools deprecation ([#189 ](https://github.com/ros2/ros2_tracing/issues/189)_)
* Make trace action parameters substitutable for xml and yaml launch files ([#188 ](https://github.com/ros2/ros2_tracing/issues/188)_)
* Make trace action parameters substitutable ([#187 ](https://github.com/ros2/ros2_tracing/issues/187)_)
* Address typing issues reported by mypy in tracetools_launch ([#184 ](https://github.com/ros2/ros2_tracing/issues/184)_)
* Contributors: Christophe Bedard, Sarthak Bagga, Shravan Deva, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools_read <https://github.com/ros2/ros2_tracing/tree/lyrical/tracetools_read/CHANGELOG.rst>`__

* Work around segfault when reading trace with babeltrace1 Python API ([#246 ](https://github.com/ros2/ros2_tracing/issues/246)_)
* Ignore A0005 ([#237 ](https://github.com/ros2/ros2_tracing/issues/237)_)
* fix setuptools deprecation ([#189 ](https://github.com/ros2/ros2_tracing/issues/189)_)
* Address typing issues reported by mypy in tracetools_launch ([#184 ](https://github.com/ros2/ros2_tracing/issues/184)_)
* Contributors: Christophe Bedard, Michael Carlstrom, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools_test <https://github.com/ros2/ros2_tracing/tree/lyrical/tracetools_test/CHANGELOG.rst>`__

* Set default values on TraceTestCase to avoid errors on >=8.2.0 pytest ([#236 ](https://github.com/ros2/ros2_tracing/issues/236)_)
* Only check test process events in test_runtime_disable ([#193 ](https://github.com/ros2/ros2_tracing/issues/193)_)
* fix setuptools deprecation ([#189 ](https://github.com/ros2/ros2_tracing/issues/189)_)
* Address typing issues reported by mypy in tracetools_launch ([#184 ](https://github.com/ros2/ros2_tracing/issues/184)_)
* Contributors: Christophe Bedard, Clara Berendsen, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools_trace <https://github.com/ros2/ros2_tracing/tree/lyrical/tracetools_trace/CHANGELOG.rst>`__

* Support tracepoints for complex message flow annotation used by ROS 2 plugin of Eclipse Trace Compass ([#233 ](https://github.com/ros2/ros2_tracing/issues/233)_)
* Ignore A0005 ([#237 ](https://github.com/ros2/ros2_tracing/issues/237)_)
* Add exec_depend on procps to tracetools_trace for ps command ([#227 ](https://github.com/ros2/ros2_tracing/issues/227)_)
* Handle SIGTERM and gracefully stop tracing in interactive tracing mode ([#219 ](https://github.com/ros2/ros2_tracing/issues/219)_)
* Use overwrite mode for snapshot sessions ([#210 ](https://github.com/ros2/ros2_tracing/issues/210)_)
* Allow creating snapshot sessions ([#195 ](https://github.com/ros2/ros2_tracing/issues/195)_)
* Add support for starting tracing at runtime ([#191 ](https://github.com/ros2/ros2_tracing/issues/191)_)
* fix setuptools deprecation ([#189 ](https://github.com/ros2/ros2_tracing/issues/189)_)
* Address typing issues reported by mypy in tracetools_launch ([#184 ](https://github.com/ros2/ros2_tracing/issues/184)_)
* Warn if kernel might be paranoid about 'perf:thread:' context fields ([#173 ](https://github.com/ros2/ros2_tracing/issues/173)_)
* Fix pluralization in ros2 trace output ([#169 ](https://github.com/ros2/ros2_tracing/issues/169)_)
* Contributors: Christophe Bedard, Michael Carlstrom, Raphael van Kempen, Shravan Deva, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `trajectory_msgs <https://github.com/ros2/common_interfaces/tree/lyrical/trajectory_msgs/CHANGELOG.rst>`__

* Fix CMAKE deprecation ([#288 ](https://github.com/ros2/common_interfaces/issues/288)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `turtlesim <https://github.com/ros/ros_tutorials/tree/lyrical/turtlesim/CHANGELOG.rst>`__

* Add icon for Lyrical Luth ([#196 ](https://github.com/ros/ros_tutorials/issues/196)_) ([#197 ](https://github.com/ros/ros_tutorials/issues/197)_)
* Use rosdep keys that select Qt5 or Qt6 by platform ([#195 ](https://github.com/ros/ros_tutorials/issues/195)_)
* Use new ROSIDL aggregate CMake target ([#194 ](https://github.com/ros/ros_tutorials/issues/194)_)
* Use get_package_share_path ([#193 ](https://github.com/ros/ros_tutorials/issues/193)_)
* fix bug loading turtle images ([#192 ](https://github.com/ros/ros_tutorials//issues/192)_)
* Updated deprecated ament_index_cpp API ([#190 ](https://github.com/ros/ros_tutorials/issues/190)_)
* Use qt6 as the default dependency from rosdep ([#189 ](https://github.com/ros/ros_tutorials/issues/189)_)
* get rid of deprecated rclcpp::spin_some() ([#183 ](https://github.com/ros/ros_tutorials/issues/183)_)
* Support Qt6 ([#170 ](https://github.com/ros/ros_tutorials/issues/170)_)
* Add icon for Kilted Kaiju ([#180 ](https://github.com/ros/ros_tutorials/issues/180)_)
* Contributors: Alejandro Hernández Cordero, Emerson Knapp, Scott K Logan, Shane Loretz, dcconner, mergify[bot]


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `turtlesim_msgs <https://github.com/ros/ros_tutorials/tree/lyrical/turtlesim_msgs/CHANGELOG.rst>`__

* fix: swap action and message file group names in CMakeLists.txt ([#186 ](https://github.com/ros/ros_tutorials/issues/186)_) ([#187 ](https://github.com/ros/ros_tutorials/issues/187)_)
* fix cmake deprecation ([#182 ](https://github.com/ros/ros_tutorials/issues/182)_)
* Contributors: mergify[bot], mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `type_description_interfaces <https://github.com/ros2/rcl_interfaces/tree/lyrical/type_description_interfaces/CHANGELOG.rst>`__

* Fix cmake deprecation ([#180 ](https://github.com/ros2/rcl_interfaces/issues/180)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `uncrustify_vendor <https://github.com/ament/uncrustify_vendor/tree/lyrical/CHANGELOG.rst>`__

* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#38 ](https://github.com/ament/uncrustify_vendor/issues/38)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `unique_identifier_msgs <https://github.com/ros2/unique_identifier_msgs/tree/lyrical/CHANGELOG.rst>`__

* fix cmake deprecation ([#33 ](https://github.com/ros2/unique_identifier_msgs/issues/33)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#31 ](https://github.com/ros2/unique_identifier_msgs/issues/31)_)
* Contributors: Chris Lalancette, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `urdf <https://github.com/ros2/urdf/tree/lyrical/urdf/CHANGELOG.rst>`__

* Remove [`urdf_world/types.h`` deprecation (`#54 ](https://github.com/ros2/urdf/issues/54)_)
* Fix CMAKE deprecation ([#48 ](https://github.com/ros2/urdf/issues/48)_)
* Removed tinyxml2_vendor dependency ([#47 ](https://github.com/ros2/urdf/issues/47)_)
* Contributors: Alejandro Hernández Cordero, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `urdf_parser_plugin <https://github.com/ros2/urdf/tree/lyrical/urdf_parser_plugin/CHANGELOG.rst>`__

* Remove [`urdf_world/types.h`` deprecation (`#54 ](https://github.com/ros2/urdf/issues/54)_)
* Fix CMAKE deprecation ([#48 ](https://github.com/ros2/urdf/issues/48)_) cmake version < then 3.10 is deprecated
* Contributors: Alejandro Hernández Cordero, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `urdfdom <https://github.com/ros/urdfdom/tree/lyrical/CHANGELOG.rst>`__

* Support for URDF Specification 1.2 * Extend parsing of acceleration, deceleration and jerk limits from [`limit`` tag (`#212 ](https://github.com/ros/urdfdom/issues/212)_) * Update default limits for the joint limits and safety limits ([#249 ](https://github.com/ros/urdfdom/issues/249)_) * Add invalid data checks to the Geometry data ([#242 ](https://github.com/ros/urdfdom/issues/242)_) * Require urdfdom_headers 3.0.0 ([#257 ](https://github.com/ros/urdfdom/issues/257)_)
* Use URDF_MAJOR_VERSION for SOVERSION ([#248 ](https://github.com/ros/urdfdom/issues/248)_)
* Revert "Extend parsing of acceleration, deceleration and jerk limits from [`limit`` tag (`#212 ](https://github.com/ros/urdfdom/issues/212)_)" This was a breaking change that will be released in 6.0.0
* Prevent CI from failing fast to allow all builds to complete ([#254 ](https://github.com/ros/urdfdom/issues/254)_)
* Remove [`urdf_world/types.h`` deprecation (`#251 ](https://github.com/ros/urdfdom/issues/251)_)
* Extend parsing of acceleration, deceleration and jerk limits from [`limit`` tag (`#212 ](https://github.com/ros/urdfdom/issues/212)_)
* ROS 2 CI: build urdfdom_headers from source ([#246 ](https://github.com/ros/urdfdom/issues/246)_)
* Disable system workflow because [`urdfdom_headers`` isn't available on Ubuntu 24.04 (`#240 ](https://github.com/ros/urdfdom/issues/240)_)
* Fix ROS 2 CI workflow by updating Ubuntu version and checkout action ([#239 ](https://github.com/ros/urdfdom/issues/239)_)
* Support for URDF Specification 1.1 * Add support for capsule geometry type ([#238 ](https://github.com/ros/urdfdom/issues/238)_) * Add documentation about versioning * Require version 2.1.0 of urdfdom_headers Co-authored-by: Steve Peters <scpeters@openrobotics.org> * Support quaternions in URDF 1.1 ([#235 ](https://github.com/ros/urdfdom/issues/235)_) Co-authored-by: Guillaume Doisy <doisyg@users.noreply.github.com>
* Fix multiple format-string vulnerabilities in URDF parser logging ([#243 ](https://github.com/ros/urdfdom/issues/243)_) User-controlled URDF content was passed directly to CONSOLE_BRIDGE_logError() at multiple call sites, allowing printf-style format string interpretation. All affected logging paths now use explicit "%s" format specifiers to ensure input is treated as data and to prevent information disclosure or undefined behavior.
* More logging format string fixes ([#244 ](https://github.com/ros/urdfdom/issues/244)_) * Add explicit "%s" format strings when logging * Use %s format string instead of string addition
* Read cmake version from package.xml ([#236 ](https://github.com/ros/urdfdom/issues/236)_) * Use regex to match version string. Based on suggestion from Chris Lalancette. * Require cmake minimum version 3.10 Co-authored-by: Chris Lalancette <clalancette@gmail.com>
* Revert "Quaternion in urdf (PR123 new attempt) (#231)" ([#231 ](https://github.com/ros/urdfdom/issues/231)_)
* Quaternion in urdf (PR123 new attempt) ([#194 ](https://github.com/ros/urdfdom/issues/194)_)
* Removed tinyxml2_vendor dependency ([#225 ](https://github.com/ros/urdfdom/issues/225)_)
* Relax the version compatibility for urdfdom_headers. ([#222 ](https://github.com/ros/urdfdom/issues/222)_)
* Removed deprecated code ([#217 ](https://github.com/ros/urdfdom/issues/217)_)
* Remove ROS 1 workflows and update ROS 2 ([#218 ](https://github.com/ros/urdfdom/issues/218)_)
* Improvements for the URDF xsd specification  ([#200 ](https://github.com/ros/urdfdom/issues/200)_)
* Update ros2.yaml ([#214 ](https://github.com/ros/urdfdom/issues/214)_)
* fix: missing header ([#216 ](https://github.com/ros/urdfdom/issues/216)_)
* Contributors: Alejandro Hernández Cordero, Amin Ya, Chris Lalancette, Florencia, Guillaume Doisy, Jose Luis Rivero, Pierre Ballif, Sai Kishor Kothakota, Steve Peters, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `urdfdom_headers <https://github.com/ros/urdfdom_headers/tree/lyrical/CHANGELOG.rst>`__

* Update lower, upper, effort, and velocity default joint limits ([#95 ](https://github.com/ros/urdfdom_headers/issues/95)_)
* Clean up declaration of ModelInterface's SharedPtrs ([#99 ](https://github.com/ros/urdfdom_headers/issues/99)_)
* Extend [`JointLimits`` class to include acceleration, deceleration and jerk limits (`#83 ](https://github.com/ros/urdfdom_headers/issues/83)_)
* Revert "Extend JointLimits class to include acceleration, deceleration and jerk limits ([#83 ](https://github.com/ros/urdfdom_headers/issues/83)_)" This was a breaking change that will be released in 3.0.0
* Clean up declaration of ModelInterface's SharedPtrs ([#99 ](https://github.com/ros/urdfdom_headers/issues/99)_)
* Revert cleanup of ModelInterface's SharedPtrs ([#33 ](https://github.com/ros/urdfdom_headers/issues/33)_)
* Revert fix for assumption that CMAKE_INSTALL_*DIR paths are relative ([#90 ](https://github.com/ros/urdfdom_headers/issues/90)_) ([#97 ](https://github.com/ros/urdfdom_headers/issues/97)_)
* Clean up declaration of ModelInterface's SharedPtrs ([#33 ](https://github.com/ros/urdfdom_headers/issues/33)_)
* Fix assumption that CMAKE_INSTALL_*DIR paths are relative ([#90 ](https://github.com/ros/urdfdom_headers/issues/90)_)
* Extend [`JointLimits`` class to include acceleration, deceleration and jerk limits (`#83 ](https://github.com/ros/urdfdom_headers/issues/83)_)
* Add support for capsule geometry type ([#94 ](https://github.com/ros/urdfdom_headers/issues/94)_)
* 2.0.2
* Read cmake version from package.xml ([#92 ](https://github.com/ros/urdfdom_headers/issues/92)_) Use regex to match version string. Copied from [ros/urdfdom#236 ](https://github.com/ros/urdfdom/issues/236)_.
* quaternions in urdf (PR 51 new attempt) + bump version ([#77 ](https://github.com/ros/urdfdom_headers/issues/77)_)
* fix cmake deprecation ([#89 ](https://github.com/ros/urdfdom_headers/issues/89)_) cmake version < then 3.10 is deprecated
* 2.0.0
* Remove all dependencies from the package.xml. ([#88 ](https://github.com/ros/urdfdom_headers/issues/88)_) This package does not have any header dependencies, so we don't need any of them here.
* Fix package.xml deps to use vendored packages ([#87 ](https://github.com/ros/urdfdom_headers/issues/87)_)
* add package.xml file from release repository ([#85 ](https://github.com/ros/urdfdom_headers/issues/85)_)
* Removed headers, implementation was deprecated and removed ([#86 ](https://github.com/ros/urdfdom_headers/issues/86)_)
* Remove CODEOWNERS. ([#81 ](https://github.com/ros/urdfdom_headers/issues/81)_) It is outdated and no longer serving its intended purpose.
* Contributors: Aarav Gupta, Alejandro Hernández Cordero, Chris Lalancette, Guillaume Doisy, Jorge J. Perez, Lucien Morey, Michal Sojka, Robert Haschke, Sai Kishor Kothakota, Steve Peters, mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `visualization_msgs <https://github.com/ros2/common_interfaces/tree/lyrical/visualization_msgs/CHANGELOG.rst>`__

* Fix CMAKE deprecation ([#288 ](https://github.com/ros2/common_interfaces/issues/288)_)
* Contributors: mosfet80


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `yaml_cpp_vendor <https://github.com/ros2/yaml_cpp_vendor/tree/lyrical/CHANGELOG.rst>`__

* Replace ament_vendor with cmake modules ([#56 ](https://github.com/ros2/yaml_cpp_vendor/issues/56)_)
* Remove CODEOWNERS and mirror-rolling-to-master workflow. ([#52 ](https://github.com/ros2/yaml_cpp_vendor/issues/52)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `zenoh_cpp_vendor <https://github.com/ros2/rmw_zenoh/tree/lyrical/zenoh_cpp_vendor/CHANGELOG.rst>`__

* Use zenoh-cpp 481b71b fixing build with MSVC 2022 in C++20 mode ([#969 ](https://github.com/ros2/rmw_zenoh/issues/969)_)
* Bump Zenoh to 1.8.0, fix Windows shutdown hang, and resolve synchronization with [`undeclare`` (`#964 ](https://github.com/ros2/rmw_zenoh/issues/964)_)
* Revert changes to build against rust >= 1.75 and bump zenoh to 1.8.0 ([#960 ](https://github.com/ros2/rmw_zenoh/issues/960)_)
* Revert patch of Cargo.lock with new Zenoh commit due to Windows test failures ([#959 ](https://github.com/ros2/rmw_zenoh/issues/959)_)
* Update Cargo.lock with new Zenoh commit ([#957 ](https://github.com/ros2/rmw_zenoh/issues/957)_)
* Build against [`rust >= 1.75`` for ROS Lyrical (`#945 ](https://github.com/ros2/rmw_zenoh/issues/945)_)
* Bump zenoh to 1.8.0 ([#935 ](https://github.com/ros2/rmw_zenoh/issues/935)_)
* Allow use of non-vendored Zenoh if present ([#908 ](https://github.com/ros2/rmw_zenoh/issues/908)_)
* Bump [`zenoh`` to 1.7.1 (`#870 ](https://github.com/ros2/rmw_zenoh/issues/870)_)
* Fix REP url locations ([#858 ](https://github.com/ros2/rmw_zenoh/issues/858)_)
* Bump zenoh to 1.6.2 ([#842 ](https://github.com/ros2/rmw_zenoh/issues/842)_)
* Bump Zenoh to 1.5.1 ([#774 ](https://github.com/ros2/rmw_zenoh/issues/774)_)
* Bump Zenoh to v1.5.0 ([#728 ](https://github.com/ros2/rmw_zenoh/issues/728)_)
* Change zenoh-c features to use its default + shared-memory + transport_serial ([#692 ](https://github.com/ros2/rmw_zenoh/issues/692)_)
* Bump Zenoh to 1.4.0 ([#652 ](https://github.com/ros2/rmw_zenoh/issues/652)_)
* fix: pin rust toolchain to v1.75.0 ([#602 ](https://github.com/ros2/rmw_zenoh/issues/602)_)
* fix: use the right commit to bump zenoh to v1.3.2 ([#607 ](https://github.com/ros2/rmw_zenoh/issues/607)_)
* Contributors: ChenYing Kuo (CY), Julien Enoch, Shane Loretz, Tim Clephas, Yadunund, Yuyuan Yuan, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `zenoh_security_tools <https://github.com/ros2/rmw_zenoh/tree/lyrical/zenoh_security_tools/CHANGELOG.rst>`__

* Address outstanding TODO items ([#896 ](https://github.com/ros2/rmw_zenoh/issues/896)_)
* Removed tinyxml2_vendor dependency ([#829 ](https://github.com/ros2/rmw_zenoh/issues/829)_)
* Fix commands in zenoh_security_tools README ([#814 ](https://github.com/ros2/rmw_zenoh/issues/814)_)
* Revert "fix: handle missing enclaves_dir argument for zenoh_security_tools (#…" ([#802 ](https://github.com/ros2/rmw_zenoh/issues/802)_)
* Correct a description error in the zenoh_security_tools README ([#789 ](https://github.com/ros2/rmw_zenoh/issues/789)_)
* fix: handle missing enclaves_dir argument for zenoh_security_tools ([#788 ](https://github.com/ros2/rmw_zenoh/issues/788)_)
* SROS: add ACL rules for TRANSIENT_LOCAL pub/sub (fix [#753 ](https://github.com/ros2/rmw_zenoh/issues/753)_) ([#779 ](https://github.com/ros2/rmw_zenoh/issues/779)_)
* Fix handling of enclave path in zenoh_security_tools ([#770 ](https://github.com/ros2/rmw_zenoh/issues/770)_)
* Update CMakeLists.txt ([#617 ](https://github.com/ros2/rmw_zenoh/issues/617)_)
* Fix warning on Windows ([#615 ](https://github.com/ros2/rmw_zenoh/issues/615)_)
* Contributors: Alejandro Hernández Cordero, Barry Xu, Christophe Bedard, Julien Enoch, Tomoya Fujita, Yadunund, mosfet80




---
[返回](../index.md)
