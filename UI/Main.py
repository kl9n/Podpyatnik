import sys
from WMain import *; from W1_1 import *
from W1_2 import *; from W2_1 import *
from W2_2 import *; from W3_1 import *
from W3_2 import *; from W3_3 import *
from W3_4 import *; from W4_1 import *
from W4_2 import *; from W4_3 import *
from W5_1 import *; from W6_1 import *
from W6_2 import *; from W9_1 import *
from WF_1 import *; from WF_2 import *
from WF_3 import *; from WF_4 import *
from WF_5 import *; from WF_6 import *
from WF_7 import *; from WR_1 import *
from WR_2 import *; from WR_3 import *
from WR_4 import *; from WF_8 import *
from WF_9 import *; from WF_10 import *
from WF_11 import *
from Diag1 import *; from Diag2 import *
from Diag3 import *; from Diag4 import *
from Diag5 import *; from Diag6 import *
from Diag7 import *
from racksectionadv import *
from rerr import *
from framedimuiadv import *
from frameerr import *
from framescreenadv import *
from racksecscreenadv import *
from PyQt5 import QtCore, QtGui, QtWidgets

class W1_1(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog1_1()
        self.ui.setupUi(self)

class W1_2(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog1_2()
        self.ui.setupUi(self)

class W2_1(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog2_1()
        self.ui.setupUi(self)

class W2_2(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog2_2()
        self.ui.setupUi(self)

class W3_1(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog3_1()
        self.ui.setupUi(self)

class W3_2(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog3_2()
        self.ui.setupUi(self)

class W3_3(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog3_3()
        self.ui.setupUi(self)

class W3_4(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog3_4()
        self.ui.setupUi(self)

class W4_1(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog4_1()
        self.ui.setupUi(self)

class W4_2(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog4_2()
        self.ui.setupUi(self)

class W4_3(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog4_3()
        self.ui.setupUi(self)

class W5_1(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog5_1()
        self.ui.setupUi(self)

class W6_1(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog6_1()
        self.ui.setupUi(self)

class W6_2(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog6_2()
        self.ui.setupUi(self)

class W9_1(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog9_1()
        self.ui.setupUi(self)

class WF_1(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogF_1()
        self.ui.setupUi(self)

class WF_2(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogF_2()
        self.ui.setupUi(self)

class WF_3(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogF_3()
        self.ui.setupUi(self)

class WF_4(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogF_4()
        self.ui.setupUi(self)

class WF_5(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogF_5()
        self.ui.setupUi(self)

class WF_6(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogF_6()
        self.ui.setupUi(self)

class WF_7(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogF_7()
        self.ui.setupUi(self)

class WF_8(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogF_8()
        self.ui.setupUi(self)

class WF_9(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogF_9()
        self.ui.setupUi(self)

class WF_10(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogF_10()
        self.ui.setupUi(self)

class WF_11(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogF_11()
        self.ui.setupUi(self)

class WR_1(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogR_1()
        self.ui.setupUi(self)

class WR_2(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogR_2()
        self.ui.setupUi(self)

class WR_3(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogR_3()
        self.ui.setupUi(self)

class WR_4(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogR_4()
        self.ui.setupUi(self)

class WDiag_1(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogDiag1()
        self.ui.setupUi(self)

class WDiag_2(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogDiag2()
        self.ui.setupUi(self)

class WDiag_3(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogDiag3()
        self.ui.setupUi(self)

class WDiag_4(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogDiag4()
        self.ui.setupUi(self)

class WDiag_5(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogDiag5()
        self.ui.setupUi(self)

class WDiag_6(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogDiag6()
        self.ui.setupUi(self)

class WDiag_7(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogDiag7()
        self.ui.setupUi(self)

class MainWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Кнопки для подпятников
        self.ui.pushButton_1_1.clicked.connect(self.op1_1)
        self.ui.pushButton_1_2.clicked.connect(self.op1_2)
        self.ui.pushButton_2_1.clicked.connect(self.op2_1)
        self.ui.pushButton_2_2.clicked.connect(self.op2_2)
        self.ui.pushButton_3_1.clicked.connect(self.op3_1)
        self.ui.pushButton_3_2.clicked.connect(self.op3_2)
        self.ui.pushButton_3_3.clicked.connect(self.op3_3)
        self.ui.pushButton_3_4.clicked.connect(self.op3_4)
        self.ui.pushButton_4_1.clicked.connect(self.op4_1)
        self.ui.pushButton_4_2.clicked.connect(self.op4_2)
        self.ui.pushButton_4_3.clicked.connect(self.op4_3)
        self.ui.pushButton_5_1.clicked.connect(self.op5_1)
        self.ui.pushButton_6_1.clicked.connect(self.op6_1)
        self.ui.pushButton_6_2.clicked.connect(self.op6_2)
        self.ui.pushButton_9_1.clicked.connect(self.op9_1)
        self.ui.pushButton_F1.clicked.connect(self.opF_1)
        self.ui.pushButton_F2.clicked.connect(self.opF_2)
        self.ui.pushButton_F3.clicked.connect(self.opF_3)
        self.ui.pushButton_F4.clicked.connect(self.opF_4)
        self.ui.pushButton_F5.clicked.connect(self.opF_5)
        self.ui.pushButton_F6.clicked.connect(self.opF_6)
        self.ui.pushButton_F7.clicked.connect(self.opF_7)
        self.ui.pushButton_F8.clicked.connect(self.opF_8)
        self.ui.pushButton_F9.clicked.connect(self.opF_9)
        self.ui.pushButton_F10.clicked.connect(self.opF_10)
        self.ui.pushButton_F11.clicked.connect(self.opF_11)
        self.ui.pushButton_R1.clicked.connect(self.opR_1)
        self.ui.pushButton_R2.clicked.connect(self.opR_2)
        self.ui.pushButton_R3.clicked.connect(self.opR_3)
        self.ui.pushButton_R4.clicked.connect(self.opR_4)
        self.ui.pushButton_lev.clicked.connect(self.oplev)
        self.ui.pushButton_frame.clicked.connect(self.opframe)
        self.ui.pushButton_diag1.clicked.connect(self.opDiag1)
        self.ui.pushButton_diag2.clicked.connect(self.opDiag2)
        self.ui.pushButton_diag3.clicked.connect(self.opDiag3)
        self.ui.pushButton_diag4.clicked.connect(self.opDiag4)
        self.ui.pushButton_diag5.clicked.connect(self.opDiag5)
        self.ui.pushButton_diag6.clicked.connect(self.opDiag6)
        self.ui.pushButton_diag7.clicked.connect(self.opDiag7)

    def op1_1 (self):
        if __name__ == "__main__":
            global win_list
            w1_1 = W1_1()
            w1_1.show()
            win_list.append(w1_1)

    def op1_2 (self):
        if __name__ == "__main__":
            global win_list
            w1_2 = W1_2()
            w1_2.show()
            win_list.append(w1_2)

    def op2_1 (self):
        if __name__ == "__main__":
            global win_list
            w2_1 = W2_1()
            w2_1.show()
            win_list.append(w2_1)

    def op2_2 (self):
        if __name__ == "__main__":
            global win_list
            w2_2 = W2_2()
            w2_2.show()
            win_list.append(w2_2)

    def op3_1 (self):
        if __name__ == "__main__":
            global win_list
            w3_1 = W3_1()
            w3_1.show()
            win_list.append(w3_1)

    def op3_2 (self):
        if __name__ == "__main__":
            global win_list
            w3_2 = W3_2()
            w3_2.show()
            win_list.append(w3_2)

    def op3_3 (self):
        if __name__ == "__main__":
            global win_list
            w3_3 = W3_3()
            w3_3.show()
            win_list.append(w3_3)

    def op3_4 (self):
        if __name__ == "__main__":
            global win_list
            w3_4 = W3_4()
            w3_4.show()
            win_list.append(w3_4)

    def op4_1 (self):
        if __name__ == "__main__":
            global win_list
            w4_1 = W4_1()
            w4_1.show()
            win_list.append(w4_1)

    def op4_2 (self):
        if __name__ == "__main__":
            global win_list
            w4_2 = W4_2()
            w4_2.show()
            win_list.append(w4_2)

    def op4_3 (self):
        if __name__ == "__main__":
            global win_list
            w4_3 = W4_3()
            w4_3.show()
            win_list.append(w4_3)

    def op5_1 (self):
        if __name__ == "__main__":
            global win_list
            w5_1 = W5_1()
            w5_1.show()
            win_list.append(w5_1)

    def op6_1 (self):
        if __name__ == "__main__":
            global win_list
            w6_1 = W6_1()
            w6_1.show()
            win_list.append(w6_1)

    def op6_2 (self):
        if __name__ == "__main__":
            global win_list
            w6_2 = W6_2()
            w6_2.show()
            win_list.append(w6_2)

    def op9_1 (self):
        if __name__ == "__main__":
            global win_list
            w9_1 = W9_1()
            w9_1.show()
            win_list.append(w9_1)

    def opF_1 (self):
        if __name__ == "__main__":
            global win_list
            wF_1 = WF_1()
            wF_1.show()
            win_list.append(wF_1)

    def opF_2 (self):
        if __name__ == "__main__":
            global win_list
            wF_2 = WF_2()
            wF_2.show()
            win_list.append(wF_2)

    def opF_3 (self):
        if __name__ == "__main__":
            global win_list
            wF_3 = WF_3()
            wF_3.show()
            win_list.append(wF_3)

    def opF_4 (self):
        if __name__ == "__main__":
            global win_list
            wF_4 = WF_4()
            wF_4.show()
            win_list.append(wF_4)

    def opF_5 (self):
        if __name__ == "__main__":
            global win_list
            wF_5 = WF_5()
            wF_5.show()
            win_list.append(wF_5)

    def opF_6 (self):
        if __name__ == "__main__":
            global win_list
            wF_6 = WF_6()
            wF_6.show()
            win_list.append(wF_6)

    def opF_7 (self):
        if __name__ == "__main__":
            global win_list
            wF_7 = WF_7()
            wF_7.show()
            win_list.append(wF_7)

    def opF_8 (self):
        if __name__ == "__main__":
            global win_list
            wF_8 = WF_8()
            wF_8.show()
            win_list.append(wF_8)

    def opF_9 (self):
        if __name__ == "__main__":
            global win_list
            wF_9 = WF_9()
            wF_9.show()
            win_list.append(wF_9)

    def opF_10 (self):
        if __name__ == "__main__":
            global win_list
            wF_10 = WF_10()
            wF_10.show()
            win_list.append(wF_10)

    def opF_11 (self):
        if __name__ == "__main__":
            global win_list
            wF_11 = WF_11()
            wF_11.show()
            win_list.append(wF_11)

    def opR_1 (self):
        if __name__ == "__main__":
            global win_list
            wR_1 = WR_1()
            wR_1.show()
            win_list.append(wR_1)

    def opR_2 (self):
        if __name__ == "__main__":
            global win_list
            wR_2 = WR_2()
            wR_2.show()
            win_list.append(wR_2)

    def opR_3 (self):
        if __name__ == "__main__":
            global win_list
            wR_3 = WR_3()
            wR_3.show()
            win_list.append(wR_3)

    def opR_4 (self):
        if __name__ == "__main__":
            global win_list
            wR_4 = WR_4()
            wR_4.show()
            win_list.append(wR_4)

    def opDiag1 (self):
        if __name__ == "__main__":
            global win_list
            diag1 = WDiag_1()
            diag1.show()
            win_list.append(diag1)

    def opDiag2(self):
        if __name__ == "__main__":
            global win_list
            diag2 = WDiag_2()
            diag2.show()
            win_list.append(diag2)

    def opDiag3(self):
        if __name__ == "__main__":
            global win_list
            diag3 = WDiag_3()
            diag3.show()
            win_list.append(diag3)

    def opDiag4 (self):
        if __name__ == "__main__":
            global win_list
            diag4 = WDiag_4()
            diag4.show()
            win_list.append(diag4)

    def opDiag5 (self):
        if __name__ == "__main__":
            global win_list
            diag5 = WDiag_5()
            diag5.show()
            win_list.append(diag5)

    def opDiag6 (self):
        if __name__ == "__main__":
            global win_list
            diag6 = WDiag_6()
            diag6.show()
            win_list.append(diag6)

    def opDiag7 (self):
        if __name__ == "__main__":
            global win_list
            diag7 = WDiag_7()
            diag7.show()
            win_list.append(diag7)

    def oplev (self):
        if __name__ == "__main__":
            global win_list
            levelnum.show()
            myapp.hide()
            win_list.append(levelnum)

    def opframe (self):
        if __name__ == "__main__":
            global win_list
            myframeapp.show()
            myapp.hide()
            win_list.append(myframeapp)

#----------------------------------------------------------------------------------------------------------------------
#МОДУЛЬ УРОВНЕЙ
class ErrWin(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogER()
        self.ui.setupUi(self)

class ScrLevWin(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogSCSC()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(levelnum.ui.lineEdit.text())
        self.ui.lineEdit_2.setText(levelnum.ui.lineEdit_2.text())
        self.ui.lineEdit_5.setText(levelnum.ui.lineEdit_5.text())
        self.ui.lineEdit_rackwidth.setText(levelnum.ui.lineEdit_rackwidth.text())
        self.ui.textEdit.setText(levelnum.ui.textEdit.toPlainText())
        self.build_section()

    def build_section (self):
        for i in range(0,11):
            self.ui.Beam[i].hide()
            self.ui.lineEditHB[i].hide()
            self.ui.lineEditHB[i].setText(levelnum.ui.lineEditHB[i].text())
        try:
            nlev = int(levelnum.ui.lineEdit_ln.text())
            step = 540//nlev
            count = step
            if nlev in [2,3,4,5,6,7,8,9,10,11,12]:
                for i in range(0,nlev-1):
                    h = 630-count
                    self.ui.Beam[i].setGeometry(QtCore.QRect(50,h,296,56))
                    self.ui.lineEditHB[i].setGeometry(QtCore.QRect(270,h-5,50,20))
                    self.ui.Beam[i].show()
                    self.ui.lineEditHB[i].show()
                    count+=step
            else:
                if __name__ == "__main__":
                    global win_list
                    ew = ErrWin()
                    ew.show()
                    win_list.append(ew)
        except:
            if __name__ == "__main__":
                #global win_list
                ew = ErrWin()
                ew.show()
                win_list.append(ew)

class MainSecWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindowSec()
        self.ui.setupUi(self)
        # Кнопка генерации
        self.ui.pushButton_ln.clicked.connect(self.ch_image)
        # Кнопка возврата к главному меню
        self.ui.pushButton_pp.clicked.connect(self.back_to_main)
        # Кнопка вывода окна для скриншота
        self.ui.pushButton_prnt.clicked.connect(self.lev_screen)

    def ch_image (self):
        for i in range(0,11):
            self.ui.Beam[i].hide()
            self.ui.lineEditHB[i].hide()
            self.ui.lineEditHB[i].setText("")
        try:
            nlev = int(self.ui.lineEdit_ln.text())
            step = 540//nlev
            count = step
            if nlev in [2,3,4,5,6,7,8,9,10,11,12]:
                for i in range(0,nlev-1):
                    h = 530-count
                    self.ui.Beam[i].setGeometry(QtCore.QRect(50,h,296,56))
                    self.ui.lineEditHB[i].setGeometry(QtCore.QRect(270,h-5,50,20))
                    self.ui.Beam[i].show()
                    self.ui.lineEditHB[i].show()
                    count+=step
            else:
                if __name__ == "__main__":
                    global win_list
                    ew = ErrWin()
                    ew.show()
                    win_list.append(ew)
        except:
            if __name__ == "__main__":
                #global win_list
                ew = ErrWin()
                ew.show()
                win_list.append(ew)

    def lev_screen(self):
        if __name__ == "__main__":
            global win_list
            scl = ScrLevWin()
            scl.show()
            win_list.append(scl)

    def back_to_main (self):
            myapp.show()
            self.close()
#Конец модуля уровней
#----------------------------------------------------------------------------------------------------------------------
#Модуль рам

class ErrFrWin(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogFER()
        self.ui.setupUi(self)

class ScrFrWin(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DialogFRSC()
        self.ui.setupUi(self)
        self.ui.tit = 'Рама {} {} Вариант: {}'.format(myframeapp.ui.lineEdit.text(),myframeapp.ui.lineEdit_frame.text(),
                                             myframeapp.ui.lineEdit_variant.text())
        self.ui.settit(self)
        self.ui.lineEdit.setText(myframeapp.ui.lineEdit.text())
        self.ui.lineEdit_frame.setText(myframeapp.ui.lineEdit_frame.text())
        self.ui.lineEdit_variant.setText(myframeapp.ui.lineEdit_variant.text())
        self.ui.textEdit.setText(myframeapp.ui.textEdit.toPlainText())
        self.firsthor = myframeapp.firsthor
        self.count_height_pic = myframeapp.count_height_pic
        self.count_height_dim = myframeapp.count_height_dim
        self.ordinary_pic_height = (72, 54, 36)
        self.ordinary_pic_widh = (178, 134, 89)
        self.ordinary_dim_height = (40, 30, 20)
        self.count_dg1 = myframeapp.count_dg1
        self.count_dim = myframeapp.count_dim
        self.count_d1 = myframeapp.count_d1
        self.count_d2 = myframeapp.count_d2
        self.count_dg2 = myframeapp.count_dg2
        self.count_g2 = myframeapp.count_g2
        self.plushdg1 = (50, 38, 25)
        self.xdim = (145, 110, 72)
        self.plushd1 = (50, 38, 25)
        self.plushd2 = (50, 38, 25)
        self.plushdg2 = (50, 38, 25)
        self.plushg2 = (39, 30, 20)
        self.picscale = myframeapp.picscale
        self.corhg2 = (1, 1, 1)
        self.corhg2l = (5, 5, 3)
        self.huinya = myframeapp.huinya
        self.undoh = myframeapp.undoh
        self.ultracount = myframeapp.ultracount
        self.cast_frame()
        self.ui.lineEdit_d0.setText(myframeapp.ui.lineEdit_d0.text())
        for i in range(0, 60):
            self.ui.lineEdit_d1[i].setText(myframeapp.ui.lineEdit_d1[i].text())

    def rebuilt_frame (self):
        history = self.undoh
        self.undoh = []
        histend = len(history)

        for j in range (0, histend):
            if history[j] == 'dg1':
                self.add_dg1()
                self.ultracount -= 1
            elif history[j] == 'dg2':
                self.add_dg2()
                self.ultracount -= 1
            elif history[j] == 'd1':
                self.add_d1()
                self.ultracount -= 1
            elif history[j] == 'd2':
                self.add_d2()
                self.ultracount -= 1
            else:
                self.add_g2()
                self.ultracount -= 1

    def set_picture_size (self):
        if self.ultracount < 11:
            if self.picscale == 0:
                return
            else:
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 600, 230, 71))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 600, 230, 71))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(160, 630, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 0
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()
        elif self.ultracount >= 11 and self.ultracount < 16:
            if self.picscale == 1:
                return
            else:
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 620, 173, 54))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 620, 173, 54))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(120, 640, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 1
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()
        elif self.ultracount >= 16 and self.ultracount <= 25:
            if self.picscale == 2:
                return
            else:
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 635, 115, 36))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 635, 115, 36))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(80, 642, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 2
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()
        else:
            if __name__ == "__main__":
                global win_list
                ew = ErrFrWin()
                ew.show()
                win_list.append(ew)


    def add_dg1 (self):
        self.set_picture_size()
        if self.huinya:
            self.count_height_dim[self.picscale] -= self.corhg2l[self.picscale]
        self.ui.label_dg1[self.count_dg1].setGeometry(QtCore.QRect(0, self.count_height_pic[self.picscale], self.ordinary_pic_widh[self.picscale], self.ordinary_pic_height[self.picscale]))
        self.ui.lineEdit_d1[self.count_dim].setGeometry(QtCore.QRect(self.xdim[self.picscale], self.count_height_dim[self.picscale], 50, self.ordinary_dim_height[self.picscale]))
        self.ui.label_dg1[self.count_dg1].show()
        self.ui.lineEdit_d1[self.count_dim].show()
        self.count_dim += 1
        self.count_dg1 += 1
        self.count_height_dim[self.picscale] -= self.plushdg1[self.picscale]
        self.count_height_pic[self.picscale] -= self.plushdg1[self.picscale]
        self.huinya = False
        self.undoh.append('dg1')
        self.ultracount += 1

    def add_dg2 (self):
        self.set_picture_size()
        if self.huinya:
            self.count_height_dim[self.picscale] -= self.corhg2l[self.picscale]
        self.ui.label_dg2[self.count_dg2].setGeometry(QtCore.QRect(0, self.count_height_pic[self.picscale], self.ordinary_pic_widh[self.picscale], self.ordinary_pic_height[self.picscale]))
        self.ui.lineEdit_d1[self.count_dim].setGeometry(QtCore.QRect(self.xdim[self.picscale], self.count_height_dim[self.picscale], 50, self.ordinary_dim_height[self.picscale]))
        self.ui.label_dg2[self.count_dg2].show()
        self.ui.lineEdit_d1[self.count_dim].show()
        self.count_dim += 1
        self.count_dg2 += 1
        self.count_height_dim[self.picscale] -= self.plushdg2[self.picscale]
        self.count_height_pic[self.picscale] -= self.plushdg2[self.picscale]
        self.huinya = False
        self.undoh.append('dg2')
        self.ultracount += 1

    def add_d1 (self):
        self.set_picture_size()
        if self.huinya:
            self.count_height_dim[self.picscale] -= self.corhg2l[self.picscale]
        self.ui.label_d1[self.count_d1].setGeometry(QtCore.QRect(0, self.count_height_pic[self.picscale], self.ordinary_pic_widh[self.picscale], self.ordinary_pic_height[self.picscale]))
        self.ui.lineEdit_d1[self.count_dim].setGeometry(QtCore.QRect(self.xdim[self.picscale], self.count_height_dim[self.picscale], 50, self.ordinary_dim_height[self.picscale]))
        self.ui.label_d1[self.count_d1].show()
        self.ui.lineEdit_d1[self.count_dim].show()
        self.count_dim += 1
        self.count_d1 += 1
        self.count_height_dim[self.picscale] -= self.plushd1[self.picscale]
        self.count_height_pic[self.picscale] -= self.plushd1[self.picscale]
        self.huinya = False
        self.undoh.append('d1')
        self.ultracount += 1

    def add_d2 (self):
        self.set_picture_size()
        if self.huinya:
            self.count_height_dim[self.picscale] -= self.corhg2l[self.picscale]
        self.ui.label_d2[self.count_d2].setGeometry(QtCore.QRect(0, self.count_height_pic[self.picscale], self.ordinary_pic_widh[self.picscale], self.ordinary_pic_height[self.picscale]))
        self.ui.lineEdit_d1[self.count_dim].setGeometry(QtCore.QRect(self.xdim[self.picscale], self.count_height_dim[self.picscale], 50, self.ordinary_dim_height[self.picscale]))
        self.ui.label_d2[self.count_d2].show()
        self.ui.lineEdit_d1[self.count_dim].show()
        self.count_dim += 1
        self.count_d2 += 1
        self.count_height_dim[self.picscale] -= self.plushd2[self.picscale]
        self.count_height_pic[self.picscale] -= self.plushd2[self.picscale]
        self.huinya = False
        self.undoh.append('d2')
        self.ultracount += 1

    def add_g2 (self):
        self.set_picture_size()
        if not self.huinya:
            self.count_height_dim[self.picscale] += self.corhg2l[self.picscale]
            self.count_height_pic[self.picscale] += self.corhg2[self.picscale]

        self.ui.label_g2[self.count_g2].setGeometry(QtCore.QRect(0, self.count_height_pic[self.picscale],
                                                                     self.ordinary_pic_widh[self.picscale],
                                                                     self.ordinary_pic_height[self.picscale]))
        self.ui.lineEdit_d1[self.count_dim].setGeometry(
                QtCore.QRect(self.xdim[self.picscale], self.count_height_dim[self.picscale], 50, self.ordinary_dim_height[self.picscale]))
        self.ui.label_g2[self.count_g2].show()
        self.ui.lineEdit_d1[self.count_dim].show()
        self.count_dim += 1
        self.count_g2 += 1
        self.count_height_dim[self.picscale] -= self.plushg2[self.picscale]
        self.count_height_pic[self.picscale] -= self.plushg2[self.picscale]
        self.huinya = True
        self.undoh.append('g2')
        self.ultracount += 1

    def cast_frame (self):
        if self.ultracount >= 1:
            if self.ultracount < 11 and self.ultracount >= 0:

                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 600, 230, 71))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 600, 230, 71))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(160, 630, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 0
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()
            elif self.ultracount >= 11 and self.ultracount < 16:

                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 620, 173, 54))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 620, 173, 54))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(120, 640, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 1
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()
            elif self.ultracount >= 16 and self.ultracount <= 25:

                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 635, 115, 36))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 635, 115, 36))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(80, 642, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 2
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()

        else:
            pass

#Главное окно------------------------------------------------------------

class MainFrameWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindowFrame()
        self.ui.setupUi(self)
        self.firsthor = True
        self.count_height_pic = [562, 591, 616]
        self.count_height_dim = [582, 606, 626]
        self.ordinary_pic_height = (72, 54, 36)
        self.ordinary_pic_widh = (178, 134, 89)
        self.ordinary_dim_height = (40, 30, 20)
        self.count_dg1 = 0
        self.count_dim = 0
        self.count_d1 = 0
        self.count_d2 = 0
        self.count_dg2 = 0
        self.count_g2 = 0
        self.plushdg1 = (50, 38, 25)
        self.xdim = (145, 110, 72)
        self.plushd1 = (50, 38, 25)
        self.plushd2 = (50, 38, 25)
        self.plushdg2 = (50, 38, 25)
        self.plushg2 = (39, 30, 20)
        self.picscale = 0
        self.corhg2 = (1, 1, 1)
        self.corhg2l = (5, 5, 3)
        self.huinya = False
        self.undoh = []
        self.ultracount = 0
        self.dimequality = False
        # Кнопки
        self.ui.pushButton_clr.clicked.connect(self.frame_clear)
        self.ui.pushButton_nd.clicked.connect(self.disable_firsthor)
        self.ui.pushButton_dg1.clicked.connect(self.add_dg1)
        self.ui.pushButton_dg2.clicked.connect(self.add_dg2)
        self.ui.pushButton_d1.clicked.connect(self.add_d1)
        self.ui.pushButton_d2.clicked.connect(self.add_d2)
        self.ui.pushButton_g2.clicked.connect(self.add_g2)
        self.ui.pushButton_canc.clicked.connect(self.step_back)
        self.ui.pushButton_prnt.clicked.connect(self.frame_screen)
        self.ui.pushButton_pp1.clicked.connect(self.back_to_main)
        self.ui.pushButton_eqcheck.clicked.connect(self.equal_dim)
        self.ui.pushButton_sum.clicked.connect(self.make_sum_dim)

    def make_sum_dim(self):
        self.sum = 0
        try:
            for i in range(0, 60):
                if len(self.ui.lineEdit_d1[i].text()) == 0:
                    continue
                else:
                    self.sum += int(self.ui.lineEdit_d1[i].text())

            self.sum += int(self.ui.lineEdit_d0.text())
            self.ui.pushButton_sum.setText("Общая сумма\nразмеров:\n\n{}мм".format(self.sum))
        except:
            self.ui.pushButton_sum.setText("ОШИБКА\nВВОДА!")

    def rebuilt_frame(self):
        history = self.undoh
        self.undoh = []
        histend = len(history)

        for j in range (0, histend):
            if history[j] == 'dg1':
                self.add_dg1()
                self.ultracount -= 1
            elif history[j] == 'dg2':
                self.add_dg2()
                self.ultracount -= 1
            elif history[j] == 'd1':
                self.add_d1()
                self.ultracount -= 1
            elif history[j] == 'd2':
                self.add_d2()
                self.ultracount -= 1
            else:
                self.add_g2()
                self.ultracount -= 1

    def set_picture_size (self):
        if self.ultracount < 11:
            if self.picscale == 0:
                return
            else:
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 600, 230, 71))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 600, 230, 71))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(160, 630, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 0
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()
        elif self.ultracount >= 11 and self.ultracount < 16:
            if self.picscale == 1:
                return
            else:
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 620, 173, 54))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 620, 173, 54))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(120, 640, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 1
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()
        elif self.ultracount >= 16 and self.ultracount <= 25:
            if self.picscale == 2:
                return
            else:
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 635, 115, 36))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 635, 115, 36))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(80, 642, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 2
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()
        else:
            if __name__ == "__main__":
                global win_list
                ew = ErrFrWin()
                ew.show()
                win_list.append(ew)


    def frame_clear (self):
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)

        for i in range (0,30):
            self.ui.label_dg1[i].hide()
            self.ui.label_dg2[i].hide()
            self.ui.label_d1[i].hide()
            self.ui.label_d2[i].hide()
            self.ui.label_g2[i].hide()

        for i in range(0, 60):
            self.ui.lineEdit_d1[i].hide()
            self.ui.lineEdit_d1[i].setText("")
            self.ui.lineEdit_d1[i].setFont(font)

        self.ui.label_g1.setGeometry(QtCore.QRect(0, 600, 230, 71))
        self.ui.label_ng.setGeometry(QtCore.QRect(0, 600, 230, 71))
        self.ui.lineEdit_d0.setGeometry(QtCore.QRect(160, 630, 50, 20))
        self.ui.lineEdit_d0.setFont(font)
        self.ui.lineEdit_d0.setText("")
        self.picscale = 0
        self.count_height_pic = [562, 591, 616]
        self.count_height_dim = [582, 606, 625]
        self.count_dg1 = 0
        self.count_dim = 0
        self.count_d1 = 0
        self.count_d2 = 0
        self.count_dg2 = 0
        self.count_g2 = 0
        self.huinya = False
        self.undoh = []
        self.ultracount = 0
        self.dimequality = False
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../pics/thumbs/checkbox/N.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.pushButton_eqcheck.setIcon(icon7)

    def disable_firsthor (self):
        if self.firsthor:
            self.ui.label_g1.hide()
            self.firsthor = False
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("../pics/thumbs/frg1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.pushButton_nd.setIcon(icon5)
        else:
            self.ui.label_g1.show()
            self.firsthor = True
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("../pics/thumbs/frg1x.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.pushButton_nd.setIcon(icon5)

    def add_dg1 (self):
        self.set_picture_size()
        if self.huinya:
            self.count_height_dim[self.picscale] -= self.corhg2l[self.picscale]
        self.ui.label_dg1[self.count_dg1].setGeometry(QtCore.QRect(0, self.count_height_pic[self.picscale], self.ordinary_pic_widh[self.picscale], self.ordinary_pic_height[self.picscale]))
        self.ui.lineEdit_d1[self.count_dim].setGeometry(QtCore.QRect(self.xdim[self.picscale], self.count_height_dim[self.picscale], 50, self.ordinary_dim_height[self.picscale]))
        self.ui.label_dg1[self.count_dg1].show()
        self.ui.lineEdit_d1[self.count_dim].show()
        self.count_dim += 1
        self.count_dg1 += 1
        self.count_height_dim[self.picscale] -= self.plushdg1[self.picscale]
        self.count_height_pic[self.picscale] -= self.plushdg1[self.picscale]
        self.huinya = False
        self.undoh.append('dg1')
        self.ultracount += 1

    def add_dg2 (self):
        self.set_picture_size()
        if self.huinya:
            self.count_height_dim[self.picscale] -= self.corhg2l[self.picscale]
        self.ui.label_dg2[self.count_dg2].setGeometry(QtCore.QRect(0, self.count_height_pic[self.picscale], self.ordinary_pic_widh[self.picscale], self.ordinary_pic_height[self.picscale]))
        self.ui.lineEdit_d1[self.count_dim].setGeometry(QtCore.QRect(self.xdim[self.picscale], self.count_height_dim[self.picscale], 50, self.ordinary_dim_height[self.picscale]))
        self.ui.label_dg2[self.count_dg2].show()
        self.ui.lineEdit_d1[self.count_dim].show()
        self.count_dim += 1
        self.count_dg2 += 1
        self.count_height_dim[self.picscale] -= self.plushdg2[self.picscale]
        self.count_height_pic[self.picscale] -= self.plushdg2[self.picscale]
        self.huinya = False
        self.undoh.append('dg2')
        self.ultracount += 1

    def add_d1 (self):
        self.set_picture_size()
        if self.huinya:
            self.count_height_dim[self.picscale] -= self.corhg2l[self.picscale]
        self.ui.label_d1[self.count_d1].setGeometry(QtCore.QRect(0, self.count_height_pic[self.picscale], self.ordinary_pic_widh[self.picscale], self.ordinary_pic_height[self.picscale]))
        self.ui.lineEdit_d1[self.count_dim].setGeometry(QtCore.QRect(self.xdim[self.picscale], self.count_height_dim[self.picscale], 50, self.ordinary_dim_height[self.picscale]))
        self.ui.label_d1[self.count_d1].show()
        self.ui.lineEdit_d1[self.count_dim].show()
        self.count_dim += 1
        self.count_d1 += 1
        self.count_height_dim[self.picscale] -= self.plushd1[self.picscale]
        self.count_height_pic[self.picscale] -= self.plushd1[self.picscale]
        self.huinya = False
        self.undoh.append('d1')
        self.ultracount += 1

    def add_d2 (self):
        self.set_picture_size()
        if self.huinya:
            self.count_height_dim[self.picscale] -= self.corhg2l[self.picscale]
        self.ui.label_d2[self.count_d2].setGeometry(QtCore.QRect(0, self.count_height_pic[self.picscale], self.ordinary_pic_widh[self.picscale], self.ordinary_pic_height[self.picscale]))
        self.ui.lineEdit_d1[self.count_dim].setGeometry(QtCore.QRect(self.xdim[self.picscale], self.count_height_dim[self.picscale], 50, self.ordinary_dim_height[self.picscale]))
        self.ui.label_d2[self.count_d2].show()
        self.ui.lineEdit_d1[self.count_dim].show()
        self.count_dim += 1
        self.count_d2 += 1
        self.count_height_dim[self.picscale] -= self.plushd2[self.picscale]
        self.count_height_pic[self.picscale] -= self.plushd2[self.picscale]
        self.huinya = False
        self.undoh.append('d2')
        self.ultracount += 1

    def add_g2 (self):
        self.set_picture_size()
        if not self.huinya:
            self.count_height_dim[self.picscale] += self.corhg2l[self.picscale]
            self.count_height_pic[self.picscale] += self.corhg2[self.picscale]

        self.ui.label_g2[self.count_g2].setGeometry(QtCore.QRect(0, self.count_height_pic[self.picscale],
                                                                     self.ordinary_pic_widh[self.picscale],
                                                                     self.ordinary_pic_height[self.picscale]))
        self.ui.lineEdit_d1[self.count_dim].setGeometry(
                QtCore.QRect(self.xdim[self.picscale], self.count_height_dim[self.picscale], 50, self.ordinary_dim_height[self.picscale]))
        self.ui.label_g2[self.count_g2].show()
        self.ui.lineEdit_d1[self.count_dim].show()
        self.count_dim += 1
        self.count_g2 += 1
        self.count_height_dim[self.picscale] -= self.plushg2[self.picscale]
        self.count_height_pic[self.picscale] -= self.plushg2[self.picscale]
        self.huinya = True
        self.undoh.append('g2')
        self.ultracount += 1

    def step_back (self):
        if self.ultracount >= 1:
            self.ultracount -= 1
            self.undoh.pop()
            self.ui.lineEdit_d1[self.count_dim - 1].setText("")

            if self.ultracount < 11 and self.ultracount >= 0:

                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 600, 230, 71))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 600, 230, 71))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(160, 630, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 0
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()
            elif self.ultracount >= 11 and self.ultracount < 16:

                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 620, 173, 54))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 620, 173, 54))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(120, 640, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 1
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()
            elif self.ultracount >= 16 and self.ultracount <= 25:

                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)

                for i in range(0, 30):
                    self.ui.label_dg1[i].hide()
                    self.ui.label_dg2[i].hide()
                    self.ui.label_d1[i].hide()
                    self.ui.label_d2[i].hide()
                    self.ui.label_g2[i].hide()

                for i in range(0, 60):
                    self.ui.lineEdit_d1[i].hide()
                    self.ui.lineEdit_d1[i].setFont(font)

                self.ui.label_g1.setGeometry(QtCore.QRect(0, 635, 115, 36))
                self.ui.label_ng.setGeometry(QtCore.QRect(0, 635, 115, 36))
                self.ui.lineEdit_d0.setGeometry(QtCore.QRect(80, 642, 50, 20))
                self.ui.lineEdit_d0.setFont(font)
                self.picscale = 2
                self.count_height_pic = [562, 591, 616]
                self.count_height_dim = [582, 606, 625]
                self.count_dg1 = 0
                self.count_dim = 0
                self.count_d1 = 0
                self.count_d2 = 0
                self.count_dg2 = 0
                self.count_g2 = 0
                self.huinya = False
                self.rebuilt_frame()

        else:
            pass

    def equal_dim (self):
        if self.dimequality:
            for i in range(self.count_dim, 60):
                self.ui.lineEdit_d1[i].setText("")
            self.dimequality = False
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap("../pics/thumbs/checkbox/N.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.pushButton_eqcheck.setIcon(icon7)
        else:
            for i in range(1, 60):
                self.ui.lineEdit_d1[i].setText(self.ui.lineEdit_d1[0].text())
            self.dimequality = True
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap("../pics/thumbs/checkbox/Y.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.pushButton_eqcheck.setIcon(icon7)

    def frame_screen (self):
        if __name__ == "__main__":
            global win_list
            scf = ScrFrWin()
            scf.show()
            win_list.append(scf)

    def back_to_main (self):
        myapp.show()
        self.close()

#Конец модуля рам
#----------------------------------------------------------------------------------------------------------------------

win_list = []

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myframeapp = MainFrameWin()
    levelnum = MainSecWin()
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())