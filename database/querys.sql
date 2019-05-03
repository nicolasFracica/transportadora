--Ver todos los viajes

SELECT Viaje.idViaje AS Codigo, Ruta.nombre AS Ruta, Empleado.nombre AS Conductor, Vehiculo.placa, Viaje.descripcion
FROM Viaje INNER JOIN Ruta ON Viaje.idRuta = Ruta.idRuta
INNER JOIN viaje_vehiculo ON viaje_vehiculo.idViaje = Viaje.idViaje
INNER JOIN Vehiculo ON Vehiculo.idVehiculo = viaje_vehiculo.idVehiculo
INNER JOIN Vehiculo_empleado ON Vehiculo.idVehiculo = Vehiculo_empleado.idVehiculo
INNER JOIN Empleado ON Empleado.idEmpleado = Vehiculo_empleado.idEmpleado;