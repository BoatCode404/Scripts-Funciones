# Hacer un seudocódigo que imprima los números pares entre 0 y 100. 

'<---- primera_forma ---->'
numeros=[]
for i in range(0,100+1):
    numeros.append(i) # agregar numeros de iteracion a la lista
pares=filter(lambda x : x %2==0,numeros)
print('Los numeros pares ente 0-100 son\n')
for i in pares:
    print(i)

'<--- segunda_forma --->'
numeros=[]
for i in range (0,100+1):
    numeros.append(i)
for i in numeros:
    if i%2==0:
        print(i)

'<--- tercera_forma--->' 
for i in range(0,100+1):
    if i%2==0:
        print(i)