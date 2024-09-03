import sys
from PySide6.QtCore import Slot  # Serve para padronizar o nosso codigo 
from PySide6.QtWidgets import QApplication, QPushButton,QWidget, QGridLayout,QMainWindow,QMessageBox
app = QApplication(sys.argv)
#Janela
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("MEU APLICATIVO CHEIROSO")
#Botões
botao1 = QPushButton('Texto do Botão 1')
botao1.setStyleSheet('font-size: 80px;')
botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')
botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')
layout= QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(botao1,1,1,1,1)
layout.addWidget(botao2,1,2,1,1)
layout.addWidget(botao3,3,1,1,2)

@Slot() # decoraçao de Slot da biblioteca QTcore
def slot_exemplo(status_bar):
    pass  

@Slot() #...
def outro_slot(checked):
    print("Esta marcado ? ",checked)

@Slot() # ...
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner

@Slot()
def mk_slot_exemplo(status_bar):
    def inner():
        status_bar.showMessage('Mostra mensagem na barra')
    return inner

status_bar = window.statusBar()
status_bar.showMessage('Mostra mensagem qualquer')
#Barra de Menu
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro Menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(mk_slot_exemplo(status_bar))



segunda_acao2 = primeiro_menu.addAction('Segundaçao ação')
segunda_acao2.setCheckable(True)
segunda_acao2.toggled.connect(outro_slot)
segunda_acao2.hovered.connect(terceiro_slot(segunda_acao2))
botao1.clicked.connect(terceiro_slot(segunda_acao2)) # isso aqui serve para conequitar o botao na segunda açao

@Slot()
def show_poup():
    messagem = QMessageBox()
    messagem.setWindowTitle("Titulo PopUp")
    messagem.setText("Saude Gabriel !")
    messagem.exec()

botao2.clicked.connect(show_poup)




window.show()# Isto aqui mostra a hieraquia da janela
app.exec()#isto aqui execulta o loop da operação