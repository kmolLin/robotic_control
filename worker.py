from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Worker(QThread):
    def __init__(self,vrepper, parent ):
        super(Worker, self).__init__(parent)
        self.stoped = False
        self.venn = vrepper
        self.parent = parent
        self.Ajoint = self.venn.get_object_by_name('A_joint')
        self.Bjoint = self.venn.get_object_by_name('B_joint')
        self.Cjoint = self.venn.get_object_by_name('C_joint')
        self.Djoint = self.venn.get_object_by_name('D_joint')
        self.Ejoint = self.venn.get_object_by_name('E_joint')
        self.Fjoint = self.venn.get_object_by_name('F_joint')
    
    def run(self):
        #do ing get data
        self.parent.axis1.insert(str(self.Ajoint.get_joint_angle()))
        self.parent.axis2.insert(str(self.Bjoint.get_joint_angle()))
        self.parent.axis3.insert(str(self.Cjoint.get_joint_angle()))
        self.parent.axis4.insert(str(self.Djoint.get_joint_angle()))
        self.parent.axis5.insert(str(self.Ejoint.get_joint_angle()))
        self.parent.axis6.insert(str(self.Fjoint.get_joint_angle()))
        
        
    def stop(self):
        self.stoped = True
        
    
