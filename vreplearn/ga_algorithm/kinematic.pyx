# -*- coding: utf-8 -*-
# kinematic math
import numpy as np
cimport numpy as np
from libc.math cimport sin,cos,pow,atan2,atan,sqrt,fabs

cdef double d6h = 86.5+170
cdef int AXIS1 = 0
cdef int AXIS2 = 1
cdef int AXIS3 = 2
cdef int AXIS4 = 3
cdef int AXIS5 = 4
cdef int AXIS6 = 5

# D-H Table
cdef double a1 = 30.0
cdef double a2 = 340.0
cdef double a3 = 40.0
cdef double d1 = 375.0
cdef double d4 = 338.0
cdef double d6 = 86.5

cdef double ERRC = 1E-6

cdef void foo(object RAD, object angles):
    cdef int i
    for i in range(6):
        RAD.append(np.radians(angles[i]))

cpdef object forward_kinematic(object angles):
    cdef object RAD = []
    cdef np.ndarray UVW = np.zeros((3,3))
    foo(RAD, angles)
    
    cdef double C1 = cos(RAD[AXIS1])
    cdef double C2 = cos(RAD[AXIS2])
    cdef double C3 = cos(RAD[AXIS3])
    cdef double C4 = cos(RAD[AXIS4])
    cdef double C5 = cos(RAD[AXIS5])
    cdef double C6 = cos(RAD[AXIS6])
    cdef double S1 = sin(RAD[AXIS1])
    cdef double S2 = sin(RAD[AXIS2])
    cdef double S3 = sin(RAD[AXIS3])
    cdef double S4 = sin(RAD[AXIS4])
    cdef double S5 = sin(RAD[AXIS5])
    cdef double S6 = sin(RAD[AXIS6])
    cdef double C23 = cos(RAD[AXIS2] - RAD[AXIS3])
    cdef double S23 = sin(RAD[AXIS2] - RAD[AXIS3])
    
    UVW[0][0] = C1 * S23 * (C4 * C5 * C6 + S4 * S6) - C1 * C23 *S5 * C6 + S1 * (C4 * S6 - S4 * C5 * C6)
    UVW[1][0] = S1 * S23 * (C4 * C5 * C6 + S4 * S6) - S1 * C23 *S5 * C6 - C1 * (C4 * S6 - S4 * C5 * C6)
    UVW[2][0] = C23 * (C4 * C5 * C6 + S4 * S6) + S23 * S5 * C6
    UVW[0][1] = C1 * S23 * (S4 * C6 - C4 * C5 * S6) + C1 * C23 * S5 * S6 + S1 * (S4 * C5 * S6 + C4 * C6)
    UVW[1][1] = S1 * S23 * (S4 * C6 - C4 * C5 * S6) + S1 * C23 * S5 * S6 - C1 * (S4 * C5 * S6 + C4 * C6)
    UVW[2][1] = C23 * (S4 * C6 - C4 * C5 * S6) - S23 * S5 * S6
    UVW[0][2] = C1 * S23 * C4 * S5 + C1 * C23 * C5 - S1 * S4 * S5
    UVW[1][2] = S1 * S23 * C4 * S5 + S1 * C23 * C5 + C1 * S4 * S5
    UVW[2][2] = C23 * C4 * S5 - S23 * C5
    
    cdef double X = C1 * (a1 + C23 * (d6h * C5 + d4) + a2 * S2 + S23 * (a3 + d6h * C4 * S5)) - d6h * S1 * S4 * S5
    cdef double Y = S1 * (a1 + C23 * (d6h * C5 + d4) + a2 * S2 + S23 * (a3 + d6h * C4 * S5)) + d6h * C1 * S4 * S5
    cdef double Z = d1 - S23 * (d6h * C5 + d4) + a2 * C2 + C23 * (a3 + d6h * C4 * S5)
     
    return X, Y, Z,R2Eul(UVW)
    
