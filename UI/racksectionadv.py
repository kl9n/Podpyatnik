# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'racksection.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowSec(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(330, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pics/thumbs/level.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Rframe_1 = QtWidgets.QLabel(self.centralwidget)
        self.Rframe_1.setGeometry(QtCore.QRect(40, 60, 20, 488))
        self.Rframe_1.setText("")
        self.Rframe_1.setPixmap(QtGui.QPixmap("../pics/levels/Рама.png"))
        self.Rframe_1.setScaledContents(True)
        self.Rframe_1.setObjectName("Rframe_1")

        self.Beam = ['','','','','','','','','','','','']
        for bn in range(0,11):
            self.Beam[bn] = QtWidgets.QLabel(self.centralwidget)
            self.Beam[bn].setGeometry(QtCore.QRect(50, 250, 296, 56))
            self.Beam[bn].setText("")
            self.Beam[bn].setPixmap(QtGui.QPixmap("../pics/levels/Балка.png"))
            self.Beam[bn].setScaledContents(True)
            self.Beam[bn].setObjectName("Beam_{}".format(bn))
            self.Beam[bn].hide()

        self.Rframe_2 = QtWidgets.QLabel(self.centralwidget)
        self.Rframe_2.setGeometry(QtCore.QRect(234, 60, 20, 488))
        self.Rframe_2.setText("")
        self.Rframe_2.setPixmap(QtGui.QPixmap("../pics/levels/Рама.png"))
        self.Rframe_2.setScaledContents(True)
        self.Rframe_2.setObjectName("Rframe_2")

        self.lineEditHB = ['', '', '', '', '', '', '', '', '', '', '', '']
        for bn in range(0,11):
            self.lineEditHB[bn] = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEditHB[bn].setGeometry(QtCore.QRect(270, 245, 50, 20))
            self.lineEditHB[bn].setFocusPolicy(QtCore.Qt.ClickFocus)
            self.lineEditHB[bn].setMaxLength(5)
            self.lineEditHB[bn].setFrame(False)
            self.lineEditHB[bn].setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.lineEditHB[bn].setObjectName("lineEdit_h{}".format(bn))
            self.lineEditHB[bn].hide()

        self.bgrnd = QtWidgets.QLabel(self.centralwidget)
        self.bgrnd.setGeometry(QtCore.QRect(0, 0, 331, 571))
        self.bgrnd.setText("")
        self.bgrnd.setPixmap(QtGui.QPixmap("../pics/levels/Bgrnd.png"))
        self.bgrnd.setScaledContents(True)
        self.bgrnd.setObjectName("bgrnd")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 0, 21, 571))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 200, 32))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../pics/levels/rscale.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit_rackwidth = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_rackwidth.setGeometry(QtCore.QRect(82, 30, 131, 20))
        self.lineEdit_rackwidth.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_rackwidth.setMaxLength(14)
        self.lineEdit_rackwidth.setFrame(False)
        self.lineEdit_rackwidth.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_rackwidth.setObjectName("lineEdit_rackwidth")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 10, 451, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 420, 295, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_ln = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ln.setGeometry(QtCore.QRect(650, 420, 141, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_ln.setFont(font)
        self.lineEdit_ln.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_ln.setMaxLength(2)
        self.lineEdit_ln.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ln.setObjectName("lineEdit_ln")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 60, 102, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 60, 31, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_2.setMaxLength(2)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_ln = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ln.setGeometry(QtCore.QRect(340, 465, 451, 41))
        self.pushButton_ln.setObjectName("pushButton_ln")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(340, 390, 451, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(500, 60, 102, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(600, 60, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_5.setMaxLength(10)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(340, 110, 131, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(470, 110, 321, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_pp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pp.setGeometry(QtCore.QRect(570, 520, 221, 41))
        self.pushButton_pp.setAutoFillBackground(False)
        self.pushButton_pp.setDefault(True)
        self.pushButton_pp.setFlat(False)
        self.pushButton_pp.setObjectName("pushButton_pp")
        self.pushButton_prnt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_prnt.setGeometry(QtCore.QRect(340, 520, 221, 41))
        self.pushButton_prnt.setObjectName("pushButton_prnt")

        self.bgrnd.raise_()
        self.Rframe_2.raise_()
        self.Rframe_1.raise_()

        for bn in range(0,11):
            self.Beam[bn].raise_()

        for bn in range(0,11):
            self.lineEditHB[bn].raise_()

        self.line.raise_()
        self.label.raise_()
        self.lineEdit_rackwidth.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_7.raise_()
        self.lineEdit_ln.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_ln.raise_()
        self.line_2.raise_()
        self.label_8.raise_()
        self.lineEdit_5.raise_()
        self.label_9.raise_()
        self.textEdit.raise_()
        self.pushButton_prnt.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.pushButton_pp.raise_()
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Отрисовка секций"))
        self.label_3.setText(_translate("MainWindow", "Производитель:"))
        self.label_7.setText(_translate("MainWindow", "Количество уровней включая пол (от 2 до 12):"))
        self.label_4.setText(_translate("MainWindow", "Вариант №:"))
        self.pushButton_ln.setText(_translate("MainWindow", "Сгенерировать рисунок в соответствии с числом уровней"))
        self.label_8.setText(_translate("MainWindow", "Рама HxB:"))
        self.label_9.setText(_translate("MainWindow", "Комментарий:"))
        self.pushButton_pp.setText(_translate("MainWindow", "Назад к подпятникам"))
        self.pushButton_prnt.setText(_translate("MainWindow", "Окно для скриншота"))