import OpenGL.GL as gl
import OpenGL.GLU as glu
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QOpenGLWidget


class GLWidget(QOpenGLWidget):
    
    
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        #self.robot = parent.robot
        self.pitch = 30.0
        self.yaw = 0.0
        self.distance =7.0
        
    def initializeGL(self):
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glClearDepth(1.0)
        gl.glEnable(gl.GL_CULL_FACE)

        
        gl.glEnable(gl.GL_POINT_SMOOTH)
        gl.glPointSize(10.0)
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glHint(gl.GL_POLYGON_SMOOTH_HINT, gl.GL_NICEST)
        gl.glHint(gl.GL_PERSPECTIVE_CORRECTION_HINT, gl.GL_NICEST)
        gl.glClearColor(0.0, 0.0, 0.0, 0.0)
        
    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT and gl.GL_DEPTH_BUFFER_BIT)
        self.setView()
        self.setLight()
        
        gl.glEnable(gl.GL_COLOR_MATERIAL)
        gl.glDisable(gl.GL_LIGHTING)
        gl.glColor4f(0.0, 0.5, 0.0, 0.5)
        
        for i in range(0, 21):
            gl.glBegin(gl.GL_LINES)
            gl.glVertex3f(-5.0+0.5*i, -5.0, 0.0) 
            gl.glVertex3f(-5.0+0.5*i, 5.0, 0.0)
            gl.glVertex3f(-5.0, -5.0+0.5*i, 0.0)
            gl.glVertex3f(5.0, -5.0+0.5*i, 0.0)
            gl.glEnd()
        gl.glColor4f(0.5, 0.5, 0.0, 0.5)
        gl.glBegin(gl.GL_LINES)
        
        #gl.glVertex3f(robot.getY(), -robot.getX(), 0.0)
        #gl.glVertex3f(robot.getY(), -robot.getX(), robot.getZ()+0.5)
        gl.glEnd()
        
        #gl.glColor4f(0.9, 0.0, 0.0, 0.5)
        #robot.displayPath()
        
        #gl.glDisable(gl.GL_COLOR_MATERIAL)
        #gl.glEnable(gl.GL_LIGHTING)
        #robot.display()
        gl.glFlush()
    def resizeGL(self, _w, _h):
        self.w = _w
        self.h = _h
        #gl.glViewport(0.0, 0.0, self.w, self.h)
        self.setView()
        
    def setPitch(self, _pitch):
        self.pitch = _pitch
    def setYaw(self, _yaw):
        self.yaw = _yaw
        
    def setDistance(self,_distance):
        self.distance = _distance
        
    def setView(self):
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        glu.gluPerspective(60.0, 1.0*(self.w/self.h), 0.1, 100.0)

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

        glu.gluLookAt(-self.distance, 0.0, 0.0, 
                  0.0, 0.0, 0.0,
                  0.0, 0.0, 1.0)
        gl.glRotatef(self.pitch, 0.0, -1.0, 0.0)
        gl.glRotatef(self.yaw, 0.0, 0.0, -1.0)
    def setLight(self):
        lamb = [ 0.1, 0.1, 0.1, 1.0 ]
        ldif = [1.0, 1.0, 1.0, 1.0]
        lpos = [-10.0, -10.0, 10.0, 1.0]
        gl.glEnable(gl.GL_COLOR_MATERIAL)
        gl.glDisable(gl.GL_LIGHTING)
        gl.glDisable(gl.GL_LIGHT0)
        gl.glColor4fv(ldif)
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex4fv(lpos)
        gl.glEnd()
        gl.glDisable(gl.GL_COLOR_MATERIAL)
        gl.glEnable(gl.GL_LIGHTING)
        gl.glEnable(gl.GL_LIGHT0)
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, lpos)
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_AMBIENT, lamb)
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, ldif)
        
    
