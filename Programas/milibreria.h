/*
2.3.4 Retorno de la funcion
Una funcion puede devolver cualquier tipo
  Devuelven un solo valor
	Tipos enteros
		shor, int, long
	Tipos flotantes
		float, double
	Tipo caracter
		char
  Devolver mas de un valor
  	Devolvemos un apuntador de cualquier tipo de los mencionados anteriormente
  Para devolver un valor de una funcion siempre se debe incluir la palabra reservada "return"

  return variableDeUnTipo;

  return apuntadorDeUnTipo;

2.3.5 Bibliotecas creadas por el usuario

Las librerias se crean como arhcivos de codigo fuente con extension ".h"
Para tener funciones que trabajan de forma generica con algo programado por otro programador.
Puedo hacer extensible el lenguaje (ejemplo stdio.h)
Pueden incluir otras librerias pero no a si misma.
Existe una forma de evitar utilizar librerias duplicadas
	#ifndef ETIQUETA
	#define ETIQUETA
	.....	
	Cuerpo de la librerias
	.....
	#endif ETIQUETA
No debe contener la funcion principal
Las librerias pueden quedar en cualquier carpeta del sistema operativo, a la hora de incluirlo

#include "c:\fundamentos\lib\milibreria.h"

Para compilar una libreria, se incluye en la linea de compilacion (ejemplo)

	gcc milibreria.h archivomain.c -o archivomain.exe

*/
#ifndef MILIBRERIA_H
#define MILIBRERIA_H

#include <stdio.h>
#include <stdlib.h>
#define MAX_NOMBRE 81
#define MAX_BOLETA 11


struct Persona {
	char nombre[MAX_NOMBRE];
};

struct Alumno {
	struct Persona alguien;
	char boleta[MAX_BOLETA];
};

// Retorno de la funcion 
struct Alumno * crearAlumnoConDatos() {
	struct Alumno * unAlumno = (struct Alumno *)malloc(sizeof(struct Alumno));
	printf( "Dame el nombre del alumno: " );
	gets(unAlumno->alguien.nombre);
	printf( "Dame la boleta del alumno: " );
	gets(unAlumno->boleta);
	return unAlumno;
}

void imprimirDatosDelAlumno(struct Alumno * unAlumno) {
	printf( "Alumno: %s\n", unAlumno->alguien.nombre );
	printf( "Boleta: %s\n", unAlumno->boleta );
}

void actualizarDatosDeAlumno(struct Alumno * unAlumno) {
	printf( "Dame el nombre del alumno: " );
	gets(unAlumno->alguien.nombre);
	printf( "Dame la boleta del alumno: " );
	gets(unAlumno->boleta);
}

void actualizarNombreDeAlumno(struct Alumno * unAlumno) {
	printf( "Dame el nombre del alumno: " );
	gets(unAlumno->alguien.nombre);
}

void actualizarBoletaDeAlumno(struct Alumno * unAlumno) {
	printf( "Dame la boleta del alumno: " );
	gets(unAlumno->boleta);
}

#endif MILIBRERIA_H