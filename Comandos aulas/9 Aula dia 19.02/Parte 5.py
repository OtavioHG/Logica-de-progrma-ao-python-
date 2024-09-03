import os 
os.system("cls")
lista_de_compras = ["feijao magico","salsicha","pao de quijo","leite em po","leite","tody","Nescal","pao","arroz","açucar","ovo","ovo de pascua ","agua","tomate","rabanete"]
tamanho = 15
tamanho1 = 0
while True:
    escolha = input("Escreva o numero corespondente \n1: Voce quer ver a lista \n2: Adicionar um elemento na lista \n3: Apagar o ultimo elemento da lista \n4 sair ")
    os.system("cls")
    if escolha is "1":
        for i in range(tamanho):
            print(lista_de_compras[i]) 
    elif escolha is "2":
        elemento = input("Oque voce quer adicionar na lista ")
        lista_de_compras.append(elemento)
        tamanho += 1
    elif escolha is "3":
        del lista_de_compras[-1]
        tamanho -= 1
    elif escolha is "4":
        print("Adeus")
        break
    else:
        print("Escreva um numero corespondente ")