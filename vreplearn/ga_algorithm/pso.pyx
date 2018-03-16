# -*- coding: utf-8 -*-
# PSO Particle Swarm Optimization algorithm
import numpy as np
cimport numpy as np

cdef class PSO(object):
    cdef int swarmSize, pNum, maxiter
    cdef double w, wp, wg, threshold, updateThreshold, rp, rg, old, gBestFitness
    cdef object func, bounds
    cdef np.ndarray particles, pBest, pBestFitness, v, gBest
    
    # init
    def __cinit__(self, object func, object settings, int swarmSize=20, double w=0.5, double wp=1.5, double wg=0.5):
        '''
        v = w*v + wp*(pBest-x) + wg*(gBest-x)
        '''
        self.swarmSize = swarmSize
        self.func = func
        self.pNum = self.func.get_nParm()#len(settings['bounds'])#self.func.get_nParm()  #
        print(self.pNum)
        self.bounds = settings['bounds']*1
        self.w = w
        self.wp = wp
        self.wg = wg
        self.gBestFitness = np.inf
        
        # init particles and velocity
        self.particles = np.zeros((self.swarmSize, self.pNum))
        self.v = np.zeros((self.swarmSize, self.pNum))
        for i, b in enumerate(self.bounds):
            self.particles[:,i] = np.random.uniform(b[0], b[1], self.swarmSize)
            self.v[:,i] = np.random.uniform(-b[1]+b[0], b[1]-b[0], self.swarmSize)
        
        print(self.swarmSize,self.pNum)
        # init fitness
        self.pBest = np.zeros((self.swarmSize, self.pNum))
        self.pBestFitness = np.ones(self.swarmSize) * np.inf
        self.updateFitness()
        
    
    # update fitness
    cdef updateFitness(self):
        for i, p in enumerate(self.particles):
            fit = self.func(p)
            # TODO : need to add fitness
            if fit < self.pBestFitness[i]:
                self.pBest[i] = p
                self.pBestFitness[i] = fit
                if fit < self.gBestFitness:
                    self.gBest = p
                    self.gBestFitness = fit
    
    cpdef run(self, threshold=0.01, updateThreshold=1e-4, maxiter=10000):
        cdef int n = 0
        while self.gBestFitness > threshold and n < maxiter:
            # update particles's velocity
            rp = np.random.rand()
            rg = np.random.rand()
            self.v = self.w*self.v + self.wp*rp*(self.pBest-self.particles) + self.wg*rg*(self.gBest-self.particles)
            
            # update particles 
            self.particles = self.particles + self.v
            for i, b in enumerate(self.bounds):
                self.particles[:,i] = np.clip(self.particles[:,i], b[0], b[1])
            # calc fitness
            old = self.gBestFitness
            self.updateFitness()
            
            if old - self.gBestFitness < 0.001:
                n += 1
            else:
                n = 0
            if n > maxiter:
                break
        return self.func.get_coordinates(self.gBest), self.gBestFitness
