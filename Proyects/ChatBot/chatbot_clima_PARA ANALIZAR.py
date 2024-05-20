import pyowm

def obtener_clima(ciudad):
    api_key =   # Reemplaza 'TU_API_KEY' con tu propia clave de API
    owm = pyowm.OWM(api_key)
    try:
        observacion = owm.weather_manager().weather_at_place(ciudad)
        clima = observacion.weather
        temperatura = clima.temperature('celsius')['temp']
        estado = clima.detailed_status
        return f"El clima en {ciudad} es {estado} con una temperatura de {temperatura}°C."
    except pyowm.commons.exceptions.NotFoundError:
        return f"No se encontró información sobre el clima de {ciudad}."

def main():
    print("¡Hola! Soy un chatbot de clima. Puedo decirte el clima actual de cualquier ciudad.")
    while True:
        ciudad = input("Por favor, ingresa el nombre de la ciudad (o 'salir' para terminar): ")
        if ciudad.lower() == 'salir':
            print("¡Hasta luego!")
            break
        else:
            pronostico = obtener_clima(ciudad)
            print(pronostico)

if __name__ == "__main__":
    main()
