'#? Hacer un seudocódigo que imprima los números del 1 al 100. Que calcule la suma de todos los números pares por un lado, y por otro, la de todos los impares.'

#* <<--- PRIMERA_FORMA --->>
listaNumeros=[]
for i in range(1,100+1):
    print(i)
    listaNumeros.append(i)
    pares=list(filter(lambda x :x%2==0 ,listaNumeros))
    inpares=list(filter(lambda x: x%1==0,listaNumeros))
print(f'la suma de los numeros pares es {sum(pares)}\nLa suma de los numeros inapres es {sum(inpares)}')

#* <<-- SEGUNDA_FORMA --->>
contadorPares=0
contadorInpares=0
for i in range(1,100+1):
    print(i)