from django.shortcuts import render
from carro.create_excel import resume_excel
from carro.models import Pedido, PedidoProducto
from django.http import HttpResponse
from django.conf import settings
import os

# Create your views here.

def download_file(request):
    req_date = request.POST.get('resumeDate')
    resume = Pedido.objects.filter(fecha_pedido__contains=req_date)
    carro = {}
    for checkout in resume:
        asked_products = PedidoProducto.objects.filter(pedido_id=checkout.id).select_related()
        carro.update({str(checkout.id): {}})
        for product in asked_products:
            carro.get(str(checkout.id)).update({str(product.producto.id): {}}) 
            carro.get(str(checkout.id)).get(str(product.producto.id)).update({
                'title': product.producto.titulo,
                'qty': product.cantidad,
                'staff': checkout.user.username,
                'customer': checkout.cliente.nombre,
                'delivery_date': checkout.fecha_entrega,
                'comments': checkout.comentarios
            }) 
    resume_excel(cart=carro)

    # File path to the file you want to download
    file_path = os.path.join(settings.BASE_DIR, 'report.xlsx')
    
    # Open the file
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="report.xlsx"'
        return response

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def resume(request):
    # send_mail_excel("", "", "", True, today)
    return render(request, "resume.html", {})
