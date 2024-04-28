import time
import os
def animated_text(text):
    for carcter in text:
        print(carcter,end='',flush=True)
        time.sleep(0.1)
def decenas_unidades(num):
    if num>9 and num<100:
        unidades=num%10
        num=num//10
        decenas=num%10
        animated_text(f'las unidades son: {unidades}\n')
        animated_text(f'las decenas son: {decenas}')
    else:
        animated_text('Digita un numero de dos cifras')
numero=int(input('Escribe un numero de dos cifras : '))
decenas_unidades(numero)