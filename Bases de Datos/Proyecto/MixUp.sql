create database MixUp
drop database MixUp

create table empleado(
	nss int not null,
	nombreP char(15),
	apPat char(15),
	apMat char(15),
	fNac date,
	direccion char(15),
	salario decimal(10, 2),
	sexo char,
	constraint cveEmpleado
		primary key (nss)
);
	insert into empleado values (1,'Zenobia','Felipe','Cruz','2002-10-05','Cuauhtémoc',10000.00,'F');
	insert into empleado values (2,'Brayan','Castillo','Olguin','2001-09-11','Chapultepec',12000.00,'M');
	insert into empleado values (3,'Einar','Rivera','Hernández','2002-01-20','Naucalpan',8000.00,'M');
	insert into empleado values (4,'Luis','Torres','Abonce','2000-07-24','Coacalco',9000.00,'M');
	insert into empleado values (5,'Josué','Vázquez','Martínez','2002-12-21','Tultitlan',11000.00,'M');
	insert into empleado values (6,'Diana','Sanchez','Perez','1995-10-05','Tlalnepantla',10000.00,'F');
--Esquema Cliente
create table cliente(
	codigoC int not null default 0,
	nombreP char(15),
	apPat char(15),
	apMat char(15),
	edad int,
	constraint cvecodigoC
		primary key (codigoC)
);
	insert into cliente values (10,'Juan','López','López',19);
	insert into cliente values (11,'Yoseline','Sánchez','López',20);
	insert into cliente values (12,'Sara','Ruiz','Martínez',18);
	insert into cliente values (13,'Enrique','Tellez','Rodriguez',21);
	insert into cliente values (14,'Daniela','García','Lara',19);
--Esquema ClienteFrecuente
create table CFrecuente(
	codigoCF int not null,
	cantCompras int not null,
	constraint cveCF
		primary key (codigoCF),
	constraint cveCliente
		foreign key (codigoCF) references cliente(codigoC)
		on delete set default on update cascade
);
	insert into CFrecuente values (12,10);
	insert into CFrecuente values (13,10);
	insert into CFrecuente values (14,12);
--Esquema Tarjeta
create table tarjeta(
	codigoCF int not null default 0,
	fechaCad date not null,
	constraint cveTarjeta
		primary key (fechaCad, codigoCF),
	constraint cveCodigoClient
		foreign key (codigoCF) references CFrecuente(codigoCF)
		on delete set default on update cascade
);

	insert into tarjeta values (13,'2021-12-21');
	insert into tarjeta values (14,'2022-01-21');
--Esquema Venta
create table venta(
	numVenta int not null default 0,
	nssVen int not null,
	codigoC int not null,
	montoV decimal(10, 2),
	constraint cveVenta
		primary key (numVenta, nssVen, codigoC),
	constraint cveVen
		foreign key (nssVen) references empleado (nss)
		on delete set default on update cascade,
	constraint cveClien
		foreign key (codigoC) references cliente(codigoC)
		on delete set default on update cascade
);
	insert into venta values (1,1,10,700.00);
	insert into venta values (2,2,12,400.00);
	insert into venta values (3,3,11,600.00);
	insert into venta values (4,4,14,1000.00);
	insert into venta values (5,5,13,400.00);
--Esquema Producto
create table producto(
	codigoP int not null default 0,
	nombrePr char(20) not null,
	precio decimal(10, 2),
	pasillo char(15) not null,
	tipo_p char(2) not null,
	formato char(15) not null,
	anioPublic date,
	genero char(15),
	constraint cveProducto
		primary key (codigoP)
);
	insert into producto values (1,'Donda',700.00,1,'M','Vinyl','2021-08-29','Hip-hop');
	insert into producto values (2,'Call Me If You',500.00,1,'M','CD','2021-06-25','Hip-hop');
	insert into producto values (3,'Memento',400.00,2,'V','DVD','2001-03-16','Suspenso');
	insert into producto values (4,'Sueños de fuga',600.00,2,'V','Blu-ray','1994-09-23','Drama');
	insert into producto values (5,'La metamorfosis',400.00,3,'L','Pasta dura','2005-05-09','Novela');
	insert into producto values (6,'1984',200.00,3,'L','Pasta blanda','2020-06-01','Ciencia ficción');
	insert into producto values (7,'Dark souls',1000.00,4,'VD','CD','2011-10-04','Souls');
	insert into producto values (8,'Half-life',120.00,4,'VD','Digital','1998-11-08','FPS');
