from django.db import models

# Create your models here.
class familiar(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    apellido = models.CharField(max_length=40)
    nacimiento = models.DateField()
    edad = models.IntegerField()
    vinculo = models.CharField(max_length=40)