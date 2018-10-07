# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_resultwindow(object):
    def setupUi(self, resultwindow):
        resultwindow.setObjectName("resultwindow")
        resultwindow.resize(600, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(resultwindow.sizePolicy().hasHeightForWidth())
        resultwindow.setSizePolicy(sizePolicy)
        resultwindow.setMinimumSize(QtCore.QSize(600, 500))
        resultwindow.setMaximumSize(QtCore.QSize(600, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../diagnostic/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        resultwindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(resultwindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 560, 460))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.tab_1)
        self.textBrowser_1.setGeometry(QtCore.QRect(-1, -1, 561, 431))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_1.setFont(font)
        self.textBrowser_1.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textBrowser_1.setOverwriteMode(False)
        self.textBrowser_1.setAcceptRichText(False)
        self.textBrowser_1.setPlaceholderText("")
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(-1, -1, 561, 431))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(-1, -1, 561, 431))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(-1, 49, 559, 381))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.label.setObjectName("label")
        self.dateEdit_start = QtWidgets.QDateEdit(self.tab_4)
        self.dateEdit_start.setGeometry(QtCore.QRect(210, 10, 91, 31))
        self.dateEdit_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_start.setCalendarPopup(True)
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(310, 10, 31, 31))
        self.label_2.setObjectName("label_2")
        self.dateEdit_end = QtWidgets.QDateEdit(self.tab_4)
        self.dateEdit_end.setGeometry(QtCore.QRect(350, 10, 91, 31))
        self.dateEdit_end.setCalendarPopup(True)
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.dateEdit_end.setDateTime(QtCore.QDateTime.currentDateTime())
        self.btnLoad = QtWidgets.QPushButton(self.tab_4)
        self.btnLoad.setGeometry(QtCore.QRect(460, 10, 80, 31))
        self.btnLoad.setObjectName("btnLoad")
        self.tabWidget.addTab(self.tab_4, "")
        resultwindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(resultwindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(resultwindow)

    def retranslateUi(self, resultwindow):
        _translate = QtCore.QCoreApplication.translate
        resultwindow.setWindowTitle(_translate("resultwindow", "Результаты"))
        self.textBrowser_1.setHtml(_translate("resultwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:400;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("resultwindow", "Проблемы"))
        self.textBrowser_2.setHtml(_translate("resultwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("resultwindow", "Причины"))
        self.textBrowser_3.setHtml(_translate("resultwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("resultwindow", "Решение"))
        self.label.setText(_translate("resultwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Все диагностики в период с </span></p></body></html>"))
        self.label_2.setText(_translate("resultwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">по</span></p></body></html>"))
        self.btnLoad.setText(_translate("resultwindow", "Загрузить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("resultwindow", "Архив"))

