#include <stdio.h>
#include <string.h>
#include <time.h>

#include "milibreriaio.h"

#define MAX_NOMBRE 60
#define MAX_BOLETA 13

#define MAX_GRUPO 10
#define MAX_ACCION 7

#define NOMBRE_ARCHIVO "alumnos.db"
#define BITACORA "bitacora.log"

struct Alumno {
	char nombre[MAX_NOMBRE];
	char boleta[MAX_BOLETA];
};



char acciones[MAX_ACCION][80] = {
	"Introducir un alumno\n",
	"Mostrar un alumno\n",
	"Mostrar al grupo\n",
	"Guardar informacion al archivo\n",
	"Leer informacion del archivo\n",
	"Buscar un alumno\n",
	"Numero de alumnos maximo en grupo alcanzado\n"
};

char *obtenerFechaYHora() {
	char *salida = (char *) malloc(sizeof(char)*128);
	time_t tiempo = time(0);
	struct tm *tlocal = localtime(&tiempo);
	strftime(salida,128,"%d/%m/%y %H:%M:%S", tlocal);
	printf("%s\n", salida);
	return salida;
}
int verificarExistencia(char archivo[]) {
	int siExiste = 0; // no existe
	FILE *fpArchivoAVerificar = abrirArchivo( archivo, "r" );
	if(fpArchivoAVerificar!=NULL) {
		siExiste = 1; // si existe
		cerrarArchivo(fpArchivoAVerificar);
	}
	return siExiste;
}


void limpiarBufferDeTeclado() {
	char ch;
	while( (ch=getchar())!='\n' && ch!=EOF);
}

void introducirInformacionAlumno(struct Alumno *unAlumno) {
	limpiarBufferDeTeclado();
	printf("Introducir nombre del alumno: ");
	fgets( unAlumno->nombre, MAX_NOMBRE, stdin );
	printf("Introducir la boleta del alumno: ");
	fgets( unAlumno->boleta, MAX_BOLETA, stdin );
}

void mostrarAlumno(struct Alumno unAlumno) {
	printf("Nombre: %s\n", unAlumno.nombre);
	printf("Boleta: %s\n", unAlumno.boleta);
}

void mostrarGrupo(int cuantos, struct Alumno grupo[]) {
	int contador = 0;
	for(contador=0; contador<cuantos; contador++) {
		mostrarAlumno( grupo[contador] );
		}
	printf("\n");
}

int calcularCuantos(struct Alumno grupo[]) {
	int contador;
	for(contador=0; contador<MAX_GRUPO; contador++) {
		if(strcmp(grupo[contador].nombre,"")==0 ) {
			break;
			}
		}
	return contador;
}

void enviarInformacionAlArchivo(struct Alumno grupo[], FILE *fpArchivo) {
	int contador = 0;
	fpArchivo = abrirArchivo( NOMBRE_ARCHIVO, "wb" );
	fwrite(grupo, sizeof(struct Alumno), MAX_GRUPO, fpArchivo);
	cerrarArchivo(fpArchivo);
	printf("%d Registros guardados.\n", MAX_GRUPO);
}

struct Alumno * leerInformacionDelArchivo(struct Alumno *grupo, FILE *fpArchivo) {
	int contador, cuantos = 0;
	fpArchivo = abrirArchivo( NOMBRE_ARCHIVO, "rb" );
	printf("Lectura de archivo: %d registros\n", MAX_GRUPO);
	fread(grupo, sizeof(struct  Alumno), MAX_GRUPO, fpArchivo );
	cerrarArchivo(fpArchivo);
	cuantos = calcularCuantos(grupo);
	mostrarGrupo(cuantos, grupo);
	return grupo;
}


void buscarAlumno(int cuantos, struct Alumno grupo[], FILE *fpBitacora) {
	int contador = 0;
	char nombreABuscar[MAX_NOMBRE];
	limpiarBufferDeTeclado();
	printf("Introducir nombre del alumno: ");
	gets(nombreABuscar);
	for( contador=0; contador<cuantos; contador++ ) {
		if(strcmp(grupo[contador].nombre, nombreABuscar)==0) {
			mostrarAlumno(grupo[contador]);
			escribirArchivo( fpBitacora, acciones[1] );
			return;
			}
		}
	printf("Alumno %s no encontrado\n", nombreABuscar);
}

void imprimirSalida(void) {
	printf("Menu del programa\n");
	printf("1. Introducir Alumno\n");
	printf("2. Leer grupo\n");
	printf("3. Guardar grupo\n");
	printf("4. Mostrar grupo\n");
	printf("5. Buscar alumno\n");
	printf("6. Salir del programa\n");
	printf("Elija uno: ");
}


void ejecutarMenu(FILE *fpArchivo) {
	int selector = 0;
	int cuantos = 0;
	FILE *fpBitacora;
	struct Alumno *grupo = (struct Alumno *) malloc(sizeof(struct Alumno)*MAX_GRUPO);
	memset(grupo, 0, sizeof(struct Alumno)*MAX_GRUPO);
	fpBitacora = abrirArchivo( BITACORA, "a+" );
	escribirArchivo(fpBitacora, obtenerFechaYHora());
	while(selector!=6) {
		imprimirSalida();
		scanf("%i", &selector);
		switch(selector) {
			case 1: // introducir un alumno
				if(cuantos<MAX_GRUPO) {
					introducirInformacionAlumno(&grupo[cuantos]);
					cuantos++;
					escribirArchivo( fpBitacora, acciones[0] );
					}
				else {
					printf("Numero de alumnos maximo en grupo alcanzado %i.\n", MAX_GRUPO );
					escribirArchivo( fpBitacora, acciones[6] );
					}
				break;
			case 2:
				grupo = leerInformacionDelArchivo(grupo, fpArchivo);
				cuantos = calcularCuantos(grupo);
				printf("cuantos %d\n", cuantos);
				escribirArchivo( fpBitacora, acciones[4] );
				break;
			case 3:
				enviarInformacionAlArchivo(grupo, fpArchivo);
				escribirArchivo( fpBitacora, acciones[3] );
				break;
			case 4:
				mostrarGrupo(cuantos, grupo);
				escribirArchivo( fpBitacora, acciones[2] );
				break;
			case 5:
				escribirArchivo( fpBitacora, acciones[5] );
				buscarAlumno(cuantos, grupo, fpBitacora);
				break;
			case 6:
				break;
			default:
				printf("Introduzca un entero con valor entre 1 y 6\n");
		}
	}
	free(grupo);
	escribirArchivo(fpBitacora, obtenerFechaYHora());
	cerrarArchivo(fpBitacora);
}

int main(int argc, char *argv[]) {
	FILE *fpArchivo = NULL;
	ejecutarMenu(fpArchivo);
}