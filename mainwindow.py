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
        
    def dowork(self, venv):
        self.work = Worker(venv, self)
        self.work.update_axis1_signal.connect(self.update_text)
        self.work.update_axis2_signal.connect(self.update_text1)
        self.work.update_axis3_signal.connect(self.update_text2)
        self.work.update_axis4_signal.connect(self.update_text3)
        self.work.update_axis5_signal.connect(self.update_text4)
        self.work.update_axis6_signal.connect(self.update_text5)
        self.work.start()
    
    def update_text(self, text):
        self.axis1.setText(str(text))
    def update_text1(self, text1):   
        self.axis2.setText(str(text1))
    def update_text2(self, text2):  
        self.axis3.setText(str(text2))
    def update_text3(self, text3):  
        self.axis4.setText(str(text3))
    def update_text4(self, text4):  
        self.axis5.setText(str(text4))
    def update_text5(self, text5):  
        self.axis6.setText(str(text5))
    
    @pyqtSlot()
    def on_radioButtonSimple_clicked(self):
        print('a')
    
    @pyqtSlot()
    def on_radioButtonTarget_clicked(self):
        
        self.venv = vrepper(headless=False)
        self.venv.start()
        # load scene
        self.venv.load_scene(os.getcwd() + '/ra605robotV2.ttt')
        
        self.Ajoint = self.venv.get_object_by_name('A_joint')
        self.Bjoint = self.venv.get_object_by_name('B_joint')
        self.Cjoint = self.venv.get_object_by_name('C_joint')
        self.Djoint = self.venv.get_object_by_name('D_joint')
        self.Ejoint = self.venv.get_object_by_name('E_joint')
        self.Fjoint = self.venv.get_object_by_name('F_joint')
        
        #print(self.Ajoint.handle, self.Bjoint.handle, self.Cjoint.handle, self.Djoint.handle, self.Ejoint.handle, self.Fjoint.handle)
        self.venv.start_nonblocking_simulation()
        
        self.dowork(self.venv)
        #self.venv.start_blocking_simulation()
        #for i in range(20):
            #print('simulation step',i)
            #print('body position',self.Ajoint.get_joint_angle())
            #self.Ajoint.set_position_target(i*20)
            # you should see things moving back and forth

            #self.venv.step_blocking_simulation() # forward 1 timestep
        # stop the simulation and reset the scene:
        #self.venv.stop_blocking_simulation()
        #print(a)
    
    @pyqtSlot()
    def on_commandLinkButtonGo_clicked(self):
        TCP = [float(self.lineEditTx.text()), float(self.lineEditTy.text()), float(self.lineEditTz.text())]
        TOV = []
        ge = [self.lineEditA, self.lineEditB, self.lineEditC]
        for i in ge:
            TOV.append(float(i.text()))
        nowact = self.getactjoint()
        Joint_Deg = self.arm.Inverse_Kinematic(TCP, TOV, nowact)
        
        self.Ajoint.set_position_target(Joint_Deg[0])
        self.Bjoint.set_position_target(Joint_Deg[1])
        self.Cjoint.set_position_target(Joint_Deg[2])
        self.Djoint.set_position_target(Joint_Deg[3])
        self.Ejoint.set_position_target(Joint_Deg[4])
        self.Fjoint.set_position_target(Joint_Deg[5])


    def getactjoint(self):
        li = [self.axis1, self.axis2, self.axis3, self.axis4,self.axis5, self.axis6]
        catch = []
        for i in li:
            catch.append(float(i.text()))
        return catch
        
