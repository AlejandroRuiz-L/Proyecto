from django.shortcuts import render
from biblioteca.form import *
from django.views.generic import View
import re
#from biblioteca.views import homeLog
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
      f = Form_Login(request.POST)
      user = request.POST.get('username')
      password = request.POST.get('password')
      log = False
      for i in User.objects.all():
        if username == i.user_name and password == i.password:
          log = True
          break
      if log:
        user_log = User.objects.get(user_name=user)
        return render(request, 'update.html', {'user':user_log})
      else:
        msg="Usuario o contraseña incorrectos"
        return render(request, 'loginUpdate.html', {'msg':msg, 'formulario':f})

def recuperar(request):
  user = request.POST.get('username')

def loginUpdate(request):
  f = Form_Login(initial={'form_type':'LoginUpdate'})
  #user = request.POST.get('username')
  
  return render(request, 'loginUpdate.html', {})
