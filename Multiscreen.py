# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fullscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from data import screen_width, screen_height
from DisplayLabel import DisplayLabel
from Trucks import Ui_Truckscreen


class Ui_Multiscreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(192, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, screen_width, screen_height))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.display_label = DisplayLabel(self.centralwidget, 0)
        self.display_label.setObjectName("display_label")
        self.display_label.setGeometry(QtCore.QRect(0, 0, screen_width, screen_height))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

