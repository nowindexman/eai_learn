> 原文地址：https://docs.ros.org/en/jazzy/Releases/Humble-Hawksbill-Complete-Changelog.html

# Humble Hawksbill changelog

This page is a list of the complete changes in all ROS 2 core packages since the previous release.

   :local:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `action_msgs <https://github.com/ros2/rcl_interfaces/tree/humble/action_msgs/CHANGELOG.rst>`__

* Update maintainers to Chris Lalancette ([#130 ](https://github.com/ros2/rcl_interfaces/issues/130)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `action_tutorials_cpp <https://github.com/ros2/demos/tree/humble/action_tutorials/action_tutorials_cpp/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `action_tutorials_interfaces <https://github.com/ros2/demos/tree/humble/action_tutorials/action_tutorials_interfaces/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `action_tutorials_py <https://github.com/ros2/demos/tree/humble/action_tutorials/action_tutorials_py/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `actionlib_msgs <https://github.com/ros2/common_interfaces/tree/humble/actionlib_msgs/CHANGELOG.rst>`__

* Interface packages should fully <depend> on the interface packages that they depend on ([#173 ](https://github.com/ros2/common_interfaces/issues/173)_)
* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Contributors: Audrow Nash, Grey


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_clang_format <https://github.com/ament/ament_lint/tree/humble/ament_clang_format/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_clang_tidy <https://github.com/ament/ament_lint/tree/humble/ament_clang_tidy/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* remove google style from clang-tidy default settings, removing need for default config file ([#337 ](https://github.com/ament/ament_lint/issues/337)_)
* Improvements to ament_lint_clang_tidy. ([#316 ](https://github.com/ament/ament_lint/issues/316)_)
* Contributors: Audrow Nash, Steven! Ragnarök, William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake <https://github.com/ament/ament_cmake/tree/humble/ament_cmake/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Add ament_cmake_gen_version_h package ([#198 ](https://github.com/ament/ament_cmake/issues/198)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz, serge-nikulin


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_auto <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_auto/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Fix typo in ament_auto_find_test_dependencies ([#363 ](https://github.com/ament/ament_cmake/issues/363)_)
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Add ament_auto_add_gtest ([#344 ](https://github.com/ament/ament_cmake/issues/344)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Daisuke Nishimatsu, Joshua Whitley, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_clang_format <https://github.com/ament/ament_lint/tree/humble/ament_cmake_clang_format/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_clang_tidy <https://github.com/ament/ament_lint/tree/humble/ament_cmake_clang_tidy/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Improvements to ament_lint_clang_tidy. ([#316 ](https://github.com/ament/ament_lint/issues/316)_)
* Contributors: Audrow Nash, Steven! Ragnarök


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_copyright <https://github.com/ament/ament_lint/tree/humble/ament_cmake_copyright/CHANGELOG.rst>`__

* Increase the ament_cmake_copyright default timeout. ([#355 ](https://github.com/ament/ament_lint/issues/355)_)
* Update forthcoming version in changelogs
* [ament_cmake_copyright] Add file exclusion support ([#328 ](https://github.com/ament/ament_lint/issues/328)_) * [ament_cmake_copyright] Add file exclusion support In the ``ament_copyright`` CMake function, the optional list argument ``EXCLUDE`` can now be used as an exclusion specifier. * [ament_cmake_copyright] Fix function header typo Remove reference to ``cppcheck`` in the ``EXCLUDE`` arg description.
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_core <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_core/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Resolve various ament_lint linter violations ([#360 ](https://github.com/ament/ament_cmake/issues/360)_) We can't add ament_lint linters in ament_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can't automatically enforce linting, it's still a good idea to try to keep conformance where possible.
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Support commands with executable targets ([#352 ](https://github.com/ament/ament_cmake/issues/352)_)
* doc/resource_index: Indent list subitems correctly ([#342 ](https://github.com/ament/ament_cmake/issues/342)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Michal Sojka, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_cppcheck <https://github.com/ament/ament_lint/tree/humble/ament_cmake_cppcheck/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* [ament_cmake_cppcheck] Fix file exclusion behavior ([#329 ](https://github.com/ament/ament_lint/issues/329)_) The ``EXCLUDE`` argument of the ``ament_cppcheck`` CMake function is a list, i.e. a multi-value keyword. As such, it needs to be placed out of the one-value keywords from the ``cmake_parse_arguments`` function call.
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Add cppcheck libraries option ([#323 ](https://github.com/ament/ament_lint/issues/323)_) * adding ament_cppcheck libraries option * pass libraries option via CMake Co-authored-by: William Wedler <william.wedler@resquared.com>
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Will


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_cpplint <https://github.com/ament/ament_lint/tree/humble/ament_cmake_cpplint/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_export_definitions <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_definitions/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_export_dependencies <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_dependencies/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Resolve various ament_lint linter violations ([#360 ](https://github.com/ament/ament_cmake/issues/360)_) We can't add ament_lint linters in ament_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can't automatically enforce linting, it's still a good idea to try to keep conformance where possible.
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_export_include_directories <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_include_directories/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_export_interfaces <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_interfaces/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_export_libraries <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_libraries/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Resolve various ament_lint linter violations ([#360 ](https://github.com/ament/ament_cmake/issues/360)_) We can't add ament_lint linters in ament_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can't automatically enforce linting, it's still a good idea to try to keep conformance where possible.
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Add note regarding interface libraries ([#339 ](https://github.com/ament/ament_cmake/issues/339)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Bjar Ne, Chris Lalancette, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_export_link_flags <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_link_flags/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_export_targets <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_export_targets/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_flake8 <https://github.com/ament/ament_lint/tree/humble/ament_cmake_flake8/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Add custom config file support for flake8 ([#331 ](https://github.com/ament/ament_lint/issues/331)_)
* Contributors: Audrow Nash, Kenji Miyake


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_gen_version_h <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_gen_version_h/CHANGELOG.rst>`__

* Add ament_generate_version_header and deprecate ament_cmake_gen_version_h ([#377 ](https://github.com/ament/ament_cmake/issues/377)_)
* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Add ament_cmake_gen_version_h package ([#198 ](https://github.com/ament/ament_cmake/issues/198)_)
* Contributors: Audrow Nash, Shane Loretz, serge-nikulin


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_gmock <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_gmock/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_google_benchmark <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_google_benchmark/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Resolve various ament_lint linter violations ([#360 ](https://github.com/ament/ament_cmake/issues/360)_) We can't add ament_lint linters in ament_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can't automatically enforce linting, it's still a good idea to try to keep conformance where possible.
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_gtest <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_gtest/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_include_directories <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_include_directories/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Make ament_include_directories_order a function to allow paths with backslashes on windows. ([#371 ](https://github.com/ament/ament_cmake/issues/371)_) * Repalce backslashes with forward slashes on Windows * Typo * Replace slashes in ARGN * Don't quote * Check ARGN has values before trying to string(REPLACE them * Make ament_include_directories_order a function
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_libraries <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_libraries/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Resolve various ament_lint linter violations ([#360 ](https://github.com/ament/ament_cmake/issues/360)_) We can't add ament_lint linters in ament_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can't automatically enforce linting, it's still a good idea to try to keep conformance where possible.
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_lint_cmake <https://github.com/ament/ament_lint/tree/humble/ament_cmake_lint_cmake/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_mypy <https://github.com/ament/ament_lint/tree/humble/ament_cmake_mypy/CHANGELOG.rst>`__

* Improve documentation by clarifying the purpose of different tools ([#357 ](https://github.com/ament/ament_lint/issues/357)_)
* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash, Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_nose <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_nose/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Support commands with executable targets ([#352 ](https://github.com/ament/ament_cmake/issues/352)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_pclint <https://github.com/ament/ament_lint/tree/humble/ament_cmake_pclint/CHANGELOG.rst>`__

* Improve documentation by clarifying the purpose of different tools ([#357 ](https://github.com/ament/ament_lint/issues/357)_)
* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash, Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_pep257 <https://github.com/ament/ament_lint/tree/humble/ament_cmake_pep257/CHANGELOG.rst>`__

* Improve documentation by clarifying the purpose of different tools ([#357 ](https://github.com/ament/ament_lint/issues/357)_)
* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash, Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_pycodestyle <https://github.com/ament/ament_lint/tree/humble/ament_cmake_pycodestyle/CHANGELOG.rst>`__

* Improve documentation by clarifying the purpose of different tools ([#357 ](https://github.com/ament/ament_lint/issues/357)_)
* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash, Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_pyflakes <https://github.com/ament/ament_lint/tree/humble/ament_cmake_pyflakes/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_pytest <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_pytest/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Fix misleading comment ([#361 ](https://github.com/ament/ament_cmake/issues/361)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Support commands with executable targets ([#352 ](https://github.com/ament/ament_cmake/issues/352)_)
* Mention other platforms in 'pytest/pytest-cov not found' warning ([#337 ](https://github.com/ament/ament_cmake/issues/337)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Christophe Bedard, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_python <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_python/CHANGELOG.rst>`__

* Use sysconfig directly to determine python lib dir ([#378 ](https://github.com/ament/ament_cmake/issues/378)_)
* Update forthcoming version in changelog
* Resolve various ament_lint linter violations ([#360 ](https://github.com/ament/ament_cmake/issues/360)_) We can't add ament_lint linters in ament_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can't automatically enforce linting, it's still a good idea to try to keep conformance where possible.
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Make ament_cmake_python symlink for symlink installs only ([#357 ](https://github.com/ament/ament_cmake/issues/357)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Make ament_python_install_package() match setuptools' egg names. ([#338 ](https://github.com/ament/ament_cmake/issues/338)_)
* Drop ament_cmake_python outdated tests. ([#340 ](https://github.com/ament/ament_cmake/issues/340)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Make ament_python_install_package() install console_scripts ([#328 ](https://github.com/ament/ament_cmake/issues/328)_)
* Contributors: Audrow Nash, Chris Lalancette, Michel Hidalgo, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_ros <https://github.com/ros2/ament_cmake_ros/tree/humble/ament_cmake_ros/CHANGELOG.rst>`__

* Refactor domain_coordinator API to use a context manager ([#12 ](https://github.com/ros2/ament_cmake_ros/issues/12)_)
* Contributors: Timo Röhling


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_target_dependencies <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_target_dependencies/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Fix bug packages with multiple configurations ([#318 ](https://github.com/ament/ament_cmake/issues/318)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_test <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_test/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Resolve various ament_lint linter violations ([#360 ](https://github.com/ament/ament_cmake/issues/360)_) We can't add ament_lint linters in ament_cmake in the traditional way without creating a circular dependency between the repositories. Even though we can't automatically enforce linting, it's still a good idea to try to keep conformance where possible.
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_uncrustify <https://github.com/ament/ament_lint/tree/humble/ament_cmake_uncrustify/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* [ament_cmake_uncrustify] Add file exclude support ([#330 ](https://github.com/ament/ament_lint/issues/330)_) In the ``ament_uncrustify`` CMake function, the optional list argument ``EXCLUDE`` can now be used as an exclusion specifier.
* Contributors: Abrar Rahman Protyasha, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_version <https://github.com/ament/ament_cmake/tree/humble/ament_cmake_version/CHANGELOG.rst>`__

* Update forthcoming version in changelog
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#362 ](https://github.com/ament/ament_cmake/issues/362)_)
* Use FindPython3 instead of FindPythonInterp ([#355 ](https://github.com/ament/ament_cmake/issues/355)_)
* Update maintainers ([#336 ](https://github.com/ament/ament_cmake/issues/336)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cmake_xmllint <https://github.com/ament/ament_lint/tree/humble/ament_cmake_xmllint/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_copyright <https://github.com/ament/ament_lint/tree/humble/ament_copyright/CHANGELOG.rst>`__

* Fix importlib_metadata warning on Python 3.10. ([#365 ](https://github.com/ament/ament_lint/issues/365)_)
* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* [ament_copyright] Fix file exclusion behavior ([#327 ](https://github.com/ament/ament_lint/issues/327)_) * [ament_copyright] Fix file exclusion behavior This commit fixes the faulty file exclusion behavior reported in https://github.com/ament/ament_lint/issues/326. Specifically, the exclusion list is matched against traversed files in the ``crawler`` module. Changes inspired by https://github.com/ament/ament_lint/pull/299/. * Update excluded file path in copyright tests Since file names are not indiscriminately matched throughout the search tree anymore, the excluded files listed in the copyright tests need to be updated relative to the root of the package. * Add test cases to check exclusion behavior Specifically, these tests check for: - Incorrect exclusion of single filenames. - Correct exclusion of relatively/absolutely addressed filenames. - Correct exclusion of wildcarded paths. * Add unit tests for crawler module These unit tests make sure both search and exclusion behaviors are correctly demonstrated by the ``ament_copyright.crawler`` module.
* Add SPDX identifiers to the licenses. ([#315 ](https://github.com/ament/ament_lint/issues/315)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cppcheck <https://github.com/ament/ament_lint/tree/humble/ament_cppcheck/CHANGELOG.rst>`__

* Disable cppcheck 2.x. ([#345 ](https://github.com/ament/ament_lint/issues/345)_)
* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Add cppcheck libraries option ([#323 ](https://github.com/ament/ament_lint/issues/323)_) * adding ament_cppcheck libraries option * pass libraries option via CMake Co-authored-by: William Wedler <william.wedler@resquared.com>
* Contributors: Audrow Nash, Chris Lalancette, Will


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_cpplint <https://github.com/ament/ament_lint/tree/humble/ament_cpplint/CHANGELOG.rst>`__

* ignore NOLINT comments with categories that come from clang-tidy ([#339 ](https://github.com/ament/ament_lint/issues/339)_)
* Update forthcoming version in changelogs
* Reapply patches Reapply parts of 232428752251de61e84ef013bcd643e35eb9038d that are still relevant.
* Update cpplint version Point to the fork https://github.com/cpplint/cpplint Contains updates for modern C++ standards (e.g. C++14 and C++17).
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* [ament_copyright] Fix file exclusion behavior ([#327 ](https://github.com/ament/ament_lint/issues/327)_) * [ament_copyright] Fix file exclusion behavior This commit fixes the faulty file exclusion behavior reported in https://github.com/ament/ament_lint/issues/326. Specifically, the exclusion list is matched against traversed files in the ``crawler`` module. Changes inspired by https://github.com/ament/ament_lint/pull/299/. * Update excluded file path in copyright tests Since file names are not indiscriminately matched throughout the search tree anymore, the excluded files listed in the copyright tests need to be updated relative to the root of the package. * Add test cases to check exclusion behavior Specifically, these tests check for: - Incorrect exclusion of single filenames. - Correct exclusion of relatively/absolutely addressed filenames. - Correct exclusion of wildcarded paths. * Add unit tests for crawler module These unit tests make sure both search and exclusion behaviors are correctly demonstrated by the ``ament_copyright.crawler`` module.
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Dirk Thomas, Jacob Perron, William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_flake8 <https://github.com/ament/ament_lint/tree/humble/ament_flake8/CHANGELOG.rst>`__

* Remove use of distutils.version.LooseVersion. ([#346 ](https://github.com/ament/ament_lint/issues/346)_)
* Update forthcoming version in changelogs
* Ignore .*/_* dirs in ament_flake8 ([#335 ](https://github.com/ament/ament_lint/issues/335)_) Other ament\_* linters specifically ignore directories starting with a dot or underscore when crawling for files to lint. They also do so implicitly, so this change mimics that same pattern so that the behavior is consistent.
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Ignore flake8-blind-except B902 ([#292 ](https://github.com/ament/ament_lint/issues/292)_)
* Contributors: Audrow Nash, Chris Lalancette, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_index_cpp <https://github.com/ament/ament_index/tree/humble/ament_index_cpp/CHANGELOG.rst>`__

* Install includes to include/ ([#83 ](https://github.com/ament/ament_index/issues/83)_)
* Remove ament_export_include_directories and ament_export_libraries ([#81 ](https://github.com/ament/ament_index/issues/81)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_index_python <https://github.com/ament/ament_index/tree/humble/ament_index_python/CHANGELOG.rst>`__

* Print warning when get_package_share_directory() does not exist (Fix [#74 ](https://github.com/ament/ament_index/issues/74)_) ([#77 ](https://github.com/ament/ament_index/issues/77)_)
* Fail lookups on invalid resource names ([#69 ](https://github.com/ament/ament_index/issues/69)_)
* Add get_package_share_path method ([#73 ](https://github.com/ament/ament_index/issues/73)_)
* Contributors: David V. Lu, rob-clarke


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_lint <https://github.com/ament/ament_lint/tree/humble/ament_lint/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_lint_auto <https://github.com/ament/ament_lint/tree/humble/ament_lint_auto/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_lint_cmake <https://github.com/ament/ament_lint/tree/humble/ament_lint_cmake/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* [ament_copyright] Fix file exclusion behavior ([#327 ](https://github.com/ament/ament_lint/issues/327)_) * [ament_copyright] Fix file exclusion behavior This commit fixes the faulty file exclusion behavior reported in https://github.com/ament/ament_lint/issues/326. Specifically, the exclusion list is matched against traversed files in the ``crawler`` module. Changes inspired by https://github.com/ament/ament_lint/pull/299/. * Update excluded file path in copyright tests Since file names are not indiscriminately matched throughout the search tree anymore, the excluded files listed in the copyright tests need to be updated relative to the root of the package. * Add test cases to check exclusion behavior Specifically, these tests check for: - Incorrect exclusion of single filenames. - Correct exclusion of relatively/absolutely addressed filenames. - Correct exclusion of wildcarded paths. * Add unit tests for crawler module These unit tests make sure both search and exclusion behaviors are correctly demonstrated by the ``ament_copyright.crawler`` module.
* Contributors: Abrar Rahman Protyasha, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_lint_common <https://github.com/ament/ament_lint/tree/humble/ament_lint_common/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Fix typo in ament_lint_common/package.xml ([#336 ](https://github.com/ament/ament_lint/issues/336)_)
* Contributors: Audrow Nash, Kenji Miyake


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_mypy <https://github.com/ament/ament_lint/tree/humble/ament_mypy/CHANGELOG.rst>`__

* Improve documentation by clarifying the purpose of different tools ([#357 ](https://github.com/ament/ament_lint/issues/357)_)
* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash, Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_package <https://github.com/ament/ament_package/tree/humble/CHANGELOG.rst>`__

* Set forthcoming for previous version
* Add support for appending to environment variables ([#130 ](https://github.com/ament/ament_package/issues/130)_) This works largely the same as 'prepend-non-duplicate', but instead puts the candidate value at the end of the target variable.
* Update maintainers to Audrow Nash ([#135 ](https://github.com/ament/ament_package/issues/135)_)
* Make python executable variable ament_package specific ([#134 ](https://github.com/ament/ament_package/issues/134)_)
* Contributors: Audrow Nash, Scott K Logan, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_pclint <https://github.com/ament/ament_lint/tree/humble/ament_pclint/CHANGELOG.rst>`__

* Improve documentation by clarifying the purpose of different tools ([#357 ](https://github.com/ament/ament_lint/issues/357)_)
* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* [ament_copyright] Fix file exclusion behavior ([#327 ](https://github.com/ament/ament_lint/issues/327)_) * [ament_copyright] Fix file exclusion behavior This commit fixes the faulty file exclusion behavior reported in https://github.com/ament/ament_lint/issues/326. Specifically, the exclusion list is matched against traversed files in the ``crawler`` module. Changes inspired by https://github.com/ament/ament_lint/pull/299/. * Update excluded file path in copyright tests Since file names are not indiscriminately matched throughout the search tree anymore, the excluded files listed in the copyright tests need to be updated relative to the root of the package. * Add test cases to check exclusion behavior Specifically, these tests check for: - Incorrect exclusion of single filenames. - Correct exclusion of relatively/absolutely addressed filenames. - Correct exclusion of wildcarded paths. * Add unit tests for crawler module These unit tests make sure both search and exclusion behaviors are correctly demonstrated by the ``ament_copyright.crawler`` module.
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_pep257 <https://github.com/ament/ament_lint/tree/humble/ament_pep257/CHANGELOG.rst>`__

* Improve documentation by clarifying the purpose of different tools ([#357 ](https://github.com/ament/ament_lint/issues/357)_)
* Remove use of distutils.version.LooseVersion. ([#346 ](https://github.com/ament/ament_lint/issues/346)_)
* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash, Bi0T1N, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_pycodestyle <https://github.com/ament/ament_lint/tree/humble/ament_pycodestyle/CHANGELOG.rst>`__

* Improve documentation by clarifying the purpose of different tools ([#357 ](https://github.com/ament/ament_lint/issues/357)_)
* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash, Bi0T1N


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_pyflakes <https://github.com/ament/ament_lint/tree/humble/ament_pyflakes/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_uncrustify <https://github.com/ament/ament_lint/tree/humble/ament_uncrustify/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* [ament_uncrustify] Fix file exclusion behavior ([#334 ](https://github.com/ament/ament_lint/issues/334)_) * [ament_uncrustify] Fix file exclusion behavior This PR fixes the file exclusion behavior reported in [#326 ](https://github.com/ament/ament_lint/issues/326)_. Specifically, the exclusion list is matched against files/directories as the search path is traversed. Tries to maintain consistency with [#327 ](https://github.com/ament/ament_lint/issues/327)_. * [ament_uncrustify] Add file exclusion tests * [ament_uncrustify] Remove erroneous pytest marker
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* [ament_uncrustify] Add ament_lint tests ([#338 ](https://github.com/ament/ament_lint/issues/338)_) * Add ``ament_lint`` tests on ``ament_uncrustify`` * Address linter warnings in ``ament_uncrustify``
* Contributors: Abrar Rahman Protyasha, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ament_xmllint <https://github.com/ament/ament_lint/tree/humble/ament_xmllint/CHANGELOG.rst>`__

* Update forthcoming version in changelogs
* Update maintainers to Michael Jeronimo and Michel Hidalgo ([#340 ](https://github.com/ament/ament_lint/issues/340)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `builtin_interfaces <https://github.com/ros2/rcl_interfaces/tree/humble/builtin_interfaces/CHANGELOG.rst>`__

* Update maintainers to Chris Lalancette ([#130 ](https://github.com/ros2/rcl_interfaces/issues/130)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `camera_calibration_parsers <https://github.com/ros-perception/image_common/tree/humble/camera_calibration_parsers/CHANGELOG.rst>`__

* Tests depend on rcpputils ([#236 ](https://github.com/ros-perception/image_common/issues/236)_)
* Remove YAML_CPP_DLL define ([#231 ](https://github.com/ros-perception/image_common/issues/231)_)
* Export a modern CMake target instead of variables and install includes to include/${PROJECT_NAME} ([#218 ](https://github.com/ros-perception/image_common/issues/218)_)
* Update maintainers ([#173 ](https://github.com/ros-perception/image_common/issues/173)_)
* Contributors: Akash, Alejandro Hernández Cordero, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `camera_info_manager <https://github.com/ros-perception/image_common/tree/humble/camera_info_manager/CHANGELOG.rst>`__

* Export a modern CMake target instead of variables and install includes to include/${PROJECT_NAME} ([#218 ](https://github.com/ros-perception/image_common/issues/218)_)
* Update maintainers ([#173 ](https://github.com/ros-perception/image_common/issues/173)_)
* Contributors: Alejandro Hernández Cordero, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `class_loader <https://github.com/ros/class_loader/tree/humble/CHANGELOG.rst>`__

* Install includes to include/ ([#191 ](https://github.com/ros/class_loader/issues/191)_)
* Fix include order for cpplint ([#192 ](https://github.com/ros/class_loader/issues/192)_)
* Update maintainers to Geoffrey Biggs and Michael Carroll ([#190 ](https://github.com/ros/class_loader/issues/190)_)
* Fix spelling mistake ([#184 ](https://github.com/ros/class_loader/issues/184)_)
* Contributors: Audrow Nash, David V. Lu!!, Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `common_interfaces <https://github.com/ros2/common_interfaces/tree/humble/common_interfaces/CHANGELOG.rst>`__

* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `composition <https://github.com/ros2/demos/tree/humble/composition/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Additional fixes for documentation in demos. ([#538 ](https://github.com/ros2/demos/issues/538)_)
* Fixing deprecated subscriber callback warnings ([#532 ](https://github.com/ros2/demos/issues/532)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `composition_interfaces <https://github.com/ros2/rcl_interfaces/tree/humble/composition_interfaces/CHANGELOG.rst>`__

* Update maintainers to Chris Lalancette ([#130 ](https://github.com/ros2/rcl_interfaces/issues/130)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `demo_nodes_cpp <https://github.com/ros2/demos/tree/humble/demo_nodes_cpp/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Add how to fix the most vexing parse problem ([#541 ](https://github.com/ros2/demos/issues/541)_) * use uniform initialization
* Fixing deprecated subscriber callback warnings ([#532 ](https://github.com/ros2/demos/issues/532)_)
* Update talker_loaned_message.cpp ([#518 ](https://github.com/ros2/demos/issues/518)_)
* Revert "Use sizeof(char) in place for sizeof(void) ([#515 ](https://github.com/ros2/demos/issues/515)_)" ([#516 ](https://github.com/ros2/demos/issues/516)_)
* change how serialized message works with subscription ([#497 ](https://github.com/ros2/demos/issues/497)_)
* Use sizeof(char) in place for sizeof(void) ([#515 ](https://github.com/ros2/demos/issues/515)_)
* Fix small print issue in allocator tutorial. ([#509 ](https://github.com/ros2/demos/issues/509)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette, Michel Hidalgo, Tomoya Fujita, William Woodall, Zongbao Feng


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `demo_nodes_cpp_native <https://github.com/ros2/demos/tree/humble/demo_nodes_cpp_native/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Fix typo in demo_nodes_cpp_native package description ([#536 ](https://github.com/ros2/demos/issues/536)_)
* Contributors: Audrow Nash, Víctor Mayoral Vilches


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `demo_nodes_py <https://github.com/ros2/demos/tree/humble/demo_nodes_py/CHANGELOG.rst>`__

* Cleanups in demo_nodes_py. ([#555 ](https://github.com/ros2/demos/issues/555)_)
* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Fixed typo executor -> executors ([#542 ](https://github.com/ros2/demos/issues/542)_)
* Update python nodes SIGINT handling ([#539 ](https://github.com/ros2/demos/issues/539)_)
* Contributors: Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, ori155


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `diagnostic_msgs <https://github.com/ros2/common_interfaces/tree/humble/diagnostic_msgs/CHANGELOG.rst>`__

* Interface packages should fully <depend> on the interface packages that they depend on ([#173 ](https://github.com/ros2/common_interfaces/issues/173)_)
* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Contributors: Audrow Nash, Grey


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `domain_coordinator <https://github.com/ros2/ament_cmake_ros/tree/humble/domain_coordinator/CHANGELOG.rst>`__

* Update maintainers to Michel Hidalgo ([#13 ](https://github.com/ros2/ament_cmake_ros/issues/13)_)
* Refactor domain_coordinator API to use a context manager ([#12 ](https://github.com/ros2/ament_cmake_ros/issues/12)_)
* Contributors: Audrow Nash, Timo Röhling


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `dummy_map_server <https://github.com/ros2/demos/tree/humble/dummy_robot/dummy_map_server/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `dummy_robot_bringup <https://github.com/ros2/demos/tree/humble/dummy_robot/dummy_robot_bringup/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `dummy_sensors <https://github.com/ros2/demos/tree/humble/dummy_robot/dummy_sensors/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `example_interfaces <https://github.com/ros2/example_interfaces/tree/humble/CHANGELOG.rst>`__

* Update maintainers to Mabel Zhang ([#15 ](https://github.com/ros2/example_interfaces/issues/15)_)
* Add changelog ([#14 ](https://github.com/ros2/example_interfaces/issues/14)_)
* Contributors: Audrow Nash, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_async_client <https://github.com/ros2/examples/tree/humble/rclcpp/services/async_client/CHANGELOG.rst>`__

* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Add example of how to prune old requests in client API ([#322 ](https://github.com/ros2/examples/issues/322)_)
* Contributors: Aditya Pande, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_cbg_executor <https://github.com/ros2/examples/tree/humble/rclcpp/executors/cbg_executor/CHANGELOG.rst>`__

* Improve scheduling configuration of examples_rclcpp_cbg_executor package ([#331 ](https://github.com/ros2/examples/issues/331)_)
* Added jitter measurement to examples_rclcpp_cbg_executor. ([#328 ](https://github.com/ros2/examples/issues/328)_)
* Fix deprecated subscriber callbacks ([#323 ](https://github.com/ros2/examples/issues/323)_)
* Remove use of get_callback_groups(). ([#320 ](https://github.com/ros2/examples/issues/320)_)
* Contributors: Abrar Rahman Protyasha, Chris Lalancette, Ralph Lange


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_action_client <https://github.com/ros2/examples/tree/humble/rclcpp/actions/minimal_action_client/CHANGELOG.rst>`__

* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Contributors: Aditya Pande


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_action_server <https://github.com/ros2/examples/tree/humble/rclcpp/actions/minimal_action_server/CHANGELOG.rst>`__

* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Contributors: Aditya Pande


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_client <https://github.com/ros2/examples/tree/humble/rclcpp/services/minimal_client/CHANGELOG.rst>`__

* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Add example of how to prune old requests in client API ([#322 ](https://github.com/ros2/examples/issues/322)_)
* Contributors: Aditya Pande, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_composition <https://github.com/ros2/examples/tree/humble/rclcpp/composition/minimal_composition/CHANGELOG.rst>`__

* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Contributors: Aditya Pande


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_publisher <https://github.com/ros2/examples/tree/humble/rclcpp/topics/minimal_publisher/CHANGELOG.rst>`__

* Add an example about how to use wait_for_all_acked ([#316 ](https://github.com/ros2/examples/issues/316)_)
* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Add try&catch statement to unique network flow publisher example ([#313 ](https://github.com/ros2/examples/issues/313)_)
* Add type adaption example ([#300 ](https://github.com/ros2/examples/issues/300)_)
* Contributors: Aditya Pande, Audrow Nash, Barry Xu, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_service <https://github.com/ros2/examples/tree/humble/rclcpp/services/minimal_service/CHANGELOG.rst>`__

* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Contributors: Aditya Pande


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_subscriber <https://github.com/ros2/examples/tree/humble/rclcpp/topics/minimal_subscriber/CHANGELOG.rst>`__

* Use [`const&`` signature for read-only sub callbacks (`#337 ](https://github.com/ros2/examples/issues/337)_)
* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Fix deprecated subscriber callbacks ([#323 ](https://github.com/ros2/examples/issues/323)_)
* Add wait set examples ([#315 ](https://github.com/ros2/examples/issues/315)_)
* Add type adaption example ([#300 ](https://github.com/ros2/examples/issues/300)_)
* Contributors: Abrar Rahman Protyasha, Aditya Pande, Audrow Nash, carlossvg


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_minimal_timer <https://github.com/ros2/examples/tree/humble/rclcpp/timers/minimal_timer/CHANGELOG.rst>`__

* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Contributors: Aditya Pande


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_multithreaded_executor <https://github.com/ros2/examples/tree/humble/rclcpp/executors/multithreaded_executor/CHANGELOG.rst>`__

* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Fix deprecated subscriber callbacks ([#323 ](https://github.com/ros2/examples/issues/323)_)
* Contributors: Abrar Rahman Protyasha, Aditya Pande


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclcpp_wait_set <https://github.com/ros2/examples/tree/humble/rclcpp/wait_set/CHANGELOG.rst>`__

* Add wait set examples ([#315 ](https://github.com/ros2/examples/issues/315)_)
* Contributors: carlossvg


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_executors <https://github.com/ros2/examples/tree/humble/rclpy/executors/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Shane Loretz ([#332 ](https://github.com/ros2/examples/issues/332)_)
* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Update python nodes sigint/sigterm handling ([#330 ](https://github.com/ros2/examples/issues/330)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_guard_conditions <https://github.com/ros2/examples/tree/humble/rclpy/guard_conditions/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Shane Loretz ([#332 ](https://github.com/ros2/examples/issues/332)_)
* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Contributors: Aditya Pande, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_action_client <https://github.com/ros2/examples/tree/humble/rclpy/actions/minimal_action_client/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Shane Loretz ([#332 ](https://github.com/ros2/examples/issues/332)_)
* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Contributors: Aditya Pande, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_action_server <https://github.com/ros2/examples/tree/humble/rclpy/actions/minimal_action_server/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Shane Loretz ([#332 ](https://github.com/ros2/examples/issues/332)_)
* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Contributors: Aditya Pande, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_client <https://github.com/ros2/examples/tree/humble/rclpy/services/minimal_client/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Shane Loretz ([#332 ](https://github.com/ros2/examples/issues/332)_)
* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_) * Updated maintainers * Removed author
* Contributors: Aditya Pande, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_publisher <https://github.com/ros2/examples/tree/humble/rclpy/topics/minimal_publisher/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Shane Loretz ([#332 ](https://github.com/ros2/examples/issues/332)_)
* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Contributors: Aditya Pande, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_service <https://github.com/ros2/examples/tree/humble/rclpy/services/minimal_service/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Shane Loretz ([#332 ](https://github.com/ros2/examples/issues/332)_)
* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Contributors: Aditya Pande, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_minimal_subscriber <https://github.com/ros2/examples/tree/humble/rclpy/topics/minimal_subscriber/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Shane Loretz ([#332 ](https://github.com/ros2/examples/issues/332)_)
* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Contributors: Aditya Pande, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_rclpy_pointcloud_publisher <https://github.com/ros2/examples/tree/humble/rclpy/topics/pointcloud_publisher/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Shane Loretz ([#332 ](https://github.com/ros2/examples/issues/332)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `examples_tf2_py <https://github.com/ros2/geometry2/tree/humble/examples_tf2_py/CHANGELOG.rst>`__

* Update maintainers to Alejandro Hernandez Cordero and Chris Lalancette ([#481 ](https://github.com/ros2/geometry2/issues/481)_)
* Use underscores instead of dashes in setup.cfg. ([#403 ](https://github.com/ros2/geometry2/issues/403)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `fastrtps_cmake_module <https://github.com/ros2/rosidl_typesupport_fastrtps/tree/humble/fastrtps_cmake_module/CHANGELOG.rst>`__

* Update maintainers to Shane Loretz ([#83 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/83)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `geometry_msgs <https://github.com/ros2/common_interfaces/tree/humble/geometry_msgs/CHANGELOG.rst>`__

* Interface packages should fully <depend> on the interface packages that they depend on ([#173 ](https://github.com/ros2/common_interfaces/issues/173)_)
* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Contributors: Audrow Nash, Grey


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `google_benchmark_vendor <https://github.com/ament/google_benchmark_vendor/tree/humble/CHANGELOG.rst>`__

* Add git buildtool dependency.
* Use git hash for google_benchmark_vendor ([#20 ](https://github.com/ament/google_benchmark_vendor/issues/20)_)
* Update to google benchmark version 1.6.1 ([#19 ](https://github.com/ament/google_benchmark_vendor/issues/19)_)
* Update maintainers to Audrow Nash ([#18 ](https://github.com/ament/google_benchmark_vendor/issues/18)_)
* Update google_benchmark to v1.5.3 ([#16 ](https://github.com/ament/google_benchmark_vendor/issues/16)_) 1. Change google_benchmark version from v1.5.2 to v1.5.3. Because v1.5.2 can not build with GCC 11 2. Removed shrink-tz-offset-size.patch because of this patch was merged in google-benchmark repo.
* Add changelog ([#15 ](https://github.com/ament/google_benchmark_vendor/issues/15)_)
* Shrink the size of the tz_offset variable. ([#13 ](https://github.com/ament/google_benchmark_vendor/issues/13)_)
* Update the patching to work on Windows without admin. ([#11 ](https://github.com/ament/google_benchmark_vendor/issues/11)_)
* Always preserve source permissions in vendor packages. ([#12 ](https://github.com/ament/google_benchmark_vendor/issues/12)_)
* Update package maintainers. ([#10 ](https://github.com/ament/google_benchmark_vendor/issues/10)_)
* Upgrade google benchmark from v1.5.1 to v1.5.2 to include QNX patch. ([#9 ](https://github.com/ament/google_benchmark_vendor/issues/9)_)
* Set the SOVERSION on benchmark libraries. ([#8 ](https://github.com/ament/google_benchmark_vendor/issues/8)_)
* Set minimum criteria for system package. ([#3 ](https://github.com/ament/google_benchmark_vendor/issues/3)_)
* Work around warnings building Google Benchmark w/Clang. ([#2 ](https://github.com/ament/google_benchmark_vendor/issues/2)_)
* Initial google_benchmark_vendor package. ([#1 ](https://github.com/ament/google_benchmark_vendor/issues/1)_)
* Initial commit.
* Contributors: Ahmed Sobhy, Audrow Nash, Chris Lalancette, Homalozoa X, Ivan Santiago Paunovic, Michel Hidalgo, Scott K Logan, Shane Loretz, Steven! Ragnarök


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `image_tools <https://github.com/ros2/demos/tree/humble/image_tools/CHANGELOG.rst>`__

* Install includes to include/${PROJECT_NAME} ([#548 ](https://github.com/ros2/demos/issues/548)_)
* Fix include order and relative paths for cpplint ([#551 ](https://github.com/ros2/demos/issues/551)_)
* Reduce the number of OpenCV libraries image_tools links against. ([#549 ](https://github.com/ros2/demos/issues/549)_)
* Adds copy constructor and assignment operator to ROSCvMatContainer ([#546 ](https://github.com/ros2/demos/issues/546)_)
* Fixes for uncrustify 0.72 ([#545 ](https://github.com/ros2/demos/issues/545)_)
* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Additional fixes for documentation in demos. ([#538 ](https://github.com/ros2/demos/issues/538)_)
* Fixing deprecated subscriber callback warnings ([#532 ](https://github.com/ros2/demos/issues/532)_)
* ambigulity: unknown type name 'nullptr_t' ([#528 ](https://github.com/ros2/demos/issues/528)_)
* Add type masquerading demos ([#482 ](https://github.com/ros2/demos/issues/482)_)
* Add support for visualizing yuv422 ([#499 ](https://github.com/ros2/demos/issues/499)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette, Gonzo, Jacob Perron, Shane Loretz, William Woodall, joshua-qnx, xwnb


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `image_transport <https://github.com/ros-perception/image_common/tree/humble/image_transport/CHANGELOG.rst>`__

* Image transport publisher crash fixes ([#235 ](https://github.com/ros-perception/image_common/issues/235)_)
* Simple IT plugins shutdown ([#225 ](https://github.com/ros-perception/image_common/issues/225)_)
* Remove PLUGINLIB__DISABLE_BOOST_FUNCTIONS definition. ([#226 ](https://github.com/ros-perception/image_common/issues/226)_)
* Fix include order for cpplint ([#221 ](https://github.com/ros-perception/image_common/issues/221)_) Relates to https://github.com/ament/ament_lint/pull/324
* Export a modern CMake target instead of variables and install includes to include/${PROJECT_NAME} ([#218 ](https://github.com/ros-perception/image_common/issues/218)_)
* Fix SimpleSubscriberPlugin ([#195 ](https://github.com/ros-perception/image_common/issues/195)_)
* Make sure to mark overridden methods as 'override'. ([#192 ](https://github.com/ros-perception/image_common/issues/192)_)
* Expose subscription options ([#186 ](https://github.com/ros-perception/image_common/issues/186)_)
* fix mistyping 'cammera_publisher.hpp -> camera_publisher.hpp' ([#177 ](https://github.com/ros-perception/image_common/issues/177)_)
* Update maintainers ([#173 ](https://github.com/ros-perception/image_common/issues/173)_)
* make CameraPublisher::getNumSubscribers() work ([#163 ](https://github.com/ros-perception/image_common/issues/163)_)
* Contributors: Alejandro Hernández Cordero, Audrow Nash, Chris Lalancette, Hye-Jong KIM, Ivan Santiago Paunovic, Jacob Perron, Michael Ferguson, RoboTech Vision, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `interactive_markers <https://github.com/ros-visualization/interactive_markers/tree/humble/CHANGELOG.rst>`__

* Do not publish if context is invalid during shutdown ([#89 ](https://github.com/ros-visualization/interactive_markers/issues/89)_)
* Install includes to include/ and misc CMake fixes ([#85 ](https://github.com/ros-visualization/interactive_markers/issues/85)_)
* Fix deprecation warning introduced after client API update ([#83 ](https://github.com/ros-visualization/interactive_markers/issues/83)_)
* Fix deprecated sub callback warnings ([#84 ](https://github.com/ros-visualization/interactive_markers/issues/84)_)
* Include tf2_geometry_msgs.hpp instead of the h file. ([#82 ](https://github.com/ros-visualization/interactive_markers/issues/82)_)
* Contributors: Abrar Rahman Protyasha, Chris Lalancette, Ivan Santiago Paunovic, Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `intra_process_demo <https://github.com/ros2/demos/tree/humble/intra_process_demo/CHANGELOG.rst>`__

* Add opencv_imgproc dependency for cv::putText ([#554 ](https://github.com/ros2/demos/issues/554)_)
* Install includes to include/${PROJECT_NAME} ([#548 ](https://github.com/ros2/demos/issues/548)_)
* Fix include order and relative paths for cpplint ([#551 ](https://github.com/ros2/demos/issues/551)_)
* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Additional fixes for documentation in demos. ([#538 ](https://github.com/ros2/demos/issues/538)_)
* Fixing deprecated subscriber callback warnings ([#532 ](https://github.com/ros2/demos/issues/532)_)
* Revert "Add type masquerading demos ([#482 ](https://github.com/ros2/demos/issues/482)_)" ([#520 ](https://github.com/ros2/demos/issues/520)_)
* Add type masquerading demos ([#482 ](https://github.com/ros2/demos/issues/482)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette, Jacob Perron, Shane Loretz, William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `kdl_parser <https://github.com/ros/kdl_parser/tree/humble/kdl_parser/CHANGELOG.rst>`__

* Depend on orocos-kdl vendor packages  ([#58 ](https://github.com/ros/kdl_parser/issues/58)_)
* Install includes to include/ and misc CMake fixes ([#61 ](https://github.com/ros/kdl_parser/issues/61)_)
* Update to uncrustify 0.72 ([#60 ](https://github.com/ros/kdl_parser/issues/60)_)
* Contributors: Chris Lalancette, Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `laser_geometry <https://github.com/ros-perception/laser_geometry/tree/humble/CHANGELOG.rst>`__

* Install headers to include/${PROJECT_NAME} ([#86 ](https://github.com/ros-perception/laser_geometry/issues/86)_)
* Explicit cast to double to prevent loss of precision
* Fix Duration casting issue leading to no undistortion
* Fix building on running on Windows Debug ([#82 ](https://github.com/ros-perception/laser_geometry/issues/82)_)
* Update python code and tests for ros2 ([#80 ](https://github.com/ros-perception/laser_geometry/issues/80)_)
* Contributors: Chris Lalancette, Jonathan Binney, Marco Lampacrescia, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch <https://github.com/ros2/launch/tree/humble/launch/CHANGELOG.rst>`__

* Sandbox environment in tests to fix repeated job failures ([#609 ](https://github.com/ros2/launch/issues/609)_)
* Start Python faster in test_execute_processs_shutdown to avoid flakey failures ([#608 ](https://github.com/ros2/launch/issues/608)_)
* Fix warnings from importlib_metdata on Python 3.10. ([#606 ](https://github.com/ros2/launch/issues/606)_)
* Add boolean substitutions ([#598 ](https://github.com/ros2/launch/issues/598)_)
* Support scoping environment variables ([#601 ](https://github.com/ros2/launch/issues/601)_)
* Fix awaiting shutdown in launch context ([#603 ](https://github.com/ros2/launch/issues/603)_)
* Fix parse respawn var ([#569 ](https://github.com/ros2/launch/issues/569)_)
* Make the logged command pretty in ExecuteLocal ([#594 ](https://github.com/ros2/launch/issues/594)_)
* 'output' is expanded as a substitution in XML/YAML files ([#577 ](https://github.com/ros2/launch/issues/577)_)
* Skip warning test if warning already happend ([#585 ](https://github.com/ros2/launch/issues/585)_)
* Use asyncio.wait with timeout rather than sleep ([#576 ](https://github.com/ros2/launch/issues/576)_)
* Make test_parser compatible with Python older than 3.8 ([#575 ](https://github.com/ros2/launch/issues/575)_)
* Propagate exceptions of completed actions to launch service main loop ([#566 ](https://github.com/ros2/launch/issues/566)_)
* Warn when loading launch extensions fails ([#572 ](https://github.com/ros2/launch/issues/572)_)
* Add in two fixes for Jammy ([#571 ](https://github.com/ros2/launch/issues/571)_)
* Evaluate math symbols and functions in python expression ([#557 ](https://github.com/ros2/launch/issues/557)_)
* Document TimerAction params ([#558 ](https://github.com/ros2/launch/issues/558)_)
* Improve launch arguments introspection ([#556 ](https://github.com/ros2/launch/issues/556)_)
* Update maintainers to Aditya Pande and Michel Hidalgo ([#559 ](https://github.com/ros2/launch/issues/559)_)
* Updated maintainers ([#555 ](https://github.com/ros2/launch/issues/555)_)
* First prototype of native pytest plugin for launch based tests ([#528 ](https://github.com/ros2/launch/issues/528)_)
* Allow for raw path specification in IncludeLaunchDescription ([#544 ](https://github.com/ros2/launch/issues/544)_)
* Adding Executable description class ([#454 ](https://github.com/ros2/launch/issues/454)_)
* event handlers: Allow to match the target action with a callable and not only with an object instance ([#540 ](https://github.com/ros2/launch/issues/540)_)
* Add AppendEnvironmentVariable action ([#543 ](https://github.com/ros2/launch/issues/543)_)
* Document EnvironmentVariable substitution resolution context caveat ([#541 ](https://github.com/ros2/launch/issues/541)_)
* Feature clear launch configs ([#515 ](https://github.com/ros2/launch/issues/515)_)
* Add examples to ExecuteProcess docs ([#525 ](https://github.com/ros2/launch/issues/525)_)
* Fix [`DeclareLaunchArgument`` xml parsing and constructor (`#529 ](https://github.com/ros2/launch/issues/529)_)
* Fix pytest run on Windows ([#526 ](https://github.com/ros2/launch/issues/526)_)
* Improving docs ([#523 ](https://github.com/ros2/launch/issues/523)_)
* Add filtering mechanism for executable prefix application ([#522 ](https://github.com/ros2/launch/issues/522)_)
* Make each parser extension provide a set of file extensions ([#516 ](https://github.com/ros2/launch/issues/516)_)
* Add missing exec dependency on PyYAML ([#493 ](https://github.com/ros2/launch/issues/493)_)
* Refactor TimerAction to allow RosTimer to extend ([#512 ](https://github.com/ros2/launch/issues/512)_)
* Improve (Not)Equals condition type hinting ([#510 ](https://github.com/ros2/launch/issues/510)_)
* Contributors: Aditya Pande, Audrow Nash, Cameron Miller, Chris Lalancette, Christophe Bedard, David V. Lu!!, Derek Chopp, HMellor, Immanuel Martini, Ivan Santiago Paunovic, Jacob Perron, Kenji Miyake, Khush Jain, Kosuke Takeuchi, Rebecca Butler, Scott K Logan, Shane Loretz, roger-strain, tumtom


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_pytest <https://github.com/ros2/launch/tree/humble/launch_pytest/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Michel Hidalgo ([#559 ](https://github.com/ros2/launch/issues/559)_)
* [launch_pytest] Modify how wait_for_output()/wait_for_stderr() work, add assert\_*() alternatives ([#553 ](https://github.com/ros2/launch/issues/553)_)
* Updated maintainers ([#555 ](https://github.com/ros2/launch/issues/555)_)
* * [launch_pytest] Fix issue when colcon --retest-until-fail flag is used ([#552 ](https://github.com/ros2/launch/issues/552)_)
* First prototype of native pytest plugin for launch based tests ([#528 ](https://github.com/ros2/launch/issues/528)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_ros <https://github.com/ros2/launch_ros/tree/humble/launch_ros/CHANGELOG.rst>`__

* Fix importlib_metadata warning on Python 3.10. ([#307 ](https://github.com/ros2/launch_ros/issues/307)_)
* Use correct namespace when evaluating parameter files for composable nodes ([#303 ](https://github.com/ros2/launch_ros/issues/303)_)
* Handle empty strings when evaluating parameters ([#300 ](https://github.com/ros2/launch_ros/issues/300)_)
* Add parameter substitution ([#297 ](https://github.com/ros2/launch_ros/issues/297)_)
* fix bug in warning when an entry point fails to load ([#243 ](https://github.com/ros2/launch_ros/issues/243)_)
* More Helpful Error Messages ([#275 ](https://github.com/ros2/launch_ros/issues/275)_)
* Update maintainers in setup.py ([#287 ](https://github.com/ros2/launch_ros/issues/287)_)
* Set parameters from file for composable nodes ([#281 ](https://github.com/ros2/launch_ros/issues/281)_)
* Update package maintainers ([#284 ](https://github.com/ros2/launch_ros/issues/284)_)
* Update node name matcher ([#282 ](https://github.com/ros2/launch_ros/issues/282)_)
* Support both parameter file configurations for composable nodes ([#259 ](https://github.com/ros2/launch_ros/issues/259)_)
* Handle substitutions in RosTimer ([#264 ](https://github.com/ros2/launch_ros/issues/264)_)
* Add SetParametersFromFile action ([#260 ](https://github.com/ros2/launch_ros/issues/260)_)
* Properly support ros_args attribute through launch frontends ([#253 ](https://github.com/ros2/launch_ros/issues/253)_)
* Add 'push_ros_namespace' alias to 'push-ros-namespace' ([#250 ](https://github.com/ros2/launch_ros/issues/250)_)
* Add ros_arguments option to Node action ([#249 ](https://github.com/ros2/launch_ros/issues/249)_)
* Refactor RosTimer to extend TimerAction ([#248 ](https://github.com/ros2/launch_ros/issues/248)_)
* ROS Timer Action ([#244 ](https://github.com/ros2/launch_ros/issues/244)_)
* Support container in frontend ([#235 ](https://github.com/ros2/launch_ros/issues/235)_)
* Fix a small typo in a comment ([#237 ](https://github.com/ros2/launch_ros/issues/237)_)
* Better document parameter handling in Node ([#234 ](https://github.com/ros2/launch_ros/issues/234)_)
* Make 'ros2 launch' work again. ([launch #201 ](https://github.com/ros2/launch_ros/issues/201)_)
* Added LaunchLogger class ([launch #145 ](https://github.com/ros2/launch/issues/145)_)
* Changed logger.warn (deprecated) to logger.warning. ([launch #199 ](https://github.com/ros2/launch/issues/199)_)
* Added Plumb rclpy.init context to get_default_launch_description. ([launch #193 ](https://github.com/ros2/launch/issues/193)_)
* Added normalize_parameters and evaluate_paramters. ([launch #192 ](https://github.com/ros2/launch/issues/192)_)
* Added normalize_remap_rule and types. ([launch #173 ](https://github.com/ros2/launch/issues/173)_)
* Renamed transitions to match changes in [`lifecycle_msgs`` (`launch #153 ](https://github.com/ros2/launch/issues/153)_)
* Added support for passing parameters as a dictionary to a Node ([launch #138 ](https://github.com/ros2/launch/issues/138)_)
* Made various fixes and added tests for remappings passed to Node actions ([launch #137 ](https://github.com/ros2/launch/issues/137)_)
* Contributors: Aditya Pande, Audrow Nash, Chris Lalancette, Christophe Bedard, David V. Lu!!, Felix Divo, Jacob Perron, Kenji Miyake, Michel Hidalgo, Rebecca Butler, William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing <https://github.com/ros2/launch/tree/humble/launch_testing/CHANGELOG.rst>`__

* Removed the deprecated [`ready_fn`` feature (`#589 ](https://github.com/ros2/launch/issues/589)_)
* Added case for instances of ExecuteLocal in resolveProcess function ([#587 ](https://github.com/ros2/launch/issues/587)_)
* Add compatitibility with pytest 7 ([#592 ](https://github.com/ros2/launch/issues/592)_)
* Renamed three files from example_processes ([#573 ](https://github.com/ros2/launch/issues/573)_)
* Fix launch_testing README.md proc keyword to process. ([#554 ](https://github.com/ros2/launch/issues/554)_) ([#560 ](https://github.com/ros2/launch/issues/560)_)
* Declare frontend group dependency & use explicit dependencies in launch_testing ([#520 ](https://github.com/ros2/launch/issues/520)_)
* Update maintainers to Aditya Pande and Michel Hidalgo ([#559 ](https://github.com/ros2/launch/issues/559)_)
* Updated maintainers ([#555 ](https://github.com/ros2/launch/issues/555)_)
* First prototype of native pytest plugin for launch based tests ([#528 ](https://github.com/ros2/launch/issues/528)_)
* Adding Executable description class ([#454 ](https://github.com/ros2/launch/issues/454)_)
* Add a "hello world" style example ([#532 ](https://github.com/ros2/launch/issues/532)_)
* Contributors: Aditya Pande, Audrow Nash, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Khush Jain, Matt Lanting, Shane Loretz, William Woodall, roger-strain


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing_ament_cmake <https://github.com/ros2/launch/tree/humble/launch_testing_ament_cmake/CHANGELOG.rst>`__

* [launch_testing_ament_cmake] Add test label ([#584 ](https://github.com/ros2/launch/issues/584)_)
* Update maintainers to Aditya Pande and Michel Hidalgo ([#559 ](https://github.com/ros2/launch/issues/559)_)
* Updated maintainers ([#555 ](https://github.com/ros2/launch/issues/555)_)
* Contributors: Aditya Pande, Audrow Nash, Keisuke Shima


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing_examples <https://github.com/ros2/examples/tree/humble/launch_testing/launch_testing_examples/CHANGELOG.rst>`__

* Readded WaitForTopics utility ([#333 ](https://github.com/ros2/examples/issues/333)_)
* Final batch of examples ([#327 ](https://github.com/ros2/examples/issues/327)_)
* Update maintainers to Aditya Pande and Shane Loretz ([#332 ](https://github.com/ros2/examples/issues/332)_)
* Updated maintainers ([#329 ](https://github.com/ros2/examples/issues/329)_)
* Reverted WaitForTopics utility usage ([#326 ](https://github.com/ros2/examples/issues/326)_)
* Moved examples ([#324 ](https://github.com/ros2/examples/issues/324)_)
* Contributors: Aditya Pande, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_testing_ros <https://github.com/ros2/launch_ros/tree/humble/launch_testing_ros/CHANGELOG.rst>`__

* Add [`hz`` param to ``talker.py`` to fix wait_for_topic_launch_test (`#309 ](https://github.com/ros2/launch_ros/issues/309)_)
* Revert WaitForTopics ([#288 ](https://github.com/ros2/launch_ros/issues/288)_)
* Update maintainers in setup.py ([#287 ](https://github.com/ros2/launch_ros/issues/287)_)
* Move pytest entrypoints to own module ([#278 ](https://github.com/ros2/launch_ros/issues/278)_)
* Update package maintainers ([#284 ](https://github.com/ros2/launch_ros/issues/284)_)
* Check that future is done, and always call rclpy.shutdown ([#273 ](https://github.com/ros2/launch_ros/issues/273)_)
* Revert "launch testing : Wait for topics to publish ([#274 ](https://github.com/ros2/launch_ros/issues/274)_)" ([#276 ](https://github.com/ros2/launch_ros/issues/276)_)
* Add WaitForTopics utility for waiting on publishers ([#274 ](https://github.com/ros2/launch_ros/issues/274)_)
* Remove unused code, Future.result() already raises ([#270 ](https://github.com/ros2/launch_ros/issues/270)_)
* Add timeout to wait for service response in example ([#271 ](https://github.com/ros2/launch_ros/issues/271)_)
* Add examples ([#263 ](https://github.com/ros2/launch_ros/issues/263)_)
* Contributors: Aditya Pande, Audrow Nash, Jacob Perron, Jorge Perez, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_xml <https://github.com/ros2/launch/tree/humble/launch_xml/CHANGELOG.rst>`__

* Fix sphinx directive to cross-ref Launch method ([#605 ](https://github.com/ros2/launch/issues/605)_)
* Add boolean substitutions ([#598 ](https://github.com/ros2/launch/issues/598)_)
* Support scoping environment variables ([#601 ](https://github.com/ros2/launch/issues/601)_)
* 'output' is expanded as a substitution in XML/YAML files ([#577 ](https://github.com/ros2/launch/issues/577)_)
* Declare frontend group dependency & use explicit dependencies in launch_testing ([#520 ](https://github.com/ros2/launch/issues/520)_)
* Update maintainers to Aditya Pande and Michel Hidalgo ([#559 ](https://github.com/ros2/launch/issues/559)_)
* Updated maintainers ([#555 ](https://github.com/ros2/launch/issues/555)_)
* Add AppendEnvironmentVariable action ([#543 ](https://github.com/ros2/launch/issues/543)_)
* Feature clear launch configs ([#515 ](https://github.com/ros2/launch/issues/515)_)
* Fix [`DeclareLaunchArgument`` xml parsing and constructor (`#529 ](https://github.com/ros2/launch/issues/529)_)
* Add 'launch' to sets of launch file extensions ([#518 ](https://github.com/ros2/launch/issues/518)_)
* Make each parser extension provide a set of file extensions ([#516 ](https://github.com/ros2/launch/issues/516)_)
* Contributors: Abrar Rahman Protyasha, Aditya Pande, Audrow Nash, Christophe Bedard, Derek Chopp, Ivan Santiago Paunovic, Jacob Perron, Kenji Miyake, Khush Jain


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `launch_yaml <https://github.com/ros2/launch/tree/humble/launch_yaml/CHANGELOG.rst>`__

* Fix sphinx directive to cross-ref Launch method ([#605 ](https://github.com/ros2/launch/issues/605)_)
* Add boolean substitutions ([#598 ](https://github.com/ros2/launch/issues/598)_)
* Support scoping environment variables ([#601 ](https://github.com/ros2/launch/issues/601)_)
* 'output' is expanded as a substitution in XML/YAML files ([#577 ](https://github.com/ros2/launch/issues/577)_)
* Declare frontend group dependency & use explicit dependencies in launch_testing ([#520 ](https://github.com/ros2/launch/issues/520)_)
* Update maintainers to Aditya Pande and Michel Hidalgo ([#559 ](https://github.com/ros2/launch/issues/559)_)
* Updated maintainers ([#555 ](https://github.com/ros2/launch/issues/555)_)
* Add AppendEnvironmentVariable action ([#543 ](https://github.com/ros2/launch/issues/543)_)
* Feature clear launch configs ([#515 ](https://github.com/ros2/launch/issues/515)_)
* Add 'launch' to sets of launch file extensions ([#518 ](https://github.com/ros2/launch/issues/518)_)
* Make each parser extension provide a set of file extensions ([#516 ](https://github.com/ros2/launch/issues/516)_)
* Contributors: Abrar Rahman Protyasha, Aditya Pande, Audrow Nash, Christophe Bedard, Derek Chopp, Jacob Perron, Kenji Miyake, Khush Jain


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `libcurl_vendor <https://github.com/ros/resource_retriever/tree/humble/libcurl_vendor/CHANGELOG.rst>`__

* Update to curl 7.81. ([#74 ](https://github.com/ros/resource_retriever/issues/74)_)
* Update maintainers ([#66 ](https://github.com/ros/resource_retriever/issues/66)_)
* Contributors: Audrow Nash, Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `libstatistics_collector <https://github.com/ros-tooling/libstatistics_collector/tree/humble/CHANGELOG.rst>`__

* Bump pascalgn/automerge-action from 0.14.3 to 0.15.2
* Bump ros-tooling/setup-ros from 0.2.2 to 0.3.0
* Bump actions/upload-artifact from 2.3.1 to 3
* Bump actions/upload-artifact from 2.2.4 to 2.3.1
* Bump actions/checkout from 2 to 3
* Bump ros-tooling/setup-ros from 0.2.1 to 0.2.2 ([#123 ](https://github.com/ros-tooling/libstatistics_collector/issues/123)_)
* Install includes to include/${PROJECT_NAME} ([#122 ](https://github.com/ros-tooling/libstatistics_collector/issues/122)_)
* Bump codecov/codecov-action from 2.0.3 to 2.1.0
* Bump pascalgn/automerge-action from 0.14.2 to 0.14.3
* Bump codecov/codecov-action from 2.0.2 to 2.0.3
* Use rosidl_get_typesupport_target() ([#116 ](https://github.com/ros-tooling/libstatistics_collector/issues/116)_)
* Bump codecov/codecov-action from 2.0.1 to 2.0.2
* Bump codecov/codecov-action from 1.5.2 to 2.0.1
* Bump actions/upload-artifact from 1 to 2.2.4
* Bump codecov/codecov-action from 1.5.1 to 1.5.2
* Bump codecov/codecov-action from 1.3.1 to 1.5.1
* Bump ros-tooling/setup-ros from 0.2.0 to 0.2.1
* Bump pascalgn/automerge-action from 0.14.1 to 0.14.2
* Bump ros-tooling/setup-ros from 0.1 to 0.2.0
* Bump pascalgn/automerge-action from 0.13.1 to 0.14.1
* Fix autoapprove
* Package.json explicitly owned by emerson to minimize notifications
* Bump hmarr/auto-approve-action from v2.0.0 to v2.1.0
* Bump codecov/codecov-action from v1.2.1 to v1.3.1
* Contributors: Chris Lalancette, Emerson Knapp, Shane Loretz, dependabot[bot]


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `libyaml_vendor <https://github.com/ros2/libyaml_vendor/tree/humble/CHANGELOG.rst>`__

* Add a buildtool dependency on git. ([#48 ](https://github.com/ros2/libyaml_vendor/issues/48)_)
* Install headers to include/${PROJECT_NAME} ([#46 ](https://github.com/ros2/libyaml_vendor/issues/46)_)
* Merge pull request [#43 ](https://github.com/ros2/libyaml_vendor/issues/43)_ from ros2/update-maintainers
* Update maintainers to Audrow Nash
* Contributors: Audrow Nash, Shane Loretz, Steven! Ragnarök


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `lifecycle <https://github.com/ros2/demos/tree/humble/lifecycle/CHANGELOG.rst>`__

* Make lifecycle demo automatically exit when done ([#558 ](https://github.com/ros2/demos/issues/558)_)
* Use default on_activate()/on_deactivate() implemenetation of Node ([#552 ](https://github.com/ros2/demos/issues/552)_)
* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Fix use of future in lifecycle demo ([#534 ](https://github.com/ros2/demos/issues/534)_)
* Fixing deprecated subscriber callback warnings ([#532 ](https://github.com/ros2/demos/issues/532)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Christophe Bedard, Ivan Santiago Paunovic, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `lifecycle_msgs <https://github.com/ros2/rcl_interfaces/tree/humble/lifecycle_msgs/CHANGELOG.rst>`__

* Update maintainers to Chris Lalancette ([#130 ](https://github.com/ros2/rcl_interfaces/issues/130)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `lifecycle_py <https://github.com/ros2/demos/tree/humble/lifecycle_py/CHANGELOG.rst>`__

* Create changelog for lifecycle_py
* Add rclpy lifecycle demo ([#547 ](https://github.com/ros2/demos/issues/547)_)
* Contributors: Audrow Nash, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `logging_demo <https://github.com/ros2/demos/tree/humble/logging_demo/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Additional fixes for documentation in demos. ([#538 ](https://github.com/ros2/demos/issues/538)_)
* Use rosidl_get_typesupport_target() ([#529 ](https://github.com/ros2/demos/issues/529)_)
* Contributors: Audrow Nash, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `message_filters <https://github.com/ros2/message_filters/tree/humble/CHANGELOG.rst>`__

* Use RCL_ROS_TIME for message_traits::TimeStamp  ([#72 ](https://github.com/ros2/message_filters/issues/72)_)
* Install includes to include/${PROJECT_NAME} ([#71 ](https://github.com/ros2/message_filters/issues/71)_)
* Update maintainers ([#67 ](https://github.com/ros2/message_filters/issues/67)_)
* Suppress rclcpp deprecation warnings in unit tests ([#62 ](https://github.com/ros2/message_filters/issues/62)_)
* Add missing overrides to subscriber.h ([#60 ](https://github.com/ros2/message_filters/issues/60)_)
* Add lifecycle node support ([#59 ](https://github.com/ros2/message_filters/issues/59)_)
* Correct package.xml and CMakeLists.txt ([#58 ](https://github.com/ros2/message_filters/issues/58)_)
* Expose Subscription Options - V2 ([#56 ](https://github.com/ros2/message_filters/issues/56)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Hunter L. Allen, Kenji Brameld, Michel Hidalgo, Rebecca Butler, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `mimick_vendor <https://github.com/ros2/mimick_vendor/tree/humble/CHANGELOG.rst>`__

* support pi zero ([#24 ](https://github.com/ros2/mimick_vendor/issues/24)_)
* Update maintainers to Geoffrey Biggs ([#23 ](https://github.com/ros2/mimick_vendor/issues/23)_)
* Update to latest commit for Apple M1 support ([#20 ](https://github.com/ros2/mimick_vendor/issues/20)_)
* Contributors: Audrow Nash, Brett Downing, Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `nav_msgs <https://github.com/ros2/common_interfaces/tree/humble/nav_msgs/CHANGELOG.rst>`__

* Interface packages should fully <depend> on the interface packages that they depend on ([#173 ](https://github.com/ros2/common_interfaces/issues/173)_)
* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Contributors: Audrow Nash, Grey


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `pendulum_control <https://github.com/ros2/demos/tree/humble/pendulum_control/CHANGELOG.rst>`__

* Fix include order and relative paths for cpplint ([#551 ](https://github.com/ros2/demos/issues/551)_)
* Remove the malloc_hook from the pendulum_demo. ([#544 ](https://github.com/ros2/demos/issues/544)_)
* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Additional fixes for documentation in demos. ([#538 ](https://github.com/ros2/demos/issues/538)_)
* Fix documentation for pendulum_control. ([#537 ](https://github.com/ros2/demos/issues/537)_)
* Contributors: Audrow Nash, Chris Lalancette, Jacob Perron


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `pendulum_msgs <https://github.com/ros2/demos/tree/humble/pendulum_msgs/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `pluginlib <https://github.com/ros/pluginlib/tree/humble/pluginlib/CHANGELOG.rst>`__

* Install includes to include/${PROJECT_NAME} and remove ament_target_dependencies calls ([#226 ](https://github.com/ros/pluginlib/issues/226)_)
* Require <memory> ([#225 ](https://github.com/ros/pluginlib/issues/225)_)
* Move LibraryLoadExceptions down a level for more accurate error messages ([#221 ](https://github.com/ros/pluginlib/issues/221)_)
* Update maintainers to Chris Lalancette ([#223 ](https://github.com/ros/pluginlib/issues/223)_)
* extend termination condition to avoid infinite loop if package.xml is not found ([#220 ](https://github.com/ros/pluginlib/issues/220)_)
* Remove deprecated headers. ([#217 ](https://github.com/ros/pluginlib/issues/217)_)
* Contributors: Alberto Soragna, Audrow Nash, Chris Lalancette, David V. Lu!!, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `pybind11_vendor <https://github.com/ros2/pybind11_vendor/tree/humble/CHANGELOG.rst>`__

* Use sha256 hash instead of tag ([#12 ](https://github.com/ros2/pybind11_vendor/issues/12)_)
* Install headers to include/${PROJECT_NAME} ([#11 ](https://github.com/ros2/pybind11_vendor/issues/11)_)
* Update pybind11 to 2.7.1. ([#10 ](https://github.com/ros2/pybind11_vendor/issues/10)_) This is the version that is shipped in Ubuntu 22.04.
* Contributors: Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `python_cmake_module <https://github.com/ros2/python_cmake_module/tree/humble/CHANGELOG.rst>`__

* require Python 3.6 as we use format strings in various places ([#10 ](https://github.com/ros2/python_cmake_module/issues/10)_)
* Document all variables set by this module ([#5 ](https://github.com/ros2/python_cmake_module/issues/5)_)
* Add changelog ([#4 ](https://github.com/ros2/python_cmake_module/issues/4)_)
* Contributors: Ivan Santiago Paunovic, Shane Loretz, William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `qt_gui_cpp <https://github.com/ros-visualization/qt_gui_core/tree/humble-devel/qt_gui_cpp/CHANGELOG.rst>`__

* Install headers to include${PROJECT_NAME} ([#259 ](https://github.com/ros-visualization/qt_gui_core/issues/259)_)
* Export targets instead of old-style CMake variables ([#257 ](https://github.com/ros-visualization/qt_gui_core/issues/257)_)
* FindPython3 explicitly instead of FindPythonInterp implicitly ([#254 ](https://github.com/ros-visualization/qt_gui_core/issues/254)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `quality_of_service_demo_cpp <https://github.com/ros2/demos/tree/humble/quality_of_service_demo/rclcpp/CHANGELOG.rst>`__

* Install includes to include/${PROJECT_NAME} ([#548 ](https://github.com/ros2/demos/issues/548)_)
* Fix include order and relative paths for cpplint ([#551 ](https://github.com/ros2/demos/issues/551)_)
* Fixes for uncrustify 0.72 ([#545 ](https://github.com/ros2/demos/issues/545)_)
* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Additional fixes for documentation in demos. ([#538 ](https://github.com/ros2/demos/issues/538)_)
* Fixing deprecated subscriber callback warnings ([#532 ](https://github.com/ros2/demos/issues/532)_)
* Initialize message correctly ([#522 ](https://github.com/ros2/demos/issues/522)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `quality_of_service_demo_py <https://github.com/ros2/demos/tree/humble/quality_of_service_demo/rclpy/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Update python nodes SIGINT handling ([#539 ](https://github.com/ros2/demos/issues/539)_)
* Contributors: Audrow Nash, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl <https://github.com/ros2/rcl/tree/humble/rcl/CHANGELOG.rst>`__

* add content-filtered-topic interfaces ([#894 ](https://github.com/ros2/rcl/issues/894)_)
* Add additional null check for timer argument ([#973 ](https://github.com/ros2/rcl/issues/973)_)
* Allow forward slashes within a parameter name rule in argument parsing ([#860 ](https://github.com/ros2/rcl/issues/860)_)
* Suppress false positive from clang-tidy ([#951 ](https://github.com/ros2/rcl/issues/951)_)
* Fix missing terminating \0 in rcl_context_impl_t.argv ([#969 ](https://github.com/ros2/rcl/issues/969)_)
* test_publisher_wait_all_ack depends on rcpputils ([#968 ](https://github.com/ros2/rcl/issues/968)_)
* Micro-optimizations in rcl ([#965 ](https://github.com/ros2/rcl/issues/965)_)
* If timer canceled, rcl_timer_get_time_until_next_call returns TIMER_CANCELED ([#963 ](https://github.com/ros2/rcl/issues/963)_)
* Add Events Executor ([#839 ](https://github.com/ros2/rcl/issues/839)_)
* Remove fastrtps customization on test_events ([#960 ](https://github.com/ros2/rcl/issues/960)_)
* Add client/service QoS getters ([#941 ](https://github.com/ros2/rcl/issues/941)_)
* introduce ROS_DISABLE_LOAN_MSG to disable can_loan_messages. ([#949 ](https://github.com/ros2/rcl/issues/949)_)
* Install includes it include/${PROJECT_NAME} ([#959 ](https://github.com/ros2/rcl/issues/959)_)
* Make rcl_difference_times args const ([#955 ](https://github.com/ros2/rcl/issues/955)_)
* Update inject_on_return test skipping logic ([#953 ](https://github.com/ros2/rcl/issues/953)_)
* Fix jump callbacks being called when zero time jump thresholds used ([#948 ](https://github.com/ros2/rcl/issues/948)_)
* Only change the default logger level if default_logger_level is set ([#943 ](https://github.com/ros2/rcl/issues/943)_)
* Add Library for wait_for_entity_helpers to deduplicate compilation ([#942 ](https://github.com/ros2/rcl/issues/942)_)
* Increase Windows timeout 15 -> 25 ms ([#940 ](https://github.com/ros2/rcl/issues/940)_)
* test should check specified number of entities. ([#935 ](https://github.com/ros2/rcl/issues/935)_)
* Fix up documentation build for rcl when using rosdoc2 ([#932 ](https://github.com/ros2/rcl/issues/932)_)
* Include rmw_event_t instead of forward declaring it ([#933 ](https://github.com/ros2/rcl/issues/933)_)
* Add rcl_publisher_wait_for_all_acked support. ([#913 ](https://github.com/ros2/rcl/issues/913)_)
* Add tracing instrumentation for rcl_take. ([#930 ](https://github.com/ros2/rcl/issues/930)_)
* Fix #include in C++ typesupport example in rcl_subscription_init docblock. ([#927 ](https://github.com/ros2/rcl/issues/927)_)
* Update includes after rcutils/get_env.h deprecation. ([#917 ](https://github.com/ros2/rcl/issues/917)_)
* Use proper rcl_logging return value type and compare to constant. ([#916 ](https://github.com/ros2/rcl/issues/916)_)
* Contributors: Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Haowei Wen, Ivan Santiago Paunovic, Jafar Abdi, Michel Hidalgo, Miguel Company, NoyZuberi, Scott K Logan, Shane Loretz, Tomoya Fujita, William Woodall, iRobot ROS, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_action <https://github.com/ros2/rcl/tree/humble/rcl_action/CHANGELOG.rst>`__

* Add Events Executor ([#839 ](https://github.com/ros2/rcl/issues/839)_)
* Install includes it include/${PROJECT_NAME} ([#959 ](https://github.com/ros2/rcl/issues/959)_)
* Fix up documentation build for rcl_action when using rosdoc2 ([#937 ](https://github.com/ros2/rcl/issues/937)_)
* Fix expired goals capacity of action server ([#931 ](https://github.com/ros2/rcl/issues/931)_)
* Wait for action server in rcl_action comm tests. ([#919 ](https://github.com/ros2/rcl/issues/919)_)
* Contributors: Michel Hidalgo, Shane Loretz, iRobot ROS, spiralray


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_interfaces <https://github.com/ros2/rcl_interfaces/tree/humble/rcl_interfaces/CHANGELOG.rst>`__

* Update maintainers to Chris Lalancette ([#130 ](https://github.com/ros2/rcl_interfaces/issues/130)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_lifecycle <https://github.com/ros2/rcl/tree/humble/rcl_lifecycle/CHANGELOG.rst>`__

* Install includes it include/${PROJECT_NAME} ([#959 ](https://github.com/ros2/rcl/issues/959)_)
* [rcl_lifecycle] Do not share transition event message between nodes ([#956 ](https://github.com/ros2/rcl/issues/956)_)
* Update maintainers to Ivan Paunovic and William Woodall ([#952 ](https://github.com/ros2/rcl/issues/952)_)
* Fix up documentation build for rcl_lifecycle when using rosdoc2 ([#938 ](https://github.com/ros2/rcl/issues/938)_)
* Rename variable to fix name shadowing warning ([#929 ](https://github.com/ros2/rcl/issues/929)_)
* Contributors: Alberto Soragna, Audrow Nash, Ivan Santiago Paunovic, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_logging_interface <https://github.com/ros2/rcl_logging/tree/humble/rcl_logging_interface/CHANGELOG.rst>`__

* Install includes to include/${PROJECT_NAME} ([#85 ](https://github.com/ros2/rcl_logging/issues/85)_)
* Fix include order for cpplint ([#84 ](https://github.com/ros2/rcl_logging/issues/84)_) Relates to https://github.com/ament/ament_lint/pull/324
* Update maintainers to Chris Lalancette ([#83 ](https://github.com/ros2/rcl_logging/issues/83)_)
* Fix renamed [`rcpputils`` header (`#81 ](https://github.com/ros2/rcl_logging/issues/81)_)
* Add Doxyfile to rcl_logging_interface package ([#80 ](https://github.com/ros2/rcl_logging/issues/80)_)
* Update includes after rcutils/get_env.h deprecation ([#75 ](https://github.com/ros2/rcl_logging/issues/75)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Christophe Bedard, Jacob Perron, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_logging_noop <https://github.com/ros2/rcl_logging/tree/humble/rcl_logging_noop/CHANGELOG.rst>`__

* Update maintainers to Chris Lalancette ([#83 ](https://github.com/ros2/rcl_logging/issues/83)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_logging_spdlog <https://github.com/ros2/rcl_logging/tree/humble/rcl_logging_spdlog/CHANGELOG.rst>`__

* Fix include order for cpplint ([#84 ](https://github.com/ros2/rcl_logging/issues/84)_) Relates to https://github.com/ament/ament_lint/pull/324
* Update maintainers to Chris Lalancette ([#83 ](https://github.com/ros2/rcl_logging/issues/83)_)
* Fix renamed [`rcpputils`` header (`#81 ](https://github.com/ros2/rcl_logging/issues/81)_)
* Update includes after rcutils/get_env.h deprecation ([#75 ](https://github.com/ros2/rcl_logging/issues/75)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Christophe Bedard, Jacob Perron


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcl_yaml_param_parser <https://github.com/ros2/rcl/tree/humble/rcl_yaml_param_parser/CHANGELOG.rst>`__

* Install includes it include/${PROJECT_NAME} ([#959 ](https://github.com/ros2/rcl/issues/959)_)
* Update maintainers to Ivan Paunovic and William Woodall ([#952 ](https://github.com/ros2/rcl/issues/952)_)
* Tweak rcl_yaml_param_parser documentation ([#939 ](https://github.com/ros2/rcl/issues/939)_)
* Contributors: Audrow Nash, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp <https://github.com/ros2/rclcpp/tree/humble/rclcpp/CHANGELOG.rst>`__

* remove DEFINE_CONTENT_FILTER cmake option ([#1914 ](https://github.com/ros2/rclcpp/issues/1914)_)
* remove things that were deprecated during galactic ([#1913 ](https://github.com/ros2/rclcpp/issues/1913)_)
* add take_data_by_entity_id API to waitable ([#1892 ](https://github.com/ros2/rclcpp/issues/1892)_)
* add content-filtered-topic interfaces ([#1561 ](https://github.com/ros2/rclcpp/issues/1561)_)
* [NodeParameters] Set name in param info pre-check ([#1908 ](https://github.com/ros2/rclcpp/issues/1908)_)
* Add test-dep ament_cmake_google_benchmark ([#1904 ](https://github.com/ros2/rclcpp/issues/1904)_)
* Add publish by loaned message in GenericPublisher ([#1856 ](https://github.com/ros2/rclcpp/issues/1856)_)
* Add missing ament dependency on rcl_interfaces ([#1903 ](https://github.com/ros2/rclcpp/issues/1903)_)
* Update data callback tests to account for all published samples ([#1900 ](https://github.com/ros2/rclcpp/issues/1900)_)
* Increase timeout for acknowledgments to account for slower Connext settings ([#1901 ](https://github.com/ros2/rclcpp/issues/1901)_)
* clang-tidy: explicit constructors ([#1782 ](https://github.com/ros2/rclcpp/issues/1782)_)
* Add client/service QoS getters ([#1784 ](https://github.com/ros2/rclcpp/issues/1784)_)
* Fix a bunch more rosdoc2 issues in rclcpp. ([#1897 ](https://github.com/ros2/rclcpp/issues/1897)_)
* time_until_trigger returns max time if timer is cancelled ([#1893 ](https://github.com/ros2/rclcpp/issues/1893)_)
* Micro-optimizations in rclcpp ([#1896 ](https://github.com/ros2/rclcpp/issues/1896)_)
* spin_all with a zero timeout. ([#1878 ](https://github.com/ros2/rclcpp/issues/1878)_)
* Add RMW listener APIs ([#1579 ](https://github.com/ros2/rclcpp/issues/1579)_)
* Remove fastrtps customization on tests ([#1887 ](https://github.com/ros2/rclcpp/issues/1887)_)
* Install headers to include/${PROJECT_NAME} ([#1888 ](https://github.com/ros2/rclcpp/issues/1888)_)
* Use ament_generate_version_header ([#1886 ](https://github.com/ros2/rclcpp/issues/1886)_)
* use universal reference to support rvalue. ([#1883 ](https://github.com/ros2/rclcpp/issues/1883)_)
* fix one subscription can wait_for_message twice ([#1870 ](https://github.com/ros2/rclcpp/issues/1870)_)
* Add return value version of get_parameter_or ([#1813 ](https://github.com/ros2/rclcpp/issues/1813)_)
* Cleanup time source object lifetimes ([#1867 ](https://github.com/ros2/rclcpp/issues/1867)_)
* add is_spinning() method to executor base class
* Cleanup the TypeAdapt tests ([#1858 ](https://github.com/ros2/rclcpp/issues/1858)_)
* Cleanup includes ([#1857 ](https://github.com/ros2/rclcpp/issues/1857)_)
* Fix include order and relative paths for cpplint ([#1859 ](https://github.com/ros2/rclcpp/issues/1859)_)
* Rename stringstream in macros to a more unique name ([#1862 ](https://github.com/ros2/rclcpp/issues/1862)_)
* Add non transform capabilities for intra-process ([#1849 ](https://github.com/ros2/rclcpp/issues/1849)_)
* Fix rclcpp documentation build ([#1779 ](https://github.com/ros2/rclcpp/issues/1779)_)
* Use UninitializedStaticallyTypedParameterException ([#1689 ](https://github.com/ros2/rclcpp/issues/1689)_)
* Add wait_for_all_acked support ([#1662 ](https://github.com/ros2/rclcpp/issues/1662)_)
* Add tests for function templates of declare_parameter ([#1747 ](https://github.com/ros2/rclcpp/issues/1747)_)
* Fixes for uncrustify 0.72 ([#1844 ](https://github.com/ros2/rclcpp/issues/1844)_)
* use private member to keep the all reference underneath. ([#1845 ](https://github.com/ros2/rclcpp/issues/1845)_)
* Make node base sharable ([#1832 ](https://github.com/ros2/rclcpp/issues/1832)_)
* Add Clock::sleep_for() ([#1828 ](https://github.com/ros2/rclcpp/issues/1828)_)
* Synchronize rcl and std::chrono steady clocks in Clock::sleep_until ([#1830 ](https://github.com/ros2/rclcpp/issues/1830)_)
* Use rclcpp::guard_condition ([#1612 ](https://github.com/ros2/rclcpp/issues/1612)_)
* Call CMake function to generate version header ([#1805 ](https://github.com/ros2/rclcpp/issues/1805)_)
* Use parantheses around logging macro parameter ([#1820 ](https://github.com/ros2/rclcpp/issues/1820)_)
* Remove author by request ([#1818 ](https://github.com/ros2/rclcpp/issues/1818)_)
* Update maintainers ([#1817 ](https://github.com/ros2/rclcpp/issues/1817)_)
* min_forward & min_backward thresholds must not be disabled ([#1815 ](https://github.com/ros2/rclcpp/issues/1815)_)
* Re-add Clock::sleep_until ([#1814 ](https://github.com/ros2/rclcpp/issues/1814)_)
* Fix lifetime of context so it remains alive while its dependent node handles are still in use ([#1754 ](https://github.com/ros2/rclcpp/issues/1754)_)
* Add the interface for pre-shutdown callback ([#1714 ](https://github.com/ros2/rclcpp/issues/1714)_)
* Take message ownership from moved LoanedMessage ([#1808 ](https://github.com/ros2/rclcpp/issues/1808)_)
* Suppress clang dead-store warnings in the benchmarks. ([#1802 ](https://github.com/ros2/rclcpp/issues/1802)_)
* Wait for publisher and subscription to match ([#1777 ](https://github.com/ros2/rclcpp/issues/1777)_)
* Fix unused QoS profile for clock subscription and make ClockQoS the default ([#1801 ](https://github.com/ros2/rclcpp/issues/1801)_)
* Fix dangerous std::bind capture in TimeSource implementation. ([#1768 ](https://github.com/ros2/rclcpp/issues/1768)_)
* Fix dangerous std::bind capture in ParameterEventHandler implementation. ([#1770 ](https://github.com/ros2/rclcpp/issues/1770)_)
* Handle sigterm, in the same way sigint is being handled. ([#1771 ](https://github.com/ros2/rclcpp/issues/1771)_)
* rclcpp::Node copy constructor: make copy of node_waitables\_ member. ([#1799 ](https://github.com/ros2/rclcpp/issues/1799)_)
* Extend NodeGraph to match what rcl provides. ([#1484 ](https://github.com/ros2/rclcpp/issues/1484)_)
* Context::sleep_for(): replace recursion with do-while to avoid potential stack-overflow. ([#1765 ](https://github.com/ros2/rclcpp/issues/1765)_)
* extend_sub_namespace(): Verify string::empty() before calling string::front(). ([#1764 ](https://github.com/ros2/rclcpp/issues/1764)_)
* Deprecate the ``void shared_ptr<MessageT>[` subscription callback signatures. (`#1713 ](https://github.com/ros2/rclcpp/issues/1713)_)
* Remove can_be_nullptr assignment check for QNX case. ([#1752 ](https://github.com/ros2/rclcpp/issues/1752)_)
* Update client API to be able to remove pending requests. ([#1734 ](https://github.com/ros2/rclcpp/issues/1734)_)
* Fix: Allow to add a node while spinning in the StaticSingleThreadedExecutor. ([#1690 ](https://github.com/ros2/rclcpp/issues/1690)_)
* Add tracing instrumentation for executor and message taking. ([#1738 ](https://github.com/ros2/rclcpp/issues/1738)_)
* Fix: Reset timer trigger time before execute in StaticSingleThreadedExecutor. ([#1739 ](https://github.com/ros2/rclcpp/issues/1739)_)
* Use FindPython3 and make python3 dependency explicit. ([#1745 ](https://github.com/ros2/rclcpp/issues/1745)_)
* Use rosidl_get_typesupport_target(). ([#1729 ](https://github.com/ros2/rclcpp/issues/1729)_)
* Fix returning invalid namespace if sub_namespace is empty. ([#1658 ](https://github.com/ros2/rclcpp/issues/1658)_)
* Add free function to wait for a subscription message. ([#1705 ](https://github.com/ros2/rclcpp/issues/1705)_)
* Use rcpputils/scope_exit.hpp and remove rclcpp/scope_exit.hpp. ([#1727 ](https://github.com/ros2/rclcpp/issues/1727)_)
* Remove unsafe get_callback_groups API. Callers should change to using for_each_callback_group(), or store the callback groups they need internally.
* Add in callback_groups_for_each. The main reason to add this method in is to make accesses to the callback_groups\_ vector thread-safe.  By having a callback_groups_for_each that accepts a std::function, we can just have the callers give us the callback they are interested in, and we can take care of the locking. The rest of this fairly large PR is cleaning up all of the places that use get_callback_groups() to instead use callback_groups_for_each().
* Use a different mechanism to avoid timers being scheduled multiple times by the MultiThreadedExecutor ([#1692 ](https://github.com/ros2/rclcpp/issues/1692)_)
* Fix windows CI ([#1726 ](https://github.com/ros2/rclcpp/issues/1726)_) Fix bug in AnyServiceCallback introduced in [#1709 ](https://github.com/ros2/rclcpp/issues/1709)_.
* Support to defer to send a response in services. ([#1709 ](https://github.com/ros2/rclcpp/issues/1709)_) Signed-off-by: Ivan Santiago Paunovic <ivanpauno@ekumenlabs.com>
* Fix documentation bug. ([#1719 ](https://github.com/ros2/rclcpp/issues/1719)_) Signed-off-by: William Woodall <william@osrfoundation.org>
* Removed left over [`is_initialized()`` implementation (`#1711 ](https://github.com/ros2/rclcpp/issues/1711)_) Leftover from https://github.com/ros2/rclcpp/pull/1622
* Fixed declare parameter methods for int and float vectors ([#1696 ](https://github.com/ros2/rclcpp/issues/1696)_)
* Cleaned up implementation of the intra-process manager ([#1695 ](https://github.com/ros2/rclcpp/issues/1695)_)
* Added the node name to an executor [`runtime_error`` (`#1686 ](https://github.com/ros2/rclcpp/issues/1686)_)
* Fixed a typo "Attack" -> "Attach" ([#1687 ](https://github.com/ros2/rclcpp/issues/1687)_)
* Removed use of std::allocator<>::rebind ([#1678 ](https://github.com/ros2/rclcpp/issues/1678)_) rebind is deprecated in c++17 and removed in c++20
* Allow declare uninitialized parameters ([#1673 ](https://github.com/ros2/rclcpp/issues/1673)_)
* Fix syntax issue with gcc ([#1674 ](https://github.com/ros2/rclcpp/issues/1674)_)
* [service] Don't use a weak_ptr to avoid leaking ([#1668 ](https://github.com/ros2/rclcpp/issues/1668)_)
* Fix doc typo ([#1663 ](https://github.com/ros2/rclcpp/issues/1663)_)
* [rclcpp] Type Adaptation feature ([#1557 ](https://github.com/ros2/rclcpp/issues/1557)_)
* Do not attempt to use void allocators for memory allocation. ([#1657 ](https://github.com/ros2/rclcpp/issues/1657)_)
* Keep custom allocator in publisher and subscription options alive. ([#1647 ](https://github.com/ros2/rclcpp/issues/1647)_)
* Fix get_publishers_subscriptions_info_by_topic test in test_node.cpp ([#1648 ](https://github.com/ros2/rclcpp/issues/1648)_)
* Use OnShutdown callback handle instead of OnShutdown callback ([#1639 ](https://github.com/ros2/rclcpp/issues/1639)_)
* use dynamic_pointer_cast to detect allocator mismatch in intra process manager ([#1643 ](https://github.com/ros2/rclcpp/issues/1643)_)
* Contributors: Abrar Rahman Protyasha, Ahmed Sobhy, Alberto Soragna, Andrea Sorbini, Audrow Nash, Barry Xu, Bi0T1N, Chen Lihui, Chris Lalancette, Christophe Bedard, Doug Smith, Emerson Knapp, Gaël Écorchard, Geoffrey Biggs, Gonzo, Grey, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Karsten Knese, Kenji Miyake, M. Hofstätter, M. Mostafa Farzan, Mauro Passerino, Michel Hidalgo, Miguel Company, Nikolai Morin, Petter Nilsson, Scott K Logan, Shane Loretz, Steve Macenski, Tomoya Fujita, William Woodall, Yong-Hao Zou, iRobot ROS, livanov93, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp_action <https://github.com/ros2/rclcpp/tree/humble/rclcpp_action/CHANGELOG.rst>`__

* remove things that were deprecated during galactic ([#1913 ](https://github.com/ros2/rclcpp/issues/1913)_)
* add take_data_by_entity_id API to waitable ([#1892 ](https://github.com/ros2/rclcpp/issues/1892)_)
* Fix rosdoc2 issues ([#1897 ](https://github.com/ros2/rclcpp/issues/1897)_)
* Add RMW listener APIs ([#1579 ](https://github.com/ros2/rclcpp/issues/1579)_)
* Install headers to include/${PROJECT_NAME} ([#1888 ](https://github.com/ros2/rclcpp/issues/1888)_)
* Fix include order and relative paths for cpplint ([#1859 ](https://github.com/ros2/rclcpp/issues/1859)_)
* Fixes for uncrustify 0.72 ([#1844 ](https://github.com/ros2/rclcpp/issues/1844)_)
* Use rclcpp::guard_condition ([#1612 ](https://github.com/ros2/rclcpp/issues/1612)_)
* Remove author by request ([#1818 ](https://github.com/ros2/rclcpp/issues/1818)_)
* Update maintainers ([#1817 ](https://github.com/ros2/rclcpp/issues/1817)_)
* Suppress clang dead-store warnings in the benchmarks. ([#1802 ](https://github.com/ros2/rclcpp/issues/1802)_)
* Deprecate the ``void shared_ptr<MessageT>[` subscription callback signatures (`#1713 ](https://github.com/ros2/rclcpp/issues/1713)_)
* Use rcpputils/scope_exit.hpp and remove rclcpp/scope_exit.hpp. ([#1727 ](https://github.com/ros2/rclcpp/issues/1727)_)
* Fixed occasionally missing goal result caused by race condition ([#1677 ](https://github.com/ros2/rclcpp/issues/1677)_)
* Bump the benchmark timeout for benchmark_action_client ([#1671 ](https://github.com/ros2/rclcpp/issues/1671)_)
* Returns CancelResponse::REJECT while goal handle failed to transit to CANCELING state ([#1641 ](https://github.com/ros2/rclcpp/issues/1641)_)
* Fix action server deadlock issue that caused by other mutexes locked in CancelCallback ([#1635 ](https://github.com/ros2/rclcpp/issues/1635)_)
* Contributors: Abrar Rahman Protyasha, Alberto Soragna, Chris Lalancette, Christophe Bedard, Jacob Perron, Kaven Yau, Shane Loretz, Tomoya Fujita, William Woodall, iRobot ROS, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp_components <https://github.com/ros2/rclcpp/tree/humble/rclcpp_components/CHANGELOG.rst>`__

* Select executor in node registration ([#1898 ](https://github.com/ros2/rclcpp/issues/1898)_)
* Fix rosdoc2 issues in rclcpp ([#1897 ](https://github.com/ros2/rclcpp/issues/1897)_)
* Fix bugprone-exception-escape in node_main.cpp.in ([#1895 ](https://github.com/ros2/rclcpp/issues/1895)_)
* small improvements to node_main.cpp.in
* Install headers to include/${PROJECT_NAME} ([#1888 ](https://github.com/ros2/rclcpp/issues/1888)_)
* Use spin() in component_manager_isolated.hpp ([#1881 ](https://github.com/ros2/rclcpp/issues/1881)_)
* add use_global_arguments for node options of component nodes ([#1776 ](https://github.com/ros2/rclcpp/issues/1776)_)
* Add rclcpp_components::component ([#1855 ](https://github.com/ros2/rclcpp/issues/1855)_)
* Add parameter to configure number of thread ([#1708 ](https://github.com/ros2/rclcpp/issues/1708)_)
* remove RCLCPP_COMPONENTS_PUBLIC in class ComponentManagerIsolated ([#1843 ](https://github.com/ros2/rclcpp/issues/1843)_)
* create component_container_isolated ([#1781 ](https://github.com/ros2/rclcpp/issues/1781)_)
* Remove author by request ([#1818 ](https://github.com/ros2/rclcpp/issues/1818)_)
* Update maintainers ([#1817 ](https://github.com/ros2/rclcpp/issues/1817)_)
* Suppress clang dead-store warnings in the benchmarks. ([#1802 ](https://github.com/ros2/rclcpp/issues/1802)_)
* Update client API to be able to remove pending requests. ([#1734 ](https://github.com/ros2/rclcpp/issues/1734)_)
* Deprecate method names that use CamelCase in rclcpp_components. ([#1716 ](https://github.com/ros2/rclcpp/issues/1716)_)
* Added a hook to generate node options in ComponentManager ([#1702 ](https://github.com/ros2/rclcpp/issues/1702)_)
* Contributors: Alberto Soragna, Chris Lalancette, Daisuke Nishimatsu, Hirokazu Ishida, Ivan Santiago Paunovic, Jacob Perron, Rebecca Butler, Shane Loretz, gezp


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclcpp_lifecycle <https://github.com/ros2/rclcpp/tree/humble/rclcpp_lifecycle/CHANGELOG.rst>`__

* remove things that were deprecated during galactic ([#1913 ](https://github.com/ros2/rclcpp/issues/1913)_)
* Fix rosdoc2 issues ([#1897 ](https://github.com/ros2/rclcpp/issues/1897)_)
* Install headers to include/${PROJECT_NAME} ([#1888 ](https://github.com/ros2/rclcpp/issues/1888)_)
* LifecycleNode::on_deactivate deactivate all managed entities. ([#1885 ](https://github.com/ros2/rclcpp/issues/1885)_)
* Automatically transition lifecycle entities when node transitions ([#1863 ](https://github.com/ros2/rclcpp/issues/1863)_)
* Remove author by request ([#1818 ](https://github.com/ros2/rclcpp/issues/1818)_)
* Update maintainers ([#1817 ](https://github.com/ros2/rclcpp/issues/1817)_)
* Suppress clang dead-store warnings in the benchmarks. ([#1802 ](https://github.com/ros2/rclcpp/issues/1802)_)
* Update forward declarations of [`rcl_lifecycle`` types (`#1788 ](https://github.com/ros2/rclcpp/issues/1788)_)
* Deprecate the ``void shared_ptr<MessageT>[` subscription callback signatures (`#1713 ](https://github.com/ros2/rclcpp/issues/1713)_)
* Update client API to be able to remove pending requests. ([#1734 ](https://github.com/ros2/rclcpp/issues/1734)_)
* Change log level for lifecycle_publisher. ([#1715 ](https://github.com/ros2/rclcpp/issues/1715)_)
* Fix: RCLCPP_PUBLIC -> RCLCPP_LIFECYCLE_PUBLIC ([#1732 ](https://github.com/ros2/rclcpp/issues/1732)_)
* Use rcpputils/scope_exit.hpp and remove rclcpp/scope_exit.hpp ([#1727 ](https://github.com/ros2/rclcpp/issues/1727)_)
* Remove unsafe get_callback_groups API. Callers should change to using for_each_callback_group(), or store the callback groups they need internally.
* Add in callback_groups_for_each. The main reason to add this method in is to make accesses to the callback_groups\_ vector thread-safe.  By having a callback_groups_for_each that accepts a std::function, we can just have the callers give us the callback they are interested in, and we can take care of the locking. The rest of this fairly large PR is cleaning up all of the places that use get_callback_groups() to instead use callback_groups_for_each().
* Fix destruction order in lifecycle benchmark ([#1675 ](https://github.com/ros2/rclcpp/issues/1675)_)
* [rclcpp] Type Adaptation feature ([#1557 ](https://github.com/ros2/rclcpp/issues/1557)_)
* Contributors: Abrar Rahman Protyasha, Alberto Soragna, Audrow Nash, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Michel Hidalgo, Shane Loretz, Tomoya Fujita, William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rclpy <https://github.com/ros2/rclpy/tree/humble/rclpy/CHANGELOG.rst>`__

* Make rclpy dependencies explicit ([#906 ](https://github.com/ros2/rclpy/issues/906)_)
* Avoid exception in Node constructor when use override for 'use_sim_time' ([#896 ](https://github.com/ros2/rclpy/issues/896)_)
* time_until_next_call returns max if timer is canceled. ([#910 ](https://github.com/ros2/rclpy/issues/910)_)
* Properly implement action server/client handle cleanup. ([#905 ](https://github.com/ros2/rclpy/issues/905)_)
* Make sure to take out contexts on Action{Client,Server}. ([#904 ](https://github.com/ros2/rclpy/issues/904)_)
* Make sure to free the goal_status_array when done using it. ([#902 ](https://github.com/ros2/rclpy/issues/902)_)
* Bugfix to Node.destroy_rate() result ([#901 ](https://github.com/ros2/rclpy/issues/901)_)
* Remove fastrtps customization on tests ([#895 ](https://github.com/ros2/rclpy/issues/895)_)
* fix typo ([#890 ](https://github.com/ros2/rclpy/issues/890)_)
* Document that Future.result() may return None ([#884 ](https://github.com/ros2/rclpy/issues/884)_)
* update doc release number ([#885 ](https://github.com/ros2/rclpy/issues/885)_)
* Fix multi-threaded race condition in client.call_async ([#871 ](https://github.com/ros2/rclpy/issues/871)_)
* Fix include order for cpplint ([#877 ](https://github.com/ros2/rclpy/issues/877)_)
* Bugfix/duration to msg precision ([#876 ](https://github.com/ros2/rclpy/issues/876)_)
* Update to pybind11 2.7.1 ([#874 ](https://github.com/ros2/rclpy/issues/874)_)
* QoS history depth is only available with KEEP_LAST ([#869 ](https://github.com/ros2/rclpy/issues/869)_)
* Implement managed nodes. ([#865 ](https://github.com/ros2/rclpy/issues/865)_)
* Make rclpy.try_shutdown() behavior to follow rclpy.shutdown() more closely. ([#868 ](https://github.com/ros2/rclpy/issues/868)_)
* Update TopicEndpointTypeEnum.__str_\_() method to include history kind and history depth. ([#849 ](https://github.com/ros2/rclpy/issues/849)_)
* Add Clock.sleep_for() using Clock.sleep_until(). ([#864 ](https://github.com/ros2/rclpy/issues/864)_)
* Add Clock.sleep_until() ([#858 ](https://github.com/ros2/rclpy/issues/858)_)
* Add __enter_\_ and __exit_\_ to JumpHandle. ([#862 ](https://github.com/ros2/rclpy/issues/862)_)
* Don't override rclpy._rclpy_pybind11 docs. ([#863 ](https://github.com/ros2/rclpy/issues/863)_)
* Improve JumpThreshold documentation and forbid zero durations. ([#861 ](https://github.com/ros2/rclpy/issues/861)_)
* Fix time.py and clock.py circular import. ([#860 ](https://github.com/ros2/rclpy/issues/860)_)
* Make context.on_shutdown() allow free functions. ([#859 ](https://github.com/ros2/rclpy/issues/859)_)
* Fix automatically declared parameters descriptor type. ([#853 ](https://github.com/ros2/rclpy/issues/853)_)
* Shutdown asynchronously when sigint is received. ([#844 ](https://github.com/ros2/rclpy/issues/844)_)
* Update maintainers. ([#845 ](https://github.com/ros2/rclpy/issues/845)_)
* Add entities to callback group before making them available to the executor to avoid a race condition. ([#839 ](https://github.com/ros2/rclpy/issues/839)_)
* Avoid race condition in client.call(). ([#838 ](https://github.com/ros2/rclpy/issues/838)_)
* Handle sigterm. ([#830 ](https://github.com/ros2/rclpy/issues/830)_)
* Use pybind11 for signal handling, and delete now unused rclpy_common, pycapsule, and handle code. ([#814 ](https://github.com/ros2/rclpy/issues/814)_)
* Fix memory leak in Service::take_request() and Client::take_response(). ([#828 ](https://github.com/ros2/rclpy/issues/828)_)
* Add Publisher.wait_for_all_acked(). ([#793 ](https://github.com/ros2/rclpy/issues/793)_)
* Only add one done callback to a future in Executor. ([#816 ](https://github.com/ros2/rclpy/issues/816)_)
* Add convert function from ParameterValue to Python builtin. ([#819 ](https://github.com/ros2/rclpy/issues/819)_)
* Call Context._logging_fini() in Context.try_shutdown(). ([#800 ](https://github.com/ros2/rclpy/issues/800)_)
* Lift LoggingSeverity enum as common dependency to logging and rcutils_logger modules ([#785 ](https://github.com/ros2/rclpy/issues/785)_)
* Set Context.__context to None in __init_\_(). ([#812 ](https://github.com/ros2/rclpy/issues/812)_)
* Remove unused function make_mock_subscription. ([#809 ](https://github.com/ros2/rclpy/issues/809)_)
* Removed common.c/h ([#789 ](https://github.com/ros2/rclpy/issues/789)_)
* Allow declaring uninitialized parameters ([#798 ](https://github.com/ros2/rclpy/issues/798)_)
* Reject cancel request if failed to transit to CANCEL_GOAL state ([#791 ](https://github.com/ros2/rclpy/issues/791)_)
* Deleted handle as it should no longer be used ([#786 ](https://github.com/ros2/rclpy/issues/786)_)
* Removed some functions in common.c and replaced them in utils.cpp ([#787 ](https://github.com/ros2/rclpy/issues/787)_)
* Moved exception.cpp/hpp to the _rclpy_pybind11 module ([#788 ](https://github.com/ros2/rclpy/issues/788)_)
* Print 'Infinite' for infinite durations in topic endpoint info ([#722 ](https://github.com/ros2/rclpy/issues/722)_)
* Break log function execution ASAP if configured severity is too high ([#776 ](https://github.com/ros2/rclpy/issues/776)_)
* Convert Node and Context to use C++ Classes ([#771 ](https://github.com/ros2/rclpy/issues/771)_)
* Misc action server improvements ([#774 ](https://github.com/ros2/rclpy/issues/774)_)
* Misc action goal handle improvements ([#767 ](https://github.com/ros2/rclpy/issues/767)_)
* Convert Guardcondition to use C++ classes ([#772 ](https://github.com/ros2/rclpy/issues/772)_)
* Removed unused structs [`rclpy_client_t`` and ``rclpy_service_t`` (`#770 ](https://github.com/ros2/rclpy/issues/770)_)
* Convert WaitSet to use C++ Classes ([#769 ](https://github.com/ros2/rclpy/issues/769)_)
* Convert ActionServer to use C++ Classes ([#766 ](https://github.com/ros2/rclpy/issues/766)_)
* Convert ActionClient to use C++ classes ([#759 ](https://github.com/ros2/rclpy/issues/759)_)
* Use py::class\_ for rcl_action_goal_handle_t ([#751 ](https://github.com/ros2/rclpy/issues/751)_)
* Convert Publisher and Subscription to use C++ Classes ([#756 ](https://github.com/ros2/rclpy/issues/756)_)
* Rename QoS*Policy enum's to \*Policy ([#379 ](https://github.com/ros2/rclpy/issues/379)_)
* Use params from node '/\*\*' from parameter YAML file ([#370 ](https://github.com/ros2/rclpy/issues/370)_)
* Updated to use params from node '/\*\*' from parameter YAML file. ([#399 ](https://github.com/ros2/rclpy/issues/399)_)
* Contributors: Alejandro Hernández Cordero, Anthony, Artem Shumov, Auguste Lalande, Barry Xu, Chris Lalancette, Emerson Knapp, Erki Suurjaak, Greg Balke, Ivan Santiago Paunovic, Jacob Perron, Lei Liu, Louise Poubel, Miguel Company, Shane Loretz, Tomoya Fujita, ksuszka


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcpputils <https://github.com/ros2/rcpputils/tree/humble/CHANGELOG.rst>`__

* Install includes to include/${PROJECT_NAME} ([#160 ](https://github.com/ros2/rcpputils/issues/160)_)
* Fix include order for cpplint ([#158 ](https://github.com/ros2/rcpputils/issues/158)_)
* [path] Declare the default assignment operator ([#156 ](https://github.com/ros2/rcpputils/issues/156)_)
* Fixes for uncrustify 0.72 ([#154 ](https://github.com/ros2/rcpputils/issues/154)_)
* Fix the BSD license headers to use the standard one. ([#153 ](https://github.com/ros2/rcpputils/issues/153)_)
* Update maintainers to Chris Lalancette ([#152 ](https://github.com/ros2/rcpputils/issues/152)_)
* Add checked convert_to_nanoseconds() function ([#145 ](https://github.com/ros2/rcpputils/issues/145)_)
* Add missing sections in docs/FEATURES.md TOC ([#151 ](https://github.com/ros2/rcpputils/issues/151)_)
* [env] Add [`set_env_var`` function (`#150 ](https://github.com/ros2/rcpputils/issues/150)_)
* Add missing cstddef include ([#147 ](https://github.com/ros2/rcpputils/issues/147)_)
* Add accumulator test to CMakeLists.txt ([#144 ](https://github.com/ros2/rcpputils/issues/144)_)
* [`rcpputils::fs``: Fix doxygen parameter identifier (`#142 ](https://github.com/ros2/rcpputils/issues/142)_)
* Make thread safety macro C++ standards compliant ([#141 ](https://github.com/ros2/rcpputils/issues/141)_)
* Fix API documentation for clean [`rosdoc2`` build (`#139 ](https://github.com/ros2/rcpputils/issues/139)_)
* Improve [`rcppmath`` Doxygen documentation (`#138 ](https://github.com/ros2/rcpputils/issues/138)_)
* Improve documentation of utilities in docs/FEATURES.md ([#137 ](https://github.com/ros2/rcpputils/issues/137)_)
* Include [`rcppmath`` utilities in docs/FEATURES.md (`#136 ](https://github.com/ros2/rcpputils/issues/136)_)
* Fix [`IllegalStateException`` reference in FEATURES (`#135 ](https://github.com/ros2/rcpputils/issues/135)_)
* migrate rolling mean from ros2_controllers to rcppmath ([#133 ](https://github.com/ros2/rcpputils/issues/133)_)
* Update includes after rcutils/get_env.h deprecation ([#132 ](https://github.com/ros2/rcpputils/issues/132)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Chris Lalancette, Christophe Bedard, Jacob Perron, Karsten Knese, Octogonapus, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rcutils <https://github.com/ros2/rcutils/tree/humble/CHANGELOG.rst>`__

* Update launch test for change related to enviroment variables in launch ([#354 ](https://github.com/ros2/rcutils/issues/354)_)
* Remove dst_size from strlen usage ([#353 ](https://github.com/ros2/rcutils/issues/353)_)
* Install headers to include\${PROJECT_NAME} ([#351 ](https://github.com/ros2/rcutils/issues/351)_)
* Use static_cast instead of C-style cast ([#349 ](https://github.com/ros2/rcutils/issues/349)_)
* Fixing up documentation build when using rosdoc2 ([#344 ](https://github.com/ros2/rcutils/issues/344)_)
* Stop double-defining structs. ([#333 ](https://github.com/ros2/rcutils/issues/333)_)
* Use FindPython3 explicitly instead of FindPythonInterp implicitly ([#345 ](https://github.com/ros2/rcutils/issues/345)_)
* Fix build on Android ([#342 ](https://github.com/ros2/rcutils/issues/342)_)
* Deprecate get_env.h and move content to env.{h,c} ([#340 ](https://github.com/ros2/rcutils/issues/340)_)
* Contributors: Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Shane Loretz, William Woodall


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `resource_retriever <https://github.com/ros/resource_retriever/tree/humble/resource_retriever/CHANGELOG.rst>`__

* Install headers to include/${PROJECT_NAME} ([#72 ](https://github.com/ros/resource_retriever/issues/72)_)
* Fix include order for cpplint ([#69 ](https://github.com/ros/resource_retriever/issues/69)_)
* Update maintainers ([#66 ](https://github.com/ros/resource_retriever/issues/66)_)
* Remove the deprecated retriever.h header ([#63 ](https://github.com/ros/resource_retriever/issues/63)_)
* Contributors: Audrow Nash, Chris Lalancette, Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw <https://github.com/ros2/rmw/tree/humble/rmw/CHANGELOG.rst>`__

* Add content filtered topics support. ([#302 ](https://github.com/ros2/rmw/issues/302)_)
* Add sequence numbers to rmw_message_info_t. ([#318 ](https://github.com/ros2/rmw/issues/318)_)
* Add rmw_feature_supported(). ([#318 ](https://github.com/ros2/rmw/issues/318)_)
* Add EventsExecutor ([#286 ](https://github.com/ros2/rmw/issues/286)_)
* Document that rmw_wait() SHOULD use a monotonic clock ([#316 ](https://github.com/ros2/rmw/issues/316)_)
* Install headers to include/${PROJECT_NAME} ([#317 ](https://github.com/ros2/rmw/issues/317)_)
* Update rmw_server_is_available() API documentation. ([#277 ](https://github.com/ros2/rmw/issues/277)_)
* Add client/service QoS getters. ([#314 ](https://github.com/ros2/rmw/issues/314)_)
* Fix up documentation build for rmw when using rosdoc2 ([#313 ](https://github.com/ros2/rmw/issues/313)_)
* Fix up errors in doxygen documentation ([#311 ](https://github.com/ros2/rmw/issues/311)_)
* Fix copy-paste error in API doc for rmw_get_gid_for_publisher ([#310 ](https://github.com/ros2/rmw/issues/310)_)
* Add rmw_publisher_wait_for_all_acked support. ([#296 ](https://github.com/ros2/rmw/issues/296)_)
* Contributors: Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Michel Hidalgo, Shane Loretz, iRobot ROS, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_connextdds <https://github.com/ros2/rmw_connextdds/tree/humble/rmw_connextdds/CHANGELOG.rst>`__

* Exclude missing sample info fields when building rmw_connextddsmicro ([#79 ](https://github.com/ros2/rmw_connextdds/issues/79)_)
* Update launch_testing_ros output filter prefixes for Connext6 ([#80 ](https://github.com/ros2/rmw_connextdds/issues/80)_)
* Add support for user-specified content filters ([#68 ](https://github.com/ros2/rmw_connextdds/issues/68)_)
* add stub for content filtered topic ([#77 ](https://github.com/ros2/rmw_connextdds/issues/77)_)
* Add rmw listener apis ([#44 ](https://github.com/rticommunity/rmw_connextdds/issues/44)_)
* Add client/service QoS getters. ([#67 ](https://github.com/rticommunity/rmw_connextdds/issues/67)_)
* Add rmw_publisher_wait_for_all_acked support. ([#20 ](https://github.com/rticommunity/rmw_connextdds/issues/20)_)
* Contributors: Andrea Sorbini, Barry Xu, Chen Lihui, Ivan Santiago Paunovic, iRobot ROS, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_connextdds_common <https://github.com/ros2/rmw_connextdds/tree/humble/rmw_connextdds_common/CHANGELOG.rst>`__

* Exclude missing sample info fields when building rmw_connextddsmicro ([#79 ](https://github.com/ros2/rmw_connextdds/issues/79)_)
* Properly initialize CDR stream before using it for filtering ([#81 ](https://github.com/ros2/rmw_connextdds/issues/81)_)
* Add support for user-specified content filters ([#68 ](https://github.com/ros2/rmw_connextdds/issues/68)_)
* add stub for content filtered topic ([#77 ](https://github.com/ros2/rmw_connextdds/issues/77)_)
* Add sequence numbers to message info structure ([#74 ](https://github.com/ros2/rmw_connextdds/issues/74)_)
* Add rmw listener apis ([#44 ](https://github.com/rticommunity/rmw_connextdds/issues/44)_)
* Fix cpplint errors ([#69 ](https://github.com/ros2/rmw_connextdds/issues/69)_)
* Add client/service QoS getters. ([#67 ](https://github.com/rticommunity/rmw_connextdds/issues/67)_)
* Update rmw_context_impl_t definition ([#65 ](https://github.com/ros2/rmw_connextdds/issues/65)_)
* Use the new rmw_dds_common::get_security_files API ([#61 ](https://github.com/ros2/rmw_connextdds/issues/61)_)
* Add rmw_publisher_wait_for_all_acked support. ([#20 ](https://github.com/rticommunity/rmw_connextdds/issues/20)_)
* Support extended signature for [`message_type_support_callbacks_t::max_serialized_size()`` from ``rosidl_typesupport_fastrtps_cpp``. (`#14 ](https://github.com/rticommunity/rmw_connextdds/issues/14)_)
* Update includes after rcutils/get_env.h deprecation. ([#55 ](https://github.com/rticommunity/rmw_connextdds/issues/55)_)
* Always modify UserObjectQosPolicy regardless of override policy. ([#53 ](https://github.com/rticommunity/rmw_connextdds/issues/53)_)
* Improved conversion of time values between ROS and DDS formats. ([#43 ](https://github.com/rticommunity/rmw_connextdds/issues/43)_)
* Allow sharing DomainParticipant with C++ applications. ([#25 ](https://github.com/rticommunity/rmw_connextdds/issues/25)_)
* Add environment variable to control override of DomainParticipantQos. ([#41 ](https://github.com/rticommunity/rmw_connextdds/issues/41)_)
* Contributors: Andrea Sorbini, Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Michel Hidalgo, Miguel Company, iRobot ROS, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_connextddsmicro <https://github.com/ros2/rmw_connextdds/tree/humble/rmw_connextddsmicro/CHANGELOG.rst>`__

* Exclude missing sample info fields when building rmw_connextddsmicro ([#79 ](https://github.com/ros2/rmw_connextdds/issues/79)_)
* Add support for user-specified content filters ([#68 ](https://github.com/ros2/rmw_connextdds/issues/68)_)
* add stub for content filtered topic ([#77 ](https://github.com/ros2/rmw_connextdds/issues/77)_)
* Add sequence numbers to message info structure ([#74 ](https://github.com/ros2/rmw_connextdds/issues/74)_)
* Add rmw listener apis ([#44 ](https://github.com/rticommunity/rmw_connextdds/issues/44)_)
* Add client/service QoS getters. ([#67 ](https://github.com/rticommunity/rmw_connextdds/issues/67)_)
* Add rmw_publisher_wait_for_all_acked support. ([#20 ](https://github.com/rticommunity/rmw_connextdds/issues/20)_)
* Contributors: Andrea Sorbini, Barry Xu, Chen Lihui, Ivan Santiago Paunovic, iRobot ROS, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_cyclonedds_cpp <https://github.com/ros2/rmw_cyclonedds/tree/humble/rmw_cyclonedds_cpp/CHANGELOG.rst>`__

* Fix get_topic_name and handling long service names
* Add serialization for SDK_DATA
* Additional checks for loan API
* Depend on just rmw_dds_common::rmw_dds_common_library ([#385 ](https://github.com/ros2/rmw_cyclonedds/issues/385)_)
* Fix error message in rmw_init_options_copy(). ([#380 ](https://github.com/ros2/rmw_cyclonedds/issues/380)_)
* Add content filter topic feature empty stub. ([#289 ](https://github.com/ros2/rmw_cyclonedds/issues/289)_)
* Update to work with Cyclone 0.9.0 and Iceoryx 2.0 ([#379 ](https://github.com/ros2/rmw_cyclonedds/issues/379)_)
* Fill message info sequence numbers as unsupported, add rmw_feature_supported() implementation. ([#381 ](https://github.com/ros2/rmw_cyclonedds/issues/381)_)
* Fix a warning by making a pointer nullptr. ([#375 ](https://github.com/ros2/rmw_cyclonedds/issues/375)_)
* Bump QDs to QL2 ([#371 ](https://github.com/ros2/rmw_cyclonedds/issues/371)_)
* Add EventsExecutor ([#256 ](https://github.com/ros2/rmw_cyclonedds/issues/256)_)
* Call dissociate_reader in rmw_destroy_subscription
* Wrap creation of new serdata_rmw within a try-catch block
* Fix memory leak in error scenario on the publish side with SHM
* Fix memory leaks on the take side with SHM
* rename _cyclonedds_has_shm to follow the convention
* Add iceoryx_binding_c as dependency to rmw_cyclonedds_cpp
* Release iox_chunk to iceoryx in serdata_free if the iox_chunk is still available
* Update iceoryx_subscriber also when constructing the serdata from the iox chunk
* Fix cpplint errors ([#363 ](https://github.com/ros2/rmw_cyclonedds/issues/363)_)
* Updates for uncrustify 0.72 ([#358 ](https://github.com/ros2/rmw_cyclonedds/issues/358)_)
* Export only rmw::rmw to downstream targets ([#360 ](https://github.com/ros2/rmw_cyclonedds/issues/360)_)
* Export modern CMake targets ([#357 ](https://github.com/ros2/rmw_cyclonedds/issues/357)_)
* Free with the same allocator in rmw_destroy_node ([#355 ](https://github.com/ros2/rmw_cyclonedds/issues/355)_)
* Add client/service QoS getters. ([#343 ](https://github.com/ros2/rmw_cyclonedds/issues/343)_)
* Updated version number and quality level. ([#349 ](https://github.com/ros2/rmw_cyclonedds/issues/349)_)
* Update package maintainers. ([#351 ](https://github.com/ros2/rmw_cyclonedds/issues/351)_)
* Fix undesired memory initialization in zero-copy data path. ([#348 ](https://github.com/ros2/rmw_cyclonedds/issues/348)_)
* Fix QoS depth settings for clients/service being ignored. ([#340 ](https://github.com/ros2/rmw_cyclonedds/issues/340)_)
* Link to Cyclone DDS in Quality Declaration. ([#342 ](https://github.com/ros2/rmw_cyclonedds/issues/342)_)
* Update rmw_context_impl_t definition ([#337 ](https://github.com/ros2/rmw_cyclonedds/issues/337)_)
* Add quality declaration for rmw_cyclonedds_cpp ([#335 ](https://github.com/ros2/rmw_cyclonedds/issues/335)_)
* Fix use of deprecated is_loan_available ([#336 ](https://github.com/ros2/rmw_cyclonedds/issues/336)_)
* Add -latomic for RISC-V ([#332 ](https://github.com/ros2/rmw_cyclonedds/issues/332)_)
* Add pub/sub init, publish and take instrumentation using tracetools ([#329 ](https://github.com/ros2/rmw_cyclonedds/issues/329)_)
* Pass the CRL down to CycloneDDS if it exists ([#325 ](https://github.com/ros2/rmw_cyclonedds/issues/325)_)
* Use the new rmw_dds_common::get_security_files API ([#323 ](https://github.com/ros2/rmw_cyclonedds/issues/323)_)
* Add rmw_publisher_wait_for_all_acked support. ([#294 ](https://github.com/ros2/rmw_cyclonedds/issues/294)_)
* Fix zero copy issues. ([#309 ](https://github.com/ros2/rmw_cyclonedds/issues/309)_)
* Handle allocation errors during message deserialization. ([#313 ](https://github.com/ros2/rmw_cyclonedds/issues/313)_)
* Update includes after rcutils/get_env.h deprecation. ([#312 ](https://github.com/ros2/rmw_cyclonedds/issues/312)_)
* Contributors: Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Dietrich Krönke, Erik Boasson, Haowei Wen, Ivan Santiago Paunovic, Jacob Perron, Joe Speed, Michel Hidalgo, Shane Loretz, Sumanth Nirmal, eboasson, guillaume-pais-siemens, iRobot ROS, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_dds_common <https://github.com/ros2/rmw_dds_common/tree/humble/rmw_dds_common/CHANGELOG.rst>`__

* Depend on target generated by rosidl_typesupport_cpp ([#58 ](https://github.com/ros2/rmw_dds_common/issues/58)_)
* Use rosidl_get_typesupport_target() and target_link_libraries(). ([#57 ](https://github.com/ros2/rmw_dds_common/issues/57)_)
* Install headers to include/${PROJECT_NAME} ([#56 ](https://github.com/ros2/rmw_dds_common/issues/56)_)
* Fix include order for cpplint ([#55 ](https://github.com/ros2/rmw_dds_common/issues/55)_)
* Fix up rmw_dds_common documentation when using rosdoc2 ([#54 ](https://github.com/ros2/rmw_dds_common/issues/54)_)
* Add support for Certificate Revocation List files ([#52 ](https://github.com/ros2/rmw_dds_common/issues/52)_)
* Silence clang warning ([`range-loop-construct``) (`#53 ](https://github.com/ros2/rmw_dds_common/issues/53)_)
* Add a common function for security files. ([#51 ](https://github.com/ros2/rmw_dds_common/issues/51)_)
* Normalize rmw_time_t according to DDS spec ([#48 ](https://github.com/ros2/rmw_dds_common/issues/48)_)
* Contributors: Andrea Sorbini, Chris Lalancette, Jacob Perron, Karsten Knese, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_fastrtps_cpp <https://github.com/ros2/rmw_fastrtps/tree/humble/rmw_fastrtps_cpp/CHANGELOG.rst>`__

* Add pub/sub init, publish and take instrumentation using tracetools ([#591 ](https://github.com/ros2/rmw_fastrtps/issues/591)_)
* Add content filter topic feature ([#513 ](https://github.com/ros2/rmw_fastrtps/issues/513)_)
* Add sequence numbers to message info structure ([#587 ](https://github.com/ros2/rmw_fastrtps/issues/587)_)
* Removed some heap interactions in rmw_serialize.cpp ([#590 ](https://github.com/ros2/rmw_fastrtps/issues/590)_)
* Add EventsExecutor ([#468 ](https://github.com/ros2/rmw_fastrtps/issues/468)_)
* Install headers to include/${PROJECT_NAME} ([#578 ](https://github.com/ros2/rmw_fastrtps/issues/578)_)
* Add client/service QoS getters. ([#560 ](https://github.com/ros2/rmw_fastrtps/issues/560)_)
* Correctly recalculate serialized size on bounded sequences. ([#540 ](https://github.com/ros2/rmw_fastrtps/issues/540)_)
* Fix type size alignment. ([#550 ](https://github.com/ros2/rmw_fastrtps/issues/550)_)
* Change links from index.ros.org -> docs.ros.org ([#539 ](https://github.com/ros2/rmw_fastrtps/issues/539)_)
* Add rmw_publisher_wait_for_all_acked support. ([#519 ](https://github.com/ros2/rmw_fastrtps/issues/519)_)
* Loan messages implementation ([#523 ](https://github.com/ros2/rmw_fastrtps/issues/523)_) * Added is_plain\_ attribute to base TypeSupport. * Added new methods to base TypeSupport. * Implementation of rmw_borrow_loaned_message. * Implementation of rmw_return_loaned_message_from_publisher. * Enable loan messages on publishers of plain types. * Implementation for taking loaned messages. * Enable loan messages on subscriptions of plain types.
* Contributors: Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Miguel Company, Shane Loretz, WideAwakeTN, iRobot ROS, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_fastrtps_dynamic_cpp <https://github.com/ros2/rmw_fastrtps/tree/humble/rmw_fastrtps_dynamic_cpp/CHANGELOG.rst>`__

* Add content filter topic feature ([#513 ](https://github.com/ros2/rmw_fastrtps/issues/513)_)
* Add sequence numbers to message info structure ([#587 ](https://github.com/ros2/rmw_fastrtps/issues/587)_)
* Add EventsExecutor ([#468 ](https://github.com/ros2/rmw_fastrtps/issues/468)_)
* Install headers to include/${PROJECT_NAME} ([#578 ](https://github.com/ros2/rmw_fastrtps/issues/578)_)
* Add client/service QoS getters. ([#560 ](https://github.com/ros2/rmw_fastrtps/issues/560)_)
* Correctly recalculate serialized size on bounded sequences. ([#540 ](https://github.com/ros2/rmw_fastrtps/issues/540)_)
* Fix type size alignment. ([#550 ](https://github.com/ros2/rmw_fastrtps/issues/550)_)
* Add rmw_publisher_wait_for_all_acked support. ([#519 ](https://github.com/ros2/rmw_fastrtps/issues/519)_)
* Loan messages implementation ([#523 ](https://github.com/ros2/rmw_fastrtps/issues/523)_) * Added is_plain\_ attribute to base TypeSupport. * Added new methods to base TypeSupport. * Implementation of rmw_borrow_loaned_message. * Implementation of rmw_return_loaned_message_from_publisher. * Enable loan messages on publishers of plain types. * Implementation for taking loaned messages. * Enable loan messages on subscriptions of plain types.
* Contributors: Barry Xu, Chen Lihui, Ivan Santiago Paunovic, Miguel Company, Shane Loretz, iRobot ROS, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_fastrtps_shared_cpp <https://github.com/ros2/rmw_fastrtps/tree/humble/rmw_fastrtps_shared_cpp/CHANGELOG.rst>`__

* Address linter waning for windows. ([#592 ](https://github.com/ros2/rmw_fastrtps/issues/592)_)
* Add pub/sub init, publish and take instrumentation using tracetools ([#591 ](https://github.com/ros2/rmw_fastrtps/issues/591)_)
* Add content filter topic feature ([#513 ](https://github.com/ros2/rmw_fastrtps/issues/513)_)
* Add sequence numbers to message info structure ([#587 ](https://github.com/ros2/rmw_fastrtps/issues/587)_)
* Add EventsExecutor ([#468 ](https://github.com/ros2/rmw_fastrtps/issues/468)_)
* Complete events support ([#583 ](https://github.com/ros2/rmw_fastrtps/issues/583)_)
* Install headers to include/${PROJECT_NAME} ([#578 ](https://github.com/ros2/rmw_fastrtps/issues/578)_)
* Change default to synchronous ([#571 ](https://github.com/ros2/rmw_fastrtps/issues/571)_)
* Fix cpplint error ([#574 ](https://github.com/ros2/rmw_fastrtps/issues/574)_)
* Fixes for uncrustify 0.72 ([#572 ](https://github.com/ros2/rmw_fastrtps/issues/572)_)
* Add client/service QoS getters. ([#560 ](https://github.com/ros2/rmw_fastrtps/issues/560)_)
* Fix QoS depth settings for clients/service being ignored. ([#564 ](https://github.com/ros2/rmw_fastrtps/issues/564)_)
* Update rmw_context_impl_t definition. ([#558 ](https://github.com/ros2/rmw_fastrtps/issues/558)_)
* Update the LoanManager to do internal locking. ([#552 ](https://github.com/ros2/rmw_fastrtps/issues/552)_)
* Pass the CRL down to Fast-DDS if available. ([#546 ](https://github.com/ros2/rmw_fastrtps/issues/546)_)
* Use the new rmw_dds_common::get_security_files ([#544 ](https://github.com/ros2/rmw_fastrtps/issues/544)_)
* Support for SubscriptionOptions::ignore_local_publications ([#536 ](https://github.com/ros2/rmw_fastrtps/issues/536)_)
* Change links from index.ros.org -> docs.ros.org ([#539 ](https://github.com/ros2/rmw_fastrtps/issues/539)_)
* Add rmw_publisher_wait_for_all_acked support. ([#519 ](https://github.com/ros2/rmw_fastrtps/issues/519)_)
* Loan messages implementation ([#523 ](https://github.com/ros2/rmw_fastrtps/issues/523)_) * Added is_plain\_ attribute to base TypeSupport. * Added new methods to base TypeSupport. * Implementation of rmw_borrow_loaned_message. * Implementation of rmw_return_loaned_message_from_publisher. * Enable loan messages on publishers of plain types. * Implementation for taking loaned messages. * Enable loan messages on subscriptions of plain types.
* Export rmw_dds_common as an rmw_fastrtps_shared_cpp dependency ([#530 ](https://github.com/ros2/rmw_fastrtps/issues/530)_)
* Update includes after rcutils/get_env.h deprecation ([#529 ](https://github.com/ros2/rmw_fastrtps/issues/529)_)
* Contributors: Audrow Nash, Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Jose Antonio Moral, Michel Hidalgo, Miguel Company, Shane Loretz, Tomoya Fujita, iRobot ROS, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_implementation <https://github.com/ros2/rmw_implementation/tree/humble/rmw_implementation/CHANGELOG.rst>`__

* add content-filtered-topic interfaces ([#181 ](https://github.com/ros2/rmw_implementation/issues/181)_)
* Add rmw_feature_supported() ([#204 ](https://github.com/ros2/rmw_implementation/issues/204)_)
* Add EventsExecutor ([#161 ](https://github.com/ros2/rmw_implementation/issues/161)_)
* Fix relative path include syntax for cpplint ([#203 ](https://github.com/ros2/rmw_implementation/issues/203)_)
* Support and prefer exported targets from rmw implementations ([#201 ](https://github.com/ros2/rmw_implementation/issues/201)_)
* Add client/service QoS getters. ([#196 ](https://github.com/ros2/rmw_implementation/issues/196)_)
* Update maintainers to Audrow Nash and Michael Carroll. ([#199 ](https://github.com/ros2/rmw_implementation/issues/199)_)
* Fix renamed [`rcpputils`` header (`#198 ](https://github.com/ros2/rmw_implementation/issues/198)_)
* Fix rmw_implementation generated documentation ([#197 ](https://github.com/ros2/rmw_implementation/issues/197)_)
* Add rmw_publisher_wait_for_all_acked. ([#188 ](https://github.com/ros2/rmw_implementation/issues/188)_)
* Attempt to load any available RMW implementation. ([#189 ](https://github.com/ros2/rmw_implementation/issues/189)_)
* Update includes after rcutils/get_env.h deprecation ([#190 ](https://github.com/ros2/rmw_implementation/issues/190)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Chen Lihui, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Michel Hidalgo, Shane Loretz, iRobot ROS, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rmw_implementation_cmake <https://github.com/ros2/rmw/tree/humble/rmw_implementation_cmake/CHANGELOG.rst>`__

* Use FastDDS as default DDS ([#315 ](https://github.com/ros2/rmw/issues/315)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `robot_state_publisher <https://github.com/ros/robot_state_publisher/tree/humble/CHANGELOG.rst>`__

* Depend on orocos_kdl_vendor ([#191 ](https://github.com/ros/robot_state_publisher/issues/191)_)
* export dependencies, to use robot_state_publisher as a component ([#193 ](https://github.com/ros/robot_state_publisher/issues/193)_)
* Fix include order for cpplint ([#186 ](https://github.com/ros/robot_state_publisher/issues/186)_)
* Change how parameter updates are handled ([#180 ](https://github.com/ros/robot_state_publisher/issues/180)_)
* Install includes to instal/${PROJECT_NAME} ([#184 ](https://github.com/ros/robot_state_publisher/issues/184)_)
* Make the change_fixed_joint test more robust ([#183 ](https://github.com/ros/robot_state_publisher/issues/183)_)
* Add in a test to make sure fixed transforms change on update
* Small C++ nice-isms in the tests
* Switch to using target_include_directories for tests
* Publish new fixed transforms when URDF is updated
* Make joint_states subscription QoS configurable; default to SensorDataQoS ([#179 ](https://github.com/ros/robot_state_publisher/issues/179)_)
* Remove dependency on urdfdom_headers ([#168 ](https://github.com/ros/robot_state_publisher/issues/168)_)
* Fix deprecated subscriber callbacks ([#173 ](https://github.com/ros/robot_state_publisher/issues/173)_)
* Cleanup the documentation in the RobotStatePublisher class. ([#172 ](https://github.com/ros/robot_state_publisher/issues/172)_)
* Always publish fixed frames to /tf_static ([#158 ](https://github.com/ros/robot_state_publisher/issues/158)_)
* corrected publish_frequency default in README ([#166 ](https://github.com/ros/robot_state_publisher/issues/166)_)
* Add tf frame_prefix parameter ([#159 ](https://github.com/ros/robot_state_publisher/issues/159)_)
* Contributors: Abrar Rahman Protyasha, Anthony Deschamps, Chris Lalancette, Jacob Perron, Kenji Brameld, Nils Schulte, Russell Joyce, Shane Loretz, Steve Nogar


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2action <https://github.com/ros2/ros2cli/tree/humble/ros2action/CHANGELOG.rst>`__

* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Depend on launch packages instead of ros_testing to avoid circular dependency ([#685 ](https://github.com/ros2/ros2cli/issues/685)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2bag <https://github.com/ros2/rosbag2/tree/humble/ros2bag/CHANGELOG.rst>`__

* support to publish as loaned message ([#981 ](https://github.com/ros2/rosbag2/issues/981)_)
* Revert "Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)" ([#984 ](https://github.com/ros2/rosbag2/issues/984)_)
* Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)
* support to publish as loaned message ([#981 ](https://github.com/ros2/rosbag2/issues/981)_)
* Revert "Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)" ([#984 ](https://github.com/ros2/rosbag2/issues/984)_)
* Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)
* Bump version number to avoid conflict
* Make sure published messages are acknowledged for play mode ([#951 ](https://github.com/ros2/rosbag2/issues/951)_)
* TopicFilter use regex_search instead of regex_match ([#932 ](https://github.com/ros2/rosbag2/issues/932)_)
* Add start-offset play option ([#931 ](https://github.com/ros2/rosbag2/issues/931)_)
* Expose bag_rewrite as [`ros2 bag convert`` (`#921 ](https://github.com/ros2/rosbag2/issues/921)_)
* Add "ignore leaf topics" option to recorder ([#925 ](https://github.com/ros2/rosbag2/issues/925)_)
* Auto-detect storage_id for Reader (if possible) ([#918 ](https://github.com/ros2/rosbag2/issues/918)_)
* Add pause/resume options to the bag recorder ([#905 ](https://github.com/ros2/rosbag2/issues/905)_)
* Add --start-paused option to [`ros2 bag play`` (`#904 ](https://github.com/ros2/rosbag2/issues/904)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Fix converter plugin choices for record ([#897 ](https://github.com/ros2/rosbag2/issues/897)_)
* Add missing spaces to error message ([#875 ](https://github.com/ros2/rosbag2/issues/875)_)
* keyboard controls for pause/resume toggle and play-next: ([#847 ](https://github.com/ros2/rosbag2/issues/847)_)
* Add --snapshot-mode argument to the "record" verb ([#851 ](https://github.com/ros2/rosbag2/issues/851)_)
* Refactor plugin query mechanism and standardize trait management ([#833 ](https://github.com/ros2/rosbag2/issues/833)_)
* Update [`PlayOptions::delay`` to ``rclcpp::Duration`` to get nanosecond resolution (`#843 ](https://github.com/ros2/rosbag2/issues/843)_)
* Load compression and serialization choices via plugin query ([#827 ](https://github.com/ros2/rosbag2/issues/827)_)
* Add delay option ([#789 ](https://github.com/ros2/rosbag2/issues/789)_)
* Avoid passing exception KeyboardInterrupt to the upper layer ([#788 ](https://github.com/ros2/rosbag2/issues/788)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Cameron Miller, Chris Lalancette, Emerson Knapp, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Kosuke Takeuchi, Michel Hidalgo, Sonia Jin, Tony Peng


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2cli <https://github.com/ros2/ros2cli/tree/humble/ros2cli/CHANGELOG.rst>`__

* Fix importlib_metadata warning on Python 3.10. ([#706 ](https://github.com/ros2/ros2cli/issues/706)_)
* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Use try_shutdown() instead of shutdown() in DirectNode.__exit_\_() ([#683 ](https://github.com/ros2/ros2cli/issues/683)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Reapply [#659 ](https://github.com/ros2/ros2cli/issues/659)_ ([#661 ](https://github.com/ros2/ros2cli/issues/661)_)
* Revert "Make the ros2cli output always line buffered ([#659 ](https://github.com/ros2/ros2cli/issues/659)_)" ([#660 ](https://github.com/ros2/ros2cli/issues/660)_)
* Make the ros2cli output always line buffered ([#659 ](https://github.com/ros2/ros2cli/issues/659)_)
* add uuid to ros2 daemon node name. ([#658 ](https://github.com/ros2/ros2cli/issues/658)_)
* Transfer daemon socket ownership on spawn. ([#652 ](https://github.com/ros2/ros2cli/issues/652)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Michel Hidalgo, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2cli_test_interfaces <https://github.com/ros2/ros2cli/tree/humble/ros2cli_test_interfaces/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2component <https://github.com/ros2/ros2cli/tree/humble/ros2component/CHANGELOG.rst>`__

* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Drop deprecated get_container_components_info() API. ([#647 ](https://github.com/ros2/ros2cli/issues/647)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2doctor <https://github.com/ros2/ros2cli/tree/humble/ros2doctor/CHANGELOG.rst>`__

* Fix importlib_metadata warning on Python 3.10. ([#706 ](https://github.com/ros2/ros2cli/issues/706)_)
* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Switch ros2 doctor to using psutil for network checks. ([#687 ](https://github.com/ros2/ros2cli/issues/687)_)
* Depend on launch packages instead of ros_testing to avoid circular dependency ([#685 ](https://github.com/ros2/ros2cli/issues/685)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Improve ros2 doctor on Windows. ([#631 ](https://github.com/ros2/ros2cli/issues/631)_)
* Add QoS compatibility check and report. ([#621 ](https://github.com/ros2/ros2cli/issues/621)_)
* Contributors: Aditya Pande, Alberto Soragna, Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2interface <https://github.com/ros2/ros2cli/tree/humble/ros2interface/CHANGELOG.rst>`__

* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Depend on launch packages instead of ros_testing to avoid circular dependency ([#685 ](https://github.com/ros2/ros2cli/issues/685)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2launch <https://github.com/ros2/launch_ros/tree/humble/ros2launch/CHANGELOG.rst>`__

* Update maintainers in setup.py ([#287 ](https://github.com/ros2/launch_ros/issues/287)_)
* Use frontend group dependency & explicit dependencies in ros2launch ([#256 ](https://github.com/ros2/launch_ros/issues/256)_)
* Update package maintainers ([#284 ](https://github.com/ros2/launch_ros/issues/284)_)
* Add regex filter for selective launch-prefix application ([#261 ](https://github.com/ros2/launch_ros/issues/261)_)
* Resolves [#37 ](https://github.com/ros2/launch_ros/issues/37)_ - Added --launch-prefix argument for 'ros2 launch' command ([#254 ](https://github.com/ros2/launch_ros/issues/254)_)
* Use sets of file extensions provided by parser extensions ([#252 ](https://github.com/ros2/launch_ros/issues/252)_)
* Simplify logic to fix absolute paths ([#230 ](https://github.com/ros2/launch_ros/issues/230)_)
* add way to include other Python launch files ([launch #122 ](https://github.com/ros2/launch/issues/122)_)
* Contributors: Audrow Nash, Cameron Miller, Christophe Bedard, Michel Hidalgo, rob-clarke


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2lifecycle <https://github.com/ros2/ros2cli/tree/humble/ros2lifecycle/CHANGELOG.rst>`__

* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Depend on launch packages instead of ros_testing to avoid circular dependency ([#685 ](https://github.com/ros2/ros2cli/issues/685)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2lifecycle_test_fixtures <https://github.com/ros2/ros2cli/tree/humble/ros2lifecycle_test_fixtures/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2multicast <https://github.com/ros2/ros2cli/tree/humble/ros2multicast/CHANGELOG.rst>`__

* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2node <https://github.com/ros2/ros2cli/tree/humble/ros2node/CHANGELOG.rst>`__

* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Depend on launch packages instead of ros_testing to avoid circular dependency ([#685 ](https://github.com/ros2/ros2cli/issues/685)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2param <https://github.com/ros2/ros2cli/tree/humble/ros2param/CHANGELOG.rst>`__

* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Fix how ros2 param interprets command-line arguments. ([#684 ](https://github.com/ros2/ros2cli/issues/684)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Removed redundant code ([#666 ](https://github.com/ros2/ros2cli/issues/666)_)
* Reapply [#659 ](https://github.com/ros2/ros2cli/issues/659)_ ([#661 ](https://github.com/ros2/ros2cli/issues/661)_)
* Fix flaky ros2 param list ([#656 ](https://github.com/ros2/ros2cli/issues/656)_)
* Skip None Result ([#646 ](https://github.com/ros2/ros2cli/issues/646)_)
* add '--write' option to avoid an unintentional data loss. ([#638 ](https://github.com/ros2/ros2cli/issues/638)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Jacob Perron, Jay Wang, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2pkg <https://github.com/ros2/ros2cli/tree/humble/ros2pkg/CHANGELOG.rst>`__

* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Use local git config instead of global ([#693 ](https://github.com/ros2/ros2cli/issues/693)_)
* Depend on launch packages instead of ros_testing to avoid circular dependency ([#685 ](https://github.com/ros2/ros2cli/issues/685)_)
* [ros2pkg] Skip copyright tests in template packages ([#676 ](https://github.com/ros2/ros2cli/issues/676)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Generate LICENSE files on ros2 pkg create. ([#650 ](https://github.com/ros2/ros2cli/issues/650)_)
* Handle ValueError ([#643 ](https://github.com/ros2/ros2cli/issues/643)_)
* Pass package exports to template in pkg create api ([#619 ](https://github.com/ros2/ros2cli/issues/619)_) ([#628 ](https://github.com/ros2/ros2cli/issues/628)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Abrar Rahman Protyasha, Aditya Pande, Amro Al-Baali, Audrow Nash, Chris Lalancette, Ivan Santiago Paunovic, Shane Loretz, rob-clarke, tim-fan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2run <https://github.com/ros2/ros2cli/tree/humble/ros2run/CHANGELOG.rst>`__

* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* check subprocess.returncode to print error message. ([#639 ](https://github.com/ros2/ros2cli/issues/639)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2service <https://github.com/ros2/ros2cli/tree/humble/ros2service/CHANGELOG.rst>`__

* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Also provide --include-hidden-services for [`ros2 service list`` verb (`#551 ](https://github.com/ros2/ros2cli/issues/551)_)
* Depend on launch packages instead of ros_testing to avoid circular dependency ([#685 ](https://github.com/ros2/ros2cli/issues/685)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* Contributors: Aditya Pande, Audrow Nash, Ivan Santiago Paunovic, Karsten Knese, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2test <https://github.com/ros2/ros_testing/tree/humble/ros2test/CHANGELOG.rst>`__

* Use new domain_coordinator API ([#10 ](https://github.com/ros2/ros_testing/issues/10)_)
* Contributors: Timo Röhling


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2topic <https://github.com/ros2/ros2cli/tree/humble/ros2topic/CHANGELOG.rst>`__

* Add timeout to kill hanging tests ([#701 ](https://github.com/ros2/ros2cli/issues/701)_)
* Add yaml dump flow style. ([#698 ](https://github.com/ros2/ros2cli/issues/698)_)
* support ros2topic echo once option. ([#695 ](https://github.com/ros2/ros2cli/issues/695)_)
* Fix special case for fastrtps incompatible QoS. ([#694 ](https://github.com/ros2/ros2cli/issues/694)_)
* Depend on launch packages instead of ros_testing to avoid circular dependency ([#685 ](https://github.com/ros2/ros2cli/issues/685)_)
* Add QoS history and depth information if available. ([#678 ](https://github.com/ros2/ros2cli/issues/678)_)
* Cleanup mislabeled BSD license ([#447 ](https://github.com/ros2/ros2cli/issues/447)_)
* Update maintainers to Aditya Pande, Audrow Nash, and Michael Jeronimo ([#673 ](https://github.com/ros2/ros2cli/issues/673)_)
* Updated maintainers ([#670 ](https://github.com/ros2/ros2cli/issues/670)_)
* Update lost messages test case ([#669 ](https://github.com/ros2/ros2cli/issues/669)_)
* Implementation of message filtering for ros2 ([#654 ](https://github.com/ros2/ros2cli/issues/654)_)
* Change default QoSProfile for pub ([#653 ](https://github.com/ros2/ros2cli/issues/653)_)
* Add option in ros2 topic pub to wait for N matching subscriptions, use N=1 by default when combined with --times ([#642 ](https://github.com/ros2/ros2cli/issues/642)_)
* [`ros2 topic pub`` starts publishing right away. (`#626 ](https://github.com/ros2/ros2cli/issues/626)_)
* Fix Topic Info Test with "Infinite" printing ([#616 ](https://github.com/ros2/ros2cli/issues/616)_)
* Add changelogs ([#635 ](https://github.com/ros2/ros2cli/issues/635)_)
* QoS autodetection ([#613 ](https://github.com/ros2/ros2cli/issues/613)_)
* Make Lost Messages option ON by default ([#633 ](https://github.com/ros2/ros2cli/issues/633)_)
* Contributors: Aditya Pande, Audrow Nash, Chris Lalancette, Emerson Knapp, Gonzo, Ivan Santiago Paunovic, Jorge Perez, Shane Loretz, Tomoya Fujita, Tully Foote, matthews-jca


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `ros2trace <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/ros2trace/CHANGELOG.rst>`__

* Fix 'ros2 trace' fini() error
* Don't require kernel tracer and detect when it's not installed
* Deprecate 'context_names' param and replace with 'context_fields'
* Contributors: Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2 <https://github.com/ros2/rosbag2/tree/humble/rosbag2/CHANGELOG.rst>`__

* Bump version number to avoid conflict
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Contributors: Chris Lalancette, Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_compression <https://github.com/ros2/rosbag2/tree/humble/rosbag2_compression/CHANGELOG.rst>`__

* Bump version number to avoid conflict
* Install headers to include/${PROJECT_NAME} ([#958 ](https://github.com/ros2/rosbag2/issues/958)_)
* Remove unnecessary public definition. ([#950 ](https://github.com/ros2/rosbag2/issues/950)_)
* Changes for uncrustify 0.72 ([#937 ](https://github.com/ros2/rosbag2/issues/937)_)
* Bugfix for broken bag split when using cache ([#936 ](https://github.com/ros2/rosbag2/issues/936)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Don't preprocess a storage file more than once ([#895 ](https://github.com/ros2/rosbag2/issues/895)_)
* added seek interface ([#836 ](https://github.com/ros2/rosbag2/issues/836)_)
* Refactor plugin query mechanism and standardize trait management ([#833 ](https://github.com/ros2/rosbag2/issues/833)_)
* fix sequential reader rollover-to-next-file strategy: ([#839 ](https://github.com/ros2/rosbag2/issues/839)_)
* Load compression and serialization choices via plugin query ([#827 ](https://github.com/ros2/rosbag2/issues/827)_)
* Contributors: Cameron Miller, Chris Lalancette, Michael Orlov, Michel Hidalgo, Shane Loretz, sonia


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_compression_zstd <https://github.com/ros2/rosbag2/tree/humble/rosbag2_compression_zstd/CHANGELOG.rst>`__

* Bump version number to avoid conflict
* Install headers to include/${PROJECT_NAME} ([#958 ](https://github.com/ros2/rosbag2/issues/958)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Contributors: Chris Lalancette, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_cpp <https://github.com/ros2/rosbag2/tree/humble/rosbag2_cpp/CHANGELOG.rst>`__

* Revert "Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)" ([#984 ](https://github.com/ros2/rosbag2/issues/984)_)
* Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)
* Revert "Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)" ([#984 ](https://github.com/ros2/rosbag2/issues/984)_)
* Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)
* Bump version number to avoid conflict
* Install headers to include/${PROJECT_NAME} ([#958 ](https://github.com/ros2/rosbag2/issues/958)_)
* Remove unnecessary public definition. ([#950 ](https://github.com/ros2/rosbag2/issues/950)_)
* Fix relative path syntax for cpplint ([#947 ](https://github.com/ros2/rosbag2/issues/947)_)
* Mark up the message_cache with TSA annotations ([#946 ](https://github.com/ros2/rosbag2/issues/946)_)
* Changes for uncrustify 0.72 ([#937 ](https://github.com/ros2/rosbag2/issues/937)_)
* Redesign in cache consumer and circular message cache to get rid from busy loop ([#941 ](https://github.com/ros2/rosbag2/issues/941)_)
* Bugfix for broken bag split when using cache ([#936 ](https://github.com/ros2/rosbag2/issues/936)_)
* Remove JumpHandler copy-implementation from PlayerClock/TimeControllerClock ([#935 ](https://github.com/ros2/rosbag2/issues/935)_)
* Auto-detect storage_id for Reader (if possible) ([#918 ](https://github.com/ros2/rosbag2/issues/918)_)
* Add --start-paused option to [`ros2 bag play`` (`#904 ](https://github.com/ros2/rosbag2/issues/904)_)
* Use the message_introspection header to get MessageMember. ([#903 ](https://github.com/ros2/rosbag2/issues/903)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Fix converter plugin choices for record ([#897 ](https://github.com/ros2/rosbag2/issues/897)_)
* Enable sanitizers only if code actually can run ([#572 ](https://github.com/ros2/rosbag2/issues/572)_)
* Need to pass introspection TS to converter plugin for it to be useful ([#896 ](https://github.com/ros2/rosbag2/issues/896)_)
* Don't preprocess a storage file more than once ([#895 ](https://github.com/ros2/rosbag2/issues/895)_)
* Fix a bug on invalid pointer address when using "MESSAGE" compressio… ([#866 ](https://github.com/ros2/rosbag2/issues/866)_)
* Metadata per file info ([#870 ](https://github.com/ros2/rosbag2/issues/870)_)
* Fix TSA warnings when building with clang thread analysis. ([#877 ](https://github.com/ros2/rosbag2/issues/877)_)
* Implement snapshot mechanism and corresponding ROS Service ([#850 ](https://github.com/ros2/rosbag2/issues/850)_)
* Circular Message Cache implementation for snapshot feature ([#844 ](https://github.com/ros2/rosbag2/issues/844)_)
* Fix discovery silently stops after unknown msg type is found. ([#848 ](https://github.com/ros2/rosbag2/issues/848)_)
* added seek interface ([#836 ](https://github.com/ros2/rosbag2/issues/836)_)
* Refactor plugin query mechanism and standardize trait management ([#833 ](https://github.com/ros2/rosbag2/issues/833)_)
* fix sequential reader rollover-to-next-file strategy: ([#839 ](https://github.com/ros2/rosbag2/issues/839)_)
* Load compression and serialization choices via plugin query ([#827 ](https://github.com/ros2/rosbag2/issues/827)_)
* Workaround for false positive findings by clang thread safety analysis in time controller jump callbacks API. ([#799 ](https://github.com/ros2/rosbag2/issues/799)_)
* Add callbacks for PlayerClock::jump(time_point) API with CI fix ([#779 ](https://github.com/ros2/rosbag2/issues/779)_)
* Revert "Add callbacks for PlayerClock::jump(time_point) API ([#775 ](https://github.com/ros2/rosbag2/issues/775)_)" ([#778 ](https://github.com/ros2/rosbag2/issues/778)_)
* Add callbacks for PlayerClock::jump(time_point) API ([#775 ](https://github.com/ros2/rosbag2/issues/775)_)
* Contributors: Audrow Nash, Barry Xu, Cameron Miller, Chris Lalancette, Emerson Knapp, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Lei Liu, Michael Orlov, Michel Hidalgo, Shane Loretz, Tony Peng, Wojciech Jaworski, sonia


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_interfaces <https://github.com/ros2/rosbag2/tree/humble/rosbag2_interfaces/CHANGELOG.rst>`__

* Bump version number to avoid conflict
* Add burst-mode to Player ([#977 ](https://github.com/ros2/rosbag2/issues/977)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Implement snapshot mechanism and corresponding ROS Service ([#850 ](https://github.com/ros2/rosbag2/issues/850)_) * Add snapshot service to recorder node * Simplify and clarify double buffering patterns
* Contributors: Cameron Miller, Chris Lalancette, Geoffrey Biggs, Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_performance_benchmarking <https://github.com/ros2/rosbag2/tree/humble/rosbag2_performance/rosbag2_performance_benchmarking/CHANGELOG.rst>`__

* Bump version number to avoid conflict
* Install headers to include/${PROJECT_NAME} ([#958 ](https://github.com/ros2/rosbag2/issues/958)_)
* Enable YAML encoding/decoding for RecordOptions and StorageOptions ([#916 ](https://github.com/ros2/rosbag2/issues/916)_) * Enable YAML encoding/decoding for RecordOptions and StorageOptions
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Updated node declare_parameter to new syntax ([#882 ](https://github.com/ros2/rosbag2/issues/882)_)
* Updated benchmark package to use writer close() instead of old reset() ([#881 ](https://github.com/ros2/rosbag2/issues/881)_)
* Contributors: Adam Dąbrowski, Chris Lalancette, Emerson Knapp, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_py <https://github.com/ros2/rosbag2/tree/humble/rosbag2_py/CHANGELOG.rst>`__

* support to publish as loaned message ([#981 ](https://github.com/ros2/rosbag2/issues/981)_)
* Revert "Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)" ([#984 ](https://github.com/ros2/rosbag2/issues/984)_)
* Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)
* support to publish as loaned message ([#981 ](https://github.com/ros2/rosbag2/issues/981)_)
* Revert "Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)" ([#984 ](https://github.com/ros2/rosbag2/issues/984)_)
* Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)
* Bump version number to avoid conflict
* Make sure published messages are acknowledged for play mode ([#951 ](https://github.com/ros2/rosbag2/issues/951)_)
* Fix relative path syntax for cpplint ([#947 ](https://github.com/ros2/rosbag2/issues/947)_)
* Update to pybind11 2.7.1 ([#945 ](https://github.com/ros2/rosbag2/issues/945)_)
* Add start-offset play option ([#931 ](https://github.com/ros2/rosbag2/issues/931)_)
* Expose bag_rewrite as [`ros2 bag convert`` (`#921 ](https://github.com/ros2/rosbag2/issues/921)_)
* Add "ignore leaf topics" option to recorder ([#925 ](https://github.com/ros2/rosbag2/issues/925)_)
* Add a ReaderWriterFactory utility to share logic for reuse ([#923 ](https://github.com/ros2/rosbag2/issues/923)_)
* Add pause/resume options to the bag recorder ([#905 ](https://github.com/ros2/rosbag2/issues/905)_)
* Add --start-paused option to [`ros2 bag play`` (`#904 ](https://github.com/ros2/rosbag2/issues/904)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Fix converter plugin choices for record ([#897 ](https://github.com/ros2/rosbag2/issues/897)_)
* Metadata per file info ([#870 ](https://github.com/ros2/rosbag2/issues/870)_)
* keyboard controls for pause/resume toggle and play-next: ([#847 ](https://github.com/ros2/rosbag2/issues/847)_)
* Add --snapshot-mode argument to the "record" verb ([#851 ](https://github.com/ros2/rosbag2/issues/851)_)
* Add stopRecording into rosbag2_py ([#854 ](https://github.com/ros2/rosbag2/issues/854)_)
* added seek interface ([#836 ](https://github.com/ros2/rosbag2/issues/836)_)
* Refactor plugin query mechanism and standardize trait management ([#833 ](https://github.com/ros2/rosbag2/issues/833)_)
* Update [`PlayOptions::delay`` to ``rclcpp::Duration`` to get nanosecond resolution (`#843 ](https://github.com/ros2/rosbag2/issues/843)_)
* Load compression and serialization choices via plugin query ([#827 ](https://github.com/ros2/rosbag2/issues/827)_)
* Add delay option ([#789 ](https://github.com/ros2/rosbag2/issues/789)_)
* Handle SIGTERM gracefully in recording ([#792 ](https://github.com/ros2/rosbag2/issues/792)_)
* Contributors: Abrar Rahman Protyasha, Afonso da Fonseca Braga, Audrow Nash, Barry Xu, Cameron Miller, Chris Lalancette, Emerson Knapp, Ivan Santiago Paunovic, Jacob Perron, Jorge Perez, Kosuke Takeuchi, Michel Hidalgo, Tony Peng, Wojciech Jaworski, sonia


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_storage <https://github.com/ros2/rosbag2/tree/humble/rosbag2_storage/CHANGELOG.rst>`__

* Revert "Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)" ([#984 ](https://github.com/ros2/rosbag2/issues/984)_)
* Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)
* Revert "Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)" ([#984 ](https://github.com/ros2/rosbag2/issues/984)_)
* Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)
* Bump version number to avoid conflict
* Install headers to include/${PROJECT_NAME} ([#958 ](https://github.com/ros2/rosbag2/issues/958)_)
* Remove unnecessary public definition. ([#950 ](https://github.com/ros2/rosbag2/issues/950)_)
* Enable YAML encoding/decoding for RecordOptions and StorageOptions ([#916 ](https://github.com/ros2/rosbag2/issues/916)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Provide MetadataIO interface to convert metadata to a string in memory, alongside file IO versions ([#894 ](https://github.com/ros2/rosbag2/issues/894)_)
* Metadata per file info ([#870 ](https://github.com/ros2/rosbag2/issues/870)_)
* Implement snapshot mechanism and corresponding ROS Service ([#850 ](https://github.com/ros2/rosbag2/issues/850)_)
* added seek interface ([#836 ](https://github.com/ros2/rosbag2/issues/836)_)
* Refactor plugin query mechanism and standardize trait management ([#833 ](https://github.com/ros2/rosbag2/issues/833)_)
* Contributors: Audrow Nash, Cameron Miller, Chris Lalancette, Emerson Knapp, Jorge Perez, Michel Hidalgo, Shane Loretz, Tony Peng, Wojciech Jaworski, sonia


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_storage_default_plugins <https://github.com/ros2/rosbag2/tree/humble/rosbag2_storage_default_plugins/CHANGELOG.rst>`__

* Bump version number to avoid conflict
* Install headers to include/${PROJECT_NAME} ([#958 ](https://github.com/ros2/rosbag2/issues/958)_)
* Emit a warning rather than crash when a message is too big for sqlite ([#919 ](https://github.com/ros2/rosbag2/issues/919)_)
* Enable YAML encoding/decoding for RecordOptions and StorageOptions ([#916 ](https://github.com/ros2/rosbag2/issues/916)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* added seek interface ([#836 ](https://github.com/ros2/rosbag2/issues/836)_)
* Contributors: Chris Lalancette, Emerson Knapp, Michel Hidalgo, Shane Loretz, William Woodall, sonia


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_test_common <https://github.com/ros2/rosbag2/tree/humble/rosbag2_test_common/CHANGELOG.rst>`__

* Bump version number to avoid conflict
* Install headers to include/${PROJECT_NAME} ([#958 ](https://github.com/ros2/rosbag2/issues/958)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Make sure the subscription exists before publishing messages ([#804 ](https://github.com/ros2/rosbag2/issues/804)_)
* Handle SIGTERM gracefully in recording ([#792 ](https://github.com/ros2/rosbag2/issues/792)_)
* Add spin_and_wait_for_matched to PublicationManager and update test c… ([#797 ](https://github.com/ros2/rosbag2/issues/797)_)
* Avoid passing exception KeyboardInterrupt to the upper layer ([#788 ](https://github.com/ros2/rosbag2/issues/788)_)
* Contributors: Barry Xu, Chris Lalancette, Emerson Knapp, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_tests <https://github.com/ros2/rosbag2/tree/humble/rosbag2_tests/CHANGELOG.rst>`__

* Revert "Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)" ([#984 ](https://github.com/ros2/rosbag2/issues/984)_)
* Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)
* Revert "Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)" ([#984 ](https://github.com/ros2/rosbag2/issues/984)_)
* Add the ability to record any key/value pair in the 'custom' field in metadata.yaml ([#976 ](https://github.com/ros2/rosbag2/issues/976)_)
* Bump version number to avoid conflict
* Add pause/resume options to the bag recorder ([#905 ](https://github.com/ros2/rosbag2/issues/905)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Fix a bug on invalid pointer address when using "MESSAGE" compressio… ([#866 ](https://github.com/ros2/rosbag2/issues/866)_)
* Metadata per file info ([#870 ](https://github.com/ros2/rosbag2/issues/870)_)
* Fix record test to reflect plugin query changes ([#838 ](https://github.com/ros2/rosbag2/issues/838)_)
* Make sure the subscription exists before publishing messages ([#804 ](https://github.com/ros2/rosbag2/issues/804)_)
* Handle SIGTERM gracefully in recording ([#792 ](https://github.com/ros2/rosbag2/issues/792)_)
* Add spin_and_wait_for_matched to PublicationManager and update test c… ([#797 ](https://github.com/ros2/rosbag2/issues/797)_)
* Remove rmw_fastrtps_cpp find_package in rosbag2_tests ([#774 ](https://github.com/ros2/rosbag2/issues/774)_)
* Contributors: Audrow Nash, Barry Xu, Cameron Miller, Chris Lalancette, Emerson Knapp, Ivan Santiago Paunovic, Jorge Perez, Michel Hidalgo, Tony Peng, Wojciech Jaworski


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosbag2_transport <https://github.com/ros2/rosbag2/tree/humble/rosbag2_transport/CHANGELOG.rst>`__

* support to publish as loaned message ([#981 ](https://github.com/ros2/rosbag2/issues/981)_)
* support to publish as loaned message ([#981 ](https://github.com/ros2/rosbag2/issues/981)_)
* Bump version number to avoid conflict
* Add burst-mode to Player ([#977 ](https://github.com/ros2/rosbag2/issues/977)_)
* Install headers to include/${PROJECT_NAME} ([#958 ](https://github.com/ros2/rosbag2/issues/958)_)
* Make sure published messages are acknowledged for play mode ([#951 ](https://github.com/ros2/rosbag2/issues/951)_)
* Changes for uncrustify 0.72 ([#937 ](https://github.com/ros2/rosbag2/issues/937)_)
* TopicFilter use regex_search instead of regex_match ([#932 ](https://github.com/ros2/rosbag2/issues/932)_)
* Add start-offset play option ([#931 ](https://github.com/ros2/rosbag2/issues/931)_)
* Add parentheses suggested by Clang on OSX to fix build warning ([#930 ](https://github.com/ros2/rosbag2/issues/930)_)
* Bag rewriter (C++) ([#920 ](https://github.com/ros2/rosbag2/issues/920)_)
* Add "ignore leaf topics" option to recorder ([#925 ](https://github.com/ros2/rosbag2/issues/925)_)
* Rewrite TopicFilter for single-call reusability ([#924 ](https://github.com/ros2/rosbag2/issues/924)_)
* Add a ReaderWriterFactory utility to share logic for reuse ([#923 ](https://github.com/ros2/rosbag2/issues/923)_)
* Add pause/resume options to the bag recorder ([#905 ](https://github.com/ros2/rosbag2/issues/905)_)
* Add logging macros for rosbag2_transport ([#917 ](https://github.com/ros2/rosbag2/issues/917)_)
* Enable YAML encoding/decoding for RecordOptions and StorageOptions ([#916 ](https://github.com/ros2/rosbag2/issues/916)_)
* Expose the QoS object wrapper ([#910 ](https://github.com/ros2/rosbag2/issues/910)_)
* Add --start-paused option to [`ros2 bag play`` (`#904 ](https://github.com/ros2/rosbag2/issues/904)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Add a Seek service ([#874 ](https://github.com/ros2/rosbag2/issues/874)_)
* Add simple keyboard control for playback rate ([#893 ](https://github.com/ros2/rosbag2/issues/893)_)
* Fix a bug on invalid pointer address when using "MESSAGE" compressio… ([#866 ](https://github.com/ros2/rosbag2/issues/866)_)
* Fix typo ([#880 ](https://github.com/ros2/rosbag2/issues/880)_)
* Use Reader's seek() method for seeking/jumping in Player ([#873 ](https://github.com/ros2/rosbag2/issues/873)_)
* keyboard controls for pause/resume toggle and play-next: ([#847 ](https://github.com/ros2/rosbag2/issues/847)_)
* Implement snapshot mechanism and corresponding ROS Service ([#850 ](https://github.com/ros2/rosbag2/issues/850)_)
* Circular Message Cache implementation for snapshot feature ([#844 ](https://github.com/ros2/rosbag2/issues/844)_)
* Add jump/seek API for Player class ([#826 ](https://github.com/ros2/rosbag2/issues/826)_)
* Restructure test_play_timing to one test per case, to see which times out ([#863 ](https://github.com/ros2/rosbag2/issues/863)_)
* Fix discovery silently stops after unknown msg type is found. ([#848 ](https://github.com/ros2/rosbag2/issues/848)_)
* Fixing deprecated subscriber callback warnings ([#852 ](https://github.com/ros2/rosbag2/issues/852)_)
* Bugfix for race condition in Player::peek_next_message_from_queue() ([#849 ](https://github.com/ros2/rosbag2/issues/849)_)
* added seek interface ([#836 ](https://github.com/ros2/rosbag2/issues/836)_)
* Update [`PlayOptions::delay`` to ``rclcpp::Duration`` to get nanosecond resolution (`#843 ](https://github.com/ros2/rosbag2/issues/843)_)
* Move notification about ready for playback inside play_messages_from_queue() ([#832 ](https://github.com/ros2/rosbag2/issues/832)_)
* Add wait for player to be ready for playback in Player::play_next() method ([#814 ](https://github.com/ros2/rosbag2/issues/814)_)
* Make sure the subscription exists before publishing messages ([#804 ](https://github.com/ros2/rosbag2/issues/804)_)
* Add delay option ([#789 ](https://github.com/ros2/rosbag2/issues/789)_)
* Copy recorder QoS profile to local variable so that temporary value isn't cleared ([#803 ](https://github.com/ros2/rosbag2/issues/803)_)
* test_play_services: fail gracefully on future error ([#798 ](https://github.com/ros2/rosbag2/issues/798)_)
* Recording with --all and --exclude fix ([#765 ](https://github.com/ros2/rosbag2/issues/765)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Barry Xu, Bastian Jäger, Cameron Miller, Chris Lalancette, Emerson Knapp, Geoffrey Biggs, Ivan Santiago Paunovic, Kosuke Takeuchi, Lei Liu, Louise Poubel, Michael Orlov, Michel Hidalgo, Piotr Jaroszek, Shane Loretz, sonia


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosgraph_msgs <https://github.com/ros2/rcl_interfaces/tree/humble/rosgraph_msgs/CHANGELOG.rst>`__

* Update maintainers to Chris Lalancette ([#130 ](https://github.com/ros2/rcl_interfaces/issues/130)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_adapter <https://github.com/ros2/rosidl/tree/humble/rosidl_adapter/CHANGELOG.rst>`__

* rename nested loop index ([#643 ](https://github.com/ros2/rosidl/issues/643)_)
* Fix how comments in action interfaces are processed ([#632 ](https://github.com/ros2/rosidl/issues/632)_)
* Pass comments in ros interface constants to the .idl generated files ([#630 ](https://github.com/ros2/rosidl/issues/630)_)
* Update package maintainers ([#624 ](https://github.com/ros2/rosidl/issues/624)_)
* Make rosidl packages use FindPython3 instead of FindPythonInterp ([#612 ](https://github.com/ros2/rosidl/issues/612)_)
* Fix escaping in string literals ([#595 ](https://github.com/ros2/rosidl/issues/595)_)
* Ignore multiple [`#`` characters and dedent comments (`#594 ](https://github.com/ros2/rosidl/issues/594)_)
* Contributors: Ivan Santiago Paunovic, Michel Hidalgo, Shane Loretz, ibnHatab


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_cli <https://github.com/ros2/rosidl/tree/humble/rosidl_cli/CHANGELOG.rst>`__

* Fix importlib_metdata warning with Python 3.10. ([#674 ](https://github.com/ros2/rosidl/issues/674)_)
* Update maintainers to Michel Hidalgo and Shane Loretz ([#633 ](https://github.com/ros2/rosidl/issues/633)_)
* Update package maintainers ([#624 ](https://github.com/ros2/rosidl/issues/624)_)
* Support passing keyword arguments to rosidl CLI extensions ([#597 ](https://github.com/ros2/rosidl/issues/597)_)
* Add missing f for format string ([#600 ](https://github.com/ros2/rosidl/issues/600)_)
* Contributors: Audrow Nash, Chris Lalancette, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_cmake <https://github.com/ros2/rosidl/tree/humble/rosidl_cmake/CHANGELOG.rst>`__

* Make rosidl_get_typesupport_target return -NOTFOUND instead of FATAL_ERROR ([#672 ](https://github.com/ros2/rosidl/issues/672)_)
* Add introspection typesupport tests for C/C++ messages ([#651 ](https://github.com/ros2/rosidl/issues/651)_)
* Use target output name for exporting typesupport library ([#625 ](https://github.com/ros2/rosidl/issues/625)_)
* Update package maintainers ([#624 ](https://github.com/ros2/rosidl/issues/624)_)
* Revert "Bundle and ensure the exportation of rosidl generated targets" ([#611 ](https://github.com/ros2/rosidl/issues/611)_)
* Add rosidl_get_typesupport_target and deprecate rosidl_target_interfaces ([#606 ](https://github.com/ros2/rosidl/issues/606)_)
* Bundle and ensure the exportation of rosidl generated targets ([#601 ](https://github.com/ros2/rosidl/issues/601)_)
* Contributors: Jonathan Selling, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_default_generators <https://github.com/ros2/rosidl_defaults/tree/humble/rosidl_default_generators/CHANGELOG.rst>`__

* Unroll group dependencies ([#20 ](https://github.com/ros2/rosidl_defaults/issues/20)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_default_runtime <https://github.com/ros2/rosidl_defaults/tree/humble/rosidl_default_runtime/CHANGELOG.rst>`__

* Unroll group dependencies ([#20 ](https://github.com/ros2/rosidl_defaults/issues/20)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_c <https://github.com/ros2/rosidl/tree/humble/rosidl_generator_c/CHANGELOG.rst>`__

* Fix error handling when copying C sequence messages ([#671 ](https://github.com/ros2/rosidl/issues/671)_)
* Install generated headers to include/${PROJECT_NAME} ([#670 ](https://github.com/ros2/rosidl/issues/670)_)
* Misc cleanup in the rosidl generator extensions ([#662 ](https://github.com/ros2/rosidl/issues/662)_)
* Set the output size unconditionally when copying sequences ([#669 ](https://github.com/ros2/rosidl/issues/669)_)
* Implement copy function for C messages ([#650 ](https://github.com/ros2/rosidl/issues/650)_)
* Implement equality operator function for C messages. ([#648 ](https://github.com/ros2/rosidl/issues/648)_)
* Generate documentation in generated C header files based on ROS interfaces comments ([#593 ](https://github.com/ros2/rosidl/issues/593)_)
* Update package maintainers ([#624 ](https://github.com/ros2/rosidl/issues/624)_)
* Make rosidl packages use FindPython3 instead of FindPythonInterp ([#612 ](https://github.com/ros2/rosidl/issues/612)_)
* Revert "Bundle and ensure the exportation of rosidl generated targets" ([#611 ](https://github.com/ros2/rosidl/issues/611)_)
* Bundle and ensure the exportation of rosidl generated targets ([#601 ](https://github.com/ros2/rosidl/issues/601)_)
* Fix a cpplint allocator regression. ([#590 ](https://github.com/ros2/rosidl/issues/590)_)
* Use RCUtils allocators in rosidl_generator_c ([#584 ](https://github.com/ros2/rosidl/issues/584)_)
* Contributors: Chris Lalancette, Ivan Santiago Paunovic, Michel Hidalgo, Nikolai Morin, Pablo Garrido, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_cpp <https://github.com/ros2/rosidl/tree/humble/rosidl_generator_cpp/CHANGELOG.rst>`__

* Install generated headers to include/${PROJECT_NAME} ([#670 ](https://github.com/ros2/rosidl/issues/670)_)
* Misc cleanup in the rosidl generator extensions ([#662 ](https://github.com/ros2/rosidl/issues/662)_)
* Add missing build_export_depend dependency ([#665 ](https://github.com/ros2/rosidl/issues/665)_)
* Fix bug where rosidl_runtime_cpp wasn't depended upon ([#660 ](https://github.com/ros2/rosidl/issues/660)_)
* Fix include order for cpplint ([#644 ](https://github.com/ros2/rosidl/issues/644)_)
* Set CXX standard to 17 ([#635 ](https://github.com/ros2/rosidl/issues/635)_)
* Update package maintainers ([#624 ](https://github.com/ros2/rosidl/issues/624)_)
* Make rosidl packages use FindPython3 instead of FindPythonInterp ([#612 ](https://github.com/ros2/rosidl/issues/612)_)
* Support flow style YAML printing ([#613 ](https://github.com/ros2/rosidl/issues/613)_)
* Revert "Bundle and ensure the exportation of rosidl generated targets" ([#611 ](https://github.com/ros2/rosidl/issues/611)_)
* Relocate to_yaml() under message namespace ([#609 ](https://github.com/ros2/rosidl/issues/609)_)
* Bundle and ensure the exportation of rosidl generated targets ([#601 ](https://github.com/ros2/rosidl/issues/601)_)
* Contributors: Jacob Perron, Jorge Perez, Michel Hidalgo, Shane Loretz, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_dds_idl <https://github.com/ros2/rosidl_dds/tree/humble/rosidl_generator_dds_idl/CHANGELOG.rst>`__

* Add changelog ([#56 ](https://github.com/ros2/rosidl_dds/issues/56)_)
* Contributors: Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_generator_py <https://github.com/ros2/rosidl_python/tree/humble/rosidl_generator_py/CHANGELOG.rst>`__

* Removes erroneous unmatched closing parenthesis ([#125 ](https://github.com/ros2/rosidl_python/issues/125)_)
* require Python 3.6 as we use format strings in various places ([#152 ](https://github.com/ros2/rosidl_python/issues/152)_)
* Fix rosidl_generator_py assuming incorect library names ([#149 ](https://github.com/ros2/rosidl_python/issues/149)_)
* Fix for msg file containing a property field that is not at the end ([#151 ](https://github.com/ros2/rosidl_python/issues/151)_)
* Update package maintainers ([#147 ](https://github.com/ros2/rosidl_python/issues/147)_)
* Use rosidl_get_typesupport_target() ([#139 ](https://github.com/ros2/rosidl_python/issues/139)_)
* Support available typesupport specification in CLI extension ([#133 ](https://github.com/ros2/rosidl_python/issues/133)_)
* Use python_d for test_cli_extension in Debug mode ([#136 ](https://github.com/ros2/rosidl_python/issues/136)_)
* Add missing float/double bounds check ([#128 ](https://github.com/ros2/rosidl_python/issues/128)_)
* Added optimization for copying arrays using buffer protocol ([#129 ](https://github.com/ros2/rosidl_python/issues/129)_)
* Add smoke test for CLI extension ([#132 ](https://github.com/ros2/rosidl_python/issues/132)_)
* Install generated Python interfaces in a Python package ([#131 ](https://github.com/ros2/rosidl_python/issues/131)_)
* Contributors: Charles Cross, Chen Lihui, Michel Hidalgo, Seulbae Kim, Shane Loretz, William Woodall, ksuszka


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_parser <https://github.com/ros2/rosidl/tree/humble/rosidl_parser/CHANGELOG.rst>`__

* Set maybe_placeholders to False for lark 1.+ compatibility ([#664 ](https://github.com/ros2/rosidl/issues/664)_)
* Generate documentation in generated C header files based on ROS interfaces comments ([#593 ](https://github.com/ros2/rosidl/issues/593)_)
* Pass comments in ros interface constants to the .idl generated files ([#630 ](https://github.com/ros2/rosidl/issues/630)_)
* Update package maintainers ([#624 ](https://github.com/ros2/rosidl/issues/624)_)
* Fix escaping in string literals ([#595 ](https://github.com/ros2/rosidl/issues/595)_)
* Contributors: Ivan Santiago Paunovic, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_runtime_c <https://github.com/ros2/rosidl/tree/humble/rosidl_runtime_c/CHANGELOG.rst>`__

* Fix error handling when copying C sequence messages ([#671 ](https://github.com/ros2/rosidl/issues/671)_)
* Set the output size unconditionally when copying sequences ([#669 ](https://github.com/ros2/rosidl/issues/669)_)
* De-duplicate Quality Level from README and QUALITY_DECLARATION ([#661 ](https://github.com/ros2/rosidl/issues/661)_)
* Install headers to include/${PROJECT_NAME} ([#658 ](https://github.com/ros2/rosidl/issues/658)_)
* Implement copy function for C messages ([#650 ](https://github.com/ros2/rosidl/issues/650)_)
* Implement equality operator function for C messages. ([#648 ](https://github.com/ros2/rosidl/issues/648)_)
* Set CXX standard to 17 ([#635 ](https://github.com/ros2/rosidl/issues/635)_)
* Update package maintainers ([#624 ](https://github.com/ros2/rosidl/issues/624)_)
* Use RCUtils allocators in rosidl_generator_c ([#584 ](https://github.com/ros2/rosidl/issues/584)_)
* Contributors: Jose Luis Rivero, Michel Hidalgo, Nikolai Morin, Pablo Garrido, Shane Loretz, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_runtime_cpp <https://github.com/ros2/rosidl/tree/humble/rosidl_runtime_cpp/CHANGELOG.rst>`__

* Add missing dependency on rosidl_runtime_c ([#666 ](https://github.com/ros2/rosidl/issues/666)_)
* De-duplicate Quality Level from README and QUALITY_DECLARATION ([#661 ](https://github.com/ros2/rosidl/issues/661)_)
* Install headers to include/${PROJECT_NAME} ([#658 ](https://github.com/ros2/rosidl/issues/658)_)
* Set CXX standard to 17 ([#635 ](https://github.com/ros2/rosidl/issues/635)_)
* Update package maintainers ([#624 ](https://github.com/ros2/rosidl/issues/624)_)
* Contributors: Jose Luis Rivero, Michel Hidalgo, Shane Loretz, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_runtime_py <https://github.com/ros2/rosidl_runtime_py/tree/humble/CHANGELOG.rst>`__

* add yaml dump flow style. ([#16 ](https://github.com/ros2/rosidl_runtime_py/issues/16)_)
* Update maintainers ([#15 ](https://github.com/ros2/rosidl_runtime_py/issues/15)_) * Update maintainers to Shane Loretz * Update Shane's email Co-authored-by: Shane Loretz <sloretz@openrobotics.org>
* Contributors: Audrow Nash, Tomoya Fujita


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_c <https://github.com/ros2/rosidl_typesupport/tree/humble/rosidl_typesupport_c/CHANGELOG.rst>`__

* Use target_link_libraries(... PRIVATE ...) in single typesupport case ([#124 ](https://github.com/ros2/rosidl_typesupport/issues/124)_)
* rosidl CMake cleanup in rosidl_typesupport_c ([#123 ](https://github.com/ros2/rosidl_typesupport/issues/123)_)
* Install headers to include/${PROJECT_NAME} ([#121 ](https://github.com/ros2/rosidl_typesupport/issues/121)_)
* Use FindPython3 ([#118 ](https://github.com/ros2/rosidl_typesupport/issues/118)_)
* Revert "Bundle and ensure the exportation of rosidl generated targets" ([#116 ](https://github.com/ros2/rosidl_typesupport/issues/116)_)
* Support available typesupport specification in CLI extensions ([#112 ](https://github.com/ros2/rosidl_typesupport/issues/112)_)
* Bundle and ensure the exportation of rosidl generated targets ([#113 ](https://github.com/ros2/rosidl_typesupport/issues/113)_)
* Fix C and C++ typesupports CLI extensions ([#111 ](https://github.com/ros2/rosidl_typesupport/issues/111)_)
* Contributors: Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_cpp <https://github.com/ros2/rosidl_typesupport/tree/humble/rosidl_typesupport_cpp/CHANGELOG.rst>`__

* Use target_link_libraries(... PRIVATE ...) in single typesupport case ([#124 ](https://github.com/ros2/rosidl_typesupport/issues/124)_)
* rosidl CMake cleanup in rosidl_typesupport_cpp ([#123 ](https://github.com/ros2/rosidl_typesupport/issues/123)_)
* Install headers to include/${PROJECT_NAME} ([#121 ](https://github.com/ros2/rosidl_typesupport/issues/121)_)
* Make sure to check typesupport handles against nullptr properly ([#119 ](https://github.com/ros2/rosidl_typesupport/issues/119)_)
* Use FindPython3 ([#118 ](https://github.com/ros2/rosidl_typesupport/issues/118)_)
* Revert "Bundle and ensure the exportation of rosidl generated targets" ([#116 ](https://github.com/ros2/rosidl_typesupport/issues/116)_)
* Support available typesupport specification in CLI extensions ([#112 ](https://github.com/ros2/rosidl_typesupport/issues/112)_)
* Bundle and ensure the exportation of rosidl generated targets ([#113 ](https://github.com/ros2/rosidl_typesupport/issues/113)_)
* Fix C and C++ typesupports CLI extensions ([#111 ](https://github.com/ros2/rosidl_typesupport/issues/111)_)
* Contributors: Chris Lalancette, Michel Hidalgo, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_fastrtps_c <https://github.com/ros2/rosidl_typesupport_fastrtps/tree/humble/rosidl_typesupport_fastrtps_c/CHANGELOG.rst>`__

* Install generated headers to include/${PROJECT_NAME} ([#88 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/88)_)
* Misc fastrtps typesupport generator cleanup ([#87 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/87)_)
* Install headers to include/${PROJECT_NAME} ([#86 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/86)_)
* Fix include order for cpplint ([#84 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/84)_)
* Update maintainers to Shane Loretz ([#83 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/83)_)
* Use FindPython3 explicitly instead of PythonInterp implicitly ([#78 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/78)_)
* Revert rosidl targets and dependencies exportation ([#76 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/76)_) * Revert "Export rosidl_typesupport_fastrtps_c* dependencies ([#75 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75)_)" * Revert "Bundle and ensure the exportation of rosidl generated targets ([#73 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73)_)"
* Correctly inform that a BoundedSequence is bounded ([#71 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/71)_)
* Export rosidl_typesupport_fastrtps_c* dependencies ([#75 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75)_)
* Bundle and ensure the exportation of rosidl generated targets ([#73 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73)_)
* Fix Fast-RTPS C++ typesupport CLI extension ([#72 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/72)_)
* Fastdds type support extensions ([#67 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/67)_)
* Remove fastrtps dependency ([#68 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/68)_)
* Contributors: Andrea Sorbini, Audrow Nash, Jacob Perron, Michel Hidalgo, Miguel Company, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_fastrtps_cpp <https://github.com/ros2/rosidl_typesupport_fastrtps/tree/humble/rosidl_typesupport_fastrtps_cpp/CHANGELOG.rst>`__

* Install generated headers to include/${PROJECT_NAME} ([#88 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/88)_)
* Misc fastrtps typesupport generator cleanup ([#87 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/87)_)
* Install headers to include/${PROJECT_NAME} ([#86 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/86)_)
* Fix include order for cpplint ([#84 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/84)_) * Fix include order for cpplint Relates to https://github.com/ament/ament_lint/pull/324 * Use double-quotes for other includes This is backwards compatible with older versions of cpplint.
* Update maintainers to Shane Loretz ([#83 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/83)_)
* Re-introduce improvements to serialization of primitive bounded sequences for C++ type support ([#81 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/81)_)
* Revert "Improve serialization of ... ([#79 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/79)_)" ([#80 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/80)_)
* Improve serialization of primitive bounded sequences in C++ type support ([#79 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/79)_)
* Use FindPython3 explicitly instead of PythonInterp implicitly ([#78 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/78)_)
* Revert rosidl targets and dependencies exportation ([#76 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/76)_) * Revert "Export rosidl_typesupport_fastrtps_c* dependencies ([#75 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75)_)" * Revert "Bundle and ensure the exportation of rosidl generated targets ([#73 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73)_)"
* Correctly inform that a BoundedSequence is bounded ([#71 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/71)_)
* Export rosidl_typesupport_fastrtps_c* dependencies ([#75 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/75)_)
* Bundle and ensure the exportation of rosidl generated targets ([#73 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/73)_)
* Fix Fast-RTPS C++ typesupport CLI extension ([#72 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/72)_)
* Fastdds type support extensions ([#67 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/67)_)
* Remove fastrtps dependency ([#68 ](https://github.com/ros2/rosidl_typesupport_fastrtps/issues/68)_)
* Contributors: Andrea Sorbini, Audrow Nash, Jacob Perron, Jorge Perez, Michel Hidalgo, Miguel Company, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_interface <https://github.com/ros2/rosidl/tree/humble/rosidl_typesupport_interface/CHANGELOG.rst>`__

* De-duplicate Quality Level from README and QUALITY_DECLARATION ([#661 ](https://github.com/ros2/rosidl/issues/661)_)
* Install headers to include/${PROJECT_NAME} ([#658 ](https://github.com/ros2/rosidl/issues/658)_)
* Add ROSIDL_TYPESUPPORT_INTERFACE__LIBRARY_NAME() macro ([#649 ](https://github.com/ros2/rosidl/issues/649)_)
* Set CXX standard to 17 ([#635 ](https://github.com/ros2/rosidl/issues/635)_)
* Update package maintainers ([#624 ](https://github.com/ros2/rosidl/issues/624)_)
* Contributors: Jose Luis Rivero, Michel Hidalgo, Shane Loretz, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_introspection_c <https://github.com/ros2/rosidl/tree/humble/rosidl_typesupport_introspection_c/CHANGELOG.rst>`__

* Install generated headers to include/${PROJECT_NAME} ([#670 ](https://github.com/ros2/rosidl/issues/670)_)
* Misc cleanup in the rosidl generator extensions ([#662 ](https://github.com/ros2/rosidl/issues/662)_)
* De-duplicate Quality Level from README and QUALITY_DECLARATION ([#661 ](https://github.com/ros2/rosidl/issues/661)_)
* Update Quality declaration to level 1 in README for instrospection pkgs ([#659 ](https://github.com/ros2/rosidl/issues/659)_)
* Install headers to include/${PROJECT_NAME} ([#658 ](https://github.com/ros2/rosidl/issues/658)_)
* Move rosidl_typesupport_introspection_cpp quality declaration to Q1 ([#657 ](https://github.com/ros2/rosidl/issues/657)_)
* Move rosidl_typesupport_introspection_c quality declaration to Q1  ([#656 ](https://github.com/ros2/rosidl/issues/656)_)
* add documentation for generators and API ([#646 ](https://github.com/ros2/rosidl/issues/646)_)
* Rework nested types' items introspection in C and C++ ([#652 ](https://github.com/ros2/rosidl/issues/652)_)
* Fix up the documentation for rosidl_typesupport_introspection_c ([#628 ](https://github.com/ros2/rosidl/issues/628)_)
* Update package maintainers ([#624 ](https://github.com/ros2/rosidl/issues/624)_)
* Quality Declaration for typesupport_introspection ([#621 ](https://github.com/ros2/rosidl/issues/621)_)
* Make rosidl packages use FindPython3 instead of FindPythonInterp ([#612 ](https://github.com/ros2/rosidl/issues/612)_)
* Revert "Bundle and ensure the exportation of rosidl generated targets" ([#611 ](https://github.com/ros2/rosidl/issues/611)_)
* Bundle and ensure the exportation of rosidl generated targets ([#601 ](https://github.com/ros2/rosidl/issues/601)_)
* Update function prefix ([#596 ](https://github.com/ros2/rosidl/issues/596)_)
* Contributors: Chris Lalancette, Jose Luis Rivero, Michel Hidalgo, Pablo Garrido, Shane Loretz, eboasson


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_introspection_cpp <https://github.com/ros2/rosidl/tree/humble/rosidl_typesupport_introspection_cpp/CHANGELOG.rst>`__

* Install generated headers to include/${PROJECT_NAME} ([#670 ](https://github.com/ros2/rosidl/issues/670)_)
* Misc cleanup in the rosidl generator extensions ([#662 ](https://github.com/ros2/rosidl/issues/662)_)
* De-duplicate Quality Level from README and QUALITY_DECLARATION ([#661 ](https://github.com/ros2/rosidl/issues/661)_)
* Update Quality declaration to level 1 in README for instrospection pkgs ([#659 ](https://github.com/ros2/rosidl/issues/659)_)
* Install headers to include/${PROJECT_NAME} ([#658 ](https://github.com/ros2/rosidl/issues/658)_)
* Move rosidl_typesupport_introspection_cpp quality declaration to Q1 ([#657 ](https://github.com/ros2/rosidl/issues/657)_)
* add documentation for generators and API ([#646 ](https://github.com/ros2/rosidl/issues/646)_)
* Rework nested types' items introspection in C and C++ ([#652 ](https://github.com/ros2/rosidl/issues/652)_)
* Set CXX standard to 17 ([#635 ](https://github.com/ros2/rosidl/issues/635)_)
* Fix up the documentation for rosidl_typesupport_introspection_cpp ([#627 ](https://github.com/ros2/rosidl/issues/627)_)
* Update package maintainers ([#624 ](https://github.com/ros2/rosidl/issues/624)_)
* Quality Declaration for typesupport_introspection ([#621 ](https://github.com/ros2/rosidl/issues/621)_)
* Make rosidl packages use FindPython3 instead of FindPythonInterp ([#612 ](https://github.com/ros2/rosidl/issues/612)_)
* Revert "Bundle and ensure the exportation of rosidl generated targets" ([#611 ](https://github.com/ros2/rosidl/issues/611)_)
* Bundle and ensure the exportation of rosidl generated targets ([#601 ](https://github.com/ros2/rosidl/issues/601)_)
* Contributors: Chris Lalancette, Jose Luis Rivero, Michel Hidalgo, Shane Loretz, eboasson, Øystein Sture


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rosidl_typesupport_introspection_tests <https://github.com/ros2/rosidl/tree/humble/rosidl_typesupport_introspection_tests/CHANGELOG.rst>`__

* Bump [`rosidl_typesupport_introspection_tests`` coverage (`#655 ](https://github.com/ros2/rosidl/issues/655)_)
* Add introspection typesupport tests for C/C++ services ([#653 ](https://github.com/ros2/rosidl/issues/653)_)
* Add introspection typesupport tests for C/C++ messages ([#651 ](https://github.com/ros2/rosidl/issues/651)_)
* Contributors: Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rpyutils <https://github.com/ros2/rpyutils/tree/humble/CHANGELOG.rst>`__

* Make sure to call abspath when adding Windows DLL directories. ([#8 ](https://github.com/ros2/rpyutils/issues/8)_)
* Update troubleshooting links to docs.ros.org ([#6 ](https://github.com/ros2/rpyutils/issues/6)_)
* Contributors: Chris Lalancette, Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_gui <https://github.com/ros-visualization/rqt/tree/humble/rqt_gui/CHANGELOG.rst>`__

* Changed getiter to iter ([#1 ](https://github.com/ros-visualization/rqt/issues/1)_) ([#241 ](https://github.com/ros-visualization/rqt/issues/241)_)
* Update maintainers ([#233 ](https://github.com/ros-visualization/rqt/issues/233)_) ([#237 ](https://github.com/ros-visualization/rqt/issues/237)_)
* add missing dependencies: rospkg-modules, python_qt_binding, rospy ([#227 ](https://github.com/ros-visualization/rqt/issues/227)_)
* bump CMake minimum version to avoid CMP0048 warning ([#219 ](https://github.com/ros-visualization/rqt/issues/219)_)
* use catkin_install_python for Python script ([#206 ](https://github.com/ros-visualization/rqt/issues/206)_)
* Contributors: Michael Jeronimo, sven-herrmann


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_gui_cpp <https://github.com/ros-visualization/rqt/tree/humble/rqt_gui_cpp/CHANGELOG.rst>`__

* Update maintainers ([#233 ](https://github.com/ros-visualization/rqt/issues/233)_) ([#237 ](https://github.com/ros-visualization/rqt/issues/237)_)
* bump CMake minimum version to avoid CMP0048 warning ([#219 ](https://github.com/ros-visualization/rqt/issues/219)_)
* [Windows] fix rqt_gui_cpp install path ([#190 ](https://github.com/ros-visualization/rqt/issues/190)_)
* [Windows] fix building ([#189 ](https://github.com/ros-visualization/rqt/issues/189)_)
* Contributors: Michael Jeronimo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_gui_py <https://github.com/ros-visualization/rqt/tree/humble/rqt_gui_py/CHANGELOG.rst>`__

* Update maintainers ([#233 ](https://github.com/ros-visualization/rqt/issues/233)_) ([#237 ](https://github.com/ros-visualization/rqt/issues/237)_)
* bump CMake minimum version to avoid CMP0048 warning ([#219 ](https://github.com/ros-visualization/rqt/issues/219)_)


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rqt_py_common <https://github.com/ros-visualization/rqt/tree/humble/rqt_py_common/CHANGELOG.rst>`__

* Update maintainers ([#233 ](https://github.com/ros-visualization/rqt/issues/233)_) ([#237 ](https://github.com/ros-visualization/rqt/issues/237)_)
* bump CMake minimum version to avoid CMP0048 warning ([#219 ](https://github.com/ros-visualization/rqt/issues/219)_)
* fix missing import bugs ([#139 ](https://github.com/ros-visualization/rqt/issues/139)_)
* Contributors: Michael Jeronimo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rti_connext_dds_cmake_module <https://github.com/ros2/rmw_connextdds/tree/humble/rti_connext_dds_cmake_module/CHANGELOG.rst>`__

* Update rti-connext-dds dependency to 6.0.1. ([#71 ](https://github.com/ros2/rmw_connextdds/issues/71)_)
* Contributors: Steven! Ragnarök


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rttest <https://github.com/ros2/realtime_support/tree/humble/rttest/CHANGELOG.rst>`__

* Install includes to include/${PROJECT_NAME} ([#114 ](https://github.com/ros2/realtime_support/issues/114)_)
* Fix include order for cpplint ([#113 ](https://github.com/ros2/realtime_support/issues/113)_)
* Fixes for uncrustify 0.72 ([#111 ](https://github.com/ros2/realtime_support/issues/111)_)
* Mark dependent targets as PRIVATE ([#112 ](https://github.com/ros2/realtime_support/issues/112)_)
* Export modern CMake targets ([#110 ](https://github.com/ros2/realtime_support/issues/110)_)
* Contributors: Chris Lalancette, Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz2 <https://github.com/ros2/rviz/tree/humble/rviz2/CHANGELOG.rst>`__

* Change links index.ros.org -> docs.ros.org. ([#698 ](https://github.com/ros2/rviz/issues/698)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_assimp_vendor <https://github.com/ros2/rviz/tree/humble/rviz_assimp_vendor/CHANGELOG.rst>`__

* Make sure to pass compiler and flags down to assimp ([#844 ](https://github.com/ros2/rviz/issues/844)_)
* Fix support for assimp 5.1.0 ([#817 ](https://github.com/ros2/rviz/issues/817)_)
* Contributors: Chris Lalancette, Silvio Traversaro


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_common <https://github.com/ros2/rviz/tree/humble/rviz_common/CHANGELOG.rst>`__

* Add implementation for cancel interface ([#809 ](https://github.com/ros2/rviz/issues/809)_)
* Install headers to include/${PROJECT_NAME} ([#829 ](https://github.com/ros2/rviz/issues/829)_)
* Remove definition of PLUGINLIB_DISABLE_BOOST. ([#821 ](https://github.com/ros2/rviz/issues/821)_)
* Fix support for assimp 5.1.0 ([#817 ](https://github.com/ros2/rviz/issues/817)_)
* Fix cpplint errors ([#818 ](https://github.com/ros2/rviz/issues/818)_)
* Set message type for ros topic display ([#800 ](https://github.com/ros2/rviz/issues/800)_)
* Fixes for uncrustify 0.72 ([#807 ](https://github.com/ros2/rviz/issues/807)_)
* Do not block visualization manager updates when opening the display panel dialog ([#795 ](https://github.com/ros2/rviz/issues/795)_)
* Switch to using Qt::MiddleButton for RViz. ([#802 ](https://github.com/ros2/rviz/issues/802)_)
* Removed traces in renderPanel ([#777 ](https://github.com/ros2/rviz/issues/777)_)
* move yaml_config_writer.hpp to public includes ([#764 ](https://github.com/ros2/rviz/issues/764)_)
* Update displays_panel.cpp ([#745 ](https://github.com/ros2/rviz/issues/745)_)
* Robot: Report mesh loading issues ([#744 ](https://github.com/ros2/rviz/issues/744)_)
* Exposed tool_manager header file. ([#767 ](https://github.com/ros2/rviz/issues/767)_)
* refactor: make const getter methods const ([#756 ](https://github.com/ros2/rviz/issues/756)_)
* Efficiently handle 3-bytes pixel formats ([#743 ](https://github.com/ros2/rviz/issues/743)_)
* Report sample lost events ([#686 ](https://github.com/ros2/rviz/issues/686)_)
* Update window close icon ([#734 ](https://github.com/ros2/rviz/issues/734)_)
* Fix missing "X" icon in panel close button ([#731 ](https://github.com/ros2/rviz/issues/731)_)
* Add rviz_rendering dependency to rviz_common ([#727 ](https://github.com/ros2/rviz/issues/727)_)
* Remove the word "Alpha" from the splash screen. ([#696 ](https://github.com/ros2/rviz/issues/696)_)
* Removed some memory leaks in rviz_rendering and rviz_rendering_tests ([#710 ](https://github.com/ros2/rviz/issues/710)_)
* Contributors: ANDOU Tetsuo, Alejandro Hernández Cordero, Chen Lihui, Chris Lalancette, Daisuke Nishimatsu, Gonzo, Ivan Santiago Paunovic, Jacob Perron, Joseph Schornak, Rebecca Butler, Shane Loretz, Silvio Traversaro, davidorchansky


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_default_plugins <https://github.com/ros2/rviz/tree/humble/rviz_default_plugins/CHANGELOG.rst>`__

* Add far plane distance property to camera ([#849 ](https://github.com/ros2/rviz/issues/849)_)
* Drop ignition-math6 from rviz_default_plugins link interface ([#833 ](https://github.com/ros2/rviz/issues/833)_)
* add implementation for cancel interface ([#809 ](https://github.com/ros2/rviz/issues/809)_)
* Install headers to include/${PROJECT_NAME} ([#829 ](https://github.com/ros2/rviz/issues/829)_)
* Remove definition of PLUGINLIB_DISABLE_BOOST. ([#821 ](https://github.com/ros2/rviz/issues/821)_)
* Remove TF filter from ImageTransportDisplay ([#788 ](https://github.com/ros2/rviz/issues/788)_)
* Add underscores to material names ([#811 ](https://github.com/ros2/rviz/issues/811)_)
* Export image_transport dependency ([#813 ](https://github.com/ros2/rviz/issues/813)_)
* Fixes for uncrustify 0.72 ([#807 ](https://github.com/ros2/rviz/issues/807)_)
* Switch to using Qt::MiddleButton for RViz. ([#802 ](https://github.com/ros2/rviz/issues/802)_)
* Add a tf_buffer_cache_time_ns to tf_wrapper ([#792 ](https://github.com/ros2/rviz/issues/792)_)
* Make libraries to avoid compiling files multiple times ([#774 ](https://github.com/ros2/rviz/issues/774)_)
* Computed inertia with ignition-math ([#751 ](https://github.com/ros2/rviz/issues/751)_)
* Fixed crash when changing rendering parameters for pointcloud2 while 'Selectable' box is unchecked ([#768 ](https://github.com/ros2/rviz/issues/768)_)
* Robot: Report mesh loading issues ([#744 ](https://github.com/ros2/rviz/issues/744)_)
* Handle NaN values for Wrench msgs ([#746 ](https://github.com/ros2/rviz/issues/746)_)
* Triangle lists support textures ([#719 ](https://github.com/ros2/rviz/issues/719)_)
* Report sample lost events ([#686 ](https://github.com/ros2/rviz/issues/686)_)
* Fix path message orientation error ([#736 ](https://github.com/ros2/rviz/issues/736)_)
* Set topic namespace in interactive markers display ([#725 ](https://github.com/ros2/rviz/issues/725)_)
* mass property visualization ([#714 ](https://github.com/ros2/rviz/issues/714)_)
* Export InteractiveMarker ([#718 ](https://github.com/ros2/rviz/issues/718)_)
* Yuv to rgb changes ([#701 ](https://github.com/ros2/rviz/issues/701)_)
* Extract message type in ImageTransportDisplay ([#711 ](https://github.com/ros2/rviz/issues/711)_)
* Duplicated code RobotJoint ([#702 ](https://github.com/ros2/rviz/issues/702)_)
* Don't attempt to moc generate files that don't have QOBJECT. ([#690 ](https://github.com/ros2/rviz/issues/690)_)
* Switch to including tf2_geometry_msgs.hpp ([#689 ](https://github.com/ros2/rviz/issues/689)_)
* Export Qt5 dependencies properly ([#687 ](https://github.com/ros2/rviz/issues/687)_)
* Add support for namespace-scoped DELETEALL action in Marker displays ([#685 ](https://github.com/ros2/rviz/issues/685)_)
* Use image_transport to subscribe to image messages ([#523 ](https://github.com/ros2/rviz/issues/523)_)
* Contributors: Akash, Alejandro Hernández Cordero, Audrow Nash, Chen Lihui, Chris Lalancette, Cory Crean, Gonzo, Greg Balke, Ivan Santiago Paunovic, Jacob Perron, Martin Idel, Michel Hidalgo, Paul, Rebecca Butler, Scott K Logan, Shane Loretz, bailaC, brian soe, cturcotte-qnx, ketatam


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_ogre_vendor <https://github.com/ros2/rviz/tree/humble/rviz_ogre_vendor/CHANGELOG.rst>`__

* Fix interface link libraries in ogre vendor ([#761 ](https://github.com/ros2/rviz/issues/761)_)
* Fix the build for Ubuntu Jammy arm64. ([#828 ](https://github.com/ros2/rviz/issues/828)_)
* Strip RPATH from installed Ogre binaries ([#688 ](https://github.com/ros2/rviz/issues/688)_)
* Contributors: Chris Lalancette, Laszlo Turanyi, Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_rendering <https://github.com/ros2/rviz/tree/humble/rviz_rendering/CHANGELOG.rst>`__

* Make getVerticesPerPoint method public and improve tests ([#843 ](https://github.com/ros2/rviz/issues/843)_)
* Disable class-memaccess warnings for Eigen ([#838 ](https://github.com/ros2/rviz/issues/838)_)
* Disable a warning when including Eigen. ([#835 ](https://github.com/ros2/rviz/issues/835)_)
* Install headers to include/${PROJECT_NAME} ([#829 ](https://github.com/ros2/rviz/issues/829)_)
* Fix support for assimp 5.1.0 ([#817 ](https://github.com/ros2/rviz/issues/817)_)
* Fix cpplint errors ([#818 ](https://github.com/ros2/rviz/issues/818)_)
* Fixes for uncrustify 0.72 ([#807 ](https://github.com/ros2/rviz/issues/807)_)
* Suppress assimp warnings in rviz_rendering build ([#775 ](https://github.com/ros2/rviz/issues/775)_)
* Fix for ogre failing when material already exists ([#729 ](https://github.com/ros2/rviz/issues/729)_)
* Removed some memory leaks in rviz_rendering and rviz_rendering_tests ([#710 ](https://github.com/ros2/rviz/issues/710)_)
* Export Qt5 dependencies properly ([#687 ](https://github.com/ros2/rviz/issues/687)_)
* Putting glsl 1.50 resources back in RenderSystem ([#668 ](https://github.com/ros2/rviz/issues/668)_)
* Contributors: Alejandro Hernández Cordero, Chris Lalancette, Jacob Perron, Jorge Perez, Michel Hidalgo, Piotr Jaroszek, Scott K Logan, Shane Loretz, Silvio Traversaro, Wolf Vollprecht


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_rendering_tests <https://github.com/ros2/rviz/tree/humble/rviz_rendering_tests/CHANGELOG.rst>`__

* Removed some memory leaks in rviz_rendering and rviz_rendering_tests ([#710 ](https://github.com/ros2/rviz/issues/710)_)
* Contributors: Alejandro Hernández Cordero


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `rviz_visual_testing_framework <https://github.com/ros2/rviz/tree/humble/rviz_visual_testing_framework/CHANGELOG.rst>`__

* Install headers to include/${PROJECT_NAME} ([#829 ](https://github.com/ros2/rviz/issues/829)_)
* Fixes for uncrustify 0.72 ([#807 ](https://github.com/ros2/rviz/issues/807)_)
* Update includes after rcutils/get_env.h deprecation ([#677 ](https://github.com/ros2/rviz/issues/677)_)
* Contributors: Chris Lalancette, Christophe Bedard, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sensor_msgs <https://github.com/ros2/common_interfaces/tree/humble/sensor_msgs/CHANGELOG.rst>`__

* Move the find_package statements for BUILD_TESTING  ([#186 ](https://github.com/ros2/common_interfaces/issues/186)_)
* Feedback on conditional sensor_msgs_library target ([#1 ](https://github.com/ros2/common_interfaces/issues/1)_) ([#183 ](https://github.com/ros2/common_interfaces/issues/183)_)
* [Fix] Fix image_encodings.hpp's URL in README ([#184 ](https://github.com/ros2/common_interfaces/issues/184)_)
* [Fix] Fix fill_image.hpp's URL in README ([#182 ](https://github.com/ros2/common_interfaces/issues/182)_)
* Add sensor_msgs_library target and install headers to include/${PROJECT_NAME} ([#178 ](https://github.com/ros2/common_interfaces/issues/178)_)
* Interface packages should fully <depend> on the interface packages that they depend on ([#173 ](https://github.com/ros2/common_interfaces/issues/173)_)
* Add YUV420 and YUV444 to image encodings ([#172 ](https://github.com/ros2/common_interfaces/issues/172)_)
* Cleanup mislabeled BSD license ([#83 ](https://github.com/ros2/common_interfaces/issues/83)_)
* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Fix rosdoc2 warnings in sensor_msgs. ([#162 ](https://github.com/ros2/common_interfaces/issues/162)_)
* Add equidistant distortion model ([#160 ](https://github.com/ros2/common_interfaces/issues/160)_)
* Use rosidl_get_typesupport_target() ([#156 ](https://github.com/ros2/common_interfaces/issues/156)_)
* Update CompressedImage documentation: add 'tiff' as a supported format ([#154 ](https://github.com/ros2/common_interfaces/issues/154)_)
* Contributors: Audrow Nash, Chris Lalancette, Grey, Hemal Shah, Homalozoa X, Ivan Santiago Paunovic, Martin Günther, Michael Jeronimo, Pablo Garrido, Shane Loretz, Tully Foote


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sensor_msgs_py <https://github.com/ros2/common_interfaces/tree/humble/sensor_msgs_py/CHANGELOG.rst>`__

* Add in a compatibility layer for older versions of numpy. ([#185 ](https://github.com/ros2/common_interfaces/issues/185)_)
* Port pointcloud creation to numpy. ([#175 ](https://github.com/ros2/common_interfaces/issues/175)_)
* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Contributors: Audrow Nash, Chris Lalancette, Florian Vahl


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `shape_msgs <https://github.com/ros2/common_interfaces/tree/humble/shape_msgs/CHANGELOG.rst>`__

* Interface packages should fully <depend> on the interface packages that they depend on ([#173 ](https://github.com/ros2/common_interfaces/issues/173)_)
* Add prism type to the SolidPrimitive.msg ([#166 ](https://github.com/ros2/common_interfaces/issues/166)_) ([#167 ](https://github.com/ros2/common_interfaces/issues/167)_)
* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Contributors: Audrow Nash, Grey, M. Fatih Cırıt


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `shared_queues_vendor <https://github.com/ros2/rosbag2/tree/humble/shared_queues_vendor/CHANGELOG.rst>`__

* Bump version number to avoid conflict
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Contributors: Chris Lalancette, Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sqlite3_vendor <https://github.com/ros2/rosbag2/tree/humble/sqlite3_vendor/CHANGELOG.rst>`__

* Bump version number to avoid conflict
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Contributors: Chris Lalancette, Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `sros2 <https://github.com/ros2/sros2/tree/humble/sros2/CHANGELOG.rst>`__

* Increase the shutdown timeout for test_generate_policy_no_nodes. ([#278 ](https://github.com/ros2/sros2/issues/278)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `statistics_msgs <https://github.com/ros2/rcl_interfaces/tree/humble/statistics_msgs/CHANGELOG.rst>`__

* Update maintainers to Chris Lalancette ([#130 ](https://github.com/ros2/rcl_interfaces/issues/130)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `std_msgs <https://github.com/ros2/common_interfaces/tree/humble/std_msgs/CHANGELOG.rst>`__

* Interface packages should fully <depend> on the interface packages that they depend on ([#173 ](https://github.com/ros2/common_interfaces/issues/173)_)
* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Contributors: Audrow Nash, Grey


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `std_srvs <https://github.com/ros2/common_interfaces/tree/humble/std_srvs/CHANGELOG.rst>`__

* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Contributors: Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `stereo_msgs <https://github.com/ros2/common_interfaces/tree/humble/stereo_msgs/CHANGELOG.rst>`__

* Interface packages should fully <depend> on the interface packages that they depend on ([#173 ](https://github.com/ros2/common_interfaces/issues/173)_)
* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Contributors: Audrow Nash, Grey


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_cli <https://github.com/ros2/system_tests/tree/humble/test_cli/CHANGELOG.rst>`__

* Updated maintainers ([#489 ](https://github.com/ros2/system_tests/issues/489)_)
* Add changelogs ([#473 ](https://github.com/ros2/system_tests/issues/473)_)
* Merge pull request [#356 ](https://github.com/ros2/system_tests/issues/356)_ from ros2/issue/321_enhance_parameter_api
* Contributors: Aditya Pande, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_cli_remapping <https://github.com/ros2/system_tests/tree/humble/test_cli_remapping/CHANGELOG.rst>`__

* Update python nodes SIGINT handling ([#490 ](https://github.com/ros2/system_tests/issues/490)_)
* Updated maintainers ([#489 ](https://github.com/ros2/system_tests/issues/489)_)
* Add changelogs ([#473 ](https://github.com/ros2/system_tests/issues/473)_)
* Contributors: Aditya Pande, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_communication <https://github.com/ros2/system_tests/tree/humble/test_communication/CHANGELOG.rst>`__

* Split test_subscriber into multiple compilation units. ([#500 ](https://github.com/ros2/system_tests/issues/500)_)
* Add test_msgs dependency ([#497 ](https://github.com/ros2/system_tests/issues/497)_)
* Update python nodes SIGINT handling ([#490 ](https://github.com/ros2/system_tests/issues/490)_)
* Updated maintainers ([#489 ](https://github.com/ros2/system_tests/issues/489)_)
* Fix deprecated subscriber callback warnings ([#483 ](https://github.com/ros2/system_tests/issues/483)_)
* Add tests for BoundedPlainSequences ([#481 ](https://github.com/ros2/system_tests/issues/481)_)
* Use rosidl_get_typesupport_target() ([#480 ](https://github.com/ros2/system_tests/issues/480)_)
* Use rcpputils/scope_exit.hpp instead of rclcpp/scope_exit.hpp ([#479 ](https://github.com/ros2/system_tests/issues/479)_)
* Add changelogs ([#473 ](https://github.com/ros2/system_tests/issues/473)_)
* Contributors: Abrar Rahman Protyasha, Aditya Pande, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_interface_files <https://github.com/ros2/test_interface_files/tree/humble/CHANGELOG.rst>`__

* Revert "Update package.xml ([#18 ](https://github.com/ros2/test_interface_files/issues/18)_)" ([#19 ](https://github.com/ros2/test_interface_files/issues/19)_)
* Update package.xml ([#18 ](https://github.com/ros2/test_interface_files/issues/18)_)
* Update maintainers to Audrow Nash ([#17 ](https://github.com/ros2/test_interface_files/issues/17)_)
* Added BoundedPlainSequences messages ([#14 ](https://github.com/ros2/test_interface_files/issues/14)_)
* Contributors: Audrow Nash, Chris Lalancette, Miguel Company, Nikolai Morin


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_launch_ros <https://github.com/ros2/launch_ros/tree/humble/test_launch_ros/CHANGELOG.rst>`__

* Increase test time tolerance ([#305 ](https://github.com/ros2/launch_ros/issues/305)_)
* Use correct namespace when evaluating parameter files for composable nodes ([#303 ](https://github.com/ros2/launch_ros/issues/303)_)
* Handle empty strings when evaluating parameters ([#300 ](https://github.com/ros2/launch_ros/issues/300)_)
* Add parameter substitution ([#297 ](https://github.com/ros2/launch_ros/issues/297)_)
* More Helpful Error Messages ([#275 ](https://github.com/ros2/launch_ros/issues/275)_)
* Update maintainers in setup.py ([#287 ](https://github.com/ros2/launch_ros/issues/287)_)
* Set parameters from file for composable nodes ([#281 ](https://github.com/ros2/launch_ros/issues/281)_)
* Update package maintainers ([#284 ](https://github.com/ros2/launch_ros/issues/284)_)
* Update node name matcher ([#282 ](https://github.com/ros2/launch_ros/issues/282)_)
* Support both parameter file configurations for composable nodes ([#259 ](https://github.com/ros2/launch_ros/issues/259)_)
* Shutdown context after test ([#267 ](https://github.com/ros2/launch_ros/issues/267)_)
* Handle substitutions in RosTimer ([#264 ](https://github.com/ros2/launch_ros/issues/264)_)
* Add SetParametersFromFile action ([#260 ](https://github.com/ros2/launch_ros/issues/260)_)
* Properly support ros_args attribute through launch frontends ([#253 ](https://github.com/ros2/launch_ros/issues/253)_)
* Add 'push_ros_namespace' alias to 'push-ros-namespace' ([#250 ](https://github.com/ros2/launch_ros/issues/250)_)
* Add ros_arguments option to Node action ([#249 ](https://github.com/ros2/launch_ros/issues/249)_)
* ROS Timer Action ([#244 ](https://github.com/ros2/launch_ros/issues/244)_)
* Support container in frontend ([#235 ](https://github.com/ros2/launch_ros/issues/235)_)
* Added normalize_remap_rule and types. ([launch #173 ](https://github.com/ros2/launch/issues/173)_)
* Fixed setup.py versions ([launch #155 ](https://github.com/ros2/launch/issues/155)_)
* Fixed a bug to ensure that shutdown event is handled correctly ([launch #154 ](https://github.com/ros2/launch/issues/154)_)
* Made various fixes and added tests for remappings passed to Node actions ([launch #137 ](https://github.com/ros2/launch/issues/137)_)
* Contributors: Aditya Pande, Audrow Nash, Christophe Bedard, David V. Lu!!, Jacob Perron, Jorge Perez, Kenji Miyake, Michel Hidalgo, Rebecca Butler


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_launch_testing <https://github.com/ros2/launch/tree/humble/test_launch_testing/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Michel Hidalgo ([#559 ](https://github.com/ros2/launch/issues/559)_)
* Updated maintainers ([#555 ](https://github.com/ros2/launch/issues/555)_)
* Contributors: Aditya Pande, Audrow Nash


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_msgs <https://github.com/ros2/rcl_interfaces/tree/humble/test_msgs/CHANGELOG.rst>`__

* Install headers to include/${PROJECT_NAME} and Depend on rosidl_typesupport\_* targets directly ([#133 ](https://github.com/ros2/rcl_interfaces/issues/133)_)
* Update maintainers to Chris Lalancette ([#130 ](https://github.com/ros2/rcl_interfaces/issues/130)_)
* Add test fixures for BoundedPlainSequences ([#125 ](https://github.com/ros2/rcl_interfaces/issues/125)_)
* Added BoundedPlainSequences to test_msgs ([#123 ](https://github.com/ros2/rcl_interfaces/issues/123)_)
* Contributors: Audrow Nash, Miguel Company, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_quality_of_service <https://github.com/ros2/system_tests/tree/humble/test_quality_of_service/CHANGELOG.rst>`__

* Update maintainers to Aditya Pande and Shane Loretz ([#491 ](https://github.com/ros2/system_tests/issues/491)_)
* Updated maintainers ([#489 ](https://github.com/ros2/system_tests/issues/489)_)
* Fix deprecated subscriber callback warnings ([#483 ](https://github.com/ros2/system_tests/issues/483)_)
* Add changelogs ([#473 ](https://github.com/ros2/system_tests/issues/473)_)
* Contributors: Abrar Rahman Protyasha, Aditya Pande, Audrow Nash, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_rclcpp <https://github.com/ros2/system_tests/tree/humble/test_rclcpp/CHANGELOG.rst>`__

* Fix include order for cpplint ([#493 ](https://github.com/ros2/system_tests/issues/493)_)
* Fix test ([#488 ](https://github.com/ros2/system_tests/issues/488)_)
* Updated maintainers ([#489 ](https://github.com/ros2/system_tests/issues/489)_)
* Add tests for rclcpp sigterm handler ([#485 ](https://github.com/ros2/system_tests/issues/485)_)
* Fix deprecated subscriber callback warnings ([#483 ](https://github.com/ros2/system_tests/issues/483)_)
* Fix deprecation warnings and failures after client API update ([#482 ](https://github.com/ros2/system_tests/issues/482)_)
* Use rosidl_get_typesupport_target() ([#480 ](https://github.com/ros2/system_tests/issues/480)_)
* Use rcpputils/scope_exit.hpp instead of rclcpp/scope_exit.hpp ([#479 ](https://github.com/ros2/system_tests/issues/479)_)
* Add test for defered service callback signature ([#478 ](https://github.com/ros2/system_tests/issues/478)_)
* Add changelogs ([#473 ](https://github.com/ros2/system_tests/issues/473)_)
* Merge pull request [#357 ](https://github.com/ros2/system_tests/issues/357)_ from ros2/ros2_658_leftovers
* Contributors: Abrar Rahman Protyasha, Aditya Pande, Christophe Bedard, Ivan Santiago Paunovic, Jacob Perron, Mauro Passerino, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_rmw_implementation <https://github.com/ros2/rmw_implementation/tree/humble/test_rmw_implementation/CHANGELOG.rst>`__

* add content-filtered-topic interfaces ([#181 ](https://github.com/ros2/rmw_implementation/issues/181)_)
* Fix linter issues ([#200 ](https://github.com/ros2/rmw_implementation/issues/200)_)
* Add client/service QoS getters. ([#196 ](https://github.com/ros2/rmw_implementation/issues/196)_)
* Added tests for bounded sequences serialization ([#193 ](https://github.com/ros2/rmw_implementation/issues/193)_)
* Add RMW_DURATION_INFINITE basic compliance test. ([#194 ](https://github.com/ros2/rmw_implementation/issues/194)_)
* Test SubscriptionOptions::ignore_local_publications. ([#192 ](https://github.com/ros2/rmw_implementation/issues/192)_)
* Add rmw_publisher_wait_for_all_acked. ([#188 ](https://github.com/ros2/rmw_implementation/issues/188)_)
* Wait for server in test_rmw_implementation service tests. ([#191 ](https://github.com/ros2/rmw_implementation/issues/191)_)
* Contributors: Barry Xu, Chen Lihui, Emerson Knapp, Jorge Perez, Jose Antonio Moral, Michel Hidalgo, Miguel Company, mauropasse


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_security <https://github.com/ros2/system_tests/tree/humble/test_security/CHANGELOG.rst>`__

* Updated maintainers ([#489 ](https://github.com/ros2/system_tests/issues/489)_)
* Fix deprecated subscriber callback warnings ([#483 ](https://github.com/ros2/system_tests/issues/483)_)
* Add changelogs ([#473 ](https://github.com/ros2/system_tests/issues/473)_)
* Simplify the test_secure_subscriber code. ([#471 ](https://github.com/ros2/system_tests/issues/471)_)
* Update includes after rcutils/get_env.h deprecation ([#472 ](https://github.com/ros2/system_tests/issues/472)_)
* Contributors: Abrar Rahman Protyasha, Aditya Pande, Chris Lalancette, Christophe Bedard, Ivan Santiago Paunovic


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_tf2 <https://github.com/ros2/geometry2/tree/humble/test_tf2/CHANGELOG.rst>`__

* Fix more instances of Eigen problems on RHEL. ([#515 ](https://github.com/ros2/geometry2/issues/515)_)
* Install includes to include/${PROJECT_NAME} and use modern CMake ([#493 ](https://github.com/ros2/geometry2/issues/493)_)
* Fix precision loss from using rclcpp::Time::seconds() ([#511 ](https://github.com/ros2/geometry2/issues/511)_)
* More Intuitive CLI for Static Transform Publisher ([#392 ](https://github.com/ros2/geometry2/issues/392)_)
* Conversion tests for toMsg() ([#423 ](https://github.com/ros2/geometry2/issues/423)_)
* Deprecate tf2_geometry_msgs.h ([#418 ](https://github.com/ros2/geometry2/issues/418)_)
* Deprecate tf2_kdl.h ([#414 ](https://github.com/ros2/geometry2/issues/414)_)
* Deprecate tf2_bullet.h ([#412 ](https://github.com/ros2/geometry2/issues/412)_)
* Contributors: Bjar Ne, Chris Lalancette, Hunter L. Allen, Kenji Brameld, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_tracetools <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/test_tracetools/CHANGELOG.rst>`__

* Introduce constants for tracepoint names
* Move actual tests out of tracetools_test to new test_tracetools package
* Contributors: Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `test_tracetools_launch <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/test_tracetools_launch/CHANGELOG.rst>`__

* Add support for preloading pthread and dl instrumentation shared libs
* Remove profile_fast option and consider LD_PRELOADing both libs
* Fix multiple LdPreload actions not working and add test
* Deprecate 'context_names' param and replace with 'context_fields'
* Move some tests from tracetools_launch to test_tracetools_launch
* Contributors: Christophe Bedard, Ingo Lütkebohle


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2 <https://github.com/ros2/geometry2/tree/humble/tf2/CHANGELOG.rst>`__

* Install includes to include/${PROJECT_NAME} and use modern CMake ([#493 ](https://github.com/ros2/geometry2/issues/493)_)
* forward declare fromMsg to avoid missing symbols in downstream libraries ([#485 ](https://github.com/ros2/geometry2/issues/485)_)
* tf2: Enable common linter tests ([#469 ](https://github.com/ros2/geometry2/issues/469)_)
* Move time functions into time.cpp.
* Change a for loop to a while loop.
* Switch to C++-style casts.
* Remove totally unused (and unreachable) code.
* Replace NULL with nullptr.
* Fix up some comments.
* Use std::make_shared where we can.
* Replace two comparisons with empty string to empty().
* Make sure to include-what-you-use.
* Remove unnecessary internal method.
* Remove long-deprecated walkToTopParent overload.
* Remove unnecessary test dependencies.
* Remove some references to the ROS 1 wiki.
* Add rosidl_runtime_cpp as build_depend and build_export_depend.
* Minor cleanups in CMakeLists.txt.
* Remove include directory that doesn't exist.
* Remove completely unnecessary target_link_libraries.
* Remove unused speed_test from tf2.
* Suppress clang warnings about enumerator attributes. ([#463 ](https://github.com/ros2/geometry2/issues/463)_)
* Change TF2Error names to be a bit more descriptive. ([#349 ](https://github.com/ros2/geometry2/issues/349)_)
* Fixed errors due to missing header link. ([#432 ](https://github.com/ros2/geometry2/issues/432)_)
* Deprecate tf2_geometry_msgs.h ([#418 ](https://github.com/ros2/geometry2/issues/418)_)
* Speedup covariance unwrapping ([#399 ](https://github.com/ros2/geometry2/issues/399)_)
* Contributors: Abrar Rahman Protyasha, Chris Lalancette, Dima Dorezyuk, João C. Monteiro, Shane Loretz, Shivam Pandey


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_bullet <https://github.com/ros2/geometry2/tree/humble/tf2_bullet/CHANGELOG.rst>`__

* Install includes to include/${PROJECT_NAME} and use modern CMake ([#493 ](https://github.com/ros2/geometry2/issues/493)_)
* Export a tf2_bullet::tf2_bullet target ([#495 ](https://github.com/ros2/geometry2/issues/495)_)
* Fix cpplint errors ([#497 ](https://github.com/ros2/geometry2/issues/497)_)
* Remove some references to the ROS 1 wiki.
* Fix tf2_bullet dependency export ([#428 ](https://github.com/ros2/geometry2/issues/428)_)
* Deprecate tf2_bullet.h ([#412 ](https://github.com/ros2/geometry2/issues/412)_)
* Contributors: Bjar Ne, Chris Lalancette, Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_eigen <https://github.com/ros2/geometry2/tree/humble/tf2_eigen/CHANGELOG.rst>`__

* Workaround broken RHEL FindEigen3.cmake ([#513 ](https://github.com/ros2/geometry2/issues/513)_)
* Install includes to include/${PROJECT_NAME} and use modern CMake ([#493 ](https://github.com/ros2/geometry2/issues/493)_)
* Disable mem-access warnings on aarch64. ([#506 ](https://github.com/ros2/geometry2/issues/506)_)
* Fix cpplint errors ([#497 ](https://github.com/ros2/geometry2/issues/497)_)
* Remove some references to the ROS 1 wiki.
* Add doTransform function for twists or wrenches ([#406 ](https://github.com/ros2/geometry2/issues/406)_)
* Reenable stamped eigen tests ([#429 ](https://github.com/ros2/geometry2/issues/429)_)
* Deprecate tf2_eigen.h ([#413 ](https://github.com/ros2/geometry2/issues/413)_)
* Contributors: AndyZe, Bjar Ne, Chris Lalancette, Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_eigen_kdl <https://github.com/ros2/geometry2/tree/humble/tf2_eigen_kdl/CHANGELOG.rst>`__

* Fix more instances of Eigen problems on RHEL. ([#515 ](https://github.com/ros2/geometry2/issues/515)_)
* Depend on orocos_kdl_vendor  ([#473 ](https://github.com/ros2/geometry2/issues/473)_)
* Install includes to include/${PROJECT_NAME} and use modern CMake ([#493 ](https://github.com/ros2/geometry2/issues/493)_)
* Fix cpplint errors ([#497 ](https://github.com/ros2/geometry2/issues/497)_)
* Contributors: Chris Lalancette, Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_geometry_msgs <https://github.com/ros2/geometry2/tree/humble/tf2_geometry_msgs/CHANGELOG.rst>`__

* Make sure to find the right Python executable. ([#514 ](https://github.com/ros2/geometry2/issues/514)_)
* Depend on orocos_kdl_vendor  ([#473 ](https://github.com/ros2/geometry2/issues/473)_)
* Install includes to include/${PROJECT_NAME} and use modern CMake ([#493 ](https://github.com/ros2/geometry2/issues/493)_)
* Drop PyKDL dependency in tf2_geometry_msgs ([#509 ](https://github.com/ros2/geometry2/issues/509)_)
* Fix cpplint errors ([#497 ](https://github.com/ros2/geometry2/issues/497)_)
* Export a tf2_geometry_msgs::tf2_geometry_msgs target ([#496 ](https://github.com/ros2/geometry2/issues/496)_)
* Feature: Add doTransform for Wrench messages ([#476 ](https://github.com/ros2/geometry2/issues/476)_)
* Remove some references to the ROS 1 wiki.
* Style fixes in tf2_geometry_msgs. ([#464 ](https://github.com/ros2/geometry2/issues/464)_)
* Fix for issue [#431 ](https://github.com/ros2/geometry2/issues/431)_ - Covariance is not transformed in do_transform_pose_with_covariance_stamped ([#453 ](https://github.com/ros2/geometry2/issues/453)_)
* doTransform non stamped msgs ([#452 ](https://github.com/ros2/geometry2/issues/452)_)
* ``tf2_geometry_msgs``: Fixing covariance transformation in ``doTransform<PoseWithCovarianceStamped, TransformStamped>[` (`#430 ](https://github.com/ros2/geometry2/issues/430)_)
* Geometry nitpicks ([#426 ](https://github.com/ros2/geometry2/issues/426)_)
* Conversion tests for toMsg() ([#423 ](https://github.com/ros2/geometry2/issues/423)_)
* Deprecate tf2_geometry_msgs.h ([#418 ](https://github.com/ros2/geometry2/issues/418)_)
* Contributors: Abrar Rahman Protyasha, Bjar Ne, Chris Lalancette, Denis Štogl, Florian Vahl, Jacob Perron, Khasreto, Shane Loretz, vineet131


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_kdl <https://github.com/ros2/geometry2/tree/humble/tf2_kdl/CHANGELOG.rst>`__

* Depend on orocos_kdl_vendor  ([#473 ](https://github.com/ros2/geometry2/issues/473)_)
* Install includes to include/${PROJECT_NAME} and use modern CMake ([#493 ](https://github.com/ros2/geometry2/issues/493)_)
* KDL python formatting and licenses ([#425 ](https://github.com/ros2/geometry2/issues/425)_)
* Deprecate tf2_kdl.h ([#414 ](https://github.com/ros2/geometry2/issues/414)_)
* Contributors: Bjar Ne, Chris Lalancette, Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_msgs <https://github.com/ros2/geometry2/tree/humble/tf2_msgs/CHANGELOG.rst>`__

* Remove dead file from tf2_msgs ([#415 ](https://github.com/ros2/geometry2/issues/415)_)
* Contributors: Chris Lalancette


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_py <https://github.com/ros2/geometry2/tree/humble/tf2_py/CHANGELOG.rst>`__

* Make sure to finalize tf2_py BufferCore. ([#505 ](https://github.com/ros2/geometry2/issues/505)_)
* Make tf2_py Use FindPython3 ([#494 ](https://github.com/ros2/geometry2/issues/494)_)
* Change TF2Error names to be a bit more descriptive. ([#349 ](https://github.com/ros2/geometry2/issues/349)_)
* Remove python_compat.h ([#417 ](https://github.com/ros2/geometry2/issues/417)_)
* Contributors: Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_ros <https://github.com/ros2/geometry2/tree/humble/tf2_ros/CHANGELOG.rst>`__

* Install includes to include/${PROJECT_NAME} and use modern CMake ([#493 ](https://github.com/ros2/geometry2/issues/493)_)
* use dedicated callback group and executor to isolate timer ([#447 ](https://github.com/ros2/geometry2/issues/447)_)
* Adding shared pointer definition to tf2 buffer ([#508 ](https://github.com/ros2/geometry2/issues/508)_)
* fix for a basic logic ([#510 ](https://github.com/ros2/geometry2/issues/510)_)
* Fix precision loss from using rclcpp::Time::seconds() ([#511 ](https://github.com/ros2/geometry2/issues/511)_)
* clear relative callback of Buffer if MessageFilter is destroyed ([#490 ](https://github.com/ros2/geometry2/issues/490)_)
* More info in tf2_echo output ([#468 ](https://github.com/ros2/geometry2/issues/468)_)
* Fix cpplint errors ([#497 ](https://github.com/ros2/geometry2/issues/497)_)
* Fixes for uncrustify 0.72 ([#486 ](https://github.com/ros2/geometry2/issues/486)_)
* More Intuitive CLI for Static Transform Publisher ([#392 ](https://github.com/ros2/geometry2/issues/392)_)
* Reduce transform listener nodes ([#442 ](https://github.com/ros2/geometry2/issues/442)_)
* [`tf2_ros``: Fix deprecated subscriber callbacks (`#448 ](https://github.com/ros2/geometry2/issues/448)_)
* Fix tf2_echo does not work with ros-args ([#407 ](https://github.com/ros2/geometry2/issues/407)_) ([#408 ](https://github.com/ros2/geometry2/issues/408)_)
* Contributors: Abrar Rahman Protyasha, Chen Lihui, Chris Lalancette, Hunter L. Allen, Jacob Perron, Kenji Brameld, PGotzmann, Shane Loretz, Steve Macenski, Zhenpeng Ge, gezp, simulacrus


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_ros_py <https://github.com/ros2/geometry2/tree/humble/tf2_ros_py/CHANGELOG.rst>`__

* Drop PyKDL dependency in tf2_geometry_msgs ([#509 ](https://github.com/ros2/geometry2/issues/509)_)
* Add in one more destroy call that was missed in testing. ([#504 ](https://github.com/ros2/geometry2/issues/504)_)
* Be much more careful about cleanup in the tf2_ros_py tests. ([#499 ](https://github.com/ros2/geometry2/issues/499)_)
* Use the correct type for BufferClient timeout_padding. ([#498 ](https://github.com/ros2/geometry2/issues/498)_) It should be a duration, not a float.
* Update maintainers to Alejandro Hernandez Cordero and Chris Lalancette ([#481 ](https://github.com/ros2/geometry2/issues/481)_)
* Fix buffer_client.py using default timeout_padding ([#437 ](https://github.com/ros2/geometry2/issues/437)_)
* Use underscores instead of dashes in setup.cfg. ([#403 ](https://github.com/ros2/geometry2/issues/403)_)
* Contributors: Audrow Nash, Carlos Andrés Álvarez Restrepo, Chris Lalancette, Florian Vahl


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_sensor_msgs <https://github.com/ros2/geometry2/tree/humble/tf2_sensor_msgs/CHANGELOG.rst>`__

* Disable mem-access warnings on aarch64. ([#506 ](https://github.com/ros2/geometry2/issues/506)_)
* Fix cpplint errors ([#497 ](https://github.com/ros2/geometry2/issues/497)_)
* Reenable sensor_msgs test ([#422 ](https://github.com/ros2/geometry2/issues/422)_)
* Deprecate tf2_sensor_msgs.h ([#416 ](https://github.com/ros2/geometry2/issues/416)_)
* Contributors: Bjar Ne, Chris Lalancette, Jacob Perron


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tf2_tools <https://github.com/ros2/geometry2/tree/humble/tf2_tools/CHANGELOG.rst>`__

* Update maintainers to Alejandro Hernandez Cordero and Chris Lalancette ([#481 ](https://github.com/ros2/geometry2/issues/481)_)
* Remove unused import ([#465 ](https://github.com/ros2/geometry2/issues/465)_)
* Adding date-time to frames filename ([#454 ](https://github.com/ros2/geometry2/issues/454)_)
* Use underscores instead of dashes in setup.cfg. ([#403 ](https://github.com/ros2/geometry2/issues/403)_)
* Contributors: Audrow Nash, Hannu Henttinen, Nisala Kalupahana


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tlsf <https://github.com/ros2/tlsf/tree/humble/tlsf/CHANGELOG.rst>`__

* Install headers to include/${PROJECT_NAME} ([#11 ](https://github.com/ros2/tlsf/issues/11)_)
* Export a modern CMake target instead of old-style variables ([#10 ](https://github.com/ros2/tlsf/issues/10)_)
* Contributors: Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tlsf_cpp <https://github.com/ros2/realtime_support/tree/humble/tlsf_cpp/CHANGELOG.rst>`__

* Install includes to include/${PROJECT_NAME} ([#114 ](https://github.com/ros2/realtime_support/issues/114)_)
* Export modern CMake targets ([#110 ](https://github.com/ros2/realtime_support/issues/110)_)
* Remove the use of malloc hooks from the tlsf_cpp tests. ([#109 ](https://github.com/ros2/realtime_support/issues/109)_)
* Contributors: Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `topic_monitor <https://github.com/ros2/demos/tree/humble/topic_monitor/CHANGELOG.rst>`__

* Update maintainers to Audrow Nash and Michael Jeronimo ([#543 ](https://github.com/ros2/demos/issues/543)_)
* Small cleanups to the topic monitor. ([#517 ](https://github.com/ros2/demos/issues/517)_)
* Fix topic_monitor for high publication rate ([#461 ](https://github.com/ros2/demos/issues/461)_)
* Use is_alive for threads. ([#510 ](https://github.com/ros2/demos/issues/510)_)
* Contributors: Audrow Nash, Chris Lalancette, Elias De Coninck


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `topic_statistics_demo <https://github.com/ros2/demos/tree/humble/topic_statistics_demo/CHANGELOG.rst>`__

* Install includes to include/${PROJECT_NAME} ([#548 ](https://github.com/ros2/demos/issues/548)_)
* Additional fixes for documentation in demos. ([#538 ](https://github.com/ros2/demos/issues/538)_)
* Fixing deprecated subscriber callback warnings ([#532 ](https://github.com/ros2/demos/issues/532)_)
* Contributors: Abrar Rahman Protyasha, Chris Lalancette, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools/CHANGELOG.rst>`__

* Install headers to include/${PROJECT_NAME}
* Merge branch 'update-mentions-of-tracetools-test' into 'master' Update applicable mentions of tracetools_test to test_tracetools See merge request [ros-tracing/ros2_tracing!259 ](https://gitlab.com/ros-tracing/ros2_tracing/-/merge_requests/259)_
* Update applicable mentions of tracetools_test to test_tracetools
* Merge branch 'version-3-1-0' into 'master' Version 3.1.0 See merge request [ros-tracing/ros2_tracing!256 ](https://gitlab.com/ros-tracing/ros2_tracing/-/merge_requests/256)_
* Correctly handle calls to TRACEPOINT() macro with no tracepoint args
* Move publisher handle tracepoint argument from rclcpp_publish to rcl_publish
* Add support for rmw init/pub, take, and executor instrumentation
* Export target on Windows and export an interface if TRACETOOLS_DISABLED
* Remove deprecated utility functions
* Contributors: Christophe Bedard, Ivan Santiago Paunovic, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools_launch <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools_launch/CHANGELOG.rst>`__

* Disable kernel tracing by default
* Don't require kernel tracer and detect when it's not installed
* Add support for preloading pthread and dl instrumentation shared libs
* Remove profile_fast option and consider LD_PRELOADing both libs
* Improve event matching for shared lib preloading
* Improve LdPreload action's lib-finding function and add proper tests
* Fix multiple LdPreload actions not working and add test
* Deprecate 'context_names' param and replace with 'context_fields'
* Support per-domain context fields for the Trace action
* Improve LdPreload.get_shared_lib_path() for when a static lib may exist
* Move some tests from tracetools_launch to test_tracetools_launch
* Expose Trace action as frontend action and support substitutions
* Contributors: Christophe Bedard, Ingo Lütkebohle


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools_test <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools_test/CHANGELOG.rst>`__

* Allow providing additional actions for TraceTestCase
* Remove default value for 'package' kwarg for TraceTestCase
* Move actual tests out of tracetools_test to new test_tracetools package
* Add tests for rmw init/pub, take, and executor instrumentation
* Add field type assertion utilities to TraceTestCase
* Fixing deprecated subscriber callback warnings
* Contributors: Abrar Rahman Protyasha, Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `tracetools_trace <https://gitlab.com/ros-tracing/ros2_tracing/-/blob/humble/tracetools_trace/CHANGELOG.rst>`__

* Disable kernel tracing by default
* Don't require kernel tracer and detect when it's not installed
* Introduce constants for tracepoint names
* Optimize default tracing session channel config values
* Deprecate 'context_names' param and replace with 'context_fields'
* Support per-domain context fields for the Trace action
* Add support for rmw init/pub, take, and executor tracepoints
* Contributors: Christophe Bedard


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `trajectory_msgs <https://github.com/ros2/common_interfaces/tree/humble/trajectory_msgs/CHANGELOG.rst>`__

* Interface packages should fully <depend> on the interface packages that they depend on ([#173 ](https://github.com/ros2/common_interfaces/issues/173)_)
* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Contributors: Audrow Nash, Grey


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `turtlesim <https://github.com/ros/ros_tutorials/tree/humble-devel/turtlesim/CHANGELOG.rst>`__

* Use [`double`` when handling ``qreal orient\_`` (`#114 ](https://github.com/ros/ros_tutorials/issues/114)_)
* Add Rolling Icon ([#133 ](https://github.com/ros/ros_tutorials/issues/133)_)
* Update maintainers to Audrow Nash and Michael Jeronimo ([#137 ](https://github.com/ros/ros_tutorials/issues/137)_)
* Fixing deprecated subscriber callback warnings ([#134 ](https://github.com/ros/ros_tutorials/issues/134)_)
* Use rosidl_get_typesupport_target() ([#132 ](https://github.com/ros/ros_tutorials/issues/132)_)
* Print out the correct node name on startup. ([#122 ](https://github.com/ros/ros_tutorials/issues/122)_)
* Contributors: Abrar Rahman Protyasha, Audrow Nash, Chris Lalancette, Katherine Scott, Seulbae Kim, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `urdf <https://github.com/ros2/urdf/tree/humble/urdf/CHANGELOG.rst>`__

* Install headers to include/${PROJECT_NAME} ([#31 ](https://github.com/ros2/urdf/issues/31)_)
* Add linter tests and fix errors ([#30 ](https://github.com/ros2/urdf/issues/30)_)
* Add in a Doxyfile to predefine macros. ([#28 ](https://github.com/ros2/urdf/issues/28)_)
* Contributors: Chris Lalancette, Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `urdf_parser_plugin <https://github.com/ros2/urdf/tree/humble/urdf_parser_plugin/CHANGELOG.rst>`__

* Install headers to include/${PROJECT_NAME} ([#31 ](https://github.com/ros2/urdf/issues/31)_)
* Add linter tests and fix errors ([#30 ](https://github.com/ros2/urdf/issues/30)_)
* Contributors: Jacob Perron, Shane Loretz


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `visualization_msgs <https://github.com/ros2/common_interfaces/tree/humble/visualization_msgs/CHANGELOG.rst>`__

* Interface packages should fully <depend> on the interface packages that they depend on ([#173 ](https://github.com/ros2/common_interfaces/issues/173)_)
* Update maintainers to Geoffrey Biggs and Tully Foote ([#163 ](https://github.com/ros2/common_interfaces/issues/163)_)
* Marker Textures ([#153 ](https://github.com/ros2/common_interfaces/issues/153)_)
* Document namespace scoped marker deletion. ([#151 ](https://github.com/ros2/common_interfaces/issues/151)_)
* Contributors: Audrow Nash, Greg Balke, Grey, Michel Hidalgo


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `yaml_cpp_vendor <https://github.com/ros2/yaml_cpp_vendor/tree/humble/CHANGELOG.rst>`__

* Add missing dependency on yaml-cpp ([#32 ](https://github.com/ros2/yaml_cpp_vendor/issues/32)_)
* Upgrade to yaml-cpp 0.7.0 ([#25 ](https://github.com/ros2/yaml_cpp_vendor/issues/25)_)
* Contributors: Chris Lalancette, Scott K Logan


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# `zstd_vendor <https://github.com/ros2/rosbag2/tree/humble/zstd_vendor/CHANGELOG.rst>`__

* Bump version number to avoid conflict
* Use git hash for zstd vendor ([#969 ](https://github.com/ros2/rosbag2/issues/969)_)
* Update package maintainers ([#899 ](https://github.com/ros2/rosbag2/issues/899)_)
* Declare missing dependency on 'git' in zstd_vendor ([#890 ](https://github.com/ros2/rosbag2/issues/890)_)
* Switch to using 'git apply' for zstd_vendor patches ([#846 ](https://github.com/ros2/rosbag2/issues/846)_)
* Contributors: Chris Lalancette, Christophe Bedard, Michel Hidalgo, Scott K Logan, Shane Loretz


---
[返回](../index.md)
