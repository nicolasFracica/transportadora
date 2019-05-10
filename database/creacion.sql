CREATE table Ruta (
	idRuta int not null auto_increment primary key,
	nombre VARCHAR(150)
);

CREATE table Vehiculo (
	idVehiculo int  not null auto_increment primary key,
	modelo VARCHAR(150),
	placa VARCHAR(150)
);

CREATE table Viaje (
	idViaje int not null auto_increment primary key,
	duracion int,
	cantidad int,
	fecha date,
	descripcion VARCHAR(150),
    idRuta int,
	foreign key (idRuta) references Ruta (idRuta)
);

CREATE table Tipo_de_mantenimiento(
	idTipoMantenimiento INT not null auto_increment primary key,
	nombre VARCHAR(150),
	descripcion VARCHAR(150)
);

CREATE table Mantenimiento (
	idMantenimiento INT not null auto_increment primary key,
	fecha DATE,
	idTipoMantenimiento int,
	FOREIGN KEY (idTipoMantenimiento) REFERENCES Tipo_de_mantenimiento (idTipoMantenimiento)
);

CREATE TABLE Ciudad (
	idCiudad INT not null auto_increment primary key,
	nombre VARCHAR(150),
	departamento VARCHAR(150)
);

CREATE TABLE Tipo_parada (
	idTipoParada INT not null auto_increment primary key,
	nombre VARCHAR(150)
);

CREATE table Cargo(
idCargo INT not null auto_increment primary key,
nombre VARCHAR(150),
descripcion VARCHAR(150)
);

CREATE TABLE Tipo_de_carga (
   idTipoDeCarga INT not null auto_increment primary key,
   nombre VARCHAR(150),
   descripción VARCHAR(150)
);

CREATE TABLE Carga (
   idCarga INT not null auto_increment primary key,
   nombre VARCHAR(150),
   idTipoDeCarga INT,
   FOREIGN KEY(idTipoDeCarga) REFERENCES Tipo_de_carga(idTipoDeCarga)	
);

CREATE table Carga_viaje (
   idCarga INT,
   idViaje INT,
   FOREIGN KEY (idCarga) REFERENCES Carga (idCarga),
   FOREIGN KEY (idViaje) REFERENCES Viaje (idViaje)
);

CREATE table Tipo_de_pago(
	idTipo_de_pago INT not null auto_increment primary key,
	nombre VARCHAR(150),
	descripcion VARCHAR(150)
);

CREATE table Factura(
	idFactura INT not null auto_increment primary key,
	fecha DATE,
	valor INT, 
	id_pago INT, 
	FOREIGN KEY (id_pago) REFERENCES Tipo_de_pago(idTipo_de_pago)
);

CREATE TABLE Parada (
	idParada INT not null auto_increment primary key,
	nombre VARCHAR(150),
	direccion VARCHAR(150),
	idCiudad INT,
	FOREIGN KEY (idCiudad) REFERENCES Ciudad(idCiudad)
);

CREATE table Viaje_factura (
   idFactura INT,
   idViaje INT,
   fecha DATE,
   FOREIGN KEY (idFactura) REFERENCES Factura (idFactura),
   FOREIGN KEY (idViaje) REFERENCES Viaje (idViaje)
);

CREATE TABLE Tipo_parada_parada_ruta (
	idTipoParada INT,
	idParada INT,
	idRuta INT,
	FOREIGN KEY(idTipoParada) REFERENCES Tipo_parada(idTipoParada),
	FOREIGN KEY(idParada) REFERENCES Parada(idParada),
	FOREIGN KEY(idRuta) REFERENCES Ruta(idRuta)
);

CREATE table Sucursal(
	idSucursal INT not null auto_increment primary key,
	idCiudad INT,
	FOREIGN KEY (idCiudad) REFERENCES Ciudad(idCiudad),
	nombre VARCHAR(150),
	direccion VARCHAR(150),
	nit INT
);

CREATE table Cliente(
	idCliente INT not null auto_increment primary key,
	nombre VARCHAR(150),
	idSucursal INT,
	FOREIGN KEY (idSucursal) REFERENCES Sucursal(idSucursal)
);

CREATE table Empleado(
	idEmpleado INT not null auto_increment primary key,
	nombre VARCHAR(150),
	fechaNacimiento DATE,
	documento INT,
	idCargo INT,
	idSucursal INT,
	FOREIGN KEY (idCargo) REFERENCES Cargo(idCargo),
	FOREIGN KEY (idSucursal) REFERENCES Sucursal(idSucursal)
);

CREATE table Vehiculo_mantenimiento(
	id_vehiculo INT,
	id_mantenimiento INT,
	FOREIGN KEY (id_vehiculo) REFERENCES Vehiculo (idVehiculo),
	FOREIGN KEY (id_mantenimiento) REFERENCES Mantenimiento(idMantenimiento)
);

Create table Emp_ve_vi (
	idEmpleado int,
	idVehiculo int,
	idViaje int,
	FOREIGN KEY (idEmpleado) REFERENCES Empleado (idEmpleado),
 	FOREIGN KEY (idVehiculo) REFERENCES Vehiculo (idVehiculo ),
	FOREIGN KEY (idViaje) REFERENCES Viaje (idViaje)
);
