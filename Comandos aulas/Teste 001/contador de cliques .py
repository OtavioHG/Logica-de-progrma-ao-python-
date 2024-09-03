from tkinter import *

# Cria a janela principal
janela = Tk()
janela.geometry("200x100")
janela.title("Cotador de Cliques")

# Define a variável para armazenar a contagem
contagem = 0

# Cria o rótulo que mostra a contagem
rotulo = Label(janela, text=f"Contagem: {contagem}")
rotulo.pack()

# Cria o botão que incrementa a contagem
botao = Button(janela, text="Clique aqui!", command=lambda: _incrementar_contagem())
botao.pack()

def _incrementar_contagem():
  global contagem
  contagem += 1
  rotulo.config(text=f"Contagem: {contagem}")

# Inicia o loop principal da janela
janela.mainloop()
