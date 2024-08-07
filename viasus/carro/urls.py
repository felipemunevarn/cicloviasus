from django.urls import path
from . import views

app_name = "carro" 

urlpatterns = [
    path("", views.carro, name="carro"),
    # path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    # path(r'^agregar/$', views.agregar_producto, name="agregar"),
    path("agregar/", views.agregar_producto, name="agregar"),
    path("restar/<producto_id>/", views.restar_unidad, name="restar"),
    path("sumar/<producto_id>/", views.sumar_unidad, name="sumar"),
    path("eliminar/<int:producto_id>/", views.elminiar_producto, name="eliminar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
    path("checkout", views.checkout, name="checkout"),
]
