from django.urls import path
from .views import calculadora

urlpatterns=[
    path('cal/',calculadora,name='cal')
]