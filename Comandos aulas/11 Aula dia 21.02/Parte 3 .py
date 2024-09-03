import os
os.system("cls")
jogador1 = input("Qual se nome jogador 1 :")
jogador2 = input("Qual seu nome jogador 2 :")
palavra1 = input(f"Qual palavra voce quer que o jogador {jogador2} Adivinhe: ")
os.system("cls")
palavra2 = input(f"Qual palavar voce quer que o jogador {jogador1} Adivinhe: ")
os.system("cls")
frase1 = []
frase2 = []
for i in range(len(palavra1)):
    frase1.append(palavra1[i])

for i in range(len(palavra2)):
    frase2.append(palavra2[i])

while True:
    tentativa1 = 5
    tentativa2 = 5
    
    jogo1 = input("Escreva uma letra para ver se ela esta na fraze: ") 
    f1 = ""
    f2 = ""

    for i in range(len(palavra2)):
        if jogo1[0] == palavra2:
            if jogo1[0] == frase1[i]:
                f1 = frase1[i]
                print(f"{frase2[i]} ")
        else: 
            print("*")
    
    jogo2 = input("Escreva uma letra para ver se ela esta na fraze: ")
   

    for i in range(len(palavra1)):
        if jogo2[0] == palavra1:
            if jogo1[0] == frase2[i]:
                f2 = frase1[i]
                print(f"{frase2[i]} ")
        else:
            print("*")


