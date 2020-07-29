# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YNWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class YN_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(250, 140)
        Dialog.setMinimumSize(QtCore.QSize(250, 140))
        Dialog.setMaximumSize(QtCore.QSize(250, 140))
        Dialog.setWindowTitle("Внимание!")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pics/icon/attention.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.YesButton = QtWidgets.QPushButton(Dialog)
        self.YesButton.setGeometry(QtCore.QRect(10, 90, 100, 40))
        self.YesButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YesButton.setText("Да, всё ок!")
        self.YesButton.setShortcut("")
        self.YesButton.setAutoDefault(True)
        self.YesButton.setDefault(False)
        self.YesButton.setFlat(False)
        self.YesButton.setObjectName("YesButton")
        self.NoButton = QtWidgets.QPushButton(Dialog)
        self.NoButton.setGeometry(QtCore.QRect(115, 90, 125, 40))
        self.NoButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NoButton.setText("Нет, сейчас добавлю!")
        self.NoButton.setShortcut("")
        self.NoButton.setAutoDefault(True)
        self.NoButton.setDefault(False)
        self.NoButton.setFlat(False)
        self.NoButton.setObjectName("NoButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 15, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setAcceptDrops(False)
        self.label.setLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 35, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setAcceptDrops(False)
        self.label_2.setLineWidth(0)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        self.first_stringtext = "Обнаружены незаполненные поля!"
        self.second_stringtext = "Продолжить сохранение?"

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", self.first_stringtext))
        self.label_2.setText(_translate("Dialog", self.second_stringtext))
