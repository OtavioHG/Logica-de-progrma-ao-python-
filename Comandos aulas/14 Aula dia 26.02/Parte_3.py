import PySide6
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout , QVBoxLayout ,QGridLayout
import sys
import random


    
roxo = "purple"
tela = QApplication(sys.argv)
botao1 = QPushButton("janeiro")
botao2 = QPushButton("fevereiro")
botao3 = QPushButton("Março")
botao4 = QPushButton("Abril")
botao5 = QPushButton("maio")
botao6 = QPushButton("junho")
botao7 = QPushButton("julho")
botao8 = QPushButton("agosto")
botao9 = QPushButton("setembro")
botao10 = QPushButton("outubro")
botao11 = QPushButton("novembro")
botao12 = QPushButton("Dezembro")
botao1.setStyleSheet("font-size: 40px; color: red")
botao2.setStyleSheet("font-size: 40px; color: red")
botao3.setStyleSheet("font-size: 40px; color: red")
botao4.setStyleSheet("font-size: 40px; color: red")
botao5.setStyleSheet("font-size: 40px; color: red")
botao6.setStyleSheet("font-size: 40px; color: red")
botao7.setStyleSheet("font-size: 40px; color: red")
botao8.setStyleSheet("font-size: 40px; color: red")
botao9.setStyleSheet("font-size: 40px; color: red")
botao10.setStyleSheet("font_size: 40px; color: red")
botao11.setStyleSheet("font_size: 40px; color: red")
botao12.setStyleSheet("font_size: 40px; color: red")
cor_aleatoria = random.randint(0,11)
if cor_aleatoria is 0:
    botao1.setStyleSheet("font-size: 40px; color: purple")
elif cor_aleatoria is 1:
    botao2.setStyleSheet(f"font-size: 40px; color: {roxo}")
elif cor_aleatoria  is 2:
    botao3.setStyleSheet(f"font-size: 40px; color: {roxo}")
elif cor_aleatoria is 3:
    botao4.setStyleSheet(f"font-size: 40px; color: {roxo}")
elif cor_aleatoria is 4:
    botao5.setStyleSheet(f"font-size: 40px; color: {roxo}")
elif cor_aleatoria  is 5:
    botao6.setStyleSheet(f"font-size: 40px; color: {roxo}")
elif cor_aleatoria is 6:
    botao7.setStyleSheet(f"font-size: 40px; color: {roxo}")
elif cor_aleatoria is 7:
    botao8.setStyleSheet(f"font-size: 40px; color: {roxo}")
elif cor_aleatoria is 8:
    botao9.setStyleSheet(f"font-size: 40px; color: {roxo}")
elif cor_aleatoria is 9:
    botao10.setStyleSheet(f"font-size: 40px; color: {roxo}")
elif cor_aleatoria is 10:
    botao11.setStyleSheet(f"font-size: 40px; color: {roxo}")
elif cor_aleatoria is 11:
    botao12.setStyleSheet(f"font-size: 40px; color: {roxo}")
    
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
lugar_dos_botao.addWidget(botao10,4,1)
lugar_dos_botao.addWidget(botao11,4,2)
lugar_dos_botao.addWidget(botao12,4,3)

janela.show()

tela.exec()