while True:
    num1 = input("Escreva um numero ")
    num2 = input("Escreva outro numero")
    numeros_validos = None # None siginifica nada, nulo, zero 
    try:
        num_1_float = float(num1)
        num_2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None
        if numeros_validos is None:
            print("1 Ou os dois numeros estao escritos de maneira errada")
            continue
        ... # os 3 pontinhos servem para deixar em aberto
    operadores = input("Escreva o simbulo de qual operaçao voce quer + ou - ou * ou / :")
    sair = input("Quer sair [s]im ")
    sair = sair.lower() # O comando lower faz as palavras que estao em maiusculas virarem minusculas
    sair =sair.startswith("s") #startswith aceita qualquer palavra que comece a letra ou numero selecionado como verdadeiro 
    print(sair)
    if sair is True:
        break