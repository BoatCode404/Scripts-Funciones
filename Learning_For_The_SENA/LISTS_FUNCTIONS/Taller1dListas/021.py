#Ejercicio  21:  Crear  una  lista  de  listas  donde  cada  sublista  contenga  tres  números  consecutivos,  luego  sumar  los elementos de cada sublista y mostrar tanto las sublistas como sus sumas.

listaDeListas=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

suma=[]

for sublista in listaDeListas:
    sumaSublista=0
    for numero in sublista:
        sumaSublista+=numero
    suma.append(sumaSublista)
print(suma)