from django.db import models

# Create your models here.
#los diferentes modelos que se crearon dependiendo las clases que se imparten en el gimnasio
class Principiante (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Intermedio(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    peso = models.IntegerField()
    
class Avanzado (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    peso = models.IntegerField()
    nro_combates = models.IntegerField()
    
class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    peso = models.IntegerField()
    nro_combates = models.IntegerField()
    edad = models.IntegerField()
    
    