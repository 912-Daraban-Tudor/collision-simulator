import sys
import numpy
import pygame
import numpy as np
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.qt_compat import QtCore, QtWidgets
if QtCore.qVersion() >= "5.":
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class Ui_MainWindow(object):
    # ########################################################################### SETUP_UI
    def setupUi(self, MainWindow):
        # ####################################################################### MAIN WINDOW SETUP
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("FastBlocks - Simulator Ciocniri Ideale")
        MainWindow.resize(450, 470)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(False)
        MainWindow.setStyleSheet("QMainWindow{"
                                 "  background-color: qlineargradient("
                                 "      spread:pad, x1:0, y1:0, x2:1, y2:1,"
                                 "      stop:0 rgba(122, 80, 152, 255),"
                                 "      stop:1 rgba(80, 80, 161, 255));"
                                 "}")

        # ####################################################################### CENTRAL WIDGET SETUP
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QWidget{"
                                         "  background-color:"
                                         "      qlineargradient(spread:pad,"
                                         "      x1:0, y1:0, x2:1, y2:1,"
                                         "      stop:0 rgba(122, 80, 152, 255),"
                                         "      stop:1 rgba(80, 80, 161, 255));"
                                         "}"
                                         "QLabel{"
                                         "  background-color: none;"
                                         "  color: rgb(250,250,250);"
                                         "}"
                                         "QComboBox{"
                                         "  background-color: rgb(215,215,215);"
                                         "  color: rgb(25,25,25);"
                                         "}\n"
                                         "QLineEdit{\n"
                                         "  background-color: rgb(175,175,175);"
                                         "  color: rgb(25,25,25);"
                                         "  border-style: none;"
                                         "}"
                                         "QLineEdit:focus{"
                                         "  border-style: none;"
                                         "  background-color: rgb(215,215,215);"
                                         "}"
                                         "QPushButton{"
                                         "  background-color:"
                                         "      rgb(215,215,215);"
                                         "  color: rgb(25,25,25);"
                                         "  border-radius: 3px;"
                                         "}"
                                         "QPushButton:hover{"
                                         "  background-color:"
                                         "      rgb(175,175,175);"
                                         "}"
                                         "QPushButton::pressed{"
                                         "  background-color:"
                                         "      rgb(150,150,150);"
                                         "}"
                                         "QRadioButton{"
                                         "  background-color: rgba(0,0,0,0);"
                                         "  color: rgb(250,250,250);"
                                         "}")

        # ####################################################################### ELEMENTE FOLOSITE IN PROGRAM
        # ####################################################################### LABEL-URI FOLOSITE
        # ####################################################################### Title Label
        self.Title_Label = QtWidgets.QLabel(self.centralwidget)
        self.Title_Label.setGeometry(QtCore.QRect(145, 20, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Title_Label.setFont(font)
        self.Title_Label.setTextFormat(QtCore.Qt.RichText)
        self.Title_Label.setObjectName("Title_textLabel")
        self.Title_Label.setText("FastBlocks")

        # ####################################################################### v1 Label
        self.v1_label = QtWidgets.QLabel(self.centralwidget)
        self.v1_label.setGeometry(QtCore.QRect(49, 90, 52, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.v1_label.setFont(font)
        self.v1_label.setObjectName("v1_textLabel")
        self.v1_label.setText("v1 =")

        # ####################################################################### m1 Label
        self.m1_label = QtWidgets.QLabel(self.centralwidget)
        self.m1_label.setGeometry(QtCore.QRect(43, 120, 52, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.m1_label.setFont(font)
        self.m1_label.setObjectName("m1_textLabel")
        self.m1_label.setText("m1 =")

        # ####################################################################### x01 Label
        self.x01_label = QtWidgets.QLabel(self.centralwidget)
        self.x01_label.setGeometry(QtCore.QRect(40, 150, 52, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.x01_label.setFont(font)
        self.x01_label.setObjectName("x01_textLabel")
        self.x01_label.setText("x01 =")

        # ####################################################################### v2 Label
        self.v2_label = QtWidgets.QLabel(self.centralwidget)
        self.v2_label.setGeometry(QtCore.QRect(49, 180, 45, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.v2_label.setFont(font)
        self.v2_label.setObjectName("v2_textLabel")
        self.v2_label.setText("v2 =")

        # ####################################################################### m2 Label
        self.m2_label = QtWidgets.QLabel(self.centralwidget)
        self.m2_label.setGeometry(QtCore.QRect(43, 210, 52, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.m2_label.setFont(font)
        self.m2_label.setObjectName("m2_textLabel")
        self.m2_label.setText("m2 =")

        # ####################################################################### x02 Label
        self.x02_label = QtWidgets.QLabel(self.centralwidget)
        self.x02_label.setGeometry(QtCore.QRect(40, 240, 52, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.x02_label.setFont(font)
        self.x02_label.setObjectName("x02_textLabel")
        self.x02_label.setText("x02 =")

        # ####################################################################### LINE EDIT-URI FOLOSITE
        # ####################################################################### v1 LineEdit
        self.lineEdit_v1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_v1.setGeometry(QtCore.QRect(90, 90, 125, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_v1.setFont(font)
        self.lineEdit_v1.setObjectName("input_v1")

        # ####################################################################### m1 LineEdit
        self.lineEdit_m1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_m1.setGeometry(QtCore.QRect(90, 120, 125, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_m1.setFont(font)
        self.lineEdit_m1.setObjectName("input_m1")

        # ####################################################################### x01 LineEdit
        self.lineEdit_x01 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x01.setGeometry(QtCore.QRect(90, 150, 125, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_x01.setFont(font)
        self.lineEdit_x01.setObjectName("input_x01")

        # ####################################################################### v2 LineEdit
        self.lineEdit_v2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_v2.setGeometry(QtCore.QRect(90, 180, 125, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_v2.setFont(font)
        self.lineEdit_v2.setObjectName("input_v2")

        # ####################################################################### m2 LineEdit
        self.lineEdit_m2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_m2.setGeometry(QtCore.QRect(90, 210, 125, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_m2.setFont(font)
        self.lineEdit_m2.setObjectName("input_m2")

        # ####################################################################### x02 LineEdit
        self.lineEdit_x02 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x02.setGeometry(QtCore.QRect(90, 240, 125, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_x02.setFont(font)
        self.lineEdit_x02.setObjectName("input_x02")

        # ####################################################################### BUTOANE FOLOSITE
        # ####################################################################### Simuleaza_Button
        self.Simuleaza_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Simuleaza_Button.setGeometry(QtCore.QRect(40, 270, 175, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Simuleaza_Button.setFont(font)
        self.Simuleaza_Button.setObjectName("Simuleaza_Button")
        self.Simuleaza_Button.setText("Simuleaza")

        # ####################################################################### Grafic_Button
        self.Grafic_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Grafic_Button.setGeometry(QtCore.QRect(40, 310, 175, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Grafic_Button.setFont(font)
        self.Grafic_Button.setObjectName("Grafic_Button")
        self.Grafic_Button.setText("Grafic")

        # ####################################################################### Calculeaza_Button
        self.Calculeaza_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Calculeaza_Button.setGeometry(QtCore.QRect(40, 350, 175, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Calculeaza_Button.setFont(font)
        self.Calculeaza_Button.setObjectName("Calculeaza_Button")
        self.Calculeaza_Button.setText("Calculeaza")

        # ####################################################################### DebugInputs_Button
        self.DateExemplu_Button = QtWidgets.QPushButton(self.centralwidget)
        self.DateExemplu_Button.setGeometry(QtCore.QRect(60, 390, 135, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.DateExemplu_Button.setFont(font)
        self.DateExemplu_Button.setObjectName("DateExemplu_Button")
        self.DateExemplu_Button.setText("Date Exemplu")

        # ####################################################################### Help_Button
        self.Help_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Help_Button.setGeometry(QtCore.QRect(10, 10, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.Help_Button.setFont(font)
        self.Help_Button.setObjectName("Help_Button")
        self.Help_Button.setText("?")

        # ####################################################################### RADIO BUTTON-URI FOLOSITE
        # ####################################################################### Ciocnire elastica
        self.CiocnireElastica_Button = QtWidgets.QRadioButton(self.centralwidget)
        self.CiocnireElastica_Button.setGeometry(QtCore.QRect(225, 90, 205, 26))
        self.CiocnireElastica_Button.setText("Ciocnire elastica")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CiocnireElastica_Button.setFont(font)
        self.CiocnireElastica_Button.setObjectName("CiocnireElastica_Button")
        self.CiocnireElastica_Button.setChecked(True)

        # ####################################################################### Ciocnire plastica
        self.CiocnirePlastica_Button = QtWidgets.QRadioButton(self.centralwidget)
        self.CiocnirePlastica_Button.setGeometry(QtCore.QRect(225, 120, 202, 29))
        self.CiocnirePlastica_Button.setText("Ciocnire plastica")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CiocnirePlastica_Button.setFont(font)
        self.CiocnirePlastica_Button.setObjectName("CiocnirePlastica_Button")

        # ####################################################################### Formalisme
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
