'''Escribe un programa que reciba una nota (0-100) y la clasifique en:
Deficiente (menos de 50)
Aprobado (50-64)
Notable (65-84)
Sobresaliente (85-100)'''
import time,os
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def clasifiacionNotas(n):
    if n>=85 and n<101:
        return("Es Sobresaliente")
    elif n>=65 and n<85:
        return("es Notable")
    elif n >=50 and n<65:
        return("Es Aprobado")
    else:
        return("Es Deficiente")
lista=[]
index=1
while True:
    os.system('cls')
    nombre=input(f"¿Cual es el nombre del estudiante {index} ? :  ")
    try:
        nota=float(input(f"Cual es la nota de {nombre} : "))
        tipoNota=clasifiacionNotas(nota)
        lista.append(((nombre,nota,tipoNota)))
        r=input("¿Quieres registrar mas estudiantes? Si ò No:  ")
        if r!='si':
            break
    except ValueError:
        animated_text("❌ Error ❌ : Se esperaba una numero como nota")
os.system('cls')
for i ,(nombre,nota,tipoNota) in enumerate(lista,1):
    print(f"El registro#{i}\nPertenece Al estudiante {nombre}\nSu nota : {nota}\nLa calificacion {tipoNota}\n")



