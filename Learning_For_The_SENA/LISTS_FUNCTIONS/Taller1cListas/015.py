#Escribe un algoritmo que genere una lista de números primos menores a 20.

numerosPrimos=[numero for numero in range(2,20)]

primos=[]

for numero in numerosPrimos:
    esPrimo=True
    for i in range(2,numero):
        if numero % i == 0 :
            esPrimo=False
            break
    if esPrimo == True:
        primos.append(numero)
print(primos)

