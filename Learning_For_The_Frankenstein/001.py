'#? Se desea calcular la distancia recorrida (m) por un móvil que tiene velocidadconstante 100 (m/s) durante un tiempo T 30 (Sg), considerar que es un MRU(Movimiento Rectilíneo Uniforme)'

import os,time
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def mru(v,t):
    mru=v*t
    return mru
lista=[]
while True:
    try:
        os.system('cls')
        print("¿Cual es la velocidad del vehiculo en km/h?")
        animated_text("responda Aca:")
        velocidad=float(input())
        print("\n¿A que tiempo en segundos iba el vehiculo?")
        animated_text("responda Aca:")
        tiempo=int(input())
    except ValueError:
        animated_text("❌ ERROR ❌ Se esperaba un numero")
        exit()
    print("\n\n¿Quieres ingresar otro registro ? Si ò No ")
    animated_text("responda Aca:")
    clasificacion=mru(velocidad,tiempo)
    lista.append(((velocidad,tiempo,clasificacion)))
    r=input().lower()
    if r!='si':
        break
os.system('cls')
for i ,(velocidad,tiempo,clasificacion) in enumerate(lista,1):
    print(f'Registro #{i}\nVehiculo con velocidad {velocidad} km/h\nEn un tiempo de {tiempo} segundos\n\nSu MRU es: {clasificacion}\n\n')