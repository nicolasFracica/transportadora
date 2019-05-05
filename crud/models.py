from django.db import connection

def metodoquery():
    query = """



    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row





def verViajes():
    query = """
        SELECT Viaje.idViaje AS Codigo, Ruta.nombre AS Ruta, Empleado.nombre AS Conductor, Vehiculo.placa, 
        Viaje.descripcion
        FROM Viaje INNER JOIN Ruta ON Viaje.idRuta = Ruta.idRuta
        INNER JOIN viaje_vehiculo ON viaje_vehiculo.idViaje = Viaje.idViaje
        INNER JOIN Vehiculo ON Vehiculo.idVehiculo = viaje_vehiculo.idVehiculo
        INNER JOIN Vehiculo_empleado ON Vehiculo.idVehiculo = Vehiculo_empleado.idVehiculo
        INNER JOIN Empleado ON Empleado.idEmpleado = Vehiculo_empleado.idEmpleado
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
