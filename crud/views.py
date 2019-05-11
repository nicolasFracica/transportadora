from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

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
    graph1()
    graph2()
    graph3()
    graph4()
    graph5()
    graph6()
    return render(request, 'crud/estadistica.html')

def get_data(request):
    name = "empty"
    if request.method == 'POST':
       name = request.POST.get("your_name")
    return render(request, 'crud/test.html', {'name': name})

def image(request):
    graph1()
    graph2()
    graph3()
    graph4()
    graph5()
    graph6()
    return render(request, 'crud/test.html')