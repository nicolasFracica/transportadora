INSERT INTO Ruta (nombre)  
VALUES 
('Ruta A'),
( 'Ruta B'),
( 'Ruta C'),
( 'Ruta D'),
('Ruta E'),
( 'Ruta F'),
('Ruta G'),  
('Ruta H'),
( 'Ruta I'),
(' Ruta J'); 


INSERT INTO Vehiculo (modelo, placa)
VALUES
( 'Mazda', 'THF123'),
( 'Nissan', 'HNG432'),
('Chevrolet', 'JHF887'),
( 'Toyota', 'DRE531'),
( 'Renault', 'VCX964'),
('Mitsubishi', 'LLO765'),
('Suzuki', 'NIC496'),
( 'Ford', 'ADF345'),
('Chevrolet', 'GER376'),
('Mazda', 'LOI850');


INSERT INTO Viaje (duracion,cantidad, fecha, descripcion, idRuta)
VALUES
( 8, 800,'2019-03-29', 'Transporte de carga delicada', 3),
( 12,1000,'2018-11-02', 'Transporte material de obras', 5),
(16,1500, '2019-07-14', 'Transporte material de obras', 10),
(10, 780,'2019-06-25', 'Transporte material perecedero', 8),
(6, 950,'2017-08-22', 'Transporte de carga delicada', 7),
( 14, 1470,'2018-04-12', 'Transporte material de obras', 2),
(5, 2000,'2019-05-08', 'Transporte material de obras', 1),
(16, 1600,'2017-03-14', 'Transporte material de obras', 4),
(8, 3000,'2019-12-07', 'Transporte material de obras', 6),
(15, 840,'2019-01-22', 'Transporte material perecedero',9);

INSERT INTO Tipo_de_mantenimiento (nombre, descripcion) VALUES 
('Mantenimiento Correctivo', 'aquel que corrige los defectos observados en los equipamientos del vehiculo'),
('Mantenimiento Preventivo', 'destinado a la conservación de equipos de los vehiculos mediante la realización de revisión');


INSERT INTO Mantenimiento (fecha, idTipoMantenimiento)
VALUES
('2019-06-12',1),
( '2019-05-18',1),
( '2018-08-13',2),
('2018-03-10',1),
('2017-04-07',1),
( '2017-02-06',1),
( '2016-09-12',2),
( '2016-11-08',2),
('2015-07-23',1),
('2019-06-29',1);


INSERT INTO Ciudad (nombre, departamento)
VALUES
( 'Bogota', 'Cundinamarca'),
('Sogamoso', 'Boyaca'),
('Medellin', 'Antioquia'),
('Cali', 'Valle del Cauca'),
('Corinto', 'Cauca'),
('Villavicencio', 'Meta'),
('Arauca', 'Arauca'),
('Barranquilla', 'Atlantico'),
('Manizales', 'Caldas'),
('Florenia', 'Caqueta');


INSERT INTO Tipo_parada (nombre) 
VALUES 
('Inicio'), 
('Intermedia'),
('Fin');

INSERT INTO Cargo (nombre, descripcion)
values
('Administrador', 'Encargado de control'),
('Gerente', 'Encargado de la sucursal'),
('Conductor','Encargado de vehiculos');

INSERT INTO Tipo_de_carga (nombre, descripción) VALUES 
('Construcción', 'Material de construcción'), 
('Material arenoso', 'Carga en estado pulverizado'),
('Inflamable', 'Material con propiedades de combustión'),
('Conductor', 'Material con propiedades conductoras'),
('Orgánico', 'Producto orgánico perecedero');

INSERT INTO Carga (nombre, idTipoDeCarga)
VALUES
('Ladrillos', 1),
('Arena blanca', 2),
('Piedra de rio', 1),
('Madera', 3),
('Arena Oscura',  2),
('Cemento',  1),
('Cobre',  4),
('PVC',  1),
('Frutas', 5),
('Flores', 5);

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

