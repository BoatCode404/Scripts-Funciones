lista=[]
def maximo(n1,n2,n3):
    return max(n1,n2,n3)
def minimo(n1,n2,n3):
    return min(n1,n2,n3)
n1,n2,n3=int(input("Digite el primer numero: ")),int(input("Digite el segundo numero: ")),int(input("Digite el tercer numero: "))
if n1==n2==n3:
    print("Todos los numeros son iguales")
    exit()
elif n1==n2 or n1==n3:
    print(f"{n1} se repite dos veces")
    exit()
elif n2==n1 or n2==n3:
    print(f"{n2} se repite dos veces")
    exit()
elif n3==n1 or n3==n2:
    print(f"{n3} se repite dos veces")
    exit()

print(f"El mayor es {maximo(n1,n2,n3)}")
print(f"El minimo es {minimo(n1,n2,n3)}")

