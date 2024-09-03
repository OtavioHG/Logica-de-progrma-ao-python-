import os
os.system("cls")
semana = int(input("Escreva um numero que coresponda a um dia da semana contando que o primeiro dia é domingo "))

if semana == 6 or semana == 7 or semana == 1:
    print("Bora tomar uma rapa")

elif semana <= 2 and semana >= 5:
    print("a gente nao pode tomar uma ")

elif semana >= 8 or semana <= 1:
    print("esse dia da semana nao existe")


