mi_diccionario={
    "nombre":'Julian',
    "apellido":'Holguin',
    "puntuacion":100
}


# Devolvemos todas las claves del diccionario
mi_diccionario.keys() # keys tambien nos sirve para iterar ( hacer bucle)

# Devolvemos el valor de una clave en especifico que pongamos en el parametro del metodo get
mi_diccionario.get('nombre')

# Devolvemos todo el diccionario PERO iterable 
mi_diccionario.items()

# borramos un o varias claves con pop
mi_diccionario.pop("apellido","nombre")

# Borramos todo el diccionario 
mi_diccionario.clear()


print(type(mi_diccionario)) # clase dict ( dict de diccionario )
print(dir(mi_diccionario)) # muestra todos los metodos que se pueden realizar con los dict 