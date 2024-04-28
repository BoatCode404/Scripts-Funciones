def hallar_divisores(num):
    divisiores=[]
    for i in range(1,num+1):
        if num%i==0:
            divisiores.append(i)
    return divisiores
n=int(input("Digite un numero entero para conocer sus divisores"))
print(f"los divisores de {n} son : {hallar_divisores(n)}")