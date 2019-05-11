from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viajes', views.viajes, name='viajes'),
    path('viajes/<int:id>', views.verViaje, name='verViaje'),
    path('viaje/<int:pk>/editar', views.editarViaje, name='editarViaje'),
    path('agregarViaje', views.agregarViaje, name='agregarViaje'),
    path('empleados', views.empleados, name='empleados'),
    path('empleados/<int:id>', views.verEmpleado, name='verEmpleado'),
    path('empleados/<int:id>/editarEmpleado',
         views.editarEmpleado, name='editarEmpleado'),
    path('agregarEmpleado',
         views.agregarEmpleado, name='agregarEmpleado'),
    path('vehiculos', views.vehiculos, name='vehiculos'),
    path('vehiculos/<int:pk>', views.verVehiculo, name='verVehiculo'),
    path('vehiculos/<int:pk>/editar', views.editarVehiculo, name='editarVehiculo'),
    path('agregarVehiculo',
         views.agregarVehiculo, name='agregarVehiculo'),
    path('estadistica', views.estadistica, name='estadistica')
]
