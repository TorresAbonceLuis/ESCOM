/*
2.2 Datos definidos por el usuario (Usuario del programa o Programador?)

Los datos (variables o constantes) empleados hasta el momento, quedan en localidades de memoria
distintas, es decir, dispersos, en el lenguaje C el programador cuenta con dos formas de tenerlas
reunidas en una sola area de memoria, ellas son:

	a) Uniones
	b) Estructuras

Con ellas el programador podra reunir lo necesario para abordar problemas complejos y programarlos
de forma simple y rapida.

2.2.1 Declaracion de una Estructura

Las estructuras en el lenguaje C emplean la palabra reservada struct, para declararla es necesario
ponerle nombre a la estructura, se recomienda lo siguiente

	a) Tratar el nombre de la estructura como NombrePropio, (Sustantivo o Pronombre)
	b) El nombre de la estructura debe estar escrito en singular

La sintaxis de un estructura es la siguiente

struct NombreDeLaEstructura {
	tipo atributoUno;
	tipo atributoDos;
	.
	.
	.
	tipo atributoEne;
};

Dentro de muchas librerias del lenguaje C existen muchas estructuras definidas
Las estructuras se declaran en la parte globlal

Como se utiliza una estructura (sintaxis)

struct NombreDeLaEstructura miEstructura; // instancia

miEstructura.atributoUno = algo; // (tipo)algo
miEstructura.atributoDos = algo; // (tipo)algo
miEstructura.atributoEne = algo; // (tipo)algo

Ejemplo:
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX 33

/*
	nombreCompleto 		= 80 bytes
	boleta         		= 15 bytes
	+ -----------------------------
	tamanio de Alumno   = 95 bytes
	95 x 33 = 3135 bytes
*/
struct Alumno {
	char nombreCompleto[80]; // Atributo de la estructura
	int edad;				 // Atributo de la estructura
	char boleta[15];		 // Atributo de la estructura
};

struct Alumno grupoUnoCVDiesciseis[MAX]; // grupoUnoCVDiesciseis es una instancia de la estructura

struct Alumno *ptrGrupo;				 // Un apuntador a la estructura

void limpiarBufferDeTeclado() {
	char ch;
	while( (ch=getchar())!='\n' && ch!=EOF);
}

void introducirAlumno(int indice){
	limpiarBufferDeTeclado();
	printf( "Nombre del alumno %d: ", (indice+1) );
	gets(grupoUnoCVDiesciseis[indice].nombreCompleto);
	printf( "Boleta del alumno: " );
	gets(grupoUnoCVDiesciseis[indice].boleta);
	printf( "Edad del alumno : " );
	scanf( "%d", &grupoUnoCVDiesciseis[indice].edad);
}

void imprimirAlumnos(char grupo[80], int numeroDeAlumnos) {
	int contador;
	printf( "\n%s\n", grupo );
	for(contador = 0; contador<numeroDeAlumnos; contador++) {
		printf("Nombre del alumno %d: %s\n",contador + 1, grupoUnoCVDiesciseis[contador].nombreCompleto);
		printf("Boleta del alumno %d: %s\n",contador + 1, grupoUnoCVDiesciseis[contador].boleta);
		printf("Edad del alumno   %d: %d\n\n",contador + 1, grupoUnoCVDiesciseis[contador].edad);
	}
}

void imprimirAlumnosPorApuntador(char grupo[80], int numeroDeAlumnos) {
	int contador = 0;
	printf( "%s\n", grupo);
	for(contador = 0; contador<numeroDeAlumnos; contador++) {
		printf("Nombre del alumno %d: %s\n",contador + 1, ptrGrupo->nombreCompleto);
		printf("Boleta del alumno %d: %s\n",contador + 1, ptrGrupo->boleta);
		printf("Edad del alumno   %d: %d\n\n",contador + 1, ptrGrupo->edad);
		*ptrGrupo++;
	}
}

void eliminarAlumno(int indice){
	int contador;
	imprimirAlumnos("Grupo 1CV16", indice);
	printf( "Alumno a eliminar: " );
	scanf( "%d", &indice );
	indice = indice - 1;
		grupoUnoCVDiesciseis[indice].nombreCompleto [0] = '\0';
  		grupoUnoCVDiesciseis[indice].boleta [0] = '\0';
  		grupoUnoCVDiesciseis[indice].edad = 0;
}

