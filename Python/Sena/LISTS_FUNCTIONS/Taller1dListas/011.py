#Ejercicio 11: Crear una lista de las primeras cinco letras del alfabeto y agregar el conteo de > 5. 

numeros=[numero for numero in range(1,21)]

conteo=0
for numero in numeros:
    if numero>5:
        conteo+=1
print(conteo)

conteoMayores=len([numero for numero in numeros if numero >5])
print(conteoMayores)


alfabeto=['A','B','C','D','E']

alfabeto.append(conteoMayores)

print(alfabeto)