import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .Carro import Carro
from catalogo.models import Producto
from carro.models import Cliente, Pedido, PedidoProducto
from carro.context_processor import total

# Create your views here.

def carro(request):
    carro = Carro(request)
    customers = Cliente.objects.all()
    return render(request, "carro.html", {'customers':customers})

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

def checkout(request):
    customer = find_customer(request)
    date = datetime.date.today().isoformat()
    total_db = total(request)["total"]
    user = request.user
    pedido = Pedido(cliente=customer, fecha=date, total=total_db, user=user)
    pedido.save()
    for item in request.session.get("carro"):
        producto = Producto.objects.get(pk=item)
        cantidad = request.session.get("carro")[item]["cantidad"]
        pedido_producto = PedidoProducto(pedido=pedido, producto=producto, cantidad=cantidad)
        pedido_producto.save()
    return HttpResponse(f'''Pedido guardado exitosamente''')

def find_customer(request):
    chosen_customer = Cliente.objects.filter(nombre=request.POST.get("customer"))
    if not chosen_customer:
        new_customer = Cliente()
        new_customer.nombre = request.POST.get("customer")
        if (new_customer.nombre == ""):
            print("ERROR")
            # CORREGIR POSIBLE ERROR
        else:
            new_customer.save()
            return(chosen_customer)
    else:
        chosen_customer = Cliente.objects.filter(nombre=request.POST.get("customer"))
    return(chosen_customer[0])