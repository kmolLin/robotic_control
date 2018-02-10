from math import *
from ..constant import constant
import numpy as np
"""
AFA = 0
BETA = 1
GAMA = 2
TOTAL_TOV = 3
DEG2RAD = pi/180.0
RAD2DEG = 180.0/pi

# 6-AXES ID
AXIS1 = 0
AXIS2 = 1
AXIS3 = 2
AXIS4 = 3
AXIS5 = 4
AXIS6 = 5
TOTAL_AXES = 6

#Error Value
#constant.ERRC.value = 1E-6

# D-H Table
a1 = 30.0
a2 = 340.0
a3 = 40.0
d1 = 375.0
d4 = 338.0
d6 = 86.5

"""
#
offset = 10

class armrobot():
    def __init__(self):
        
        self.a1 = constant.a1.value
        self.a2 = constant.a2.value
        self.a3 = constant.a3.value
        self.d1 = constant.d1.value
        self.d4 = constant.d4.value
        self.d6 = constant.d6.value
        pass
    """
    def Forward_Kinematic(self, DEG):
        RAD = []
        d6h = d6
        for i in range(AXIS1,TOTAL_AXES ):
            RAD.append( DEG[i] * DEG2RAD)
        C1 = cos(RAD[AXIS1])
        C2 = cos(RAD[AXIS2])
        C3 = cos(RAD[AXIS3])
        C4 = cos(RAD[AXIS4])
        C5 = cos(RAD[AXIS5])
        C6 = cos(RAD[AXIS6])
        S1 = sin(RAD[AXIS1])
        S2 = sin(RAD[AXIS2])
        S3 = sin(RAD[AXIS3])
        S4 = sin(RAD[AXIS4])
        S5 = sin(RAD[AXIS5])
        S6 = sin(RAD[AXIS6])
        C23 = cos(RAD[AXIS2] - RAD[AXIS3])
        S23 = sin(RAD[AXIS2] - RAD[AXIS3])

        UVW[0][0] = C1 * S23 * (C4 * C5 * C6 + S4 * S6) - C1 * C23 *S5 * C6 + S1 * (C4 * S6 - S4 * C5 * C6)
        UVW[1][0] = S1 * S23 * (C4 * C5 * C6 + S4 * S6) - S1 * C23 *S5 * C6 - C1 * (C4 * S6 - S4 * C5 * C6)
        UVW[2][0] = C23 * (C4 * C5 * C6 + S4 * S6) + S23 * S5 * C6
        UVW[0][1] = C1 * S23 * (S4 * C6 - C4 * C5 * S6) + C1 * C23 * S5 * S6 + S1 * (S4 * C5 * S6 + C4 * C6)
        UVW[1][1] = S1 * S23 * (S4 * C6 - C4 * C5 * S6) + S1 * C23 * S5 * S6 - C1 * (S4 * C5 * S6 + C4 * C6)
        UVW[2][1] = C23 * (S4 * C6 - C4 * C5 * S6) - S23 * S5 * S6
        UVW[0][2] = C1 * S23 * C4 * S5 + C1 * C23 * C5 - S1 * S4 * S5
        UVW[1][2] = S1 * S23 * C4 * S5 + S1 * C23 * C5 + C1 * S4 * S5
        UVW[2][2] = C23 * C4 * S5 - S23 * C5

        
        
        
        a = C1 * S23 * (C4 * C5 * C6 + S4 * S6) - C1 * C23 *S5 * C6 + S1 * (C4 * S6 - S4 * C5 * C6)
        b = S1 * S23 * (C4 * C5 * C6 + S4 * S6) - S1 * C23 *S5 * C6 - C1 * (C4 * S6 - S4 * C5 * C6)
        c = C23 * (C4 * C5 * C6 + S4 * S6) + S23 * S5 * C6
        d = C1 * S23 * (S4 * C6 - C4 * C5 * S6) + C1 * C23 * S5 * S6 + S1 * (S4 * C5 * S6 + C4 * C6)
        e = S1 * S23 * (S4 * C6 - C4 * C5 * S6) + S1 * C23 * S5 * S6 - C1 * (S4 * C5 * S6 + C4 * C6)
        f = C23 * (S4 * C6 - C4 * C5 * S6) - S23 * S5 * S6
        g = C1 * S23 * C4 * S5 + C1 * C23 * C5 - S1 * S4 * S5
        h = S1 * S23 * C4 * S5 + S1 * C23 * C5 + C1 * S4 * S5
        i = C23 * C4 * S5 - S23 * C5
        UVW = [[a, b, c], [d, e, f], [g, h, i]]
        
        X = C1 * (a1 + C23 * (d6h * C5 + d4) + a2 * S2 + S23 * (a3 + d6h * C4 * S5)) - d6h * S1 * S4 * S5
        Y = S1 * (a1 + C23 * (d6h * C5 + d4) + a2 * S2 + S23 * (a3 + d6h * C4 * S5)) + d6h * C1 * S4 * S5
        Z = d1 - S23 * (d6h * C5 + d4) + a2 * C2 + C23 * (a3 + d6h * C4 * S5)
        TCP = [X, Y, Z]
        print(TCP)
        #print("*"*8)
        #print(self.R2Eul(UVW))
        #print("*"*10)
        print(self.R2Eul(UVW))
        return TCP, self.R2Eul(UVW)
    """
    
    
    def Inverse_Kinematic(self, TCP, TOV, actjoint):
        
        RAD = np.zeros((1, 6))
        THETA =  np.zeros((4, 6))
        dT = np.zeros((4, 6))
        U=[]
        V=[]
        W=[]
        Joint_Deg = []
        dif = np.zeros((1, 4))
        UVM =  self.Eul2R(TOV)
        #print(UVM)
        d6h = 0
        
        for i in range(0, 3):
            U.append(UVM[i][0])  #appen
            V.append(UVM[i][1]) 
            W.append(UVM[i][2]) 

        Px = TCP[0]-d6h*W[0]
        Py = TCP[1]-d6h*W[1]
        Pz = TCP[2]-d6h*W[2]
        cnt = 0
        passkey = 1
        
        while(passkey):
            # Theta1
            RAD[0, 0] = atan2(Py, Px)
            #print(RAD[0, 0]*RAD2DEG)
            C1 = cos(RAD[0, 0])
            S1 = sin(RAD[0, 0])
            # Theta3    +- ???
            Px2 = pow(Px, 2)
            Py2 = pow(Py, 2)
            Pz2 = pow(Pz - d1, 2) ##d1
            k1 = 2.0 * a2 * d4
            k2 = 2.0 * a2 * a3
            k3 = Px2 + Py2 + Pz2 - 2.0 * a1 * (Px * C1 + Py * S1) + pow(a1, 2) - pow(a3, 2) - pow(d4, 2) - pow(a2, 2)
            kcnt = pow(k1, 2) + pow(k2, 2) - pow(k3, 2)
            if kcnt < 0:
                print("Didn't have correct code.")
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
                RAD[0, AXIS4] = atan2(-r33, r13)
            elif S5 < constant.ERRC.value:
                RAD[0, AXIS4] = atan2(r33, -r13)
            
            C4 = cos(RAD[0, AXIS4])
            S4 = sin(RAD[0, AXIS4])
            
            #theta 6
            if S5 > constant.ERRC.value:
                RAD[0, constant.AXIS6.value] = atan2(-r22, r21)
            elif S5 < constant.ERRC.value:
                RAD[0, constant.AXIS6.value] = atan2(r22, -r21)
                
            for i in range(AXIS1,constant.TOTAL_AXES.value ):
                THETA[cnt][i]= RAD[0, i]
            
            if cnt==3:
                passkey = 0
            cnt = cnt+1
        #print(THETA*RAD2DEG)
        for i in range(0, cnt):
            for j in range(AXIS1, constant.TOTAL_AXES.value):
                dT[i][j] = THETA[i][j]*constant.RAD2DEG.value - actjoint[j] # TODO : not sure  - act_joint[j]
                #print(dT[i][j])
                dif[0, i] = dif[0, i] + pow(dT[i][j], 2)
            dif[0, i] = sqrt(dif[0, i])
        dif_min = dif[0, 0]
        min = 0
        for i in range(1, 4):
            if dif_min>dif[0, i]:
                dif_min = dif[0, i]
                min = i
        for i in range(AXIS1, TOTAL_AXES):
            Joint_Deg.append(THETA[min][i]* constant.RAD2DEG.value)
            actjoint[i] = THETA[min][i] * constant.RAD2DEG.value
        
        print(Joint_Deg)
        return Joint_Deg
        
    def Eul2R(self, EUL):
        RAD = []
        for i in range(constant.AFA.value, 3):
            RAD.append(EUL[i]*constant.DEG2RAD.value)
            
        Ca = cos(RAD[constant.AFA.value])
        Cb = cos(RAD[constant.BETA.value])
        Cg = cos(RAD[constant.GAMA.value])
        Sa = sin(RAD[constant.AFA.value])
        Sb = sin(RAD[constant.BETA.value])
        Sg = sin(RAD[constant.GAMA.value])
        R = [Ca * Cg - Sa * Cb * Sg,Sa * Cg + Ca * Cb * Sg,  Sb * Sg], [-Ca * Sg - Sa * Cb * Cg,-Sa * Sg + Ca * Cb * Cg ,Sb * Cg ], [Sa * Sb,-Ca * Sb, Cb ]
        return R    
    
    def R2Eul(self, R):
        RAD = [0.0, 0.0, 0.0]
        U = []
        V = []
        W = []
        EUL = []
        for i in range(0, 3):
            U.append(R[i][0])
            V.append(R[i][1])
            W.append(R[i][2])
        
        RAD[constant.BETA.value] = atan2(sqrt(pow(W[0], 2) + pow(W[1], 2)), W[2])
        if (fabs(sin(RAD[constant.BETA.value])) <= constant.ERRC.value):
            RAD[constant.GAMA.value] = 0.0
            RAD[constant.AFA.value] = atan2(V[0], U[0])
        else:
            RAD[constant.AFA.value] = atan2(W[0], (-W[1]))
        
        if fabs(RAD[constant.AFA.value]) + fabs(RAD[constant.GAMA.value]) >= pi:
            RAD[constant.BETA.value] = atan2(-sqrt(pow(W[0], 2) + pow(W[1], 2)), W[2])
            RAD[constant.AFA.value] = atan2(-W[0], W[1])
            RAD[constant.GAMA.value] = atan2(-U[2], -V[2])
        for i in range(constant.AFA.value, constant.TOTAL_TOV.value):
            EUL.append( RAD[i] * RAD2DEG)
        return EUL
        
"""
if __name__=='__main__':
    import sys
    a = armrobot()
    #TCP = [0.0, 368.0, 500]
    TCP = [300.229, -50.919, 600.0]
    #TOV = [180.0, 0.0, 0.0]
    TOV = [-90.0, 0.0, 90.0]
    DEG = [0, 0, 90, 0, 0, 0]
    #GG = [180.0, 13.700509349103092, 114.13038634373724, -180.0, 10.429876994634144, -0.0]
    #a.Forward_Kinematic(DEG)
    act = [89.9, 0.0, -0.0, -0.0, -90.0, 0.0]
    c =  a.Inverse_Kinematic(TCP, TOV, act)
    #d, e = a.Forward_Kinematic(GG)
    print(c)
    #print(e)
"""
    
    
    
    
    
    
