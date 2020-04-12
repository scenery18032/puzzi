# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\passLevel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import QRect,QMetaObject,QCoreApplication
from PyQt5.QtGui import  QFont
from PyQt5.QtWidgets import QFrame,QWidget,QVBoxLayout,QLabel,QGridLayout,QPushButton



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 294)
        self.line_2 = QFrame(Dialog)
        self.line_2.setGeometry(QRect(40, 230, 321, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setGeometry(QRect(100, 120, 56, 85))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.useTime = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily(".PingFang SC0")
        font.setPointSize(16)
        self.useTime.setFont(font)
        self.useTime.setObjectName("useTime")
        self.verticalLayout.addWidget(self.useTime)
        self.useCount = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily(".PingFang SC0")
        font.setPointSize(16)
        self.useCount.setFont(font)
        self.useCount.setObjectName("useCount")
        self.verticalLayout.addWidget(self.useCount)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(70, 50, 241, 51))
        font = QFont()
        font.setFamily(".PingFang SC0")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget_2 = QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QRect(60, 250, 274, 30))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.next = QPushButton(self.layoutWidget_2)
        self.next.setObjectName("next")
        self.gridLayout_2.addWidget(self.next, 0, 0, 1, 1)
        self.quit = QPushButton(self.layoutWidget_2)
        self.quit.setObjectName("quit")
        self.gridLayout_2.addWidget(self.quit, 0, 2, 1, 1)
        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.line = QFrame(Dialog)
        self.line.setGeometry(QRect(40, 20, 321, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QFrame(Dialog)
        self.line_4.setGeometry(QRect(350, 30, 16, 211))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QFrame(Dialog)
        self.line_3.setGeometry(QRect(30, 30, 16, 211))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "闯关成功！"))
        self.useTime.setText(_translate("Dialog", "用时"))
        self.useCount.setText(_translate("Dialog", "步数"))
        self.label.setText(_translate("Dialog", "恭喜你！通过第一关"))
        self.next.setText(_translate("Dialog", "继续游戏"))
        self.quit.setText(_translate("Dialog", "退出游戏"))
