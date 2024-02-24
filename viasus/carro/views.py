from django.shortcuts import render, redirect
from .Carro import Carro
from catalogo.models import Producto

# Create your views here.

def carro(request):
    carro = Carro(request)
    print(carro.carro)
    for item in carro.carro.items():
        print(item)
    return render(request, "carro.html")

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.agregar(producto=producto)
    return redirect("catalogo")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("catalogo")
