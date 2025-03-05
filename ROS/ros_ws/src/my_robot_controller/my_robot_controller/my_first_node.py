#!usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):
    
    def __init__(self):
        super().__init__("first_node")
        self.create_timer(1.5, self.timer_callback)
        self.counter_ = 0
    
    def timer_callback(self):
        self.get_logger().info(f'ROS 2 counts {self.counter_}')
        self.counter_ += 1


def main(args=None):
    rclpy.init(args=args)

    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
