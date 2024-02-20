from django.urls import path
from . import views

urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("buscar", views.buscar),
    path("pedidoprueba", views.pedidoprueba),
]
