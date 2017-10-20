Name:		ros-kinetic-comm-msgs
Version:	1.11.2
Release:	0
Summary:	ROS comm-msgs package
License:	BSD
URL:		https://github.com/ros/ros_comm_msgs.git
Source0:	%{name}-%{version}.tar.gz
Source1001:	ros-kinetic-comm-msgs.manifest
BuildRequires:	cmake
BuildRequires:	ros-kinetic-catkin
BuildRequires:	ros-kinetic-message-generation
BuildRequires:	ros-kinetic-std-msgs

%description
Messages relating to the ROS Computation Graph. These are generally considered to be low-level messages that end users do not interact with.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%{__ros_setup}

pushd rosgraph_msgs
%{__ros_build}
popd

pushd std_srvs
%{__ros_build}
popd

%install
%{__ros_setup}

pushd rosgraph_msgs
%{__ros_install}
popd

pushd std_srvs
%{__ros_install}
popd

%package -n ros-kinetic-rosgraph-msgs
Summary:	ROS rosgraph_msgs package
Requires:	ros-kinetic-message-runtime
Requires:	ros-kinetic-std-msgs
%description -n ros-kinetic-rosgraph-msgs
Messages relating to the ROS Computation Graph. These are generally considered to be low-level messages that end users do not interact with.
%files -n ros-kinetic-rosgraph-msgs -f rosgraph_msgs/build/install_manifest.txt
%manifest ros-kinetic-comm-msgs.manifest
%defattr(-,root,root)

%package -n ros-kinetic-std-srvs
Summary:	ROS std_srvs package
Requires:	ros-kinetic-message-runtime
%description -n ros-kinetic-std-srvs
Common service definitions.
%files -n ros-kinetic-std-srvs -f std_srvs/build/install_manifest.txt
%manifest ros-kinetic-comm-msgs.manifest
%defattr(-,root,root)
