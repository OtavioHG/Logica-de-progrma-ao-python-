import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget,QGridLayout,QMainWindow

tela = QApplication(sys.argv)
janela  = QMainWindow()
central_widget = QWidget()
janela.setCentralWidget(central_widget)
janela.setWindowTitle("Jogo do vasco 2.0")


statu_bar = janela.statusBar()
lista1 = janela.menuBar()
lista2 = janela.menuBar()
lista3 = janela.menuBar()
lista4 = janela.menuBar()
menu1 = lista1.addMenu("1")
menu2 = lista2.addMenu("2")
menu3 = lista3.addMenu("3")
menu4 = lista4.addMenu("4")
menu1.addAction("oi")
menu2.addAction("tudo")
menu3.addAction("bem")
menu4.addAction("...")

def slot_exemplo(statu_bar):
    statu_bar.showMessage("deu certo")
def slot_exemplo2(statu_bar):
    statu_bar.showMessage("vamo la")
def slot_exemplo3(statu_bar):
    statu_bar.showMessage("voce consege")
def slot_exemplo4(statu_bar):
    statu_bar.showMessage("ta mo junto")

menu1.triggered.connect(lambda:slot_exemplo(statu_bar))
menu2.triggered.connect(lambda:slot_exemplo2(statu_bar))
menu3.triggered.connect(lambda:slot_exemplo3(statu_bar))
menu4.triggered.connect(lambda:slot_exemplo4(statu_bar))







janela.show()
tela.exec()