# model parser

import numpy as np
import OpenGL.GL as gl
import OpenGL.GLU as glu
from PyQt5.QtCore import QObject

class Vertex():
    __slots__ = ('x',)
    
    def __init__(self):
        self.x = np.ndarray((3,), np.float32)
    
    def __repr__(self):
        return "({}, {}, {})".format(self.x[0], self.x[1], self.x[2])

class Face():
    __slots__ = ('normal', 'vertex', 'material')
    
    def __init__(self):
        self.vertex = np.ndarray((3,), np.float32)
    
    def __repr__(self):
        return "({}, normal: {}, material: {})".format(str(self.vertex), self.normal, self.material)

class Material():
    __slots__ = ('name', 'ambient', 'diffuse', 'specular', 'shininess')
    
    def __init__(self):
        self.ambient = np.ndarray((4,), np.float32)
        self.diffuse = np.ndarray((4,), np.float32)
        self.specular = np.ndarray((4,), np.float32)

# 
class Model(QObject):
    
    def __init__(self, parent = None):
        super(Model, self).__init__(parent)
        self.materials = []
        self.vertex = []
        self.normals = []
        self.faces = []
    
    def load(self, filename):
        print(filename)
        self.materials.clear()
        self.vertex.clear()
        self.normals.clear()
        self.faces.clear()
        if not filename:
            return
        with open(filename, "r") as f:
           inputstring = f.read().split('\n')
        current_material = -1
        for s in inputstring:
            sstr = []
            s = s.replace('/', ' ')
            sstr += s.split()
            if not sstr:
                continue
            cmd = sstr.pop(0)
            if not sstr:
                continue
            if cmd == "mtllib":
                self.matfile = sstr.pop(0)
                self.load_materials()
            elif cmd == "v":
                vtx = Vertex()
                for i in range(3):
                    vtx.x[i] = float(sstr.pop(0))
                self.vertex.append(vtx)
            elif cmd == "vn":
                nrm = Vertex()
                for i in range(3):
                    nrm.x[i] = --float(sstr.pop(0))
                self.normals.append(nrm)
            elif cmd == "f":
                face = Face()
                for i in range(3):
                    face.vertex[i] = float(sstr.pop(0))
                    face.normal = float(sstr.pop(0))
                face.material = current_material
                self.faces.append(face)
            elif cmd == "usemtl":
                matname = sstr.pop(0)
                for i in range(len(self.materials)):
                    if matname == self.materials[i].name:
                        break
                current_material = 0  # i
        print("Obj loaded")
    
    def load_materials(self):
        print("Loading materials: {}".format(self.matfile))
        if not self.matfile:
            return
        with open(self.matfile, "r") as f:
           inputstring = f.read().split('\n')
           #print(inputstring)
        nmat = Material()
        for line in inputstring:
            sstr = line.split()
            if not sstr:
                continue
            cmd = sstr.pop(0)
            if not sstr:
                continue
            if cmd == "newmtl":
                nmat.name = sstr.pop(0)
            elif cmd == "Ns":
                nmat.shininess = float(sstr.pop(0))
            elif cmd == "Ka":
                for i in range(3):
                    nmat.ambient[i] = float(sstr.pop(0))
            elif cmd == "Kd":
                for i in range(3):
                    nmat.diffuse[i] = float(sstr.pop(0))
            elif cmd =="Ks":
                for i in range(3):
                    nmat.specular[i] = float(sstr.pop(0))
            elif cmd == "d":
                alpha = float(sstr.pop(0))
                nmat.ambient[3] = alpha
                nmat.diffuse[3] = alpha
                nmat.specular[3] = alpha
            elif cmd == "illum":
                self.materials.append(nmat)
        print("Materials loaded")
    
    def display(self):
        emiss = np.zeros(4, dtype = np.float32)
        gl.glBegin(gl.GL_TRIANGLES)

        current_material = -1
        for face in self.faces:
            mat = face.material
            if current_material != mat:
                m = self.materials[mat]
                gl.glEnd()
                
                gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, m.diffuse)
                gl.glMaterialfv(gl.GL_FRONT, gl.GL_DIFFUSE, m.diffuse)
                gl.glMaterialfv(gl.GL_FRONT, gl.GL_SPECULAR, m.specular)
                gl.glMaterialfv(gl.GL_FRONT, gl.GL_EMISSION, emiss)
                gl.glMaterialfv(gl.GL_FRONT, gl.GL_SHININESS, m.shininess)
                
                current_material = mat
                gl.glBegin(gl.GL_TRIANGLES)
                
            n_normal = int(face.normal - 1)
            
            gl.glNormal3fv(self.normals[n_normal].x)
            
            for j in range(3):
                n_vtx = int(face.vertex[j] - 1)
                gl.glVertex3fv(self.vertex[n_vtx].x)
            
        gl.glEnd()
        

if __name__ == '__main__':
    m = Model()
    m.load("base.obj")
    m.display()
    #print(m.materials)
    print(m.vertex)
    #print(m.normals)
    #print(m.faces)
