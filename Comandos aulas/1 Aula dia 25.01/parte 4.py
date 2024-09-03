import os
os.system("cls")
idade = int(input("qual sua idade ?"))

if idade <=5:
    print("voce esta na creche")
elif idade == 6 or idade <= 10:
    print("ensino fundamental")
elif idade == 11 or idade < 14:
    print("ensino fundamental II")
elif idade > 14:
    print("ensino medio")
else:
    print("em honra a otavio")