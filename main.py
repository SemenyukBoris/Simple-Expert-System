import sys
import json
import ast
from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox

import design
import result_design

class ResultWindow(QtWidgets.QMainWindow, result_design.Ui_resultwindow):
    def __init__(self, parent=None):

        super().__init__()
        self.setupUi(self)          
        self.test1 = []
        self.test2 = []
        self.test3 = []
        self.answer1 = []
        self.answer2 = []
        self.answer3 = []

        self.btnLoad.clicked.connect(self.load_archive)
        
    def load_archive(self):
        self.textBrowser_4.clear()
        self.date1 = self.dateEdit_start.date()
        self.date2 = self.dateEdit_end.date()
        self.string = ""
        self.format = "%d-%m-%Y"
        with open('data/archive.dat', 'r', encoding='utf-8-sig') as download:
            for line in download:
                self.string = line
                self.string = ast.literal_eval(self.string)
                self.obj = datetime.strptime(self.string[0], self.format)
                if self.obj >= self.date1 and self.obj <= self.date2:
                    self.textBrowser_4.append("<b>" + self.string[0] + " -> "  + self.string[1] + "</b>")
                    self.textBrowser_4.append(self.string[2] + " | " + self.string[3] + " | " + self.string[4])  
                    for i in range(5, len(self.string)-1):
                        # calling good procedure which make text browser like better 
                        self.archive_errors(self.string[i])



    def clear_all(self):
        self.textBrowser_1.clear()
        self.textBrowser_2.clear()
        self.textBrowser_3.clear()

    def print_all(self):
        self.flag = False
        self.index_t = 0
        self.index_a = 0
        with open('data/result1.dat','r', encoding='utf-8-sig') as res1:
            self.test1 = json.load(res1)
        with open('data/result2.dat','r', encoding='utf-8-sig') as res2:
            self.test2 = json.load(res2)
        with open('data/result3.dat','r', encoding='utf-8-sig') as res3:
            self.test3 = json.load(res3)
            
        with open('data/answer1.dat','r', encoding='utf-8-sig') as ans1:
            self.answer1 = json.load(ans1)
# ---------------------------------------------------------------------------------------------
        while True:
            if self.index_t == len(self.test1) or self.index_a == len(self.answer1):
                break
            if self.test1[self.index_t][0] == self.answer1[self.index_a][0]:
                if self.test1[self.index_t][1] == self.answer1[self.index_a][1]:
                    if self.flag == False:
                        self.textBrowser_1.append("<b>Аппаратная часть</b>\n")  
                        self.textBrowser_2.append("<b>Аппаратная часть</b>\n")  
                        self.textBrowser_3.append("<b>Аппаратная часть</b>\n")
                        font = QtGui.QFont()
                        font.setBold(False)
                        self.textBrowser_1.setFont(font)
                        self.textBrowser_2.setFont(font)
                        self.textBrowser_3.setFont(font)
                        self.flag = True
                    if self.answer1[self.index_a][2] == "":
                        self.index_t += 1
                        self.index_a = 0
                        continue
                    self.textBrowser_1.append(self.answer1[self.index_a][2])  
                    self.textBrowser_2.append(self.answer1[self.index_a][3])  
                    self.textBrowser_3.append(self.answer1[self.index_a][4])
                    self.index_t += 1
                    self.index_a = 0
                else:
                    self.index_a += 1
            else:
                self.index_a += 1
        self.textBrowser_1.append("\n")  
        self.textBrowser_2.append("\n")  
        self.textBrowser_3.append("\n")
# ---------------------------------------------------------------------------------------------
        with open('data/answer2.dat','r', encoding='utf-8-sig') as ans2:
            self.answer2 = json.load(ans2)
        self.index_t = 0
        self.index_a = 0
        self.flag = False
        while True:
            if self.index_t == len(self.test2) or self.index_a == len(self.answer2):
                break
            if self.test2[self.index_t][0] == self.answer2[self.index_a][0]:
                if self.test2[self.index_t][1] == self.answer2[self.index_a][1]:
                    if self.flag == False:
                        self.textBrowser_1.append("<b>Устройства компьютера</b>")  
                        self.textBrowser_2.append("<b>Устройства компьютера</b>")  
                        self.textBrowser_3.append("<b>Устройства компьютера</b>")
                        font = QtGui.QFont()
                        font.setBold(False)
                        self.textBrowser_1.setFont(font)
                        self.textBrowser_2.setFont(font)
                        self.textBrowser_3.setFont(font)
                        self.flag = True
                    if self.answer2[self.index_a][2] == "":
                        self.index_t += 1
                        self.index_a = 0
                        continue
                    self.textBrowser_1.append(self.answer2[self.index_a][2])  
                    self.textBrowser_2.append(self.answer2[self.index_a][3])  
                    self.textBrowser_3.append(self.answer2[self.index_a][4])
                    self.index_t += 1
                    self.index_a = 0
                else:
                    self.index_a += 1
            else:
                self.index_a += 1
        self.textBrowser_1.append("\n")  
        self.textBrowser_2.append("\n")  
        self.textBrowser_3.append("\n")
