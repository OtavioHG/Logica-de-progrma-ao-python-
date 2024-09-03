import os 
os.system("cls")
contador = True
while contador :
    condicao = input("\nOla seja bem vindo meu fi a o menu do lobby suas opiçaos sao essas (escreva o numero corespondente)"   
                "\n 0.sair \n 1.Dar Boas Vindas \n 2. Quantos vivas o otavia Merece \n 3. Uma mesagem secreta\n 4.uma mesagem intrigante ")
    try:
        con = int(condicao)
        if con == 0:
            print("Adeus")
            break
        elif con == 1:
            print(" Ola seja bem vindo ")
        elif con == 2:
            vivas = int(input("quantos vivas o otavio merece ? "))
            for i in range(vivas):
                print(f"{i+1}° viva otavio seu bobo")
        elif con == 3:
            print("OLA BONITAO")
        elif con == 4:
            print("Oque veio primeiro a laranja cor ou a laranja fruta ")
        else:
            print("escreva um numero corespondente ")
    except:
        print("escreva um numero bobo")

