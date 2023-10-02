from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    apellido=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    telefono=models.IntegerField()

    def __str__(self):
        return f'{self.apellido} {self.nombre}'

class Productos(models.Model):
    codigo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=30)
    precio=models.IntegerField()

    def __str__(self):
        return self.descripcion

class Proveedores(models.Model):
    apellido=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    telefono=models.IntegerField()

    def __str__(self):
        return f'{self.apellido} {self.nombre}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
