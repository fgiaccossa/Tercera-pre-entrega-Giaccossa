from django import forms

class Pasajeroform(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    edad=forms.IntegerField(max_value=99)
    email=forms.EmailField()
    telefono=forms.IntegerField(max_value=30)

class Contacto(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()
    consulta=forms.TextInput()

class Destinoform(forms.Form):
    destino=forms.CharField(max_length=40)
    salida=forms.DateField()
    llegada = forms.DateField()

class Preferenciasform(forms.Form):
    equipaje=forms.BooleanField()
    comidas=forms.BooleanField()
    bebidas=forms.BooleanField()