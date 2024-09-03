# instalar o pyside6 (pip instal pyside6)
# QPushButton é a funçao que add um botao
# QHBoxLayout de lado QVBoxLayout um encima do outro 
import PySide6.QtCore # Biblioteca PySide6.QtCore 
from PySide6.QtWidgets import QApplication,QPushButton,QHBoxLayout,QWidget,QGridLayout
import sys 

#print(PySide6.__version__) # verificar versao do PySide6
#print(PySide6.QtCore.__version__) # verificando versao do zPySide6.QtCore

app = QApplication(sys.argv)
botao = QPushButton("Aperte aqui",) # criar um botao 
botao.setStyleSheet("font-size: 40px; color: purple;") # o parametro do botao 
botao1 = QPushButton("ola mundo ")
botao1.setStyleSheet("font-size: 40px; color: red")
#botao1.show()
#botao.show() # para mostra o botao na jenela 
central = QWidget()
layout = QGridLayout()# ele é a mistura do QH e o QV
#layout = QHBoxLayout()
central.setLayout(layout)
layout.addWidget(botao, 1 , 1)
layout.addWidget(botao1, 2 ,1)
central.show()
app.exec() # para executar o codigo em loop 