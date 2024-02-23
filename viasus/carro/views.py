from django.shortcuts import render, redirect
from .Carro import Carro
from catalogo.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.agregar(producto=producto)

    return redirect("catalogo")

def carro(request):
    carro = Carro(request)
    # productos = 
    return render(request, "carro.html", carro)

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("catalogo")