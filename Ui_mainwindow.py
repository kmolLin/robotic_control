# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\kmol\robotic_control\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 609)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalSliderYaw = QtWidgets.QSlider(self.centralWidget)
        self.horizontalSliderYaw.setGeometry(QtCore.QRect(340, 530, 641, 21))
        self.horizontalSliderYaw.setMinimum(-180)
        self.horizontalSliderYaw.setMaximum(180)
        self.horizontalSliderYaw.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderYaw.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSliderYaw.setTickInterval(10)
        self.horizontalSliderYaw.setObjectName("horizontalSliderYaw")
        self.verticalSliderPitch = QtWidgets.QSlider(self.centralWidget)
        self.verticalSliderPitch.setGeometry(QtCore.QRect(300, 30, 21, 481))
        self.verticalSliderPitch.setMinimum(-90)
        self.verticalSliderPitch.setMaximum(90)
        self.verticalSliderPitch.setProperty("value", 30)
        self.verticalSliderPitch.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderPitch.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSliderPitch.setTickInterval(10)
        self.verticalSliderPitch.setObjectName("verticalSliderPitch")
        self.groupBoxTarget = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBoxTarget.setEnabled(True)
        self.groupBoxTarget.setGeometry(QtCore.QRect(20, 130, 251, 201))
        self.groupBoxTarget.setObjectName("groupBoxTarget")
        self.lineEditTx = QtWidgets.QLineEdit(self.groupBoxTarget)
        self.lineEditTx.setEnabled(True)
        self.lineEditTx.setGeometry(QtCore.QRect(50, 20, 113, 20))
        self.lineEditTx.setObjectName("lineEditTx")
        self.lineEditTy = QtWidgets.QLineEdit(self.groupBoxTarget)
        self.lineEditTy.setGeometry(QtCore.QRect(50, 50, 113, 20))
        self.lineEditTy.setObjectName("lineEditTy")
        self.commandLinkButtonGo = QtWidgets.QCommandLinkButton(self.groupBoxTarget)
        self.commandLinkButtonGo.setEnabled(True)
        self.commandLinkButtonGo.setGeometry(QtCore.QRect(180, 80, 61, 41))
        self.commandLinkButtonGo.setObjectName("commandLinkButtonGo")
        self.label_9 = QtWidgets.QLabel(self.groupBoxTarget)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 16, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.groupBoxTarget)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 16, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBoxTarget)
        self.label_8.setGeometry(QtCore.QRect(20, 25, 16, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEditTz = QtWidgets.QLineEdit(self.groupBoxTarget)
        self.lineEditTz.setGeometry(QtCore.QRect(50, 80, 113, 20))
        self.lineEditTz.setObjectName("lineEditTz")
        self.label_11 = QtWidgets.QLabel(self.groupBoxTarget)
        self.label_11.setGeometry(QtCore.QRect(20, 110, 16, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEditA = QtWidgets.QLineEdit(self.groupBoxTarget)
        self.lineEditA.setGeometry(QtCore.QRect(50, 110, 113, 20))
        self.lineEditA.setObjectName("lineEditA")
        self.label_12 = QtWidgets.QLabel(self.groupBoxTarget)
        self.label_12.setGeometry(QtCore.QRect(20, 140, 16, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBoxTarget)
        self.label_13.setGeometry(QtCore.QRect(20, 170, 16, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEditB = QtWidgets.QLineEdit(self.groupBoxTarget)
        self.lineEditB.setGeometry(QtCore.QRect(50, 140, 113, 20))
        self.lineEditB.setObjectName("lineEditB")
        self.lineEditC = QtWidgets.QLineEdit(self.groupBoxTarget)
        self.lineEditC.setGeometry(QtCore.QRect(50, 170, 113, 20))
        self.lineEditC.setObjectName("lineEditC")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 30, 251, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButtonSimple = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonSimple.setGeometry(QtCore.QRect(20, 20, 101, 17))
        self.radioButtonSimple.setChecked(True)
        self.radioButtonSimple.setObjectName("radioButtonSimple")
        self.radioButtonTarget = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonTarget.setGeometry(QtCore.QRect(20, 50, 101, 17))
        self.radioButtonTarget.setObjectName("radioButtonTarget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(330, 20, 661, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(40, 340, 42, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.axis1 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis1.setGeometry(QtCore.QRect(88, 340, 129, 20))
        self.axis1.setObjectName("axis1")
        self.axis2 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis2.setGeometry(QtCore.QRect(88, 368, 129, 20))
        self.axis2.setObjectName("axis2")
        self.label_16 = QtWidgets.QLabel(self.centralWidget)
        self.label_16.setGeometry(QtCore.QRect(40, 368, 42, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.axis3 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis3.setGeometry(QtCore.QRect(88, 396, 129, 20))
        self.axis3.setObjectName("axis3")
        self.label_17 = QtWidgets.QLabel(self.centralWidget)
        self.label_17.setGeometry(QtCore.QRect(40, 396, 42, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_20 = QtWidgets.QLabel(self.centralWidget)
        self.label_20.setGeometry(QtCore.QRect(40, 424, 42, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.axis4 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis4.setGeometry(QtCore.QRect(88, 424, 129, 20))
        self.axis4.setObjectName("axis4")
        self.axis5 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis5.setGeometry(QtCore.QRect(88, 452, 129, 20))
        self.axis5.setObjectName("axis5")
        self.label_18 = QtWidgets.QLabel(self.centralWidget)
        self.label_18.setGeometry(QtCore.QRect(40, 452, 42, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralWidget)
        self.label_19.setGeometry(QtCore.QRect(40, 480, 42, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.axis6 = QtWidgets.QLineEdit(self.centralWidget)
        self.axis6.setGeometry(QtCore.QRect(88, 480, 129, 20))
        self.axis6.setObjectName("axis6")
        self.horizontalSlider = QtWidgets.QSlider(self.centralWidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(54, 508, 84, 22))
        self.horizontalSlider.setProperty("value", 10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(40, 508, 16, 16))
        self.label.setObjectName("label")
        self.axis1.raise_()
        self.axis2.raise_()
        self.label_16.raise_()
        self.axis3.raise_()
        self.label_17.raise_()
        self.label_20.raise_()
        self.axis4.raise_()
        self.axis5.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.axis6.raise_()
        self.horizontalSlider.raise_()
        self.label.raise_()
        self.horizontalSliderYaw.raise_()
        self.verticalSliderPitch.raise_()
        self.groupBoxTarget.raise_()
        self.groupBox_3.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_10.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1049, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScarySim"))
        self.horizontalSliderYaw.setToolTip(_translate("MainWindow", "Yaw"))
        self.verticalSliderPitch.setToolTip(_translate("MainWindow", "Pitch"))
        self.groupBoxTarget.setTitle(_translate("MainWindow", "Target"))
        self.lineEditTx.setText(_translate("MainWindow", "1.0"))
        self.lineEditTy.setText(_translate("MainWindow", "1.0"))
        self.commandLinkButtonGo.setText(_translate("MainWindow", "GO"))
        self.label_9.setText(_translate("MainWindow", "Y"))
        self.label_7.setText(_translate("MainWindow", "Z"))
        self.label_8.setText(_translate("MainWindow", "X"))
        self.lineEditTz.setText(_translate("MainWindow", "0.0"))
        self.label_11.setText(_translate("MainWindow", "A"))
        self.lineEditA.setText(_translate("MainWindow", "0.0"))
        self.label_12.setText(_translate("MainWindow", "B"))
        self.label_13.setText(_translate("MainWindow", "C"))
        self.lineEditB.setText(_translate("MainWindow", "0.0"))
        self.lineEditC.setText(_translate("MainWindow", "0.0"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Mode"))
        self.radioButtonSimple.setText(_translate("MainWindow", "Simple steering"))
        self.radioButtonTarget.setText(_translate("MainWindow", "Target steering"))
        self.label_10.setText(_translate("MainWindow", "Axis1"))
        self.label_16.setText(_translate("MainWindow", "Axis2"))
        self.label_17.setText(_translate("MainWindow", "Axis3"))
        self.label_20.setText(_translate("MainWindow", "Axis4"))
        self.label_18.setText(_translate("MainWindow", "Axis5"))
        self.label_19.setText(_translate("MainWindow", "Axis6"))
        self.label.setText(_translate("MainWindow", "V"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

