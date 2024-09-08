def mayorYDiferencia(e1,e2,e3):
    mayor= max(e1,e2,e3)
    menor= min(e1,e2,e3)
    d= mayor-menor
    print("el mayor es ", mayor)
    return mayor
n1,n2,n3=int(input("Ingrese el primer numero entero: ")),int(input("Ingrese el segundo numero entero: ")),int(input("Ingrese el tercer numero entero: "))
mayor=mayorYDiferencia(n1,n2,n3)