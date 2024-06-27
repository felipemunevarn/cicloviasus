from openpyxl import Workbook
from catalogo.models import Producto

def create_excel(request, daily_cart, customer):
    if (request != ""):
        cart = request.session.get("carro")
    else:
        cart = daily_cart
    user = request.user
    delivery_date = request.POST.get("deliveryDate")
    comments = request.POST.get("comments")
    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'Codigo'
    ws['B1'] = 'Nombre'
    ws['C1'] = 'Cantidad'
    ws['D1'] = 'Vendedor'
    ws['E1'] = 'Cliente'
    ws['F1'] = 'FechaEntrega'
    ws['G1'] = 'Comentarios'
    row = 2
    column = 1
    for item in cart:
        producto = Producto.objects.get(pk=item)
        ws.cell(row=row, column=column, value=producto.codigo)
        column += 1 
        ws.cell(row=row, column=column, value=producto.titulo)
        column += 1 
        ws.cell(row=row, column=column, value=cart[item]["cantidad"])
        column += 1 
        ws.cell(row=row, column=column, value=user.username)
        column += 1 
        ws.cell(row=row, column=column, value=customer)
        column += 1 
        ws.cell(row=row, column=column, value=delivery_date)
        column += 1 
        ws.cell(row=row, column=column, value=comments)
        column = 1 
        row += 1 
    wb.save('./report.xlsx')