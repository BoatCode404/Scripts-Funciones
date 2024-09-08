#Ejercicio 18: Crear una lista de números del 1 al 10 y mostrar solo los números que no son múltiplos de 2


numeros=[numero for numero in range(1,11)]
lista=[numero for numero in numeros if numero%2!=0]
print(lista)