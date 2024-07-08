#Escribe un algoritmo que calcule el producto de todos los elementos impares de una lista de números enteros. 

numeros=[numero for numero in range(1,20+1)]

productoNumero=1
for numero in numeros:
    if numero%2!=0:
        productoNumero*=numero

print(productoNumero)