#!/usr/bin/env python
import rospy
from std_msgs.msg import String
global n1_str
global n2_str
def callback1(data):
    n1_str=data.data
    print(n1_str, end='')
def callback2(data):
    n2_str=data.data
    print(":",n2_str)

def listener():

    rospy.init_node('node3', anonymous=True)

    rospy.Subscriber('team_abhiyaan', String, callback1)
    rospy.Subscriber('autonomy', String, callback2)

if __name__ == '__main__':
    listener()
