# Hacer un seudocódigo que imprima todos los números naturales que hay desde la unidad hasta un número que introducimos por teclado. 

'<--- primera_forma --->'

numeros=[]
cantidadN=int(input("¿Cuantos numeros quieres imprimir?: "))
for i in range(cantidadN+1):
    numeros.append(i)
for i in range(len(numeros)):
    print(numeros[i])


'<--- segunda_forma --->'

for i in range(cantidadN+1):
    print(i)