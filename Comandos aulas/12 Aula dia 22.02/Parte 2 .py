import random


def oliverira(nome):
    caraquiteres = list(nome)
    random.shuffle(caraquiteres)
    frase = ''.join(caraquiteres)
    print(frase)

nom = input("Esceva um nome: ")

oliverira(nom)


