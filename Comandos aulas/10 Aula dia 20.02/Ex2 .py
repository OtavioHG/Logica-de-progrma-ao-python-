frase = "Otavio legal"

#print(frase.count("pa")) # o metodo count conta caracteres em uma varivael
i = 0
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    print(letra_atual)
    
    i += 1