# -*- coding: utf-8 -*-
from libc.math cimport (
    pow,
    sqrt,
    isnan,
    sin,
    cos,
    atan2,
    radians,
    degrees,
)
from cpython cimport bool
cimport numpy as np
nan = float("nan")

cpdef object armInverse(double TCP[3], double TOV[3],double actjoint[6]):
    cdef double  C1, C2, C3, C4, C5, S1, S2, S3, S4, S5, C23, S23
	cdef double  Px, Py, Pz, k1, k2, k3, kcnt
	cdef double  Px2, Py2, Pz2
	cdef double  theta3_1, theta3_2, theta5_1, theta5_2
	cdef double  mu1, mu2, v1, v2, gama1, gama2
	cdef double  r13, r33, r21, r22, r23
	cdef double  RAD[6], UVW[3][3], THETA[4][6], dT[4][6], dif[4]
	cdef double  U[3], V[3], W[3]
	cdef int       min, dif_min
    
    
    UVW = Eul2R(TOV)
    
    for i in range(0,3):
        U[i] = UVW[i][0]
        V[i] = UVW[i][1]
        W[i] = UVW[i][2]
        
    Px = TCP[X] - d6h * W[X]
    Py = TCP[Y] - d6h * W[Y]
    Pz = TCP[Z] - d6h * W[Z]

    int cnt = 0, pass = 1
    while (pass):
    
        # theta 1
        RAD[AXIS1] = atan2(Py, Px)
        C1 = cos(RAD[AXIS1])
        S1 = sin(RAD[AXIS1])
        
        # theta 3
        Px2 = pow(Px, 2)
        Py2 = pow(Py, 2)
        Pz2 = pow(Pz - d1, 2) ##d1
        k1 = 2.0 * a2 * d4
        k2 = 2.0 * a2 * a3
        k3 = Px2 + Py2 + Pz2 - 2.0 * a1 * (Px * C1 + Py * S1) + pow(a1, 2) - pow(a3, 2) - pow(d4, 2) - pow(a2, 2)
        kcnt = pow(k1, 2) + pow(k2, 2) - pow(k3, 2)
        if kcnt < 0:
                print("Didn't have correct answer.")
        else :
            theta3_1 = 2.0 * atan((k1 + sqrt(kcnt)) / (k2 + k3))
            theta3_2 = 2.0 * atan((k1 - sqrt(kcnt)) / (k2 + k3))
        #print(theta3_1*RAD2DEG,"23", theta3_2*RAD2DEG)
        if cnt <=1:
            RAD[0, constant.AXIS3.value] = theta3_1
        else:
            RAD[0, constant.AXIS3.value] = theta3_2

        C3 = cos(RAD[0, constant.AXIS3.value])
        S3 = sin(RAD[0, constant.AXIS3.value])
        
        # Theta2
        mu1 = -a3 * S3 + d4 *C3
        mu2 = a3 * C3 + d4 * S3 + a2
        v1 = a3 * C3 + d4 * S3 + a2
        v2 = a3 * S3 - d4 * C3
        gama1 = Px * C1 + Py * S1 - a1
        gama2 = Pz - d1
        
        RAD[0, constant.AXIS2.value] = atan(((mu1 * gama2) - (gama1 * mu2)) / ((gama1 * v2) - (v1 * gama2)))
        
        C2 = cos(RAD[0, constant.AXIS2.value])
        S2 = sin(RAD[0, constant.AXIS2.value])
        C23 = cos(RAD[0, constant.AXIS2.value] - RAD[0, constant.AXIS3.value])
        S23 = sin(RAD[0, constant.AXIS2.value] - RAD[0, constant.AXIS3.value])
        
        # Theta5
        r21 = -U[0] * C1 * C23 - U[1] * S1 * C23 + U[2] * S23
        r22 = -V[0] * C1 * C23 - V[1] * S1 * C23 + V[2] * S23
        r23 = -W[0] * C1 * C23 - W[1] * S1 * C23 + W[2] * S23
        theta5_1 = atan2(sqrt(pow(r21, 2) + pow(r22, 2)), -r23)
        theta5_2 = atan2(-sqrt(pow(r21, 2) + pow(r22, 2)), -r23)
        
        if cnt ==0 or cnt == 2:
            RAD[0, constant.AXIS5.value] = theta5_1
        else:
            RAD[0, constant.AXIS5.value] = theta5_2
            
        C5 = cos(RAD[0, constant.AXIS5.value])
        S5 = sin(RAD[0, constant.AXIS5.value])
        # Theta4
        r13 = W[0] * C1 * S23 + W[1] * S1 * S23 + W[2] * C23
        r33 = W[0] * S1 - W[1] * C1
        
        if S5> constant.ERRC.value:
            RAD[0, constant.AXIS4.value] = atan2(-r33, r13)
        elif S5 < constant.ERRC.value:
            RAD[0, constant.AXIS4.value] = atan2(r33, -r13)
        C4 = cos(RAD[0, constant.AXIS4.value])
        S4 = sin(RAD[0, constant.AXIS4.value])
        
        #theta 6
        if S5 > constant.ERRC.value:
            RAD[0, constant.AXIS6.value] = atan2(-r22, r21)
        elif S5 < constant.ERRC.value:
            RAD[0, constant.AXIS6.value] = atan2(r22, -r21)
        for i in range(constant.AXIS1.value,constant.TOTAL_AXES.value ):
            THETA[cnt][i]= RAD[0, i]
        if cnt==3:
            passkey = 0
        cnt = cnt+1
        
        for i in range(0, cnt):
            for j in range(constant.AXIS1.value, constant.TOTAL_AXES.value):
                dT[i][j] = THETA[i][j]*constant.RAD2DEG.value - actjoint[j] 
                dif[0, i] = dif[0, i] + pow(dT[i][j], 2)
            dif[0, i] = sqrt(dif[0, i])
        dif_min = dif[0, 0]
        min = 0
        for i in range(1, 4):
            if dif_min>dif[0, i]:
                dif_min = dif[0, i]
                min = i
                
        for i in range(constant.AXIS1.value, constant.TOTAL_AXES.value):
            Joint_Deg.append(degrees(THETA[min][i]))
            actjoint[i] = degrees(THETA[min][i])
            
        return Joint_Deg
        
        
    
