# -*- coding: utf-8 -*-

from planpath import build_path
from rga import Genetic
from pso import PSO
from kinematic import forward_kinematic, Inverse_Kinematic
from time import time
import matplotlib.pyplot as plt
import numpy as np
from particleSwarmOptimization import ParticleSwarmOptimization

t0 = time()
Target= [(450, 0, 150), (455, 0, 150), (455, -10, 150), (450, -10, 150), (450, 0, 150)]
Posture = np.array([0, 180, 0])
startstate = np.array([0, 0, -90, 0, -90, 0])
func = build_path({'Target':Target, 'Posture':Posture, 'startstate':startstate})
GeneticPrams = {'nPop':1500, 'pCross':0.85, 'pMute':0.05, 'pWin':0.85, 'bDelta':5., 'maxGen':1000, 'report':0} # 'minFit':0.1,'maxGen':10000 ,
foo = Genetic(func, GeneticPrams)
angles, time_and_fitness = foo.run()
print("second:", time()-t0)
print(angles)
gen = []
chromElite = []
timee= []
    
val = tuple((int(e.split(',')[0]), float(e.split(',')[1]), float(e.split(',')[2])) for e in time_and_fitness.split(';')[0:-1])

for e in val:
    gen.append(e[0])
    chromElite.append(e[1])
    timee.append(e[2])

plt.plot(gen,chromElite) 
for angle in angles:
    print(*forward_kinematic(angle))

plt.show()

"""
Target= [(450, 0, 150)]
Posture = np.array([0, 180, 0])
func = build_path({'Target':Target, 'Posture':Posture})
bound =  [(0,360)]*6
PSOPrams = {'pMute':0.05,'maxGen':500, 'report':0, 'bounds': bound}

#def fitness(x):
#        return (x[0]-5)**2 + (x[1]-10)**2 + (x[2]+10)**2
        
foo = PSO(func, PSOPrams)
xopt, fopt = foo.run(threshold=1e-6)
print("自製pso：{} {}".format(fopt, xopt))
for angle in xopt:
    print(*forward_kinematic(angle))
#print(forward_kinematic(xopt))

opt = ParticleSwarmOptimization()
Target= [(450, 0, 150), (455, 0, 150)]
Posture = np.array([0, 180, 0])
func = build_path({'Target':Target, 'Posture':Posture})
bound =  [(0,360)]*6
options = [20, 1.5, 1.5, 0.5, 1.0]
threshold=1e-6
foo = opt.runOptimizer(func, Target, np.zeros((2, 6)), 1000, options, threshold, True )
"""
