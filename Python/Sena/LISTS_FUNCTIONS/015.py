'''
Elabore un algoritmo que permita ingresar el monto de venta alcanzado por un
vendedor durante el mes, luego de calcular la bonificación que le corresponde
sabiendo:
Monto Bonificación
0 - 1000 0
1000 -5000 3
5000 - 20000 5
20000 a más  8
'''
import os,time
index=1
lista=[]
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def tipoBoni(v):
    if v >=20000:
        return("Su bonificacion es de 8 ")
    elif v >=5000 and v<20000:
        return("Su bonificacion es de 5 ")
    elif v >=1000 and v<5000:
        return("Su bonificacion es de 3 ")
    else:
        return("Su bonificacion es de 0")
while True:
    os.system('cls')
    animated_text(f"Cual es el nombre del vendedor {index}: ")
    nombre=input()
    venta=int(input(f"¿Cual es la venta alcanzada de {nombre} este mes ?: "))
    bonificacion=tipoBoni(venta) 
    lista.append(((nombre,venta,bonificacion)))
    index+=1
    print("¿Quires agregar otro registro? Si ò No")
    animated_text("Responde Aca:")
    r=input().lower()
    if r!='si':
        break
os.system('cls')
'''bonificacion=list(map(tipoBoni,lista))
for i ,(nombre,venta,bonificacion) in enumerate(zip(nombres,lista,bonificacion),1):'''
for i ,(nombre,venta,bonificacion) in enumerate(lista,1):
    print(f'registro #{i}\nVendedor: {nombre}\nVenta Del mes: {venta}\n{bonificacion}\n\n')

#! <<--- Segunda_Forma --->>

import os
import time

def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)

def tipoBoni(v):
    if v >=20000:
        return "Su bonificación es de 8 "
    elif v >=5000 and v<20000:
        return "Su bonificación es de 5 "
    elif v >=1000 and v<5000:
        return "Su bonificación es de 3 "
    else:
        return "Su bonificación es de 0"

nombres = [] #? Agregamos esta lista
ventas = []

index = 1

while True:
    os.system('cls')
    animated_text(f"Cual es el nombre del vendedor {index}: ")
    nombre = input()
    ventas.append(int(input(f"¿Cuál es la venta alcanzada de {nombre} este mes?: ")))
    nombres.append(nombre) #? Agregamos nombre a la lista nueva nombres[]
    index += 1
    print("¿Quieres agregar otro registro? Si o No")
    animated_text("Responde Aca: ")
    r = input().lower()
    if r != 'si':
        break

os.system('cls')
bonificacion = list(map(tipoBoni, ventas)) #! Linea Nueva

for i, (nombre, venta, tipo) in enumerate(zip(nombres, ventas, bonificacion), 1): #! Linea Nueva
    print(f'Registro #{i}\nVendedor: {nombre}\nVenta del mes: {venta}\n{tipo}\n')
