# ros2 run image_tools showimage --ros-args --remap image:=/camera1/image_raw
import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from scipy.ndimage.measurements import center_of_mass
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

TURN_LEFT_SPD = 0.15
TURN_RIGHT_SPD = 0.125
STRAIGHT_SPD = 0.25
ANGULAR_VEL = 0.4
OFFSET_Y = 500
TIMER_PERIOD = 1

prev = (400, 400)

def image_callback(msg):

    global img_grayscale
    img_grayscale = bridge.imgmsg_to_cv2(msg,desired_encoding='mono8')

def callback():
    global prev
    global img_grayscale

    try:
        # img_grayscale = bridge.imgmsg_to_cv2(data, 'mono8')
        _, img_bin = cv2.threshold(img_grayscale, 128, 1, cv2.THRESH_BINARY_INV)

        # print('we are here', img_bin.shape)

        coords_bin = center_of_mass(img_bin[-300:])
        y = coords_bin[0] + OFFSET_Y
        x = coords_bin[1]

        if np.isnan(x) or np.isnan(y):
            x = prev[0]
            y = prev[1]
        else:
            prev = (x, y)
    
        print((x,y))

        move = Twist()

        if x < 350:
            move.linear.x = TURN_LEFT_SPD
            move.angular.z = ANGULAR_VEL
            pub.publish(move)
        elif x >= 350 and x <= 450:
            move.linear.x = STRAIGHT_SPD
            move.angular.z = 0.0
            pub.publish(move)
        else:
            move.linear.x = TURN_RIGHT_SPD
            move.angular.z = -1 * ANGULAR_VEL
            pub.publish(move)

        # move.angular.z = 0.9
        # move.linear.x = 0.0
        # pub.publish(move)

    except Exception as e:
        print(e)

def main(args=None):
    rclpy.init(args=args)

    global bridge, pub
    bridge = CvBridge()
    node = rclpy.create_node('move_robot')
    sub = node.create_subscription(Image, '/camera1/image_raw', image_callback, rclpy.qos.qos_profile_sensor_data)
    pub = node.create_publisher(Twist, '/cmd_vel', rclpy.qos.qos_profile_system_default)
    rate = node.create_rate(2)
    timer = node.create_timer(TIMER_PERIOD, callback=callback)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
