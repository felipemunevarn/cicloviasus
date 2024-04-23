from datetime import datetime
from django.shortcuts import render
from carro.create_excel import create_excel
from carro.models import Pedido, PedidoProducto

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def resume(request):
    today = datetime.now().date().strftime("%Y-%m-%d")
    day_checkouts = Pedido.objects.filter(fecha_pedido__contains=today)
    carro = {}
    for checkout in day_checkouts:
        asked_products = PedidoProducto.objects.filter(pedido_id=checkout.id).select_related()
        for product in asked_products:
            if (str(product.producto.id) in carro):
                carro.get(str(product.producto.id)).update({ 'cantidad':carro.get(str(product.producto.id))["cantidad"] + product.cantidad})
            else:
                carro.update({str(product.producto.id): {}})
                carro.get(str(product.producto.id)).update({ 'cantidad': product.cantidad })
    create_excel(request="", daily_cart=carro)
    # send_mail_excel("", "", "", True, today)
    return render(request, "resume.html")
