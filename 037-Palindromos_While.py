palabra=''
while palabra>='':
    palabra=input("Cual es la palabra\n").lower()
    if len(palabra)>=3 and palabra==palabra[::-1]:
        print("Es palindroma")
    else:
        print("No es palindroma")

'====== OTRA SOLUCION CON WHILE ========='

palabra = input("Ingrese una palabra: ").lower()
es_palindromo = True
i = 0
j = len(palabra) - 1 # j contendrá el índice del último carácter de la cadena palabra.

while i < j:
    if palabra[i] != palabra[j]:
        es_palindromo = False
        break
    i += 1 
    j -= 1

if es_palindromo:
    print("Sí, es un palíndromo.")
else:
    print("No, no es un palíndromo.")