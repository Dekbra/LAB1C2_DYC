from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout)
from PyQt5.QtCore import Qt  # Para definir las alineaciones
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NOMBRE")

        #Widget central
        central = QWidget()

        #Creamos los layouts
        vlayout = QVBoxLayout()

        #Creamos los widgets
        self.labelName = QLabel("Nombre: Diego Cabrera")
        self.labelAge = QLabel("Edad: 19 años")  

        # Centramos los widgets
        self.labelName.setAlignment(Qt.AlignCenter)
        self.labelAge.setAlignment(Qt.AlignCenter)

        #Agregamos los widgets al layout
        vlayout.addWidget(self.labelName)
        vlayout.addWidget(self.labelAge)

        central.setLayout(vlayout)
        self.setCentralWidget(central)

app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()
