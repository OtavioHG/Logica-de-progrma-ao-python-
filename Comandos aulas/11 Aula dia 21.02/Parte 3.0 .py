def verificar_letra(letra, palavra_secreta, letras_corretas):
    if letra in palavra_secreta:
        letras_corretas.append(letra)
        return True
    else:
        return False

def exibir_palavra_secreta(palavra_secreta, letras_corretas):
    palavra_exibida = ''
    for letra in palavra_secreta:
        if letra in letras_corretas:
            palavra_exibida += letra
        else:
            palavra_exibida += '*'
    return palavra_exibida

def main():
    palavra_secreta = input("Digite a palavra secreta: ").lower()
    letras_corretas = []
    tentativas = len(palavra_secreta) + 2

    while tentativas > 0:
        print("\nPalavra secreta:", exibir_palavra_secreta(palavra_secreta, letras_corretas))
        print("Tentativas restantes:", tentativas)
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if letra in letras_corretas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        if verificar_letra(letra, palavra_secreta, letras_corretas):
            print("Letra correta!")
        else:
            print("Letra incorreta!")

        if '*' not in exibir_palavra_secreta(palavra_secreta, letras_corretas):
            print("\nParabéns! Você venceu! A palavra secreta é:", palavra_secreta)
            break

        tentativas -= 1
    else:
        print("\nFim do jogo! Você perdeu. A palavra secreta era:", palavra_secreta)

if __name__ == "__main__":
    main()

