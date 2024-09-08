from django.shortcuts import render
from django.http import HttpResponse  # Importa HttpResponse, aunque no se está utilizando en este caso.

# Vista de la calculadora
def calculadora_view(request):
    resultado = None  # Variable para almacenar el resultado de la operación
    error = None  # Variable para almacenar mensajes de error si ocurren
    
    if request.method == 'POST':  # Verifica si el formulario ha sido enviado (método POST)
        # Obtiene los valores enviados a través del formulario HTML usando sus nombres como claves
        num1_str = request.POST.get("numero1")  # Primer número como cadena de texto
        num2_str = request.POST.get("numero2")  # Segundo número como cadena de texto
        operacion = request.POST.get('operacion')  # Operación seleccionada (suma, resta, etc.)

        # Verifica que los valores no estén vacíos y que se haya seleccionado una operación
        if num1_str and num2_str and operacion:
            try:
                # Convierte los valores de los números de cadena de texto a flotantes (números decimales)
                num1 = float(num1_str)
                num2 = float(num2_str)

                # Realiza la operación seleccionada
                if operacion == "suma":
                    resultado = num1 + num2  # Suma
                elif operacion == "resta":
                    resultado = num1 - num2  # Resta
                elif operacion == "multiplicacion":
                    resultado = num1 * num2  # Multiplicación
                elif operacion == "division":
                    if num2 != 0:  # Verifica que el segundo número no sea cero para evitar la división por cero
                        resultado = num1 / num2  # División
                    else:
                        error = "Error: División por cero"  # Muestra un mensaje de error si se intenta dividir por cero
            except ValueError:
                # Si no se pueden convertir los valores a números, muestra un mensaje de error
                error = "Error: Ingresar valores numéricos válidos"
        else:
            # Si alguno de los campos del formulario está vacío, muestra un mensaje de error
            error = "Error: Todos los campos son obligatorios"
    
    # Renderiza la plantilla HTML "calculadora.html", pasando el resultado y el mensaje de error como contexto
    return render(request, "calculadora.html", {"resultado": resultado, "error": error})