void eliminarAlumnoPorApuntadores(int indice, int numeroDeAlumnos){
	imprimirAlumnos("Grupo 1CV16", numeroDeAlumnos);
	printf( "Cual alumno desea eliminar?" );
	scanf( "%d", &indice );
	indice = indice-1;
	ptrGrupo += indice;
  	ptrGrupo->nombreCompleto[0] = '\0';
  	ptrGrupo->boleta[0] = '\0';
  	ptrGrupo->edad = 0; 
}

void modificarDatosDelAlumno(int numeroDeAlumnos){
	int indice;
	imprimirAlumnos("Grupo 1CV16", numeroDeAlumnos);
	printf( "Cual alumno desea modificar: " );
	scanf( "%d", &indice );
	indice = indice-1;
	limpiarBufferDeTeclado();
	printf( "Nombre del alumno : ");
	gets(grupoUnoCVDiesciseis[indice].nombreCompleto);
	printf( "Boleta del alumno: " );
	gets(grupoUnoCVDiesciseis[indice].boleta);
	printf( "Edad del alumno : " );
	scanf( "%d", &grupoUnoCVDiesciseis[indice].edad);
}

void modificarDatosDelAlumnoPorApuntadores(int numeroDeAlumnos, int indice){
	imprimirAlumnos("Grupo 1CV16", numeroDeAlumnos);
	printf( "Cual alumno desea modificar: " );
	scanf( "%d", &indice );
	indice = indice-1;
	ptrGrupo += indice;
	limpiarBufferDeTeclado();
	printf( "Nombre del alumno : ");
	gets(ptrGrupo->nombreCompleto);
	printf( "Boleta del alumno: " );
	gets(ptrGrupo->boleta);
	printf( "Edad del alumno : " );
	scanf( "%d", &ptrGrupo->edad);
}

void ejecutarMenu (){
	int indice = 0, contador;
	int numeroDeAlumnos = 0;
	int opcion = 0;
	while( opcion != 5 ){
		ptrGrupo = grupoUnoCVDiesciseis;
		printf( "Menu del programa\n" );
		printf( "1. Introducir alumno\n" );
		printf( "2. Imprimir lista de alumnos\n" );
		printf( "3. Eliminar alumno\n" );
		printf( "4. Modificar datos del alumno\n" );
		printf( "5. Salir del programa\n" );
		printf( "Elija una opcion: " );
		scanf( "%d", &opcion );
		printf( "\n" );
		switch ( opcion ){
			case 1:
				introducirAlumno(numeroDeAlumnos);
				numeroDeAlumnos++;
				break;
			case 2:
				imprimirAlumnos("Grupo 1CV16", numeroDeAlumnos);
				imprimirAlumnosPorApuntador("Grupo 1CV16", numeroDeAlumnos);
				break;
			case 3:
				eliminarAlumnoPorApuntadores(numeroDeAlumnos, numeroDeAlumnos);
				break;
			case 4:
				modificarDatosDelAlumnoPorApuntadores(numeroDeAlumnos, numeroDeAlumnos);
				break;
			case 5:
				printf( "Hasta luego \n" );
				break;
			default:
				printf( "Elije una opcion entre 1 y 5\n" );
		}	
	}
}
/*
  Hacer un menu para procesar la estructura
  1. Introducir alumno
  2. Imprimir lista de alumnos (indice a la estructura)
  3. Imprimir lista de alumnos (aritmetica de apuntador)
  4. Eliminar un alumno. (indice a la estructura)
  	imprimir a los alumnos
  	elegir el indice del alumno
  	ptrGrupo[indice].nombreCompleto[0] = '\0'
  	ptrGrupo[indice].boleta[0] = '\0'
  	ptrGrupo[indice].edad = 0
  5. Eliminar un alumno. (apuntador a la estructura)
  	imprimir a los alumnos
	elegir el indice del alumno
	ptrGrupo += indice;
  	ptrGrupo->nombreCompleto[0] = '\0'
  	ptrGrupo->boleta[0] = '\0'
  	ptrGrupo->edad = 0
  6. Modificar datos del alumno (indice)
  7. Modificad datos del alumno (apuntador)
  8. salir del programa
*/

int main(int argc, char *argv[]) {
	//int numeroDeAlumnos, contador;
	ejecutarMenu();
	/*
	printf("Cuantos alumnos desea introducir (maximo: %d): ", MAX );
	scanf("%d", &numeroDeAlumnos);
	for( contador=0; contador<numeroDeAlumnos; contador++ ) {
		introducirAlumno(contador);
		}
	imprimirAlumnos("Grupo 1CV16", numeroDeAlumnos);
	ptrGrupo = grupoUnoCVDiesciseis;
	imprimirAlumnosPorApuntador("Grupo 1CV16", numeroDeAlumnos);
	*/
	return 0;
}