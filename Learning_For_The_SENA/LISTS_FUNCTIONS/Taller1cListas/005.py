#Escribe un algoritmo que genere una lista donde cada elemento sea el cubo de los números del 1 al 10.

import funciones

listaCubos=[]

for i in range(1,11):
    listaCubos.append(i**3)
print(listaCubos)

cubos=[num**3 for num in range(1,11)]
print(cubos)


rango=int(input("Cual es el rango de la lista:"))
print(funciones.listaCubos(rango))