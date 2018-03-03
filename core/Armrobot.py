# armrobot class

from .model.model import Model
import OpenGL.GL as gl
from PyQt5.QtCore import QObject

class Armrobot(QObject):
    
    def __init__(self, parent = None):
        super(Armrobot, self).__init__(parent)
        self.baseModel = Model()
        self.arm1Model = Model()
        self.arm2Model = Model()
        self.arm3Model = Model()
        self.baseModel.load("base.obj")
        
    def display(self):
        self.baseModel.display()
        #gl.glTranslatef(0.0, 0.0, 0.9)
        """
        gl.glRotatef(th1, 0.0, 0.0, 1.0)
        arm1Model.display()
        gl.glTranslatef(0.0, -r1, 0.1)
        gl.glRotatef(th2, 0.0, 0.0, 1.0)
        arm2Model.display()
        gl.glTranslatef(0.0, -r2, -0.5 + z)
        arm3Model.display()
        """
        
