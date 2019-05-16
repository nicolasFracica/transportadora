from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
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


def editarViaje(request, id):
    viajes = viaje(id)
    rutas = getRutas()
    placas = getVehiculos()
    conductores = getEmpleados()
    materiales = getCarga()
    context = {'Viaje': viajes, 'Ruta': rutas,
               'Carro': placas, 'Empleado': conductores, 'Carga': materiales}
    return render(request, 'crud/editarViaje.html', context)


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
    lugar = getSucursal()
    context = {'Empleado': empleados, 'Sucursal': lugar}
    return render(request, 'crud/editarEmpleado.html', context)


def agregarEmpleado(request):
    return render(request, 'crud/agregarEmpleado.html')


def vehiculos(request):
    vehiculos = verVehiculos()
    context = {'Lista': vehiculos}
    return render(request, 'crud/vehiculos.html', context)


def verVehiculo(request, id):
    vehiculos = verVehiculos()
    carro = vehiculo(id)
    context = {'Lista': vehiculos, 'Vehiculo': carro}
    return render(request, 'crud/verVehiculo.html', context)


def editarVehiculo(request, id):
    carro = vehiculo(id)
    context = {'Vehiculo': carro}
    return render(request, 'crud/editarVehiculo.html', context)


def agregarVehiculo(request):
    return render(request, 'crud/agregarVehiculo.html')


def estadistica(request):
    graph1()
    graph2()
    graph3()
    graph4()
    graph5()
    graph6()
    return render(request, 'crud/estadistica.html')


def get_data(request):
    return render(request, 'crud/test.html')


def avisoEViaje(request, id):
    if request.method == 'POST':
        route = request.POST.get("ruta")
        name = request.POST.get("conductor")
        plate = request.POST.get("placa")
        weight = request.POST.get("peso")
        cargo = request.POST.get("material")
        date = request.POST.get("fecha")
        desc = request.POST.get("descripcion")
        hour = request.POST.get("duracion")
        price = request.POST.get("costo")
        pay = request.POST.get("pago")

        def idRuta(route):
            dict = {
                'Ruta A': 1,
                'Ruta B': 2,
                'Ruta C': 3,
                'Ruta D': 4,
                'Ruta E': 5,
                'Ruta F': 6,
                'Ruta G': 7,
                'Ruta H': 8,
                'Ruta I': 9,
                ' Ruta J': 10,
            }
            return dict.get(route)

        def idCarga(cargo):
            dict = {
                'Ladrillos': 1,
                'Arena blanca': 2,
                'Piedra de rio': 3,
                'Madera': 4,
                'Arena Oscura': 5,
                'Cemento': 6,
                'Cobre': 7,
                'PVC': 8,
                'Frutas': 9,
                'Flores': 10
            }
            return dict.get(cargo)

        def idPago(pay):
            dict = {
                'Tarjeta de Crédito': 1,
                'Tarjeta Débito': 2,
                'Efectivo': 3,
                'Cheque': 4
            }
            return dict.get(pay)
    pago = idPago(pay)
    camino = idRuta(route)
    material = idCarga(cargo)
    updateViaje(id, camino, name, plate, weight,
                material, date, desc, hour, price, pago)
    return render(request, 'crud/avisoEVI.html')


def avisoEEmpleado(request, id):
    if request.method == 'POST':
        name = request.POST.get("first_name")
        document = request.POST.get("documento")
        calendar = request.POST.get("inicio")
        work = request.POST.get("cargo")
        place = request.POST.get("sucursal")
        fecha = datetime.strptime(calendar, '%Y-%m-%d')
        date = fecha.date()
        date = date.strftime('%Y-%m-%d')

    def idCargo(work):
        dict = {
            'Administrador': 1,
            'Gerente': 2,
            'Conductor': 3
        }
        return dict.get(work)
    cargo = idCargo(work)

    def idSucursal(place):
        dict = {
            'Sucursal 1': 1,
            'Sucursal 2': 2,
            'Sucursal 3': 3,
            'Sucursal 4': 4,
            'Sucursal 5': 5,
            'Sucursal 6': 6,
            'Sucursal 7': 7,
            'Sucursal 8': 8,
            'Sucursal 9': 9,
            'Sucursal 10': 10,
        }
        return dict.get(place)
    sucursal = idSucursal(place)

    updateEmpleado(name, document, date, cargo, sucursal, id)
    return render(request, 'crud/avisoEEmpleado.html')


def eliminarEmpleado(request, id):
    deleteEmpleado(id)
    return render(request, 'crud/avisoDEmpleado.html')


def eliminarVehiculo(request, id):
    deleteVehiculo(id)
    return render(request, 'crud/avisoDVehiculo.html')


def eliminarViaje(request, id):
    deleteViaje(id)
    return render(request, 'crud/avisoDViaje.html')


def avisoEVehiculo(request, id):
    if request.method == 'POST':
        placa = request.POST.get("placas")
        modelo = request.POST.get("modelo")
        descripcion = request.POST.get("descripcion")
        fecha = request.POST.get("fecha")
    if descripcion == 'correción defectos en el vehiculo':
        mantenimiento = 1
    if descripcion == 'conservación de los vehiculos':
        mantenimiento = 2
    updateVehiculo(placa, modelo, id)
    updateMantenimiento(fecha, mantenimiento, id)
    return render(request, 'crud/avisoEV.html')


def image(request):
    graph1()
    graph2()
    graph3()
    graph4()
    graph5()
    graph6()
    return render(request, 'crud/test.html')
