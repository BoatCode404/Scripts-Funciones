# Escribe un algoritmo que sume todos los elementos pares de una lista de números enteros.

import funciones
numeros=[1,2,3,4,5,6,7,8,9,10]

sumaPares=sum([numero for numero in numeros if numero%2!=1])
sumaPares2=sum([numero for numero in numeros if numero%2==0])

print(sumaPares)
print(sumaPares2)

#listaPares=[]
listaPares=0
for numero in numeros :
    if numero % 2 == 0:
       #listaPares.append(numero)
       listaPares+=numero
#sumPares=print(f'{sum(listaPares)}')
print(listaPares)

print(f'La suma de los numero es : {funciones.sumaLista(numeros)}')