from django.db import models

# Create your models here.

class pasajero (models.Model):
    nombre=models.CharField(max_length=40, verbose_name="Nombre")
    apellido=models.CharField(max_length=40, verbose_name="Apellido")
    edad=models.IntegerField(max_length=3, verbose_name="Edad")
    email=models.EmailField(verbose_name="Email")
    telefono=models.IntegerField(max_length=10, verbose_name="Teléfono")


class destino (models.Model):
    destino=models.CharField(max_length=40)
    fecha=models.DateField()

class Preferencias (models.Model):
    equipaje=models.BooleanField()
    comidas=models.BooleanField()
    bebidas=models.BooleanField()

