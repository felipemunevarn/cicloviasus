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

def index(request):
    # print(request.session.get("carro"))
    # print(total(request))
    # print(request.user.id)
    # chosen_customer = Cliente.objects.filter(nombre=request.POST.get("customer"))
    # if not chosen_customer:
    #     new_customer = Cliente()
    #     new_customer.nombre = request.POST.get("customer")
    #     print(new_customer)
    #     new_customer.save()
    # else:
    #     print(chosen_customer.values()[0]["id"])
    return HttpResponse(f'''Hola, saludos!!!''')
