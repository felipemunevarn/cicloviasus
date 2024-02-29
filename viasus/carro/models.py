from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=999, default=None)
    telefono = models.CharField(max_length=20, default=None)
    correo = models.CharField(max_length=13, default=None)

    def __str__(self):
        return f'Nombre: {self.nombre}'