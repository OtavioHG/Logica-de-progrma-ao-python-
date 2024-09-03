import os
os.system("cls")
semana = ["Domingo","Segunda","terça","Quarta","Quinta","Sexta","Sabado"]
mes = [1,2,3,4,5,6,7,8,9,10,11,12]
print(f"Semana: {semana}")
print(f"Mes: {mes}")
semana.extend(mes)
print(semana)
semana.append(13)
print(semana)