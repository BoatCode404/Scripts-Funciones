acomulador={ 
    "Gryffindor 🦁":0,
    "Ravenclaw  🦅":0,
    "Hufflepuff 🦡":0,
    "Slytherin  🐍":0
    }
print("¿Te gusta Amanecer o anochecer? ")
print("1) Amanecer  🌅 ")
print("2) Anochecer 🌃 ")
r1=int(input("Responda Aca: "))
if r1==1:
    acomulador["Gryffindor 🦁"]+=1 
    acomulador["Ravenclaw  🦅"]+=1
elif r1==2:
    acomulador["Hufflepuff 🦡"]+=1
    acomulador["Slytherin  🐍"]+=1
else:
    print("Entrada Incorrecta")
print("Cuando muera, quiero que la gente me recuerde como?")
print("1) El Bueno  🫶 ")
print("2) El Grande 🦒 ")
print("3) El sabio  ☯️ ")
print("4) El Audaz  💪 ")
r2=int(input("Responda Aca: "))
if r2==1:
    acomulador["Hufflepuff 🦡"]+=2
elif r2==2:
    acomulador["Slytherin  🐍"]+=2
elif r2==3:
    acomulador["Ravenclaw  🦅"]+=2
elif r2==4:
    acomulador["Gryffindor 🦁"]+=2
else:
    print("Entrada Incorrecta")
print("¿Qué tipo de instrumento le agrada más al oído? ")
print("1) El Violin   🎻 ")
print("2) La Trompeta 🎺 ")
print("3) El Piano    🎹 ")
print("4) El tambor   🥁 ")
r3=int(input("Responda Aca: "))
if r3==1:
    acomulador["Slytherin  🐍"]+=4
elif r3==2: 
    acomulador["Hufflepuff 🦡"]+=4
elif r3==3:
    acomulador["Ravenclaw  🦅"]+=4
elif r3==4:
    acomulador["Gryffindor 🦁"]+=4
else:
    print("Entrada Incorrecta ")
casa_ganadora=max(acomulador,key=acomulador.get)
print("¡ Felicitaciones perteneces a : ", casa_ganadora + " !")