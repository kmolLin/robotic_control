cdef extern from "..core\kinematic\Invers_kinematic":        
    cpdef double Inverse_Kinematic(double TCP[3], double TOV[3])
