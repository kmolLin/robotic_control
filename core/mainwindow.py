# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from .Ui_mainwindow import Ui_MainWindow
# from core.vrep_commucation.vrepper import vrepper
import core.vrep_commucation.vrep as vrep
import os
from core.kinematic.Invers_kinematic.invers_kinematic import armrobot
from .worker import Worker
import time
from core.motionPlanning.trapezoid import graph_chart

import numpy as np
from math import radians
import matplotlib.pyplot as plt


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
            spinbox.setEnabled(True)
            self.jointtable.setCellWidget(row, 1, spinbox)
        for row in range(0, 6):
            spinbox = QDoubleSpinBox()
            spinbox.setMaximum(10000)
            spinbox.setMinimum(-10000)
            spinbox.setEnabled(True)
            self.tcptable.setCellWidget(row, 1, spinbox)

        self.arm = armrobot()
        self.jpos = np.zeros(6)

    def dowork(self, clientID, handles):
        self.work = Worker(clientID, handles, self)
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

        print('Program started')
        vrep.simxFinish(-1)
        while True:
            self.clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
            if self.clientID > -1:
                break
            else:
                time.sleep(0.2)
                print("Failed connecting to remote API server!")
        print("Connection success!")
        vrep.simxSetFloatingParameter(self.clientID, vrep.sim_floatparam_simulation_time_step, 0.005,
                                      vrep.simx_opmode_blocking)

        vrep.simxSynchronous(self.clientID, True)
        vrep.simxStartSimulation(self.clientID, vrep.simx_opmode_blocking)
        self.handles = []
        for name in (
                'A_joint',
                'B_joint',
                'C_joint',
                'D_joint',
                'E_joint',
                'F_joint',
        ):
            _, handle = vrep.simxGetObjectHandle(self.clientID, name, vrep.simx_opmode_blocking)
            self.handles.append(handle)
        print(self.handles)

        for i in range(6):
            _, self.jpos[i] = vrep.simxGetJointPosition(self.clientID, self.handles[i], vrep.simx_opmode_streaming)
        lastCmdTime = vrep.simxGetLastCmdTime(self.clientID)
        vrep.simxSynchronousTrigger(self.clientID)
        self.dowork(self.clientID, self.handles)

    @pyqtSlot()
    def on_joint_ctr_btn_clicked(self):
        inputjoint = [self.jointtable.cellWidget(i, 1).value() for i in range(6)]
        nowact = [float(self.jointtable.item(i, 0).text()) for i in range(6)]
        result = list(map(lambda x: abs(x[0] - x[1]), zip(inputjoint, nowact)))
        print(result)
        indexx = result.index(max(result))
        text = f"G00 X{round(nowact[indexx], 3)} Y10 F6000\n" + \
               f"G01 X{round(inputjoint[indexx], 3)} Y20\n"
        # text = f"G01 X{inputjoint[indexx]} Y10 F6000\n"
        print(text)

        i = 0.0
        ts = None
        sgo = []
        vgo = []
        ago = []
        jgo = []
        for tp in graph_chart(text):
            for s, v, a, j in tp.iter(
                    tp.s,
                    tp.v,
                    tp.a,
                    tp.j
            ):
                sgo.append((i, s))
                vgo.append((i, v))
                ago.append((i, a))
                jgo.append((i, j))
                i += tp.t_s
                if ts is None:
                    ts = tp.t_s
        alljoint = []
        for i in range(6):
            alljoint.append([float(result[i]) / max(result) * float(s[1]) for s in sgo])

        for g in range(len(alljoint[0])):
            vrep.simxPauseCommunication(self.clientID, True)
            for i in range(6):
                vrep.simxSetJointTargetPosition(self.clientID, self.handles[i], radians(alljoint[i][g]),
                                                vrep.simx_opmode_oneshot)
            vrep.simxPauseCommunication(self.clientID, False)
            vrep.simxSynchronousTrigger(self.clientID)
            vrep.simxGetPingTime(self.clientID)

        # for i in range(6):
        #     plt.plot([s[0] for s in sgo], alljoint[i])
        # plt.show()

    @pyqtSlot()
    def on_move_btn_clicked(self):
        TCP = [self.tcptable.cellWidget(i, 1).value() for i in range(3)]
        TOV = [self.tcptable.cellWidget(i, 1).value() for i in range(3, 6)]
        nowact = [float(self.jointtable.item(i, 0).text()) for i in range(6)]
        Joint_Deg = self.arm.Inverse_Kinematic(TCP, TOV, nowact)
        
        for i, handle in enumerate(self.work.handles):
            handle.set_position_target(Joint_Deg[i])

