import decimal
import os
os.system("cls")

picanha = float(input("O quilo da picanha é 40 R$ quantos quilos voce vai quere"))
valor = round(picanha*40+(0.07*picanha*40) ,2)
print(f"O preço da picanha foi de {picanha*40} junto com o imposto de 7% deu {valor}")
letra = str(input("Escreva uma letra para ver se voce ganha 2% de desconto "))
if letra == 'O' or letra == 'o':
    print(f"voce ganhou 2% de desconto na picanha o valor deu {valor-0.02*valor}")
else:
    print("voce nao ganhou desconto ")
