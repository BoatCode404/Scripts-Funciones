from django.urls import path
from .views import calculadora_view

urlpatterns=[
    path('calculadora/',calculadora_view ,name='calculadora')
]