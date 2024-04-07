from django import forms
from .models import Genre
from user.models import DocumentType

class Form_Login(forms.Form):
  username = forms.CharField(
    label='Nombre de usuario',
    widget=forms.TextInput(attrs={'class':'form__item'})
    )
  pswd = forms.CharField(
    label='Contraseña',
    widget=forms.PasswordInput(attrs={'class':'form__item'})
    )

class Form_Register(forms.Form):
  #class Meta:
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
  likes = forms.ModelMultipleChoiceField(
    queryset=Genre.objects.all(),
    label='Gustos (No obligatorio)',
    required = False,
    widget=forms.CheckboxSelectMultiple
    )
  #likes2 = forms.ModelMultipleChoiceField(
  #  required = False, widget=forms.CheckboxSelectMultiple, choices=genres)

  #libros = forms.CheckboxSelectMultiple(queryset=Genre.objects.all())
  '''
    model = Genre
    fields = ['titulo', 'generos']
    likes = {
      'generos':forms.CheckboxSelectMultiple
    }
  '''
  """
class SimpleForm(forms.Form):
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
  """