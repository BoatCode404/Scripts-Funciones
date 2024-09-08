# Juego de adivinasas
adivina=0
numero_intentos=0
while adivina !=6 and numero_intentos<6:
    adivina=int(input("Cual crees que es el numero escondido: "))
    numero_intentos+=1
print("Los has conseguido el numero era 6")