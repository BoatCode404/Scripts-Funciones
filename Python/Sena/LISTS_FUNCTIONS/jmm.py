horas = 49
valorHora = 5000

# Calcula las horas extras
horasExtras = max(0, horas - 40)

# Inicializa el salario base
salario = valorHora * min(horas, 40)

# Calcula el salario de las horas extras
if horasExtras > 0:
    if horasExtras <= 8:
        salario += horasExtras * valorHora * 2
    else:
        salario += 8 * valorHora * 2
        salario += (horasExtras - 8) * valorHora * 3

print(salario)
