import sys
# import PyQt5
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel, QWidgets
from Trucks import Ui_MainWindow
from Fullscreen import Ui_Fullscreen
from Splitscreen import Ui_Splitscreen
# from PyQt5.QtCore import QTimer,QDateTime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime, Qt
from data import *
#
# class WinForm(QWidget):
#     def __init__(self,parent=None):
#         super(WinForm, self).__init__(parent)
#         self.setWindowTitle('QTimer example')
#
#         self.listFile=QListWidget()
#         self.label=QLabel('Label')
#         self.startBtn=QPushButton('Start')
#         self.endBtn=QPushButton('Stop')
#
#         layout=QGridLayout()
#
#         self.timer=QTimer()
#         self.timer.start(1000)
#         self.timer.timeout.connect(self.showTime)
#
#         layout.addWidget(self.label,0,0,1,2)
#         layout.addWidget(self.startBtn,1,0)
#         layout.addWidget(self.endBtn,1,1)

    #     self.startBtn.clicked.connect(self.startTimer)
    #     self.endBtn.clicked.connect(self.endTimer)
    #
    #     self.setLayout(layout)
    #
    # def showTime(self):
    #     time=QDateTime.currentDateTime()
    #     timeDisplay=time.toString('yyyy-MM-dd hh:mm:ss dddd')
    #     self.label.setText(timeDisplay)
    #
    # def startTimer(self):
    #     self.timer.start(1000)
    #     self.startBtn.setEnabled(False)
    #     self.endBtn.setEnabled(True)
    #
    # def endTimer(self):
    #     self.timer.stop()
    #     self.startBtn.setEnabled(True)
    #     self.endBtn.setEnabled(False)

class Main(QtWidgets.QMainWindow):
    def __init__(self, mode):
        super(Main, self).__init__()
        self.mode = mode
        self.hasChangedDisplayMode = False

        # build ui
        self.getOption()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.start(1000)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.move(0,0)
        self.timer.timeout.connect(self.updateMode)
        self.timer.timeout.connect(self.getOption)



    def getOption(self):
        if self.mode == 1:
            self.ui = Ui_MainWindow()
            self.hasChangedDisplayMode = True
        elif self.mode == 2:
            self.ui = Ui_Fullscreen()
            self.hasChangedDisplayMode = True
        elif self.mode == 3:
            self.ui = Ui_Splitscreen()
            self.hasChangedDisplayMode = True
        if self.hasChangedDisplayMode:
            self.ui.setupUi(self)
            self.hasChangedDisplayMode = False
    def updateMode(self):
        self.mode = int(req("get", ip_mode).json()[0]['activeMode'])
        print(self.mode)



if __name__ == '__main__':
    mode = 1
    app = QtWidgets.QApplication(sys.argv)
    main = Main(mode)
    main.show()
    sys.exit(app.exec_())


