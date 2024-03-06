from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Producto
import datetime

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=999, default=None, blank=True, null=True)
    telefono = models.CharField(max_length=20, default=None, blank=True, null=True)
    correo = models.CharField(max_length=13, default=None, blank=True, null=True)

    def __str__(self):
        return f'Nombre: {self.nombre}'
    
class Pedido(models.Model):
    fecha = models.CharField(max_length=20)
    total = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE) 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    cantidad = models.IntegerField()