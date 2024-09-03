import os
os.system("cls")
picole = int(input("ola seja ebm vindo a picole cremoso qual picoler voce vai quer escreva o numero corespondente"
                   "1 côco 10 R$ 2 Leiteninho 10 R$ 3 canjica 10 R$ 4 beterraba 10 R$ 5 carne de porco 10 R$ 6 ovo 10 R$ 7 chiclete 10 R$  8 canela 10 R$ 9 quijo 10 R$ 10 miojo 10 R$ "))
if picole == 3 or picole == 4:
    valor = 10*0.90
    print(f"voce ganho um desconto de 10% que deu {valor}")

else:
    valor = 10
    print("voce nao ganho desconto ")

nome = input("Qual o nome do seu bairro")
nom1 = nome.strip()
nom2 = len(nom1)

if nom2 >= 12:
    print(f"voce ganhou 50% de desconto o preço foi de  {valor*0.50}")

else:
    print(f"o preço do seu picole foi de {valor}")