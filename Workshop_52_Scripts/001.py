# Hacer un seudocódigo que imprima los números del 1 al 100.

numeros=[]
for i in range(1,100+1):
    numeros.append(i) # Guardar numeros 1-100 en lista con for
for i in range(len(numeros)):
    print(numeros[i]) # Recorrer la lista con len
