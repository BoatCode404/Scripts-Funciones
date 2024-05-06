'''Escribe un programa que reciba una temperatura (en grados Celsius) y la
clasifique en:
Frío (menos de 10°C)
Templado (10-20°C)
Cálido (21-30°C)
Caluroso (más de 30°C
'''
import time
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def tipoTemperatura(t):
    if t>=30:
        return("Caluroso")
    elif t>=21 and t<30:
        return("Calido")
    elif t>=10 and t<21:
        return("Templado")
    else:
        return("Frio")
lista=[]
contador=1
while True:
    temperatura=int(input(f"Escriba la {contador} temperatura: "))
    lista.append(temperatura)
    contador+=1
    animated_text("¿Quieres Ingresar mas temperaturas?\nSi\nNo\nResponda Aca: ")
    r=input().lower()
    if r !='si':
        break
tipos=list(map(tipoTemperatura,lista))
for i,tipo in enumerate(tipos,1):
    print(f'temperatura {i}: {tipo}')