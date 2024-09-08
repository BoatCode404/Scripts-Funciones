#Escribe una función que verifique si una palabra es un palíndromo.



def verifica_palindromos(palabra):
    if palabra==palabra[::-1]:
        print(f'{palabra} es palindroma')
    else:
        print(f'{palabra} no es palindroma')


def main():
    while True:
        palabra=input('Escriba una palabra para saber si es palindroma: ')
        verifica_palindromos(palabra)




if __name__=='__main__':
    
    main()