import sys; from pprint import pprint
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

def get_podpyatnikdict():
    try:
        with open(dict_file_path, mode='r', encoding = 'UTF-8') as dictfile:
            for line in dictfile:
                if len(line) > 10:
                    bufline = line[:-1]
                    buflist = bufline.split('|')
                    sizevalues = buflist[4].split('@')
                    manufacturer = buflist[0]
                    size = buflist[1]
                    type = buflist[2]
                    try:
                        podpyatnik_dict[manufacturer][size][type].append(sizevalues)
                    except:
                        dictitem_builder(manufacturer=manufacturer, size=size, type=type, sizevalues=sizevalues)
                    print('Загружен словарь из файла: ', dict_file_path)
                    pprint(podpyatnik_dict)
                else:
                    print('Файл словаря пуст')
                    continue
    except:
        #Сделать окно "Ошибка загрузки сохраненных данных"
        print('Ошибка загрузки словаря, файл отсутствует или поврежден')

def filelinetailconstructor(manufacturer,size,type,index,sizevalues):
    buffer = ''
    for item in sizevalues:
        buffer += item + '@'
    buffer = buffer[:-1]
    flist = '{}|{}|{}|{}|{}\n'.format(manufacturer,size,type,str(index),buffer)
    return flist

def dictitem_builder(manufacturer,size,type,sizevalues):
    variantlist = []
    typedict = {}
    sizedict = {}
    variantlist.append(sizevalues)
    try:
        podpyatnik_dict[manufacturer][size][type] = variantlist
    except:
        typedict[type] = variantlist
        try:
            podpyatnik_dict[manufacturer][size] = typedict
        except:
            sizedict[size] = typedict
            podpyatnik_dict[manufacturer] = sizedict

def get_podpyatnik_sizes(list):
    buffer = []
    for char in list:
        #если в числе стоит запятая, то берет только первую часть до запятой
        spchar = char.split(',')
        char = spchar[0]
        try:
            buffer.append(float(char))
        except:
            continue
    buffer.sort()
    try:
        x = int(buffer.pop())
        y = int(buffer.pop())
        sizes = '{}x{}'.format(x, y)
        return sizes
    except:
        return 'Без размеров'

def save_podpyatnik_to_dict(openedwindow):
    openedwindow.mainsizevalues = []
    if openedwindow.ui.lineEdit_6.text():
        openedwindow.ui.lineEdit_6.setText(openedwindow.ui.lineEdit_6.text().capitalize())
        for i in range(0,len(openedwindow.ui.lineEditlist)):
            openedwindow.mainsizevalues.append(openedwindow.ui.lineEditlist[i].text())
    else:
        return
    openedwindow.manufacturer = openedwindow.ui.lineEdit_6.text()
    openedwindow.podpyatniksize = get_podpyatnik_sizes(openedwindow.mainsizevalues)
    openedwindow.podpyatniktype = openedwindow.ui.__class__.__name__
    print('Список размеров - ',openedwindow.mainsizevalues)
    print('Производитель - ',openedwindow.manufacturer)
    print('Размер подпятника - ',openedwindow.podpyatniksize)
    print('Класс окна - ',openedwindow.podpyatniktype)
    try:
        for ss in podpyatnik_dict[openedwindow.manufacturer][openedwindow.podpyatniksize][openedwindow.podpyatniktype]:
            if openedwindow.mainsizevalues == ss:
                print('Найдены идентичные размеры в вариантах этого типа')
                is_exist = True
                break
            else:
                is_exist = False
        if not is_exist:
            podpyatnik_dict[openedwindow.manufacturer][openedwindow.podpyatniksize][openedwindow.podpyatniktype].append(openedwindow.mainsizevalues)
            print('Добавляем новый вариант имеющегося типа')
    except:
        print('Еще ничего нет,запускаю билдер')
        dictitem_builder(manufacturer=openedwindow.manufacturer, size=openedwindow.podpyatniksize,type=openedwindow.podpyatniktype,sizevalues=openedwindow.mainsizevalues)
    pprint(podpyatnik_dict)

