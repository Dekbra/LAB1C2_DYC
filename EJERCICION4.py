from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datos de Mascotas")

        #Widget central
        central = QWidget()

        # y creamos el layout principal
        vlayout = QVBoxLayout()

        # Creamos widgets para las 3 mascotas, con tres datos básicos: el nombre, la edad yyy el tipo de animal/mascota
        # Mascota 1
        self.labelMascota1 = QLabel("Mascota #1:")
        self.labelNombre1 = QLabel("Nombre:")
        self.editNombre1 = QLineEdit()
        self.labelEdad1 = QLabel("Edad:")
        self.editEdad1 = QLineEdit()
        self.labelTipo1 = QLabel("Tipo de mascota:")
        self.editTipo1 = QLineEdit()

        # mascota 2
        self.labelMascota2 = QLabel("Mascota #2:")
        self.labelNombre2 = QLabel("Nombre:")
        self.editNombre2 = QLineEdit()
        self.labelEdad2 = QLabel("Edad:")
        self.editEdad2 = QLineEdit()
        self.labelTipo2 = QLabel("Tipo de mascota:")
        self.editTipo2 = QLineEdit()

        # mascota 3
        self.labelMascota3 = QLabel("Mascota #3:")
        self.labelNombre3 = QLabel("Nombre:")
        self.editNombre3 = QLineEdit()
        self.labelEdad3 = QLabel("Edad:")
        self.editEdad3 = QLineEdit()
        self.labelTipo3 = QLabel("Tipo de mascota:")
        self.editTipo3 = QLineEdit()

        # Botón para mostrar los datos ingresados
        self.boton = QPushButton("Enviar")
        self.resultado = QLabel("")  # Etiqueta para mostrar los resultados

        # Conectar el botón para mostrar los datos
        self.boton.clicked.connect(self.mostrar_datos)

        # Añadimos los widgets de cada mascota al layout :D
        # Mascota 1
        vlayout.addWidget(self.labelMascota1)
        vlayout.addWidget(self.labelNombre1)
        vlayout.addWidget(self.editNombre1)
        vlayout.addWidget(self.labelEdad1)
        vlayout.addWidget(self.editEdad1)
        vlayout.addWidget(self.labelTipo1)
        vlayout.addWidget(self.editTipo1)

        # mascota 2
        vlayout.addWidget(self.labelMascota2)
        vlayout.addWidget(self.labelNombre2)
        vlayout.addWidget(self.editNombre2)
        vlayout.addWidget(self.labelEdad2)
        vlayout.addWidget(self.editEdad2)
        vlayout.addWidget(self.labelTipo2)
        vlayout.addWidget(self.editTipo2)

        # mascota 3
        vlayout.addWidget(self.labelMascota3)
        vlayout.addWidget(self.labelNombre3)
        vlayout.addWidget(self.editNombre3)
        vlayout.addWidget(self.labelEdad3)
        vlayout.addWidget(self.editEdad3)
        vlayout.addWidget(self.labelTipo3)
        vlayout.addWidget(self.editTipo3)

        # Botón y resultado
        vlayout.addWidget(self.boton)
        vlayout.addWidget(self.resultado)

        central.setLayout(vlayout)
        self.setCentralWidget(central)

    def mostrar_datos(self):
        # Obtener los datos ingresados de las tres mascotas
        nombre1 = self.editNombre1.text()
        edad1 = self.editEdad1.text()
        tipo1 = self.editTipo1.text()

        nombre2 = self.editNombre2.text()
        edad2 = self.editEdad2.text()
        tipo2 = self.editTipo2.text()

        nombre3 = self.editNombre3.text()
        edad3 = self.editEdad3.text()
        tipo3 = self.editTipo3.text()

        # Mostrar los datos en el label resultado
        self.resultado.setText(f"Mascota 1:\nNombre: {nombre1}, Edad: {edad1}, Tipo: {tipo1}\n\n"
                               f"Mascota 2:\nNombre: {nombre2}, Edad: {edad2}, Tipo: {tipo2}\n\n"
                               f"Mascota 3:\nNombre: {nombre3}, Edad: {edad3}, Tipo: {tipo3}")

# y este es el codigo para ejecutar la app
app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()
