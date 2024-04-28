numeral_input=input("Cual numero romano quiere convertir a entero: ")
def roman_to_int(numeral):
    entero_convertido=0 #Esto guardara el entero e imprimira al final
    if "CM" in numeral:
            entero_convertido +=900
            numeral=numeral.replace("CM",  "")
    if "CD" in numeral:
            entero_convertido +=400
            numeral=numeral.replace("CD",  "")
    if "XL" in numeral:
            entero_convertido +=90
            numeral=numeral.replace("XC",  "")
    if "XC" in numeral:
            entero_convertido +=40
            numeral=numeral.replace("XL",  "")
    if "IX" in numeral:
            entero_convertido +=9
            numeral=numeral.replace("IX",  "")
    if "IV" in numeral:
            entero_convertido +=4
            numeral=numeral.replace("IV",  "")
    for i in numeral:
        if i == "M":
            entero_convertido +=1000
        elif i == "D":
            entero_convertido +=500
        elif i == "C":
            entero_convertido +=100
        elif i == "L":
            entero_convertido +=50
        elif i == "X":
            entero_convertido +=10
        elif i == "V":
            entero_convertido +=5
        elif i == "I":
            entero_convertido +=1
    print("Los números romanos que ha introducido se traducen por: " + str(entero_convertido) + " !")
roman_to_int(numeral_input)

