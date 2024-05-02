#Escribir un programa que pida al usuario ingresar su edad y luego le diga si es mayor de edad o no.
import os,time
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
edades=[]
mayores=0
menores=0
try:
    animated_text('¿ A cuantas personas vas a registrar hoy para saber si son mayores de edad?:')
    cantidadPersonas=int(input())
    for i in range(cantidadPersonas):
        animated_text('\nCual es su edad:')
        edadUsuario=int(input())
        edades.append(edadUsuario)
        if edades[i] >= 18:
            animated_text('Usted es Mayor')
            mayores+=1
        else:
            animated_text('Usted es Menor')
            menores+=1
    animated_text(f"\nla cantidad de mayores segun los registros son : {mayores}\nLa cantidad de menores segun los registros son : {menores}")
except ValueError:
    print("Se esperaba un numero entero")