INSERT INTO Ruta (idRuta, nombre)  
VALUES 
(1,'Ruta A'),
(2, 'Ruta B'),
(3, 'Ruta C'),
(4, 'Ruta D'),
(5, 'Ruta E'),
(6, 'Ruta F'),
(7, 'Ruta G'),  
(8, 'Ruta H'),
(9, 'Ruta I'),
(10,' Ruta J'); 


INSERT INTO Vehiculo (idVehiculo, modelo, placa)
VALUES
(1, 'Mazda', 'THF123'),
(2, 'Nissan', 'HNG432'),
(3, 'Chevrolet', 'JHF887'),
(4, 'Toyota', 'DRE531'),
(5, 'Renault', 'VCX964'),
(6, 'Mitsubishi', 'LLO765'),
(7, 'Suzuki', 'NIC496'),
(8, 'Ford', 'ADF345'),
(9, 'Chevrolet', 'GER376'),
(10, 'Mazda', 'LOI850');


INSERT INTO Viaje (idViaje, duracion, fecha, descripcion, idRuta)
VALUES
(1, 8, '2019-03-29', 'Transporte de carga delicada', 3),
(2, 12,'2018-11-02', 'Transporte material de obras', 5),
(3, 16, '2019-07-14', 'Transporte material de obras', 10),
(4, 10, '2019-06-25', 'Transporte material perecedero', 8),
(5, 6, '2017-08-22', 'Transporte de carga delicada', 7),
(6, 14, '2018-04-12', 'Transporte material de obras', 2),
(7, 5, '2019-05-08', 'Transporte material de obras', 1),
(8, 16, '2017-03-14', 'Transporte material de obras', 4),
(9, 8, '2019-12-07', 'Transporte material de obras', 6),
(10, 5, '2019-01-22', 'Transporte material perecedero',9);


INSERT INTO Mantenimiento (idMantenimiento, fecha)
VALUES
(1, '2019-06-12'),
(2, '2019-05-18'),
(3, '2018-08-13'),
(4, '2018-03-10'),
(5, '2017-04-07'),
(6, '2017-02-06'),
(7, '2016-09-12'),
(8, '2016-11-08'),
(9, '2015-07-23'),
(10, '2019-06-29');

INSERT INTO Tipo_de_mantenimiento ( idTipoDeMantenimiento, nombre, descripcion) VALUES 
(1, 'Mantenimiento Correctivo', 'aquel que corrige los defectos observados en los equipamientos del vehiculo'),
(2, 'Preventivo', 'destinado a la conservación de equipos de los vehiculos mediante la realización de revisión');

INSERT INTO Ciudad (idCiudad, nombre, departamento)
VALUES
(1, 'Bogota', 'Cundinamarca'),
(2, 'Sogamoso', 'Boyaca'),
(3,  'Medellin', 'Antioquia'),
(4, 'Cali', 'Valle del Cauca'),
(5, 'Corinto', 'Cauca'),
(6, 'Villavicencio', 'Meta'),
(7, 'Arauca', 'Arauca'),
(8,'Barranquilla', 'Atlantico'),
(9, 'Manizales', 'Caldas'),
(10, 'Florenia', 'Caqueta');


INSERT INTO Tipo_parada (idTipoParada, nombre) 
VALUES 
(1, 'Inicio'), 
(2,'Intermedia'),
(3, 'Fin');

INSERT INTO Cargo(idCargo, nombre, descripcion)
values
(1, 'Administrador', 'Encargado de control'),
(2, 'Gerente', 'Encargado de la sucursal'),
(3, 'Conductor', 'Encargado de vehiculos');

INSERT INTO Tipo_de_carga (idTipoDeCarga, nombre, descripción) VALUES 
(1,'Construcción', 'Material de construcción'), 
(2,'Material arenoso', 'Carga en estado pulverizado'),
(3,'Inflamable', 'Material con propiedades de combustión'),
(4,'Conductor', 'Material con propiedades conductoras'),
(5,'Orgánico', 'Producto orgánico perecedero');

INSERT INTO Carga (idCarga, nombre, idTipoDeCarga)
VALUES
(1, 'Ladrillos', 1),
(2, 'Arena blanca', 2),
(3, 'Piedra de rio', 1),
(4, 'Madera', 3),
(5, 'Arena Oscura',  2),
(6, 'Cemento',  1),
(7, 'Cobre',  4),
(8, 'PVC',  1),
(9, 'Frutas', 5),
(10, 'Flores', 5);

INSERT INTO Carga_viaje (idCarga, idViaje)
VALUES
(1, 2), 
(2, 3), 
(3, 6), 
(4, 1), 
(5, 7), 
(6, 8), 
(7, 5), 
(8, 9), 
(9, 10), 
(10, 4); 

INSERT INTO Tipo_de_pago (idTipo_de_pago, nombre, descripcion) VALUES
(1, 'Tarjeta Crédito', 'Pago a través de tarjeta de crédito'), 
(2, 'Tarjeta Débito', 'Pago a través de tarjeta de débito'),
(3, 'Efectivo', 'Pago en efectivo'),
(4, 'Cheque', 'Pago a través de cheque');

INSERT INTO Factura (idFactura, fecha, valor, id_pago) VALUES
(1, '2019-03-29', 1000000, 1),
(2, '2018-11-02', 1500000, 3),
(3, '2019-07-14', 2000000, 2),
(4, '2019-03-29', 2500000, 4),
(5, '2017-08-22', 3000000, 2),
(6, '2018-04-12', 3500000, 1),
(7, '2019-05-08', 4000000, 1),
(8, '2017-03-14', 4500000, 4),
(9, '2019-12-07', 500000, 3),
(10, '2019-01-22', 550000, 1);

