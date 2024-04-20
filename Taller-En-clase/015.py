import time
import os
def animated_text(text):
    for caracter in text:
        print(caracter,end='',flush=True)
        time.sleep(0.1)
def bonificacion(range):
    if range>=20000:
        animated_text('!😱 Wow¡ Has alcanzado la meta toma tu bonificacion de 8 💵💵')
    elif range<20000 and range>=5000:
        animated_text('!😱 Wow¡ Has alcanzado la meta toma tu bonificacion de 5 💵💵')
    elif range<5000 and range>=1000:
        animated_text('!😱 Wow¡ Has alcanzado la meta toma tu bonificacion de 3💵💵')
    else:
        animated_text("😭 Estamos muy desepcionados ")
r=int(input("Cual es su monto de venta ⬇️ \n"))
bonificacion(r)
