from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from sys import argv, exit
if __name__=='__main__':
    QApplication.setStyle('fusion')
    app = QApplication(argv)
    run = MainWindow()
    run.show()
    exit(app.exec_())
