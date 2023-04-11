# mini_pupper_ros_demos

## Installation

```sh
mkdir -p ~/demos_ws/src
cd ~/demos_ws/src
git clone https://github.com/hdumcke/mini_pupper_ros_demos.git
cd ~/demos_ws
colcon build --symlink-install
```

## Run demos

### Show URDF model
```sh
source ~/demos_ws/install/setup.bash
ros2 launch mini_pupper_description urdf_viewer.launch.py
```

### Show Camera
```sh
source ~/demos_ws/install/setup.bash
ros2 launch mini_pupper_viewers camera_viewer.launch.py
```

### Show IMU
```sh
sudo apt install -y ros-humble-rviz-imu-plugin
source ~/demos_ws/install/setup.bash
ros2 launch mini_pupper_viewers imu_viewer.launch.py
```

### Show Lidar
```sh
source ~/demos_ws/install/setup.bash
ros2 launch mini_pupper_viewers ld06_viewer.launch.py
```

### opencv demo
```sh
source ~/demos_ws/install/setup.bash
ros2 run opencv_demo opencv_demo
```

In a new terminal:

```sh
ros2 run rqt_image_view rqt_image_view
```

/image_raw shows the image from the camera
/opencv_tests/images shows the image manipulated by openCV
