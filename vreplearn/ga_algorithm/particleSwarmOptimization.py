# -*- coding: utf-8 -*-
"""
Module: particleSwarmOptimization.py
Author: L. J. Miranda
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class ParticleSwarmOptimization(object):
    
    def __init__(self):
        pass
    
    def runOptimizer(self, objectiveFcn, target, params, iterations, options, threshold, animate):
        """
        Runs the particle swarm optimization (PSO) algorithm in order to minimize
        the objective function given different parameters.
        
        Inputs:
            - objectiveFcn: the function to be optimized (type -> method).
            - target: target coordinate used as basis.
            - params: np array of the initial parameters to be optimized.
            - iterations: number of iterations that PSO will run. (default = 1000)
            - options: a list containing the parameters for PSO behavior, 
                      in this case, options = [swarmSize c1 c2 w epsilon v_initial]
                      [0] swarmSize - the number of particles or swarm size
                      [1] c1 - cognitive parameter
                      [2] c2 - social parameter
                      [3] w  - inertia weight
                      [4] epsilon - the spread of the particles.
                      [5] v_initial - initial velocity
            - threshold: set the threshold when to exit the optimizer. 
            - animate: trigger to show animation of particles, input 1 to animate. (default = 0)
            
        Returns:
            - final_params: returns an np-array of the final parameters after the given number of iterations.
            - cost: returns the final cost. [TODO]
            - cost_hist: returns the cost history given the number of iterations. [TODO]
        """
        
        ################################################################################
        #                             INITIALIZE MATRICES                              #
        ################################################################################
        size_params = params.size
        
        # Current Positions of the Swarm
        currentPos = np.random.uniform(0,1,[options[0], size_params]) * options[4] + params.T
        
        # Initialize Personal Best Position
        pBestPos = currentPos;

        # Initialize Global Best Position
        J = []
        for i in range(options[0]):
            temp = objectiveFcn(currentPos[i,:], target)
            J.append(temp[1])
        
        minIndex = np.argmin(J)
        gBestPos = currentPos[minIndex,:]
            
        # Initialize Velocity Matrix
        velocityMatrix = options[5] * np.ones([options[0], size_params])
        
        # Initialize Record Vectors
        J_hist = []
        pBestRecord = []
        cBestRecord = []

        
        
        ################################################################################
        #                             PSO ALGORITHM                                    #   
        ################################################################################
        
        for i in range(iterations):
            # Update the pbest and gbest
            for particle in range(options[0]):
                # Set the personal best option
                costParticle = objectiveFcn(currentPos[particle,:],target)
                costpBest = objectiveFcn(pBestPos[particle,:],target)
                cBestRecord.append(costParticle[1])
                if costParticle[1] < costpBest[1]:
                    pBestPos[particle,:] = currentPos[particle,:]
                costpBest2 = objectiveFcn(pBestPos[particle,:],target)
                pBestRecord.append(costpBest2[1])
                # Set the global best option
                costgBest = objectiveFcn(gBestPos,target)
                if costParticle[1] < costgBest[1]:
                    gBestPos = currentPos[particle,:]
            


            #------------------- HELPER FUNCTIONS --------------------------#            
            # Helper functions for display
            cost = objectiveFcn(gBestPos,target)
            self.consoleDisplay(i,cost[1])    
            
            temp = [i, cost[1], np.mean(pBestRecord)]
            J_hist.append(temp)
            
            # Helper functions for animation
            if animate==1:
                swarmPos = []
                for n in range(options[0]):
                    pos = objectiveFcn(currentPos[n,:], target)
                    swarmPos.append(pos[0])
                
                swarmPos = np.asarray(swarmPos)
                xVec = swarmPos[:,0]
                yVec = swarmPos[:,1]
                zVec = swarmPos[:,2]
                swarmPos = swarmPos.tolist()
                fig = plt.figure()
                self.plotParticles3D(fig,xVec,yVec,zVec,i)
            
            # If the cost is greater than the threshold
            if cost[1] > threshold:
                # Update the velocities and position.
                for particle in range(options[0]):
                    # Update velocity
                    cognitive = (options[1] * np.random.uniform(0,1,[1,6])) * (pBestPos[particle,:] - currentPos[particle,:])
                    social = (options[2] * np.random.uniform(0,1,[1,6])) * (gBestPos - currentPos[particle,:])
                    velocityMatrix[particle,:] = (options[3] * velocityMatrix[particle,:]) + cognitive + social
                    # Update position
                    currentPos[particle,:] = currentPos[particle,:] + velocityMatrix[particle,:]

            else:
                # Return the parameters if the cost is less than the threshold
                final_params = gBestPos
                return final_params, J_hist
                
        # Return the parameters if the iterations finished and the cost didn't go below threshold            
        final_params = gBestPos
        return final_params, J_hist
            

    def consoleDisplay(self, i, cost):      
        statement = 'Iteration: ' + str(i) + ' | Cost: ' + str(cost)
        print(statement)
    
    def plotParticles3D(self,fig,x,y,z,i):
        fig.clear()
        fig.suptitle('Particle End-Tip Position', fontsize=20)
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, c='r', marker='o')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_xlim([-5, 5])
        ax.set_ylim([-5, 5])
        ax.set_zlim([0, 5])
        save_format = 'png'
        plt.savefig('figure_' + str(i) + '.' + save_format, dpi=300)
        plt.show()
        
