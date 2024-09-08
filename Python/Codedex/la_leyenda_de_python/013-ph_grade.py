def tipo_ph(v):
    if v>7:
        return " Basico"
    elif v<7:
        return " Acido "
    else:
        return " Neutral"
ph=int(input("cual es el ph :"))
print(f"El tipo de ph es {tipo_ph(ph)}")