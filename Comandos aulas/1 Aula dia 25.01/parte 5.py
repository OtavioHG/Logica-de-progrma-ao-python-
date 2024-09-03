import os
os.system('cls')
nome=input('Qual nome você proíbe ? ')
nomex=input('Qual seu nome ? ')

nomao=str(nome).replace(nome,'Queridão')
idade= int (input ('Qual sua idade ? ' ))
if nomex==nome:
    print("Você não pode jogar pois seu nome esta na lista ")
elif idade<=10:
    print(f'{nomao} pode jogar jogos da categoria livre')
elif idade ==11 or idade<17:
    print(f'{nomao} pode jogar jogos de adolescente')

else:
    print(f'{nomao} pode jogar todos os tipos de jogos')