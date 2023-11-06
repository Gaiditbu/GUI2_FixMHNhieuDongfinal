# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FRSA.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
import webbrowser

# thư viện tự định nghĩa
#from packagename import Classname
from ClassRSA import *
from ClassREADWRITE import *
from ClassDialogBox import *

#import ui form
from FCeasar import *
from FVigenere import *
from FTrithemius import *
from FBelasco import *
from FMotdong import *
from FNhieudong import *
from FXORCeasar import *
from FXORVigenere import *
from FXORTrithemius import *
from FXORBelasco import *


class Ui_WRSA(object):
    def setupUi(self, WRSA):

        # khai biến trong Class để xử lý
        self.path = ''  # biến lưu đường dẫn
        self.ListContent = []  # mảng lưu toàn bộ nội dung đọc dc từ file
        self.strContent = ''  # biến dùng để đổi kiểu dữ liệu từ list qua str
        self.p = ''
        self.c = ''
        self.kD = 0
        self.kE = 0
        self.kN = 0
        self.clickedcounter=0 #biến lưu số lần bấm btn

        WRSA.setObjectName("WRSA")
        WRSA.resize(1086, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("tainguyen/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WRSA.setWindowIcon(icon)
        WRSA.setStyleSheet("\n"
"color:black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #F6BE5E, stop:0.25 #F8C976, stop:0.5 #FAD794, stop:0.75 #FCE3B4, stop:1 #FDF1D4);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WRSA)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 541, 111))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(33)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font-size: 20px;\n"
"font: 75 33pt \"Montserrat\";\n"
"\n"
"border: 3px solid #0099FF;\n"
"border-radius: 20px;\n"
"color:black;\n"
"\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Btn_ReadFile = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_ReadFile.setGeometry(QtCore.QRect(870, 150, 191, 71))
        self.Btn_ReadFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_ReadFile.setMouseTracking(False)
        self.Btn_ReadFile.setTabletTracking(False)
        self.Btn_ReadFile.setAutoFillBackground(False)
        self.Btn_ReadFile.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    background-color: #0099FF;\n"
"    border: 3px solid #FF9933;\n"
"    font: 75 16pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    border-color:#0099FF ;\n"
"    color: black;\n"
"}\n"
"")
        self.Btn_ReadFile.setObjectName("Btn_ReadFile")
        self.Btn_MaHoa = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_MaHoa.setGeometry(QtCore.QRect(870, 240, 191, 71))
        self.Btn_MaHoa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_MaHoa.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    background-color: #0099FF;\n"
"    border: 3px solid #FF9933;\n"
"    font: 75 16pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    border-color:#0099FF ;\n"
"    color: black;\n"
"}\n"
"")
        self.Btn_MaHoa.setObjectName("Btn_MaHoa")
        self.Btn_GiaiMa = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_GiaiMa.setGeometry(QtCore.QRect(870, 340, 191, 71))
        self.Btn_GiaiMa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_GiaiMa.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    background-color: #0099FF;\n"
"    border: 3px solid #FF9933;\n"
"    font: 75 16pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    border-color:#0099FF ;\n"
"    color: black;\n"
"}\n"
"")
        self.Btn_GiaiMa.setObjectName("Btn_GiaiMa")
        self.tbPath = QtWidgets.QLineEdit(self.centralwidget)
        self.tbPath.setGeometry(QtCore.QRect(20, 150, 811, 71))
        font = QtGui.QFont()
        font.setFamily("Bebas Nueue123")
        font.setPointSize(12)
        self.tbPath.setFont(font)
        self.tbPath.setStyleSheet("background-color:white;\n"
"border-radius:20px;\n"
"color:black;\n"
"font: 12pt \"Bebas Nueue123\";\n"
"border: 3px solid #FF9933;")
        self.tbPath.setText("")
        self.tbPath.setMaxLength(32782)
        self.tbPath.setFrame(True)
        self.tbPath.setClearButtonEnabled(False)
        self.tbPath.setObjectName("tbPath")
        self.tbNoiDung = QtWidgets.QTextEdit(self.centralwidget)
        self.tbNoiDung.setGeometry(QtCore.QRect(20, 240, 811, 171))
        font = QtGui.QFont()
        font.setFamily("Bebas Nueue123")
        font.setPointSize(12)
        self.tbNoiDung.setFont(font)
        self.tbNoiDung.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tbNoiDung.setStyleSheet("QTextEdit {\n"
"    padding-top: 10px;\n"
"    padding-bottom: 10px;\n"
"    background-color: white;\n"
"    font: 12pt \"Bebas Nueue123\";\n"
"    border-radius: 20px;\n"
"    color: black;\n"
"    border: 3px solid #FF9933;\n"
"}\n"
"")
        self.tbNoiDung.setObjectName("tbNoiDung")
        self.tbKetQua = QtWidgets.QTextEdit(self.centralwidget)
        self.tbKetQua.setGeometry(QtCore.QRect(20, 550, 811, 181))
        font = QtGui.QFont()
        font.setFamily("Bebas Nueue123")
        font.setPointSize(12)
        self.tbKetQua.setFont(font)
        self.tbKetQua.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tbKetQua.setStyleSheet("QTextEdit {\n"
"    padding-top: 10px;\n"
"    padding-bottom: 10px;\n"
"    background-color: white;\n"
"    font: 12pt \"Bebas Nueue123\";\n"
"    border-radius: 20px;\n"
"    color: black;\n"
"    border: 3px solid #FF9933;\n"
"}\n"
"")
        self.tbKetQua.setObjectName("tbKetQua")
        self.Btn_Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Clear.setGeometry(QtCore.QRect(870, 550, 191, 81))
        self.Btn_Clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_Clear.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    background-color: #0099FF;\n"
