# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 676)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.offsettable = QtWidgets.QTableWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offsettable.sizePolicy().hasHeightForWidth())
        self.offsettable.setSizePolicy(sizePolicy)
        self.offsettable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.offsettable.setObjectName("offsettable")
        self.offsettable.setColumnCount(2)
        self.offsettable.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.offsettable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.offsettable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.offsettable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.offsettable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.offsettable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.offsettable.setHorizontalHeaderItem(1, item)
        self.verticalLayout_9.addWidget(self.offsettable)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.setoffset_btn = QtWidgets.QPushButton(self.centralWidget)
        self.setoffset_btn.setEnabled(False)
        self.setoffset_btn.setObjectName("setoffset_btn")
        self.horizontalLayout_21.addWidget(self.setoffset_btn)
        self.loadfile = QtWidgets.QPushButton(self.centralWidget)
        self.loadfile.setEnabled(False)
        self.loadfile.setObjectName("loadfile")
        self.horizontalLayout_21.addWidget(self.loadfile)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setSpacing(6)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.axiscombox = QtWidgets.QComboBox(self.centralWidget)
        self.axiscombox.setEnabled(False)
        self.axiscombox.setObjectName("axiscombox")
        self.axiscombox.addItem("")
        self.axiscombox.addItem("")
        self.axiscombox.addItem("")
        self.axiscombox.addItem("")
        self.axiscombox.addItem("")
        self.axiscombox.addItem("")
        self.horizontalLayout_22.addWidget(self.axiscombox)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.jog_p_btn = QtWidgets.QPushButton(self.centralWidget)
        self.jog_p_btn.setEnabled(False)
        self.jog_p_btn.setObjectName("jog_p_btn")
        self.horizontalLayout_23.addWidget(self.jog_p_btn)
        self.jog_n_btn = QtWidgets.QPushButton(self.centralWidget)
        self.jog_n_btn.setEnabled(False)
        self.jog_n_btn.setObjectName("jog_n_btn")
        self.horizontalLayout_23.addWidget(self.jog_n_btn)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_23)
        self.verticalLayout_5.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_15.addLayout(self.verticalLayout_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.jointtable = QtWidgets.QTableWidget(self.groupBox_2)
        self.jointtable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.jointtable.setObjectName("jointtable")
        self.jointtable.setColumnCount(2)
        self.jointtable.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.jointtable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.jointtable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.jointtable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.jointtable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.jointtable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.jointtable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.jointtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.jointtable.setHorizontalHeaderItem(1, item)
        self.verticalLayout_11.addWidget(self.jointtable)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setSpacing(6)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_24.addWidget(self.label_25)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalLayout_24.addWidget(self.horizontalSlider_3)
        self.doubleSpinBox_33 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_33.setObjectName("doubleSpinBox_33")
        self.horizontalLayout_24.addWidget(self.doubleSpinBox_33)
        self.verticalLayout_11.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_15.addWidget(self.groupBox_2)
        self.gridGroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.gridGroupBox)
        self.verticalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.tcptable = QtWidgets.QTableWidget(self.gridGroupBox)
        self.tcptable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tcptable.setObjectName("tcptable")
        self.tcptable.setColumnCount(2)
        self.tcptable.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tcptable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcptable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcptable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcptable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcptable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcptable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcptable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcptable.setHorizontalHeaderItem(1, item)
        self.verticalLayout_12.addWidget(self.tcptable)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.radioButton = QtWidgets.QRadioButton(self.gridGroupBox)
        self.radioButton.setEnabled(False)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_25.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridGroupBox)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_25.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridGroupBox)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_25.addWidget(self.radioButton_3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_15.addWidget(self.gridGroupBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setSpacing(6)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.start_btn = QtWidgets.QPushButton(self.centralWidget)
        self.start_btn.setEnabled(False)
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout_4.addWidget(self.start_btn)
        self.stop_btn = QtWidgets.QPushButton(self.centralWidget)
        self.stop_btn.setEnabled(False)
        self.stop_btn.setObjectName("stop_btn")
        self.verticalLayout_4.addWidget(self.stop_btn)
        self.servo_on_btn = QtWidgets.QPushButton(self.centralWidget)
        self.servo_on_btn.setObjectName("servo_on_btn")
        self.verticalLayout_4.addWidget(self.servo_on_btn)
        self.servo_off_btn = QtWidgets.QPushButton(self.centralWidget)
        self.servo_off_btn.setEnabled(False)
        self.servo_off_btn.setObjectName("servo_off_btn")
        self.verticalLayout_4.addWidget(self.servo_off_btn)
        self.exit_btn = QtWidgets.QPushButton(self.centralWidget)
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout_4.addWidget(self.exit_btn)
        self.horizontalLayout_26.addLayout(self.verticalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ed_editor = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_editor.setObjectName("ed_editor")
        self.verticalLayout_7.addWidget(self.ed_editor)
        self.list_nc = QtWidgets.QListWidget(self.centralWidget)
        self.list_nc.setObjectName("list_nc")
        self.verticalLayout_7.addWidget(self.list_nc)
        self.horizontalLayout_26.addLayout(self.verticalLayout_7)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setSpacing(6)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_26 = QtWidgets.QLabel(self.groupBox_4)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_31.addWidget(self.label_26)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.groupBox_4)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalLayout_31.addWidget(self.horizontalSlider_4)
        self.doubleSpinBox_31 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_31.setObjectName("doubleSpinBox_31")
        self.horizontalLayout_31.addWidget(self.doubleSpinBox_31)
        self.verticalLayout.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setSpacing(6)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_32.addWidget(self.label_27)
        self.doubleSpinBox_32 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_32.setObjectName("doubleSpinBox_32")
        self.horizontalLayout_32.addWidget(self.doubleSpinBox_32)
        self.verticalLayout.addLayout(self.horizontalLayout_32)
        self.verticalLayout_13.addWidget(self.groupBox_4)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setSpacing(6)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.move_btn = QtWidgets.QPushButton(self.centralWidget)
        self.move_btn.setEnabled(True)
        self.move_btn.setObjectName("move_btn")
        self.horizontalLayout_33.addWidget(self.move_btn)
        self.joint_ctr_btn = QtWidgets.QPushButton(self.centralWidget)
        self.joint_ctr_btn.setEnabled(False)
        self.joint_ctr_btn.setObjectName("joint_ctr_btn")
        self.horizontalLayout_33.addWidget(self.joint_ctr_btn)
        self.verticalLayout_14.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setSpacing(6)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.p2p_ctr_btn = QtWidgets.QPushButton(self.centralWidget)
        self.p2p_ctr_btn.setEnabled(False)
        self.p2p_ctr_btn.setObjectName("p2p_ctr_btn")
        self.horizontalLayout_34.addWidget(self.p2p_ctr_btn)
        self.cp_ctr_btn = QtWidgets.QPushButton(self.centralWidget)
        self.cp_ctr_btn.setEnabled(False)
        self.cp_ctr_btn.setObjectName("cp_ctr_btn")
        self.horizontalLayout_34.addWidget(self.cp_ctr_btn)
        self.verticalLayout_14.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setSpacing(6)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.enter_btn = QtWidgets.QPushButton(self.centralWidget)
        self.enter_btn.setEnabled(False)
        self.enter_btn.setObjectName("enter_btn")
        self.horizontalLayout_35.addWidget(self.enter_btn)
        self.mode_btn = QtWidgets.QPushButton(self.centralWidget)
        self.mode_btn.setEnabled(False)
        self.mode_btn.setObjectName("mode_btn")
        self.horizontalLayout_35.addWidget(self.mode_btn)
        self.verticalLayout_14.addLayout(self.horizontalLayout_35)
        self.verticalLayout_13.addLayout(self.verticalLayout_14)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setSpacing(6)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setSpacing(6)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.readtxt_btn = QtWidgets.QPushButton(self.centralWidget)
        self.readtxt_btn.setEnabled(True)
        self.readtxt_btn.setObjectName("readtxt_btn")
        self.horizontalLayout_37.addWidget(self.readtxt_btn)
        self.home_btn = QtWidgets.QPushButton(self.centralWidget)
        self.home_btn.setEnabled(True)
        self.home_btn.setObjectName("home_btn")
        self.horizontalLayout_37.addWidget(self.home_btn)
        self.horizontalLayout_36.addLayout(self.horizontalLayout_37)
        self.verticalLayout_13.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_26.addLayout(self.verticalLayout_13)
        self.verticalLayout_6.addLayout(self.horizontalLayout_26)
        self.verticalLayout_2.addLayout(self.verticalLayout_6)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(6)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_20.addWidget(self.label_6)
        self.enablegui = QtWidgets.QCheckBox(self.centralWidget)
        self.enablegui.setObjectName("enablegui")
        self.horizontalLayout_20.addWidget(self.enablegui)
        self.radioButtonSimple = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButtonSimple.setChecked(True)
        self.radioButtonSimple.setObjectName("radioButtonSimple")
        self.horizontalLayout_20.addWidget(self.radioButtonSimple)
        self.radioButtonTarget = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButtonTarget.setObjectName("radioButtonTarget")
        self.horizontalLayout_20.addWidget(self.radioButtonTarget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 893, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "robotic arm"))
        self.groupBox.setTitle(_translate("MainWindow", "TCP Offset"))
        item = self.offsettable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.offsettable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        item = self.offsettable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Z"))
        item = self.offsettable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "T"))
        item = self.offsettable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Output"))
        item = self.offsettable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Input"))
        self.setoffset_btn.setText(_translate("MainWindow", "Set Offset"))
        self.loadfile.setText(_translate("MainWindow", "Load File"))
        self.axiscombox.setItemText(0, _translate("MainWindow", "Axis1"))
        self.axiscombox.setItemText(1, _translate("MainWindow", "Axis2"))
        self.axiscombox.setItemText(2, _translate("MainWindow", "Axis3"))
        self.axiscombox.setItemText(3, _translate("MainWindow", "Axis4"))
        self.axiscombox.setItemText(4, _translate("MainWindow", "Axis5"))
        self.axiscombox.setItemText(5, _translate("MainWindow", "Axis6"))
        self.jog_p_btn.setText(_translate("MainWindow", "+"))
        self.jog_n_btn.setText(_translate("MainWindow", "-"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Joint Position"))
        item = self.jointtable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Axis1"))
        item = self.jointtable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Axis2"))
        item = self.jointtable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Axis3"))
        item = self.jointtable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Axis4"))
        item = self.jointtable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Axis5"))
        item = self.jointtable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Axis6"))
        item = self.jointtable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Output"))
        item = self.jointtable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Input"))
        self.label_25.setText(_translate("MainWindow", "V:"))
        self.doubleSpinBox_33.setSuffix(_translate("MainWindow", "%"))
        self.gridGroupBox.setTitle(_translate("MainWindow", "TCP and TOV"))
        item = self.tcptable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.tcptable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        item = self.tcptable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Z"))
        item = self.tcptable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "A"))
        item = self.tcptable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "B"))
        item = self.tcptable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "C"))
        item = self.tcptable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Output"))
        item = self.tcptable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Input"))
        self.radioButton.setText(_translate("MainWindow", "Input"))
        self.radioButton_2.setText(_translate("MainWindow", "Forward"))
        self.radioButton_3.setText(_translate("MainWindow", "Down"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.servo_on_btn.setText(_translate("MainWindow", "Servo ON"))
        self.servo_off_btn.setText(_translate("MainWindow", "Servo OFF"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Gripper Control"))
        self.label_26.setText(_translate("MainWindow", "F:"))
        self.doubleSpinBox_31.setSuffix(_translate("MainWindow", "%"))
        self.label_27.setText(_translate("MainWindow", "Delay"))
        self.doubleSpinBox_32.setSuffix(_translate("MainWindow", "sec"))
        self.move_btn.setText(_translate("MainWindow", "Move"))
        self.joint_ctr_btn.setText(_translate("MainWindow", "Joint Control"))
        self.p2p_ctr_btn.setText(_translate("MainWindow", "P2P Control"))
        self.cp_ctr_btn.setText(_translate("MainWindow", "CP Control"))
        self.enter_btn.setText(_translate("MainWindow", "Enter"))
        self.mode_btn.setText(_translate("MainWindow", "Change Mode"))
        self.readtxt_btn.setText(_translate("MainWindow", "Read TXT"))
        self.home_btn.setText(_translate("MainWindow", "Home"))
        self.label_6.setText(_translate("MainWindow", "Mode"))
        self.enablegui.setText(_translate("MainWindow", "Enable Gui"))
        self.radioButtonSimple.setText(_translate("MainWindow", "Simple steering"))
        self.radioButtonTarget.setText(_translate("MainWindow", "Target steering"))


