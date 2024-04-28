import random
pregunta=input("Cual es la pregunta: ")
num=random.randint(1,9)
if num==1:
    print("Sí, definitivamente.")
elif num==2:
    print("Decididamente.")
elif num==3:
        print("Sin ninguna duda.")
elif num==4:
        print("Respuesta confusa, inténtelo de nuevo.")
elif num==5:
        print("Vuelve a preguntar más tarde.")
elif num==6:    
        print("Mejor no te lo digo ahora.")
elif num==7:
        print("Mis fuentes dicen que no.")
elif num==8:
        print("Perspectivas no muy buenas.")
elif num==9:
        print("Muy dudoso.")