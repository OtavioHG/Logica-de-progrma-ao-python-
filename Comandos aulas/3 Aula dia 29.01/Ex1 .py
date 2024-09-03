entrada = input("Escreva E para entra ou S para sair ")
senha1 = input("Escreva a senha ")
senha2 = "12345"

if (entrada == 'e' or entrada == 'E') and senha1 == senha2:
    print("voce entrou")
else:
    print("voce saiu")