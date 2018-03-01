#python3 foward kinematic
from ..constant import constant

class foward_kinematic():
    def __init__(self):
        AXIS1 = constant.AXIS1.value
        AXIS2 = constant.AXIS2.value
        AXIS3 = constant.AXIS3.value
        AXIS4 = constant.AXIS4.value
        AXIS5 = constant.AXIS5.value
        AXIS6 = constant.AXIS6.value
        TOTAL_AXES = constant.TOTAL_AXES.value
        DEG2RAD = constant.DEG2RAD.value
        self.a1 = constant.a1.value
        self.a2 = constant.a2.value
        self.a3 = constant.a3.value
        self.d1 = constant.d1.value
        self.d4 = constant.d4.value
        self.d6 = constant.d6.value
        
        
    def Forward_Kinematic(self, DEG):
        RAD = []
        d6h = self.d6
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
        
        X = C1 * (self.a1 + C23 * (d6h * C5 + d4) + self.a2 * S2 + S23 * (self.a3 + d6h * C4 * S5)) - d6h * S1 * S4 * S5
        Y = S1 * (self.a1 + C23 * (d6h * C5 + d4) + self.a2 * S2 + S23 * (self.a3 + d6h * C4 * S5)) + d6h * C1 * S4 * S5
        Z = self.d1 - S23 * (d6h * C5 + self.d4) + self.a2 * C2 + C23 * (self.a3 + d6h * C4 * S5)
        TCP = [X, Y, Z]
        print(self.R2Eul(UVW))
        return TCP, self.R2Eul(UVW)
        
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
