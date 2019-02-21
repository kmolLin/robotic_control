# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from .Ui_mainwindow import Ui_MainWindow
from core.vrep_commucation.vrepper import vrepper
import os
from core.kinematic.Invers_kinematic.invers_kinematic import armrobot
from .worker import Worker
import time


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.dt = 0.0
        for row in range(0, 4):
            spinbox = QDoubleSpinBox()
            spinbox.setMaximum(10000)
            spinbox.setMinimum(-10000)
            spinbox.setEnabled(False)
            self.offsettable.setCellWidget(row, 1, spinbox)
        for row in range(0, 6):
            spinbox = QDoubleSpinBox()
            spinbox.setMaximum(10000)
            spinbox.setMinimum(-10000)
            spinbox.setEnabled(False)
            self.jointtable.setCellWidget(row, 1, spinbox)
        for row in range(0, 6):
            spinbox = QDoubleSpinBox()
            spinbox.setMaximum(10000)
            spinbox.setMinimum(-10000)
            spinbox.setEnabled(True)
            self.tcptable.setCellWidget(row, 1, spinbox)

        self.arm = armrobot()

    def dowork(self, venv):
        self.work = Worker(venv, self)
        self.work.update_signal.connect(self.motor_angle)
        self.work.start()
    
    @pyqtSlot(list)
    def motor_angle(self, data):
        for i, value in enumerate(data):
            self.jointtable.setItem(i, 0, QTableWidgetItem(f"{value:.04f}"))
    
    @pyqtSlot()
    def on_radioButtonSimple_clicked(self):
        print('a')
    
    @pyqtSlot()
    def on_radioButtonTarget_clicked(self):
        guimode = self.enablegui.isTristate()
        print(guimode)
        self.venv = vrepper(headless=False)
        self.venv.start()
        # load scene
        self.venv.load_scene(os.getcwd() + '/ra605robotV2.ttt')
        # self.venv.start_nonblocking_simulation()
        self.venv.start_blocking_simulation()
        for i in range(10):
            self.venv.step_blocking_simulation()
            self.handles = []
            for name in (
                    'A_joint',
                    'B_joint',
                    'C_joint',
                    'D_joint',
                    'E_joint',
                    'F_joint',
            ):
                self.handles.append(self.venv.get_object_by_name(name))
            self.motor_angle([handle.get_joint_angle() for handle in self.handles])


        # self.dowork(self.venv)

    @pyqtSlot()
    def on_move_btn_clicked(self):
        TCP = [self.tcptable.cellWidget(i, 1).value() for i in range(3)]
        TOV = [self.tcptable.cellWidget(i, 1).value() for i in range(3, 6)]
        nowact = [float(self.jointtable.item(i, 0).text()) for i in range(6)]
        Joint_Deg = self.arm.Inverse_Kinematic(TCP, TOV, nowact)
        
        for i, handle in enumerate(self.work.handles):
            handle.set_position_target(Joint_Deg[i])

