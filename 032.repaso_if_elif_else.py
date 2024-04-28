# Write code below 💖
height=float(input('¿Cual es su altura?\n'))
credits=float(input('¿Cuantos Creditos tiene?\n'))
if height>=137 and credits>=10:
    print('Disfrute el viaje')
    exit()
if height>=137 and credits<10:
        print('No tienes suficientes creditos')
elif height<137 and credits>=10:
    print('No Eres lo suficiente alto para pasar')
else:
    print("No cumple ningun requisito")