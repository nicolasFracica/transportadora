from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mundo desde index.")


def viaje(request):
    return HttpResponse("Hola mundo desde viaje.")


def verViaje(request):
    return HttpResponse("Hola mundo desde verViaje.")


def editarViaje(request):
    return HttpResponse("Hola mundo desde editarViaje.")


def agregarViaje(request):
    return HttpResponse("Hola mundo desde agregarViaje.")


def empleado(request):
    return HttpResponse("hola mundo desde empleado")


def verEmpleado(request):
    return HttpResponse("Hola mundo desde verEmpleado.")


def editarEmpleado(request):
    return HttpResponse("Hola mundo desde editarEmpleado.")


def agregarEmpleado(request):
    return HttpResponse("Hola mundo desde agregarEmpleado.")


def vehiculo(request):
    return HttpResponse("Hola mundo desde vehiculo.")


def verVehiculo(request):
    return HttpResponse("Hola mundo desde verVehiculo.")


def editarVehiculo(request):
    return HttpResponse("Hola mundo desde editarVehiculo.")


def agregarVehiculo(request):
    return HttpResponse("Hola mundo desde agregarVehiculo.")


def estadistica(request):
    return HttpResponse("Hola mundo desde estadistica.")
