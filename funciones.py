import time
import os
# Convertir grados Fahrenheit a Celsius 🌡️
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
# Calcular IMC (indice de masa corporal) 💪
def calcular_IMC(p,a):
    IMC={p/a**2}
    return IMC
# Calcular la hipotenusa de un triangulo 📐
def hipotenusa(l1,l2):
    h=(l1**2+l2**2)**0.5
    return h
# Conversion de monedas a dolares 💵
def conversion_monedas_a_USD(m1,m2,m3):
    USD_colombia=0.00026
    USD_brazil=0.20
    USD_peru=0.27
    c=m1*USD_colombia+m2*USD_brazil+m3*USD_peru
    return c
# Contrar Movimiento Rectiliano Uniforme (Distancia)📏
def encontrarMru(v,t):
    d=v*t
    return d
# area y semiperimetro de un triangulo con 3 lados ↕️↔️
def area_y_perimetro(l1,l2,l3):
    s=(l1+l2+l3)/2
    a=(s*(s-l1)*(s-l2)*(s-l3))**0.5
    print(a)
    return a
# Distancia entre dos puntos 🧷
def distanciaDosPuntos(a1, b1, a2, b2):
    d = ((a2 - a1) ** 2 + (b2 - b1) ** 2) ** 0.5
    return d
# Saber edad segun año actual 😶‍🌫️
def edad_persona(f):
    año_actual=2024
    e=año_actual-f
    return e
# Mayor y diferencia de cualquier dato 🔣
def mayorYDiferencia(e1,e2):
    mayor= max(e1,e2)
    menor= min(e1,e2)
    d= mayor-menor
    print("la diferencia es de ",d," Años "," Y el mayor es ", mayor)
    return d,mayor
# Conocer Tipo de triangulo 📐
def tipo_tringulo(l1,l2,l3):
    if l1==l2==l3:
        return " El tringulo es equilatero "
    elif l1==l2 or l1==l3 or l3==l2:
        return " El tringulo es isoceles "
    else:
        return " El tringulo es escaleno "
# Tipo de PH 🌡️
def tipo_ph(v):
    if v>7:
        return " Basico"
    elif v<7:
        return " Acido "
    else:
        return " Neutral"
# Encontrar Polindromos
def encontrarPalindromos(frase):
    frase.lower()
    if len(frase)>=3 and frase==frase[::-1]:
        palindromo=print(f"La frase {frase} es un palindromo ")
        return palindromo 
    else:
        print("No es un palindromo")
# Funcion para animar texto
def animated_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
# Encontrar Decenas y uidades
def decenas_unidades(num):
    if num>9 and num<100:
        unidades=num%10
        num=num//10
        decenas=num%10
        animated_text(f'las unidades son: {unidades}\n')
        animated_text(f'las decenas son: {decenas}')
    else:
        animated_text('Digita un numero de dos cifras')
# Limpiar Pantalla para todos los sistemas operativos
def limpiarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')