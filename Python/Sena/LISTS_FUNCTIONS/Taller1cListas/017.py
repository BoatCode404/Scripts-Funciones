#Escribe un algoritmo que elimine los elementos en posiciones impares de una lista

numeros=[numero for numero in range(1,21)]

for numero in numeros:
    if numero % 2 != 0:
        numeros.remove(numero)
print(numeros)


lista_Pares=[numero for numero in numeros if numero%2==0]

print(lista_Pares)