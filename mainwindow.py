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
        
        venv = vrepper(headless=False)
        #venv.start()
        

    
    
    @pyqtSlot()
    def on_radioButtonSimple_clicked(self):
        print('a')
    
    @pyqtSlot()
    def on_radioButtonTarget_clicked(self):
        
        venv = vrepper.vrepper(headless=False)
        venv.start()
        # load scene
        venv.load_scene(os.getcwd() + '/scenes/body_joint_wheel.ttt')
    
    @pyqtSlot()
    def on_commandLinkButtonGo_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
