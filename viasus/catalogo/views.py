from .models import Producto
from django.shortcuts import render, redirect

# Create your views here.

def catalogue(request):
    if (request.GET.get('busqueda') == ''):
        result = Producto.objects.all().order_by("titulo")
    else:
        result = Producto.objects.filter(titulo__contains=request.GET.get('busqueda', '')).order_by("titulo")
    for product in result:
        product.precio = int(product.precio)
    return render(request, "catalogue.html", {"result": result})

def buscar(request):
    return redirect(request, 'catalogue')

