from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    ur_type = LaunchConfiguration("ur_type")
    use_fake_hardware = LaunchConfiguration("use_fake_hardware")
    com_port = LaunchConfiguration("com_port")

    xacro_file = os.path.join(
        get_package_share_directory("ur_robotiq_description"),
        "urdf",
        "ur3_robotiq_140.urdf.xacro"
    )

    robot_description = ParameterValue(
        Command([
            "xacro ",
            xacro_file,
            " ur_type:=", ur_type,
            " use_fake_hardware:=", use_fake_hardware,
            " com_port:=", com_port,
        ]),
        value_type=str
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "ur_type",
            default_value="ur3",
            description="UR robot type"
        ),
        DeclareLaunchArgument(
            "use_fake_hardware",
            default_value="true",
            description="Use fake hardware for visualization"
        ),
        DeclareLaunchArgument(
            "com_port",
            default_value="/dev/ttyUSB0",
            description="Serial port for gripper"
        ),

        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            output="screen",
            parameters=[{"robot_description": robot_description}],
        ),

        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            output="screen",
        ),

        Node(
            package="rviz2",
            executable="rviz2",
            output="screen",
        ),
    ])