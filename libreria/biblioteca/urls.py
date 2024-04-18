"""libreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

#Urls Django 1.8.19
'''
from django.conf.urls import include, url
from django.contrib import admin
from biblioteca.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name = 'Home'),
    url(r'^login/', login, name = 'Login'),
    url(r'^biblioteca/', biblioteca, name = 'Biblioteca'),
    url(r'^contacto/', contacto, name = 'Contacto'),
    url(r'^recuperar/', recuperar, name = 'Recuperar'),
    url(r'^registro/', registro, name = 'Registro'),
    url(r'^buscar/', buscar, name = 'Buscar'),
    url(r'^consultar/', consultar, name = 'Consultar'),
    url(r'nosotros/', nosotros, name = 'Nosotros'),
    url(r'validate/', Validate.form, name = 'Validar'),
    url(r'book/', book, name = "Book"),
]
'''

#urls Django 5.0.2
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name = 'Home'),
    path('biblioteca/', biblioteca, name = 'Biblioteca'),
    path('nosotros/', nosotros, name = 'Nosotros'),
    path('recuperar/', recuperar, name = 'Recuperar'),
    path('buscar/', buscar, name = 'Buscar'),
    path('consultar/', consultar, name = 'Consultar'),
    path('book/', book, name = "Book"),
    path('leer/', read, name = 'Read'),
    path('favorite/', favoriteBook, name="Favorite_book")
]
    #path('validate/', Validate.form, name = 'Validar'),
