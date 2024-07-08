#Escribe un algoritmo que alterne mayúsculas y minúsculas en una lista de strings.

strings=["Hello Word","Baby Night","BoatCode"]

stringsAlternadas=[]

for i , string in enumerate(strings):
    if i % 2 == 0:
        stringsAlternadas.append(string.upper())
    else:
        stringsAlternadas.append(string.lower())

print(stringsAlternadas)
