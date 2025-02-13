Create table Cliente(
	codigo int not null,
	rfc char(15) not null,
	nombre char(20) not null,
	apa char(20) not null,
	ama char(20),
	codigoaval int not null default 1,
constraint cveCliente
	primary key (codigo),
constraint cveAval
	foreign key (codigoaval) references Cliente (codigo)
	on delete set default on update cascade
);

create table telefonoContacto(
	telefono char(10) not null,
	codigo int not null,
constraint cvetelefono
	primary key (telefono,codigo),
constraint cvecodigo
	foreign key (codigo) references Cliente (codigo)
);
create table garage(
	direccion char(50) not null,
constraint cvegarage
	primary key (direccion)
);
create table agencia(
	direccionAg char(50) not null,
constraint cvegagencia
	primary key (direccionAg)
);
create table coche (
	codestado int not null,
	numsecuen int not null,
	marca char(20),
	color char(20),
	precioalquiler int not null,
	numestacion int,
	direccion char(50) not null,
constraint cvecoche
	primary key (codestado,numsecuen),
constraint cvedireccion
	foreign key (direccion) references garage (direccion)
);
alter table coche add folio int not null;
alter table coche add codigo int not null;
create table reservacion(
	folio int not null,
	inicio date not null,
	fin date not null,
	codigo int not null,
	direccion char(50),
constraint cvereservacion
	primary key (folio, codigo),
constraint cvecodclient
	foreign key (codigo) references cliente (codigo),
constraint cvedirec
	foreign key (direccion) references agencia (direccionAg)
);
alter table coche
add constraint cvecodfol
	foreign key (folio,codigo) references reservacion(folio,codigo);