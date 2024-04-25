correctas=float(input("Esciba el numero de respuestas correctas:"))
incorrectas=float(input("Escriba el numero de respuetas incorrectas:"))
blanco=float(input("Escriba el numero de respuestas en blanco:"))
sumaCorrectas=correctas*4
sumaIncorrectas=incorrectas*-1
sumaTotal=sumaCorrectas+sumaIncorrectas
print("El puntaje final es :",sumaTotal)