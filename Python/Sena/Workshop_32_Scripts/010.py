def mayorYDiferencia(e1,e2):
    mayor= max(e1,e2)
    menor= min(e1,e2)
    d= mayor-menor
    print("la diferencia es de ",d," Años "," Y el mayor es ", mayor)
    return d,mayor
hermano1,hermano2=int(input("Cual es la edad del hermano 1 : ")),int(input("Cual es la edad del hermano 2 :"))
mayor_diferencia=mayorYDiferencia(hermano1,hermano2)