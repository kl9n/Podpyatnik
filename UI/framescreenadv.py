# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'framescreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogFRSC(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 670)
        Dialog.setMinimumSize(QtCore.QSize(230, 670))
        Dialog.setMaximumSize(QtCore.QSize(650, 670))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pics/thumbs/frd1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.tit = "Рама"
        self.lineEdit_d0 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_d0.setGeometry(QtCore.QRect(160, 630, 50, 20))
        self.lineEdit_d0.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_d0.setMaxLength(4)
        self.lineEdit_d0.setFrame(False)
        self.lineEdit_d0.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_d0.setObjectName("lineEdit_d0")

        self.label_g1 = QtWidgets.QLabel(Dialog)
        self.label_g1.setGeometry(QtCore.QRect(0, 600, 230, 71))
        self.label_g1.setText("")
        self.label_g1.setPixmap(QtGui.QPixmap("../pics/frame/G1.png"))
        self.label_g1.setScaledContents(True)
        self.label_g1.setObjectName("label_g1")

        self.label_ng = QtWidgets.QLabel(Dialog)
        self.label_ng.setGeometry(QtCore.QRect(0, 600, 230, 71))
        self.label_ng.setText("")
        self.label_ng.setPixmap(QtGui.QPixmap("../pics/frame/NG.png"))
        self.label_ng.setScaledContents(True)
        self.label_ng.setObjectName("label_ng")

        self.bgrnd = QtWidgets.QLabel(Dialog)
        self.bgrnd.setGeometry(QtCore.QRect(0, 0, 670, 671))
        self.bgrnd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bgrnd.setText("")
        self.bgrnd.setPixmap(QtGui.QPixmap("../pics/frame/Bgrnd.png"))
        self.bgrnd.setScaledContents(True)
        self.bgrnd.setObjectName("bgrnd")

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 330, 411, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.lineEdit_frame = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_frame.setGeometry(QtCore.QRect(330, 380, 261, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_frame.setFont(font)
        self.lineEdit_frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_frame.setMaxLength(10)
        self.lineEdit_frame.setFrame(False)
        self.lineEdit_frame.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_frame.setObjectName("lineEdit_frame")

        self.lineEdit_variant = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_variant.setGeometry(QtCore.QRect(340, 430, 41, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_variant.setFont(font)
        self.lineEdit_variant.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_variant.setMaxLength(2)
        self.lineEdit_variant.setFrame(False)
        self.lineEdit_variant.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_variant.setObjectName("lineEdit_variant")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 430, 102, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(230, 380, 102, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(250, 480, 391, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")

        self.label_dg1 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                          '', '', '', '', '', '', '']
        self.label_dg2 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                          '', '', '', '', '', '', '']
        self.label_d1 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                         '', '', '', '', '', '']
        self.label_d2 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                         '', '', '', '', '', '']
        self.label_g2 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                         '', '', '', '', '', '']
        self.lineEdit_d1 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                            '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        for i in range (0,30):
            self.label_dg1[i] = QtWidgets.QLabel(Dialog)
            self.label_dg1[i].setGeometry(QtCore.QRect(0, 562, 178, 72))
            self.label_dg1[i].setText("")
            self.label_dg1[i].setPixmap(QtGui.QPixmap("../pics/frame/DG1.png"))
            self.label_dg1[i].setScaledContents(True)
            self.label_dg1[i].setObjectName("label_dg1{}".format(i))
            self.label_dg1[i].hide()

            self.label_d1[i] = QtWidgets.QLabel(Dialog)
            self.label_d1[i].setGeometry(QtCore.QRect(0, 512, 178, 72))
            self.label_d1[i].setText("")
            self.label_d1[i].setPixmap(QtGui.QPixmap("../pics/frame/D1.png"))
            self.label_d1[i].setScaledContents(True)
            self.label_d1[i].setObjectName("label_d1{}".format(i))
            self.label_d1[i].hide()

            self.label_d2[i] = QtWidgets.QLabel(Dialog)
            self.label_d2[i].setGeometry(QtCore.QRect(0, 462, 178, 72))
            self.label_d2[i].setText("")
            self.label_d2[i].setPixmap(QtGui.QPixmap("../pics/frame/D2.png"))
            self.label_d2[i].setScaledContents(True)
            self.label_d2[i].setObjectName("label_d2{}".format(i))
            self.label_d2[i].hide()

            self.label_dg2[i] = QtWidgets.QLabel(Dialog)
            self.label_dg2[i].setGeometry(QtCore.QRect(0, 362, 178, 72))
            self.label_dg2[i].setText("")
            self.label_dg2[i].setPixmap(QtGui.QPixmap("../pics/frame/DG2.png"))
            self.label_dg2[i].setScaledContents(True)
            self.label_dg2[i].setObjectName("label_dg2{}".format(i))
            self.label_dg2[i].hide()

            self.label_g2[i] = QtWidgets.QLabel(Dialog)
            self.label_g2[i].setGeometry(QtCore.QRect(0, 314, 178, 72))
            self.label_g2[i].setText("")
            self.label_g2[i].setPixmap(QtGui.QPixmap("../pics/frame/G2.png"))
            self.label_g2[i].setScaledContents(True)
            self.label_g2[i].setObjectName("label_g2{}".format(i))
            self.label_g2[i].hide()

        for i in range(0, 60):
            self.lineEdit_d1[i] = QtWidgets.QLineEdit(Dialog)
            self.lineEdit_d1[i].setGeometry(QtCore.QRect(145, 592, 50, 20))
            self.lineEdit_d1[i].setFocusPolicy(QtCore.Qt.ClickFocus)
            self.lineEdit_d1[i].setMaxLength(4)
            self.lineEdit_d1[i].setFrame(False)
            self.lineEdit_d1[i].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.lineEdit_d1[i].setObjectName("lineEdit_d1{}".format(i))
            self.lineEdit_d1[i].hide()

        self.bgrnd.raise_()
        self.label_g1.raise_()
        self.label_ng.raise_()
        self.lineEdit_d0.raise_()
        self.horizontalLayoutWidget.raise_()
        self.lineEdit_frame.raise_()
        self.lineEdit_variant.raise_()
        self.label_5.raise_()
        self.label_8.raise_()
        self.textEdit.raise_()

        for i in range(0,30):

            self.label_dg1[i].raise_()
            self.label_d1[i].raise_()
            self.label_d2[i].raise_()
            self.label_dg2[i].raise_()
            self.label_g2[i].raise_()

        for i in range(0, 60):
            self.lineEdit_d1[i].raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def settit (self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", self.tit))

    def retranslateUi(self, Dialog):
        self.settit(Dialog)
        _translate = QtCore.QCoreApplication.translate
        self.label_4.setText(_translate("Dialog", "Производитель:"))
        self.label_5.setText(_translate("Dialog", "Вариант №:"))
        self.label_8.setText(_translate("Dialog", "Рама HxB:"))
