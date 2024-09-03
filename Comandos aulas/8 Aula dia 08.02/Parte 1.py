import os
os.system("cls")
var = None
while var is None:
    try:
        letra = input("Escolha uma letra ").upper()
        if letra[0] == letra[0]:
            var = True
    except:
            var = None
        
while True:
    try:
        nome1 = input("Escolha o nome do jogador 1°: ")
        nome2 = input("Escolha o nome do jogador 2°: ")
        
        letra1 = input(f"Escreva uma palavra jogador {nome1} : ").upper().strip()
        letra2 = input(f"Escreva uma palavra jogador {nome2} : ").upper().strip()
        letra3 = letra1.startswith(letra[0])
        letra4 = letra2.startswith(letra[0])
        pont1 = 0
        pont2 = 0
        letracont1 = 0
        letracont2 = 0
        letracont1 += len(letra1)
        letracont2 += len(letra2)

        if letra3 == True and letra4 == True:
                pont1 += letracont1
                pont2 += letracont2
                print(f"\nA pontuaçao do jogador 1° {pont1}\nA pontuaçao do jogador 2° {pont2}")


        elif (letra3 is False) and (letra4 is True):
                letracont2 = len(letra2)
                pont1 += 0
                pont2 += letracont2
                
                print(f"O jogador 1 perdeu por que ele escreveu uma palavra que começa {letra1[0]} ")
                print(f"\nA pontuaçao do jogador 1° {pont1}\nA pontuaçao do jogador 2° {pont2}")
                break

        elif (letra3 is True) and (letra4 is False):

                pont1 += letracont1
                pont2 += 0

                print(f"O jagador 2 perdeu por que ele escreveu uma palavra que começa {letra2[0]}")
                print(f"\nA pontuaçao do jogador 1° {pont1}\nA pontuaçao do jogador 2° {pont2}")
                break
        elif (letra3 is False) and (letra4 is False):
                pont1 += 0
                pont2 += 0
                print(f"Os dois jogadores perderam jogador 1 perdeu por escrever {letra1[0]} o jogador perdeu por quer escreveu {letra2[0]}")
                print(f"\nA pontuaçao do jogador 1° {pont1}\nA pontuaçao do jogador 2° {pont2}")
                break


        sair = input("voce quer sair ? s para sim qual quer outra tecla para nao ").lower()
        if sair == "s":
            print("adeus")
            break
        else:
            ...
    except:
        print("Escreva alguma coisa pfv")          



    
