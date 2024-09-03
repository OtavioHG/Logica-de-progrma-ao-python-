pernaDePau = int(input("quantas pernas de pau voce quer ?  todas custao 14 reis "))
preoco = 14*pernaDePau

if pernaDePau <= 10:
    print("sem des conto bobinho")

elif pernaDePau >= 11 and pernaDePau <= 20:
    pert=preoco*0.95
    print("voce teve um desconto de 5% ")

elif pernaDePau >= 21 and pernaDePau <=30:
    pert=preoco*0.90
    print("voce teve um  desconto de 10% R$")

else:
    pert = preoco*0.85
    print("voce ganhou um desconto de 15%")

nome = str(input("qual seu nome "))

n1=len(nome)

if n1 >= 8:
    desconto = pert*0.95
    print(f"voce ganhou mais um desconto de 5% opreço total é {desconto}")

else:
    print(f"voce nao ganhou mais desconto o preço total foi {pert}")