import PySide6
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout , QVBoxLayout ,QGridLayout
import sys

tela = QApplication(sys.argv)
botao1 = QPushButton("1")
botao2 = QPushButton("2")
botao3 = QPushButton("3")
botao4 = QPushButton("4")
botao5 = QPushButton("5")
botao6 = QPushButton("6")
botao7 = QPushButton("7")
botao8 = QPushButton("8")
botao9 = QPushButton("9")
botao1.setStyleSheet("font-size: 40px; color: purple")
botao2.setStyleSheet("font-size: 40px; color: red")
botao3.setStyleSheet("font-size: 40px; color: pink")
botao4.setStyleSheet("font-size: 40px; color: blue")
botao5.setStyleSheet("font-size: 40px; color: green")
botao6.setStyleSheet("font-size: 40px; color: brown")
botao7.setStyleSheet("font-size: 40px; color: black")
botao8.setStyleSheet("font-size: 40px; color: yellow")
botao9.setStyleSheet("font-size: 40px; color: gray")
janela = QWidget()
lugar_dos_botao = QGridLayout()
janela.setLayout(lugar_dos_botao)
lugar_dos_botao.addWidget(botao1 , 1,1)
lugar_dos_botao.addWidget(botao2 , 1,2)
lugar_dos_botao.addWidget(botao3 , 1,3)
lugar_dos_botao.addWidget(botao4 , 2,1)
lugar_dos_botao.addWidget(botao5 ,2,2)
lugar_dos_botao.addWidget(botao6, 2,3)
lugar_dos_botao.addWidget(botao7 , 3,1)
lugar_dos_botao.addWidget(botao8 , 3,2)
lugar_dos_botao.addWidget(botao9,3,3)


janela.show()

tela.exec()