from django.urls import path
from . import views

urlpatterns = [
    path("", views.catalogue, name="catalogue"),
    path("index", views.index, name="index"),
    path("buscar", views.buscar),
    path("pedidoprueba", views.pedidoprueba),
]