cpdef object Eul2R(double EUL[3]):
    cdef double RAD[3]
    cdef double Ca, Cb, Cg, Sa, Sb, Sg
    
    for i in range(0,3):
        RAD[i] = radians(EUL[i])
    
    Ca = cos(RAD[AFA])
    Cb = cos(RAD[BETA]) 
    Cg = cos(RAD[GAMA])
    Sa = sin(RAD[AFA])
    Sb = sin(RAD[BETA])
    Sg = sin(RAD[GAMA])
    
    """
    R[0 * 3 + 0] = Ca * Cg - Sa * Cb * Sg
    R[1 * 3 + 0] = Sa * Cg + Ca * Cb * Sg
    R[2 * 3 + 0] = Sb * Sg
    R[0 * 3 + 1] = -Ca * Sg - Sa * Cb * Cg
    R[1 * 3 + 1] = -Sa * Sg + Ca * Cb * Cg
    R[2 * 3 + 1] = Sb * Cg
    R[0 * 3 + 2] = Sa * Sb
    R[1 * 3 + 2] = -Ca * Sb
    R[2 * 3 + 2] = Cb
    """
    return  R = [[Ca * Cg - Sa * Cb * Sg, -Ca * Sg - Sa * Cb * Cg, Sa * Sb], 
                    [Sa * Cg + Ca * Cb * Sg, -Sa * Sg + Ca * Cb * Cg, -Ca * Sb],
                    [Sb * Sg, Sb * Cg, Cb]]

#cdef extern from "core\kinematic\Invers_kinematic\robotinverse.h":        
#    cpdef double Inverse_Kinematic(double TCP[3], double TOV[3])
