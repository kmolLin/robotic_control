# -*- coding: utf-8 -*-
from libc.math cimport (
    pow,
    sqrt,
    isnan,
    sin,
    cos,
    atan2
)
from cpython cimport bool

nan = float("nan");

cpdef object armInverse(double TCP[3], double TOV[3]):
    cdef double  C1, C2, C3, C4, C5, S1, S2, S3, S4, S5, C23, S23;
	cdef double  Px, Py, Pz, k1, k2, k3, kcnt;
	cdef double  Px2, Py2, Pz2;
	cdef double  theta3_1, theta3_2, theta5_1, theta5_2;
	cdef double  mu1, mu2, v1, v2, gama1, gama2;
	cdef double  r13, r33, r21, r22, r23;
	cdef double  RAD[6], UVW[3][3], THETA[4][6], dT[4][6], dif[4];
	cdef double  U[3], V[3], W[3];
	cdef int       min, dif_min;
    
    
    Eul2R(TOV, &UVW[0][0])

#cdef extern from "core\kinematic\Invers_kinematic\robotinverse.h":        
#    cpdef double Inverse_Kinematic(double TCP[3], double TOV[3])
