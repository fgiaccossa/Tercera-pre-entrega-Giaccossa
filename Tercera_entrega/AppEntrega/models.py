from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre=models.CharField(max_lenght=40)
    camada=models.IntegerField()

class Estudiante (models.Model):
    nombre=models.CharField(max_lenght=40)
    apellido=models.CharField(max_lenght=40)
    email=models.EmailField()

class Profesor (models.Model):
    nombre=models.CharField(max_lenght=40)
    apellido=models.CharField(max_lenght=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

class Entregable (models.Model):
    nombre=models.CharField(max_lenght=40)
    FechaDeEntrega=models.DateField()
    entregado=models.BooleanField()
