# Hacer un seudocódigo que solo nos permita introducir S o N.  Recorrer una lista con While
letrasPosibles=['s','n',4,1.0]



'<--- recorrer_con_While --->'
indice_contador=0
while True:
    if indice_contador < len(letrasPosibles):
        print(letrasPosibles[indice_contador])
        indice_contador+=1
    else:
        break



'<--- bucle_de_opciones --->'
while True:
    letra=input(" Ingrese una letra: ")
    if letra in letrasPosibles:
        print(" Opcion validad . A Dios ")
        break
    else:
        print(" Opcion Invalida . Vuelve a Intentar ")