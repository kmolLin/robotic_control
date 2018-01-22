

#include "robotinverse.h"

#define PI       (4.0 * atan(1.0))
#define DEG2RAD  (PI / 180.0)
#define RAD2DEG  (180.0 / PI)

#define CYCLE_TIME  500    // unit: micro-second

/***********************************************/
/*             6 - A X E S   I D  	           */
/***********************************************/
#define	AXIS1            0
#define	AXIS2			 1
#define	AXIS3			 2
#define	AXIS4			 3
#define	AXIS5			 4
#define	AXIS6			 5
#define	TOTAL_AXES		 6
//NEW
#define	TCPX			 6
#define	TCPY			 7
#define	TCPZ			 8

/***********************************************/
/*           T C P   D I R E C T I O N         */
/***********************************************/
#define X                0
#define Y                1
#define Z                2
#define TOOL             3 //T
#define TOTAL_TCP        3
#define A                3
#define B                4
#define C                5
#define MODE             6

/***********************************************/
/*             E U L E R   A N G L E           */
/***********************************************/
#define AFA              0
#define BETA             1
#define GAMA             2
#define TOTAL_TOV        3

/***********************************************/
/*             R - P - Y   A N G L E           */
/***********************************************/
#define ROLL             0
#define PITCH            1
#define YAW              2

/***********************************************/
/*               D - H   T A B L E             */
/***********************************************/
#define a1               30.0
#define a2               340.0
#define a3               40.0
#define d1               375.0
#define d4               338.0
#define d6               86.5

/***********************************************/
/*            S E R V O   S T A T E	           */
/***********************************************/
#define	SERVO_OFF		 0
#define	SERVO_ON		 1

/***********************************************/
/*            M O T I O N   M O D E	           */
/***********************************************/
#define	PRO_POS          1
#define	PRO_VEL			 3
#define	TOR_PRO			 4
#define	HOMING			 6
#define	ITR_POS			 7
#define	CYC_POS			 8
#define	CYC_VEL			 9
#define	CYC_TOR			 10

/***********************************************/
/*            J O G   V E L O C I T Y          */
/***********************************************/
#define	JOG_MAX          25000 // Unit: Pulse
#define	JOG_MIN			 0     // Unit: Pulse

/***********************************************/
/*             E R R O R   V A L U E           */
/***********************************************/
#define ERRC             1e-6

/***********************************************/
/*             C H O O S E N   T O V           */
/***********************************************/
#define INPUT            0
#define FORWARD          1
#define DOWN             2

/***********************************************/
/*             C H O O S E N   T O V           */
/***********************************************/
#define JOINT            0
#define PTP              1
#define CP               2
#define GRIP             3
#define VAC              4





extern SHV *shv;
HANDLE mSHV = NULL;
HANDLE mEVENT = NULL;
RTN_ERR ret;
U16_T   masterId = 0;
U16_T   slaveCnt;
SHV     SMData;
U8_T    DOData = 1;
TClintParam clientParam;
int Servo_flag[6];
double offset[6] = { 2.418372, -1.962033, -1.639384, 4.038733, 2.106662, 18.246204 };//-3.421195
int test = 0;
/***********************************************/
/*           P 2 P   P A R A M E T E R         */
/***********************************************/
double Ts = 0.0005;
double Jmax = 10000.0;
double dsmax, dVmin, dt, Lmin, k[6], kp[6], Nt[5], L[5];
double Lmov, Lc, Tacc, Tc, Tcnt;
double Vcmd, Acmd, Jcmd;
double p, v, a, j;
int    max, Nacc, Nc, type, N[6];
double act_joint[6];

int	   JogTc = 0, Jogcnt = 0, Jogwait = 0;
int	   JogBasicPos = 0;
double vel, revgain;
double JogBasicTCP[3], JogBasicTOV[3];
/***********************************************/
/*            C P   P A R A M E T E R          */
/***********************************************/
double Ese[3], M[4], K[4], Pact[3], Ptar[3], Eact[3], Etar[3], Ract[3][3];
double Pi[3], Ei[3], Efi[3], Ri[3][3], Rfi[3][3], Joint[6];
double ldsmax, dp;
int    lmax;

/***********************************************/
/*            N C   P A R A M E T E R          */
/***********************************************/
int    Pidx = 0;
double Cmd[6];



