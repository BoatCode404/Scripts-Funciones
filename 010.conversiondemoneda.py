def conversion_monedas_a_USD(m1,m2,m3):
    USD_colombia=0.00026
    USD_brazil=0.20
    USD_peru=0.27
    c=m1*USD_colombia+m2*USD_brazil+m3*USD_peru
    return c
m_pesos,m_soles,m_reales=float(input("Ingrese el monto en pesos colombianos: ")),float(input("Ingrese el monto en soles peruanos: ")),float(input("Ingrese el monto en reales brasileños: "))
dolares=conversion_monedas_a_USD(m_pesos,m_soles,m_reales)
print(f"Los dolares son 💵 : {dolares:.2f} ..¡¡¡ ")