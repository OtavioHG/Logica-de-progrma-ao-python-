import random 
import os
os.system("cls")

gosto = []
for i in range(3):
 gosto1 = input(f"{i+1}° Escreva uma coisa que voce goste de fazer:  ")
 gosto.append(gosto1)

nao_gosto = []
for i in range(3):
 nao_gosto1 = input(f"{i+1}° Escreva uma coisa que voce nao de fazer goste:  ")
 nao_gosto.append(nao_gosto1)
 
sorteio = random.randint(0,2)
print(f"Voce vai fazer {gosto[sorteio]} e vai fazer {nao_gosto[sorteio]}")