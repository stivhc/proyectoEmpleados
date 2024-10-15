from django.urls import path
from . import views

urlpatterns = [
    path("empleados/", views.mostrar_empleados, name="mostrar_empleados"),
]
