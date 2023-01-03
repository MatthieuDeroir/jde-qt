# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fullscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from DisplayLabel import DisplayLabel
from utils.req import req
from data import *

from PyQt5.QtCore import QDir, Qt, QUrl, QTimer
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon


class Ui_Fullscreen(object):
    def __init__(self, index):
        self.index = index
        self.path = "./"
        self.current_path = './'
        timer = QTimer()
        timer.start(1000)  # Update the UI every 1 second
        timer.timeout.connect(self.updateUi)
        timer.timeout.connect(self.setupUi)
        self.hasModifiedMediaSource = True

    def updateUi(self):
        try:
            fetched_datas = req("get", ip_fs).json()
            self.path = fetched_datas[self.index]['path']
        except:
            print("cant fetch datas")
        if self.path != self.current_path:
            self.current_path = self.path
            self.hasModifiedMediaSource = True
        else:
            self.hasModifiedMediaSource = False

    def setupUi(self, MainWindow):
        if self.hasModifiedMediaSource:
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(192, 433)
            if self.path[-3:] == 'mp4':
                videoWidget = QVideoWidget()
                wid = QtWidgets.QWidget(MainWindow)
                MainWindow.setCentralWidget(wid)
                self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
                layout = QVBoxLayout()
                layout.addWidget(videoWidget)
                wid.setLayout(layout)
                self.mediaPlayer.setObjectName("display_label")
                self.mediaPlayer.setVideoOutput(videoWidget)
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('/home/pi/jde/panel/GUI/Chats.mp4')))
                self.mediaPlayer.play()
            else:
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(0, 0, screen_width, screen_height))
                self.label.setObjectName("label")
                MainWindow.setCentralWidget(self.centralwidget)

                self.display_label = DisplayLabel(self.centralwidget, self.index)
                self.display_label.setObjectName("display_label")
                self.display_label.setStyleSheet("background-image: url(./fullscreen.png)")
                self.display_label.setStyleSheet("background-image:url(./fullscreenBlack.png)")
                self.display_label.setGeometry(QtCore.QRect(0, 0, screen_width, screen_height))

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
