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
        
    update_axis1_signal = pyqtSignal(str)
    update_axis2_signal = pyqtSignal(str)
    update_axis3_signal = pyqtSignal(str)
    update_axis4_signal = pyqtSignal(str)
    update_axis5_signal = pyqtSignal(str)
    update_axis6_signal = pyqtSignal(str)
    
    def run(self):
        #do ing get data
        self.update_axis1_signal.emit(str(self.Ajoint.get_joint_angle()))
        self.update_axis2_signal.emit(str(self.Bjoint.get_joint_angle()))
        self.update_axis3_signal.emit(str(self.Cjoint.get_joint_angle()))
        self.update_axis4_signal.emit(str(self.Djoint.get_joint_angle()))
        self.update_axis5_signal.emit(str(self.Ejoint.get_joint_angle()))
        self.update_axis6_signal.emit(str(self.Fjoint.get_joint_angle()))

        
    def stop(self):
        self.stoped = True
        
    
