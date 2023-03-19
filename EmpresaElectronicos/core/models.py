from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
    def __str__(self):
        return f'{self.id} - {self.nombre} {self.apellido} - {self.email}'

class Empleado(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    puesto=models.CharField(max_length=20)
    email=models.EmailField()
    def __str__(self):
        return f'{self.id} - {self.nombre} {self.apellido} - {self.puesto} - {self.email}'

class Producto(models.Model):
    nombre=models.CharField(max_length=20)
    precio=models.FloatField()
    def __str__(self):
        return f'{self.id} - {self.nombre} - ${self.precio}'