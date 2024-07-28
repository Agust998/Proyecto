from django.db import models

# Create your models here.

class alumno(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

class profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    profesion = models.CharField(max_length=40)
    
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()