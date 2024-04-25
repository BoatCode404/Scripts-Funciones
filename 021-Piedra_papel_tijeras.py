import time
import os
import random
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
opciones=['piedra','papel','tijeras']
while True:
    animated_text('Escriba tal cual\nPiedra\nPapel\nTijeras\n')
    usuario=input().lower()
    os.system('cls')
    if usuario in opciones:
        maquina=random.choice(opciones)
        print(f"Tu elegiste {usuario}")
        print(f"La maquina eligio {maquina}")
        if usuario==maquina:
            animated_text("Es un empate\n")
        elif usuario =='papel' and maquina=='piedra':
            print('jugador gana\n')
        elif usuario == 'piedra' and maquina=='tijeras':
            print('Jugador gana\n')
        elif usuario=='tijeras'and maquina=='papel':
            print('Jugador gana\n')
        else: print('La maquina gana\n')
        break