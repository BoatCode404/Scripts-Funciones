n1,n2,n3=int(input("Digite un numero: ")),int(input("Digite un numero: ")),int(input("Digite un numero: "))
if (n3>n1 or n3>n2) and n2>n1:
    print(f"Mayor: {n3}\nMenor: {n1}\nMitad: {n2}")
elif (n1>n3 or n1>n2) and n2>n3 :
    print(f"Mayor: {n1}\nMenor: {n3}\nMitad: {n2}")
elif (n2>n1 or n2>n3) and n2>n1:
    print(f"Mayor: {n2}\nMenor: {n3}\nMitad: {n1}")
elif n1==n2==n3:
    print(f"numero: {n1}\nnumero: {n2}\nnumero: {n3}\nSon Iguales")
else:
    print(f"Mayor: {n1}\nMenor: {n2}\nMitad: {n3}")