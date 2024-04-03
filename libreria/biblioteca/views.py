from django.shortcuts import render
from biblioteca.models import *
#from django.views.decorators.csrf import csrf_protect
#rom django.utils.decorators import method_decorator
#from django.views.generic.base import View
#from static.img import libros as lb, img

# Create your views here.
from django.shortcuts import render

def home(request):
  books = Book.objects.all()
  genres = {}
  for book in books:
    genres['assets/%s'%(str(book.portada))] = {book:book.genre.all()}

  return render(request, 'index.html', {'generos':genres})

def login(request):

  return render(request, 'login.html', {})

def registro(request):
  
  generos = Genre.objects.all()

  return render(request, 'registro.html', {'generos':generos})

def book(request):
  #p = Book.objects.all()
  id_book = request.GET.get('instancia')
  b = Book.objects.get(id = id_book)
  g = b.genre.all()
  book = {'assets/%s'%(str(b.portada)):{b:g}}

  #for libro in p:
    #libro.portada = '%s'%(str(libro.portada)[2:])
    #libro.save()
  

  return render(request, 'book.html', {'book':book})

def validate(request):
  return render(request, 'validate.html', {})
#validar sin terminar
'''
@method_decorator(csrf_protect)
class Validate(View):
  def form(self, request):
    validado = False

    return render(request, 'validate.html', {'validado':validado})
'''
def biblioteca(request):
  size = Book.objects.all().count()
  books1 = {}
  books2 = {}
  books3 = {}
  id_book = 1
  #limit = int(size / 3)
  #for i in gens:
  #  gen.append(i)
  while True:
    try:
      query = Book.objects.get(id=id_book)
      genre = query.genre.all()
      if query:
        if id_book > size:
          break
        elif len(books1) < 10:
          books1['assets/%s'%(str(query.portada))] = {query:genre}
          id_book += 1
    
        elif len(books2) < 10:
          books2['assets/%s'%(str(query.portada))] = {query:genre}
          id_book += 1
        
        else:
          books3['assets/%s'%(str(query.portada))] = {query:genre}
          id_book += 1
    except:
      id_book += 1
  
  return render(request, 'biblioteca.html', {'books1':books1, 'books2':books2,
    'books3':books3, 'size':size})

def contacto(request):
  return render(request, 'contacto.html', {})

def recuperar(request):
  return render(request, 'recuperar_contrasena.html', {})

def consultar(request):
  libros = {}
  libro1 = Book.objects.get(id=1)
  libro2 = Book.objects.get(id=2)
  genre1 = libro1.genre.all()
  genre2 = libro2.genre.all()
  libros['assets/%s'%(str(libro1.portada))] = {libro1:genre1}
  libros['assets/%s'%(str(libro2.portada))] = {libro2:genre2}

  return render(request, 'consulta.html', {'libros':libros})

def buscar(request):

  name = request.GET.get('buscar_libro')
  books = Book.objects.all()
  search = {}
  for book in books:
    gen = book.genre.all()
    if name.lower() in book.title.lower():
      search['assets/%s'%(str(book.portada))] = {gen:book}
  
  cnt = len(search)

  return render(request, 'buscar.html', {'cnt':cnt, 'search':search})
  
def nosotros(request):
  return render(request, 'nosotros.html', {})