import tkinter as tk

# Cria a janela principal
janela = tk.Tk()

# Cria o botão
botao = tk.Button(janela, text="Clique aqui!")

# Define a ação do botão
def acao_do_botao():
    print("O botão foi clicado!")

botao.config(command=acao_do_botao)

# Exibe a janela
janela.mainloop()
