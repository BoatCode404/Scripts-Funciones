#Escribe una función que filtre los números mayores que un valor dado en una lista.





def filtro(valor,lista):
    #forma 3
  return [num for num in lista if num>valor]
  """   # forma 1

        mayores=[] 
    for x in lista:
        if x>valor:
            mayores.append(x)
    print(f'Los numeros mayores a {valor} que estan en la lista son : \n')
    return mayores
        

    #forma 2
    return lista[valor:] """
 
    









if __name__=='__main__':
    usuario=int(input('Digita un numero al cual quieres filtrar : '))
    
    numeros=[n for n in range(1,101)]

    listaFiltrada=filtro(usuario,numeros)
    print(listaFiltrada)

