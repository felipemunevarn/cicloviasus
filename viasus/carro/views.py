from django.conf import settings
from django.shortcuts import render, redirect
from .Carro import Carro
from catalogo.models import Producto
from carro.models import Cliente, Pedido, PedidoProducto
from carro.context_processor import total
from django.core.mail import send_mail

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
    total_db = total(request)["total"]
    user = request.user
    delivery_date = request.POST.get("deliveryDate")
    if (delivery_date == ''):
        pedido = Pedido(cliente=customer, total=total_db, user=user)
    else:
        pedido = Pedido(cliente=customer, total=total_db, user=user, fecha_entrega=delivery_date)
    pedido.save()
    for item in request.session.get("carro"):
        producto = Producto.objects.get(pk=item)
        cantidad = request.session.get("carro")[item]["cantidad"]
        pedido_producto = PedidoProducto(pedido=pedido, producto=producto, cantidad=cantidad)
        pedido_producto.save()
    # send_email(request, customer, total_db, pedido)
    return render(request, "checkout.html")

def find_customer(request):
    chosen_customer = Cliente.objects.filter(nombre=request.POST.get("customer"))
    if not chosen_customer:
        chosen_customer = save_new_customer(request)
    return chosen_customer[0]

def save_new_customer(request):
    new_customer = Cliente()
    new_customer.nombre = request.POST.get("customer")
    new_customer.save()
    return new_customer

def send_email(request, customer, total_db, pedido):
    message = f"Venta del vendedor: {request.user.username} al cliente: {customer.nombre}\n"
    message += f'Total: ${total_db}\n\n'
    message += f'Codigo,Nombre,Cantidad\n'
    for item in request.session.get("carro"):
        producto = Producto.objects.get(pk=item)
        cantidad = request.session.get("carro")[item]["cantidad"]
        pedido_producto = PedidoProducto(pedido=pedido, producto=producto, cantidad=cantidad)
        pedido_producto.save()
        message += f'{producto.codigo},{producto.titulo},{cantidad}\n'
    subject = f"Venta del vendedor: {request.user.username} al cliente: {customer.nombre}"
    email_from = settings.EMAIL_HOST_USER
    recipient = ["felipemunevarn@gmail.com"]
    send_mail(subject, message, email_from, recipient)
