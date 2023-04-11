import cv2

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge


class OpenCVDemo(Node):

    def __init__(self):
        super().__init__('line_follower')
        self.subscription = self.create_subscription(
            Image,
            'image_raw',
            self.listener_callback,
            10)
        self.pub_img = self.create_publisher(Image,
                                             "/opencv_tests/images", 10)
        self.cvb = CvBridge()
        self.ball_xv = 10
        self.ball_yv = 10
        self.ball_x = 100
        self.ball_y = 100

    def listener_callback(self, msg):
        image_input = self.cvb.imgmsg_to_cv2(msg,
                                             desired_encoding='bgr8')
        self.get_logger().info("Got image: %s" % msg.encoding)

        cv2.circle(image_input, (self.ball_x, self.ball_y), 10, 255, -1)

        self.ball_x += self.ball_xv
        self.ball_y += self.ball_yv
        if self.ball_x in [10, 630]:
            self.ball_xv = -self.ball_xv
        if self.ball_y in [10, 470]:
            self.ball_yv = -self.ball_yv

        out_msg = self.cvb.cv2_to_imgmsg(image_input)
        out_msg.header.frame_id = msg.header.frame_id
        out_msg.encoding = 'bgr8'
        self.pub_img.publish(out_msg)


def main(args=None):
    rclpy.init(args=args)

    demo = OpenCVDemo()

    rclpy.spin(demo)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    demo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
