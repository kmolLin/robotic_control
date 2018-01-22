from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        Extension(
            "geomConstraintSolver",
            sources=[
                "..core\kinematic\Invers_kinematic.cpp",
            ],
        ),
        compiler_directives={'boundscheck':True}
    ),
    include_dirs=["..core\kinematic\Invers_kinematic", "v_repMath"]
)
