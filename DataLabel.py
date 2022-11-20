from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, QDateTime
from data import data, ip, blink_time
from utils.req import req


class DataLabel(QLabel):
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
            fetched_datas = req("get", ip).json()
            if self.category == 'ref':
                self.data = str(fetched_datas[self.index]['plate'])
            elif self.category == 'dock':
                self.data = str(fetched_datas[self.index]['dockIndex'])
            elif self.category == 'state':
                if fetched_datas[self.index]['state'] is False:
                    self.data = 'WAIT'
                elif fetched_datas[self.index]['state'] is True and fetched_datas[self.index]['flag'] is True:
                    self.data = 'COME'
                else:
                    self.data = 'LOADING'


            if (self.category is 'state' or self.category is 'dock') and fetched_datas[self.index]['plate'] == '':
                self.data = ''
            # if self.category is 'state' and self.data is 'COME' and self.time > blink_time:
            #     self.data = "LOADING"
            #     req("put", ip + "/" + fetched_datas[self.index]["_id"], {
            #         "flag": False
            #     })
            #     print(req("get", ip).json()[self.index]['flag'])
            #     self.time = 0
            # elif self.category is 'state' and self.data == 'COME' and self.time <= blink_time:
            #     self.time = self.time + 1

        except:
            print("cant fetch datas")

# self.data[self.index][self.category] = fetched_datas[self.index]

    def updateData(self):
        self.setText(self.data)
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
