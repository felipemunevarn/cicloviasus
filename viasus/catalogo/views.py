from django.http import HttpResponse
from django.template import RequestContext
from .models import Producto
from carro.models import Cliente
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
    chosen_customer = Cliente.objects.filter(nombre=request.POST.get("browser"))
    if not chosen_customer:
        new_customer = Cliente()
        new_customer.nombre = request.POST.get("browser")
        new_customer.direccion = "some"
        new_customer.telefono = "some"
        new_customer.correo = "some"
        print(new_customer)
        new_customer.save()
    else:
        print(chosen_customer.values()[0]["id"])
    return HttpResponse(f'''Hola, saludos!!!''')
