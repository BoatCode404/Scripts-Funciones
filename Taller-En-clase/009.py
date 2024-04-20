def area_y_perimetro(l1,l2,l3):
    s=(l1+l2+l3)/2
    a=(s*(s-l1)*(s-l2)*(s-l3))**0.5
    print(a)
    return a
l1,l2,l3=float(input("Cual es el lado 1 del triangulo : ")),float(input("Cual es el lado 2 del triangulo : ")),float(input("Cual es el lado 3 del triangulo : "))
area=area_y_perimetro(l1,l2,l3)