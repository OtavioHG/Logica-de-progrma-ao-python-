import os
os.system("cls")
email1 = True
while email1 == True:
    email = input("Escreva seu email ")
    email1 = "@" in email
    if email1 == True:
        print("Email valido")

    else:
        print("Email invalido")

   

