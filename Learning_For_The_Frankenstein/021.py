'''Escribe un programa que reciba la velocidad del viento (en km/h) y la
clasifique en:
Calmado (menos de 5 km/h)
Ligero (5-19 km/h)
Moderado (20-39 km/h)
Fuerte (más de 40 km/h)'''

import os,time
listaVelocidades=[]
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def clasificacionViento(v):
    if v>=40:
        return("Viento Fuerte")
    elif v>=20 and v<40:
        return("Viento Moderado")
    elif v>=5 and v<20:
        return("Viento Ligero")
    else:
        return("Viento Calmado")
while True:
    os.system('cls')
    try:
        print("Bienvenido al Medidor de viento automatico\nPara empezar escribe la velocidad del viento en km/h ")
        velocidad=float(input("Aca: "))
        tipo=clasificacionViento(velocidad)
        listaVelocidades.append((velocidad,tipo))
    except ValueError:
        animated_text("❌ ERROR ❌ SE ESPERABA UN NUMERO")
    animated_text("\n\n¿Quieres Escribir mas velocidades? Si Ò No \n")
    r=input("Responde aca:")
    if r!='si':
        break
os.system('cls')
'''clasificacion=list(map(clasificacionViento,listaVelocidades))'''
for i,(velocidad,tipo) in enumerate(listaVelocidades,1):
    print(f"el registro #{i} con velocidad de {velocidad} km/h es un : {tipo}\n")