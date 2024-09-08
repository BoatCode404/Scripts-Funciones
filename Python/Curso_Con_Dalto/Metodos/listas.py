# creando una lista con list ( no tiene sentido y no es lo mas usado )

lista_con_list = list ( [ 5,34 ,False] )


# Asi se crean las listas normalmente 

lista = ["Hola",34,35,56,True,False,4.6]

# contar la cantidad de elementos que hay en la lista 

cantidad_elementos = len(lista)

# agregar elementos a la lista con append 

lista.append(False)

# agregar elementos con insert con un indice especifico 

lista.insert(2,'Dato insertado en la posicion 2')

# agregando elementos con extend pero con []

lista.extend([11,27])

# eliminando elementos por su indice con pop

lista.pop(0) # -1 para eliminar el ultimo 

# eliminando elementos por su valor con remove 

lista.remove('Dato insertado en la posicion 2')


# eliminando todos los elementos de la lista 

lista.clear()

# ordenar los elementos de forma ordenada Acendentemente ( solo numeros )

lista.sort()

# ordenar los elementos de forma ordenada desendente ( solo numeros )

lista.sort(reverse=True)

# invertirtiendo los elementos de una lista 

lista.reverse()

# con este comando vemos todos los metodos que podemos hacer con las listas 
print(dir(lista))


# contar un elemento especifico  de una lista con con count

conteo = lista.count(False)

print ( conteo)