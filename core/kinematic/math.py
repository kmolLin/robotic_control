#from math import *
from sympy import *

AFA = 0
BETA = 180
GAMMA = 0

Ca = cos(0)
Cb = cos(pi)
Cg = cos(0)
Sa = sin(0)
Sb = sin(pi)
Sg = sin(0)


print([[Ca * Cg - Sa * Cb * Sg, Sa * Cg + Ca * Cb * Sg,Sb * Sg ], [-Ca * Sg - Sa * Cb * Cg, -Sa * Sg + Ca * Cb * Cg, Sa * Sb  ], [ Sb * Cg, -Ca * Sb, Cb]])

C1 = Symbol('C1')
S1 = Symbol('S1')
C23 = Symbol('C23')
S23 = Symbol('S23')

theta4 = Symbol('theta4')
theta5 = Symbol('theta5')
theta6 = Symbol('theta6')
'''
a = C1 * S23 
b = S1 * S23
c = S1 * C23
d = C1 * C23
'''

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
d = Symbol('d')


f1 = a * (cos(theta4) * cos(theta5) * cos(theta6) + sin(theta4) * sin(theta6)) - d *sin(theta5) * cos(theta6) + S1 * (cos(theta4) * sin(theta6) - sin(theta4) * cos(theta5) * cos(theta6)) -1.0
f2 = b * (cos(theta4) * cos(theta5) * cos(theta6) + sin(theta4) * sin(theta6)) - c *sin(theta5) * cos(theta6) - C1 * (cos(theta4) * sin(theta6) - sin(theta4) * cos(theta5) * cos(theta6))
f3 = C23 * (cos(theta4) * cos(theta5) * cos(theta6) + sin(theta4) * sin(theta6)) + S23 * sin(theta5) * cos(theta6)
f4 = a * (sin(theta4) * cos(theta6) - cos(theta4) * cos(theta5) * sin(theta6)) + d * sin(theta5) * sin(theta6) + S1 * (sin(theta4) * cos(theta5) * sin(theta6) + cos(theta4) * cos(theta6))
f5 = b * (sin(theta4) * cos(theta6) - cos(theta4) * cos(theta5) * sin(theta6)) + c * sin(theta5) * sin(theta6) - C1 * (sin(theta4) * cos(theta5) * sin(theta6) + cos(theta4) * cos(theta6))+1
f6 = C23 * (sin(theta4) * cos(theta6) - cos(theta4) * cos(theta5) * sin(theta6)) - S23 * sin(theta5) * sin(theta6)
f7 = a * cos(theta4) * sin(theta5) + d * cos(theta5) - S1 * sin(theta4) * sin(theta5)
f8 = b * cos(theta4) * sin(theta5) + c * cos(theta5) + C1 * sin(theta4) * sin(theta5)
f9= C23 * cos(theta4) * sin(theta5) - S23 * cos(theta5)+1

sol = solve((f1, f2, f3, f4, f5, f6, f7, f8, f9), theta4, theta5, theta6)
print(sol)
