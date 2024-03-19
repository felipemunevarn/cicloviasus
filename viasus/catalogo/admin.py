from django.contrib import admin
from .models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'codigo']
    list_filter = ['activo']
    list_display = ['codigo', 'titulo', 'precio', 'activo']
    list_editable = ['precio', 'activo']

admin.site.register(Producto, ProductoAdmin)