import os
os.system("cls")
condicao = True # valor booleano

while condicao: #olha se a condiçao foi satifeita
   nome= input("Escreva seu nome ")
   print(f"seu nome é {nome}")
   
   if nome == 'sair' : #olaha se a condiçao foi satifeita
      break #fecha o laço de repitiçao
     
print("voce saiu do laço")
    