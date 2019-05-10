--Ver todos los viajes

SELECT Viaje.idViaje AS Codigo, Ruta.nombre AS Ruta, Empleado.nombre AS Conductor, Vehiculo.placa, Viaje.descripcion
FROM Viaje INNER JOIN Ruta ON Viaje.idRuta = Ruta.idRuta
INNER JOIN viaje_vehiculo ON viaje_vehiculo.idViaje = Viaje.idViaje
INNER JOIN Vehiculo ON Vehiculo.idVehiculo = viaje_vehiculo.idVehiculo
INNER JOIN Vehiculo_empleado ON Vehiculo.idVehiculo = Vehiculo_empleado.idVehiculo
INNER JOIN Empleado ON Empleado.idEmpleado = Vehiculo_empleado.idEmpleado;


--Ver todos los empleados

SELECT Empleado.idEmpleado, Empleado.nombre, Empleado.documento, Cargo.nombre, Empleado.fechaNacimiento
FROM Empleado INNER JOIN Cargo ON Empleado.idCargo = Cargo.idCargo;


--Ver todos los vehículos

SELECT Vehiculo.idVehiculo, Vehiculo.modelo, Vehiculo.placa, Tipo_de_mantenimiento.nombre
FROM Vehiculo 
INNER JOIN Vehiculo_mantenimiento ON Vehiculo_mantenimiento.id_vehiculo = Vehiculo.idVehiculo 
INNER join Mantenimiento on Mantenimiento.idMantenimiento = Vehiculo_mantenimiento.id_mantenimiento
INNER JOIN Tipo_de_mantenimiento ON Tipo_de_mantenimiento.idTipoMantenimiento = Mantenimiento.idTipoMantenimiento
ORDER BY Vehiculo.idVehiculo ASC;
