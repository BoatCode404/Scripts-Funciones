#Escribe un algoritmo que filtre una lista de palabras y devuelva solo las palabras que contienen una subcadena específica.

palabras=['holo','santiago','arroz','mongo']


subcadena='a'

for palabra in palabras:
    if subcadena in palabra:
        print(palabra)


