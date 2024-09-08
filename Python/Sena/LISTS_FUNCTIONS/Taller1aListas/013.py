#Encuentra y muestra el índice del número 4 en la lista ordenada.

numeros=[numero for numero in range(1,6)]

for i,valor in enumerate(numeros):
    if valor == 4:
        print(f'Numero : {valor} --- Indice : {i}')
        break

index=numeros.index(4)
print(index)
