#Ejercicio 14: Crear una lista con los números del 1 al 10 y eliminar el primer elemento que sea mayor que 5. Mostrar la lista resultante.


numeros=[numero for numero in range(1,11) ]

for numero in numeros:
    if numero>5:
        numeros.remove(numero)
        break
print(numeros)


