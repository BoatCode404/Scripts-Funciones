'''Escribe un programa que reciba la cantidad de libros leídos por una persona en
un año y la clasifique en:
No lector (menos de 1 libro)
Ocasional (1-4 libros)
Frecuente (5-12 libros)
Ávido lector (más de 12 libros)'''
import time,os
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def clasificacionPersona(c):
    if c>12:
        return("Avido")
    elif c>=5 and c<13:
        return("Frecuente")
    elif c>=1 and c<5:
        return("Ocasional")
    else:
        return("No lector")
lista=[]
index=1
while True:
    cantidadLibros=int(input(f"Registro #{index}\n¿Cuantos libros has leido este año?: "))
    lista.append(cantidadLibros)
    index+=1
    print("¿Quieres agregar mas registros? Si ò No ")
    animated_text("Responde Aca: ")
    r=input().lower()
    if r!='si':
        break
tipoPersona=list(map(clasificacionPersona,lista))
for i , tipo in enumerate(tipoPersona,1):
    print(f"Registro #{i}\nEs un {tipo} ")