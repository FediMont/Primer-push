from unittest import defaultTestLoader
from django.db import models

# Create your models here.
class Bibliotecas(models.Model):
    nombre = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=60)
    apertura = models.CharField(max_length=100)
    link = models.URLField(max_length=100, blank=True, null=True)
    imagen = models.URLField(max_length=300, blank=True, null=True)
