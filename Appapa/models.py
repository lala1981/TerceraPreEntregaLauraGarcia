from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    empresa = models.CharField(max_length=40)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    precio = models.FloatField()
    
class Pago(models.Model):
    forma_pago = models.CharField(max_length=40)

