from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CLAVE")

        # agregamos widget central
        central = QWidget()

        #  y despues creamos los layouts
        vlayout = QVBoxLayout()

        # Creamos los widgets
        self.labelInstruction = QLabel("Introduce tu clave:")  # Instrucción fuera del campo de entrada
        self.editPassword = QLineEdit()
        self.editPassword.setEchoMode(QLineEdit.Password)  # Con el echomode ocultamos los caracteres para proteger la contraseña
        self.labelPassword = QLabel("Clave ingresada:")
        boton = QPushButton("Enviar")

        # Conectamos el botón con los edit
        boton.clicked.connect(self.mostrar_clave)

        # Agregar widgets al layout
        vlayout.addWidget(self.labelInstruction)  # Instrucción arriba del campo de entrada
        vlayout.addWidget(self.editPassword)
        vlayout.addWidget(boton)
        vlayout.addWidget(self.labelPassword)

        central.setLayout(vlayout)
        self.setCentralWidget(central)

    def mostrar_clave(self):
        # Obtener la clave ingresada y mostrarla en el label
        password = self.editPassword.text()
        self.labelPassword.setText(f"Clave ingresada: {password}")

app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()
