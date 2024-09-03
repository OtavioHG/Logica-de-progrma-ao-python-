
def oliverira(num1):
    for i in range(num1):
        i+=1
        print(str(i)*i)
tubas = True
while tubas:
    try:
        num = int(input("Escreva um numero: "))

        oliverira(num)
        tubas = False

    except:
        print("escreva um numero")