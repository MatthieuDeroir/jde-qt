from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QVBoxLayout

from DisplayLabel import DisplayLabel
from data import *
from utils.req import req

class Ui_Splitscreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(screen_width, screen_height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        layout = QVBoxLayout()
        self.centralwidget.setLayout(layout)
        MainWindow.setCentralWidget(self.centralwidget)

        try:
            self.fetched_datas = req("get", ip_fs).json()
        except:
            print("cant fetch datas")

        for i in range(1, 4):
            if self.fetched_datas[i]['format'] == 'mp4':
                videoWidget = QVideoWidget()
                layout.addWidget(videoWidget, 0, 0)
                mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
                mediaPlayer.setObjectName("mediaPlayer")
                mediaPlayer.setVideoOutput(videoWidget)
                mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path_to_video+self.fetched_datas[i]['path'])))
                videoWidget.show()
                videoWidget.raise_()
                mediaPlayer.play()
                mediaPlayer.error.connect(self.handleError)
            else:
                display_label = DisplayLabel(self.centralwidget, i)
                display_label.setObjectName("display_label_" + str(i))
                layout.addWidget(display_label)


    def handleError(self, error):
        if error == QMediaPlayer.ResourceError:
            print("Media file not found or network error")
        elif error == QMediaPlayer.QMediaPlayer.FormatError:
            print("Media file format not supported")
        elif error == QMediaPlayer.AccessDeniedError:
            print("Access to media file denied")
        else:
            print("Error while playing the media file")