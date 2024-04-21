from django.shortcuts import render
from biblioteca.form import *
#from django.views.generic import View
import re
from biblioteca.views import Book
'''
class Validates(View):
  logued = False
  user_log = ''
'''
def login(request):
  f = Form_Login(initial={'form_type':'Login'})

  return render(request, 'login.html', {'formulario':f})

def registro(request):
  f = Form_Register(initial={'form_type':'Registro'})

  return render(request, 'registro.html', {'formulario':f})

def validate_email(email):
  pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  if re.match(pattern, email):
    return True
  else:
    return False
    
def validate_password(password):
  flag=False
  if len(password) >= 8:
    flag = True
  return flag

def update(request, user="", m=""):
  u = request.POST.get('username')
  log = True
  try:
    user = User.objects.get(user_name=u)
  except:
    try:
      u = user
    except:
      log = False
    return render(request, 'update.html', {'log':log})
  f = Form_Register(initial={'form_type':'Update', 'first_name':user.first_name, 'last_name':user.last_name, 'user_name':user.user_name, 'password':user.password, 'email':user.email, 'document':user.document, 'likes':user.likes})
  books = Book.objects.all()

  return render(request, 'update.html', {'formulario':f, 'user':user, 'log':log, 'books':books, 'msg':m})

def validate(request):
  #msg = ""
  if request.method == 'POST':
    if request.POST.get('form_type') == 'Registro':
      form = Form_Register(request.POST)
      registrado = False
      if form.is_valid():
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        user = request.POST.get('user_name')
        pswd = request.POST.get('password')
        email = request.POST.get('email')
        d = request.POST.get('document')
        like = request.POST.get('likes')
        user_names = []
        emails = []
        for i in User.objects.all():
          emails.append(i.email)
          user_names.append(i.user_name)
        if email in emails or user in user_names:
          msg = "El usuario o el email ya se encuentra registrado."
          return render(request, 'registro.html', {'formulario':form, 'msg':msg})
        else:
          try:
            doc = DocumentType.objects.get(id=d)
          except:
            doc = DocumentType.objects.get(document='No especificado')
          try:
            genre = Genre.objects.get(id=like)
          except:
            genre = Genre.objects.get(name='No especificado')
          registrado = True
          User(first_name=firstname, last_name=lastname,
                        user_name=user, password=pswd, email=email,
                        document=doc, likes=genre
                        ).save()
          return render(request, 'validate.html', {'registrado':registrado})
      else:
        return render(request, 'registro.html', {'formulario':form})
    if request.POST.get('form_type') == 'Login':
      form = Form_Login(request.POST)
      log = False
      username = request.POST.get('username')
      password = request.POST.get('password')
      for i in User.objects.all():
        if username == i.user_name and password == i.password:
          log = True
          break
      if log:
        user_log = User.objects.get(user_name=username)
        #return homeLog(request, user_log)
        return render(request, 'validate.html', {'logueado':log, 'user':user_log})
      else:
        msg="Usuario o contraseña incorrectos"
        return render(request, 'login.html', {'msg':msg, 'formulario':form})
    if request.POST.get('form_type') == 'LoginUpdate':
      fLog = Form_Login(request.POST)
      #fReg = Form_Register(initial={'form_type':'Update'})
      user = request.POST.get('username')
      password = request.POST.get('password')
      log = False
      for i in User.objects.all():
        if user == i.user_name and password == i.password:
          log = True
          break
      if log:
        user_log = User.objects.get(user_name=user)
        #return render(request, 'update.html', {'user':user_log, 'formulario':fReg})
        return update(request)
      else:
        msg="Usuario o contraseña incorrectos"
        return render(request, 'loginUpdate.html', {'msg':msg, 'formulario':fLog})

def recuperar(request):
  user = request.POST.get('username')
  pass

def loginUpdate(request):
  f = Form_Login(initial={'form_type':'LoginUpdate'})
  #user = request.POST.get('username')
  
  return render(request, 'loginUpdate.html', {'formulario':f})

def dataUpdated(request):
  user = request.POST.get('usuario')
  try:
    userLog = User.objects.get(user_name = user)
  except:
    msg = "!El usuario no existe!"
    return render(request, 'notFound.html', {'msg':msg})
  userName = request.POST.get('user_name')
  email = request.POST.get('email')
  emails = []
  userNames = []
  for i in User.objects.all():
    emails.append(i.email)
    userNames.append(i.user_name)
  if userName in userNames or email in emails:
    msg = "El usuario o el email ya existe"
    return update(request, user = user, m = msg)
  firstName = request.POST.get('first_name')
  lastName = request.POST.get('last_name')
  password = request.POST.get('password')
  doc = request.POST.get('document')
  document = DocumentType.objects.get(id=doc)
  like = request.POST.get('likes')
  likes = Genre.objects.get(id=like)
  book = request.POST.get('favoriteBook')
  favoriteBook = Book.objects.get(id=book)
  userLog.first_name = firstName
  userLog.last_name = lastName
  userLog.user_name = userName
  userLog.password = password
  userLog.email = email
  userLog.document = document
  userLog.likes = likes
  userLog.favorite_books.add(favoriteBook)
  userLog.save()
  msg = "!Los datos han sido actualizados!"

  return render(request, 'dataUpdated.html', {'msg':msg})

def deleteAccount(request):
  user = request.POST.get('instancia')
  log = True
  msg = "!Se ha eliminado la cuenta!"
  try:
    User.objects.get(user_name = user).delete()
  except:
    log = False
    msg = "!El usuario no existe!"

  return render(request, 'deleteAccount.html', {'msg':msg, 'log':log})