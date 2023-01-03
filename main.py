import sys
# import PyQt5
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel, QWidgets
from Trucks import Ui_Truckscreen
from Fullscreen import Ui_Fullscreen
from Splitscreen import Ui_Splitscreen
from Shutdown import Ui_Shutdown
# from PyQt5.QtCore import QTimer,QDateTime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime, Qt
from data import *
from datetime import datetime
import subprocess
import requests
import time
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
    stop = 1

    def __init__(self, mode):
        super(Main, self).__init__()
        self.mode = mode
        self.current_mode = 3
        self.hasChangedDisplayMode = True
        self.index = index
        self.start = ["", ""]
        self.stop = ["", ""]
        self.veille = True
        self.lastMedia = True
        # build ui

        self.getOption()
        # self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.start(1000)
        #self.timer.start(media . duration)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.move(0, 0)
        self.timer.timeout.connect(self.updateMode)
        self.timer.timeout.connect(self.getOption)
        self.timer.timeout.connect(self.screenBlanking)

    def getOption(self):
        #TODO : Implicitement, la selection d'un mode signifie également la séléction d'un format de média (video ou image)
            if self.current_mode is not self.mode:
                self.hasChangedDisplayMode = True
                self.current_mode = self.mode

            if self.mode == 3:
                self.timer.start(self.medias[self.index]['duration'] * 1000)
                if self.index > 4:
                    if len(self.medias) != 5:
                        self.ui = Ui_Fullscreen(self.index)
                        self.ui.setupUi(self)
                        self.lastMedia = True
                    if self.index >= len(self.medias) - 1:
                        self.index = 3
                elif self.index == 4 and self.lastMedia == True:
                    self.ui = Ui_Truckscreen()
                    self.ui.setupUi(self)
                    self.lastMedia = False
                self.index = self.index + 1

            elif self.mode == 2 and self.hasChangedDisplayMode == True:
                self.ui = Ui_Fullscreen(0)
                
            elif self.mode == 1 and self.hasChangedDisplayMode == True:
                self.ui = Ui_Splitscreen()
                
            elif self.mode == 0 and self.hasChangedDisplayMode == True:
                self.ui = Ui_Shutdown(-1)

                
            if self.hasChangedDisplayMode and self.mode != 3:
                self.timer.start(1000)
                self.ui.setupUi(self)
                self.hasChangedDisplayMode = False
                self.lastMedia = True
        
            return self.index

    def updateMode(self):
        try:
            self.mode = int(req("get", ip_mode).json()[0]['activeMode'])
            self.modeBack = int(req("get", ip_mode).json()[0]['modeBack'])
            self.medias = req("get", ip_fs).json()
            self.start = req("get", ip_sb).json()[0]['start'].split(":")
            self.stop = req("get", ip_sb).json()[0]['stop'].split(":")
            self.sstart = req("get", ip_sb).json()[1]['start'].split(":")
            self.sstop = req("get", ip_sb).json()[1]['stop'].split(":")
            self.dstart = req("get", ip_sb).json()[2]['start'].split(":")
            self.dstop = req("get", ip_sb).json()[2]['stop'].split(":")
        except:
            print("cant fetch datas")

    def screenBlanking(self):
        now = datetime.now()
        self.current_hour = now.strftime("%H")
        self.current_minute = now.strftime("%M")
        self.current_days = now.strftime("%A")
        #print("Il est ", self.current_hour, ":", self.current_minute,  self.current_days)
        try:
            #print("La veille est prévue entre ", self.start[0], ":", self.start[1], " et ", self.stop[0], ":", self.stop[1])
            if self.current_days == "Sunday":
                if self.dstart[0] < self.current_hour:
                    self.veille = False
                    self.display("on")
                elif self.dstart[0] == self.current_hour and self.dstart[1] <= self.current_minute:
                    self.veille = False
                    self.display("on")
                else:
                    self.display("off")
            elif self.current_days == "Saturday":
                if self.sstart[0] <= self.sstop[0]:
                    if self.sstart[0] < self.current_hour:
                        if self.sstop[0] > self.current_hour:
                            self.display("on")

                        elif self.sstop[0] == self.current_hour and self.sstop[1] > self.current_minute:
                            self.display("on")

                        else:
                            self.display("off")

                    elif self.sstart[0] == self.current_hour and self.sstart[1] <= self.current_minute:
                        if self.sstop[0] > self.current_hour:
                            self.display("on")

                        elif self.sstop[0] == self.current_hour and self.sstop[1] > self.current_minute:
                            self.display("on")
                        else:
                            self.display("off")

                elif self.sstart[0] > self.sstop[0]:
                    if self.sstart[0] < self.current_hour:
                        if self.sstop[0] > self.current_hour:
                            self.display("off")

                        elif self.sstop[0] == self.current_hour and self.sstop[1] > self.current_minute:
                            self.display("off")

                        else:
                            self.display("on")

                    elif self.sstart[0] == self.current_hour and self.sstart[1] <= self.current_minute:
                        if self.sstop[0] > self.current_hour:
                            self.display("off")

                        elif self.sstop[0] == self.current_hour and self.sstop[1] > self.current_minute:
                            self.display("off")
                        else:
                            self.display("on")
            else:
                if self.start[0] <= self.stop[0]:
                    if self.start[0] < self.current_hour:
                        if self.stop[0] > self.current_hour:
                            self.display("on")   
                        elif self.stop[0] == self.current_hour and self.stop[1] > self.current_minute:
                            self.display("on")

                        else:
                            self.display("off")
                            

                    elif self.start[0] == self.current_hour and self.start[1] <= self.current_minute:
                        if self.stop[0] > self.current_hour:
                            self.display("on")

                        elif self.stop[0] == self.current_hour and self.stop[1] > self.current_minute:
                            self.display("on")
                        else:
                            self.display("off")
                            

                elif self.start[0] > self.stop[0]:
                    if self.start[0] < self.current_hour:
                        if self.stop[0] > self.current_hour:
                            self.display("off")

                        elif self.stop[0] == self.current_hour and self.stop[1] > self.current_minute:
                            self.display("off")
                            

                        else:
                            self.display("off")
                           
                    elif self.start[0] == self.current_hour and self.start[1] <= self.current_minute:
                        if self.stop[0] > self.current_hour:
                            self.display("off")
                           
                        elif self.stop[0] == self.current_hour and self.stop[1] > self.current_minute:
                            self.display("off")
                            
                        else:
                            self.display("off")

        except:
            print('start and stop not init')

    def display(self, state):
        # print("PROCESS", state)
        #subprocess.Popen(["xset", "-d", ":0", "dpms", "force",
        #              state], stdout=subprocess.PIPE)
        

        if state == "on" and self.veille == False:
          
            requests.put( ip_mode_put, data={'activeMode': self.modeBack})
            self.veille = True
        elif state == "off" and self.veille == True:
            
            requests.put( ip_mode_put, data={'activeMode': '0'}) 
            self.veille = False
            




if __name__ == '__main__':
    mode = 3
    medias = []
    index = 3
    app = QtWidgets.QApplication(sys.argv)
    main = Main(mode)
    main.show()
    sys.exit(app.exec_())
