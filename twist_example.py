""" Example of how to set attributes in ROS messages """

def twist_fill():
    """Creates new Twist object"""
    """Populates the linear and angular coordinate values with 3.0"""
    A = Twist()
    A.linear.x = 0.5
    A.linear.y = 0.5
    A.linear.z = 0.5
    A.angular.x = 0.5
    A.angular.y = 0.5
    A.angular.z = 0.5
    return A