# ---------------------------------------------------------------------------------------------
        with open('data/answer3.dat','r', encoding='utf-8-sig') as ans3:
            self.answer3 = json.load(ans3)
        self.index_t = 0
        self.index_a = 0
        self.flag = False
        while True:
            if self.index_t == len(self.test3) or self.index_a == len(self.answer3):
                break
            if self.test3[self.index_t][0] == self.answer3[self.index_a][0]:
                if self.test3[self.index_t][1] == self.answer3[self.index_a][1]:
                    if self.flag == False:
                        self.textBrowser_1.append("<b>Операционная система</b>")  
                        self.textBrowser_2.append("<b>Операционная система</b>")  
                        self.textBrowser_3.append("<b>Операционная система</b>")
                        font = QtGui.QFont()
                        font.setBold(False)
                        self.textBrowser_1.setFont(font)
                        self.textBrowser_2.setFont(font)
                        self.textBrowser_3.setFont(font)
                        self.flag = True
                    if self.answer3[self.index_a][2] == "":
                        self.index_t += 1
                        self.index_a = 0
                        continue
                    self.textBrowser_1.append(self.answer3[self.index_a][2])  
                    self.textBrowser_2.append(self.answer3[self.index_a][3])  
                    self.textBrowser_3.append(self.answer3[self.index_a][4])
                    self.index_t += 1
                    self.index_a = 0
                else:
                    self.index_a += 1
            else:
                self.index_a += 1
        self.textBrowser_1.append("\n")  
        self.textBrowser_2.append("\n")  
        self.textBrowser_3.append("\n")
# ---------------------------------------------------------------------------------------------
    def archive_errors(self, para):
        self.error1 = []
        self.error2 = []
        self.error3 = []          
        with open('data/answer1.dat','r', encoding='utf-8-sig') as ans1:
            self.error1 = json.load(ans1)
        with open('data/answer2.dat','r', encoding='utf-8-sig') as ans2:
            self.error2 = json.load(ans2)
        with open('data/answer3.dat','r', encoding='utf-8-sig') as ans3:
            self.error3 = json.load(ans3)
        for i in range(0,12):
            if self.error1[i][0] == para[0]:
                if self.error1[i][1] == para[1]:
                    if self.error1[i][2] == '':
                        return
                    else:
                        self.textBrowser_4.append("   - " + self.error1[i][2])
                        return  
       
        for i in range(0,21):
            if self.error2[i][0] == para[0]:
                if self.error2[i][1] == para[1]:
                    if self.error2[i][2] == '':
                        return
                    else:
                        self.textBrowser_4.append("   - " + self.error2[i][2])
                        return 

        for i in range(0,23):
            if self.error3[i][0] == para[0]:
                if self.error3[i][1] == para[1]:
                    if self.error3[i][2] == '':
                        return
                    else:
                        self.textBrowser_4.append("   - " + self.error3[i][2])
                        return
# ---------------------------------------------------------------------------------------------
    def download_archive(self):
        self.string = ''
        self.temp_string = ''
        with open('data/archive.dat', 'r', encoding='utf-8-sig') as download:
            for line in download:
                self.string = line
                self.string = ast.literal_eval(self.string)
                self.textBrowser_4.append("<b>" + self.string[0] + "</b> "  + self.string[1] + "")
                self.textBrowser_4.append(self.string[2] + " " + self.string[3] + " " + self.string[4])  
                for i in range(5, len(self.string)-1):
                    # calling good procedure which make text browser like better 
                    self.archive_errors(self.string[i])
                    
