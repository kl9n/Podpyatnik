# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W3_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog3_1(object):
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
        self.label.setPixmap(QtGui.QPixmap("../pics/main/3-1.jpg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(365, 465, 51, 31))
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
        self.lineEdit_2.setGeometry(QtCore.QRect(485, 398, 41, 41))
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
        self.lineEdit_3.setGeometry(QtCore.QRect(485, 252, 41, 31))
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
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(275, 512, 61, 31))
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
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 270, 41, 71))
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
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 9, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(485, 285, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(220, 255, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_7.setMaxLength(3)
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(195, 465, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_8.setAutoFillBackground(True)
        self.lineEdit_8.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setMaxLength(3)
        self.lineEdit_8.setFrame(False)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(87, 380, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setTabletTracking(False)
        self.lineEdit_9.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_9.setAutoFillBackground(False)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setMaxLength(3)
        self.lineEdit_9.setFrame(False)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.menuButton = QtWidgets.QPushButton(Dialog)
        self.menuButton.setGeometry(QtCore.QRect(510, 10, 41, 41))
        self.menuButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../pics/thumbs/menubtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon4)
        self.menuButton.setIconSize(QtCore.QSize(35, 35))
        self.menuButton.setShortcut("")
        self.menuButton.setDefault(False)
        self.menuButton.setFlat(True)
        self.menuButton.setObjectName("menuButton")

        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(500, 100, 51, 51))
        self.saveButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../pics/thumbs/savebtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon1)
        self.saveButton.setIconSize(QtCore.QSize(45, 45))
        self.saveButton.setShortcut("")
        self.saveButton.setDefault(False)
        self.saveButton.setFlat(True)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.hide()

        self.screenshotButton = QtWidgets.QPushButton(Dialog)
        self.screenshotButton.setGeometry(QtCore.QRect(500, 170, 51, 51))
        self.screenshotButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../pics/thumbs/screenshotbtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.screenshotButton.setIcon(icon2)
        self.screenshotButton.setIconSize(QtCore.QSize(40, 40))
        self.screenshotButton.setShortcut("")
        self.screenshotButton.setDefault(False)
        self.screenshotButton.setFlat(True)
        self.screenshotButton.setObjectName("screenshotButton")
        self.screenshotButton.hide()

        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(500, 240, 51, 51))
        self.deleteButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../pics/thumbs/deletebtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon3)
        self.deleteButton.setIconSize(QtCore.QSize(45, 45))
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
        self.lineEditlist.append(self.lineEdit_7)
        self.lineEditlist.append(self.lineEdit_8)
        self.lineEditlist.append(self.lineEdit_9)

        self.lineEdit_6.hide()
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(200, 9, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "3 Отверстия Тип1"))
        self.lineEdit_3.setText(_translate("Dialog", "Ø"))
        self.label_2.setText(_translate("Dialog", "Производитель:"))
        self.label_3.setText(_translate("Dialog", "2 отв."))
        self.lineEdit_7.setText(_translate("Dialog", "Ø"))
