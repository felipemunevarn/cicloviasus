from django.shortcuts import render, redirect
from .Carro import Carro
from catalogo.models import Producto

# Create your views here.

def agregar_producto(request, prodcuto_id):
    carro = Carro(request)
    producto = Producto.obejcts.get(id = prodcuto_id)
    carro.agregar(producto=producto)

    return redirect("catalogo")