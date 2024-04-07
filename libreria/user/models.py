from django.db import models
from biblioteca.models import *

# Create your models here.
class DocumentType(models.Model):
  document = models.CharField(max_length=30, help_text='Tipo de documento', null=True)
  doc = models.CharField(max_length=10, help_text='Sigla del tipo de documento')

  def __str__(self):
    return '%s (%s)'%(self.doc, self.document)

class User(models.Model):
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length = 50)
  user_name = models.CharField(max_length = 50)
  password = models.CharField(max_length = 50)
  email = models.EmailField()
  likes = models.ManyToManyField(Genre)

  def __str__(self):
    return '%s %s'%(self.first_name, self.last_name)