"    border: 3px solid #FF9933;\n"
"    font: 75 16pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    border-color:#0099FF ;\n"
"    color: black;\n"
"}\n"
"")
        self.Btn_Clear.setObjectName("Btn_Clear")
        self.Btn_WriteFile = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_WriteFile.setGeometry(QtCore.QRect(870, 650, 191, 81))
        self.Btn_WriteFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_WriteFile.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    background-color: #0099FF;\n"
"    border: 3px solid #FF9933;\n"
"    font: 75 16pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    border-color:#0099FF ;\n"
"    color: black;\n"
"}\n"
"")
        self.Btn_WriteFile.setObjectName("Btn_WriteFile")
        #==================================================================================
        self.label_e = QtWidgets.QLabel(self.centralwidget)
        self.label_e.setGeometry(QtCore.QRect(15, 440, 110, 71))
        self.label_e.setStyleSheet("border-radius:20px;\n"
"background-color:#0099FF;\n"
"border: 3px solid #FF9933;\n"
"font: 75 16pt \"Montserrat\";\n"
"")
        self.label_e.setAlignment(QtCore.Qt.AlignCenter)
        self.label_e.setObjectName("label_e")
        #==================================================================================
        self.tbKeyE = QtWidgets.QLineEdit(self.centralwidget)
        self.tbKeyE.setGeometry(QtCore.QRect(133, 440, 150, 71))
        font = QtGui.QFont()
        font.setFamily("Bebas Nueue123")
        font.setPointSize(12)
        self.tbKeyE.setFont(font)
        self.tbKeyE.setStyleSheet("background-color:white;\n"
"border-radius:20px;\n"
"color:black;\n"
"font: 12pt \"Bebas Nueue123\";\n"
"border: 3px solid #FF9933;")
        self.tbKeyE.setText("")
        self.tbKeyE.setMaxLength(32782)
        self.tbKeyE.setFrame(True)
        self.tbKeyE.setClearButtonEnabled(False)
        self.tbKeyE.setObjectName("tbKeyE")
        #===================================================================================
        self.label_d = QtWidgets.QLabel(self.centralwidget)
        self.label_d.setGeometry(QtCore.QRect(290, 440, 110, 71))
        self.label_d.setStyleSheet("border-radius:20px;\n"
"background-color:#0099FF;\n"
"border: 3px solid #FF9933;\n"
"font: 75 16pt \"Montserrat\";\n"
"")
        self.label_d.setAlignment(QtCore.Qt.AlignCenter)
        self.label_d.setObjectName("label_d")

        self.tbKeyD = QtWidgets.QLineEdit(self.centralwidget)
        self.tbKeyD.setGeometry(QtCore.QRect(407, 440, 150, 71))
        font = QtGui.QFont()
        font.setFamily("Bebas Nueue123")
        font.setPointSize(12)
        self.tbKeyD.setFont(font)
        self.tbKeyD.setStyleSheet("background-color:white;\n"
"border-radius:20px;\n"
"color:black;\n"
"font: 12pt \"Bebas Nueue123\";\n"
"border: 3px solid #FF9933;")
        self.tbKeyD.setText("")
        self.tbKeyD.setMaxLength(32782)
        self.tbKeyD.setFrame(True)
        self.tbKeyD.setClearButtonEnabled(False)
        self.tbKeyD.setObjectName("tbKeyD")
        #===================================================================================
        self.label_n = QtWidgets.QLabel(self.centralwidget)
        self.label_n.setGeometry(QtCore.QRect(565, 440, 110, 71))
        self.label_n.setStyleSheet("border-radius:20px;\n"
"background-color:#0099FF;\n"
"border: 3px solid #FF9933;\n"
"font: 75 16pt \"Montserrat\";\n"
"")
        self.label_n.setAlignment(QtCore.Qt.AlignCenter)
        self.label_n.setObjectName("label_n")

        self.tbKeyN = QtWidgets.QLineEdit(self.centralwidget)
        self.tbKeyN.setGeometry(QtCore.QRect(683, 440, 150, 71))
        font = QtGui.QFont()
        font.setFamily("Bebas Nueue123")
        font.setPointSize(12)
        self.tbKeyN.setFont(font)
        self.tbKeyN.setStyleSheet("background-color:white;\n"
"border-radius:20px;\n"
"color:black;\n"
"font: 12pt \"Bebas Nueue123\";\n"
"border: 3px solid #FF9933;")
        self.tbKeyN.setText("")
        self.tbKeyN.setMaxLength(32782)
        self.tbKeyN.setFrame(True)
        self.tbKeyN.setClearButtonEnabled(False)
        self.tbKeyN.setObjectName("tbKeyN")
        #===========================================================================
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(870, 440, 191, 71))
        self.label_2.setStyleSheet("border-radius:20px;\n"
"background-color:#0099FF;\n"
"border: 3px solid #FF9933;\n"
"font: 75 16pt \"Montserrat\";\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        #==============================================================================
        WRSA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WRSA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 20))
        self.menubar.setStyleSheet("QMenuBar {\n"
"    background-color: #F0F0F0;\n"
"    font: bold 12px;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    spacing: 3px;\n"
"    padding: 2px 10px;\n"
"    background-color: #F0F0F0;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #0099FF;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QMenuBar::item:hover {\n"
"    background-color: white;\n"
"}\n"
"")
        self.menubar.setObjectName("menubar")
        self.menuM_h_a = QtWidgets.QMenu(self.menubar)
        self.menuM_h_a.setObjectName("menuM_h_a")
        self.menuThayThe = QtWidgets.QMenu(self.menuM_h_a)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../tainguyen/encrypt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuThayThe.setIcon(icon1)
        self.menuThayThe.setObjectName("menuThayThe")
        self.menuChuyenVi = QtWidgets.QMenu(self.menuM_h_a)
        self.menuChuyenVi.setIcon(icon1)
        self.menuChuyenVi.setObjectName("menuChuyenVi")
        self.menuXOR = QtWidgets.QMenu(self.menuM_h_a)
        self.menuXOR.setIcon(icon1)
        self.menuXOR.setObjectName("menuXOR")
        self.menuT_p = QtWidgets.QMenu(self.menubar)
        self.menuT_p.setObjectName("menuT_p")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        WRSA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WRSA)
        self.statusbar.setObjectName("statusbar")
        WRSA.setStatusBar(self.statusbar)
        self.menuExit = QtWidgets.QAction(WRSA)
        self.menuExit.setObjectName("menuExit")
        self.menuOpen = QtWidgets.QAction(WRSA)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../tainguyen/openfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuOpen.setIcon(icon2)
        self.menuOpen.setIconVisibleInMenu(True)
        self.menuOpen.setObjectName("menuOpen")
        self.menuSave = QtWidgets.QAction(WRSA)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../tainguyen/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSave.setIcon(icon3)
        self.menuSave.setObjectName("menuSave")
        self.menuWebsite = QtWidgets.QAction(WRSA)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../tainguyen/global.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuWebsite.setIcon(icon4)
        self.menuWebsite.setObjectName("menuWebsite")
        self.menuAbout = QtWidgets.QAction(WRSA)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../tainguyen/aboutus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAbout.setIcon(icon5)
        self.menuAbout.setObjectName("menuAbout")
        self.actionVignere = QtWidgets.QAction(WRSA)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../tainguyen/encrypt1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVignere.setIcon(icon6)
        self.actionVignere.setObjectName("actionVignere")
        self.actionTrithemius = QtWidgets.QAction(WRSA)
        self.actionTrithemius.setIcon(icon6)
        self.actionTrithemius.setObjectName("actionTrithemius")
        self.actionBelasco = QtWidgets.QAction(WRSA)
        self.actionBelasco.setIcon(icon6)
        self.actionBelasco.setObjectName("actionBelasco")
        self.actionMotdong = QtWidgets.QAction(WRSA)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../tainguyen/Arrow1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMotdong.setIcon(icon7)
        self.actionMotdong.setObjectName("actionMotdong")
        self.actionNhieudong = QtWidgets.QAction(WRSA)
        self.actionNhieudong.setIcon(icon7)
        self.actionNhieudong.setObjectName("actionNhieudong")
        self.actionXOR_Ceasar = QtWidgets.QAction(WRSA)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../tainguyen/xor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionXOR_Ceasar.setIcon(icon8)
        self.actionXOR_Ceasar.setObjectName("actionXOR_Ceasar")
        self.actionXOR_Vignere = QtWidgets.QAction(WRSA)
        self.actionXOR_Vignere.setIcon(icon8)
        self.actionXOR_Vignere.setObjectName("actionXOR_Vignere")
        self.actionXOR_Trithemius = QtWidgets.QAction(WRSA)
        self.actionXOR_Trithemius.setIcon(icon8)
        self.actionXOR_Trithemius.setObjectName("actionXOR_Trithemius")
        self.actionXOR_Belasco = QtWidgets.QAction(WRSA)
        self.actionXOR_Belasco.setIcon(icon8)
        self.actionXOR_Belasco.setObjectName("actionXOR_Belasco")
        self.actionTho_t = QtWidgets.QAction(WRSA)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../tainguyen/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTho_t.setIcon(icon9)
        self.actionTho_t.setObjectName("actionTho_t")
        self.actionCeasar = QtWidgets.QAction(WRSA)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../../tainguyen/encrypt1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCeasar.setIcon(icon10)
        self.actionCeasar.setObjectName("actionCeasar")
        self.menuThayThe.addAction(self.actionCeasar)
        self.menuThayThe.addSeparator()
        self.menuThayThe.addAction(self.actionVignere)
        self.menuThayThe.addSeparator()
        self.menuThayThe.addAction(self.actionTrithemius)
        self.menuThayThe.addSeparator()
        self.menuThayThe.addAction(self.actionBelasco)
        self.menuChuyenVi.addAction(self.actionMotdong)
        self.menuChuyenVi.addSeparator()
        self.menuChuyenVi.addAction(self.actionNhieudong)
        self.menuXOR.addAction(self.actionXOR_Vignere)
        self.menuXOR.addSeparator()
        self.menuXOR.addAction(self.actionXOR_Trithemius)
        self.menuXOR.addSeparator()
        self.menuXOR.addAction(self.actionXOR_Belasco)
        self.menuM_h_a.addAction(self.menuThayThe.menuAction())
        self.menuM_h_a.addSeparator()
        self.menuM_h_a.addAction(self.menuChuyenVi.menuAction())
        self.menuM_h_a.addSeparator()
        self.menuM_h_a.addAction(self.menuXOR.menuAction())
        self.menuT_p.addAction(self.menuOpen)
        self.menuT_p.addSeparator()
        self.menuT_p.addAction(self.menuSave)
        self.menuT_p.addSeparator()
        self.menuT_p.addAction(self.actionTho_t)
        self.menuHelp.addAction(self.menuWebsite)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.menuAbout)
        self.menubar.addAction(self.menuT_p.menuAction())
        self.menubar.addAction(self.menuM_h_a.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(WRSA)
        QtCore.QMetaObject.connectSlotsByName(WRSA)

    def retranslateUi(self, WRSA):
        _translate = QtCore.QCoreApplication.translate
        WRSA.setWindowTitle(_translate("WRSA", "WRSA"))
        self.label.setText(_translate("WRSA", "MÃ HÓA RSA"))
        self.Btn_ReadFile.setText(_translate("WRSA", "Đọc File"))
        self.Btn_MaHoa.setText(_translate("WRSA", "Mã hóa"))
        self.Btn_GiaiMa.setText(_translate("WRSA", "Giải mã"))
        self.tbNoiDung.setHtml(_translate("WRSA", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bebas Nueue123\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Btn_Clear.setText(_translate("WRSA", "Clear"))
        self.Btn_WriteFile.setText(_translate("WRSA", "Export"))
        self.label_2.setText(_translate("WRSA", "Key"))
        self.menuM_h_a.setTitle(_translate("WRSA", "Mã hóa"))
        self.menuThayThe.setTitle(_translate("WRSA", "Thay Thế"))
        self.menuChuyenVi.setTitle(_translate("WRSA", "Chuyển Vị"))
        self.menuXOR.setTitle(_translate("WRSA", "XOR"))
        self.menuT_p.setTitle(_translate("WRSA", "Tệp"))
        self.menuHelp.setTitle(_translate("WRSA", "Help"))
        self.menuExit.setText(_translate("WRSA", "Thoát"))
        self.menuOpen.setText(_translate("WRSA", "Open"))
        self.menuOpen.setShortcut(_translate("WRSA", "Ctrl+O"))
        self.menuSave.setText(_translate("WRSA", "Save"))
        self.menuSave.setShortcut(_translate("WRSA", "Ctrl+S"))
        self.menuWebsite.setText(_translate("WRSA", "Website"))
        self.menuAbout.setText(_translate("WRSA", "About us"))
        self.actionVignere.setText(_translate("WRSA", "Vignere"))
        self.actionTrithemius.setText(_translate("WRSA", "Trithemius"))
        self.actionBelasco.setText(_translate("WRSA", "Belasco"))
        self.actionMotdong.setText(_translate("WRSA", "Trên 01 Dòng"))
        self.actionNhieudong.setText(_translate("WRSA", "Trên Nhiều  Dòng"))
        self.actionXOR_Ceasar.setText(_translate("WRSA", "XOR Ceasar"))
        self.actionXOR_Vignere.setText(_translate("WRSA", "XOR Vignere"))
        self.actionXOR_Trithemius.setText(_translate("WRSA", "XOR Trithemius"))
        self.actionXOR_Belasco.setText(_translate("WRSA", "XOR Belasco"))
        self.actionTho_t.setText(_translate("WRSA", "Thoát"))
        self.actionCeasar.setText(_translate("WRSA", "Ceasar"))
        self.label_e.setText(_translate("WRSA", "Khóa E"))
        self.label_d.setText(_translate("WRSA", "Khóa D"))
        self.label_n.setText(_translate("WRSA", "Khóa N"))

        # viết các hàm chức năng - button clicked

        self.Btn_GiaiMa.clicked.connect(self.FGiaiMa)
        self.Btn_MaHoa.clicked.connect(self.FMaHoa)
        self.Btn_Clear.clicked.connect(self.FClear)

        self.Btn_ReadFile.clicked.connect(self.FGetPath)
        self.Btn_WriteFile.clicked.connect(self.FWrite)

        # viết các hàm chức năng - menubar
        #menu mã hoá
        self.actionCeasar.triggered.connect(self.formCeasar)
        self.actionVignere.triggered.connect(self.formVignere)
        self.actionTrithemius.triggered.connect(self.formTrithemius)
        self.actionBelasco.triggered.connect(self.formBelasco)
        self.actionMotdong.triggered.connect(self.formMotdong)
        self.actionNhieudong.triggered.connect(self.formNhieuDong)
        self.actionXOR_Ceasar.triggered.connect(self.formXORCeasar)
        self.actionXOR_Vignere.triggered.connect(self.formXORVignere)
        self.actionXOR_Trithemius.triggered.connect(self.formXORTrithemius)
        self.actionXOR_Belasco.triggered.connect(self.formXORBelasco)
        #menu tep
        self.actionTho_t.triggered.connect(lambda:self.FExit(Ceasarform)) #thoát
        self.menuOpen.triggered.connect(self.FGetPath)
        self.menuSave.triggered.connect(self.FWrite)
        self.menuWebsite.triggered.connect(self.FOpenweb)
        self.menuAbout.triggered.connect(self.FAbout)

        #hàm cho action bar - menubar  
        # 1/ gọi form
        # gọi cửa sổ Ceasar form
    def formCeasar(self):
        self.Ceasarform = QtWidgets.QMainWindow()
        self.ui = Ui_Ceasarform()
        self.ui.setupUi(self.Ceasarform)
        self.Ceasarform.show()

# gọi cửa sổ Vignere form
    def formVignere(self):
        self.Vignereform = QtWidgets.QMainWindow()
        self.ui = Ui_Vignereform()
        self.ui.setupUi(self.Vignereform)
        self.Vignereform.show()

# gọi cửa sổ Trithemius form
    def formTrithemius(self):
        self.Trithemiusform = QtWidgets.QMainWindow()
        self.ui = Ui_Trithemiusform()
        self.ui.setupUi(self.Trithemiusform)
        self.Trithemiusform.show()

# gọi cửa sổ Belasco form
    def formBelasco(self):
        self.Belascoform = QtWidgets.QMainWindow()
        self.ui = Ui_Belascoform()
        self.ui.setupUi(self.Belascoform)
        self.Belascoform.show()

# gọi cửa sổ Motdong form
    def formMotdong(self):
        self.motdongform = QtWidgets.QMainWindow()
        self.ui = Ui_motdongform()
        self.ui.setupUi(self.motdongform)
        self.motdongform.show()

# gọi cửa sổ Nhieudong form
    def formNhieuDong(self):
        self.Nhieudongform = QtWidgets.QMainWindow()
        self.ui = Ui_Nhieudongform()
        self.ui.setupUi(self.Nhieudongform)
        self.Nhieudongform.show()

# gọi cửa sổ XORCeasar form
    def formXORCeasar(self):
        self.XORCeasar = QtWidgets.QMainWindow()
        self.ui = Ui_XORCeasar()
        self.ui.setupUi(self.XORCeasar)
        self.XORCeasar.show()

# gọi cửa sổ XORVignere form
    def formXORVignere(self):
        self.XORVignere = QtWidgets.QMainWindow()
        self.ui = Ui_XORVignere()
        self.ui.setupUi(self.XORVignere)
        self.XORVignere.show()

# gọi cửa sổ XORTrithemius form
    def formXORTrithemius(self):
        self.XORTrithemius = QtWidgets.QMainWindow()
        self.ui = Ui_XORTrithemius()
        self.ui.setupUi(self.XORTrithemius)
        self.XORTrithemius.show()

# gọi cửa sổ XORBelasco form
    def formXORBelasco(self):
        self.XORbelascoform = QtWidgets.QMainWindow()
        self.ui = Ui_XORbelascoform()
        self.ui.setupUi(self.XORbelascoform)
        self.XORbelascoform.show()
# 2/ chức năng 
    def FOpenweb(self):
        print("Open web")
        webbrowser.open('https://thientrinhit.notion.site/M-H-a-C-i-n-V-i-Python-0f324ba86e76440f86c7a30cb89294d0') 
    def FSave(self):
        print("Fsave")
        webbrowser.open('https://thientrinhit.notion.site/M-H-a-C-i-n-V-i-Python-0f324ba86e76440f86c7a30cb89294d0') 
    def FAbout(self):
        print("FAbout")
        messagebox.showinfo("About Us"," ● Made By 3T Team \n ● Version 1.0 \n ● © Copyright 3T Team \n ● Contact us: \n    1. Email: trinhthanhthien6.ms365.com \n    2. Tel: 0377678622 \n    3. Website: thien323.top")
    def FOpen(self):
        print("FOpen")
        webbrowser.open('https://thientrinhit.notion.site/M-H-a-C-i-n-V-i-Python-0f324ba86e76440f86c7a30cb89294d0') 
    def FExit(self,Ceasarform):
        print("FExit")
        Ceasarform.hide()

# định nghĩa hàm
    def FTest(self):
        print ("Test") 
        

    def FGetPath(self):
        print("Đọc Path")
        cCPath = CPath()

        self.path = cCPath.getPath()
        self.tbPath.setText(self.path)
        print(self.path)
        if (self.path==''): #nếu chọn chức năng chọn file mà k chọn dc file nào thì nó tự gán file trắng cho đọc
              self.path='tainguyen/empty.txt'
        else:
                # đọc rồi xuất file luôn
                print("Đọc file")
                
                cREADWRITE = READWRITE(self.path, '','')
                self.ListContent = cREADWRITE.DocFile()
                strContent = ''.join(self.ListContent)  # convert list to string
                if strContent.rfind('[;] ') != -1:
                     strContentPl = strContent.split('[;] ')
                     key = strContentPl[1].split(', ')
                     self.tbNoiDung.setText(strContentPl[0])
                     self.tbKeyD.setText(key[0])
                     self.tbKeyN.setText(key[1])
                else:
                     self.tbNoiDung.setText(strContent)
                     

    def FMaHoa(self):
        # viết hàm kiểm tra nội dung phải có đầy đủ nội dung truyền vào và key thì mới mã hóa
        # key phải là số nguyên
        # này viết hàm gọi cho tiện
        # kiểm tra nội dung input trước -> kiểm tra key

        self.p = self.tbNoiDung.toPlainText()
        # print(ord(self.p))
        self.c = self.tbKetQua.toPlainText()
        self.kE = self.tbKeyE.text()
        self.kN = self.tbKeyN.text()
        print("kiểm tra nội dung input")
        if self.FKtraInput(self.p)!=0:
                messagebox.showerror("ERROR","Vui Lòng Nhập Nội Dung Cần Mã Hóa !!!")
        else:
                print("Kiểm tra khóa")
                try: 
                      self.kE = int(self.kE)
                      if self.kE <= 1:
                            self.kE = 0
                except:
                      self.kE = 0
                try: 
                      self.kN = int(self.kN)
                      if self.kN <= 1:
                            self.kN = 0
                except:
                      self.kN = 0
                if self.kE > self.kN:
                      self.kN = 0
                      self.kE = 0
                
                print('Bắt Đầu Mã hóa')
                cRSA = RSAClass(self.p, '', self.kE, 0, self.kN)
                cRSA.MaHoa()
                c1 = cRSA.c

                self.tbKeyE.setText('')
                self.kE = cRSA.e
                self.tbKeyE.setText(str(self.kE))
                self.tbKeyD.setText('')
                self.kD = cRSA.d
                self.tbKeyD.setText(str(self.kD))
                self.tbKeyN.setText('')
                self.kN = cRSA.n
                self.tbKeyN.setText(str(self.kN))
                self.c = ''
                for i in range(0, len(c1) - 1 , 1):
                     self.c = self.c + str(c1[i]) + ', '
                self.c = self.c + str(c1[-1])
                self.tbKetQua.setText('')
                self.tbKetQua.setText(self.c)
                #if self.FKtraKey(self.k) == 0:
                #        messagebox.showerror("ERROR","Vui Lòng Nhập Key Là Số Nguyên!!!")
                #else:
                #        print("bắt đầu MaHoa")
                #        # ép kiểu từ string qua int
                #        cCCeasar = CCeasar(self.p, '', int(self.k))
                #        c1 = cCCeasar.MaHoa()
                #        #print(ord(c1))
                #        # mỗi lần click giaima hoac mã hóa thì sẽ xóa khung kết quả đi
                #        self.tbKetQua.setText('')
                #        # nếu k muốn thì đóng cmt lại để nó cộng dồn
                #        self.tbKetQua.setText(c1)


    def FGiaiMa(self):
        self.c=self.tbNoiDung.toPlainText()
        #print(ord(self.c)) #chỉ nếu dùng ord thì chỉ in được char k in dc str
        self.p=self.tbKetQua.toPlainText()
        self.kD=self.tbKeyD.text()
        self.kN=self.tbKeyN.text()
        print("kiểm tra nội dung input")
        if self.FKtraInput(self.c)!=0:
                messagebox.showerror("ERROR","Vui Lòng Nhập Nội Dung Cần Giải Mã !!!")
        else:
                print("Kiểm tra khóa")
                cont = True
                #Kiểm tra C
                cArray = self.c.split(', ')
                for i in range(0, len(cArray),1):
                    try:
                        cArray[i] = int(cArray[i])
                    except:
                        messagebox.showerror("ERROR","Vãn bản mã không hợp lệ !!!")
                        cont = False
                        break
                
                #Kiểm tra Khóa
                if cont:
                    try:
                        self.kD = int(self.kD)
                        if self.kD < 1:
                             cont = False
                             messagebox.showerror("ERROR","Khóa D không hợp lệ !!!")
                    except:
                        cont = False
                        messagebox.showerror("ERROR","Khóa D phải là số nguyên dương !!!")
                if cont:
                    try:
                        self.kN = int(self.kN)
                        if self.kN < 1:
                             cont = False
                             messagebox.showerror("ERROR","Khóa N không hợp lệ !!!")
                    except:
                        cont = False
                        messagebox.showerror("ERROR","Khóa N phải là số nguyên dương !!!")
                
                if cont:
                     print('Bắt Đầu Mã hóa')
                     cRSA = RSAClass('', cArray, self.kE, self.kD, self.kN)
                     cRSA.GiaiMa()
                     self.p = cRSA.p
                     
                     self.tbKeyD.setText('')
                     self.tbKeyD.setText(str(cRSA.d))
                     self.tbKeyN.setText('')
                     self.tbKeyN.setText(str(cRSA.n))
                     self.tbKetQua.setText('')
                     self.tbKetQua.setText(self.p)
                #if self.FKtraKey(self.k) == 0:
                #        messagebox.showerror("ERROR","Vui Lòng Nhập Key Là Số Nguyên!!!")
                #else:
                        #cCCeasar = CCeasar('',self.c,int(self.k)) #do hàm Giai mã nhận đối được c nên mình phải đổi biến chéo cho nhau
                        #c1= cCCeasar.GiaiMa()
                        #print(ord(c1))
                        #mỗi lần click giaima hoac mã hóa thì sẽ xóa khung kết quả đi
                        #self.tbKetQua.setText('')
                        #nếu k muốn thì đóng cmt lại để nó cộng dồn
                        #self.tbKetQua.setText(c1)
                #print("đã xuất kết quả")
        
    def FClear(self):
        print("Bắt đầu Clear")
        self.tbKetQua.setText('')
        self.tbNoiDung.setText('')
        self.tbKeyE.setText('')
        self.tbKeyD.setText('')
        self.tbKeyN.setText('')
        self.tbPath.setText('')

    def FWrite(self): #hàm save file
        print("Kiểm tra nội dung output")
        if self.FKtraInput(self.tbKetQua.toPlainText())!=0:
                messagebox.showinfo("Information","Chưa có nội dung kết quả !!!")
        else:
                print("bắt đầu Save file")
                self.clickedcounter=self.clickedcounter+1
                print("count",self.clickedcounter)
                cREADWRITE = READWRITE(self.path, 'RSA'+'_'+str(self.kE)+'_'+str(self.kN)+'_'+str(self.clickedcounter),self.tbKetQua.toPlainText()+'[;] '+str(self.kD)+', '+str(self.kN)) #ép kiểu str cho count mình gán tên
                cREADWRITE.GhiFile()
                messagebox.showinfo("Information","Đã Lưu File Thành Công !!!")
                print("đã ghi file xong")
        
             
    def FKtraKey(self,strKey):
        # C1 ép kiểu từ str qua int rồi so sánh type number
        # vì mình k thể ép int cho 1 giá trị của chuỗi k phải là số được
        # C2 :v mà nếu là số thì chỉ cần sau ép kiểu mà giá trị tuyệt đối nó lớn hơn hoặc = 0 thì auto là số
        # uish mình đỉnh quá trời :v ahahha
        value=0
        
        try:
            value=int(strKey)
            return value
        except ValueError:
            #return False # return về cờ rồi so sánh cũng dc
            return value

    def FKtraInput(self,strInput):
        #nếu empty hoặc '' thì bắt nhập nội dung
        flag=0 # bằng 0 thì là true
        if strInput =='':
             flag=1
             return flag
        return flag
    
    def KTraOutput(self,strOutput):
        #nếu empty hoặc '' thì bắt nhập nội dung
        flag=0 # bằng 0 thì là true
        if strOutput =='':
             flag=1
             return flag
        return flag
    
    def CountClicked(self):
        self.clickedcounter += 1
        ... # Rest of slot handling


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WRSA = QtWidgets.QMainWindow()
    ui = Ui_WRSA()
    ui.setupUi(WRSA)
    WRSA.show()
    sys.exit(app.exec_())
