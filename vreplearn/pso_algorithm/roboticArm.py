# -*- coding: utf-8 -*-
"""
Module: roboticArm.py
Author: L. J. Miranda
"""

import numpy as np
import math

import particleSwarmOptimization

class RoboticArm(object):
    
    def __init__(self, d1, d2, d4, d6):
        self.d1 = d1
        self.d2 = d2
        self.d4 = d4
        self.d6 = d6
    
    def forwardKinematics(self, params, target):
        """
        Computes for the end-tip position of the Robotic Arm with respect to the joint parameters
        
        Inputs:
            - params: Joint variables that can be found in the manipulator (all angles should be in radians):
                [0]: Theta1    [3]: Theta4
                [1]: Theta2    [4]: Theta5
                [2]: D3        [5]: Theta6
                
        Returns:
            - pos: end-tip position of the manipulator (x,y,z coordinates).
            - cost: the cost of these params end-tip position with respect to the target.
        """
        t_00 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        t_01 = self.getTransformMatrix(params[0], self.d2, 0, -math.pi/2)
        t_12 = self.getTransformMatrix(params[1], self.d2,0,-math.pi/2)
        t_23 = self.getTransformMatrix(0,params[2], 0, -math.pi/2)
        t_34 = self.getTransformMatrix(params[3], self.d4, 0, -math.pi/2)
        t_45 = self.getTransformMatrix(params[4], 0, 0, math.pi/2)
        t_56 = self.getTransformMatrix(params[5], self.d6,0 ,0)
        
        Etip = t_00.dot(t_01).dot(t_12).dot(t_23).dot(t_34).dot(t_45).dot(t_56)
        pos = np.array([Etip[0,3],Etip[1,3],Etip[2,3]])
        cost = self.L2Distance(pos, target)
        returnMessage = [pos,cost]
        return returnMessage
        
        
    def getTransformMatrix(self, theta, d, a, alpha):
        """
        Gets the transformation matrix using the Denavit-Hartenberg method.
        
        Inputs:
            - theta: joint angle
            - d: link offset
            - a: link length
            - alpha: link twist
        
        Returns:
            - T: a numpy array transformation matrix
        """
        T = np.array([[math.cos(theta), -math.sin(theta)*math.cos(alpha), math.sin(theta)*math.sin(alpha), a * math.cos(theta)],
                     [math.sin(theta), math.cos(theta)*math.cos(alpha), -math.cos(theta)*math.sin(alpha), a*math.sin(theta)],
                     [0, math.sin(alpha), math.cos(alpha), d],
                     [0,0,0,1]])
        
        return T
                
        
    def L2Distance(self,query,target):
        x_dist = (target[0] - query[0])**2
        y_dist = (target[1] - query[1])**2
        z_dist = (target[2] - query[2])**2
        d = math.sqrt(x_dist + y_dist + z_dist)
        return d
