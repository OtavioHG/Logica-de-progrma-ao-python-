# Pip install pyside6 ( vai instalar a interface grafica ) (successfully instaled pyde6 addons )
#print(PySide6.__version__) # testa se a verçao da biblioteca é ver se ela ta  instalada Corretamente
# QHBoxLayout , QVBoxLayout Orijontal e Vertical
# QGridLayout pode ser tanto na vertical quanto na orijontal 

import PySide6.QtCore 
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout , QVBoxLayout ,QGridLayout
import sys


app = QApplication(sys.argv)
botao = QPushButton("Coisa") # define um botao 
botao.setStyleSheet(f"font-size: 40px; color:red") # vai modificar como o botao vai ser mostrado ("fonte": 40px; color;red)
botao1 = QPushButton("ola mundo")
botao1.setStyleSheet(f"font-size: 40px; color:purple")
#botao.show() # mostra o botao na tela 
#botao1.show()

central_widget = QWidget() # a janela responsavel 
layout = QGridLayout() # oque cuida oque esta dentro da janela 
central_widget.setLayout(layout)
layout.addWidget(botao , 1,1)
layout.addWidget(botao1, 1,2)
central_widget.show() # isso mostra a hiraquia da janela 


app.exec() # é como se foçe um loop que impede de fechar o app 

 