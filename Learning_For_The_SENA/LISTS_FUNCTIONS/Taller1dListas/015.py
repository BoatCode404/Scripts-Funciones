#Ejercicio 15: Crear una lista con los elementos de la lista original elevados a la potencia de su índice y mostrar la lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

potencias=[]

for i , numero in enumerate(numeros):
    potencia=numero ** i
    potencias.append(potencia)
print(potencias)

p=[numero ** i for i , numero in enumerate(numeros) ]
print(p)