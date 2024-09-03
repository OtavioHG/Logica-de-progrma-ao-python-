import PySide6
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout , QVBoxLayout ,QGridLayout
import sys

tela = QApplication(sys.argv)
botao1 = QPushButton("ola")
botao2 = QPushButton("dudu")
botao3 = QPushButton("como")
botao4 = QPushButton("vc ta ?")
botao1.setStyleSheet("font-size: 40px; color: purple")
botao2.setStyleSheet("font-size: 40px; color: red")
botao3.setStyleSheet("font-size: 40px; color: pink")
botao4.setStyleSheet("font-size: 40px; color: blue")
janela = QWidget()
lugar_dos_botao = QGridLayout()
janela.setLayout(lugar_dos_botao)
lugar_dos_botao.addWidget(botao1 , 1,1)
lugar_dos_botao.addWidget(botao2 , 1,2)
lugar_dos_botao.addWidget(botao3 , 2,1)
lugar_dos_botao.addWidget(botao4 , 2,2)
janela.show()

tela.exec()
