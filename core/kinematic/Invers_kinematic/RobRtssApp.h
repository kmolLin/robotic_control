﻿//////////////////////////////////////////////////////////////////
//
// RobRtssApp.h - header file
//
// This file was generated using the RTX64 Application Template for Visual Studio.
//
// Created: 2017/8/14 下午 05:53:06 
// User: User
//
//////////////////////////////////////////////////////////////////

#pragma once
//This define will deprecate all unsupported Microsoft C-runtime functions when compiled under RTSS.
//If using this define, #include <rtapi.h> should remain below all windows headers
//#define UNDER_RTSS_UNSUPPORTED_CRT_APIS


//#include <stdio.h>
//#include <string.h>
//#include <ctype.h>
//#include <conio.h>
//#include <stdlib.h>
#include <math.h>

void P2Pplanning(double m[6], double Vmax);
void EulerIntr(double act_tcp[3], double act_tov[3], double tar_tcp[3], double tar_tov[3]);
void Inverse_Kinematic(double TCP[3], double TOV[3], double* Joint_Deg);
void Eul2R(double EUL[3], double *R);
void R2Eul(double R[3][3], double* EUL);
void Eulstr2end(double ES[3], double EE[3], double* ESE);
void Movement(double Pact[3], double Ptar[3], double ESE[3], double* MOVEMONT);
void Exit_Process();

//test
double S_shape(int cnt);
  
