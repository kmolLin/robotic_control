# distutils: language=c++

cdef extern from "v_repMath/4x4Matrix.h":        
    cdef cppclass C4X4Matrix 

cdef extern from "v_repMath/3Vector.h":
    cdef cppclass C3Vector:
        C3Vector()
        C3Vector(float v0,float v1,float v2)
        C3Vector(float v[3])
        C3Vector(C3Vector& v)
        float* ptr()

cdef extern from "v_repMath/4Vector.h":
    cdef cppclass C4Vector:  
        C4Vector()
        C4Vector(float v0,float v1,float v2,float v3)
        C4Vector(float v[4])
        C4Vector(C3Vector& v)
        C4Vector(C4Vector& q)
        C4Vector(float a,float b,float g)
        C4Vector(float angle, C3Vector& axis)
        C4Vector(C3Vector& startV, C3Vector& endV)


        C3Vector getEulerAngles()
        
cdef extern from "v_repMath/6Vector.h":
    cdef cppclass C6Vector:
        C6Vector()
        C6Vector(float v0,float v1,float v2,float v3,float v4,float v5)
        C6Vector( float v[6])
        C6Vector(C3Vector& v0, C3Vector& v1)
        C6Vector(C6Vector& v)
        void clear()
        
cdef extern from "v_repMath/7Vector.h":
    cdef cppclass C7Vector:
        C7Vector()
        C7Vector(C7Vector& v)
        C7Vector(C4Vector& q)
        C7Vector(C3Vector& x)
        C7Vector(C4Vector& q,C3Vector& x)
        C7Vector(float m[4][4])
        C7Vector(C4X4Matrix& m)
        C7Vector(float angle,C3Vector& pos,C3Vector& dir)

cdef extern from "v_repMath/Vector.h":
    cdef cppclass CVector:
        CVector()
        CVector(int nElements)
        CVector(C3Vector& v)
        CVector(C4Vector& v)
        CVector(C6Vector& v)
        CVector(C7Vector& v)
        CVector(CVector& v)

cdef extern from "v_repMath/3x3Matrix.h":
    cdef cppclass C3X3Matrix:
        C3X3Matrix()
        C3X3Matrix(C4Vector& q)
        C3X3Matrix(C3X3Matrix& m)
        C3X3Matrix(C3Vector& xAxis, C3Vector& yAxis, C3Vector& zAxis)

cdef extern from "v_repMath/4x4Matrix.h":        
    cdef cppclass C4X4Matrix:
        C4X4Matrix()
        C4X4Matrix(C4X4Matrix& m)
        C4X4Matrix(CMatrix& m)
        C4X4Matrix(float m[4][4])
        C4X4Matrix(C3X3Matrix& m, C3Vector& x)
        C4X4Matrix(C3Vector& x, C3Vector& y, C3Vector& z, C3Vector& pos)
        C4X4Matrix(C7Vector& transf)

cdef extern from "v_repMath/4X4FullMatrix.h":
    cdef cppclass C4X4FullMatrix:
        C4X4FullMatrix()   # Needed for serialization
        C4X4FullMatrix(C4X4Matrix& m)
        C4X4FullMatrix(C4X4FullMatrix& m)

cdef extern from "v_repMath/6X6Matrix.h":
    cdef cppclass C6X6Matrix:
        C6X6Matrix()
        C6X6Matrix(C6X6Matrix& m)
        C6X6Matrix(C3X3Matrix& m00,C3X3Matrix& m01, C3X3Matrix& m10, C3X3Matrix& m11)

cdef extern from "v_repMath/MMatrix.h":
    cdef cppclass CMatrix:
        CMatrix()
        CMatrix(int nRows,int nCols)
        CMatrix(C3X3Matrix& m)
        CMatrix(C4X4Matrix& m)
        CMatrix(C6X6Matrix& m)
        CMatrix(CMatrix& m)

cdef extern from "v_repMath/VPoint.h":
    cdef cppclass VPoint:
        VPoint() 
        VPoint(int initX,int initY) 

from libcpp cimport bool

cdef extern from "v_repMath/MyMath.h":
    cdef cppclass CMath:
        CMath()
        @staticmethod
        void limitValue(float minValue,float maxValue,float &value)
        @staticmethod
        void limitValue(int minValue,int maxValue,int &value)

        @staticmethod
        float robustAsin(float v)
        @staticmethod
        float robustAcos(float v)
        @staticmethod
        float robustFmod(float v,float w)
        @staticmethod
        double robustmod(double v,double w)
        @staticmethod
        bool isFloatNumberOk(float v)
        @staticmethod
        bool isDoubleNumberOk(double v)

        
