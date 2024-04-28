import random
abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num=['0','1','2','3','4','5','6','7','8','9,']
simbol=['!', '#', '$', '%', '&','*', '+']
cantidadLetras=int(input("Cuantas letras desea en la contraseña : "))
cantidadNumeros=int(input("Cuantos numeros desea en la contraseña : "))
cantidadCaracter=int(input("Cuantos caracter desea en la contraseña : "))
contraseña=[]
for i in range(1,cantidadLetras+1):
    contraseña.append(random.choice(abc))
for i in range(1,cantidadNumeros+1):
    contraseña+=random.choice(num)
for i in range(1,cantidadCaracter+1):
    contraseña+=random.choice(simbol)
random.shuffle(contraseña)
verContraseña=""
for i in contraseña:
    verContraseña+= i
print(verContraseña)