# Line Following Robot using ROS2 and OpenCV

[YouTube video](https://youtu.be/0nfNSA2cqoE?si=NMAKeIKJ6WOGHYg-)


## Setup

Before running the robot, add the model path to the environment:

```bash
export GAZEBO_MODEL_PATH=/home/esayas/Desktop/line_follower/src/simple_robot_description/models:$GAZEBO_MODEL_PATH
```

## Launch Gazebo Simulation

To launch the Gazebo simulation, use the following command:

```bash
ros2 launch simple_robot_description gazebo.launch.py
```
## View Camera Feed

To view the camera feed, run the following command:

```bash
ros2 run image_tools showimage --ros-args --remap image:=/camera1/image_raw
```
## Run Line Follower Script

To execute the line follower script, use the following command:

```bash
ros2 run simple_robot_description joint_commander
```
