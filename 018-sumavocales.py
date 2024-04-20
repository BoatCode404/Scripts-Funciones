sumaA=0
sumaB=0
sumaC=0
sumaD=0
try:
    palabra=input("Cual es la palabra: ")
    for letra in palabra:
        if letra.lower() == "a":
            sumaA+=1
        elif letra.lower() == "b":
            sumaB+=1
        elif letra.lower() == "c":
            sumaC+=1
        elif letra.lower() == "d":
            sumaD+=1
except ValueError:
    print("Error Has escrito un numero")
print(f"La cantidad de Vocales que hay en la palabra : {palabra} es:")
print(f"Cantidad de vocales(A):{sumaA}")
print(f"Cantidad de vocales(B):{sumaB}")
print(f"Cantidad de vocales(C):{sumaC}")
print(f"Cantidad de vocales(D):{sumaD}")
      
    