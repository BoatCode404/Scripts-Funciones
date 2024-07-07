# Escribe un algoritmo que calcule el producto de todos los elementos impares de una lista de números enteros.
import funciones

numeros=[]
for i in range(1,20):
    numeros.append(i)

productoImpares=1
for numero in numeros:
    if numero % 2 !=0:
        productoImpares*=numero
print(productoImpares)

print(f'El producto de los elementos de la lista es : {funciones.prductoImpares(numeros)} ')