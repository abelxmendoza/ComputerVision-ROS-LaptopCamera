#!/usr/bin/env python

    """
    This is a Python script that captures video from the default camera (index 0) of the computer 
    and publishes it as a ROS Image message. It uses the OpenCV library for capturing and processing 
    the frames and the cv_bridge library for converting the OpenCV images to ROS Image messages. 
    The captured video frames are continuously displayed in a window until the user presses the 'q' key. 
    This script can be used as a ROS node to stream camera data to other ROS nodes for further processing or visualization.
    """

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def main():
    rospy.init_node('camera_publisher', anonymous=True)
    bridge = CvBridge()
    pub = rospy.Publisher('camera_image', Image, queue_size=10)
    cap = cv2.VideoCapture(0)

    while not rospy.is_shutdown():
        ret, frame = cap.read()

        try:
            image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            pub.publish(image_msg)
        except CvBridgeError as e:
            print(e)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