cpdef object Inverse_Kinematic(object TCP,object TOV, object actjoint):
    cdef np.ndarray THETA =  np.zeros((4, 6))
    cdef np.ndarray dT = np.zeros((4, 6))
    cdef np.ndarray RAD = np.zeros((6))
    cdef np.ndarray U= np.zeros((3))
    cdef np.ndarray V= np.zeros((3))
    cdef np.ndarray W= np.zeros((3))
    Joint_Deg = []
    cdef np.ndarray dif = np.zeros((4))
    UVM =  Eul2R(TOV)
    
    for i in range(0, 3):
        U[i] = UVM[i][0]
        V[i] = UVM[i][1]
        W[i] = UVM[i][2]
        
    Px = TCP[0]-d6h*W[0]
    Py = TCP[1]-d6h*W[1]
    Pz = TCP[2]-d6h*W[2]
    
    cdef int cnt = 0
    cdef int passkey = 1
    
    while(passkey):
        # Theta1
        RAD[0] = atan2(Py, Px)
        C1 = cos(RAD[0])
        S1 = sin(RAD[0])
        # Theta3    +- ???
        Px2 = pow(Px, 2)
        Py2 = pow(Py, 2)
        Pz2 = pow(Pz - d1, 2) ##d1
        k1 = 2.0 * a2 * d4
        k2 = 2.0 * a2 * a3
        k3 = Px2 + Py2 + Pz2 - 2.0 * a1 * (Px * C1 + Py * S1) + pow(a1, 2) - pow(a3, 2) - pow(d4, 2) - pow(a2, 2)
        kcnt = pow(k1, 2) + pow(k2, 2) - pow(k3, 2)
        if kcnt < 0:
            check = False
            return (0, 0, 0, 0, 0, 0) , check
            break
        else :
            theta3_1 = 2.0 * atan((k1 + sqrt(kcnt)) / (k2 + k3))
            theta3_2 = 2.0 * atan((k1 - sqrt(kcnt)) / (k2 + k3))
            check = True
            
        if cnt <=1:
            RAD[2] = theta3_1
        else:
            RAD[2] = theta3_2
            
        C3 = cos(RAD[2])
        S3 = sin(RAD[2])
        
        # Theta2
        mu1 = -a3 * S3 + d4 *C3
        mu2 = a3 * C3 + d4 * S3 + a2
        v1 = a3 * C3 + d4 * S3 + a2
        v2 = a3 * S3 - d4 * C3
        gama1 = Px * C1 + Py * S1 - a1
        gama2 = Pz - d1
    
        RAD[1] = atan(((mu1 * gama2) - (gama1 * mu2)) / ((gama1 * v2) - (v1 * gama2)))
        
        C2 = cos(RAD[1])
        S2 = sin(RAD[1])
        C23 = cos(RAD[1] - RAD[2])
        S23 = sin(RAD[1] - RAD[2])
        
        # Theta5
        r21 = -U[0] * C1 * C23 - U[1] * S1 * C23 + U[2] * S23
        r22 = -V[0] * C1 * C23 - V[1] * S1 * C23 + V[2] * S23
        r23 = -W[0] * C1 * C23 - W[1] * S1 * C23 + W[2] * S23
        theta5_1 = atan2(sqrt(pow(r21, 2) + pow(r22, 2)), -r23)
        theta5_2 = atan2(-sqrt(pow(r21, 2) + pow(r22, 2)), -r23)
        
        if cnt ==0 or cnt == 2:
            RAD[4] = theta5_1
        else:
            RAD[4] = theta5_2
            
        C5 = cos(RAD[4])
        S5 = sin(RAD[4])
        # Theta4
        r13 = W[0] * C1 * S23 + W[1] * S1 * S23 + W[2] * C23
        r33 = W[0] * S1 - W[1] * C1
        
        if S5> ERRC:
            RAD[3] = atan2(-r33, r13)
        elif S5 < ERRC:
            RAD[3] = atan2(r33, -r13)
        C4 = cos(RAD[3])
        S4 = sin(RAD[3])
        
        #theta 6
        if S5 > ERRC:
            RAD[5] = atan2(-r22, r21)
        elif S5 < ERRC:
            RAD[5] = atan2(r22, -r21)
            
        for i in range(6):
            THETA[cnt][i]= RAD[i]
        if cnt==3:
            passkey = 0
        cnt = cnt+1
    for i in range(0, cnt):
        for j in range(0, 6):
            dT[i][j] = np.degrees(THETA[i][j]) - actjoint[j]
            dif[i] = dif[i] + pow(dT[i][j], 2)
        dif[i] = sqrt(dif[i])
    dif_min = dif[0]
    min = 0
    for i in range(1, 4):
        if dif_min>dif[i]:
            dif_min = dif[i]
            min = i
    for i in range(6):
        Joint_Deg.append(np.degrees(THETA[min][i]))
    return Joint_Deg
    

    
cdef object Eul2R(object EUL):
    cdef object RAD = []
    for i in range(3):
        RAD.append(np.radians(EUL[i]))
        
    Ca = cos(RAD[0])
    Cb = cos(RAD[1])
    Cg = cos(RAD[2])
    Sa = sin(RAD[0])
    Sb = sin(RAD[1])
    Sg = sin(RAD[2])
    cdef object R = [[Ca * Cg - Sa * Cb * Sg, Sa * Cg + Ca * Cb * Sg,Sb * Sg ], [-Ca * Sg - Sa * Cb * Cg, -Sa * Sg + Ca * Cb * Cg, Sa * Sb  ], [ Sb * Cg, -Ca * Sb, Cb]]
    return R 

cdef R2Eul(object R):
    cdef np.ndarray RAD = np.zeros((3))
    cdef np.ndarray U= np.zeros((3))
    cdef np.ndarray V= np.zeros((3))
    cdef np.ndarray W= np.zeros((3))
    cdef np.ndarray EUL = np.zeros((3))
    for i in range(0, 3):
        U[i] = R[i][0]
        V[i] = R[i][1]
        W[i] = R[i][2]
    
    RAD[1] = atan2(sqrt(pow(W[0], 2) + pow(W[1], 2)), W[2])
    if (fabs(sin(RAD[1])) <= ERRC):
        RAD[2] = 0.0
        RAD[0] = atan2(V[0], U[0])
    else:
        RAD[0] = atan2(W[0], (-W[1]))
        RAD[2] = atan2(U[2], V[2])
        
    if fabs(RAD[0]) + fabs(RAD[2]) >= np.pi:
        RAD[1] = atan2(-sqrt(pow(W[0], 2) + pow(W[1], 2)), W[2])
        RAD[0] = atan2(-W[0], W[1])
        RAD[2] = atan2(-U[2], -V[2])
    #for i in range(0, 3):
    EUL = np.rad2deg( RAD)
    return EUL
