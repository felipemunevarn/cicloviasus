from django.urls import path
from . import views

urlpatterns = [
    path("registro", views.View_Register.as_view(), name="signin"),
    path("", views.close_session, name="close"),
    path("ingresar", views.user_login, name="login"),
]
