import tkinter as tk
import os
def confir():
    s1 = senha1.get().isspace()
    s1s = len(senha1.get())
    s2 = senha2.get().isspace()
    s2s = len(senha2.get())
    if s1 == True or s1s == 0 or s2 == True or s2s == 0:
        mes2 = tk.Label(janela,text="Por favor escreva alguma coisa")
        mes2.pack()
    
    elif senha1.get() == senha2.get():
        mes2 = tk.Label(janela,text="senha valida")
        mes2.pack()
        mes3 = tk.Label(janela,text="Seja bem vindo")
        mes3.pack()
    else:
        mes2 = tk.Label(janela,text="senha invalida tente novamente")
        mes2.pack()

janela = tk.Tk()
janela.geometry("300x300")
janela.title("Cadastro")
mes1 = tk.Label(janela,text="Coloqui sua senha aqui")
mes1.pack()
senha1 = tk.Entry(janela)
senha1.pack()
mes2 = tk.Label(janela,text="Confirme sua senha")
mes2.pack()
senha2 = tk.Entry(janela)
senha2.pack()
confirme = tk.Button(janela,text="Confirmar",command=confir)
confirme.pack()
janela.mainloop()