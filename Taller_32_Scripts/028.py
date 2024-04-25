import os
vocales=["a","e","i","o","u"]
suma_vocales=0
suma_consonantes=0
for i in range(1,10+1):
    letras=input("Digite una letra\n").lower()
    if letras in vocales:
        suma_vocales+=1
    else:
        suma_consonantes+=1
print(f"La cantidad de vocales ingresadas fueron : {suma_vocales}\nLa cantidad de consonantes ingresadas fueron : {suma_consonantes}")