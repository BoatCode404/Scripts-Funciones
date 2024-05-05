# Introducir un numero por teclado. Que nos diga si es par o impar. 
'<--- primera_forma --->'
'''
while True:
    numero=int(input(" Digita un numero : "))
    if numero%2==0:
        print(f"El {numero} es par")
    else:
        print(f'El {numero} es impar')
    
'''

'<--- segunda_forma --->'
import os
listaNumeros=[]
cantidadNumeros=int(input("cuantos numeros vas a ingresar para saber si son pares o impares : "))
for i in range(cantidadNumeros):
    numero=int(input("ingresa el numero : "))
    listaNumeros.append(numero)
print(f'Los numeros pares fueron')
pares=list(filter(lambda x : x%2==0,listaNumeros))
for i in pares:
    print(i)
print(f'\n\nLos numeros inpares fueron')
impares=list(filter(lambda x : x%2==1,listaNumeros))
for i in impares:
    print(i)
print(f'la cantidad de numeros pares que se ingresaron fueron {len(pares)}\nLa cantidad de numeros impares que se ingresaron fueron {len(impares)}')



'<--- tercera_forma --->'
def par_impar(num):
    if num%2==0:
        print(f'{num} es par')
    else:
        print(f'{num}es inpar')
numero=int(input("digite un numero"))
par_impar(numero)