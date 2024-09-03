import tkinter as tk

def botaoc():
        try:
            janelac = tk.Toplevel()
            janelac.geometry("200x100")
           

            leb = tk.Label(janelac,text = f"O numero que voce escreveu é {entrada.get()}" )

            num1 = int(entrada.get())
    
            if num1%2 == 0:
                saida1 = tk.Label(janelac,text="Esse numero é par")
        
            else:
                saida1 = tk.Label(janelac,text="Esse numero é impar")

            leb.pack()
            saida1.pack()  
        except:
            numerror = tk.Label(janelac,text="Por favo escreva um numero ")
            numerror.pack()

janela = tk.Tk()
ola = tk.Label(janela,text="Escreva um numero")
ola.pack()
entrada = tk.Entry(janela)
entrada.pack()
botao = tk.Button(janela, text = "sim",command=botaoc)
botao.pack()
janela.mainloop()