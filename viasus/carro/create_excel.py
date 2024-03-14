from openpyxl import Workbook
from catalogo.models import Producto

def create_excel(request, daily_cart):
    if (request != ""):
        cart = request.session.get("carro")
    else:
        cart = daily_cart
    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'Codigo'
    ws['B1'] = 'Nombre'
    ws['C1'] = 'Cantidad'
    row = 2
    column = 1
    for item in cart:
        producto = Producto.objects.get(pk=item)
        ws.cell(row=row, column=column, value=producto.codigo)
        column += 1 
        ws.cell(row=row, column=column, value=producto.titulo)
        column += 1 
        ws.cell(row=row, column=column, value=cart[item]["cantidad"])
        column = 1 
        row += 1 
    wb.save('report.xlsx')