import sys
import numpy
import pygame
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

# Foloseste clasa din fisierul separat
from MW_Setup import *


def Normalize(val):
    return 1/(1 + numpy.exp(-val))*80


# ############################################################################### CLASA NECESARA PENTRU
# ############################################################################### CONSTRUIREA GRAFICULUI
class GraficWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        data = ui.GetVM()
        v1 = data[0]
        m1 = data[1]
        x01 = data[2]
        v2 = data[3]
        m2 = data[4]
        x02 = data[5]
        u = (m1*v1+m2*v2)/(m1+m2)
        u1 = 2*u - v1
        u2 = 2*u - v2
        Intert = (x02-x01)/(v1-v2)
        Interx = v1*Intert+x01

        self.main = QtWidgets.QWidget()
        self.setCentralWidget(self.main)
        layout = QtWidgets.QVBoxLayout(self.main)
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(dynamic_canvas)
        self.dynamic_ax = dynamic_canvas.figure.subplots()

        Arr1 = numpy.linspace(0, Intert, 5001)
        Arr2 = numpy.linspace(Intert, 2*Intert, 5001)

        self.line1, = self.dynamic_ax.plot(Arr1, v1*Arr1+x01, 'r')
        self.line2, = self.dynamic_ax.plot(Arr1, v2*Arr1+x02, 'g')
        self.line3, = self.dynamic_ax.plot(Arr2, u1*(Arr2-Intert)+Interx, 'r')
        self.line4, = self.dynamic_ax.plot(Arr2, u2*(Arr2-Intert)+Interx, 'g')
        self.line5, = self.dynamic_ax.plot(Arr2, u*(Arr2-Intert)+Interx, 'm')

        self.timer = dynamic_canvas.new_timer(1000000)
        self.timer.add_callback(self.update_canvas)
        self.timer.start()

    def update_canvas(self):
        data = ui.GetVM()
        v1 = data[0]
        m1 = data[1]
        x01 = data[2]
        v2 = data[3]
        m2 = data[4]
        x02 = data[5]
        u = (m1*v1+m2*v2)/(m1+m2)
        u1 = 2*u - v1
        u2 = 2*u - v2
        Intert = (x02-x01)/(v1-v2)
        Interx = v1*Intert+x01

        Arr1 = numpy.linspace(0, Intert, 5001)
        Arr2 = numpy.linspace(Intert, 2*Intert, 5001)

        self.line1.set_data(Arr1, v1*Arr1+x01)
        self.line2.set_data(Arr1, v2*Arr1+x02)
        self.line3.set_data(Arr2, u1*(Arr2-Intert)+Interx)
        self.line4.set_data(Arr2, u2*(Arr2-Intert)+Interx)
        self.line5.set_data(Arr2, u*(Arr2-Intert)+Interx)

        self.line1.figure.canvas.draw()
        self.line2.figure.canvas.draw()
        self.line3.figure.canvas.draw()
        self.line4.figure.canvas.draw()
        self.line5.figure.canvas.draw()


