from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Oil (models.Model):
	nombre = models.CharField(max_length=30)
	fecha_emision = models.DateField()
	precio = models.DecimalField(max_digits = 8, decimal_places = 2)

