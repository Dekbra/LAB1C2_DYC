from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Introduccion de Cédula y Nombre")

        #Widget central
        central = QWidget()

        # Luego Creamos los layouts
        vlayout = QVBoxLayout()

        #Creamos los widgets
        self.labelCedula = QLabel("Ingrese su número de cédula:")
        self.editCedula = QLineEdit()

        self.labelNombre = QLabel("Ingrese su nombre completo:")
        self.editNombre = QLineEdit()

        self.boton = QPushButton("Enviar")
        self.resultado = QLabel("")  # Para mostrar la cédula y el nombre ingresados :D

        # Conectar el botón para mostrar los datos ingresados
        self.boton.clicked.connect(self.mostrar_datos)

        # Agregar widgets al layout
        vlayout.addWidget(self.labelCedula)
        vlayout.addWidget(self.editCedula)
        vlayout.addWidget(self.labelNombre)
        vlayout.addWidget(self.editNombre)
        vlayout.addWidget(self.boton)
        vlayout.addWidget(self.resultado)

        central.setLayout(vlayout)
        self.setCentralWidget(central)

    def mostrar_datos(self):
        # Obtener los datos ingresados
        cedula = self.editCedula.text()
        nombre = self.editNombre.text()

        # Y esto es pel label para mostrar los datos en la misma ventana
        self.resultado.setText(f"Cédula: {cedula}\nNombre: {nombre}")

# Código para ejecutar la aplicacion.
app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()
