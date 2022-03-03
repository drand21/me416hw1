#!/usr/bin/env python
"""listener accumulator"""

import rospy
from std_msgs.msg import String

msg_accumulated = String()

def callback(msg):
    """ Callback to receive a message and accumulate it """
    global msg_accumulated
    content = msg.data
    msg_accumulated.data = ' '.join([msg_accumulated.data, content])

def main():
    """Node setup and main ROS loop"""
    #define global msg_accumulated so it can be used in callback and main
    global msg_accumulated

    #Init node. anonymous=True allows multiple launch with automatically assigned names
    rospy.init_node('listener_accumulator', anonymous='True')

    #setting up publisher and subscriber
    pub = rospy.Publisher('chatter_repeated', String, queue_size=10)
    rospy.Subscriber('chatter', String, callback)

    #while loop to publish at 1/3Hz
    rate = rospy.Rate(1.0/3.0) #have to do 1.0/3.0 becasue that will make a double (1/3 will be converted to 0)
    while not rospy.is_shutdown():
        pub.publish(msg_accumulated)
        rospy.loginfo(' I accumulated %s', msg_accumulated.data)

        #clearing the msg_accumulated so it can repopulate for the next cycle
        msg_accumulated.data = ''
        rate.sleep()

    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    finally:
        #This is the place to put any "clean up" code that should be executed
        #on shutdown even in case of errors, e.g., closing files or windows
        pass
