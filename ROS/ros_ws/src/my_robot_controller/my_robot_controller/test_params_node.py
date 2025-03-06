#!usr/bin/env python3

import rclpy
from rclpy.node import Node


class MyTestParamsNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.declare_parameters(
            namespace='',
            parameters=[
                ('bool_value', rclpy.Parameter.Type.BOOL),
                ('int_number', rclpy.Parameter.Type.INTEGER),
                ('float number', rclpy.Parameter.Type.DOUBLE),
                ('str_text', rclpy.Parameter.Type.STRING),
                ('bool_array', rclpy.Parameter.Type.BOOL_ARRAY),
                ('nested_param.another_int', rclpy.Parameter.Type.INTEGER),
            ]
        )

def main(args=None):
    rclpy.init(args=args)

    node = MyTestParamsNode()
    rclpy.spin(node)

    rclpy.shutdown()
