#Ejercicio 6.- Se requiere el desarrollo de un programa que demuestre la creación y manipulación de 
#matrices  en  la  programación,  específicamente  enfocándose  en  el  concepto  de  la  transposición  de 
#matrices. Para este fin, el programa debe realizar las siguientes tareas:

""" a) Generar una Matriz Aleatoria: El programa debe inicialmente crear una matriz A de dimensiones 4x5, 
es decir, compuesta por 4 filas y 5 columnas. Cada elemento de esta matriz debe ser un número entero 
aleatorio generado dentro del rango de 1 a 100. 
b)  Transponer  la  Matriz:  Posteriormente,  el  programa  debe  calcular  la  matriz  transpuesta  de  A, 
denominada B. Dado que A es una matriz de 4x5, B será una matriz de 5x4. La transposición implica que 
el elemento en la posición (i, j) en A será trasladado a la posición (j, i) en B. 
c)  Visualización  de  las  Matrices:  Después  de  generar  la  matriz  original  y  su  transpuesta,  el  programa 
debe mostrar ambas matrices en la pantalla. Primero se debe mostrar toda la matriz original A, seguida 
por la matriz transpuesta B. Cada fila de la matriz se debe imprimir en una línea separada para facilitar 
la visualización.
 """


import random as r

filas=4
columnas=5

for i in range(filas):
    for j in range(columnas):

