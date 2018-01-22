# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_mainwindow import Ui_MainWindow
from openglw import GLWidget

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
        

    
    
    @pyqtSlot()
    def on_radioButtonSimple_clicked(self):
        print('a')
