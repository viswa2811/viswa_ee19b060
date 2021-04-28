#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def node2():
    pub = rospy.Publisher('autonomy', String, queue_size=10)
    rospy.init_node('node2', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
    	n1_str = "Fueled By Autonomy"
    	rospy.loginfo(n1_str)
    	pub.publish(n1_str)
    	rate.sleep()

if __name__ == '__main__':
    try:
        node2()
    except rospy.ROSInterruptException:
        pass