void Inverse_Kinematic(double TCP[3], double TOV[3])
{
	double  C1, C2, C3, C4, C5, S1, S2, S3, S4, S5, C23, S23;
	double  Px, Py, Pz, k1, k2, k3, kcnt;
	double  Px2, Py2, Pz2;
	double  theta3_1, theta3_2, theta5_1, theta5_2;
	double  mu1, mu2, v1, v2, gama1, gama2;
	double  r13, r33, r21, r22, r23;
	double  RAD[6], UVW[3][3], THETA[4][6], dT[4][6], dif[4];
	double  U[3], V[3], W[3];
	double  d6h = d6 + shv->ToolOffset;
	int     min, dif_min;

	ZeroMemory(&RAD, sizeof(RAD));
	ZeroMemory(&UVW, sizeof(UVW));
	ZeroMemory(&THETA, sizeof(THETA));
	ZeroMemory(&dif, sizeof(dif));

	Eul2R(TOV, &UVW[0][0]);

	for (int i = 0; i < 3; i++)
	{
		U[i] = UVW[i][0];	V[i] = UVW[i][1];	W[i] = UVW[i][2];
	}

	///  腕部中心點  ///
	Px = TCP[X] - d6h * W[X];
	Py = TCP[Y] - d6h * W[Y];
	Pz = TCP[Z] - d6h * W[Z];

	int cnt = 0, pass = 1;
	while (pass)
	{
		/// Theta1  ///
		RAD[AXIS1] = atan2(Py, Px);
		C1 = cos(RAD[AXIS1]);
		S1 = sin(RAD[AXIS1]);

		/// Theta3  ////
		Px2 = pow(Px, 2);
		Py2 = pow(Py, 2);
		Pz2 = pow(Pz - d1, 2);
		k1 = 2.0 * a2 * d4;
		k2 = 2.0 * a2 * a3;
		k3 = Px2 + Py2 + Pz2 - 2.0 * a1 * (Px * C1 + Py * S1) + pow(a1, 2) - pow(a3, 2) - pow(d4, 2) - pow(a2, 2);
		kcnt = pow(k1, 2) + pow(k2, 2) - pow(k3, 2);
		theta3_1 = 2.0 * atan((k1 + sqrt(kcnt)) / (k2 + k3));
		theta3_2 = 2.0 * atan((k1 - sqrt(kcnt)) / (k2 + k3));

		if (cnt <= 1)  RAD[AXIS3] = theta3_1;
		else           RAD[AXIS3] = theta3_2;

		C3 = cos(RAD[AXIS3]);
		S3 = sin(RAD[AXIS3]);

		//// Theta2 ////
		mu1 = -a3 * S3 + d4 *C3;
		mu2 = a3 * C3 + d4 * S3 + a2;
		v1 = a3 * C3 + d4 * S3 + a2;
		v2 = a3 * S3 - d4 * C3;
		gama1 = Px * C1 + Py * S1 - a1;
		gama2 = Pz - d1;

		RAD[AXIS2] = atan(((mu1 * gama2) - (gama1 * mu2)) / ((gama1 * v2) - (v1 * gama2)));

		C2 = cos(RAD[AXIS2]);
		S2 = sin(RAD[AXIS2]);
		C23 = cos(RAD[AXIS2] - RAD[AXIS3]);
		S23 = sin(RAD[AXIS2] - RAD[AXIS3]);

		//// Theta5 ////
		r21 = -U[X] * C1 * C23 - U[Y] * S1 * C23 + U[Z] * S23;
		r22 = -V[X] * C1 * C23 - V[Y] * S1 * C23 + V[Z] * S23;
		r23 = -W[X] * C1 * C23 - W[Y] * S1 * C23 + W[Z] * S23;

		theta5_1 = atan2(sqrt(pow(r21, 2) + pow(r22, 2)), -r23);
		theta5_2 = atan2(-sqrt(pow(r21, 2) + pow(r22, 2)), -r23);

		if (cnt == 0 || cnt == 2)  RAD[AXIS5] = theta5_1;
		else                       RAD[AXIS5] = theta5_2;

		C5 = cos(RAD[AXIS5]);
		S5 = sin(RAD[AXIS5]);

		//// Theta4 ////
		r13 = W[X] * C1 * S23 + W[Y] * S1 * S23 + W[Z] * C23;
		r33 = W[X] * S1 - W[Y] * C1;

		if (S5 > ERRC)         RAD[AXIS4] = atan2(-r33, r13);
		else if (S5 < ERRC)    RAD[AXIS4] = atan2(r33, -r13);

		C4 = cos(RAD[AXIS4]);
		S4 = sin(RAD[AXIS4]);

		//// Theta6 ////
		if (S5 > ERRC)         RAD[AXIS6] = atan2(-r22, r21);
		else if (S5 < ERRC)    RAD[AXIS6] = atan2(r22, -r21);

		for (int i = AXIS1; i < TOTAL_AXES; ++i)
		{
			THETA[cnt][i] = RAD[i];
		}

		if (cnt == 3) pass = 0;
		cnt = cnt + 1;
	}

	for (int i = 0; i < cnt; ++i)
	{
		for (int j = AXIS1; j < TOTAL_AXES; ++j)
		{
			dT[i][j] = THETA[i][j] * RAD2DEG - act_joint[j];
			dif[i] = dif[i] + pow(dT[i][j], 2);
		}
		dif[i] = sqrt(dif[i]);
	}

	dif_min = dif[0];
	min = 0;
	for (int i = 1; i < 4; ++i)
	{
		if (dif_min > dif[i])
		{
			dif_min = dif[i];
			min = i;
		}
	}

	for (int i = AXIS1; i < TOTAL_AXES; i++)
	{
		Joint_Deg[i] = THETA[min][i] * RAD2DEG;
		act_joint[i] = THETA[min][i] * RAD2DEG;
	}
	return double Joint_Deg;
}

