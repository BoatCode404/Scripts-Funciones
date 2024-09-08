texto1="hola , como , estas"

dir(texto1)#Con dir podemos saber todas las funciones que podemos hacer con dicho metodo en este caso el metodo es cadena


#Convertimos todo el texto en mayuscula
resultado = texto1.upper()


#Convertimos todo el texto en miniscula 
resultado = texto1.lower()


#Convertimos el texto con las primeras letras mayusculas
resultado = texto1.capitalize()


#Buscamos un cadena dentro de otra cadena , si no encuentra resultdado devuelve -1
resultado = texto1.find('')


# Buscamos el indice segun el elemento en la cadena de texto , si no hay concidencias nos muestra un error en ves de -1 esa es la diferencia con el find , lanz una exepcion 
resultado = texto1.index('')


# si es numerico devolvemos True de lo contrario sera false
resultado = texto1.isnumeric()


# si es afalnumerico devolvemos True de lo contrario sera false
resultado = texto1.isalpha()


#devuleve la cantidad de veces que concida
resultado = texto1.count('o')

# contamos la cantidad de caracteres que tiene un cadena 
resultado = len(texto1)

# verifica si una cadena comienza con 

resultado = texto1.startswith('')


# verifica si una cadena termina con 

resultado =  texto1.endswith('')

# remplaza una cadena dada por otra cadena dada xd

resultado = texto1.replace('hola','buenas')


# separa cadena con la cadena que le pasemos 

resultado = texto1.split(',')
print(resultado)


# Asi miramos el tipo de dato 
print(type(resultado))


