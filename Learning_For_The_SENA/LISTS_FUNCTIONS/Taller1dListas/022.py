#Crear una lista que contenga una mezcla de números y cadenas de texto y mostrar solo los elementos que sean cadenas de texto

listaMixta=[True,False,10.1,12,-5,'5','Hola']

texto=[texto for texto in listaMixta if isinstance(texto,int)]

print(texto)

