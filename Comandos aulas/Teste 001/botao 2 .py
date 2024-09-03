import tkinter as tk

def acao_do_botao():
    # Cria uma nova janela com a mensagem "Bem vindo!"
    janela_bem_vindo = tk.Toplevel()
    janela_bem_vindo.geometry("200x100")
    janela_bem_vindo.title("Bem vindo!")

    # Cria um label com a mensagem "Bem vindo!"
    label_bem_vindo = tk.Label(janela_bem_vindo, text="Bem vindo!")
    label_bem_vindo.pack()

# Cria a janela principal
janela = tk.Tk()
janela.geometry("1000x180")

# Cria o botão
botao = tk.Button(janela, text="Clique aqui!", command=acao_do_botao)


# Exibe o botão
botao.pack()

# Exibe a janela principal
janela.mainloop()