# ---------------------------------------------------------------------------------------------
                
                
class MainWindow(QtWidgets.QMainWindow, design.Ui_test1):
    def __init__(self):

        super().__init__()

        self.setupUi(self)
        self.resultWin = None
        self.data = []
        self.test1 = []
        self.test2 = []
        self.test3 = []

        self.btnStart.clicked.connect(self.start_click)
        self.btnArchive.clicked.connect(self.archive_click)
        self.btnPage1Next.clicked.connect(self.next_click_1)
        self.btnPage1Prev.clicked.connect(self.prev_click_1)

        self.btnPage2Next.clicked.connect(self.next_click_2)
        self.btnPage2Prev.clicked.connect(self.prev_click_2)

        self.btnPage3Next.clicked.connect(self.next_click_3)
        self.btnPage3Prev.clicked.connect(self.prev_click_3)


    def start_click(self):
        self.model = self.lineEdit_1model.text()
        self.proc = self.lineEdit_2proc.text()
        self.video = self.lineEdit_3video.text()
        self.storage = self.lineEdit_4storage.text()
        self.date = self.dateEdit.date().toString('dd-MM-yyyy')
        self.data.append(self.date)
        self.data.append(self.model)
        self.data.append(self.proc)
        self.data.append(self.video)
        self.data.append(self.storage)
        if self.model == "" or self.proc == "" or self.video == "" or self.storage == "":
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.buttonReply = QMessageBox.question(self, "Ошибка ввода данных", "Все поля должны быть заполнены!", QMessageBox.Ok)
        else:
            self.stackedWidget.setCurrentIndex(1)

    def archive_click(self):
        if not self.resultWin:
            self.resultWin = ResultWindow(self)     
        self.resultWin.show()
        self.resultWin.tabWidget.setCurrentIndex(3)   
        self.resultWin.load_archive()
              
    
    def collect_test1(self):
        self.test1.clear()
# -- 1 --------------------------------------      
        if self.radioButton_11a.isChecked():
            self.test1.append(('1.1','a'))
        if self.radioButton_11b.isChecked():
            self.test1.append(('1.1','b'))
        if self.radioButton_11c.isChecked():
            self.test1.append(('1.1','c'))
        if self.radioButton_11d.isChecked():
            self.test1.append(('1.1','d'))
        if self.radioButton_11e.isChecked():
            self.test1.append(('1.1','e'))  
# -- 2 ---------------------------------------
        if self.radioButton_12a.isChecked():
            self.test1.append(('1.2','a'))
        if self.radioButton_12b.isChecked():
            self.test1.append(('1.2','b'))
        if self.radioButton_12c.isChecked():
            self.test1.append(('1.2','c'))        
# -- 3 ---------------------------------------  
        if self.radioButton_13a.isChecked():
            self.test1.append(('1.3','a'))
        if self.radioButton_13b.isChecked():
            self.test1.append(('1.3','b'))
# -- 4 ---------------------------------------
        if self.radioButton_14a.isChecked():
            self.test1.append(('1.4','a'))
        if self.radioButton_14b.isChecked():
            self.test1.append(('1.4','b'))
# -- data ------------------------------------
        self.data.extend(self.test1)
# ---list-to-file-----------------------------
        with open('data/result1.dat', 'w', encoding='utf-8-sig') as f1:
            json.dump(self.test1, f1)      

    def collect_test2(self):
        self.test2.clear()
# -- 1 ---------------------------------------
        if self.radioButton_21a.isChecked():
            self.test2.append(('2.1','a'))
        if self.radioButton_21b.isChecked():
            self.test2.append(('2.1','b'))
        if self.radioButton_21c.isChecked():
            self.test2.append(('2.1','c'))
        if self.radioButton_21d.isChecked():
            self.test2.append(('2.1','d'))
# -- 2 ---------------------------------------
        if self.radioButton_22a.isChecked():
            self.test2.append(('2.2','a'))
        if self.radioButton_22b.isChecked():
            self.test2.append(('2.2','b'))
        if self.radioButton_22c.isChecked():
            self.test2.append(('2.2','c'))
# -- 3 ---------------------------------------
        if self.radioButton_23a.isChecked():
            self.test2.append(('2.3','a'))
        if self.radioButton_23b.isChecked():
            self.test2.append(('2.3','b'))
        if self.radioButton_23c.isChecked():
            self.test2.append(('2.3','c'))
        if self.radioButton_23d.isChecked():
            self.test2.append(('2.3','d'))
