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
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
cantidadVendedores=int(input("¿Cuantos registros vas hacer?: "))
for i in range(cantidadVendedores):
    animated_text(f"Cual es el nombre del vendedor {i+1}: ")
    nombre=input()
    venta=int(input(f" ¿ Cual es la venta alcanzada de {nombre} este mes ?:  \n"))
    if venta >=20000:
        animated_text("Su bonificacion es de 8 ")
    elif venta >=5000 and venta<20000:
        animated_text("Su bonificacion es de 5 ")
    elif venta >=1000 and venta<5000:
        animated_text("Su bonificacion es de 3 ")
    else:
        animated_text("Su bonificacion es de 0 \n\n")

