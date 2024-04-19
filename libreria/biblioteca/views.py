from django.shortcuts import render, HttpResponse, redirect
from biblioteca.models import *
from user.views import User#Validates
#from user.models import User, DocumentType
from django.contrib.auth.decorators import login_required
from .form import Form_Login
#from django.views.decorators.csrf import csrf_protect
#rom django.utils.decorators import method_decorator
#from django.views.generic.base import View


def home(request):
  f = Form_Login(request.POST, initial={'form_type':'Login'})
  user = request.GET.get('user')
  if user != "":
    try:
      user_log = User.objects.get(user_name=user)
    except:
      user_log = '...'#user
  #if logued:
  #user = Validates.user_log
    books = Book.objects.all()
    genres = {}
    for book in books:
      genres['assets/%s'%(str(book.portada))] = {book:book.genre.all()}

    return render(request, 'index.html', {'generos':genres, 'user':user_log})
  else:
    return render(request, 'login.html', {'formulario':f})

  """
def homeLog(request, log):
  books = Book.objects.all()
  genres = {}
  for book in books:
    genres['assets/%s'%(str(book.portada))] = {book:book.genre.all()}
  return home
  """
  #return render(request, 'index.html', {'generos':genres, 'logueado':log})

def book(request):
  #p = Book.objects.all()
  id_book = request.GET.get('instancia')
  b = Book.objects.get(id = id_book)
  g = b.genre.all()
  book = {'assets/%s'%(str(b.portada)):{b:g}}

  return render(request, 'book.html', {'book':book})

def read(request):
  ins = request.GET.get('instancia')
  b = Book.objects.get(id=ins)
  book = {'%s'%(str(b.pdf)[4:]):b}

  return render(request, 'leer.html', {'libro':book, 'pdf':b.pdf})

def notFound(request):
  return render(request, 'notFound.html', {})


def biblioteca(request):
#  if logued:
  f = Form_Login(request.POST)
  user = request.POST.get('user')
  if user != "":
    books = {}
    for libro in Book.objects.all():
      genre = libro.genre.all()
      books['assets/%s'%(str(libro.portada))] = {libro:genre}
    size = len(books)

    return render(request, 'biblioteca.html', {'libros':books, 'size':size})
  else:
    return render(request, 'login.html', {'formulario':f})


def nosotros(request):
  books = Book.objects.all()

  return render(request, 'nosotros.html', {'libros':books})


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

def favoriteBook(request):
  id_book = request.GET.get('favorite')
  book = Book.objects.get(id=id_book)

  return render(request, 'favorite_book.html', {'libro':book})
