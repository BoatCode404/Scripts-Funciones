#Hacer un pseudocódigo que imprima los números impares hasta el 100 y que imprima cuantos impares hay. 
numeros=[]
for i in range(1,100+1):
    numeros.append(i)
impares=filter(lambda x: x%2==1,numeros)
for i in impares:
    print(i)
totalImpares=print(f' El total de numeros impares que hay son {len(numeros)}')
