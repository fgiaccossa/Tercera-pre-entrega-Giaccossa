from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
class UserRegisterForm(UserCreationForm):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    edad=forms.IntegerField(max_value=99)
    email=forms.EmailField()
    telefono=forms.IntegerField()

class AuthenticationForm(AuthenticationFormForm):
    Usuario=forms.CharField(max_length=40)
    Password=forms.PasswordInput()


class Preferenciasform(forms.Form):
    equipaje=forms.BooleanField()
    comidas=forms.BooleanField()
    bebidas=forms.BooleanField()