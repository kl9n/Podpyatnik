# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'racksecscreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(670, 650)
        self.bgrnd = QtWidgets.QLabel(Dialog)
        self.bgrnd.setGeometry(QtCore.QRect(0, 0, 671, 651))
        self.bgrnd.setText("")
        self.bgrnd.setPixmap(QtGui.QPixmap("../pics/levels/Bgrnd.png"))
        self.bgrnd.setScaledContents(True)
        self.bgrnd.setObjectName("bgrnd")
        self.Beam_1 = QtWidgets.QLabel(Dialog)
        self.Beam_1.setGeometry(QtCore.QRect(50, 350, 296, 56))
        self.Beam_1.setText("")
        self.Beam_1.setPixmap(QtGui.QPixmap("../pics/levels/Балка.png"))
        self.Beam_1.setScaledContents(True)
        self.Beam_1.setObjectName("Beam_1")
        self.lineEdit_HB = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_HB.setGeometry(QtCore.QRect(270, 345, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_HB.setFont(font)
        self.lineEdit_HB.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_HB.setMaxLength(5)
        self.lineEdit_HB.setFrame(False)
        self.lineEdit_HB.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_HB.setObjectName("lineEdit_HB")
        self.Rframe_1 = QtWidgets.QLabel(Dialog)
        self.Rframe_1.setGeometry(QtCore.QRect(40, 160, 20, 488))
        self.Rframe_1.setText("")
        self.Rframe_1.setPixmap(QtGui.QPixmap("../pics/levels/Рама.png"))
        self.Rframe_1.setScaledContents(True)
        self.Rframe_1.setObjectName("Rframe_1")
        self.lineEdit_rackwidth = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_rackwidth.setGeometry(QtCore.QRect(82, 130, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_rackwidth.setFont(font)
        self.lineEdit_rackwidth.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_rackwidth.setMaxLength(14)
        self.lineEdit_rackwidth.setFrame(False)
        self.lineEdit_rackwidth.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_rackwidth.setObjectName("lineEdit_rackwidth")
        self.Rframe_2 = QtWidgets.QLabel(Dialog)
        self.Rframe_2.setGeometry(QtCore.QRect(234, 160, 20, 488))
        self.Rframe_2.setText("")
        self.Rframe_2.setPixmap(QtGui.QPixmap("../pics/levels/Рама.png"))
        self.Rframe_2.setScaledContents(True)
        self.Rframe_2.setObjectName("Rframe_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 130, 200, 32))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../pics/levels/rscale.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 561, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 60, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_2.setMaxLength(2)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(180, 60, 102, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(280, 60, 191, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_5.setMaxLength(10)
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 102, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(340, 160, 321, 481))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        self.bgrnd.raise_()
        self.Rframe_1.raise_()
        self.label.raise_()
        self.Rframe_2.raise_()
        self.Beam_1.raise_()
        self.lineEdit_HB.raise_()
        self.lineEdit_rackwidth.raise_()
        self.horizontalLayoutWidget.raise_()
        self.lineEdit_2.raise_()
        self.label_8.raise_()
        self.lineEdit_5.raise_()
        self.label_4.raise_()
        self.textEdit.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Секция"))
        self.label_3.setText(_translate("Dialog", "Производитель:"))
        self.label_8.setText(_translate("Dialog", "Рама HxB:"))
        self.label_4.setText(_translate("Dialog", "Вариант №:"))
