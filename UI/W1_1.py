# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W1_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog1_1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(560, 560))
        Dialog.setMaximumSize(QtCore.QSize(560, 560))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pics/icon/Podpyatnik.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWhatsThis("")
        Dialog.setAccessibleDescription("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 560, 560))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(560, 560))
        self.label.setMaximumSize(QtCore.QSize(560, 560))
        self.label.setAutoFillBackground(True)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../pics/main/1-1.jpg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 499, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(3)
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 450, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 360, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_3.setMaxLength(3)
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setMaxLength(3)
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(410, 300, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setTabletTracking(False)
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setMaxLength(3)
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 9, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(510, 10, 41, 41))
        self.saveButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../pics/thumbs/savebtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon1)
        self.saveButton.setIconSize(QtCore.QSize(35, 35))
        self.saveButton.setShortcut("")
        self.saveButton.setDefault(False)
        self.saveButton.setFlat(True)
        self.saveButton.setObjectName("saveButton")

        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(510, 510, 41, 41))
        self.deleteButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../pics/thumbs/deletebtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon2)
        self.deleteButton.setIconSize(QtCore.QSize(35, 35))
        self.deleteButton.setShortcut("")
        self.deleteButton.setDefault(False)
        self.deleteButton.setFlat(True)
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.hide()

        self.lineEditlist = []
        self.lineEditlist.append(self.lineEdit)
        self.lineEditlist.append(self.lineEdit_2)
        self.lineEditlist.append(self.lineEdit_3)
        self.lineEditlist.append(self.lineEdit_4)
        self.lineEditlist.append(self.lineEdit_5)
        self.lineEditlist.append(self.lineEdit_6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "1 Отверстие Тип1"))
        self.lineEdit_3.setText(_translate("Dialog", "Ø"))
        self.label_2.setText(_translate("Dialog", "Производитель:"))
