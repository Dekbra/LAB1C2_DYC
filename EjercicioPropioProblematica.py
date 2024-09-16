# Ok la problematica en este ejercicio es la siguiente, yo ordeno las muestras medicas para darselas a los doctores entonces lo que yo meramente necesito es una aplicaion para poder
# seleccionar las muestras medicas de manera correcta, lo que necesito es ver el tipo de muestra que debo seleccionar para esto se usará un ComboBox y ademas necesito agregar una 
# cantidad de muestras para poder darle al doctor, entonces lo que se va a moestrar en el label es basicmaente el nombre de la muestra y la cantidad que seleccioné.

# Los nombres de las muestras medicas serian: Reversal Flex, Tazarol Rapid, Tazarol duo, Neuro Tazarol, Movisil Duo y Dromadol forte.


#EXPLICACION DEL CODIGO!!!

# Bueno, el funcionamiento del codigo creo que es algo muy sencill, basicamente lo que se hace es que tengo ordenadas todas las muestras en un ComboBox para asi tenerlas 
# y poder seleccionarlas de la mejor manera siempre que necesite una sola la busco y la selecciono y con el SpinBox me facilita el hecho de agregar la cantidad de muestras
# que le dare al doctor y aparte de eso le da un mejor aspecto, asi mismo me ayuda a poder tener a la mano ambas opciones y poder tanto seleccionar el tipo de muestra como
# seleccionar la cantidad que necesito y asi agilizar y hacer mas practica la manera en que necesito tomarlas para poder entregarlas, me ayuda a ser mas organizado basicamente.

 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QSpinBox, QPushButton)
import sys

class SampleManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion de Muestras Medicas")

        # Layout principal
        layout = QVBoxLayout()

        # Label para la instrucción
        self.labelInstruccion = QLabel("Seleccione el tipo de muestra médica y la cantidad:")
        layout.addWidget(self.labelInstruccion)

        # Ponemos el ComboBox para seleccionar el tipo de muestra médica :D
        self.comboBoxMuestras = QComboBox()
        self.comboBoxMuestras.addItems([
            "Reversal Flex", "Tazarol Rapid", "Tazarol Duo", 
            "Neuro Tazarol", "Movisil Duo", "Dromadol Forte"
        ])
        layout.addWidget(self.comboBoxMuestras)

        # usamos el spinBox para seleccionar la cantidad de muestras
        self.spinBoxCantidad = QSpinBox()
        self.spinBoxCantidad.setRange(1, 100)  # Límite de 1 a 100 muestras
        layout.addWidget(self.spinBoxCantidad)

        # Botón para enviar la selección
        self.botonEnviar = QPushButton("Confirmar Seleccion")
        layout.addWidget(self.botonEnviar)

        # Label para mostrar la selección que hemos hecho
        self.labelResultado = QLabel("")
        layout.addWidget(self.labelResultado)

        # conectar el botón para mostrar los resultados
        self.botonEnviar.clicked.connect(self.mostrar_resultado)

        #establecer el layout
        self.setLayout(layout)

    def mostrar_resultado(self):
        muestra_seleccionada = self.comboBoxMuestras.currentText()
        cantidad_seleccionada = self.spinBoxCantidad.value()
        self.labelResultado.setText(f"Has seleccionado {cantidad_seleccionada} muestras de {muestra_seleccionada}")

#Codigo para ejecutar la app
app = QApplication(sys.argv)
ventana = SampleManager()
ventana.show()
app.exec()
