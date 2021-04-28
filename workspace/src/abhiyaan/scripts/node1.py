#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def node1():
    pub = rospy.Publisher('team_abhiyaan', String, queue_size=10)
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
    	n1_str = "Team Abhiyaan"
    	rospy.loginfo(n1_str)
    	pub.publish(n1_str)
    	rate.sleep()

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass

