from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    viajes = verViajes()
    context = {'Lista': viajes[-6:]}
    return render(request, 'crud/index.html', context)


def viajes(request):
    viajes = verViajes()
    context = {'Lista': viajes}
    return render(request, 'crud/viajes.html', context)


def verViaje(request, id):
    lista = verViajes()
    viajes = viaje(id)
    context = {'Viaje': viajes, 'Lista': lista}
    return render(request, 'crud/verViaje.html', context)


def editarViaje(request):
    return HttpResponse("Hola mundo desde editarViaje.")


def agregarViaje(request):
    empleados = getEmpleados()
    ciudades = getCiudades()
    contextCi = {'Ciudades': ciudades}
    contextEm = {'Empleados': empleados}
    return render(request, 'crud/agregarViaje.html', contextCi, contextEm)


def empleados(request):
    empleados = verEmpleados()
    context = {'Lista': empleados}
    return render(request, 'crud/empleados.html', context)


def verEmpleado(request, id):
    lista = verEmpleados()
    empleados = empleado(id)
    context = {'Empleado': empleados, 'Lista': lista}
    return render(request, 'crud/verEmpleado.html', context)


def editarEmpleado(request, id):
    empleados = empleado(id)
    context = {'Empleado': empleados}
    return render(request, 'crud/editarEmpleado.html', context)


def agregarEmpleado(request):
    return HttpResponse("Hola mundo desde agregarEmpleado.")


def vehiculos(request):
    vehiculos = verVehiculos()
    context = {'Lista': vehiculos}
    return render(request, 'crud/vehiculos.html', context)


def verVehiculo(request):
    return HttpResponse("Hola mundo desde verVehiculo.")


def editarVehiculo(request):
    return HttpResponse("Hola mundo desde editarVehiculo.")


def agregarVehiculo(request):
    return HttpResponse("Hola mundo desde agregarVehiculo.")


def estadistica(request):
    return HttpResponse("Hola mundo desde estadistica.")
