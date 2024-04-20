from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name = 'Login'),
    path('registro/', registro, name = 'Registro'),
    path('validate/', validate, name="Validar"),
    path('update/', update, name = "Update")
]