def save_dict_to_file():
    with open(dict_file_path, mode='w', encoding = 'UTF-8') as dictfile:
        print('Открыли файл ',dict_file_path)
        for manufacturer in podpyatnik_dict:
            for size in podpyatnik_dict[manufacturer]:
                for type in podpyatnik_dict[manufacturer][size]:
                    i=0
                    for sizevalues in podpyatnik_dict[manufacturer][size][type]:
                        print('Дошли до конструктора строки')
                        line = filelinetailconstructor(manufacturer=manufacturer,size=size,type=type,index=i,sizevalues=sizevalues)
                        dictfile.write(line)
                        i+=1
                        print('Строка {} записана в файл {}'.format(line, dict_file_path))

def delete_podpyatnik(openedwindow):
    # i = 0
    # for values in podpyatnik_dict[manufacturer][size][type]:
    #     if values == sizevalues:
    #         podpyatnik_dict[manufacturer][size][type].pop(i)
    #         break
    #     i += 1
    # if len(podpyatnik_dict[manufacturer][size][type]) < 1:
    #     podpyatnik_dict[manufacturer][size].pop(type)
    # if len(podpyatnik_dict[manufacturer][size]) < 1:
    #     podpyatnik_dict[manufacturer].pop(size)
    # if len(podpyatnik_dict[manufacturer]) < 1:
    #     podpyatnik_dict.pop(manufacturer)
    # print('Удалено')
    # pprint(podpyatnik_dict)
    pass

class ShowPodpyatnik(QtWidgets.QDialog):
    def __init__(self, ui):
        QtWidgets.QWidget.__init__(self)
        self.ui = ui
        self.ui.setupUi(self)
        self.ui.saveButton.clicked.connect(self.save_on_click)
        self.ui.deleteButton.clicked.connect(self.delete_on_click)

    def save_on_click(self):
        save_podpyatnik_to_dict(self)
        save_dict_to_file()

    def delete_on_click(self):
        delete_podpyatnik(self)
        save_dict_to_file()

class ShowDiagonal(QtWidgets.QDialog):
    def __init__(self, ui):
        QtWidgets.QWidget.__init__(self)
        self.ui = ui
        self.ui.setupUi(self)

class MainWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Кнопки для подпятников
        self.ui.pushButton_1_1.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog1_1'))
        self.ui.pushButton_1_2.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog1_2'))
        self.ui.pushButton_2_1.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog2_1'))
        self.ui.pushButton_2_2.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog2_2'))
        self.ui.pushButton_3_1.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog3_1'))
        self.ui.pushButton_3_2.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog3_2'))
        self.ui.pushButton_3_3.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog3_3'))
        self.ui.pushButton_3_4.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog3_4'))
        self.ui.pushButton_4_1.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog4_1'))
        self.ui.pushButton_4_2.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog4_2'))
        self.ui.pushButton_4_3.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog4_3'))
        self.ui.pushButton_5_1.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog5_1'))
        self.ui.pushButton_6_1.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog6_1'))
        self.ui.pushButton_6_2.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog6_2'))
        self.ui.pushButton_9_1.clicked.connect(lambda: self.open_podpyatnik_window('Ui_Dialog9_1'))
        self.ui.pushButton_F1.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogF_1'))
        self.ui.pushButton_F2.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogF_2'))
        self.ui.pushButton_F3.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogF_3'))
        self.ui.pushButton_F4.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogF_4'))
        self.ui.pushButton_F5.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogF_5'))
        self.ui.pushButton_F6.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogF_6'))
        self.ui.pushButton_F7.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogF_7'))
        self.ui.pushButton_F8.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogF_8'))
        self.ui.pushButton_F9.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogF_9'))
        self.ui.pushButton_F10.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogF_10'))
        self.ui.pushButton_F11.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogF_11'))
        self.ui.pushButton_R1.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogR_1'))
        self.ui.pushButton_R2.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogR_2'))
        self.ui.pushButton_R3.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogR_3'))
        self.ui.pushButton_R4.clicked.connect(lambda: self.open_podpyatnik_window('Ui_DialogR_4'))
        self.ui.pushButton_lev.clicked.connect(self.oplev)
        self.ui.pushButton_frame.clicked.connect(self.opframe)
        self.ui.pushButton_diag1.clicked.connect(lambda: self.open_diagonal_window('Ui_DialogDiag1'))
        self.ui.pushButton_diag2.clicked.connect(lambda: self.open_diagonal_window('Ui_DialogDiag2'))
        self.ui.pushButton_diag3.clicked.connect(lambda: self.open_diagonal_window('Ui_DialogDiag3'))
        self.ui.pushButton_diag4.clicked.connect(lambda: self.open_diagonal_window('Ui_DialogDiag4'))
        self.ui.pushButton_diag5.clicked.connect(lambda: self.open_diagonal_window('Ui_DialogDiag5'))
        self.ui.pushButton_diag6.clicked.connect(lambda: self.open_diagonal_window('Ui_DialogDiag6'))
        self.ui.pushButton_diag7.clicked.connect(lambda: self.open_diagonal_window('Ui_DialogDiag7'))

    def open_podpyatnik_window(self, ui):
        if __name__ == "__main__":
            global win_list
            w1_2 = ShowPodpyatnik(ui_type_dict[ui])
            w1_2.show()
            win_list.append(w1_2)

    def open_diagonal_window(self, ui):
        if __name__ == "__main__":
            global win_list
            diag1 = ShowDiagonal(ui_type_dict[ui])
            diag1.show()
            win_list.append(diag1)

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
        self.ui.pushButton_sum.setText("Проверить сумму\nразмеров")

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
ui_type_dict = {'Ui_Dialog1_1':Ui_Dialog1_1(),
                'Ui_Dialog1_2':Ui_Dialog1_2(),
                'Ui_Dialog2_1':Ui_Dialog2_1(),
                'Ui_Dialog2_2':Ui_Dialog2_2(),
                'Ui_Dialog3_1':Ui_Dialog3_1(),
                'Ui_Dialog3_2':Ui_Dialog3_2(),
                'Ui_Dialog3_3':Ui_Dialog3_3(),
                'Ui_Dialog3_4':Ui_Dialog3_4(),
                'Ui_Dialog4_1':Ui_Dialog4_1(),
                'Ui_Dialog4_2':Ui_Dialog4_2(),
                'Ui_Dialog4_3':Ui_Dialog4_3(),
                'Ui_Dialog5_1':Ui_Dialog5_1(),
                'Ui_Dialog6_1':Ui_Dialog6_1(),
                'Ui_Dialog6_2':Ui_Dialog6_2(),
                'Ui_Dialog9_1':Ui_Dialog9_1(),
                'Ui_DialogF_1':Ui_DialogF_1(),
                'Ui_DialogF_2':Ui_DialogF_2(),
                'Ui_DialogF_3':Ui_DialogF_3(),
                'Ui_DialogF_4':Ui_DialogF_4(),
                'Ui_DialogF_5':Ui_DialogF_5(),
                'Ui_DialogF_6':Ui_DialogF_6(),
                'Ui_DialogF_7':Ui_DialogF_7(),
                'Ui_DialogF_8':Ui_DialogF_8(),
                'Ui_DialogF_9':Ui_DialogF_9(),
                'Ui_DialogF_10':Ui_DialogF_10(),
                'Ui_DialogF_11':Ui_DialogF_11(),
                'Ui_DialogR_1':Ui_DialogR_1(),
                'Ui_DialogR_2':Ui_DialogR_2(),
                'Ui_DialogR_3':Ui_DialogR_3(),
                'Ui_DialogR_4':Ui_DialogR_4(),
                'Ui_DialogDiag1':Ui_DialogDiag1(),
                'Ui_DialogDiag2':Ui_DialogDiag2(),
                'Ui_DialogDiag3':Ui_DialogDiag3(),
                'Ui_DialogDiag4':Ui_DialogDiag4(),
                'Ui_DialogDiag5':Ui_DialogDiag5(),
                'Ui_DialogDiag6':Ui_DialogDiag6(),
                'Ui_DialogDiag7':Ui_DialogDiag7()}

dict_file_path = 'ppdata.ppsf'
podpyatnik_dict = {}
get_podpyatnikdict()

win_list = []

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myframeapp = MainFrameWin()
    levelnum = MainSecWin()
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())