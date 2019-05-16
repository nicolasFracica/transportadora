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
	    inner JOIN Mantenimiento on Mantenimiento.idMantenimiento = Vehiculo_mantenimiento.id_mantenimiento
        INNER JOIN Tipo_de_mantenimiento ON Tipo_de_mantenimiento.idTipoMantenimiento = Mantenimiento.idTipoMantenimiento
        ORDER BY Vehiculo.idVehiculo ASC;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()
    return row


def getEmpleados():
    query = """
        Select e.nombre
        from Empleado e
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def getCiudades():
    query = """
        Select c.nombre
        from Ciudad c
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def getVehiculos():
    query = """
        Select v.placa
        from Vehiculo v
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def getRutas():
    query = """
        SELECT Ruta.nombre FROM Ruta
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def getCarga():
    query = """
        SELECT Carga.nombre FROM Carga
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def getSucursal():
    query = """
        SELECT Sucursal.nombre FROM Sucursal
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def viaje(id):
    query = """
        SELECT Ruta.nombre, Empleado.nombre, Vehiculo.placa, Viaje.cantidad, Carga.nombre,
        Viaje.descripcion, Viaje.fecha, Viaje.duracion, Factura.valor, Tipo_de_pago.nombre, Viaje.idViaje
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


def empleado(id):
    query = """
        SELECT Empleado.nombre, Empleado.documento, Empleado.fechaNacimiento, Cargo.nombre, Sucursal.nombre, Empleado.idEmpleado
        FROM Empleado INNER JOIN Sucursal ON Empleado.idSucursal = Sucursal.idSucursal
        INNER JOIN Cargo ON Empleado.idCargo = Cargo.idCargo
        WHERE Empleado.idEmpleado = """ + str(id)

    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def vehiculo(id):
    query = """
        SELECT Vehiculo.modelo, Vehiculo.placa, Tipo_de_mantenimiento.nombre, Tipo_de_mantenimiento.descripcion,
        Mantenimiento.fecha, Vehiculo.idVehiculo
        FROM Vehiculo INNER JOIN Vehiculo_mantenimiento ON Vehiculo_mantenimiento.id_vehiculo = Vehiculo.idVehiculo
	    INNER JOIN Mantenimiento on Mantenimiento.idMantenimiento = Vehiculo_mantenimiento.id_mantenimiento
        INNER JOIN Tipo_de_mantenimiento ON Tipo_de_mantenimiento.idTipoMantenimiento = Mantenimiento.idTipoMantenimiento
        WHERE Vehiculo.idVehiculo = """ + str(id)

    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def updateEmpleado(name, document, date, cargo, sucursal, id):
    query = """
        UPDATE Empleado
        SET nombre = '""" + name + """',
        fechaNacimiento = '""" + date + """',
        documento = """ + str(document) + """,
        idCargo = """ + str(cargo) + """,
        idSucursal = """ + str(sucursal) + """ WHERE idEmpleado = """ + str(id)

    with connection.cursor() as cursor:
        cursor.execute(query)


def updateVehiculo(placa, modelo, id):
    query = """
        UPDATE Vehiculo
        SET modelo = '""" + modelo + """',
        placa = '""" + placa + """' WHERE idVehiculo = """ + str(id)

    with connection.cursor() as cursor:
        cursor.execute(query)


def updateMantenimiento(fecha, mantenimiento, id):
    query2 = """
        INSERT INTO Mantenimiento(fecha, idTipoMantenimiento)
        VALUES('""" + fecha + """', """ + str(mantenimiento) + """)
        """
    query3 = """
        INSERT INTO Vehiculo_mantenimiento(id_vehiculo, id_mantenimiento)
        VALUES(""" + str(id) + """, """ + str(mantenimiento) + """)
        """

    with connection.cursor() as cursor:
        cursor.execute(query2)
        cursor.execute(query3)


def updateViaje(id, camino, name, plate, weight, material, date, desc, hour, price, pago):
    query1 = """
        UPDATE Viaje SET duracion = """ + hour + """, cantidad = """ + weight + """,
        fecha = '""" + date + """', descripcion = '""" + desc + """', 
        idRuta = """ + str(camino) + """ WHERE idViaje = """ + str(id)

    query2 = """
        UPDATE Carga_viaje SET idCarga = """ + str(material) + """ 
        WHERE idViaje = """ + str(id)

    query3 = """
        UPDATE Factura SET fecha = '""" + date + """', valor = """ + str(price) + """,
        id_pago = """ + str(pago) + """ WHERE idFactura = """ + str(id)

    query4 = """
        UPDATE Viaje_factura SET fecha = '""" + date + """' WHERE idFactura = """ + str(id)
    
    with connection.cursor() as cursor:
        cursor.execute(query1)
        cursor.execute(query2)
        cursor.execute(query3)
        cursor.execute(query4)
    

def deleteEmpleado(id):
    query = """
        DELETE FROM Empleado WHERE idEmpleado = """ + str(id)

    with connection.cursor() as cursor:
        cursor.execute(query)

def deleteVehiculo(id):
    query = """
        DELETE FROM Vehiculo WHERE idVehiculo = """ +str(id)

    with connection.cursor() as cursor:
        cursor.execute(query)

def deleteViaje(id):
    query = """
        DELETE FROM Viaje WHERE idViaje = """ +str(id)
    
    with connection.cursor() as cursor:
        cursor.execute(query)

def graph1():
    delimage(1)
    
    engine = sql.create_engine('mysql+mysqldb://root:Sergiop9@localhost:3306/Transportadora')
    busqueda2 = pd.read_sql_query("select ruta.nombre ruta,sum(factura.valor) valor,concat(ruta.nombre,' - ',sum(factura.valor)) concat, sum(factura.valor)*100/(select sum(factura.valor) from factura) Porcentaje from factura inner join viaje_factura on viaje_factura.idFactura = factura.idFactura inner join viaje on viaje.idViaje = viaje_factura.idViaje inner join ruta on ruta.idRuta = viaje.idRuta inner join ( select p.nombre parada, r.nombre ruta from tipo_parada_parada_ruta as tppr inner join parada p on p.idParada = tppr.idParada inner join tipo_parada tp on tp.idTipoParada = tppr.idTipoParada  inner join ruta r on r.idRuta = tppr.idRuta where tp.nombre = 'Fin') ruta_inicio on ruta.nombre = ruta_inicio.ruta group by ruta.nombre",engine)

    colors = ['seagreen','darkgreen','lawngreen','lime','springgreen','aquamarine','aqua','deepskyblue','lightseagreen','mediumaquamarine']
    plt.pie (busqueda2.Porcentaje, colors= colors, labels =busqueda2.ruta,radius = 2 ,autopct='%1.2f%%',shadow = True, explode = [0,0,0,0.1,0,0,0,0,0,0])
    plt.legend (labels =busqueda2.concat,loc="center left", bbox_to_anchor=(1.5, 1.2))

    
    plt.savefig(parentDir+"/static/images/graph1.png", bbox_inches='tight')
    plt.figure()

def graph2():
    delimage(2)
    engine = sql.create_engine('mysql+mysqldb://root:Sergiop9@localhost:3306/Transportadora')
    b1=pd.read_sql_query('select year(vi.fecha) fecha, month(vi.fecha) mes, sum(f.valor) valor from Empleado e inner join Emp_ve_vi evv on evv.idEmpleado = e.idEmpleado  inner join Vehiculo v on v.idVehiculo = evv.idVehiculo  inner join Viaje vi on vi.idViaje = evv.idViaje  inner join viaje_factura vf on vf.idViaje = vi.idViaje  inner join factura f on f.idFactura = vf.idFactura group by year(vi.fecha),month(vi.fecha) having fecha = "2019" ;',engine)
    b2=pd.read_sql_query('select year(vi.fecha) fecha, month(vi.fecha) mes, sum(f.valor) valor from Empleado e inner join Emp_ve_vi evv on evv.idEmpleado = e.idEmpleado  inner join Vehiculo v on v.idVehiculo = evv.idVehiculo  inner join Viaje vi on vi.idViaje = evv.idViaje  inner join viaje_factura vf on vf.idViaje = vi.idViaje  inner join factura f on f.idFactura = vf.idFactura group by year(vi.fecha),month(vi.fecha) having fecha = "2018" ;',engine)
    b3=pd.read_sql_query('select year(vi.fecha) fecha, month(vi.fecha) mes, sum(f.valor) valor from Empleado e inner join Emp_ve_vi evv on evv.idEmpleado = e.idEmpleado  inner join Vehiculo v on v.idVehiculo = evv.idVehiculo  inner join Viaje vi on vi.idViaje = evv.idViaje  inner join viaje_factura vf on vf.idViaje = vi.idViaje  inner join factura f on f.idFactura = vf.idFactura group by year(vi.fecha),month(vi.fecha) having fecha = "2017" ;',engine)
    plt.bar(b3.mes,b3.valor, label="2017",color = 'lime')
    plt.bar(b2.mes,b2.valor,label ="2018", color='yellowgreen')
    plt.bar(b1.mes,b1.valor, label ="2019",color = 'deepskyblue')
    plt.xticks([i for i in range(14)])
    plt.xlabel("Mes del año")
    plt.ylabel ("Ganancia")
    plt.legend()

    
    plt.savefig(parentDir+"/static/images/graph2.png", bbox_inches='tight')
    plt.figure()

def graph3():
    delimage(3)
    engine = sql.create_engine('mysql+mysqldb://root:Sergiop9@localhost:3306/Transportadora')
    b=pd.read_sql_query("SELECT Viaje.descripcion descripcion,Vehiculo.modelo modelo, COUNT(Vehiculo.modelo)AS Conteo FROM Viaje INNER JOIN Emp_ve_vi ON Emp_ve_vi.idViaje = Viaje.idViaje INNER JOIN Vehiculo ON Vehiculo.idVehiculo = Emp_ve_vi.idVehiculo WHERE Viaje.descripcion = 'Transporte material de obras' GROUP BY Vehiculo.modelo UNION SELECT Viaje.descripcion descripcion, Vehiculo.modelo modelo, COUNT(Vehiculo.modelo)AS conteo FROM Viaje INNER JOIN Emp_ve_vi ON Emp_ve_vi.idViaje = Viaje.idViaje INNER JOIN Vehiculo ON Vehiculo.idVehiculo = Emp_ve_vi.idVehiculo WHERE Viaje.descripcion = 'Transporte material perecedero' GROUP BY Vehiculo.modelo UNION SELECT Viaje.descripcion descripcion, Vehiculo.modelo modelo, COUNT(Vehiculo.modelo)AS conteo FROM Viaje INNER JOIN Emp_ve_vi ON Emp_ve_vi.idViaje = Viaje.idViaje INNER JOIN Vehiculo ON Vehiculo.idVehiculo = Emp_ve_vi.idVehiculo WHERE Viaje.descripcion = 'Transporte de carga delicada'GROUP BY Vehiculo.modelo;", engine)
    plt.style.use('seaborn-darkgrid')


    colors = ['lime', 'limegreen','springgreen', 'mediumspringgreen','mediumaquamarine', 'aquamarine','turquoise', 'cyan', 'darkturquoise']
    b.plot(kind='bar',x='modelo',y='Conteo', color=colors)
    plt.xlabel('Modelo',fontname="Arial", fontsize=15, fontweight='bold')
    plt.ylabel('# de Autos por Modelo',fontname="Arial", fontsize=15, fontweight='bold')
    plt.title('NÚMERO DE AUTOS POR MODELO',fontname="Arial", fontsize=18,fontstyle='italic', fontweight='bold')
    plt.xticks(size = 'medium', color = 'black', rotation = 45)
    plt.yticks(size = 'medium', color = 'black')
    
    plt.savefig(parentDir+"/static/images/graph3.png", bbox_inches='tight')
    plt.figure()

def graph4():
    delimage(4)
    engine = sql.create_engine('mysql+mysqldb://root:Sergiop9@localhost:3306/Transportadora')
    b=pd.read_sql_query("SELECT Viaje.descripcion descripcion,Vehiculo.modelo modelo, COUNT(Vehiculo.modelo)AS Conteo FROM Viaje INNER JOIN Emp_ve_vi ON Emp_ve_vi.idViaje = Viaje.idViaje INNER JOIN Vehiculo ON Vehiculo.idVehiculo = Emp_ve_vi.idVehiculo WHERE Viaje.descripcion = 'Transporte material de obras' GROUP BY Vehiculo.modelo UNION SELECT Viaje.descripcion descripcion, Vehiculo.modelo modelo, COUNT(Vehiculo.modelo)AS conteo FROM Viaje INNER JOIN Emp_ve_vi ON Emp_ve_vi.idViaje = Viaje.idViaje INNER JOIN Vehiculo ON Vehiculo.idVehiculo = Emp_ve_vi.idVehiculo WHERE Viaje.descripcion = 'Transporte material perecedero' GROUP BY Vehiculo.modelo UNION SELECT Viaje.descripcion descripcion, Vehiculo.modelo modelo, COUNT(Vehiculo.modelo)AS conteo FROM Viaje INNER JOIN Emp_ve_vi ON Emp_ve_vi.idViaje = Viaje.idViaje INNER JOIN Vehiculo ON Vehiculo.idVehiculo = Emp_ve_vi.idVehiculo WHERE Viaje.descripcion = 'Transporte de carga delicada'GROUP BY Vehiculo.modelo;", engine)
    plt.style.use('seaborn-darkgrid')


    colors = ['lime', 'limegreen','springgreen', 'mediumspringgreen','mediumaquamarine', 'aquamarine','turquoise', 'cyan', 'darkturquoise']
    b.plot(kind='bar',x='modelo',y='Conteo', color=colors)
    plt.xlabel('Modelo',fontname="Arial", fontsize=15, fontweight='bold')
    plt.ylabel('# de Autos por Modelo',fontname="Arial", fontsize=15, fontweight='bold')
    plt.title('NÚMERO DE AUTOS POR MODELO',fontname="Arial", fontsize=18,fontstyle='italic', fontweight='bold')
    plt.xticks(size = 'medium', color = 'black', rotation = 45)
    plt.yticks(size = 'medium', color = 'black')
    


    colors = [ 'cyan','turquoise', 'darkturquoise']
    b.groupby('descripcion')['modelo'].nunique().plot(kind='bar', color=colors)
    plt.xlabel('Descripción',fontname="Arial", fontsize=15, fontweight='bold')
    plt.ylabel('# de Autos por Descripción',fontname="Arial", fontsize=15, fontweight='bold')
    plt.title('NÚMERO DE AUTOS QUE TRANSPORTAN LOS TIPOS DE CARGA',fontname="Arial", fontsize=15,fontstyle='italic', fontweight='bold')
    plt.xticks(size = 'small', color = 'black', rotation = 45)
    plt.yticks(size = 'small', color = 'black')
    
    plt.savefig(parentDir+"/static/images/graph4.png", bbox_inches='tight')
    plt.figure()


def graph5():
    delimage(5)
    engine = sql.create_engine('mysql+mysqldb://root:Sergiop9@localhost:3306/Transportadora')
    b=pd.read_sql_query("SELECT Viaje.descripcion descripcion,Vehiculo.modelo modelo, COUNT(Vehiculo.modelo)AS Conteo FROM Viaje INNER JOIN Emp_ve_vi ON Emp_ve_vi.idViaje = Viaje.idViaje INNER JOIN Vehiculo ON Vehiculo.idVehiculo = Emp_ve_vi.idVehiculo WHERE Viaje.descripcion = 'Transporte material de obras' GROUP BY Vehiculo.modelo UNION SELECT Viaje.descripcion descripcion, Vehiculo.modelo modelo, COUNT(Vehiculo.modelo)AS conteo FROM Viaje INNER JOIN Emp_ve_vi ON Emp_ve_vi.idViaje = Viaje.idViaje INNER JOIN Vehiculo ON Vehiculo.idVehiculo = Emp_ve_vi.idVehiculo WHERE Viaje.descripcion = 'Transporte material perecedero' GROUP BY Vehiculo.modelo UNION SELECT Viaje.descripcion descripcion, Vehiculo.modelo modelo, COUNT(Vehiculo.modelo)AS conteo FROM Viaje INNER JOIN Emp_ve_vi ON Emp_ve_vi.idViaje = Viaje.idViaje INNER JOIN Vehiculo ON Vehiculo.idVehiculo = Emp_ve_vi.idVehiculo WHERE Viaje.descripcion = 'Transporte de carga delicada'GROUP BY Vehiculo.modelo;", engine)
    plt.style.use('seaborn-darkgrid')


    colors = ['lime', 'limegreen','springgreen', 'mediumspringgreen','mediumaquamarine', 'aquamarine','turquoise', 'cyan', 'darkturquoise']
    b.plot(kind='bar',x='modelo',y='Conteo', color=colors)
    plt.xlabel('Modelo',fontname="Arial", fontsize=15, fontweight='bold')
    plt.ylabel('# de Autos por Modelo',fontname="Arial", fontsize=15, fontweight='bold')
    plt.title('NÚMERO DE AUTOS POR MODELO',fontname="Arial", fontsize=18,fontstyle='italic', fontweight='bold')
    plt.xticks(size = 'medium', color = 'black', rotation = 45)
    plt.yticks(size = 'medium', color = 'black')
    


    colors = [ 'cyan','turquoise', 'darkturquoise']
    b.groupby('descripcion')['modelo'].nunique().plot(kind='bar', color=colors)
    plt.xlabel('Descripción',fontname="Arial", fontsize=15, fontweight='bold')
    plt.ylabel('# de Autos por Descripción',fontname="Arial", fontsize=15, fontweight='bold')
    plt.title('NÚMERO DE AUTOS QUE TRANSPORTAN LOS TIPOS DE CARGA',fontname="Arial", fontsize=15,fontstyle='italic', fontweight='bold')
    plt.xticks(size = 'small', color = 'black', rotation = 45)
    plt.yticks(size = 'small', color = 'black')



    colors = ['darksalmon', 'peachpuff','palegreen', 'paleturquoise','pink', 'wheat','khaki', 'lightskyblue', 'lightyellow']
    ax=b.groupby(['descripcion','modelo'])['Conteo'].size().unstack().plot(kind='bar',stacked=True, color=colors, label='Modelo')
    plt.xlabel('Descripción',fontname="Arial", fontsize=15, fontweight='bold')
    plt.ylabel('# de Autos por Descripción',fontname="Arial", fontsize=15, fontweight='bold')
    plt.suptitle('NÚMERO DE AUTOS QUE TRANSPORTAN LOS TIPOS DE CARGA',fontname="Arial", fontsize=13,fontstyle='italic', fontweight='bold')
    plt.title('(Especificación de los Modelos)',fontname="Arial", fontsize=11,fontstyle='italic', fontweight='bold')
    plt.xticks(size = 'small', color = 'black', rotation = 45)
    plt.yticks(size = 'small', color = 'black')
    chartBox = ax.get_position()
    ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
    ax.legend(loc='upper center', bbox_to_anchor=(1.3, 0.8), shadow=True, ncol=1)

    
    plt.savefig(parentDir+"/static/images/graph5.png", bbox_inches='tight')
    plt.figure()



def graph6():
    delimage(6)
    engine = sql.create_engine('mysql+mysqldb://root:Sergiop9@localhost:3306/Transportadora')
    a=pd.read_sql_query("SELECT tipoMante.nombre mantenimiento, v.placa, viaje.descripcion,viaje.duracion, f.valor FROM tipo_de_mantenimiento tipoMante INNER JOIN mantenimiento m ON m.idTipoMantenimiento = tipoMante.idTipoMantenimiento INNER JOIN vehiculo_mantenimiento vM ON m.idMantenimiento = vM.id_mantenimiento INNER JOIN vehiculo v ON vM.id_vehiculo = v.idVehiculo INNER JOIN Emp_ve_vi evv on evv.idVehiculo = v.idVehiculo INNER JOIN viaje viaje ON evv.idViaje = viaje.idViaje INNER JOIN viaje_factura vF ON viaje.idViaje = vF.idViaje INNER JOIN factura f ON vF.idFactura = f.idFactura INNER JOIN (SELECT F.idFactura AS idFactura, F.valor AS valorFacturado,viaje.duracion AS duracionFacturado, viaje.idViaje AS idViaje FROM viaje Viaje INNER JOIN viaje_factura vF ON Viaje.idViaje = vF.idViaje INNER JOIN factura F ON vF.idFactura = F.idFactura WHERE vF.idFactura = F.idFactura AND vF.idViaje = viaje.idViaje)Facturado ON vF.idViaje = Facturado.idFactura WHERE m.idTipoMantenimiento = 1 ORDER BY valor;",engine)
    plt.style.use('seaborn-darkgrid')
    colors=['springgreen', 'mediumspringgreen','mediumaquamarine', 'aquamarine','turquoise', 'cyan', 'darkturquoise']
    ax=a.plot(kind='bar',x='valor',y='duracion', color=colors)

    ax.text(5.5, 16.0, "JHF887", transform=ax.transData)
    ax.text(1.4, 16.0, "LADF345", transform=ax.transData)
    ax.text(-0.5, 15.0, "LOI850", transform=ax.transData)
    ax.text(3.5, 14.0, "LLO765", transform=ax.transData)
    ax.text(0.5, 12.0, "HNG432", transform=ax.transData)
    ax.text(2.5, 6.0, "VCX964", transform=ax.transData)
    ax.text(4.6, 5.0, "NIC496", transform=ax.transData)

    plt.xlabel('Valor',fontname="Arial", fontsize=15, fontweight='bold')
    plt.ylabel('Duración del Viaje (Horas)',fontname="Arial", fontsize=15, fontweight='bold')
    plt.xticks(size = 'medium', color = 'black', rotation = 45)
    plt.yticks(size = 'medium', color = 'black')
    plt.title("VALOR DE LOS VIAJES, CON SU RESPECTIVA DURACIÓN", fontname="Arial", fontsize=18,fontstyle='italic', fontweight='bold')


    chartBox = ax.get_position()
    ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
    ax.legend(loc='upper center', bbox_to_anchor=(3, 0.8), shadow=True, ncol=1)
        
    plt.savefig(parentDir+"/static/images/graph6.png", bbox_inches='tight')
    plt.figure()

def delimage(img):
    strFile = parentDir+"static/images/graph"+str(img)+".png"
    if os.path.isfile(strFile):
        os.remove(strFile)   # Opt.: os.system("rm "+strFile)
