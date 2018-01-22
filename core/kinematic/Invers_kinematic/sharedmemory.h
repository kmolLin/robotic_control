#ifndef _SHAREDMEMORY_H
#define _SHAREDMEMORY_H

#pragma once
#include "NexCoeMotion.h"

#define PI       (4.0 * atan(1.0))
#define DEG2RAD  (PI / 180.0)
#define RAD2DEG  (180.0 / PI)

#define SHM_NAME  _T("6AxisRobot")
#define EVN_NAME_START_MASTER  _T("Start_Master")
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

typedef struct
{
	double      Deg2Pulse[6];
	double      Pulse2Deg[6];
	double      Gear_Ratio[6];
	I32_T       PULSE[6];
}Unit_Conv;

typedef struct
{
	double		CtrMode;
	double		Gripara[3];
	double		RobVel;
	int         Vac;
	double		Cmd[6];
	double		Feedrate;
	int			bpv, bkp;
	double		ds[6], T[6];
	int			fbp[6];
	double		len;
}NfuNC;

typedef	struct
{
	double		CtrMode;
	double		Gripara[3];
	double		Cmd[6];
	double		Feedrate;
	int			bpv, bkp;
	double		ds[6], T[6], Kma[6], Kta[6];
	int			fbp[6];
	double		len, dsmax, Kmt, Ktm;
	int			mas;
}CVF;

typedef struct
{
	CANAxis_T   mAxis[6];
	U16_T       masterId;
	U16_T       MasterState;
	I32_T       ReadActualPos[6];
	double      DisplayActualPos[6];
	double      ActualTCP[3];
	double      ActualTOV[3];
	I32_T       TargetPos[6];
	I32_T       Velcity;
	////////////////////////////////////	
	Unit_Conv   UnitConversion;
	NfuNC		NCFIFO[5000];
	CVF			CVFFIFO[5000];
	////////////////////////////////////	
	int         UIStop;
	int         UIServoOnOff;
	int         UIJog;
	int			UIAxisSel;
	int         UIMove;
	int         UIJointCtr;
	int         UIP2PCtr;
	int         UICPCtr;
	int         UIPaint;
	int         UIReadTxt;
	////////////////////////////////////
	int         MotionMode;
	int         Interpolate;
	int         Count;
	double      ZeroOffset[6]; //Unit:degree
	double      TCPOffset[3];  //Unit:mm
	double      ToolOffset;
	int         BasicPos[6];   //Unit:pulse
	double      MovingPos[6];
	double      MovingTCP[3];
	double      MovingTOV[3];
	int         NCnum, CVFnum;
	int         Ctov;

	BOOL		GOpen;
	BOOL		GClose;
	BOOL		GMove;
	int			GPosition, GPostion1;
	int			GSpeed, GSpeed1;
	int			GForce, GForce1;
	double      GDelay;
}SHV;

static SHV *shv;

#endif