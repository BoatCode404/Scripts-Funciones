def hipotenusa(l1,l2):
    h=(l1**2+l2**2)**0.5
    return h
n1,n2=float(input("Cual es el primer lado del triangulo: ")),float(input("Cual es el segundo lado del triangulo: "))
h=hipotenusa(n1,n2)
print(f"La hipotenusa del triangulo es : {h}")
