# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""


from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_mainwindow import Ui_MainWindow
from openglw import GLWidget
from core.vrep_commucation.vrepper import vrepper
import os
from core.kinematic.Invers_kinematic.invers_kinematic import armrobot
from worker import Worker
import time


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.dt = 0.0
        self.view1 = GLWidget()
        
        self.verticalLayout.addWidget(self.view1)
        
        self.arm = armrobot()
        #venv.start()
        

    
    
    @pyqtSlot()
    def on_radioButtonSimple_clicked(self):
        print('a')
    
    @pyqtSlot()
    def on_radioButtonTarget_clicked(self):
        a = []
        
        self.venv = vrepper(headless=True)
        self.venv.start()
        # load scene
        self.venv.load_scene(os.getcwd() + '/ra605robot.ttt')
        
        self.Ajoint = self.venv.get_object_by_name('A_joint')
        self.Bjoint = self.venv.get_object_by_name('B_joint')
        self.Cjoint = self.venv.get_object_by_name('C_joint')
        self.Djoint = self.venv.get_object_by_name('D_joint')
        self.Ejoint = self.venv.get_object_by_name('E_joint')
        self.Fjoint = self.venv.get_object_by_name('F_joint')
        
        self.work = Worker(self.venv, self)
        self.work.start()
        
        
        print(self.Ajoint.handle, self.Bjoint.handle, self.Cjoint.handle, self.Djoint.handle, self.Ejoint.handle, self.Fjoint.handle)
        
        self.venv.start_blocking_simulation()
        for i in range(20):
            print('simulation step',i)
            print('body position',self.Ajoint.get_joint_angle())
            #a.append([self.Ajoint.get_joint_angle(), self.Bjoint.get_joint_angle(), self.Cjoint.get_joint_angle(), self.Djoint.get_joint_angle(), self.Ejoint.get_joint_angle(), self.Fjoint.get_joint_angle()])

            self.Ajoint.set_position_target(i*20)
            # you should see things moving back and forth

            self.venv.step_blocking_simulation() # forward 1 timestep
            time.sleep(2)
        # stop the simulation and reset the scene:
        self.venv.stop_blocking_simulation()
        print(a)
    
    @pyqtSlot()
    def on_commandLinkButtonGo_clicked(self):
        TCP = [self.lineEditTx.value(), self.lineEditTy.value(), self.lineEditTz.value()]
        TOV = [-90.0, 0.0, 90.0]
        self.arm.Inverse_Kinematic(TCP, TOV)
