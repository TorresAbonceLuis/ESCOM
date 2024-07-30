create table proyecto(
	nump int not null,
	nomp char(20),
	lugar char (50),
	constraint cveproy
		primary key (nump)
);
create table empleado(
	apa char(15) not null,
	ama char(15),
	nombre char(15) not null,
	nss int not null,
	direccion char(40),
	salario int,
	sexo char (15),
	fechaN date,
	nssSup int,
	constraint cveempleado
		primary key ( nss ),
	constraint cveSup
		foreign key (nssSup) references empleado (nss)
);
create table dependiente(
	apa char (15) not null,
	ama char (15),
	nombre char (15) not null,
	sexo char (15),
	parentesco char (15),
	fechaNac date,
	nssEmp int not null,
	constraint cevDepen
		primary key (apa,nombre,nssEmp),
	constraint cveNssEmp
		foreign key (nssEmp) references empleado (nss)
);
create table departamento (
	numd int not null,
	nomd char(20),
	nssEmp int,
	fechadir date,
	nump int,
	constraint cveDepa
		primary key (numd),
	constraint cvenssEmp
		foreign key (nssEmp) references empleado(nss)
	on delete set default,
	constraint cvenump
		foreign key (nump) references proyecto(nump)
);
alter table proyecto 
	add numdc int not null,
	add constraint cvenumdc
		foreign key (numdc) references departamento(numd);
alter table empleado
	add numdads int not null,
	add constraint cvenumdads
		foreign key (numdads) references departamento (numd);
		
create table lugar(
	nssEmp int not null,
	nump int not null,
	hrs int,
	constraint cvelugar
		primary key (nssEmp,nump),
	constraint cvenssemp
		foreign key (nssEmp) references empleado(nss),
	constraint cvenump
		foreign key(nump) references proyecto(nump)
);
create table trabaja_en(
	numd int not null,
	lugaru char(30),
	constraint cvetrabaja
		primary key (numd,lugaru),
	constraint cvenumd
		foreign key (numd) references departamento (numd)
);