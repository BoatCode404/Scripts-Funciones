from django.shortcuts import render

# Vista para la calculadora mejorada
def calculadora(request):
    cantidad = None
    resultado = None
    error = None
    numeros = []
    
    if request.method == 'POST':
        cantidad_str = request.POST.get('cantidad')
        
        if cantidad_str and 'numero_0' not in request.POST:
            try:
                cantidad = int(cantidad_str)
            except ValueError:
                error = 'Por favor ingresa una cantidad válida.'
        elif 'numero_0' in request.POST:
            try:
                cantidad = int(request.POST.get('cantidad'))
                operacion = request.POST.get('operacion')
                
                # Recogemos los números ingresados en el formulario
                for i in range(cantidad):
                    num_str = request.POST.get(f'numero_{i}')
                    numeros.append(float(num_str))
                
                # Realizamos la operación seleccionada
                if operacion == 'suma':
                    resultado = sum(numeros)
                elif operacion == 'resta':
                    resultado = numeros[0] - sum(numeros[1:])
                elif operacion == 'multiplicacion':
                    resultado = 1
                    for num in numeros:
                        resultado *= num
                elif operacion == 'division':
                    try:
                        resultado = numeros[0]
                        for num in numeros[1:]:
                            resultado /= num
                    except ZeroDivisionError:
                        error = 'Error: división por cero.'
            except ValueError:
                error = 'Por favor ingresa valores numéricos válidos.'
        else:
            error = 'Por favor ingresa la cantidad de números.'

    # Calculamos el rango y el índice de los números para pasarlos al template
    rango = range(cantidad) if cantidad else None
    
    return render(request, 'calcufor.html', {
        'cantidad': cantidad,
        'resultado': resultado,
        'error': error,
        'numeros': numeros,
        'rango': rango
    })
