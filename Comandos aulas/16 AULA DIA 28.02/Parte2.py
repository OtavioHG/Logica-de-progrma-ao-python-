import sys
from PySide6.QtWidgets import QApplication, QPushButton,QWidget, QGridLayout,QMainWindow
app = QApplication(sys.argv)
#Janela
window = QMainWindow()
central_widget = QWidget()


def numero1():

def outro_slot(checked):
    print("Esta marcado ? ",checked)

def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


status_bar = window.statusBar()
status_bar.showMessage('Mostra mensagem qualquer')
#Barra de Menu
menu = window.menuBar()
primeiro_menu = menu.addMenu('Numero')
segundo_menu = menu.addMenu("Espoente")
terceiro_menu = menu.addMenu("Numero")


#primeira_acao = primeiro_menu.addAction('Primeira ação')
#primeira_acao.triggered.connect(lambda: slot_exemplo(status_bar))



num11 = primeiro_menu.addAction('0')
num22 = primeiro_menu.addAction('1')
num33 = primeiro_menu.addAction('2')
num44 = primeiro_menu.addAction('3')
num55 = primeiro_menu.addAction('4')
num66 = primeiro_menu.addAction('5')
num77 = primeiro_menu.addAction('6')
num88 = primeiro_menu.addAction('7')
num99 = primeiro_menu.addAction('8')
segunda_acao2 = primeiro_menu.addAction('9')
segunda_acao2.setCheckable(True)
segunda_acao2.toggled.connect(outro_slot)
segunda_acao2.hovered.connect(terceiro_slot(segunda_acao2))

es1 = segundo_menu.addAction('+')
es2 = segundo_menu.addAction('-')
es3 = segundo_menu.addAction('*')
es4 = segundo_menu.addAction('/')
es1.setCheckable(True)
es1.toggled.connect(outro_slot)
es2.setCheckable(True)
es2.toggled.connect(outro_slot)
es3.setCheckable(True)
es3.toggled.connect(outro_slot)
es4.setCheckable(True)
es4.toggled.connect(outro_slot)

num1 = terceiro_menu.addAction('0')
num2 = terceiro_menu.addAction('1')
num3 = terceiro_menu.addAction('2')
num4 = terceiro_menu.addAction('3')
num5 = terceiro_menu.addAction('4')
num6 = terceiro_menu.addAction('5')
num7 = terceiro_menu.addAction('6')
num8 = terceiro_menu.addAction('7')
num9 = terceiro_menu.addAction('8')
segunda_acao2 = terceiro_menu.addAction('9')
segunda_acao2.setCheckable(True)
segunda_acao2.toggled.connect(outro_slot)
segunda_acao2.hovered.connect(terceiro_slot(segunda_acao2))




window.show()# Isto aqui mostra a hieraquia da janela
app.exec()#isto aqui execulta o loop da operação