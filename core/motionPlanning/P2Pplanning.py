# p2pplanning

from typing import Tuple
from math import (
    ceil, 
    fabs,
    pow, 
    sqrt
)
import numpy as np

Jmax = 10000
Ts = 0.0001

def P2Pplanning(m: Tuple[float], Vmax: float, now_joint: Tuple[float]):
    """ motion planning
    m is six motor joint
    Vmax is build set velocity
    nowjoint is the motor position
    """
    for i in range(6):
        m[i] = m[i]-now_joint[i]
    # find max angle
    dsmax = abs(max(m, key=abs))
    if (dsmax == 0) or (Vmax == 0):
        print("P2Pplanning Error")
        return
    k = []
    for i in range(6):
        k.append(m[i]/dsmax)
    Lmov = dsmax
    dVmin = Jmax*Ts*Ts
    # V Jmax Lmov K
    Nacc = ceil(sqrt(Vmax/dVmin))
    Tacc = Nacc * Ts
    Jcmd = Vmax / pow(Tacc, 2)
    Lmin = 2.0 * Jcmd * pow(Tacc, 3)
    Tc = 0.0
    Nc = 0
    if Lmov > Lmin:
        type = 4
        Lc = Lmov - Lmin
        Nc = ceil(Lc / (Vmax * Ts))
        Tc = Nc * Ts
    else:
        type = 3
        Nacc = ceil(pow(Lmov / (2.0 * Jmax), 1.0 / 3.0) / Ts)
        Tacc = Nacc * Ts
    Vcmd = Lmov / (2.0 * Tacc + Tc)
    Acmd = Vcmd / Tacc
    Jcmd = Vcmd / pow(Tacc, 2)
    N = np.zeros(6)
    Nt = np.zeros(5)
    L = np.zeros(5)
    
    N[0] = Nacc
    N[1] = Nacc + Nacc
    N[2] = N[1] + Nc
    N[3] = N[2] + Nacc
    N[4] = N[3] + Nacc
    N[5] = N[4] + 0

    Nt[0] = Tacc    
    Nt[1] = Tacc + Tacc
    Nt[2] = Nt[1] + Tc
    Nt[3] = Nt[2] + Tacc
    Nt[4] = Nt[3] + Tacc

    L[0] = Jcmd * pow(Tacc, 3) / 6.0
    L[1] = L[0] + Vcmd*Tacc - Jcmd*Tacc*Tacc*Tacc/6.0
    L[2] = L[1] + Vcmd*Tc
    L[3] = L[2] + Vcmd*Tacc - Jcmd*Tacc*Tacc*Tacc/6.0
    L[4] = L[3] + Jcmd*pow(Tacc, 3)/6.0
    
    
    
    
    
    
    
