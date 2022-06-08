from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True , null=True)
    SKU = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)

