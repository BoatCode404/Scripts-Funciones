import time
import os
def animated_text(text):
    for carcter in text:
        print(carcter,end='',flush=True)
        time.sleep(0.1)
try:
    diccionario={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X"}
    num=int(input("Seleccione un numero para saber su equivalente en romano : "))
    if num == 1: 
        print(diccionario[1])
    elif num == 2:
        print(diccionario[2])
    elif num == 3:
        print(diccionario[3])
    elif num == 4:
        print(diccionario[4])
    elif num == 5:
        print(diccionario[5])
    elif num == 6:
        print(diccionario[6])
    elif num == 7:
        print(diccionario[7])
    elif num == 8:
        print(diccionario[8])
    elif num == 9:
        print(diccionario[9])
    elif num == 10:
        print(diccionario[10])
    else:
        animated_text('😒 Este programa solo acepta numeros 1-10 , lo lamento ')
except ValueError:
    animated_text('❌ ERROR ESPERABAMOS UN NUMERO ❌')