from django import forms
from .models import Genre
from user.models import DocumentType, User
#from django.contrib.auth.models import User

class Form_Login(forms.Form):
  username = forms.CharField(
    label='Nombre de usuario',
    widget=forms.TextInput(attrs={'class':'form__item'})
    )
  password = forms.CharField(
    label='Contraseña',
    widget=forms.PasswordInput(attrs={'class':'form__item'})
    )
  form_type = forms.CharField(
    widget=forms.HiddenInput
  )

class Form_Register(forms.ModelForm):
  #Formulario basado en modelos
  password = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
  form_type = forms.CharField(widget=forms.HiddenInput)

  class Meta:
    model = User
    fields = ['first_name','last_name','user_name','password','email','document','likes']
    '''
    widgets={
      'first_name':forms.TextInput(attrs={'class':'form__item'}),
      'last_name':forms.TextInput(attrs={'class':'form__item'}),
      'user_name':forms.TextInput(attrs={'class':'form__item'}),
      'password':forms.PasswordInput(attrs={'class':'form__item'}),
      'email':forms.EmailInput(attrs={'class':'form__item'}),
      'document':forms.Select(attrs={'class':'form__item'}),
      'likes':forms.Select(attrs={'class':'form__item'})
    }
    '''
    labels={
      'first_name':'Nombres',
      'last_name':'Apellidos',
      'user_name':'Nombre de usuario',
      'password':'Contraseña',
      'email':'Correo electrónico',
      'document':'Documento de identidad(No obligatorio)',
      'likes':'Género favorito(No obligatorio)'
    }

    def __init__(self, *args, **kwargs):
      super(Form_Register, self).__init__(*args, **kwargs)
      self.fields['Genero favorito'].queryset = Genre.objects.all()
  
  #formulario basado en funciones
  """
  firstname = forms.CharField(
    label = 'Nombres',
    widget=forms.TextInput(attrs={'class':'form__item'}))
  lastname = forms.CharField(
    label = 'Apellidos',
    widget=forms.TextInput(attrs={'class':'form__item'}))
  username = forms.CharField(
    label='Nombre de usuario',
    widget=forms.TextInput(attrs={'class':'form__item'}))
  pswd = forms.CharField(
    label='Contraseña',
    widget=forms.PasswordInput(attrs={'class':'form__item'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form__item'}))
  doc = forms.ModelChoiceField(
    queryset=DocumentType.objects.all(),
    label="Tipo de documento",
    widget=forms.Select(attrs={'class':'form__item'}),
    required=False
    )
  def generos():
    opciones = []
    for g in Genre.objects.all():
      opciones.append((f'{g.id}', f'{g.name}'))
    return opciones
  likes = forms.ChoiceField(
    #queryset=Genre.objects.all(),
    label='Género favorito (No obligatorio)',
    required = False,
    widget=forms.RadioSelect,
    choices=generos()
    )
  form_type = forms.CharField(
    widget=forms.HiddenInput
    )
  """