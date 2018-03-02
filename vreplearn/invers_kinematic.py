from math import *
from constant import constant
import numpy as np
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

    def Inverse_Kinematic(self, TCP, TOV, actjoint):
        a1 = self.a1
        a2 = self.a2
        a3 = self.a3
        d1 = self.d1
        d4 = self.d4
        d6 = self.d6
        
        RAD = np.zeros((1, 6))
        THETA =  np.zeros((4, 6))
        dT = np.zeros((4, 6))
        U=[]
        V=[]
        W=[]
        Joint_Deg = []
        dif = np.zeros((1, 4))
        UVM =  self.Eul2R(TOV)
        # TODO: need to make gui
        d6h = d6+offset
        
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
                #print("No correct answer.")
                check = False
                return (0, 0, 0, 0, 0, 0), check
                break
            else :
                theta3_1 = 2.0 * atan((k1 + sqrt(kcnt)) / (k2 + k3))
                theta3_2 = 2.0 * atan((k1 - sqrt(kcnt)) / (k2 + k3))
                check = True
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
            
        return Joint_Deg , check
        
    def Eul2R(self, EUL):
        RAD = []
        for i in range(constant.AFA.value, 3):
            RAD.append(radians(EUL[i]))
            
        Ca = cos(RAD[constant.AFA.value])
        Cb = cos(RAD[constant.BETA.value])
        Cg = cos(RAD[constant.GAMA.value])
        Sa = sin(RAD[constant.AFA.value])
        Sb = sin(RAD[constant.BETA.value])
        Sg = sin(RAD[constant.GAMA.value])
        R = [[Ca * Cg - Sa * Cb * Sg, Sa * Cg + Ca * Cb * Sg,Sb * Sg ], [-Ca * Sg - Sa * Cb * Cg, -Sa * Sg + Ca * Cb * Cg, Sa * Sb  ], [ Sb * Cg, -Ca * Sb, Cb]]
        return R 
    
    
    
    
    
    
