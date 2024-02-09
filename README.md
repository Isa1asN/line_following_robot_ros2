# Line Following Robot using ROS2 and OpenCV

[![Line Following Robot Video](https://github.com/Isa1asN/line_following_robot_ros2/blob/main/Screencast%20from%2002-09-2024%2001_43_40%20PM.mp4)](https://github.com/Isa1asN/line_following_robot_ros2/blob/main/Screencast%20from%2002-09-2024%2001_43_40%20PM.mp4)

## Setup

Before running the robot, add the model path to the environment:

```bash
export GAZEBO_MODEL_PATH=/home/esayas/Desktop/line_follower/src/simple_robot_description/models:$GAZEBO_MODEL_PATH

## Launch Gazebo Simulation

To launch the Gazebo simulation, use the following command:

```bash
ros2 launch simple_robot_description gazebo.launch.py

## View Camera Feed

To view the camera feed, run the following command:

```bash
ros2 run image_tools showimage --ros-args --remap image:=/camera1/image_raw

## Run Line Follower Script

To execute the line follower script, use the following command:

```bash
ros2 run simple_robot_description joint_commander
