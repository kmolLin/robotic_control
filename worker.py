from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Worker(QThread):
    def __init__(self,vrepper, parent ):
        super(Worker, self).__init__(parent)
        self.stoped = False
        self.venn = vrepper
        self.handles = []
        for name in (
            'A_joint',
            'B_joint',
            'C_joint',
            'D_joint',
            'E_joint',
            'F_joint',
        ):
            self.handles.append(self.venn.get_object_by_name(name))
    
    update_signal = pyqtSignal(list)
    
    def run(self):
        #do ing get data
        while 1:
            self.update_signal.emit([
                handle.get_joint_angle()
                for handle in self.handles
            ])

        
    def stop(self):
        self.stoped = True
        
    