void Eul2R(double EUL[3], double *R)
{
	double RAD[3];
	double Ca, Cb, Cg, Sa, Sb, Sg;

	ZeroMemory(&RAD, sizeof(RAD));
	for (int i = AFA; i < 3; i++){
		RAD[i] = EUL[i] * DEG2RAD;
	}

	Ca = cos(RAD[AFA]), Cb = cos(RAD[BETA]), Cg = cos(RAD[GAMA]);
	Sa = sin(RAD[AFA]), Sb = sin(RAD[BETA]), Sg = sin(RAD[GAMA]);

	R[0 * 3 + 0] = Ca * Cg - Sa * Cb * Sg;
	R[1 * 3 + 0] = Sa * Cg + Ca * Cb * Sg;
	R[2 * 3 + 0] = Sb * Sg;
	R[0 * 3 + 1] = -Ca * Sg - Sa * Cb * Cg;
	R[1 * 3 + 1] = -Sa * Sg + Ca * Cb * Cg;
	R[2 * 3 + 1] = Sb * Cg;
	R[0 * 3 + 2] = Sa * Sb;
	R[1 * 3 + 2] = -Ca * Sb;
	R[2 * 3 + 2] = Cb;
}

void R2Eul(double R[3][3], double* EUL)
{
	double RAD[3] = { 0.0, 0.0, 0.0 };
	double U[3], V[3], W[3];

	ZeroMemory(&RAD, sizeof(RAD));

	for (int i = 0; i < 3; i++){
		U[i] = R[i][0];	V[i] = R[i][1];	W[i] = R[i][2];
	}

	RAD[BETA] = atan2(sqrt(pow(W[0], 2) + pow(W[1], 2)), W[2]);

	if (fabs(sin(RAD[BETA])) <= ERRC){
		RAD[GAMA] = 0.0;
		RAD[AFA] = atan2(V[0], U[0]);
	}
	else{
		RAD[AFA] = atan2(W[0], (-W[1]));
		RAD[GAMA] = atan2(U[2], V[2]);
	}

	if (fabs(RAD[AFA]) + fabs(RAD[GAMA]) >= (4.0 * atan(1.0))){
		RAD[BETA] = atan2(-sqrt(pow(W[0], 2) + pow(W[1], 2)), W[2]);
		RAD[AFA] = atan2(-W[0], W[1]);
		RAD[GAMA] = atan2(-U[2], -V[2]);
	}

	for (int i = AFA; i < TOTAL_TOV; i++){ EUL[i] = RAD[i] * RAD2DEG; }