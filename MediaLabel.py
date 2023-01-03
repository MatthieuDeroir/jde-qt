from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, QDateTime
from data import *
from utils.req import req
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget



class MediaLabel(QLabel):
    def __init__(self, widget, pos):
        super().__init__(widget)
        self.timer = QTimer()
        self.pos = pos

        self.timer.start(1000)

        self.timer.timeout.connect(self.fetchData)
        self.timer.timeout.connect(self.updateMedia)
        self.setScaledContents(True)

        self.path = "./"
        self.current_path = "./"
        self.hasModifiedMediaSource = True

        # Create a QMediaPlayer object and set its video output to the label
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self)


    def fetchData(self):
        print("DisplayLabel")
        if self.pos == -1:
            self.path = "medias/fullscreenBlack.png"
        else:
            try:
                fetched_datas = req("get", ip_fs).json()
                self.path = fetched_datas[self.pos]['path']
            except:
                print("cant fetch datas")
            if self.path != self.current_path:
                self.current_path = self.path
                self.hasModifiedMediaSource = True
            else:
                self.hasModifiedMediaSource = False

    def updateMedia(self):
        if self.hasModifiedMediaSource:
            #"""Set the media file to be displayed in the label."""
            _, file_extension = os.path.splitext(self.path)
            if file_extension in ('.jpg', '.png', '.gif'):
                # Load the image and set it as the label's pixmap
                pixmap = QtGui.QPixmap(self.path)
                self.setPixmap(pixmap)
            else:
                # Set the media player's media to the video file
                media = QMediaContent(QtCore.QUrl.fromLocalFile(self.path))
                self.media_player.setMedia(media)
                self.media_player.play()

    # def updateData(self):
    #     if self.pos == -1:
    #         self.setStyleSheet("background-image:url(" + self.path + ")")
    #     else:
    #         self.setStyleSheet("background-image:url(" + path_to_media + self.path + ")")

    def blink(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()
