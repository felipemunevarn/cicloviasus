from django.shortcuts import render, redirect
from .Carro import Carro
from catalogo.models import Producto
from carro.models import Cliente

# Create your views here.

def carro(request):
    carro = Carro(request)
    clients = Cliente.objects.all()
    return render(request, "carro.html", {'clients':clients})

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.agregar(producto=producto)
    return redirect("catalogue")

def restar_unidad(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.restar(producto=producto)
    return redirect("carro:carro")

def sumar_unidad(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.sumar(producto=producto)
    return redirect("carro:carro")

def elminiar_producto(request, producto_id):
    carro = Carro(request)
    carro.eliminar(producto_id=producto_id)
    return redirect("carro:carro")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("catalogue")
