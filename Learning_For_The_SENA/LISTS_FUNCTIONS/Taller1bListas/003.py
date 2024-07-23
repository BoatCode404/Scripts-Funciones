#Escribe un algoritmo que cuente cuántas veces aparece un número específico en una lista

numeros=[1,2,2,2,3,4,3,3]

conteo=0
for numero in numeros:
    if numero == 2:
        conteo+=1

print(conteo)

#-------------------------
num=2
contador= numeros.count(num)
print(contador)