from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viajes', views.viajes, name='viajes'),
    path('viajes/<int:id>', views.verViaje, name='verViaje'),
    path('viajes/<int:id>/editar', views.editarViaje, name='editarViaje'),
    path('viajes/<int:id>/eliminar', views.eliminarViaje, name='eliminarViaje'),
    path('agregarViaje', views.agregarViaje, name='agregarViaje'),
    path('empleados', views.empleados, name='empleados'),
    path('empleados/<int:id>', views.verEmpleado, name='verEmpleado'),
    path('empleados/<int:id>/editar',
         views.editarEmpleado, name='editarEmpleado'),
    path('empleados/<int:id>/eliminar',
         views.eliminarEmpleado, name="eliminarEmpleado"),
    path('agregarEmpleado',
         views.agregarEmpleado, name='agregarEmpleado'),
    path('vehiculos', views.vehiculos, name='vehiculos'),
    path('vehiculos/<int:id>', views.verVehiculo, name='verVehiculo'),
    path('vehiculos/<int:id>/editar', views.editarVehiculo, name='editarVehiculo'),
    path('vehiculos/<int:id>/eliminar',
         views.eliminarVehiculo, name='eliminarVehiculo'),
    path('agregarVehiculo',
         views.agregarVehiculo, name='agregarVehiculo'),
    path('estadistica', views.estadistica, name='estadistica'),
    path('test', views.get_data, name='test'),
    path('avisoEE/<int:id>', views.avisoEEmpleado, name='avisoEEmpleado'),
    path('avisoEV/<int:id>', views.avisoEVehiculo, name='avisoEVehiculo'),
    path('avisoEVI/<int:id>', views.avisoEViaje, name='avisoEViaje'),

]
