import os
os.system("cls")

idade = input("Qual sua idade meu fi: ")
altura = input("Qual sua altura meu fi: ")

try:
    idade1 = int(idade)
    altura1 = float(altura)
    idade >= 12 or  altura1 >= 1.50
   # if idade >= 12 or  altura1 >= 1.50:
    print("voce pode andar na motanha russa")
    #else:
       # print("voce nao pode andar na motanha russa")


except:
    print("voce nao pode andar na motanha russa")
    print(f"escreva sua idade c4b4ço ou sual altura verdadeira ")
