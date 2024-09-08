#Escribe un algoritmo que elimine las palabras de menos de 4 caracteres de una lista de strings.

listaStrings=['hola','julian','carro','cas','h']


masDeCuatro=[palabra for palabra in listaStrings if len(palabra)>=4]

print(masDeCuatro)