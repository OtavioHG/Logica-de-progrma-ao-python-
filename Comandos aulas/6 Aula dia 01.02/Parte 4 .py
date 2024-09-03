import os
import time

while True:
    
    contagem = input("Escreva um numero para contagem ")
    try:
        con =int(contagem)
        for i in range(con):
            print(i+1)
            time.sleep(1)
        quer = input("Escreva S para começar de novo ou qual quer tecla ")
        if quer == 's' or quer == 'S':
            continue

        else:
            print("adues")
            break
    except:
        print("voce nao escreveu um numero bobinho ")
            

       