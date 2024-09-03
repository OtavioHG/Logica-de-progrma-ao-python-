import random
import sys
from PySide6.QtCore import Slot  # Serve para padronizar o nosso codigo 
from PySide6.QtWidgets import QApplication, QPushButton,QWidget, QGridLayout,QMainWindow,QMessageBox

adivinha = ["sim","Não","Talvez"]
app = QApplication(sys.argv)
tela = QMainWindow()
central = QWidget()
tela.setCentralWidget(central)
tela.setWindowTitle("Parte 1")

botao1 = QPushButton("bObo")
botao1.setStyleSheet('font-size: 80px;')
layout= QGridLayout()
central.setLayout(layout)
layout.addWidget(botao1,1,1,1,1)

@Slot()
def show_poup():
    messagem = QMessageBox()
    messagem.setWindowTitle("Titulo PopUp")
    messagem.setText(f"{adivinha[random.randint(0,2)]}")
    messagem.exec()


botao1.clicked.connect(show_poup)


tela.show()
app.exec()
