from django.shortcuts import render
from biblioteca.form import *

logued = False

def login(request):
  f = Form_Login(initial={'form_type':'Login'})

  return render(request, 'login.html', {'formulario':f})

def registro(request):
  f = Form_Register(initial={'form_type':'Registro'})

  return render(request, 'registro.html', {'formulario':f})


def validate(request):
  form = Form_Register(request.POST)
  validate = form.is_valid()
  registrado = False
  log = False
  msg = ""
  if request.method == 'POST':
    if request.POST.get('form_type') == 'Registro':
      if validate:
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        user = request.POST.get('user_name')
        pswd = request.POST.get('password')
        email = request.POST.get('email')
        d = request.POST.get('document')
        doc = DocumentType.objects.get(id=d)
        like = request.POST.get('likes')
        genre = Genre.objects.get(id=like)
        emails = []
        user_names = []
        for i in User.objects.all():
          emails.append(i.email)
          user_names.append(i.user_name)
        if email in emails or user in user_names:
          msg = "El usuario o el email ya se encuentra registrado."
        else:
          registrado = True
          User(first_name=firstname, last_name=lastname,
                      user_name=user, password=pswd, email=email,
                      document=doc, likes=genre
                      ).save()
          return render(request, 'validate.html', {'registrado':registrado})
    if request.POST.get('form_type') == 'Login':
      form = Form_Login(request.POST)
      username = request.POST.get('username')
      password = request.POST.get('password')
      for i in User.objects.all():
        if username == i.user_name and password == i.password:
          log = True
          logued = True
      if log:
        return render(request, 'validate.html', {'logueado':log})
      else:
        msg="Usuario o contraseña incorrectos"
        return render(request, 'login.html', {'msg':msg, 'formulario':form})

    else:
      form = Form_Register(request.POST)
      return render(request, 'registro.html', {'formulario':form, 'msg':msg})
