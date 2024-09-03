import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget,QGridLayout,QMainWindow


fonte = "font_size: 40px"
#janelas 
app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("Ola mundo")

#botaos
botao1= QPushButton("Botão 1")
botao1.setStyleSheet(fonte)
botao2= QPushButton("Botão 2")
botao2.setStyleSheet(fonte)
botao3= QPushButton("Botão 3")
botao3.setStyleSheet(fonte)

# layout 
#layout = QGridLayout()
#central_widget.setLayout(layout)
#layout.addWidget(botao1,1,1,1,1)
#layout.addWidget(botao2,1,2,1,1)
#layout.addWidget(botao3,1,3,1,1)

# açao dos botaos 
statu_bar = window.statusBar()
statu_bar.showMessage("SUA MAE")
menu = window.menuBar()
menu1 = menu.addMenu("ola gostosa")
menu1.addAction("desculpa era brincadeira")
def slot_exemplo(statu_bar):
    statu_bar.showMessage("deu certo")
menu1.triggered.connect(lambda:slot_exemplo(statu_bar))


window.show()
app.exec()