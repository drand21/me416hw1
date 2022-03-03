"""functions for modeling ROSBot"""

#import numpy as np
# from math import cos, sin

def model_parameters():
    """Returns two constant model parameters"""
    k = 1.0
    d = 0.5
    return k, d

#def system_matrix(theta):
#    """Returns a numpy array with the A(theta) matrix for a differential drive robot"""
#    return A


#def system_field(z, u):
#    """Computes the field at a given state for the dynamical model"""
#    return dot_z


#def euler_step(z, u, stepSize):
#    """Integrates the dynamical model for one time step using Euler's method"""
#    return zp


def twist_to_speeds(speed_linear, speed_angular):
    """function twist_to_speeds"""
    # Takes the desired linear and angular velocity
    # returns normalized speeds for the left and right motor
    # Inputs are in range of [-1.0, 1.0] and outputs are in same range
    # Higher right value indicates robot will spin counter-clockwise
    # Lower will spin clockwise, right=left indicates straight movement
    right = speed_linear*0.5
    left = speed_linear*0.5
    # Linear and Angular velocities are given same weight
    # An input linear speed of 1.0 will return a linear speed of 0.5 in both wheels
    # An input angular speed of 1.0 on top of above speed will result in
    # Right wheel output at 1 while left wheel output at 0

    right = right + speed_angular*0.5
    left = left - speed_angular*0.5
    return left, right