INSERT INTO Tipo_de_pago (nombre, descripcion) VALUES
('Tarjeta Crédito', 'Pago a través de tarjeta de crédito'), 
('Tarjeta Débito', 'Pago a través de tarjeta de débito'),
('Efectivo', 'Pago en efectivo'),
('Cheque', 'Pago a través de cheque');

INSERT INTO Factura (fecha, valor, id_pago) VALUES
('2019-03-29', 1000000, 1),
('2018-11-02', 1500000, 3),
('2019-07-14', 2000000, 2),
('2019-03-29', 2500000, 4),
('2017-08-22', 3000000, 2),
('2018-04-12', 3500000, 1),
('2019-05-08', 4000000, 1),
('2017-03-14', 4500000, 4),
('2019-12-07', 500000, 3),
('2019-01-22', 550000, 1);

INSERT INTO Parada (nombre, direccion, idCiudad)
VALUES 
(' Parada 1','Calle 2 #5-2',1),
(' Parada 2','Calle 10 #6-7',2),
(' Parada 3','Calle 3 #4-9',3),
(' Parada 4','Calle 9 #2-11',4),
(' Parada 5','Calle 12 #16-4',5),
(' Parada 6','Calle 4 #8-2',6),
(' Parada 7','Cra 5 #17-6',7),
(' Parada 8','Cra 8 #5-12',8),
(' Parada 9','Cra 1 #6-15',9),
(' Parada 10','Cra 4 #6-9',10),
(' Parada 11','Calle 20 #63-71',5);

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



INSERT INTO Sucursal (idCiudad, nombre, direccion, nit)
VALUES
(1, 'Sucursal 1', 'Calle 164 #7b-46', 6439),
(2, 'Sucursal 2', 'Calle 45 #8a-89', 7640),
(3, 'Sucursal 3', 'Cra 15 #156-76', 8730),
(4, 'Sucursal 4', 'Cra 17 #124-66', 0981),
(5, 'Sucursal 5', 'Cra 19 #166-76', 5432),
(6, 'Sucursal 6', 'Cra 15 #156-76', 8730),
(7, 'Sucursal 7', 'Cra 13 #126-77', 7639),
(8, 'Sucursal 8', 'Calle 159 #11-06', 8739),
(9, 'Sucursal 9', 'Calle 129 #7b-98', 8766),
(10, 'Sucursal 10', 'Cra 10 #156-12', 1680);

INSERT INTO Cliente(nombre, idSucursal)
VALUES
('Jaime Arenas', 10), 
('Benito Díaz', 8), 
('Fabio Vazquez', 6), 
('Efraín Gonzales', 4),  
('Alvaro Santos', 2), 
('Juan Manuel Uribe', 9), 
('Gustavo Fajardo', 5), 
('Sergio Petro', 7), 
('Hugo Chavez', 3), 
('Ricardo Sanchez', 1);

INSERT INTO Empleado (nombre, fechaNacimiento, documento, idCargo, idSucursal)
values
('Juan Perez', '1985-06-09', 1010145577, 1,3),
('Esparza Roma', '1985-07-20', 1409660802, 2, 1),
('Arturo Cruz', '1980-08-15', 528965572, 3, 2),
('Manuel Molina', '1960-09-21', 10101557, 3, 3),
('Raúl Campos', '1990-01-05', 228218540, 2, 4),
('Oriol Leon', '1989-06-02', 528965572, 3, 5),
('Noa Marquez', '1989-03-30', 537621922, 2, 5),
('Valentina Gonzalez', '1978-04-01', 198175420, 3, 5),
('Luna Blanco', '1997-05-13', 501121962, 3, 3),
('Javier Ramirez', '2000-05-19', 614209054, 2, 2);


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

INSERT INTO Emp_ve_vi(idEmpleado, idViaje, idVehiculo)
Values
(3,1,1),
(9,2,2),
(4,3,3),
(9,4,4),
(4,5,5),
(8,6,6),
(9,7,7),
(3,8,8),
(6,9,9),
(9,10,10);

