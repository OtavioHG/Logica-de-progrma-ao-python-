import os
os.system("cls")
nome = input("qual seu nome é sobrenome ")
idade = input("qual idade vcoe tem ")
sobrenome = nome.split()

print(f"seu nome : {nome}\n sua idade é : {idade}\na primeira letra do seu nome ")
print (f"{nome[0]}, é a letra final é {nome[-1]} vou trocar o sobrenome {sobrenome[0]} ")
print(f" {str(sobrenome[1].replace(sobrenome[1],'feio'))}")