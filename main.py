import sys
# import PyQt5
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel, QWidgets
from Trucks import Ui_Truckscreen
from Fullscreen import Ui_Fullscreen
from Splitscreen import Ui_Splitscreen
from Multiscreen import Ui_Multiscreen
# from PyQt5.QtCore import QTimer,QDateTime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime, Qt
from data import *
from datetime import datetime
import subprocess
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
        self.start = ""
        self.stop = ""
        self.current_mode = 3
        self.hasChangedDisplayMode = True



        # build ui
        self.getOption()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.start(1200)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.move(0,0)
        self.timer.timeout.connect(self.updateMode)
        self.timer.timeout.connect(self.getOption)
        self.timer.timeout.connect(self.screenBlanking)



    def getOption(self):
        if self.current_mode is not self.mode:
            self.hasChangedDisplayMode = True
            self.current_mode = self.mode
        if self.mode == 3 and self.hasChangedDisplayMode == True:
            self.ui = Ui_Truckscreen()
        elif self.mode == 2 and self.hasChangedDisplayMode == True:
            self.ui = Ui_Fullscreen()
        elif self.mode == 1 and self.hasChangedDisplayMode == True:
            self.ui = Ui_Splitscreen()
        if self.hasChangedDisplayMode:
            self.ui.setupUi(self)
            self.hasChangedDisplayMode = False
    def updateMode(self):
        self.mode = int(req("get", ip_mode).json()[0]['activeMode'])
        self.start = req("get", ip_sb).json()[0]['start'].split(":")
        self.stop = req("get", ip_sb).json()[0]['stop'].split(":")

    def screenBlanking(self):
        now = datetime.now()
        self.current_hour = now.strftime("%H")
        self.current_minute = now.strftime("%M")
        print("Il est ", self.current_hour, ":", self.current_minute)
        print("La veille est prévue entre ", self.start[0], ":", self.start[1], " et ", self.stop[0], ":", self.stop[1])
        if self.start[0] <= self.stop[0]:
            if self.start[0] < self.current_hour:
                print("start est inferieur a stop")
                if self.stop[0] > self.current_hour:
                    print("### L'ECRAN EST ETEINT ###")
                    print("### HEURE ###")
                    self.display("off")

                elif self.stop[0] == self.current_hour and self.stop[1] >= self.current_minute:
                    print("### L'ECRAN EST ETEINT ###")
                    print("### MINUTE ###")
                    self.display("off")

                else:
                    print("### L'ECRAN EST ALLUME ###")
                    self.display("on")


            elif self.start[0] == self.current_hour and self.start[1] <= self.current_minute:
                if self.stop[0] > self.current_hour:
                    print("### L'ECRAN EST ETEINT ###")
                    print("### HEURE ###")
                    self.display("off")

                elif self.stop[0] == self.current_hour and self.stop[1] >= self.current_minute:
                    print("### L'ECRAN EST ETEINT ###")
                    print("### MINUTE ###")
                    self.display("off")
                else:
                    print("### L'ECRAN EST ALLUME ###")
                    self.display("on")


        elif self.start[0] > self.stop[0]:
            print("start est superieur ou egal a stop")
            pass

    def display(self, state):
        # print("PROCESS", state)
        subprocess.Popen(["xset", "-d", ":0", "dpms", "force", state], stdout=subprocess.PIPE)



if __name__ == '__main__':
    mode = 3
    app = QtWidgets.QApplication(sys.argv)
    main = Main(mode)
    main.show()
    sys.exit(app.exec_())


