import os

import launch
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg_share = FindPackageShare('mini_pupper_navigation').find('mini_pupper_navigation')
    conf_dir = os.path.join(pkg_share, 'config')
    conf_file = os.path.join(conf_dir, 'robot_localization.config.yaml')
    loc = Node(package='robot_localization',
               executable='ekf_node',
               name='ekf_filter_node',
               output='screen',
               parameters=[conf_file],
               remappings=[("imu", "imu/data")]
               )

    return launch.LaunchDescription([loc])
