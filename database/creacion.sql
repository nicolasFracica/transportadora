CREATE table Ruta (
	idRuta int primary key,
	nombre VARCHAR(150)
);

CREATE table Vehiculo (
	idVehiculo int primary key,
	modelo VARCHAR(150),
	placa VARCHAR(150)
);

CREATE table Viaje (
	idViaje int primary key,
	duracion int,
	fecha date,
	descripcion VARCHAR(150),
    idRuta int,
	foreign key (idRuta) references Ruta (idRuta)
);

CREATE table Mantenimiento (
	idMantenimiento INT PRIMARY KEY,
	fecha DATE
);

CREATE table Tipo_de_mantenimiento(
	idTipoDeMantenimiento INT PRIMARY KEY,
	nombre VARCHAR(150),
	descripcion VARCHAR(150)
);

CREATE TABLE Ciudad (
	idCiudad INT PRIMARY KEY,
	nombre VARCHAR(150),
	departamento VARCHAR(150)
);

CREATE TABLE Tipo_parada (
	idTipoParada INT PRIMARY KEY,
	nombre VARCHAR(150)
);

CREATE table Cargo(
    idCargo INT PRIMARY KEY,
    nombre VARCHAR(150),
    descripcion VARCHAR(150)
);

CREATE TABLE Tipo_de_carga (
   idTipoDeCarga INT PRIMARY KEY,
   nombre VARCHAR(150),
   descripción VARCHAR(150)
);

CREATE TABLE Carga (
   idCarga INT PRIMARY KEY,
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
	idTipo_de_pago INT PRIMARY KEY,
	nombre VARCHAR(150),
	descripcion VARCHAR(150)
);

CREATE table Factura(
	idFactura INT PRIMARY KEY,
	fecha DATE,
	valor INT, 
	id_pago INT, 
	FOREIGN KEY (id_pago) REFERENCES Tipo_de_pago(idTipo_de_pago)
);

CREATE TABLE Parada (
	idParada INT PRIMARY KEY,
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
    idSucursal INT PRIMARY KEY,
    idCiudad INT,
    FOREIGN KEY (idCiudad) REFERENCES Ciudad(idCiudad),
    nombre VARCHAR(150),
    direccion VARCHAR(150),
    nit INT
);

CREATE table Cliente(
    idCliente INT PRIMARY KEY,
    nombre VARCHAR(150),
    idSucursal INT,
    FOREIGN KEY (idSucursal) REFERENCES Sucursal(idSucursal)
);

CREATE table Empleado(
    idEmpleado INT PRIMARY KEY,
    nombre VARCHAR(150),
    fechaNacimiento DATE,
    documento INT,
    idCargo INT,
    idSucursal INT,
    FOREIGN KEY (idCargo) REFERENCES Cargo(idCargo),
    FOREIGN KEY (idSucursal) REFERENCES Sucursal(idSucursal)
);

CREATE table Vehiculo_empleado (
	idVehiculo INT,
    idEmpleado INT,
	FOREIGN KEY (idEmpleado) REFERENCES Empleado (idEmpleado),
	FOREIGN KEY (idVehiculo) REFERENCES Vehiculo (idVehiculo)
);

CREATE table Vehiculo_mantenimiento(
	id_vehiculo INT,
	id_mantenimiento INT,
	FOREIGN KEY (id_vehiculo) REFERENCES Vehiculo (idVehiculo),
	FOREIGN KEY (id_mantenimiento) REFERENCES Mantenimiento(idMantenimiento)
);

CREATE table Tipo_mantenimiento(
	id_mantenimiento INT,
	id_tipo INT, 
	FOREIGN KEY (id_mantenimiento) REFERENCES Mantenimiento(idMantenimiento),
	FOREIGN KEY (id_tipo) REFERENCES Tipo_de_mantenimiento (idTipoDeMantenimiento)
);

CREATE table viaje_vehiculo (
	idViaje INT,
    idVehiculo INT,
	FOREIGN KEY (idViaje) REFERENCES  Viaje (idViaje),
	FOREIGN KEY (idVehiculo) REFERENCES  Vehiculo (idVehiculo)
);
