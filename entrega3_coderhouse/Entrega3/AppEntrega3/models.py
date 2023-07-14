from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    
class Peliculas(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

class Arriendos(models.Model):
    nombre_pelicula = models.CharField(max_length=100)
    fecha_arriendo = models.DateField()
    cliente_arriendo = models.CharField(max_length=50)