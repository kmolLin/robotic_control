from math import *
import numpy as np

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
ERRC = 1E-6

# D-H Table
a1 = 30.0
a2 = 340.0
a3 = 40.0
d1 = 375.0
d4 = 338.0
d6 = 86.5

#
offset = 10

class armrobot():
    
    def Forward_Kinematic(self, DEG):
        RAD = [6]
        d6h = d6#+offset
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
        """
        UVW[0][0] = C1 * S23 * (C4 * C5 * C6 + S4 * S6) - C1 * C23 *S5 * C6 + S1 * (C4 * S6 - S4 * C5 * C6)
        UVW[1][0] = S1 * S23 * (C4 * C5 * C6 + S4 * S6) - S1 * C23 *S5 * C6 - C1 * (C4 * S6 - S4 * C5 * C6)
        UVW[2][0] = C23 * (C4 * C5 * C6 + S4 * S6) + S23 * S5 * C6
        UVW[0][1] = C1 * S23 * (S4 * C6 - C4 * C5 * S6) + C1 * C23 * S5 * S6 + S1 * (S4 * C5 * S6 + C4 * C6)
        UVW[1][1] = S1 * S23 * (S4 * C6 - C4 * C5 * S6) + S1 * C23 * S5 * S6 - C1 * (S4 * C5 * S6 + C4 * C6)
        UVW[2][1] = C23 * (S4 * C6 - C4 * C5 * S6) - S23 * S5 * S6
        UVW[0][2] = C1 * S23 * C4 * S5 + C1 * C23 * C5 - S1 * S4 * S5
        UVW[1][2] = S1 * S23 * C4 * S5 + S1 * C23 * C5 + C1 * S4 * S5
        UVW[2][2] = C23 * C4 * S5 - S23 * C5
        """
        
        
        
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
        print(self.R2Eul(UVW))
        return self.R2Eul(UVW)
        
    
    
    def Inverse_Kinematic(self, TCP, TOV):
        RAD = np.zeros((1, 6))
        THETA =  np.zeros((4, 6))
        dT = np.zeros((4, 6))
        U=[]
        V=[]
        W=[]
        dif = [4]
        UVM =  self.Eul2R(TOV)
        
        for i in range(0, 3):
            U.append(UVM[i][0])  #appen
            V.append(UVM[i][1]) 
            W.append(UVM[i][2]) 
            
            
        Px = TCP[0]
        Py = TCP[1]
        Pz = TCP[2]
        cnt = 0
        passkey = 1
        while(passkey):
            # Theta1
            RAD[0, 0] = atan2(Py, Px)
            #print(cos(RAD[0]))
            C1 = cos(RAD[0, 0])
            S1 = sin(RAD[0, 0])
            # Theta3
            Px2 = pow(Px, 2)
            Py2 = pow(Py, 2)
            Pz2 = pow(Pz - d1, 2)
            k1 = 2.0 * a2 * d4
            k2 = 2.0 * a2 * a3
            k3 = Px2 + Py2 + Pz2 - 2.0 * a1 * (Px * C1 + Py * S1) + pow(a1, 2) - pow(a3, 2) - pow(d4, 2) - pow(a2, 2)
            kcnt = k1*k1 + k2*k2 - k3*k3
            theta3_1 = 2.0 * atan((k1 + sqrt(kcnt)) / (k2 + k3))
            theta3_2 = 2.0 * atan((k1 - sqrt(kcnt)) / (k2 + k3))
           
            RAD[0, 4] = 20.0
            print(theta3_1)
            #print(RAD[0, 0])
            if cnt <=1:
                RAD[0, AXIS3] = theta3_1
            else:
                RAD[0, AXIS3] = theta3_2
                
            C3 = cos(RAD[0, AXIS3])
            S3 = sin(RAD[0, AXIS3])
            # Theta2
            mu1 = -a3 * S3 + d4 *C3
            mu2 = a3 * C3 + d4 * S3 + a2
            v1 = a3 * C3 + d4 * S3 + a2
            v2 = a3 * S3 - d4 * C3
            gama1 = Px * C1 + Py * S1 - a1
            gama2 = Pz - d1
            RAD[0, AXIS2] = atan(((mu1 * gama2) - (gama1 * mu2)) / ((gama1 * v2) - (v1 * gama2)))
            C2 = cos(RAD[0, AXIS2])
            S2 = sin(RAD[0, AXIS2])
            C23 = cos(RAD[0, AXIS2] - RAD[0, AXIS3])
            S23 = sin(RAD[0, AXIS2] - RAD[0, AXIS3])
            # Theta5
            r21 = -U[0] * C1 * C23 - U[1] * S1 * C23 + U[2] * S23
            r22 = -V[0] * C1 * C23 - V[1] * S1 * C23 + V[2] * S23
            r23 = -W[0] * C1 * C23 - W[1] * S1 * C23 + W[2] * S23
            theta5_1 = atan2(sqrt(pow(r21, 2) + pow(r22, 2)), -r23)
            theta5_2 = atan2(-sqrt(pow(r21, 2) + pow(r22, 2)), -r23)
            if cnt ==0 or cnt == 2:
                RAD[0, AXIS5] = theta5_1
            else:
                RAD[0, AXIS5] = theta5_2
            C5 = cos(RAD[0, AXIS5])
            S5 = sin(RAD[0, AXIS5])
            # Theta4
            r13 = W[0] * C1 * S23 + W[1] * S1 * S23 + W[2] * C23
            r33 = W[0] * S1 - W[1] * C1
            if S5> ERRC:
                RAD[0, AXIS4] = atan2(-r33, r13)
            elif S5 < ERRC:
                RAD[0, AXIS4] = atan2(r33, -r13)
            
            C4 = cos(RAD[0, AXIS4])
            S4 = sin(RAD[0, AXIS4])
            #theta 6
            if S5 > ERRC:
                RAD[0, AXIS6] = atan2(-r22, r21)
            elif S5 < ERRC:
                RAD[0, AXIS6] = atan2(r22, -r21)
                
            for i in range(AXIS1,TOTAL_AXES ):
                THETA[cnt][i]= RAD[0, i]
            
            if cnt==3:
                passkey = 0
            cnt = cnt+1
        #print(THETA)
        for i in range(0, cnt):
            for j in range(AXIS1, TOTAL_AXES):
                dT[i][j] = THETA[i][j]*RAD2DEG  # TODO : not sure  - act_joint[j]
                #print(dT[i][j])
                dif[i] = dif[i] + pow(dT[i][j], 2)
            dif[i] = sqrt(dif[i])
            
        dif_min = dif[0]
        min = 0
        for i in range(1, 4):
            if dif_min>dif[i]:
                dif_min = dif[i]
                min = i
        for i in range(AXIS1, TOTAL_AXES):
            Joint_Deg[i] = THETA[min][i] * RAD2DEG
            act_joint[i] = THETA[min][i] * RAD2DEG
        
        print(Joint_Deg)
        return Joint_Deg
        
    def Eul2R(self, EUL):
        RAD = []
        for i in range(AFA, 3):
            RAD.append(EUL[i]*DEG2RAD)
            
        Ca = cos(RAD[AFA])
        Cb = cos(RAD[BETA])
        Cg = cos(RAD[GAMA])
        Sa = sin(RAD[AFA])
        Sb = sin(RAD[BETA])
        Sg = sin(RAD[GAMA])
        R = [Ca * Cg - Sa * Cb * Sg,Sa * Cg + Ca * Cb * Sg,  Sb * Sg], [-Ca * Sg - Sa * Cb * Cg,-Sa * Sg + Ca * Cb * Cg ,Sb * Cg ], [Sa * Sb,-Ca * Sb, Cb ]
        return R    
    
    def R2Eul(self, R):
        RAD = [0.0, 0.0, 0.0]
        U = [3]
        V = [3]
        W = [3]
        EUL = []
        for i in range(0, 2):
            U.append(R[i][0])
            V.append(R[i][1])
            W.append(R[i][2])
        #print(U, V, W)
        
        RAD[BETA] = atan2(sqrt(pow(W[0], 2) + pow(W[1], 2)), W[2])
        if (fabs(sin(RAD[BETA])) <= ERRC):
            RAD[GAMA] = 0.0
            RAD[AFA] = atan2(V[0], U[0])
        else:
            RAD[AFA] = atan2(W[0], (-W[1]))
        
        if fabs(RAD[AFA]) + fabs(RAD[GAMA]) >= pi:
            RAD[BETA] = atan2(-sqrt(pow(W[0], 2) + pow(W[1], 2)), W[2])
            RAD[AFA] = atan2(-W[0], W[1])
            RAD[GAMA] = atan2(-U[3], -V[3])
        for i in range(AFA, TOTAL_TOV):
            EUL.append( RAD[i] * RAD2DEG)
        return EUL
        
        
if __name__=='__main__':
    a = armrobot()
    TCP = [150.2666498607823, -43.72852546813191, 377.0]
    TOV = [90.0, 71.56505117707799, 0.0]
    DEG = [0, -90, 180, -90, 90, 90]
    #a.Forward_Kinematic(DEG)
    a.Inverse_Kinematic(TCP, TOV)
    
    
    
    
    
    
    
