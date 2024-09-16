from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datos de una Persona")

        #widget central
        central = QWidget()

        # Creamos el layout principal
        vlayout = QVBoxLayout()

        # Creamos widgets para los 10 datos
       
        self.labelNombre = QLabel("Nombre:")
        self.editNombre = QLineEdit()

        
        self.labelApellido = QLabel("Apellido:")
        self.editApellido = QLineEdit()

        
        self.labelEdad = QLabel("Edad:")
        self.editEdad = QLineEdit()

        
        self.labelGenero = QLabel("Genero/Sexo:")
        self.editGenero = QLineEdit()

        
        self.labelDireccion = QLabel("Direccion:")
        self.editDireccion = QLineEdit()

        
        self.labelCiudad = QLabel("Ciudad:")
        self.editCiudad = QLineEdit()

       
        self.labelPais = QLabel("Pais:")
        self.editPais = QLineEdit()

        
        self.labelCorreo = QLabel("Correo electronico:")
        self.editCorreo = QLineEdit()

        
        self.labelTelefono = QLabel("Numero de telefono:")
        self.editTelefono = QLineEdit()

       
        self.labelProfesion = QLabel("Profesion:")
        self.editProfesion = QLineEdit()

        # aqui va el boton para mostrar los datos ingresados
        self.boton = QPushButton("Enviar")
        self.resultado = QLabel("")  # etiqueta para mostrar los resultados

        # Conectamos el boton para mostrar los datos
        self.boton.clicked.connect(self.mostrar_datos)

        # Añadimos los widgets al layout :D
        vlayout.addWidget(self.labelNombre)
        vlayout.addWidget(self.editNombre)
        vlayout.addWidget(self.labelApellido)
        vlayout.addWidget(self.editApellido)
        vlayout.addWidget(self.labelEdad)
        vlayout.addWidget(self.editEdad)
        vlayout.addWidget(self.labelGenero)
        vlayout.addWidget(self.editGenero)
        vlayout.addWidget(self.labelDireccion)
        vlayout.addWidget(self.editDireccion)
        vlayout.addWidget(self.labelCiudad)
        vlayout.addWidget(self.editCiudad)
        vlayout.addWidget(self.labelPais)
        vlayout.addWidget(self.editPais)
        vlayout.addWidget(self.labelCorreo)
        vlayout.addWidget(self.editCorreo)
        vlayout.addWidget(self.labelTelefono)
        vlayout.addWidget(self.editTelefono)
        vlayout.addWidget(self.labelProfesion)
        vlayout.addWidget(self.editProfesion)

        #Boton y resultado
        vlayout.addWidget(self.boton)
        vlayout.addWidget(self.resultado)

        central.setLayout(vlayout)
        self.setCentralWidget(central)

    def mostrar_datos(self):
        # Obtenencion de los datos ingresados
        nombre = self.editNombre.text()
        apellido = self.editApellido.text()
        edad = self.editEdad.text()
        genero = self.editGenero.text()
        direccion = self.editDireccion.text()
        ciudad = self.editCiudad.text()
        pais = self.editPais.text()
        correo = self.editCorreo.text()
        telefono = self.editTelefono.text()
        profesion = self.editProfesion.text()

        # Mostrar los datos en el label resultado
        self.resultado.setText(f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nGénero: {genero}\n"
                               f"Dirección: {direccion}\nCiudad: {ciudad}\nPaís: {pais}\nCorreo: {correo}\n"
                               f"Teléfono: {telefono}\nProfesión: {profesion}")

# Y finalmente el codigo para ejecutar la aplicacion
app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()
