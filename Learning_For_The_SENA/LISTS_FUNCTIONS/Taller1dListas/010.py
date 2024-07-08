#Ejercicio 10: Contar el número de elementos en la lista original que son mayores que 5 y mostrar el conteo.

numeros=[numero for numero in range(1,21)]

conteo=0
for numero in numeros:
    if numero>5:
        conteo+=1
print(conteo)

conteoMayores=len([numero for numero in numeros if numero >5])
print(conteoMayores)