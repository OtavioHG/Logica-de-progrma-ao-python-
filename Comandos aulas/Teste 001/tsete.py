num1 = input("escreva um numero")
try:
    num2 = int(num1)
    print(f"{num2}")
    num3 = input("escreva outro numero ")
    try:
        num4 = int(num3)
        print(f"{num4}")
    except:
        print("nao é um numero @")
except:
    print("nao é um numero")