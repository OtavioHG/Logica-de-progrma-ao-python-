import os

print("ola seja bem vindo a loja loja")
categoria = input("Qual categoria voce quer 1 para linha branca 2 para informatica 3 para construção escrava o numero da categoria ")



if categoria == 1:
    produto=input("1:Geladeira 1500 R$ \n 2:Microondas 200 R$ \n Escreva o numero do produto que voce quer escolher ")


elif categoria == 2:
    produto = input("1:Computador Game 4000 R$ \n 2:kit Gamer sem computador 600 R$ \n Escreva o numero do produto que voce quer escolher ")

elif categoria == 3:
    produto = input("1:Cimento 50Kg 50 R$ \n 2: Tijolos 500 inudades 100 R$ \n Escreva o numero do produto que voce quer escolher ")

else:
    print("")