--Esquema ProductoDescuento
create table prodDescuento(
	codigoP int not null,
	descuento decimal(10, 2),
	constraint cvepD
		primary key (codigoP, descuento),
	constraint cveProd
		foreign key (codigoP) references producto (codigoP)
		on delete set default on update cascade
);
	insert into prodDescuento values (7,100.00);
--Esquema ProductoPremio
create table prodPremio(
	codigoP int not null,
	premio char(30),
	constraint cvePP
		primary key (codigoP, premio),
	constraint cveProd
		foreign key (codigoP) references producto (codigoP)
		on delete set default on update cascade
);
	insert into prodPremio values (4,'Oscar mejor película');
	insert into prodPremio values (8,'GOTY 1999');
--Esquema Música
create table musica(
	codigoPM int not null,
	artista char(30),
	nTracks int,
	constraint cvemusica
		primary key (codigoPM),
	constraint cveCodigoMus
		foreign key (codigoPM) references producto (codigoP)
		on delete set default on update cascade
);

	insert into musica values (1,'Kanye West',27);
	insert into musica values (2,'Tyler, the creator',16);
--Esquema Video
create table video(
	codigoPV int not null,
	duraciónMin int,
	director char(30),
	constraint cveVideo
		primary key(codigoPV),
	constraint cveCodigoPV
		foreign key (codigoPV) references producto (codigoP)
);
	insert into video values (3,113,'Christopher Nolan');
	insert into video values (4,142,'Frank Darabont');
--Esquema Actores
create table actores(
	codigoPVid int not null,
	nombreActor char(30),
	constraint cveActores
		primary key (codigoPVid, nombreActor),
	constraint cveCodigoPVid
		foreign key (codigoPVid) references video (codigoPV)
);
	insert into actores values (3,'Guy Pearce');
	insert into actores values (3,'Carrie-Anne Moss');
	insert into actores values (3,'Joe Pantoliano');
	insert into actores values (4,'Tim Robbins');
	insert into actores values (4,'Morgan Freeman');
--Esquema Libro
create table libro(
	codigoPL int not null,
	pags int,
	autor char(30),
	editorial char(30),
	constraint cveLibro
		primary key (codigoPL),
	constraint cveCodigoPL
		foreign key (codigoPL) references producto(codigoP)
);
	insert into libro values (5,352,'George Orwell','Random House');
	insert into libro values (6,176,'Franz Kafka','Akal');
--Esquema Videojuego
create table videojuego(
	codigoPVD int not null,
	desarrolladoPor char(30),
	plataforma char(25),
	constraint cveVideojuego
		primary key (codigoPVD),
	constraint cveCodigoJue
		foreign key (codigoPVD) references producto (codigoP)
);
	insert into videojuego values (7,'From Software','Xbox 360');
	insert into videojuego values (8,'Valve','PC');
--esque Ventas de cada empleado
create table empleadoVentas as(
	select nssVen,sum(montoV) as "MontoTotal"
	from venta
	group by nssVen
)
--Crear la funcion para el trigger
create or replace function ventas() returns TRIGGER 
as $$
begin
	update empleadoVentas
	set "MontoTotal"="MontoTotal"+new.montoV
	where nssVen = new.nssVen;
	return new;
end $$
Language plpgsql
--crear el trigger
create or replace trigger tr_VentasCadaEmpleado 
after insert or update on venta 
for each row 
execute procedure ventas();
--Esquema bono
create table bono as(
	select nssVen,"MontoTotal",("MontoTotal"*.10) as Bono
	from empleadoventas
	where "MontoTotal"=(select max("MontoTotal")
					  from empleadoventas)
)
--crar funcion para trigger bono
create or replace function bono() returns TRIGGER 
as $$
begin
	update bono
	set nssven= (select nssVen
				 from empleadoVentas
				 where "MontoTotal"=(select max("MontoTotal")
				 					 from empleadoVentas))
	,"MontoTotal" =(select "MontoTotal"
					   from empleadoVentas
				  	   where "MontoTotal"=(select max("MontoTotal")
				 					  	   from empleadoVentas))
	,bono =(select ("MontoTotal"*.10) as Bono
			   from empleadoVentas
			   where "MontoTotal"=(select max("MontoTotal")
				 				   from empleadoVentas))
	where nssven!=(select nssven
				  from empleadoVentas
				  where "MontoTotal"=(select max("MontoTotal")
				 					  from empleadoVentas));
	return new;
end $$
Language plpgsql
--crar trigger para bono
create or replace trigger tr_BonoTotal 
after insert or update on empleadoVentas 
for each row 
execute procedure bono();