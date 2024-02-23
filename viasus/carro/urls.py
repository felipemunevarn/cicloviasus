from django.urls import path
from . import views

app_name = "carro" 

urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]
