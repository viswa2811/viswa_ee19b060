#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


class Maneuver:

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle2/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle2/cmd_vel',
                                                  Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                Pose, self.update_pose1)
        self.pose_subscriber = rospy.Subscriber('/turtle2/pose',
                                                Pose, self.update_pose2)
        self.pose_publisher = rospy.Publisher('/turtle2/pose',
                                                  Pose, queue_size=10)

        self.pose1 = Pose()
        self.pose2=Pose()
        self.rate = rospy.Rate(10)

    def update_pose1(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose1 = data
        self.pose1.x = round(self.pose1.x, 4)
        self.pose1.y = round(self.pose1.y, 4)
    def update_pose2(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose2 = data
        self.pose2.x = round(self.pose2.x, 4)
        self.pose2.y = round(self.pose2.y, 4)

    def euclidean_distance(self,):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((self.pose1.x - self.pose2.x), 2) +
                    pow((self.pose1.y - self.pose2.y), 2))


    def move(self):
        

        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        safe_dist = float(input("Set your safe distance: "))

        vel_msg = Twist()
        while(self.euclidean_distance()>=2):
            # Linear velocity in the x-axis.
            vel_msg.linear.x = 0.5
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
        
            print(self.pose2.x,self.pose2.y)
            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            # Publish at the desired rate.
            self.rate.sleep()
        vel_msg.linear.x=0
        self.velocity_publisher.publish(vel_msg)
        while(self.pose2.theta<=1.5):
            vel_msg.angular.z=0.3
            self.velocity_publisher.publish(vel_msg)
        vel_msg.angular.z=0
        self.velocity_publisher.publish(vel_msg)    
        while self.euclidean_distance() < safe_dist:

            # Linear velocity in the x-axis.
            vel_msg.linear.x = 0.5
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            print(self.pose2.x,self.pose2.y)

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()
        vel_msg.linear.x=0
        self.velocity_publisher.publish(vel_msg)
        while(self.pose2.theta>=0):
            vel_msg.angular.z=-0.3
            self.velocity_publisher.publish(vel_msg)
        vel_msg.angular.z=0
        self.velocity_publisher.publish(vel_msg) 
        while(self.pose2.x<=10):
            vel_msg.linear.x = 0.5
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)
         # Stopping our robot after the movement is over.
        vel_msg.linear.x=0
        self.velocity_publisher.publish(vel_msg)

        # If we press control + C, the node will stop.
        rospy.spin()

if __name__ == '__main__':
    try:
        x = Maneuver()
        x.move()
    except rospy.ROSInterruptException:
        pass
