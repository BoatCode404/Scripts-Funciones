import math
lado1=float(input("Escriba el lado 1 del triamgulo cualquiera:"))
lado2=float(input("Escriba el lado 2 del triamgulo cualquiera:"))
lado3=float(input("Escriba el lado 3 del triamgulo cualquiera:"))
semiPerimetro=(lado1+lado2+lado3)/2
areaTringulo=math.sqrt((semiPerimetro*(semiPerimetro-lado1)*(semiPerimetro-lado2)*(semiPerimetro-lado3)))
print("El area del triangulo es:",areaTringulo)