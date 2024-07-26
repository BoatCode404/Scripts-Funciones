""" Se te ha asignado la tarea de desarrollar un programa que cree y muestre los elementos 
de una matriz bidimensional de dimensiones 4x5, es decir, 4 filas y 5 columnas. Cada elemento de la 
matriz  debe  ser  un  número  entero  generado  aleatoriamente  entre  1  y  100,  inclusivo.  Una  vez 
generada,  la  matriz  debe  ser  mostrada  en  pantalla,  elemento  por  elemento,  junto  con  sus  índices 
correspondientes para facilitar su identificación """

import random as r

#Dimensiones
filas=4
columnas=5

#Lista Principal(Matriz Principal)
matriz=[]


for i in range(filas):
    fila=[]
    for j in range(columnas):
        numeroAzar = r.randint(1,101)
        fila.append(numeroAzar)
    matriz.append(fila)




for i in range(filas):
    for j in range(columnas):
        print(f'indices {i},{j} = {matriz[i][j]}')
    print('') # esto es para pasar a la siguiente fila




for fila in matriz:
    for elemento in fila:
        print(f'{elemento:3}',end='') # :3 significa el espaciado que hay entre cada numero
    print('')



