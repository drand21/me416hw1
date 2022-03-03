#!/usr/bin/env python
"""Simple talker demo that published std_msgs/Strings messages to the 'chatter' topic"""

import rospy
from std_msgs.msg import String


def main():
    """Node setup and main ROS loop"""
    #Init node. anonymous=True allows multiple launch with automatically assigned names
    rospy.init_node('talker', anonymous='True')

    #Prepare publisher on the 'chatter' topic
    pub = rospy.Publisher('chatter', String, queue_size=10)

    #Prepare list of strings
    msg = ["beans", "greens", "tomatoes", "potatoes"]

    #Set rate to use (in Hz)
    rate = rospy.Rate(4.0/3.0)

    #Set counter to iterate through msg
    i = 0
    
    while not rospy.is_shutdown():
        if i == len(msg):
            i = 0

        #Write to console
        rospy.loginfo(msg[i])

        #Publish
        pub.publish(msg[i])
        i = i + 1

        #Wait until it is done
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    finally:
        #This is the place to put any "clean up" code that should be executed
        #on shutdown even in case of errors, e.g., closing files or windows
        pass
