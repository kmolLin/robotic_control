# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\eric6_workspace\robotic_control\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_21.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(11, 11, 11, 11)
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
        self.verticalLayout_10.addLayout(self.horizontalLayout_20)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_21 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_18.addWidget(self.label_21)
        self.xoffset = QtWidgets.QLineEdit(self.centralWidget)
        self.xoffset.setEnabled(True)
        self.xoffset.setObjectName("xoffset")
        self.horizontalLayout_18.addWidget(self.xoffset)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_14 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.yoffset = QtWidgets.QLineEdit(self.centralWidget)
        self.yoffset.setObjectName("yoffset")
        self.horizontalLayout_16.addWidget(self.yoffset)
        self.verticalLayout_8.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_17.setSpacing(6)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.zoffset = QtWidgets.QLineEdit(self.centralWidget)
        self.zoffset.setObjectName("zoffset")
        self.horizontalLayout_17.addWidget(self.zoffset)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_19.setSpacing(6)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_22 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_19.addWidget(self.label_22)
        self.tooloffset = QtWidgets.QLineEdit(self.centralWidget)
        self.tooloffset.setObjectName("tooloffset")
        self.horizontalLayout_19.addWidget(self.tooloffset)
        self.verticalLayout_8.addLayout(self.horizontalLayout_19)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.axis1 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis1.setMaxLength(8)
        self.axis1.setObjectName("axis1")
        self.horizontalLayout.addWidget(self.axis1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.axis2 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis2.setMaxLength(8)
        self.axis2.setObjectName("axis2")
        self.horizontalLayout_2.addWidget(self.axis2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.axis3 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis3.setMaxLength(8)
        self.axis3.setObjectName("axis3")
        self.horizontalLayout_3.addWidget(self.axis3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_20 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_4.addWidget(self.label_20)
        self.axis4 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis4.setMaxLength(8)
        self.axis4.setObjectName("axis4")
        self.horizontalLayout_4.addWidget(self.axis4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_5.addWidget(self.label_18)
        self.axis5 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis5.setMaxLength(8)
        self.axis5.setObjectName("axis5")
        self.horizontalLayout_5.addWidget(self.axis5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_19 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_6.addWidget(self.label_19)
        self.axis6 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis6.setMaxLength(8)
        self.axis6.setObjectName("axis6")
        self.horizontalLayout_6.addWidget(self.axis6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(self.centralWidget)
        self.horizontalSlider.setProperty("value", 10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_7.addWidget(self.horizontalSlider)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.commandLinkButtonGo = QtWidgets.QCommandLinkButton(self.centralWidget)
        self.commandLinkButtonGo.setEnabled(True)
        self.commandLinkButtonGo.setObjectName("commandLinkButtonGo")
        self.horizontalLayout_7.addWidget(self.commandLinkButtonGo)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEditTx = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditTx.setEnabled(True)
        self.lineEditTx.setObjectName("lineEditTx")
        self.horizontalLayout_8.addWidget(self.lineEditTx)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lineEditTy = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditTy.setObjectName("lineEditTy")
        self.horizontalLayout_9.addWidget(self.lineEditTy)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.lineEditTz = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditTz.setObjectName("lineEditTz")
        self.horizontalLayout_10.addWidget(self.lineEditTz)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.lineEditA = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditA.setObjectName("lineEditA")
        self.horizontalLayout_11.addWidget(self.lineEditA)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.lineEditB = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditB.setObjectName("lineEditB")
        self.horizontalLayout_12.addWidget(self.lineEditB)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.lineEditC = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditC.setObjectName("lineEditC")
        self.horizontalLayout_13.addWidget(self.lineEditC)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.verticalLayout_10.addLayout(self.verticalLayout_3)
        self.horizontalLayout_14.addLayout(self.verticalLayout_10)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_14)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalSliderPitch = QtWidgets.QSlider(self.centralWidget)
        self.verticalSliderPitch.setMinimum(-90)
        self.verticalSliderPitch.setMaximum(90)
        self.verticalSliderPitch.setProperty("value", 30)
        self.verticalSliderPitch.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderPitch.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSliderPitch.setTickInterval(10)
        self.verticalSliderPitch.setObjectName("verticalSliderPitch")
        self.horizontalLayout_15.addWidget(self.verticalSliderPitch)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_15.addLayout(self.verticalLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.horizontalSliderYaw = QtWidgets.QSlider(self.centralWidget)
        self.horizontalSliderYaw.setMinimum(-180)
        self.horizontalSliderYaw.setMaximum(180)
        self.horizontalSliderYaw.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderYaw.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSliderYaw.setTickInterval(10)
        self.horizontalSliderYaw.setObjectName("horizontalSliderYaw")
        self.verticalLayout_6.addWidget(self.horizontalSliderYaw)
        self.horizontalLayout_21.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
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
        self.label_6.setText(_translate("MainWindow", "Mode"))
        self.enablegui.setText(_translate("MainWindow", "Enable Gui"))
        self.radioButtonSimple.setText(_translate("MainWindow", "Simple steering"))
        self.radioButtonTarget.setText(_translate("MainWindow", "Target steering"))
        self.label_3.setText(_translate("MainWindow", "TCP Offset"))
        self.label_21.setText(_translate("MainWindow", "X"))
        self.xoffset.setText(_translate("MainWindow", "0.0"))
        self.label_14.setText(_translate("MainWindow", "Y"))
        self.yoffset.setText(_translate("MainWindow", "0.0"))
        self.label_15.setText(_translate("MainWindow", "Z"))
        self.zoffset.setText(_translate("MainWindow", "0.0"))
        self.label_22.setText(_translate("MainWindow", "T"))
        self.tooloffset.setText(_translate("MainWindow", "0.0"))
        self.label_4.setText(_translate("MainWindow", "Joint Position"))
        self.label_10.setText(_translate("MainWindow", "Axis1"))
        self.label_16.setText(_translate("MainWindow", "Axis2"))
        self.label_17.setText(_translate("MainWindow", "Axis3"))
        self.label_20.setText(_translate("MainWindow", "Axis4"))
        self.label_18.setText(_translate("MainWindow", "Axis5"))
        self.label_19.setText(_translate("MainWindow", "Axis6"))
        self.label.setText(_translate("MainWindow", "V :"))
        self.label_2.setText(_translate("MainWindow", "%"))
        self.commandLinkButtonGo.setText(_translate("MainWindow", "GO"))
        self.label_5.setText(_translate("MainWindow", "TCP and TOV"))
        self.label_8.setText(_translate("MainWindow", "X"))
        self.lineEditTx.setText(_translate("MainWindow", "1.0"))
        self.label_9.setText(_translate("MainWindow", "Y"))
        self.lineEditTy.setText(_translate("MainWindow", "1.0"))
        self.label_7.setText(_translate("MainWindow", "Z"))
        self.lineEditTz.setText(_translate("MainWindow", "0.0"))
        self.label_11.setText(_translate("MainWindow", "A"))
        self.lineEditA.setText(_translate("MainWindow", "0.0"))
        self.label_12.setText(_translate("MainWindow", "B"))
        self.lineEditB.setText(_translate("MainWindow", "0.0"))
        self.label_13.setText(_translate("MainWindow", "C"))
        self.lineEditC.setText(_translate("MainWindow", "0.0"))
        self.verticalSliderPitch.setToolTip(_translate("MainWindow", "Pitch"))
        self.horizontalSliderYaw.setToolTip(_translate("MainWindow", "Yaw"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

