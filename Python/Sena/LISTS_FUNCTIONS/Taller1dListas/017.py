#Ejercicio 17: Crear una lista de las primeras cinco palabras de una lista de palabras y convertirlas a mayúsculas. Mostrar la lista resultante.

palabras=['Hola Mundo','Amar Planeta','Vivir Bien','Deciciones','a']

mayusculas=[palabra.upper() for palabra in palabras]
print(mayusculas)