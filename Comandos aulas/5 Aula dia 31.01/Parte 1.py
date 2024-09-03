import os 
os.system("cls")
id_1 = input("escreva se id ")
try :
    id_2 = float(id_1)
    senha = input("Crie uma senha a senha precisa ter * ")
    if "*" in senha:
        print("senha valida")
        login = input("Ecreva seu id ")
        login1 = input("Escreva sua senha ")
        if login == id_1 and login1 == senha:
            print("Voce fez login com suceso ")
        else:
            print("voce nao consegiu logar")
    else:
        print(" Senha Invalida ")

except:
    print("id invalido ")