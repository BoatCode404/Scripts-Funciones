#Ejercicio 20: Crear una lista con los elementos de la lista original ordenados en orden descendente y mostrar la lista.

numeros=[1,100,50,80,70,500,100,1025,3,4,9,55,28]

descendente=sorted(numeros,reverse=True)
ascendente=sorted(numeros)
print(f'descendente-{descendente}\n\tascendente-{ascendente}')