INSERT INTO Parada ( idParada, nombre, direccion, idCiudad)
VALUES 
(1,' Parada 1','Calle 2 #5-2',1),
(2,' Parada 2','Calle 10 #6-7',2),
(3,' Parada 3','Calle 3 #4-9',3),
(4,' Parada 4','Calle 9 #2-11',4),
(5,' Parada 5','Calle 12 #16-4',5),
(6,' Parada 6','Calle 4 #8-2',6),
(7,' Parada 7','Cra 5 #17-6',7),
(8,' Parada 8','Cra 8 #5-12',8),
(9,' Parada 9','Cra 1 #6-15',9),
(10,' Parada 10','Cra 4 #6-9',10),
(11,' Parada 11','Calle 20 #63-71',5);

INSERT INTO Viaje_factura (idFactura, idViaje, fecha) values 
(1, 1, '2019-03-29'),
(2, 2 ,'2018-11-02'),
(3, 3, '2019-07-14'),
(4, 4, '2019-03-29'),
(5, 5, '2017-08-22'),
(6, 6, '2018-04-12'),
(7, 7, '2019-05-08'),
(8, 8, '2017-03-14'),
(9, 9, '2019-12-07'),
(10, 10, '2019-01-22');

INSERT INTO Sucursal (idSucursal, idCiudad, nombre, direccion, nit)
VALUES
(1, 1, 'Sucursal 1', 'Calle 164 #7b-46', 6439),
(2, 2, 'Sucursal 2', 'Calle 45 #8a-89', 7640),
(3, 3, 'Sucursal 3', 'Cra 15 #156-76', 8730),
(4, 4, 'Sucursal 4', 'Cra 17 #124-66', 0981),
(5, 5, 'Sucursal 5', 'Cra 19 #166-76', 5432),
(6, 6, 'Sucursal 6', 'Cra 15 #156-76', 8730),
(7, 7, 'Sucursal 7', 'Cra 13 #126-77', 7639),
(8, 8, 'Sucursal 8', 'Calle 159 #11-06', 8739),
(9, 9, 'Sucursal 9', 'Calle 129 #7b-98', 8766),
(10, 10, 'Sucursal 10', 'Cra 10 #156-12', 1680);

INSERT INTO Cliente(idCliente, nombre, idSucursal) VALUES
(1, 'Jaime Arenas', 10), 
(2, 'Benito Díaz', 8), 
(3, 'Fabio Vazquez', 6), 
(4, 'Efraín Gonzales', 4),  
(5, 'Alvaro Santos', 2), 
(6, 'Juan Manuel Uribe', 9), 
(7, 'Gustavo Fajardo', 5), 
(8, 'Sergio Petro', 7), 
(9, 'Hugo Chavez', 3), 
(10, 'Ricardo Sanchez', 1);

INSERT INTO Empleado (idEmpleado, nombre, fechaNacimiento, documento, idCargo, idSucursal)
values
(1, 'Juan Perez', '1985-06-09', 1010145577, 1,3),
(2, 'Esparza Roma', '1985-07-20', 1409660802, 2, 1),
(3, 'Arturo Cruz', '1980-08-15', 528965572, 3, 2),
(4, 'Manuel Molina', '1960-09-21', 10101557, 3, 3),
(5, 'Raúl Campos', '1990-01-05', 228218540, 2, 4),
(6, 'Oriol Leon', '1989-06-02', 528965572, 3, 5),
(7, 'Noa Marquez', '1989-03-30', 537621922, 2, 5),
(8, 'Valentina Gonzalez', '1978-04-01', 198175420, 3, 5),
(9, 'Luna Blanco', '1997-05-13', 501121962, 3, 3),
(10, 'Javier Ramirez', '2000-05-19', 614209054, 2, 2);

INSERT INTO Vehiculo_empleado(idVehiculo, idEmpleado) VALUES
(1,3),
(2,9),
(3,4),
(4,9),
(5,4),
(6,8),
(7,9),
(8,3),
(9,6),
(10,9);

INSERT INTO Vehiculo_mantenimiento(id_Vehiculo, id_Mantenimiento) VALUES
(3,1),
(10,2),
(9,3),
(5,4),
(2,5),
(7,6),
(1,7),
(4,8),
(8,9),
(6,10);

INSERT INTO Tipo_mantenimiento (id_mantenimiento, id_tipo) VALUES
(1,1),
(2,1),
(3,2),
(4,1),
(5,1),
(6,1),
(7,2),
(8,2),
(9,1),
(10,1);

INSERT INTO viaje_vehiculo(idViaje, idVehiculo) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9),
(10,10);

Insert into Tipo_parada_parada_ruta (idTipoParada, idParada, idRuta)
values
(1,2,1),
(2,4,1),
(2,5,1),
(3,6,1),
(1,1,2),
(3,5,2),
(1,11,3),
(2,10,3),
(3,9,3),
(1,8,4),
(2,6,4),
(2,7,4),
(2,3,4),
(3,1,4),
(1,5,5),
(2,3,5),
(2,1,5),
(3,6,5),
(1,8,6),
(3,10,6),
(1,4,7),
(2,5,7),
(2,6,7),
(3,7,7),
(1,10,8),
(2,9,8),
(2,8,8),
(2,7,8),
(3,6,8),
(1,2,9),
(2,4,9),
(3,6,9),
(1,1,10),
(2,3,10),
(2,5,10),
(2,7,10),
(2,9,10),
(3,10,10);

