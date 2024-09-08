''' Escribe un programa que reciba la altura de una persona (en centímetros) y la
clasifique en:
Baja (menos de 1.50 cm)
Promedio (1.50-1.80 cm)
Alta (más de 1.80 cm'''
import time,os
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def clasificacionAltura(a):
    if a>180:
        return("Perona Alta")
    elif a>=150 and a<181:
        return("Persona Promedio")
    else :
        return("Persona Baja")
lista=[]
index=1
while True:
    os.system('cls')
    try:
        altura=float(input(f"Registro #{index}\nCual es tu altura: "))
        lista.append(altura)
        index+=1
        print("\n¿Quieres ingresar mas registros? Si ò No ")
        animated_text("Responda Aca: ")
        r=input().lower()
        if r!='si':
            break
    except ValueError:
        animated_text("❌ERROR❌: Se esperaba un numero\n")
os.system('cls')
tipos=list(map(clasificacionAltura,lista))
for i ,tipoPersona in enumerate(tipos,1):
    print(f"Registro #{i}\nEs una {tipoPersona}\n")