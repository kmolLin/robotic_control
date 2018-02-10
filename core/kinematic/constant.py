# constant for robotic arm
from enum import Enum
from math import *

class constant(Enum):
    
    AFA = 0
    BETA = 1
    GAMA = 2
    TOTAL_TOV = 3
    DEG2RAD = pi/180.0
    RAD2DEG = 180.0/pi
    # 6-AXES ID
    AXIS1 = 0
    AXIS2 = 1
    AXIS3 = 2
    AXIS4 = 3
    AXIS5 = 4
    AXIS6 = 5
    TOTAL_AXES = 6
    
    #Error Value
    ERRC = 1E-6
    
    # D-H Table
    a1 = 30.0
    a2 = 340.0
    a3 = 40.0
    d1 = 375.0
    d4 = 338.0
    d6 = 86.5
    