# ############################################################################### EXTINDERE A CLASEI
# ############################################################################### CU TOATE FUNCTIILE
class Functions(Ui_MainWindow):
    def setup(self):
        self.Simuleaza_Button.clicked.connect(self.SimuleazaFunction)
        self.Grafic_Button.clicked.connect(self.ConstruiesteGraficFunction)
        self.Calculeaza_Button.clicked.connect(self.CalculeazaFunction)
        self.DateExemplu_Button.clicked.connect(self.DateExempluFunction)
        self.Help_Button.clicked.connect(self.HelpFunction)

    # ########################################################################### Informatii despre functionare
    def HelpFunction(self):
        Predef_Message = "Pentru o functionare corecta:\n- masele m1 si m2 trebuie sa fie pozitive\n- pozitiile initiale x01 si x02 trebuie sa fie intre 0 si 400, x01<x02\n- a nu se exagera :)"

        msg = QMessageBox()
        msg.setWindowTitle("Ajutor")
        msg.setText(Predef_Message)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        msg.setWindowIcon(icon)

        x = msg.exec_()

    # ########################################################################### Seteaza input-uri
    def DateExempluFunction(self):
        self.lineEdit_v1.setText("5")
        self.lineEdit_m1.setText("1")
        self.lineEdit_x01.setText("30")
        self.lineEdit_v2.setText("-3")
        self.lineEdit_m2.setText("3")
        self.lineEdit_x02.setText("400")

    # ########################################################################### Obtine datele de intrare
    def GetVM(self):
        v1 = self.lineEdit_v1.text()
        m1 = self.lineEdit_m1.text()
        x01 = self.lineEdit_x01.text()
        v2 = self.lineEdit_v2.text()
        m2 = self.lineEdit_m2.text()
        x02 = self.lineEdit_x02.text()

        sw = 1
        for i in [v1, m1, x01, v2, m2, x02]:
            if i == "":
                sw = 0
        if sw == 0:
            return 0
        else:
            v1 = float(v1)
            m1 = float(m1)
            x01 = float(x01)
            v2 = float(v2)
            m2 = float(m2)
            x02 = float(x02)
            return (v1, m1, x01, v2, m2, x02)

    # ########################################################################### Calculeaza
    def CalculeazaFunction(self):
        msg = QMessageBox()
        msg.setWindowTitle("Calcul")

        data = self.GetVM()
        if data == 0:
            msg.setText("Nu exista date")

        else:
            Intert = (data[5]-data[2])/(data[0]-data[3])
            Interx = data[0]*Intert+data[2]
            message = 'Momentul ciocnirii: {}s\nPozitia ciocnirii: {}m'.format(Intert, Interx)
            msg.setText(message)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        msg.setWindowIcon(icon)
        x = msg.exec_()

    # ########################################################################### Simuleaza
    def SimuleazaFunction(self):
        data = self.GetVM()

        if data != 0:
            pygame.init()
            pygame.display.set_caption("Simulare")
            myicon = pygame.image.load("Icon.png")
            pygame.display.set_icon(myicon)
            SimWindow = pygame.display.set_mode((600, 400))
            SimWindow.fill((217, 217, 217))
            # SimClock = pygame.time.Clock()

            v1 = data[0]
            m1 = data[1]
            x1_pos = data[2]
            v2 = data[3]
            m2 = data[4]
            x2_pos = data[5]

            m1n = Normalize(m1)
            m2n = Normalize(m2)

            color1 = (255, 0, 0)
            color2 = (0, 255, 0)
            y01 = 200
            y02 = 200 + m1n-m2n

            u = (m1*v1+m2*v2)/(m1+m2)
            u1 = 2*u - v1
            u2 = 2*u - v2
            t = 0

            elastic = self.CiocnireElastica_Button.isChecked()

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                SimWindow.fill((217, 217, 217))

                pygame.draw.rect(SimWindow, color1, pygame.Rect(
                    x1_pos, y01, m1n, m1n
                ))
                pygame.draw.rect(SimWindow, color2, pygame.Rect(
                    x2_pos, y02, m2n, m2n
                ))

                t += 0.01
                if x1_pos+m1n >= x2_pos:
                    if elastic:
                        v1 = u1
                        v2 = u2
                    else:
                        v1 = v2 = u
                x1_pos += 0.01*v1
                x2_pos += 0.01*v2
                pygame.display.flip()
            pygame.quit()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Simulare")
            msg.setText("Nu exista date")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
            msg.setWindowIcon(icon)
            x = msg.exec_()

    def ConstruiesteGraficFunction(self):
        data = self.GetVM()

        if data != 0:
            qapp = QtWidgets.QApplication.instance()
            if not qapp:
                qapp = QtWidgets.QApplication(sys.argv)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
            qapp.setWindowIcon(icon)

            app = GraficWindow()
            app.setWindowTitle("Grafic")
            app.show()
            app.activateWindow()
            app.raise_()
            qapp.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Grafic")
            msg.setText("Nu exista date")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
            msg.setWindowIcon(icon)
            x = msg.exec_()


# ############################################################################### MAIN
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Functions()
    ui.setupUi(MainWindow)
    ui.setup()

    MainWindow.show()

    sys.exit(app.exec_())
