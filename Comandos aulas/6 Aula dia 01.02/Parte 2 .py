contador = 0
while contador <= 100:
    contador += 1
    
    if contador >= 10 and contador <= 27:
        print(f"Nao vou mostra o numero {contador}")
        continue
    else:
        print(contador)