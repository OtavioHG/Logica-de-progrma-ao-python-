import tkinter as tk
import os
import math as mt
contador = 0
num1 = 0
num2 = 0

def numero():
    global contador, num1 , num2
    contador += 1

    if contador == 1:
        num1 = float(num.get())

    elif contador == 2:
        num2 = float(num.get())

    else:
        erro = tk.Label(Cal,text="so aceitamos dois numeros ")
        erro.pack()
    
def soma():
    soma = num1 + num2
    resultado = tk.Toplevel()
    res = tk.Label(resultado,text=f"A soma dos numeros é {soma}")
    res.pack()

def subitracao():
    subitracao = num1-num2
    resultado = tk.Toplevel()
    res = tk.Label(resultado,text=f"A su bitrçao dos numeros é {subitracao}")
    res.pack()

def multipicacao():
    multipicacao = num1*num2
    resultado = tk.Toplevel()
    res = tk.Label(resultado,text=f"A su bitrçao dos numeros é {multipicacao}")
    res.pack()

def divisao():
    resultado = tk.Toplevel()
    if num1 is 0 and num2 is 0:
        res = tk.Label(resultado,text="nao pode dividir 0 por zero")
        res.pack()
    elif num1 is 0:
        res = tk.Label(resultado,text="nao pode dividir 0 por zero")
        res.pack()
    else:
        div = num1/num2
        
        res = tk.Label(resultado,text=f"A su bitrçao dos numeros é {div}")
        res.pack()

def ponte():
    multi = num1**num2
    resultado = tk.Toplevel()
    res = tk.Label(resultado,text=f"A potencia é {multi}")  
    res.pack()

def raiz():
    rai = num1**(1/num2)
    resultado = tk.Toplevel()
    res = tk.Label(resultado,text=f"A raiz é {rai}")
    res.pack()
    
Cal = tk.Tk()
mg = tk.Label(Cal,text= "Escreva um numero ")
mg.pack()
num = tk.Entry(Cal)
num.pack()
contador = 0
confirme = tk.Button(Cal,text="Confirmar",command=numero)
confirme.pack()
mais = tk.Button(Cal,text="+",command=soma)
mais.pack()
menos = tk.Button(Cal,text="-",command=subitracao)
menos.pack()
multi = tk.Button(Cal,text="*",command=multipicacao)
multi.pack()
divi = tk.Button(Cal,text="/",command=divisao)
divi.pack()
potencia = tk.Button(Cal,text="**",command=ponte)
potencia.pack()
ra = tk.Button(Cal,text="√",command=raiz)
ra.pack()


Cal.mainloop()