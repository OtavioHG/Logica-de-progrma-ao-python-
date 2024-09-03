def converter_para_12h(hora):
    if hora == 0:
        return 12
    elif hora <= 12:
        return hora
    else:
        return hora - 12

def obter_periodo(hora):
    if hora < 12:
        return 'A.M.'
    else:
        return 'P.M.'


while True:
    try:
        hora = int(input("Digite a hora 0 a 23: "))
        if hora < 0 or hora > 23:
            print("Por favor, digite uma hora válida de 0 a 23.")
            continue

        minutos = int(input("Digite os minutos 0 a 59: "))
        if minutos < 0 or minutos > 59:
            print("Por favor, digite minutos válidos 0 a 59.")
            continue

        hora_convertida = converter_para_12h(hora)
        periodo = obter_periodo(hora)

        print(f"A hora convertida é: {hora_convertida}:{minutos:02d} {periodo}")

        continuar = input("Deseja converter outro horário? (s/n): ")
        if continuar.lower() != 's':
            break
    except ValueError:
        print("Por favor, digite um número inteiro para as horas e minutos.")


