def valorn(num):
    if num > 0:
        print("O numero é positivo")
    else:
        print("O numero é negativo")

tubas = True
while tubas:
    try:
        numero = float(input("Escreva um numero por favor "))
        valorn(numero)
        tubas = False
    except:
        print("por favo escreva um numero senhor cavalo ")
