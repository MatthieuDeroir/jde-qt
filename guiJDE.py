# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self):
        super().__init__()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(190, 463)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color:black;")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 50, 191, 171))
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:orange;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:green;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:white;")
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setScaledContents(False)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:orange;")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_7.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color:green;")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_7.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color:white;")
        self.label_22.setTextFormat(QtCore.Qt.AutoText)
        self.label_22.setScaledContents(False)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_7.addWidget(self.label_22)
        self.gridLayout.addLayout(self.horizontalLayout_7, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:orange;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:green;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:white;")
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:orange;")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:blue;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:orange;")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:blue;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:white;")
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setScaledContents(False)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:orange;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_6.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:blue;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:white;")
        self.label_19.setTextFormat(QtCore.Qt.AutoText)
        self.label_19.setScaledContents(False)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_6.addWidget(self.label_19)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 240, 189, 23))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_4.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:white;")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_8.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:white;")
        self.label_24.setTextFormat(QtCore.Qt.AutoText)
        self.label_24.setScaledContents(False)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_8.addWidget(self.label_24)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 280, 191, 171))
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        self.gridLayoutWidget_2.setFont(font)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_25.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:orange;")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_9.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:red;")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_9.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:white;")
        self.label_27.setTextFormat(QtCore.Qt.AutoText)
        self.label_27.setScaledContents(False)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_9.addWidget(self.label_27)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_28.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color:orange;")
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_10.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color:red;")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_10.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:white;")
        self.label_30.setTextFormat(QtCore.Qt.AutoText)
        self.label_30.setScaledContents(False)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_10.addWidget(self.label_30)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 5, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_31.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color:orange;")
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_11.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color:red;")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_11.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color:white;")
        self.label_33.setTextFormat(QtCore.Qt.AutoText)
        self.label_33.setScaledContents(False)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_11.addWidget(self.label_33)
        self.gridLayout_2.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_34.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color:orange;")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_12.addWidget(self.label_34)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color:red;")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_12.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color:white;")
        self.label_36.setTextFormat(QtCore.Qt.AutoText)
        self.label_36.setScaledContents(False)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_12.addWidget(self.label_36)
        self.gridLayout_2.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_37 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_37.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color:orange;")
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_13.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color:red;")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_13.addWidget(self.label_38)
        self.label_39 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color:white;")
        self.label_39.setTextFormat(QtCore.Qt.AutoText)
        self.label_39.setScaledContents(False)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_13.addWidget(self.label_39)
        self.gridLayout_2.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_40 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_40.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color:orange;")
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_14.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color:red;")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_14.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color:white;")
        self.label_42.setTextFormat(QtCore.Qt.AutoText)
        self.label_42.setScaledContents(False)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_14.addWidget(self.label_42)
        self.gridLayout_2.addLayout(self.horizontalLayout_14, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 11, 85, 20))
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 90, 21))
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 10, 187, 21))
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.label_2.raise_()
        self.gridLayoutWidget.raise_()
        self.horizontalLayoutWidget_8.raise_()
        self.gridLayoutWidget_2.raise_()
        self.label.raise_()
        self.label_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_14.setText(_translate("Form", "0123456789"))
        self.label_15.setText(_translate("Form", "COME"))
        self.label_16.setText(_translate("Form", "13"))
        self.label_20.setText(_translate("Form", "0123456789"))
        self.label_21.setText(_translate("Form", "COME"))
        self.label_22.setText(_translate("Form", "13"))
        self.label_8.setText(_translate("Form", "0123456789"))
        self.label_9.setText(_translate("Form", "COME"))
        self.label_10.setText(_translate("Form", "13"))
        self.label_5.setText(_translate("Form", "0123456789"))
        self.label_6.setText(_translate("Form", "LOADING"))
        self.label_7.setText(_translate("Form", "13"))
        self.label_11.setText(_translate("Form", "0123456789"))
        self.label_12.setText(_translate("Form", "LOADING"))
        self.label_13.setText(_translate("Form", "13"))
        self.label_17.setText(_translate("Form", "0123456789"))
        self.label_18.setText(_translate("Form", "LOADING"))
        self.label_19.setText(_translate("Form", "13"))
        self.label_4.setText(_translate("Form", "NEXT TRUCKS"))
        self.label_23.setText(_translate("Form", "STATE"))
        self.label_24.setText(_translate("Form", "DOCKS"))
        self.label_25.setText(_translate("Form", "0123456789"))
        self.label_26.setText(_translate("Form", "WAIT"))
        self.label_27.setText(_translate("Form", "13"))
        self.label_28.setText(_translate("Form", "0123456789"))
        self.label_29.setText(_translate("Form", "WAIT"))
        self.label_30.setText(_translate("Form", "13"))
        self.label_31.setText(_translate("Form", "0123456789"))
        self.label_32.setText(_translate("Form", "WAIT"))
        self.label_33.setText(_translate("Form", "13"))
        self.label_34.setText(_translate("Form", "0123456789"))
        self.label_35.setText(_translate("Form", "WAIT"))
        self.label_36.setText(_translate("Form", "13"))
        self.label_37.setText(_translate("Form", "0123456789"))
        self.label_38.setText(_translate("Form", "WAIT"))
        self.label_39.setText(_translate("Form", "13"))
        self.label_40.setText(_translate("Form", "0123456789"))
        self.label_41.setText(_translate("Form", "WAIT"))
        self.label_42.setText(_translate("Form", "13"))
        self.label.setText(_translate("Form", "LOADING TRUCKS"))
        self.label_2.setText(_translate("Form", "STATE"))
        self.label_3.setText(_translate("Form", "DOCKS"))