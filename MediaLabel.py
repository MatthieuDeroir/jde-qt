# from PyQt5.QtWidgets import QLabel
# from PyQt5.QtCore import QTimer, QDateTime
from data import *
# from utils.req import req
# import os
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
#
#
#
# class MediaLabel(QLabel, QVideoWidget):
#     def __init__(self, widget, pos):
#         super().__init__(widget)
#         self.timer = QTimer()
#         self.pos = pos
#
#         self.timer.start(1000)
#
#         self.timer.timeout.connect(self.fetchData)
#         self.timer.timeout.connect(self.updateMedia)
#         self.setScaledContents(True)
#
#         self.path = "./"
#         self.current_path = "./"
#         self.hasModifiedMediaSource = True
#
#         # Create a QVideoWidget to display the video
#         video_widget = QVideoWidget()
#
#         # Create a QLabel to show the pixmap
#         self.image_label = QLabel(self)
#         self.image_label.setScaledContents(True)
#
#         # Set the media to the video file
#
#
#
#         # Create a QMediaPlayer object and set its video output to the label
#         self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
#         self.media_player.setVideoOutput(self)
#
#
#     def fetchData(self):
#         print("DisplayLabel")
#         if self.pos == -1:
#             self.path = "medias/fullscreenBlack.png"
#         else:
#             try:
#                 fetched_datas = req("get", ip_fs).json()
#                 self.path = fetched_datas[self.pos]['path']
#             except:
#                 print("cant fetch datas")
#             if self.path != self.current_path:
#                 self.current_path = self.path
#                 self.hasModifiedMediaSource = True
#                 print("Media source Modified !")
#             else:
#                 self.hasModifiedMediaSource = False
#
#     def updateMedia(self):
#         if self.hasModifiedMediaSource:
#
#             #"""Set the media file to be displayed in the label."""
#             _, file_extension = os.path.splitext(path_to_media + self.path)
#             if file_extension in ('.jpg', '.png', '.gif', '.jpeg'):
#                 print("File is an image")
#                 # Load the image and set it as the label's pixmap
#                 pixmap = QtGui.QPixmap(path_to_media + self.path)
#                 print("Pixmap created")
#                 self.image_label.setPixmap(pixmap)
#                 print("Pixmap setted")
#                 # self.setStyleSheet("background-image:url(" + path_to_media + self.path + ")")
#
#             else:
#                 print("File is a video")
#                 # Set the media player's media to the video file
#                 media = QMediaContent(QtCore.QUrl.fromLocalFile(path_to_media + self.path))
#
#                 self.media_player.setMedia(media)
#                 self.media_player.play()
#                 print("media played")
#
#     # def updateData(self):
#     #     if self.pos == -1:
#     #         self.setStyleSheet("background-image:url(" + self.path + ")")
#     #     else:
#     #         self.setStyleSheet("background-image:url(" + path_to_media + self.path + ")")
#
#     def blink(self):
#         if self.isHidden():
#             self.show()
#         else:
#             self.hide()
# #

import os
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class MediaLabel(QLabel, QVideoWidget):
    def __init__(self, widget, pos):
        super().__init__(widget)
        self.timer = QTimer()
        self.pos = pos
        self.timer.start(1000) # update every second
        self.timer.timeout.connect(self.fetchData)
        self.timer.timeout.connect(self.updateMedia)
        self.setScaledContents(True)
        self.path = "./"
        self.current_path = "./"
        self.hasModifiedMediaSource = True
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self)

    def fetchData(self):
        if self.pos == -1:
            self.path = "medias/fullscreenBlack.png"
        else:
            # fetch data from database
            fetched_datas = req("get", ip_fs).json()
            self.path = fetched_datas[self.pos]['path']
            if self.path != self.current_path:
                self.current_path = self.path
                self.hasModifiedMediaSource = True
            else:
                self.hasModifiedMediaSource = False

    def updateMedia(self):
        if self.hasModifiedMediaSource:
            _, file_extension = os.path.splitext(path_to_media + self.path)
            if file_extension in ('.jpg', '.png', '.gif', '.jpeg'):
                # Load the image and set it as the label's pixmap
                pixmap = QtGui.QPixmap(path_to_media + self.path)
                self.setPixmap(pixmap)
            else:
                # Set the media player's media to the video file
                media = QMediaContent(QtCore.QUrl.fromLocalFile(path_to_media + self.path))
                self.media_player.setMedia(media)
                self.media_player.play()
