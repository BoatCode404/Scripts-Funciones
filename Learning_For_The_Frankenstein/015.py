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
nombres=[]
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
    nombres.append(nombre)
    venta=int(input(f"¿Cual es la venta alcanzada de {nombre} este mes ?: "))
    lista.append(venta)
    index+=1
    print("¿Quires agregar otro registro? Si ò No")
    animated_text("Responde Aca:")
    r=input().lower()
    if r!='si':
        break
os.system('cls')
bonificacion=list(map(tipoBoni,lista))
for i ,(nombre,venta,bonificacion) in enumerate(zip(nombres,lista,bonificacion),1):
        print(f'registro #{i}\nVendedor: {nombre}\nVenta Del mes: {venta}\n{bonificacion}\n\n')