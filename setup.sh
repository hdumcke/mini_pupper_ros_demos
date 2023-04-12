#!/bin/bash
#
# This is for installation in vurtual machines.
# Be carerfull if you run this on your PC as it might overwrite parts of your installation
#

set -e

### Get directory where this script is installed
BASEDIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

sudo apt install -y python-is-python3

### Install pip
cd /tmp
wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

### Install ROS2
cd ~
git clone https://github.com/Tiryoh/ros2_setup_scripts_ubuntu.git
./ros2_setup_scripts_ubuntu/run.sh

### INstall demos
mkdir -p ~/demos_ws/src
cd ~/demos_ws/src
git clone https://github.com/hdumcke/mini_pupper_ros_demos.git
cd ~/demos_ws
rosdep update && rosdep install --from-path src --ignore-src -y --skip-keys microxrcedds_agent --skip-keys micro_ros_agent
sudo pip install setuptools==58.2.0 # suppress colcon build warning
colcon build --symlink-install

# Cyclon DDS
sudo apt install -y ros-humble-rmw-cyclonedds-cpp
echo 'export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp' >> ~/.bashrc

echo 'export ROS_DOMAIN_ID=0' >> ~/.bashrc
