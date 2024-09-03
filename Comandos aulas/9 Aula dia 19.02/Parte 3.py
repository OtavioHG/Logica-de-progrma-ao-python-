import os 
os.system("cls")
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [11,12,13]
print(f"1° {lista1}")
print(f"2° {lista2}")
print(f"3° {lista3}")
lista2.extend(lista3)
lista1.clear()
print(f"1° {lista1}")
print(f"2°,3° {lista2}")