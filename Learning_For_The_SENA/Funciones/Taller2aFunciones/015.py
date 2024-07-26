#Escribe  una  función  que  filtre  una  lista  de  palabras  y  devuelva  solo  las  palabras  que  contienen  una subcadena específica

def filtro(subcadena,lista):
    return [palabra for palabra in lista if subcadena in palabra]


sub='a'

cadenas=['hola','mundo','halo']

filtrada=filtro(sub,cadenas)
print(filtrada)