#include <stdio.h>
#include <string.h>
#include <time.h>

#include "milibreriaio.h"

#define MAX_NOMBRE 60
#define MAX_BOLETA 13
#define MAX_EDAD 80
#define MAX 180

// hard code NO debe estar aqui
//#define MAX_GRUPO 10


// 1. Pedirle al usuario el nombre del archivo a guardar el grupo .bin
// 2. Pedirle al usuario el nombre del archivo a leer del grupo   .bin
// 3. Pedir al usuario el tamanio del grupo (cambiar MAX_GRUPO por una variable local min=30 max=36)

// 4. Va a cambiar la estructura acomodar las funciones para leer y guardar
//	(si es necesario), explicar porque cambio o porque no cambio
int tamanioGrupo(char tipo[15]) {
	FILE *fp;
	int tamanio;
	if (tipo == "wb"){
		fp = abrirArchivo("config.bin","wb");	
		printf("Seleccione el tamanio del grupo: ");
		scanf("%d",&tamanio);
		escribirEnteroAArchivo(fp,tamanio);
		cerrarArchivo(fp);
	}
	fp = abrirArchivo("config.bin","rb");
	tamanio = leerEnteroDeArchivo(fp);
	return tamanio;
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

//struct Persona {
	//char nombre[MAX_NOMBRE];
	//int edad;
//};

struct Alumno {
	char nombre[MAX_NOMBRE];
	char boleta[MAX_BOLETA];
	char edad[MAX_EDAD];
};

void limpiarBufferDeTeclado() {
	char ch;
	while( (ch=getchar())!='\n' && ch!=EOF);
}

void introducirInformacionAlumno(struct Alumno *unAlumno) {
	limpiarBufferDeTeclado();
	printf("Introducir nombre del alumno: ");
	//scanf("%s", unAlumno->nombre);
	fgets( unAlumno->nombre, MAX_NOMBRE, stdin );
	printf("Introducir la boleta del alumno: ");
	fgets( unAlumno->boleta, MAX_BOLETA, stdin );
	printf("Introducir la edad del alumno: ");
	fgets( unAlumno->edad, MAX_EDAD, stdin );
}

void mostrarAlumno(struct Alumno unAlumno) {
	printf("Nombre: %s\n", unAlumno.nombre);
	printf("Boleta: %s\n", unAlumno.boleta);
	printf( "Edad %d\n",unAlumno.edad );
}

void mostrarGrupo(int cuantos, struct Alumno grupo[]) {
	int contador = 0;
	for(contador=0; contador<cuantos; contador++) {
		mostrarAlumno( grupo[contador] );
		}
	printf("\n");
}

int calcularCuantos(struct Alumno grupo[],int maxGrupo) {
	int contador;
	for(contador=0; contador<maxGrupo; contador++) {
		if(strcmp(grupo[contador].nombre,"")==0 ) {
			break;
			}
		}
	return contador;
}

void enviarInformacionAlArchivo(struct Alumno grupo[], FILE *fpArchivo, char nombreDeArchivo[], int maxGrupo) {
	int contador = 0;
	fpArchivo = abrirArchivo( nombreDeArchivo, "a+b" );
	fwrite(grupo, sizeof(struct Alumno), maxGrupo, fpArchivo);
	cerrarArchivo(fpArchivo);
	printf("%d Registros guardados.\n", maxGrupo);
}

struct Alumno * leerInformacionDelArchivo(struct Alumno *grupo, FILE *fpArchivo, char nombreDeArchivo[],int maxGrupo) {
	int contador, cuantos = 0;
	fpArchivo = abrirArchivo( nombreDeArchivo, "rb" );
	printf("Lectura de archivo: %d registros\n", maxGrupo);
	fread(grupo, sizeof(struct  Alumno), maxGrupo, fpArchivo );
	cerrarArchivo(fpArchivo);
	cuantos = calcularCuantos(grupo,maxGrupo);
	mostrarGrupo(cuantos, grupo);
	return grupo;
}
int buscarAlumno(int cuantos,struct Alumno grupo[]){
	int opcion,contador;
	char aux[MAX_NOMBRE];
	char nombreBuscar[30],boleta[30],edad[30];
	printf( "Manera de buscar\n" );
	printf( "1.Por Nombre\n" );
	printf( "2.Por Boleta\n" );
	printf( "3.Por edad\n" );
	printf( "Seleccione una opcion:" );
	scanf( "%d",&opcion );
	switch (opcion)
	{
	case 1:
		printf( "Nombre del alumno a buscar:" );
		scanf( "%s",nombreBuscar );
		for(contador=0;contador<cuantos;contador++){
			strcpy(aux, grupo[contador].nombre);
			aux[strlen(aux)-1] =  '\0';
			if(strcmp(aux,nombreBuscar)==0){
				mostrarAlumno(grupo[contador]);
				return 0;
			}
		}
		printf( "Alumno no encontrado.\n" );
		break;
	case 2:
		printf( "Numero de boleta del alumno a buscar:" );
		scanf( "%s",&boleta );
		for(contador=0;contador<cuantos;contador++){
			strcpy(aux, grupo[contador].boleta);
			aux[strlen(aux)-1] =  '\0';
			if(strcmp(aux,boleta)==0){
				mostrarAlumno(grupo[contador]);
			return 0;
			}
		}
		printf( "Alumno no encontrado.\n" );
		break;
	case 3:
		printf( "Edad del alumno a buscar:" );
		scanf( "%s",&edad );
		for(contador=0;contador<cuantos;contador++){
			strcpy(aux, grupo[contador].edad);
			aux[strlen(aux)-1] =  '\0';
			if(strcmp(aux,edad)==0){
				mostrarAlumno(grupo[contador]);
			return 0;
			}
		}
		printf( "Alumno no encontrado.\n" );
		return 1;
		break;
	default:
		printf( "Eliga una opcion\n" );
		break;
	}
}
void editarAlumno(int cuantos,struct Alumno grupo[]){
	int opcion,contador;
	char aux[MAX_NOMBRE];
	char nombreBuscar[30],boleta[30],edad[30];
	printf( "Manera de buscar\n" );
	printf( "1.Por Nombre\n" );
	printf( "2.Por Boleta\n" );
	printf( "3.Por edad\n" );
	printf( "Seleccione una opcion:" );
	scanf( "%d",&opcion );
	switch (opcion)
	{
	case 1:
		printf( "Nombre del alumno a buscar:" );
		scanf( "%s",nombreBuscar );
		for(contador=0;contador<cuantos;contador++){
			strcpy(aux, grupo[contador].nombre);
			aux[strlen(aux)-1] =  '\0';
			if(strcmp(aux,nombreBuscar)==0){
				mostrarAlumno(grupo[contador]);
				introducirInformacionAlumno(&grupo[contador]);
				return;
			}
		}
		printf( "Alumno no encontrado.\n" );
		break;
	case 2:
		printf( "Numero de boleta del alumno a buscar:" );
		scanf( "%s",&boleta );
		for(contador=0;contador<cuantos;contador++){
			strcpy(aux, grupo[contador].boleta);
			aux[strlen(aux)-1] =  '\0';
			if(strcmp(aux,boleta)==0){
				mostrarAlumno(grupo[contador]);
				introducirInformacionAlumno(&grupo[contador]);
			return;
			}
		}
		printf( "Alumno no encontrado.\n" );
		break;
	case 3:
		printf( "Edad del alumno a buscar:" );
		scanf( "%s",&edad );
		for(contador=0;contador<cuantos;contador++){
			strcpy(aux, grupo[contador].edad);
			aux[strlen(aux)-1] =  '\0';
			if(strcmp(aux,edad)==0){
				mostrarAlumno(grupo[contador]);
				introducirInformacionAlumno(&grupo[contador]);
			return;
			}
		}
		printf( "Alumno no encontrado.\n" );
		break;
	default:
		printf( "Eliga una opcion\n" );
		break;
	}
}
void borrarAlumno(int cuantos, struct Alumno grupo[],int size){
	int alumno, contador;
	char caracter;
	alumno=buscarAlumno(cuantos, grupo);
	if (alumno >= 0) {
		printf("Desea eliminar a este alumno? (S/N)\n");
		caracter = getch();
	}
	else {caracter = 'n';}
	if (caracter != 'S' && caracter != 's') {
		printf("Proceso Cancelado, el Alumno NO fue eliminado\n");
		return;
	}
	if (alumno >= 0) {
		for (contador=alumno+1;contador<size;contador++) {
		strcpy(grupo[contador-1].nombre,grupo[contador].nombre);
		strcpy(grupo[contador-1].boleta,grupo[contador].boleta);
		strcpy(grupo[contador-1].edad,grupo[contador].edad);	
	}
	printf("Alumno Eliminado\n");
	}
}

void checharRegistros(char string[MAX])
{
    FILE *fp;
    char tempo[MAX],out[MAX];
    int i;
    time_t t;
    struct tm *tm;
    t=time(NULL);
    tm = localtime(&t);
    strftime(tempo, MAX, "[%d/%m/%y - %H:%M]", tm );
    strcpy(out,tempo);
    strcat(out,"\n");
    strcat(out,string);
    fp = abrirArchivo("bitacora.txt","a+");
    escribirArchivo(fp,out);
    cerrarArchivo(fp);
}
/*void buscarAlumno(int cuantos, struct Alumno grupo[]) {
	int contador = 0;
	char nombreABuscar[MAX_NOMBRE];
	limpiarBufferDeTeclado();
	printf("Introducir nombre del alumno: ");
	gets(nombreABuscar);
	for( contador=0; contador<cuantos; contador++ ) {
		if(strcmp(grupo[contador].nombre, nombreABuscar)==0) {
			mostrarAlumno(grupo[contador]);
			return;
			}
	}
	printf("Alumno %s no encontrado\n", nombreABuscar);
}
*/
// 5. Editar alumno
// Algoritmo
//	1. Buscar al alumno 
//  2. Si se encuentra entonces se edita
//     en caso contrario volver a intentar
// El usuario puede elegir si busca por nombre o busca por edad o busca por boleta
// Si es por edad entonces mostrar a todos los alumnos de esa edad y el usuario que elija uno

// 6. Eliminar un alumno (se cambio de grupo o se dio de baja)

// 7. Poder instroducir mas alumnos en un grupo incompleto

void imprimirSalida(void) {
	printf("Menu del programa\n");
	printf("1. Introducir Alumno\n");
	printf("2. Leer grupo\n");
	printf("3. Guardar grupo\n");
	printf("4. Mostrar grupo\n");
	printf("5. Editar alumno\n");
	printf("6. Eliminar un alumno\n");
	printf("7. Introducir mas alumnos a un grupo\n" );
	printf("8. Salir del programa\n" );
	printf("Elija uno: ");
}

void ejecutarMenu(FILE *fpArchivo) {
	checharRegistros("A la hora indicada se abrio el programa.");
	int tamanio ;
	int selector = 0;
	int cuantos = 0;
	char nombreDeArchivo[10];
	if(verificarExistencia==0){
		tamanio=tamanioGrupo("rb");
	}else{
		tamanio=tamanioGrupo("wb");
	}
	struct Alumno *grupo = (struct Alumno *) malloc(sizeof(struct Alumno)*tamanio);
	memset(grupo, 0, sizeof(struct Alumno)*tamanio);
	while(selector!=8) {
		imprimirSalida();
		scanf("%i", &selector);
		switch(selector) {
			case 1:
				checharRegistros("A la hora indicada se introdujo a un alumno.");
				if(cuantos<tamanio) {
					introducirInformacionAlumno(&grupo[cuantos]);
					cuantos++;
				}else {
					printf("Numero de alumnos maximo en grupo alcanzado %i.\n", tamanio );
				}
				break;
			case 2:
				checharRegistros("A la hora indicada se leyo a un grupo.");
				printf( "Nombre del archivo a leer del grupo:" );
				limpiarBufferDeTeclado();
				gets(nombreDeArchivo);
				printf( "Numero de alumnos:" );
				scanf( "%d",&tamanio );
				grupo = leerInformacionDelArchivo(grupo, fpArchivo, nombreDeArchivo,tamanio);
				cuantos = calcularCuantos(grupo,tamanio);
				printf("cuantos %d\n", cuantos);
				break;
			case 3:
				checharRegistros("A la hora indicada se guardo a un grupo.");
				if(cuantos<0){
					printf( "El minimo de alumnos para crear el grupo es de 30.\n" );
					printf( "Faltan: %d alumnos\n",tamanio-cuantos);
					break;
				}
				printf( "Nombre del archivo donde guardar al grupo:" );
				limpiarBufferDeTeclado();
				gets(nombreDeArchivo);
				enviarInformacionAlArchivo(grupo, fpArchivo, nombreDeArchivo,tamanio);
				break;
			case 4:
				checharRegistros("A la hora indicada se mostro a un alumno.");
				mostrarGrupo(cuantos, grupo);
				break;
			case 5:
				checharRegistros("A la hora indicada se edito a un alumno.");
				editarAlumno(cuantos, grupo);
				break;
			case 6:
			checharRegistros("A la hora indicada se elimino a un alumno.");
				borrarAlumno(cuantos,grupo,tamanio);
				break;
			case 7:
			checharRegistros("A la hora indicada se modifico el tamanio del grupo.");
				tamanio = tamanioGrupo("wb");
			default:
			printf("Introduzca un entero con valor entre 1 y 7\n");
		}
	}
	free(grupo);
	checharRegistros( "A la hora indicada se cerro el programa." );
}

int main(int argc, char *argv[]) {
	FILE *fpArchivo = NULL;
	ejecutarMenu(fpArchivo);
}