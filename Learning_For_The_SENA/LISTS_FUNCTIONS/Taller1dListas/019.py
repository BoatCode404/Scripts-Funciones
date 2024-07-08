#Ejercicio 19: Crear una lista de palabras y mostrar solo las palabras que contienen la letra 'a'.

palabras=['Hola Mundo','Amar Planeta','Vivir Bien','Deciciones']

lista=[palabra for palabra in palabras if 'a' in palabra]
print(lista)