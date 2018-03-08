# -*- coding: utf-8 -*-

from planpath import build_path
from rga import Genetic
from kinematic import forward_kinematic, Inverse_Kinematic
from time import time
import matplotlib.pyplot as plt
import numpy as np

t0 = time()
Target= [(50, 0, 150), (55, 0, 150), (55, -10, 150), (50, -10, 150), (50, 0, 150)]
Posture = np.array([0, 180, 0])
func = build_path({'Target':Target, 'Posture':Posture})
GeneticPrams = {'nPop':1500, 'pCross':0.85, 'pMute':0.05, 'pWin':0.95, 'bDelta':5.,'maxGen':500 , 'report':0} # 'minFit':0.1,
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

