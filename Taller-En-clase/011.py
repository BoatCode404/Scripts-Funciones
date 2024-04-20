print("A continuacion ingrese la produccion en unidades correspondientes a cada dia ")
l,m,m,j,v,s=int(input("Lunes: ")),int(input("Martes: ")),int(input("Miercoles: ")),int(input("Juves: ")),int(input("Viernes: ")),int(input("Sabado: "))
suma=l+m+m+j+v+s
if suma >=100:
    print("Merece incentivo 💵💵")
else: 
    print("no merece incentivo 😒😒")