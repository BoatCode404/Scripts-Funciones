#aca van las urls 

from django.urls import path # esto es para importar la libreria de djgango path 
from . import views # esto es para importar todo lo que esta en views.py

urlpatterns=[
    path("hola_mundo/",views.hola_mundo,name="hola_mundo")
]