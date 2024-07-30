// 2.4 Estrcuturas anidadas (Con apuntadores TAREA) 

#include <stdio.h>
#include <stdlib.h>

#define MAX_NOMBRE 80
#define MAX_FECHA 11
#define MAX_BOLETA 11
#define MAX_ALUMNOS 33


struct SerHumano { 
	char fechaNacimiento[MAX_FECHA]; // formato :: aaaa/mm/dd\0 :: si mm<10 mm=08 :: si dd<10 dd=05
};

struct Persona {
	struct SerHumano *humano;		// Apuntador a la Estructura anidada
	char nombre[MAX_NOMBRE];
};

struct Alumno {
	struct Persona *alguien;			// Apuntador a la Estructura anidada
	char boleta[MAX_BOLETA]; 		// 10 digitos numericos aaaaxxxxxx\0
};

struct Alumno grupoDeFundamentos[MAX_ALUMNOS]; // instancia de Alumno
int contador = 0;

void limpiarBufferDeTeclado() {
	char ch;
	while( (ch=getchar())!='\n' && ch!=EOF);
}

void introducirAlumno() {
	limpiarBufferDeTeclado();	
	printf( "Alumno (%d):\n", contador+1 );
	grupoDeFundamentos[contador].alguien = (struct Persona *)malloc(sizeof(struct Persona));
	grupoDeFundamentos[contador].alguien->humano = (struct SerHumano *)malloc(sizeof(struct SerHumano));
	printf( "Fecha de nacimiento (aaaa/mm/dd): " );
	gets(grupoDeFundamentos[contador].alguien->humano->fechaNacimiento);
	printf( "Nombre completo                 : " );
	gets(grupoDeFundamentos[contador].alguien->nombre);
	printf( "Boleta                          : " );
	gets(grupoDeFundamentos[contador].boleta);
	contador++;
}

void visualizarAlumno(int indice) {
	if(indice<0 || indice>=MAX_ALUMNOS) {
		printf( "Error: indice fuera de rango" );
		return;
	}else{
		indice = indice-1;
		printf( "Alumno (%d):\n", indice+1 );
		printf( "Fecha de nacimiento : %s\n", grupoDeFundamentos[indice].alguien->humano->fechaNacimiento);
		printf( "Nombre completo     : %s\n", grupoDeFundamentos[indice].alguien->nombre);
		printf( "Boleta              : %s\n", grupoDeFundamentos[indice].boleta);
	}
}

void visualizarATodosLosAlumnos() {
	int numeroDeAlumno;
	for(numeroDeAlumno=1; numeroDeAlumno<=contador; numeroDeAlumno++) {
		visualizarAlumno(numeroDeAlumno);
		}
}

void ejecutarMenu() {
	int opcion = -500;
	int indice = 0;
	while(opcion != 4) {
		printf( "Menu de la aplicacion.\n" );
		printf( "1. Introducir alumno.\n" );
		printf( "2. Visualizar alumno.\n" );
		printf( "3. Visualizar al grupo.\n" );
		printf( "4. Salir del programa.\n" );
		printf( "Elija una opcion: " );
		scanf( "%d", &opcion );
		switch( opcion ) {
			case 1: // introducir un alumno
				introducirAlumno();
				break;
			case 2:
				printf( "Dame el numero del alumno: " );
				scanf( "%d", &indice );
				visualizarAlumno(indice);
				break;
			case 3:
				visualizarATodosLosAlumnos();
				break;
			case 4:
				printf( "Hasta luego, buen dia.\n" );
				break;
			default:
				printf( "Elija una opcion entre 1 y 4.\n" );
			}
		}
}

int main(int argc, char *argv[]) {
	ejecutarMenu();
	return 0;
}