# -- 4 ---------------------------------------
        if self.radioButton_24a.isChecked():
            self.test2.append(('2.4','a'))
        if self.radioButton_24b.isChecked():
            self.test2.append(('2.4','b'))
        if self.radioButton_24c.isChecked():
            self.test2.append(('2.4','c'))
        if self.radioButton_24d.isChecked():
            self.test2.append(('2.4','d'))
# -- 5 ---------------------------------------
        if self.checkBox_25a.isChecked():
            self.test2.append(('2.5','a'))
        if self.checkBox_25b.isChecked():
            self.test2.append(('2.5','b'))
        if self.checkBox_25c.isChecked():
            self.test2.append(('2.5','c'))
        if self.checkBox_25d.isChecked():
            self.test2.append(('2.5','d'))
        if self.checkBox_25e.isChecked():
            self.test2.append(('2.5','e'))
# -- data ------------------------------------
        self.data.extend(self.test2)
# ---list-to-file-----------------------------
        with open('data/result2.dat', 'w', encoding='utf-8-sig') as f2:
            json.dump(self.test2, f2)


    def collect_test3(self):
        self.test3.clear()
# -- 1 ---------------------------------------
        if self.checkBox_31a.isChecked():
            self.test3.append(('3.1','a'))
        if self.checkBox_31b.isChecked():
            self.test3.append(('3.1','b'))
        if self.checkBox_31c.isChecked():
            self.test3.append(('3.1','c'))
        if self.checkBox_31d.isChecked():
            self.test3.append(('3.1','d'))
# -- 2 ---------------------------------------
        if self.checkBox_32a.isChecked():
            self.test3.append(('3.2','a'))
        if self.checkBox_32b.isChecked():
            self.test3.append(('3.2','b'))
        if self.checkBox_32c.isChecked():
            self.test3.append(('3.2','c'))
        if self.checkBox_32d.isChecked():
            self.test3.append(('3.2','d'))
# -- 3 ---------------------------------------
        if self.checkBox_33a.isChecked():
            self.test3.append(('3.3','a'))
        if self.checkBox_33b.isChecked():
            self.test3.append(('3.3','b'))
        if self.checkBox_33c.isChecked():
            self.test3.append(('3.3','c'))
# -- 4 ---------------------------------------
        if self.checkBox_34a.isChecked():
            self.test3.append(('3.4','a'))
        if self.checkBox_34b.isChecked():
            self.test3.append(('3.4','b'))
        if self.checkBox_34c.isChecked():
            self.test3.append(('3.4','c'))
        if self.checkBox_34d.isChecked():
            self.test3.append(('3.4','d'))
# -- 5 ---------------------------------------
        if self.checkBox_35a.isChecked():
            self.test3.append(('3.5','a'))
        if self.checkBox_35b.isChecked():
            self.test3.append(('3.5','b'))
        if self.checkBox_35c.isChecked():
            self.test3.append(('3.5','c'))
        if self.checkBox_35d.isChecked():
            self.test3.append(('3.5','d'))
# -- 6 ---------------------------------------
        if self.checkBox_36a.isChecked():
            self.test3.append(('3.6','a'))
        if self.checkBox_36b.isChecked():
            self.test3.append(('3.6','b'))
        if self.checkBox_36c.isChecked():
            self.test3.append(('3.6','c'))
        if self.checkBox_36d.isChecked():
            self.test3.append(('3.6','d'))
# -- data ------------------------------------
        self.data.extend(self.test3)
# ---list-to-file-----------------------------
        with open('data/result3.dat', 'w', encoding='utf-8-sig') as f3:
            json.dump(self.test3,f3)

# --------------------------------------------            
    def next_click_1(self):
        self.collect_test1()
        self.stackedWidget.setCurrentIndex(2)

    def prev_click_1(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def next_click_2(self):
        self.collect_test2()
        self.stackedWidget.setCurrentIndex(3)

    def prev_click_2(self):
        self.stackedWidget.setCurrentIndex(1)

    def prev_click_3(self):
        self.stackedWidget.setCurrentIndex(2)

    def next_click_3(self):
        self.collect_test3()
        with open('data/archive.dat', 'a', encoding='utf-8-sig') as arch:                
            arch.write(str(self.data) + '\n')
        self.open_result()
        
    def open_result(self):
        if not self.resultWin:
            self.resultWin = ResultWindow(self)
        self.resultWin.show()
        self.resultWin.tabWidget.setCurrentIndex(0)  
        self.resultWin.clear_all()
        self.resultWin.print_all()
        #self.resultWin.download_archive()

def main():
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
    

