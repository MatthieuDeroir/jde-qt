from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, QDateTime
from data import data, ip_fs, blink_time
from utils.req import req


class DisplayLabel(QLabel):
    def __init__(self, widget, index, category):
        super().__init__(widget)
        self.timer = QTimer()
        self.index = index
        self.category = category
        self.timer.start(1000)
        self.data = ""
        self.previous_state = "LOADING"
        self.time = 0
        self.timer.timeout.connect(self.updateData)
        self.timer.timeout.connect(self.fetchData)

    def fetchData(self):
        try:
            fetched_datas = req("get", ip_fs).json()
            ## TODO:
            # GET DATA
            print(fetched_datas)

        except:
            print("cant fetch datas")

# self.data[self.index][self.category] = fetched_datas[self.index]

    def updateData(self):
        self.setText(self.data)
        self.show()
        # self.setStyleSheet("background-image: url(./"+ self.data +")")
        if self.category == 'state' and self.data == 'COME':
            self.timer.timeout.connect(self.blink)
            self.setStyleSheet("color: #66FF22")
        elif self.category == 'state' and self.data == 'LOADING':
            self.setStyleSheet("color: blue")
        elif self.category == 'state' and self.data == 'WAIT':
            self.setStyleSheet("color: orange")


    def blink(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()
