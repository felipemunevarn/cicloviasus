from django.shortcuts import render, redirect
from .Carro import Carro
from catalogo.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request)
    print(producto_id)
    producto = Producto.objects.get(id = producto_id)
    carro.agregar(producto=producto)

    return redirect("catalogo")