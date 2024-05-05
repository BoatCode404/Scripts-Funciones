#Imprimir y contar los múltiplos de 3 desde la unidad hasta un número que introducimos por teclado. 

'#TODO <<-- primera_forma --->>'

listaNumeros=[]
contador=0
try:
    longitud=int(input("Digite hasta donde quieres conocer los numeros que son multiplos de 3 : "))
    for i in range(longitud):
        if i%3==0:
            listaNumeros.append(i)
            contador+=1
    print(f"los multiplos de 3 que hay de 0-{longitud} son \n")
    for i in range(len(listaNumeros)):
        print(listaNumeros[i])
    print(f"en total hay {contador} numeros que son multiplos de 3 de 0-{longitud} \n")
except ValueError:
    print("Se esperaba un numero para el rango")



