# pso testcode
from particleSwarmOptimization import ParticleSwarmOptimization

from roboticArm import RoboticArm

import numpy as np

# Initialize arm with distances

# Say, d1=5, d2=4, d4=7, d6=8

arm = RoboticArm(d1=5,d2=4,d4=7,d6=8)

opt = ParticleSwarmOptimization()

# Run optimizer with your parameters and arm.forwardKinematics as the

# objective function. Be sure to define your variables first (i.e. target, params, etc) 

# before passing them to the function.
target = (-2, 2, 3)
params = np.zeros((6))
iterations = 1000
options = [20, 1.5, 1.5, 0.5, 1.0, 1]
threshold = 1E-5

final_params, J_hist = opt.runOptimizer(arm.forwardKinematics, target, params, iterations, options, threshold, True)
print(final_params, J_hist)
#opt.plotParticles3D()
