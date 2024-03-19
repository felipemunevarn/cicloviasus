from django.contrib import admin
from .models import Cliente, Pedido, PedidoProducto

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_display = ["fecha_pedido", "user", "cliente", "fecha_entrega"]

class PedidoProductoAdmin(admin.ModelAdmin):
    list_select_related = ["pedido", "producto"]

admin.site.register(Cliente)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoProducto, PedidoProductoAdmin)