from django.http import HttpResponse # hay que añadir esta libreria para mostrar un mensaje como un html
from django.shortcuts import render

# Create your views here. aca es donde va toda la logica
def hola_mundo(request): # el request sirve para el metodo post y get se pone como atributo 
    return HttpResponse("Este es mi primer hola mundo con django 💖")

