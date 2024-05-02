# Hacer un seudocódigo que imprima los números del 100 al 0, en orden decreciente.  
numeros=[]
for i in range(100,-1,-1):
    numeros.append(i)
for i in range(len(numeros)):
    print(numeros[i])