import os
import time
def limpiarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
def animated_text(text):
    for caracter in text:
        print(caracter,end='',flush=True)
        time.sleep(0.1)
def encontrar_pares(n):
    try:
        if n !=0 and n%2==0:
            animated_text(f'{n} ES PAR ')
        else:
            animated_text(f'{n} ES INPAR ')
    except ValueError:
        animated_text('❌ERRROR SE ESPERABA UN NUMERO❌')
animated_text('Escriba un numero para saber si es par ⬇️\n')
numero=int(input())
limpiarpantalla()
encontrar_pares(numero)
