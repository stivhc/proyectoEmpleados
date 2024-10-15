from django.shortcuts import render


def mostrar_empleados(request):
    empleados = [
        "Ramírez Mantequilla",
        "Fideo Fidel",
        "Carlitos Lechuga",
        "Mario Hugo",
        "Juan Carlos Bodoque",
        "Tulio Tribiño",
    ]
    context = {"empleados": empleados}
    return render(
        request, "empleados/empleados.html", context
    )  # Create your views here.
