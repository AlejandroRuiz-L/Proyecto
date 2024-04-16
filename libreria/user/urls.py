from django.urls import path
from .views import Validates

urlpatterns = [
    path('', Validates.login, name = 'Login'),
    path('registro/', Validates.registro, name = 'Registro'),
    path('validate/', Validates.validate, name="Validar")
]