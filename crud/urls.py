from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viaje', views.viaje, name='viaje'),
    path('viaje/<int:pk>', views.verViaje, name='verViaje'),
    path('viaje/<int:pk>/editar', views.editarViaje, name='editarViaje'),
    path('viaje/<int:pk>/agregar', views.agregarViaje, name='agregarViaje'),
    path('empleado', views.empleado, name='empleado'),
    path('empleado/<int:pk>', views.verEmpleado, name='verEmpleado'),
    path('empleado/<int:pk>/editar', views.editarEmpleado, name='editarEmpleado'),
    path('empleado/<int:pk>/agregar',
         views.agregarEmpleado, name='agregarEmpleado'),
    path('vehiculo', views.vehiculo, name='vehiculo'),
    path('vehiculo/<int:pk>', views.verVehiculo, name='verVehiculo'),
    path('vehiculo/<int:pk>/editar', views.editarVehiculo, name='editarVehiculo'),
    path('vehiculo/<int:pk>/agregar',
         views.agregarVehiculo, name='agregarVehiculo'),
    path('estadistica', views.estadistica, name='estadistica')
]
