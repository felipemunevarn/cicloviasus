from django.http import HttpResponse
from django.template import RequestContext
from .models import Producto
from django.shortcuts import render, redirect
from carro.context_processor import total

# Create your views here.

def catalogue(request):
    if (request.GET.get('busqueda') == ''):
        result = Producto.objects.all()
    else:
        result = Producto.objects.filter(titulo__contains=request.GET.get('busqueda', ''))
    return render(request, "catalogue.html", {"result": result})

def buscar(request):
    return redirect(request, 'catalogue')

def pedidoprueba(request):
    return HttpResponse(f'''Del articulo 0010013000011 se pidio {request.POST.get('0010013000011', 0)} unidad(es)\n\n\t
                        Del articulo 0010046000012 se pidio {request.POST.get('0010046000012', "nada")} unidad(es)                      
                        ''')
def index(request):
    print(request.session.get("carro"))
    print(total(request))
    print(request.user.id)
    print(request.GET.get("browser"))
    return HttpResponse(f'''Hola, saludos!!!''')
