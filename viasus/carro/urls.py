from django.urls import path
from . import views

app_name = "carro" 

urlpatterns = [
    path("", views.carro, name="carro"),
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("restar/<producto_id>/", views.restar_unidad, name="restar"),
    path("eliminar/<int:producto_id>/", views.elminiar_producto, name="eliminar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]
