import os
os.system("cls")
num = input("escreva um numero ")

num1 = num.lstrip()
num2 = len(num1)
if num2  > 0:
    num4 = int(num1)
    if num4%2 == 0:
        print(f"o numero é par") 

    else:
        print("o numero é impar")
else:
    print("voce nao escreveu nada")    