# -*- coding: utf-8 -*-

from planpath import build_path
from rga import Genetic
from kinematic import forward_kinematic, Inverse_Kinematic
from time import time
import matplotlib.pyplot as plt

t0 = time()
Target= [(150, 0, 300), (155, 0, 300), (155, -10, 300), (150, -10, 300)]
func = build_path({'Target':Target})
GeneticPrams = {'nPop':500, 'pCross':0.95, 'pMute':0.05, 'pWin':0.95, 'bDelta':5.,'maxGen':1000 , 'report':0} # 'minFit':0.1,
foo = Genetic(func, GeneticPrams)
angles, f = foo.run()
print(time()-t0)
print(angles)

for angle in angles:
    print(tuple(round(v, 4) for v in forward_kinematic(angle)))

    


