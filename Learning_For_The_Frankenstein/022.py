'''Escribe un programa que reciba la velocidad máxima de un automóvil (en km/h) y
lo clasifique en:
Económico (menos de 140 km/h)
Estándar (140-180 km/h)
Deportivo (181-220 km/h)
De alto rendimiento (más de 220 km/h'''
import os,time
lista=[]
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def clasificacionAuto(v):
    if v>220:
        return("Vehiculo de alto Rendimiento")
    elif v>=181 and v<221:
        return("Vehiculo Deportivo")
    elif v>=140 and v<181:
        return("Vehiculo Estandar")
    else:
        return("Vehiculo Economico")
while True:
    os.system('cls')
    velocidad=float(input("¿Cual es la velocidad del vehiculo?: "))
    lista.append((velocidad))
    animated_text("¿Quieres Ingresar mas velocidades? Si Ò No ")
    r=input("Responda Aca:")
    if r!='si':
        break
os.system('cls')
tipos=list(map(clasificacionAuto,lista))
for i ,tipo in enumerate(tipos,1):
    print(f'El Registro #{i} tiene una velocidad de {velocidad} es un {tipo}\n')