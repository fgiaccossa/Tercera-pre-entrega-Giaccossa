from django import forms

class pasajero (forms.ModelForm):
    nombre=models.CharField(max_length=40, verbose_name="Nombre")
    apellido=models.CharField(max_length=40, verbose_name="Apellido")
    edad=models.IntegerField(max_length=3, verbose_name="Edad")
    email=models.EmailField(verbose_name="Email")
    telefono=models.IntegerField(max_length=10, verbose_name="Teléfono")
