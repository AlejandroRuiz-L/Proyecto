from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name = 'Login'),
    path('registro/', registro, name = 'Registro'),
    path('validate/', validate, name="Validar"),
    path('loginUpdate/', loginUpdate, name = "LoginUpdate"),
    path('update/', update, name = "Update"),
    path('dataUpdated', dataUpdated, name = 'Updated'),
    path('deleteAccount', deleteAccount, name = "DeleteAccount")
]
