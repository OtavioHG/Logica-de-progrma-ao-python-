#valores = [10,20,30,40,100]

#for i in valores:
    #print(f"O valor final do produto é : R${i}")


#-------------------------------------------------------------------------------


#while True:
    #cores = ["Azul","Amarelo","Vermelho"]

    #cor = input("Qual cor voce quer meu amigo: ")
    #cor1 = cor.title().strip()

    #if cor1 in cores:
        #print("tem sim meu amigo")
        #break
    #else:
        #print("vou ficar te devendo ")
        #qualcor = input("Qual cor voce quer agente vai criar para voce ").strip()
    
    #cores.append(qualcor)
#----------------------------------------------------------------------------------

#frutas = input("Escreva o nome das frutas separado por virgulas")
#frutas_usuario = frutas.split(",")

#print(frutas_usuario)

#----------------------------------------------------------------------------------


from array import array
letras = ["a","b","c","d"]
numeros = [10,20,30,40]
nfloat = [1.2,1.3,1.4]
print(letras)
print(numeros)
print(nfloat)
print()

letras = array("u",["a","b","c","d"])
numeros = array("i",[10,20,30,40])
nfloat = array("f",nfloat)

print(letras)
print(numeros)
print(nfloat)