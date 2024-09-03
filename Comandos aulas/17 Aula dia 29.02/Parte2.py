import random
import sys
from PySide6.QtCore import Slot  # Serve para padronizar o nosso codigo 
from PySide6.QtWidgets import QApplication, QPushButton,QWidget, QGridLayout,QMainWindow,QMessageBox


global cont
global n
cont = 0
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

botao2 = QPushButton("sorteio")
botao2.setStyleSheet('font-size: 80px;')
central.setLayout(layout)
layout.addWidget(botao2,1,2,1,1)

@Slot()
def show_poup():
    global cont
    global n
    cont += 1
    messagem = QMessageBox()
    messagem.setWindowTitle("Sorteio")
    messagem.setText(f"voce voce apertou o batao {cont}")
  
    if n == cont:
        messagem.setText(f"ja deu nao vou aguntar mais ")
        cont = 0
        
    messagem.exec()

def sorteio():
    global cont
    global n
    n = random.randint(1,10)
    messagem = QMessageBox()
    messagem.setWindowTitle("Sorteio")
    messagem.setText(f"voce voce apertou o batao {n}")
    messagem.exec()


botao1.clicked.connect(show_poup)
botao2.clicked.connect(sorteio)


tela.show()
app.exec()