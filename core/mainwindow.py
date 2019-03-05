# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from .Ui_mainwindow import Ui_MainWindow
import core.vrep_commucation.vrep as vrep
import os
from core.kinematic.Invers_kinematic.invers_kinematic import armrobot
from .worker import Worker
import time
from core.motionPlanning.trapezoid import Trapezoid, SShape
from core.motionPlanning.v_planning import s_shape_interplation

import numpy as np
from math import radians
import matplotlib.pyplot as plt
import cv2


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
        self.clientID = None
        self.camhandle = None
        self.handles = []
        self.jpos = np.zeros(6)
        self.joint_pos = [0] * 6

    def dowork(self, clientID, handles):
        self.work = Worker(clientID, handles, self)
        self.work.update_signal.connect(self.motor_angle)
        self.work.start()
    
    @pyqtSlot(list)
    def motor_angle(self, data):
        for i, value in enumerate(data):
            self.joint_pos[i] = value
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
        vrep.simxSynchronous(self.clientID, True)

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
        _, self.camhandle = vrep.simxGetObjectHandle(self.clientID, 'Vision_sensor', vrep.simx_opmode_blocking)
        print(self.handles)
        for i in range(6):
            _, self.jpos[i] = vrep.simxGetJointPosition(self.clientID, self.handles[i], vrep.simx_opmode_streaming)
        lastCmdTime = vrep.simxGetLastCmdTime(self.clientID)
        vrep.simxSynchronousTrigger(self.clientID)
        self.dowork(self.clientID, self.handles)

    @pyqtSlot()
    def on_joint_ctr_btn_clicked(self):
        inputjoint = [self.jointtable.cellWidget(i, 1).value() for i in range(6)]
        nowact = self.joint_pos
        length = list(map(lambda x: abs(x[0] - x[1]), zip(inputjoint, nowact)))
        lengthvec = list(map(lambda x: (x[0] - x[1]), zip(inputjoint, nowact)))
        indexx = length.index(max(length))
        s_tmp, _, _, _ = s_shape_interplation(nowact[indexx], 0, inputjoint[indexx], 0, 100)
        alljoint = []
        for i in range(6):
            alljoint.append([nowact[i] + (float(s) * lengthvec[i] / length[indexx]) for s in s_tmp])

        dlg = QProgressDialog("Process", "Cancel", 0, len(alljoint[0]), self)
        dlg.setWindowModality(Qt.WindowModal)
        dlg.show()

        for g in range(len(alljoint[0])):
            vrep.simxPauseCommunication(self.clientID, True)
            for i in range(6):
                vrep.simxSetJointTargetPosition(self.clientID, self.handles[i], radians(alljoint[i][g]),
                                                vrep.simx_opmode_streaming)
            vrep.simxPauseCommunication(self.clientID, False)
            QCoreApplication.processEvents()
            dlg.setValue(g)
            vrep.simxSynchronousTrigger(self.clientID)

        dlg.setValue(len(alljoint[0]))
        dlg.deleteLater()

    @pyqtSlot()
    def on_move_btn_clicked(self):
        TCP = [self.tcptable.cellWidget(i, 1).value() for i in range(3)]
        TOV = [self.tcptable.cellWidget(i, 1).value() for i in range(3, 6)]
        nowact = self.joint_pos
        Joint_Deg = self.arm.Inverse_Kinematic(TCP, TOV, nowact)
        
        # for i, handle in enumerate(self.work.handles):
        #     handle.set_position_target(Joint_Deg[i])

    @pyqtSlot()
    def on_capture_btn_clicked(self):
        print(self.camhandle)
        _, resolution, image = vrep.simxGetVisionSensorImage(self.clientID, self.camhandle, 0, vrep.simx_opmode_streaming)
        time.sleep(1)
        _, resolution, image = vrep.simxGetVisionSensorImage(self.clientID, self.camhandle, 0, vrep.simx_opmode_buffer)
        time.sleep(1)
        img = np.array(image, dtype=np.uint8)
        img.resize([resolution[0], resolution[1], 3])
        img = np.rot90(img, 2)
        img = np.fliplr(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        file = "gear4.png"
        cv2.imwrite(file, img)

    @pyqtSlot()
    def on_vaclum_btn_clicked(self):
        check, jj, _, _, _ = vrep.simxCallScriptFunction(self.clientID, "suctionPad", vrep.sim_scripttype_childscript,
                                            "enableSuctionCup", [1], [], [], bytearray(), vrep.simx_opmode_oneshot)
        print(jj)

    def closeEvent(self, event):
        if self.clientID is not None:
            vrep.simxStopSimulation(self.clientID, vrep.simx_opmode_oneshot)
        event.accept()

