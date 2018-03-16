# -*- coding: utf-8 -*-
# planpath code

from kinematic import (
    forward_kinematic,
    Inverse_Kinematic
)
import numpy as np
cimport numpy as np
from libc.math cimport pow, sqrt

cdef double FAILURE = 9487945

#This class used to build path 
cdef class build_path(object):
    # Target get px py pz
    cdef object motors,upper, lower, targetPoint
    cdef np.ndarray posture
    cdef int POINTS
    
    def __cinit__(self,object mechanismParams):
        '''
        mechanismParams = {
            'Target',
            'Posture',
            'Follower',
            'constraint',
            'Expression',
            'IMax', 'LMax', 'FMax', 'AMax',
            'IMin', 'LMin', 'FMin', 'AMin'
        }
        '''
        self.targetPoint = mechanismParams['Target']
        self.posture = mechanismParams['Posture']
        self.POINTS = len(self.targetPoint)
        #upper
        #self.upper = [360]*6*self.POINTS
        self.upper = [165, 125, 185, 190, 115, 360]*self.POINTS
        #lower
        #self.lower = [0]*6*self.POINTS
        self.lower = [-165, -85, -55, -190, -115, -360]*self.POINTS
        
    cpdef object get_upper(self):
        return self.upper
    
    cpdef object get_lower(self):
        return self.lower
        
    cpdef int get_nParm(self):
        return 6*self.POINTS
    
    def  __call__(self, v):
        return self.run(v)
    
    cdef double run(self, object v):
        """
        v: a list of parameter [J1,J2,J3,J4,J5,J6]
        """
        #My fitness
        cdef double fitness = 0
        cdef np.ndarray tmp_array = np.array(v).reshape((-1,6))
        cdef double distance
        cdef np.ndarray posturederror
        cdef double anglefitness = 0
        cdef np.ndarray posture_old
        for i, angles in enumerate(tmp_array):
            if i != 0:
                anglefitness = np.sum(np.abs(angles - tmp_array[i-1]))
            x, y, z,posture_old = forward_kinematic(angles)
            x1, y1, z1 = self.targetPoint[i]
            distance = sqrt(pow(x-x1,2)+pow(y-y1,2)+pow(z-z1,2))
            #posturederror = np.abs(self.posture - posture_old)
            fitness += distance+anglefitness
        
        return fitness
    
    cpdef np.ndarray get_coordinates(self, object v):
        return np.array(v).reshape((-1,6))
