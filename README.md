# line_following_robot_ros2
A line track follower robot using ros2 and cv2

<video src='' width='600'/>

Add the model path to env:
- export GAZEBO_MODEL_PATH=/home/esayas/Desktop/line_follower/src/simple_robot_description/models:$GAZEBO_MODEL_PATH

To launch:
- ros2 launch simple_robot_description gazebo.launch.py

To view the camera feed:
- ros2 run image_tools showimage --ros-args --remap image:=/camera1/image_raw

To run the line follower script:
- ros2 run simple_robot_description joint_commander
