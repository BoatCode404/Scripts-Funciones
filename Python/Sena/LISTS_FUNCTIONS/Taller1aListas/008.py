#Usa `extend()` para agregar los números [7, 8, 9] al final de la lista y muestra el resultado.

numeros=[numero for numero in range(1,6)]
numeros.extend([7,8,9])
print(numeros)