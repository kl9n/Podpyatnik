# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rerr.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogER(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(310, 70)
        Dialog.setMinimumSize(QtCore.QSize(310, 70))
        Dialog.setMaximumSize(QtCore.QSize(310, 70))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pics/icon/info.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 280, 16))
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.title = ''

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def settitle (self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", self.title))

    def retranslateUi(self, Dialog):
        self.settitle(Dialog)

