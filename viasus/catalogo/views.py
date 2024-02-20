from django.http import HttpResponse
from .models import Producto
from django.shortcuts import render, redirect

# Create your views here.

def catalogo(request):
    if (request.GET.get('busqueda') == ''):
        result = Producto.objects.all()
    else:
        result = Producto.objects.filter(titulo__contains=request.GET.get('busqueda', ''))
    return render(request, "catalogo.html", {"result": result})

def buscar(request):
    return redirect(request, 'catalogo')

def pedidoprueba(request):
    print(request.POST.get("0010013000011", 0))
    print(request.POST.get("0010046000012", "nada"))
    return HttpResponse(f'''Del articulo 0010013000011 se pidio {request.POST.get('0010013000011', 0)} unidad(es)\n\n\t
                        Del articulo 0010046000012 se pidio {request.POST.get('0010046000012', "nada")} unidad(es)                      
                        ''')
