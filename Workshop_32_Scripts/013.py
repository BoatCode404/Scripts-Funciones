def tipo_tringulo(l1,l2,l3):
    if l1==l2==l3:
        return " El tringulo es equilatero "
    elif l1==l2 or l1==l3 or l3==l2:
        return " El tringulo es isoceles "
    else:
        return " El tringulo es escaleno "
n1,n2,n3=int(input("Digite el primer lado :")),int(input("Digite el segundo lado :")),int(input("Digite el tercer lado :"))
print(tipo_tringulo(n1,n2,n3))