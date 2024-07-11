from openpyxl import Workbook
from openpyxl import cell
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
    column_widths = [6,6,7,8,7,12,11]
    for item in cart:
        producto = Producto.objects.get(pk=item)
        ws.cell(row=row, column=column, value=producto.codigo)
        if (len(producto.codigo) > column_widths[column-1]):
            column_widths[column-1] = len(producto.codigo)
        column += 1 
        ws.cell(row=row, column=column, value=producto.titulo)
        if (len(producto.titulo) > column_widths[column-1]):
            column_widths[column-1] = len(producto.titulo)
        column += 1 
        ws.cell(row=row, column=column, value=cart[item]["cantidad"])
        column += 1 
        ws.cell(row=row, column=column, value=user.username)
        if (len(user.username) > column_widths[column-1]):
            column_widths[column-1] = len(user.username)
        column += 1 
        ws.cell(row=row, column=column, value=customer.nombre)
        if (len(customer.nombre) > column_widths[column-1]):
            column_widths[column-1] = len(customer.nombre)
        column += 1 
        ws.cell(row=row, column=column, value=delivery_date)
        if (len(delivery_date) > column_widths[column-1]):
            column_widths[column-1] = len(delivery_date)
        column += 1 
        ws.cell(row=row, column=column, value=comments)
        if (len(comments) > column_widths[column-1]):
            column_widths[column-1] = len(comments)
        column = 1 
        row += 1

    # Calculate column widths based on cell content

    for i, column_width in enumerate(column_widths, 1):
        column_letter = chr(64 + i)  # Convert index to column letter
        ws.column_dimensions[column_letter].width = column_width + 5
    wb.save('./report.xlsx')
    wb.close()

def resume_excel(cart):
    wb = Workbook()
    ws = wb.active

    ws['A1'] = 'Pedido'
    ws['B1'] = 'CodProducto'
    ws['C1'] = 'Nombre'
    ws['D1'] = 'Cantidad'
    ws['E1'] = 'Vendedor'
    ws['F1'] = 'Cliente'
    ws['G1'] = 'FechaEntrega'
    ws['H1'] = 'Comentarios'

    row = 2
    column = 1

    column_widths = [6,11,6,7,8,7,12,11]

    for item,products in cart.items():
        for prod,atts in products.items():
            ws.cell(row=row, column=column, value=item)
            if (len(item) > column_widths[column-1]):
                column_widths[column-1] = len(item)
            column += 1 

            ws.cell(row=row, column=column, value=prod)
            if (len(prod) > column_widths[column-1]):
                column_widths[column-1] = len(prod)
            column += 1

            ws.cell(row=row, column=column, value=atts['title'])
            if (len(atts['title']) > column_widths[column-1]):
                column_widths[column-1] = len(atts['title'])
            column += 1

            ws.cell(row=row, column=column, value=atts['qty'])
            column += 1

            ws.cell(row=row, column=column, value=atts['staff'])
            if (len(atts['staff']) > column_widths[column-1]):
                column_widths[column-1] = len(atts['staff'])
            column += 1 

            ws.cell(row=row, column=column, value=atts['customer'])
            if (len(atts['customer']) > column_widths[column-1]):
                column_widths[column-1] = len(atts['customer'])
            column += 1 

            ws.cell(row=row, column=column, value=atts['delivery_date'])
            column += 1 
            
            ws.cell(row=row, column=column, value=atts['comments'])
            if (len(atts['comments']) > column_widths[column-1]):
                column_widths[column-1] = len(atts['comments'])
            
            column = 1 
            row += 1

    # Calculate column widths based on cell content

    for i, column_width in enumerate(column_widths, 1):
        column_letter = chr(64 + i)  # Convert index to column letter
        ws.column_dimensions[column_letter].width = column_width + 5
    wb.save('./report.xlsx')
    wb.close()
