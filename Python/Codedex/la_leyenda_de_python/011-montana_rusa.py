requisitoAltura=float(1.37)
requisitoCredito=int(10)
altura,creditos=float(input("Cual es su altura : ")),int(input("Cuantos puntos tiene: "))
if altura >= requisitoAltura and creditos>= requisitoCredito:
    print("¡Disfruta el viaje! 🎢")
elif creditos>=requisitoCredito and altura<requisitoAltura:
    print("No eres lo suficientemente alto para montar😒")
elif altura>=requisitoAltura and creditos<requisitoCredito:
    print("No tienes suficientes creditos para montar😒")
else:
    print("No Has cumplido ningun requisito para subir😕")