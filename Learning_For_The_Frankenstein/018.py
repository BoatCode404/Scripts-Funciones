'''Escribe un programa que reciba una nota (0-100) y la clasifique en:
Deficiente (menos de 50)
Aprobado (50-64)
Notable (65-84)
Sobresaliente (85-100)'''
import time
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
cantidadNotas=int(input("¿Cuantas notas vas a ingresar?: "))
for i in range(cantidadNotas):
    nombre=input(f"¿Cual es el nombre del estudiante {i+1}?:  ")
    nota=int(input(f"Escriba la {i+1} nota del estudiante {nombre}: "))
    if nota>=85 and nota<101:
        animated_text("La nota es Sobresaliente\n\n")
    elif nota>=65 and nota<85:
        animated_text("La nota es Notable\n\n")
    elif nota >=50 and nota<65:
        animated_text("La nota es Aprobado\n\n")
    else:
        animated_text("La nota es Deficiente\n\n")




