from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Worker(QThread):
    def __init__(self,vrepper, parent ):
        super(Worker, self).__init__(parent)
        self.stoped = False
        self.venn = vrepper
        self.Ajoint = self.venn.get_object_by_name('A_joint')
        self.Bjoint = self.venn.get_object_by_name('B_joint')
        self.Cjoint = self.venn.get_object_by_name('C_joint')
        self.Djoint = self.venn.get_object_by_name('D_joint')
        self.Ejoint = self.venn.get_object_by_name('E_joint')
        self.Fjoint = self.venn.get_object_by_name('F_joint')
        
    update_axis1_signal = pyqtSignal(float)
    update_axis2_signal = pyqtSignal(float)
    update_axis3_signal = pyqtSignal(float)
    update_axis4_signal = pyqtSignal(float)
    update_axis5_signal = pyqtSignal(float)
    update_axis6_signal = pyqtSignal(float)
    
    def run(self):
        #do ing get data
        while(1):
            self.update_axis1_signal.emit(self.Ajoint.get_joint_angle())
            self.update_axis2_signal.emit(self.Bjoint.get_joint_angle())
            self.update_axis3_signal.emit(self.Cjoint.get_joint_angle())
            self.update_axis4_signal.emit(self.Djoint.get_joint_angle())
            self.update_axis5_signal.emit(self.Ejoint.get_joint_angle())
            self.update_axis6_signal.emit(self.Fjoint.get_joint_angle())

        
    def stop(self):
        self.stoped = True
        
    
