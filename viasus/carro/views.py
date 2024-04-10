from django.shortcuts import render, redirect
from carro.create_excel import create_excel
from .Carro import Carro
from catalogo.models import Producto
from carro.models import Cliente, Pedido, PedidoProducto
from carro.context_processor import total
from django.core.mail import EmailMessage
from viasus.settings import BASE_DIR
import os

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
    comments = request.POST.get("comments")
    if (delivery_date == ''):
        pedido = Pedido(cliente=customer, total=total_db, user=user, comentarios=comments)
    else:
        pedido = Pedido(cliente=customer, total=total_db, user=user, comentarios=comments, fecha_entrega=delivery_date)
    pedido.save()
    for item in request.session.get("carro"):
        producto = Producto.objects.get(pk=item)
        cantidad = request.session.get("carro")[item]["cantidad"]
        pedido_producto = PedidoProducto(pedido=pedido, producto=producto, cantidad=cantidad)
        pedido_producto.save()
    create_excel(request, daily_cart="")
    send_mail_excel(request, customer, pedido, False, "")
    return render(request, "checkout.html")

def find_customer(request):
    chosen_customer = Cliente.objects.filter(nombre=request.POST.get("customer"))
    if not chosen_customer:
        save_new_customer(request)
        chosen_customer = Cliente.objects.filter(nombre=request.POST.get("customer"))
    return chosen_customer[0]

def save_new_customer(request):
    new_customer = Cliente()
    new_customer.nombre = request.POST.get("customer")
    new_customer.save()

def send_mail_excel(request, customer, pedido, daily, today):
    if (daily == False):
        email = EmailMessage(
            f"Pedido # {pedido.id} con fecha {pedido.fecha_pedido.now().date()}",
            f"Venta del vendedor {request.user.username} al cliente {customer.nombre}",
            "afmunene@gmail.com",
            ["felipemunevarn@gmail.com"]
        )
    else:
        email = EmailMessage(
            f"Resumen del dia con fecha {today}",
            f"En el adjunto el resumen de todas las ventas al cierre del dia {today}",
            "afmunene@gmail.com",
            ["felipemunevarn@gmail.com"]
        )
    # email.attach_file("C:/Users/Administrator/Documents/cicloviasus/viasus/report.xlsx")
    email.attach_file(os.path.join(BASE_DIR, 'report.xls'))
    email.send(fail_silently=False)
