from django.db import connection
import numpy as np
import pandas as pd
import matplotlib as plt


def metodoquery():
    query = """



    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def verViajes():
    query = """
        SELECT Viaje.idViaje AS Codigo, Ruta.nombre AS Ruta, Empleado.nombre AS Conductor, Vehiculo.placa, Carga.nombre
       
        FROM Viaje INNER JOIN Ruta ON Viaje.idRuta = Ruta.idRuta
        INNER JOIN viaje_vehiculo ON viaje_vehiculo.idViaje = Viaje.idViaje
        INNER JOIN Vehiculo ON Vehiculo.idVehiculo = viaje_vehiculo.idVehiculo
        INNER JOIN Vehiculo_empleado ON Vehiculo.idVehiculo = Vehiculo_empleado.idVehiculo
        INNER JOIN Empleado ON Empleado.idEmpleado = Vehiculo_empleado.idEmpleado
        INNER JOIN Carga_viaje on Carga_viaje.idViaje = Viaje.idViaje
        INNER JOIN Carga on Carga.idCarga = Carga_viaje.idCarga
        ORDER BY Viaje.idViaje
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def verEmpleados():
    query = """
        SELECT Empleado.idEmpleado, Empleado.nombre, Empleado.documento, Cargo.nombre, Empleado.fechaNacimiento
        FROM Empleado INNER JOIN Cargo ON Empleado.idCargo = Cargo.idCargo;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def verVehiculos():
    query = """
        SELECT Vehiculo.idVehiculo, Vehiculo.modelo, Vehiculo.placa, Tipo_de_mantenimiento.nombre
        FROM Vehiculo INNER JOIN Vehiculo_mantenimiento 
        ON Vehiculo_mantenimiento.id_vehiculo = Vehiculo.idVehiculo INNER JOIN Tipo_mantenimiento
        ON Vehiculo_mantenimiento.id_mantenimiento = Tipo_mantenimiento.id_mantenimiento
        INNER JOIN Tipo_de_mantenimiento 
        ON Tipo_de_mantenimiento.idTipoDeMantenimiento = Tipo_mantenimiento.id_tipo
        ORDER BY Vehiculo.idVehiculo ASC;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()
    return row


def getEmpleados():
    query = """
        Select e.nombre
        from empleado e
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def getCiudades():
    query = """
        Select c.nombre
        from ciudad c
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row
