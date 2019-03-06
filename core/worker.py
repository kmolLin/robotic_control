from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from core.vrep_commucation import vrep
from math import degrees


class Worker(QThread):
    def __init__(self, clinetID, handles, parent):
        super(Worker, self).__init__(parent)
        self.stoped = False
        self.handles = handles
        self.clientID = clinetID
    
    update_signal = pyqtSignal(list)
    
    def run(self):
        #do ing get data
        while 1:
            self.update_signal.emit([
                self.__get_joint_angle(handle)
                for handle in self.handles
            ])

    def __get_joint_angle(self, joint_handle):
        _, jpos = vrep.simxGetJointPosition(self.clientID, joint_handle, vrep.simx_opmode_buffer)
        return degrees(jpos)

    def stop(self):
        self.stoped = True

