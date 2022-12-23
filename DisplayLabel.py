from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, QDateTime
from data import *
from utils.req import req


class DisplayLabel(QLabel):
    def __init__(self, widget, posi):
        super().__init__(widget)
        self.timer = QTimer()
        self.posi = posi 
        
       
        if self.posi == 0 or  self.posi == 1 or self.posi == 2 or self.posi == 3:
            self.timer.start(1000)
            self.timer.timeout.connect(self.fetchData)
            self.timer.timeout.connect(self.updateData)
        else:
            self.timer.start(100)
            self.timer.timeout.connect(self.fetchData)
            self.timer.timeout.connect(self.updateData)
        self.path = "./"
        
        self.screen = False 
        

    def fetchData(self):
        print("DisplayLabel")
        try:
            fetched_datas = req("get", ip_fs).json()
            self.path = fetched_datas[self.posi]['path']
            print(self.path)
            ## TODO:
            # GET DATA


        except:
            print("cant fetch datas")


    def updateData(self):
        if self.posi == 1000:
            if self.screen == False:
                self.setStyleSheet("background-image:url(./fullscreenBlack.png)")
                self.screen = True 
        else:    
            self.setStyleSheet("background-image:url(" + path_to_media + self.path + ")")
            self.screen = False



    def blink(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()
