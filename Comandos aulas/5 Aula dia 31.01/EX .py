import os 
os.system("cls")
num1_str = (input("Escreva um número fi "))

#if num1_str.isdigit() or num1_str.isdecimal():
    #num_float = float(num1_str)
    #print(f"E um numero mesmo é o dobro dele é {num_float*2}")

#else:
  #  print("seu coco de vaca nao é o numero ")

#print(num1_str.isdigit())

try:
    print(f"voce escreveu {num1_str} ")
    num_float = float(num1_str)
    print(f"O dobro do numero {num1_str} é {num_float}")
    oi = input("escreva oi ")
    try:
        print("voce escreveu oi")

    except:
        print("voce nao escreveu oi")

except:
    print("isso nao é um numero ")
