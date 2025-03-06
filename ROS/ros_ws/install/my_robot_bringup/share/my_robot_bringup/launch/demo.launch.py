from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    talker_node = Node(
        package="demo_nodes_cpp",
        executable="talker",
        name="vardomiro_talker",
        remappings= [
            ("chatter", "kiss_flowers")
        ]
    )

    listener_node = Node(
        package="demo_nodes_py",
        executable="listener",
        remappings= [
            ("chatter", "kiss_flowers")
        ]
    )

    ld.add_action(talker_node)
    ld.add_action(listener_node)

    return ld
