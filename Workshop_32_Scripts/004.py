partidosPerdidos=float(input("Esciba el numero de respuestas correctas:"))
partidosGanados=float(input("Escriba el numero de respuetas incorrectas:"))
partidosEmpatados=float(input("Escriba el numero de respuestas en blanco:"))
sumaPartidosPerdidos=partidosPerdidos*0
sumaPartidosGanados=partidosGanados*3
sumaPartidosEmpatados=partidosEmpatados*1
sumaTotal=sumaPartidosEmpatados+sumaPartidosGanados+sumaPartidosPerdidos
print("El puntaje final es :",sumaTotal)