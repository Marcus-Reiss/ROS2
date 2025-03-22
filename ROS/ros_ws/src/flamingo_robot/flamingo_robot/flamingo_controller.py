#!usr/bin/env python3
import rclpy
from rclpy.node import Node
import torch
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray


class FlamingoController(Node):

    def __init__(self):

        super().__init__("flamingo_controller")
        self.declare_parameter('policy_path', 'policy.pt')
        policy_path = self.get_parameter('policy_path').value

        # Loading the policy
        self.policy = torch.jit.load(policy_path)
        self.policy.eval()

        # Subscribers
        self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        self.create_subscription(JointState, 'joint_state', self.joint_state_callback, 10)

        # Publisher
        self.joint_cmd_pub = self.create_publisher(Float64MultiArray, 'joint_command', 10)

        # Variables to store state
        self.joint_positions = None
        self.joint_velocities = None
        self.angular_pos_base = None
        self.angular_vel_base = None
        self.last_action = None

    def cmd_vel_callback(self, msg):

        #
        pass

    def joint_state_callback(self, msg):

        # Mapping joint names to positions
        self.joint_positions = torch.tensor(msg.position, dtype=torch.float32)
        self.joint_velocities = torch.tensor(msg.velocity, dtype=torch.float32)

        # Preparing inputs for the policy
        if self.joint_positions is not None and self.joint_velocities is not None:
            input_tensor = torch.cat([self.joint_positions, self.joint_velocities])
            if self.last_action is not None:
                input_tensor = torch.cat([input_tensor, self.last_action])

        # Computing the action
        action = self.policy(input_tensor)
        self.last_action = action  # Updates last_action

        # Publishing the action
        cmd_msg = Float64MultiArray()
        cmd_msg.data = action.tolist()
        self.joint_cmd_pub.publish(cmd_msg)
    
def main(args=None):

    rclpy.init(args=args)

    node = FlamingoController()
    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()
