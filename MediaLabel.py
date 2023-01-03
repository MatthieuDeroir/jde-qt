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

        # Create a QLabel to show the pixmap
        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)

        # Create a QMediaPlayer object and set its video output to the label
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.image_label)


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
                print("Media source Modified !")
            else:
                self.hasModifiedMediaSource = False

    def updateMedia(self):
        if self.hasModifiedMediaSource:

            #"""Set the media file to be displayed in the label."""
            _, file_extension = os.path.splitext(path_to_media + self.path)
            if file_extension in ('.jpg', '.png', '.gif', '.jpeg'):
                print("File is an image")
                # Load the image and set it as the label's pixmap
                pixmap = QtGui.QPixmap(path_to_media + self.path)
                print("Pixmap created")
                self.image_label.setPixmap(pixmap)
                print("Pixmap setted")
                # self.setStyleSheet("background-image:url(" + path_to_media + self.path + ")")

            else:
                print("File is a video")
                # Create a QMovie object and set the file name to the video file
                movie = QtGui.QMovie(path_to_media + self.path)
                # Set the movie to be displayed in the label
                self.setMovie(movie)
                # Start playing the movie
                movie.start()
                print("media played")

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
