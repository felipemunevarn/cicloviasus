from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.CharField(max_length=999)
    precio = models.FloatField(default=0.0)
    codigo = models.CharField(max_length=13)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Codigo: {self.codigo} Titulo: {self.titulo} Precio: {self.precio}'