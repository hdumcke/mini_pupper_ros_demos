import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor

from geometry_msgs.msg import Twist

class CmdVelTest(Node):

    def __init__(self):
        super().__init__('cmd_vel_test')
        self.declare_params()
        self.set_params()
        self.get_logger().info("frequency: %s" % self.frequency)
        self.get_logger().info("duration: %s" % self.duration)
        self.get_logger().info("max_velocity: %s" % self.max_velocity)
        self.pub = self.create_publisher(Twist,
                                         "/cmd_vel",
                                         10)
        self.time_start = self.get_clock().now().nanoseconds
        self.current_velocity = 0.0
        timer = self.create_timer(1 / self.frequency, self.timer_callback)

    def declare_params(self):
        self.declare_parameter('frequency', 5, ParameterDescriptor(description='cmd_vel publish frequency in Hz'))
        self.declare_parameter('change_rate', 3, ParameterDescriptor(description='how fast to change to ax_velocity'))
        self.declare_parameter('duration', 2.0, ParameterDescriptor(description='duration in sec'))
        self.declare_parameter('max_velocity', 0.2, ParameterDescriptor(description='max velocity in m/sec'))

    def set_params(self):
        self.frequency = self.get_parameter('frequency').get_parameter_value().integer_value
        self.change_rate = self.get_parameter('change_rate').get_parameter_value().integer_value
        self.duration = self.get_parameter('duration').get_parameter_value().double_value
        self.max_velocity = self.get_parameter('max_velocity').get_parameter_value().double_value


    def timer_callback(self):
        if self.get_clock().now().nanoseconds - self.time_start > self.duration * 1e+9:
             self.current_velocity -= self.max_velocity / self.change_rate
        else:
             self.current_velocity += self.max_velocity / self.change_rate
        if self.current_velocity > self.max_velocity:
            self.current_velocity = self.max_velocity
        if self.current_velocity < 0.0:
            self.current_velocity = 0.0
        msg = Twist()
        msg.linear.x, msg.linear.y, msg.angular.z = self.get_velocity()
        self.pub.publish(msg)

    def get_velocity(self):
        x = self.current_velocity
        y = 0.0
        z = 0.0
        return x, y, z


def main(args=None):
    rclpy.init(args=args)

    node = CmdVelTest()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
