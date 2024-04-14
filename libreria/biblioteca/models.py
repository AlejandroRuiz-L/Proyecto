from django.db import models
#from django.urls import reverse #django 5.0.2
#used to generate URLs by reversing the URL pattern
#import uuid
#Reuqerida para las instancias de libros unicos
from datetime import date

# Create your models here.
class Genre(models.Model):
  """Modelo que representa un genero literario"""
  name = models.CharField(max_length=200)
  help_text = "Ingrese el genero literario (Ficción, fantasía, etc)."

  def __str__(self):
    """Representa la instancia particular del modelo"""
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
  date = models.DateField(default='1900-01-01')
  summary = models.TextField(max_length=1000, help_text='Ingrese una breve descripcion del libro')
  isbn = models.CharField('ISBN', max_length=30)
  genre = models.ManyToManyField(Genre, help_text="Seleccione un genero para el libro")
  portada = models.ImageField(default=None, blank=True)
  content = models.BinaryField(blank=True)
  pdf = models.FileField(upload_to='pdfs/', blank=True)

  def __str__(self):
    """String que representa al objeto Book"""
    return self.title

  #def get_absolute_url(self):#Django 5.0.2
  #  """Devuelve el URL a una instancia particular de Book"""
  #  return reverse('booo-detail', args=[str(self.id)])

#class BookInstance(models.Model):#Django 5.0.2
#  """Modelo que representa una copia especifica de un libro
#  (i.e. que puede ser prestado por la biblioteca)"""
#  id = models.UUIDField(primary_key=True, default=uuid.uuid4,help_text="id unico para el libro en toda la biblioteca")

class Author(models.Model):
  """Modelo que representa a un autor"""
  first_name = models.CharField(max_length=100, null=True)
  last_name = models.CharField(max_length=100, null=True)
  date_of_birth = models.DateField(null=True, blank=True)
  date_of_death = models.DateField('Died', null=True, blank=True)

  #def get_absolute_url(self):#Django 5.0.2
  #  """retorna la URL para acceder a una instancia particular del autor"""
  #  return reverse('author-detail', args=[str(self.id)])
  
  def __str__(self):
    """String para representar el objeto modelo"""
    return '%s, %s'%(self.last_name, self.first_name)

'''
class User(models.Model):
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length = 50)
  user_name = models.CharField(max_length = 50)
  email = models.EmailField()
  password = models.CharField(max_length = 50)
  likes = models.ManyToManyField(Genre, null = True)
  favorite_book = ForeignKey('Book', on_delete = models.SET_NULL, null = True)
  favorite_author = ForeignKey('Author', on_delete = models.SET_NULL, null = True)
'''