# Hacer un programa que imprima la suma de los 100 primeros números. 

'<---- primera_forma ---->'
numeros=[]
for i in range(1,100+1):
    numeros.append(i) # agregar numeros de iteracion a la lista
print(f'La suma de los primeros 100 numeros es\n{sum(numeros)}')

'<--- segunda_forma --->'
suma=0
for i in range(1,100+1):
    suma+=i
print(suma)


