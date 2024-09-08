#Ejercicio 5: Crear una nueva lista que contenga solo los elementos impares de la lista original y mostrarla.

numeros=[1,2,3,4,5,6,7,8]

impares=[numero for numero in numeros if numero%2!=0]
print(impares)