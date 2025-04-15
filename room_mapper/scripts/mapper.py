#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    rospy.loginfo(f"Received scan with {len(msg.ranges)} points")
    if msg.ranges:
        rospy.loginfo(f"First range value: {msg.ranges[0]:.2f} m")

def main():
    rospy.init_node('scan_subscriber', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, scan_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
