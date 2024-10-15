from django.urls import path
from . import views

urlpatterns = [
    path("mostrar_empleados/", views.mostrar_empleados, name="mostrar_empleados"),
]
