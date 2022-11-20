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
    def __init__(self, option):
        super(Main, self).__init__()
        self.option = option

        # build ui
        self.getOption()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.getOption)
        self.timer.start(1000)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.move(0,0)


    def getOption(self):
        if option == 0:
            self.ui = Ui_MainWindow()
        elif option == 1:
            self.ui = Ui_Fullscreen()
        elif option == 2:
            self.ui = Ui_Splitscreen()
    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')



if __name__ == '__main__':
    option = 0
    app = QtWidgets.QApplication(sys.argv)
    main = Main(option)
    main.show()
    sys.exit(app.exec_())


