import tkinter as tk

def confirmar_texto():
    # Obtém o texto digitado na caixa de entrada
    texto = entrada.get()

    # Exibe o texto em uma nova janela
    janela_confirmacao = tk.Toplevel()
    janela_confirmacao.geometry("200x100")
    janela_confirmacao.title("Confirmação")
   
   

    label_confirmacao = tk.Label(janela_confirmacao, text=texto)
    label_confirmacao.pack()

# Cria a janela principal
janela = tk.Tk()

# Cria a caixa de entrada
entrada = tk.Entry(janela)

# Cria o botão
botao_confirmar = tk.Button(janela, text="Confirmar", command=confirmar_texto)

# Exibe a caixa de entrada e o botão
entrada.pack()
botao_confirmar.pack()

# Exibe a janela principal
janela.mainloop()
