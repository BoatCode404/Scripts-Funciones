#Escribir un programa que pida al usuario dos números y luego muestre el resultado de la suma de esos dos números.
import time,os
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
numeros=[]
try:
    cantidasNumeros=3
    while cantidasNumeros!=2:
        animated_text('¿Cuantos numeros quieres sumar hoy? Escriba minimo dos numeros\n')
        cantidasNumeros=int(input("Responda Aca:"))
    for i in range(cantidasNumeros):
        animated_text(f'Escriba un numero: ')
        agregar=int(input())
        numeros.append(agregar)
    os.system('cls')
    print(f'la suma de los numeros es {sum(numeros)}')
except ValueError:
    print("Se esperaba un numero entero")
