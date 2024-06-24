%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-rqt-console
Version:        2.2.1
Release:        4%{?dist}%{?release_suffix}
Summary:        ROS rqt_console package

License:        BSD
URL:            http://wiki.ros.org/rqt_console
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jazzy-ament-index-python
Requires:       ros-jazzy-python-qt-binding >= 0.2.19
Requires:       ros-jazzy-rcl-interfaces
Requires:       ros-jazzy-rclpy
Requires:       ros-jazzy-rqt-gui
Requires:       ros-jazzy-rqt-gui-py
Requires:       ros-jazzy-rqt-py-common
Requires:       ros-jazzy-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif

%description
rqt_console provides a GUI plugin for displaying and filtering ROS messages.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/jazzy"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Mon Jun 24 2024 Dharini Dutia <dharini@openrobotics.org> - 2.2.1-4
- Autogenerated by Bloom

* Fri Apr 19 2024 Dharini Dutia <dharini@openrobotics.org> - 2.2.1-3
- Autogenerated by Bloom

* Wed Mar 06 2024 Dharini Dutia <dharini@openrobotics.org> - 2.2.1-2
- Autogenerated by Bloom

