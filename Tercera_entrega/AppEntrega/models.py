from django.db import models

# Create your models here.

class Pasajero (models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    email=models.EmailField()
    telefono=models.IntegerField()


class Destino (models.Model):
    destino=models.CharField(max_length=40)
    salida=models.DateField()
    llegada = models.DateField()

class Preferencias (models.Model):
    equipaje=models.BooleanField(default=False, name="Incluir equipaje de bodeja")
    comidas=models.BooleanField(default=False, name="Incluir comidas durante el vuelo")
    bebidas=models.BooleanField(default=False, name="Incluir bebidas libres durante el vuelo")

