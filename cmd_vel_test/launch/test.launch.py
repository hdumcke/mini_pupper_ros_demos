import os
import launch
from launch_ros.actions import Node
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    config_dir = os.path.join(get_package_share_directory('cmd_vel_test'), 'config')

    cmd_vel_node = Node(package='cmd_vel_test',
                        executable='cmd_vel_test',
                        output='screen',
                        parameters=[
                            os.path.join(config_dir, 'cmd_vel_test.yaml')
                            ])
    return launch.LaunchDescription([cmd_vel_node])
