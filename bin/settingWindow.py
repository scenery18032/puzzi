# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\settingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect,QMetaObject,QCoreApplication
from PyQt5.QtGui import  QFont
from PyQt5.QtWidgets import QCheckBox,QComboBox,QFrame,QWidget,QVBoxLayout,QLabel,QGridLayout,QPushButton

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 294)
        self.randomMode = QCheckBox(Dialog)
        self.randomMode.setGeometry(QRect(150, 90, 91, 31))
        font = QFont()
        font.setFamily(".PingFang SC0")
        font.setPointSize(14)
        self.randomMode.setFont(font)
        self.randomMode.setObjectName("randomMode")
        self.levelMode = QCheckBox(Dialog)
        self.levelMode.setGeometry(QRect(270, 90, 91, 31))
        font = QFont()
        font.setFamily(".PingFang SC0")
        font.setPointSize(14)
        self.levelMode.setFont(font)
        self.levelMode.setObjectName("levelMode")
        self.line = QFrame(Dialog)
        self.line.setGeometry(QRect(40, 30, 321, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QFrame(Dialog)
        self.line_2.setGeometry(QRect(40, 240, 321, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QFrame(Dialog)
        self.line_3.setGeometry(QRect(30, 40, 16, 211))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QFrame(Dialog)
        self.line_4.setGeometry(QRect(350, 40, 16, 211))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.levelSelect = QComboBox(Dialog)
        self.levelSelect.setGeometry(QRect(150, 180, 191, 31))
        self.levelSelect.setObjectName("levelSelect")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setGeometry(QRect(60, 60, 71, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mode = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily(".PingFang SC0")
        font.setPointSize(14)
        self.mode.setFont(font)
        self.mode.setObjectName("mode")
        self.verticalLayout.addWidget(self.mode)
        self.level = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily(".PingFang SC0")
        font.setPointSize(14)
        self.level.setFont(font)
        self.level.setObjectName("level")
        self.verticalLayout.addWidget(self.level)
        self.layoutWidget_2 = QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QRect(70, 250, 274, 30))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comfirm = QPushButton(self.layoutWidget_2)
        self.comfirm.setObjectName("comfirm")
        self.gridLayout_2.addWidget(self.comfirm, 0, 0, 1, 1)
        self.cancel = QPushButton(self.layoutWidget_2)
        self.cancel.setObjectName("cancel")
        self.gridLayout_2.addWidget(self.cancel, 0, 2, 1, 1)
        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.cancel.clicked.connect(Dialog.close)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置"))
        self.randomMode.setText(_translate("Dialog", "随机"))
        self.levelMode.setText(_translate("Dialog", "选关"))
        self.mode.setText(_translate("Dialog", "模式"))
        self.level.setText(_translate("Dialog", "选关"))
        self.comfirm.setText(_translate("Dialog", "确定"))
        self.cancel.setText(_translate("Dialog", "取消"))
        self.label.setText(_translate("Dialog", " "))