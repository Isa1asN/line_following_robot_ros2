from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.actions import ExecuteProcess


def generate_launch_description():
    ld = LaunchDescription()

    package_name = "simple_robot_description"

    gazebo_launch = IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py']),
        launch_arguments={
            'world': PathJoinSubstitution([FindPackageShare(package_name), 'worlds', 'empty.world']),
            }.items()
    )

    simple_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'robot', '-x', '0.0', '-y', '0.0', '-z', '1.0',
                   '-file', PathJoinSubstitution([FindPackageShare(package_name),  'models', 'arm_1dof.xacro'])])
    

    # add joint_state_publisher
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        arguments=[PathJoinSubstitution([FindPackageShare(package_name), 'models', 'arm_1dof.xacro'])])
    
    # add robot_state_publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        arguments=[PathJoinSubstitution([FindPackageShare(package_name), 'models', 'arm_1dof.xacro'])])
    
    # move_robot = Node(
    #     package='simple_robot_description',
    #     executable='joint_commander',
    #     name='move_robot'
    # )




    ld.add_action(gazebo_launch)
    ld.add_action(simple_robot)

    ld.add_action(joint_state_publisher)
    ld.add_action(robot_state_publisher)

    # ld.add_action(move_robot)


    return ld

# ros2 run controller_manager spawner joint_trajectory_controller
# ros2 run simple_robot_description joint_commander

# ros2 run image_tools showimage --ros-args --remap image:=/camera1/image_raw

# export GAZEBO_MODEL_PATH=/home/esayas/Desktop/line_follower/src/simple_robot_description/models:$GAZEBO_MODEL_PATH
