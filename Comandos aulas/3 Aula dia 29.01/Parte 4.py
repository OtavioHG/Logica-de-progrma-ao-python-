import os
os.system("cls")
nome = input("escreva seu nome fi ")
geometrico = input("Escreva um numero de lados fi ")

verdadeiro = geometrico.isnumeric()

if verdadeiro == True:
    gem1=geometrico.strip()
    gem2 = int(gem1)
    if nome != "Otavio" and gem2 == 3:
        print(f"É um tringulo {nome}")
    
    elif nome != "Otavio" and gem2 == 4:
        print(f"É um qualdrado {nome}")

    elif nome == 'Otavio' and gem2 == 3:
        print(f"Nome muito feio {nome} é um tringulo")

    elif nome == 'Otavio' and gem2 == 4:
        print(f"Nome feio da poxa {nome} ie um qualdrado ")
    
    else:
        print("nao sei qual forma é essa ?")
else:
    print("Escreva um numero por favor ")
