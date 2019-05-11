from django.db import connection
import numpy as np
import pandas as pd
import sqlalchemy as sql
import matplotlib.pyplot as plt
import os
from IPython import get_ipython


parentDir = os.path.dirname(os.path.abspath(__file__))


def metodoquery():
    query = """



    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def verViajes():
    query = """
        SELECT Viaje.idViaje AS Codigo, Ruta.nombre AS Ruta, Empleado.nombre AS Conductor, Vehiculo.placa, Carga.nombre, Viaje.cantidad
        FROM Viaje 
	    INNER JOIN Ruta ON Viaje.idRuta = Ruta.idRuta
	    inner join Emp_ve_vi on Emp_ve_vi.idViaje = Viaje.idViaje 
        INNER JOIN Vehiculo ON Vehiculo.idVehiculo = Emp_ve_vi.idVehiculo
        INNER JOIN Empleado ON Empleado.idEmpleado = Emp_ve_vi.idEmpleado
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
        FROM Vehiculo 
	    INNER JOIN Vehiculo_mantenimiento ON Vehiculo_mantenimiento.id_vehiculo = Vehiculo.idVehiculo 
	    inner join mantenimiento on mantenimiento.idMantenimiento = Vehiculo_mantenimiento.id_mantenimiento
        INNER JOIN Tipo_de_mantenimiento ON Tipo_de_mantenimiento.idTipoMantenimiento = mantenimiento.idTipoMantenimiento
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


def empleado(id):
    query = """
        SELECT Empleado.idEmpleado, Empleado.nombre, Empleado.documento,
        Cargo.nombre, Empleado.fechaNacimiento
        FROM Empleado INNER JOIN Cargo ON
        Empleado.idCargo = Cargo.idCargo
        WHERE Empleado.idEmpleado =  """ + str(id)

    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def viaje(id):
    query = """
        SELECT Ruta.nombre, Empleado.nombre, Vehiculo.placa, Viaje.cantidad, Carga.nombre, 
        Tipo_de_carga.descripción, Viaje.fecha, Viaje.duracion, Factura.valor, Tipo_de_pago.nombre
        FROM Viaje INNER JOIN Ruta ON Viaje.idRuta = Ruta.idRuta
        INNER JOIN Emp_ve_vi ON Emp_ve_vi.idViaje = Viaje.idViaje
        INNER JOIN Empleado ON Emp_ve_vi.idEmpleado = Empleado.idEmpleado
        INNER JOIN Vehiculo ON Emp_ve_vi.idVehiculo = Vehiculo.idVehiculo
        INNER JOIN Carga_viaje ON Carga_viaje.idViaje = Viaje.idViaje
        INNER JOIN Carga ON Carga_viaje.idCarga = Carga.idCarga
        INNER JOIN Tipo_de_carga ON Tipo_de_carga.idTipoDeCarga = Carga.idTipoDeCarga
        INNER JOIN Viaje_factura ON Viaje_factura.idViaje = Viaje.idViaje
        INNER JOIN Factura ON Viaje_factura.idFactura = Factura.idFactura
        INNER JOIN Tipo_de_pago ON Tipo_de_pago.idTipo_de_pago = Factura.id_pago
        WHERE Viaje.idViaje = """ + str(id) + """ ORDER BY Viaje.idViaje """

    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row
