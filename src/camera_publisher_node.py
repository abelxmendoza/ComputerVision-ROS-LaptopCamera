#!/usr/bin/env python

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

