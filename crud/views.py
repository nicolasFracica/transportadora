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


def verViaje(request):
    return render(request, 'crud/verViajes.html')


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


def verEmpleado(request):
    return HttpResponse("Hola mundo desde verEmpleado.")


def editarEmpleado(request):
    return HttpResponse("Hola mundo desde editarEmpleado.")


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
