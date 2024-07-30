#ifndef MILIBRERIAIO_H
#define MILIBRERIAIO_H

#include <stdio.h>
#include <stdlib.h>
/* Funcion para abrir un archivo en cualquier modo
 * archivo : Variable que contiene el nombre del archivo
 * modo    : Modo de apertura del archivo
 * return  : devuelve el puntero del archivo, si es NULL no paso nada
 */
FILE *abrirArchivo( char archivo[80], char modo[10] ) {
	FILE *fp;
	if ((fp = fopen(archivo, modo))==NULL) {
		printf("No puedo abrir el archivo %s.\n", archivo);
		exit(1);
	}
	return fp;
}
/* Funcion para leer el archivo en modo texto, lee un caracter a la vez hasta 
 * terminar el archivo
 * fp : Puntero al archivo que debe leerse
 */
void leerArchivo( FILE *fp ) {
	char ch;
	do {
		ch = getc(fp);
		printf("%c", ch );
	} while(!feof(fp));
	printf("\n");
}
/* Funcion para escribir un mensaje en un archivo
 * fp      : El puntero del archivo al cual se le envia el mensaje
 * mensaje : El mensaje que se introducira en el archivo
 */
void escribirArchivo( FILE *fp, char mensaje[160] ) {
	int indice=0;
	while(mensaje[indice]!='\0') {
		putc(mensaje[indice], fp);
		indice++;
		}
	putc('\n', fp);
}
/* Funcion que copia un archivo (archivoEntrada) en otro (archivoSalida) pueden ser de texto
 * o binario
 * in             : Apuntador al archivo de donde se lee
 * archivoEntrada : El nombre del archivo que se lee
 * out            : Apuntador al archivo donde se escribe la copia
 * archivoSalida  : Al nombre del archivo que se escribe
 */
void copiarArchivo(FILE *in, char *archivoEntrada, FILE *out, char *archivoSalida) {
	char ch;
	/* This code actually copies the file. */
	printf("Copiando archivo %s en archivo %s\n", archivoEntrada, archivoSalida);
	do {
		//printf("Dentro del while\n");
		ch = getc(in);
		//printf("%c\n", ch );
		if(!feof(in)) {
			putc(ch, out);
			}
	} while(!feof(in));
	printf(".... Hecho\n");
}
/* Funcion para escribir desde el teclado lo que se quiere escribir en el
 * fp             : Apuntador al archivo donde se desea escribir
 * caracterDeParo : Caracter para detener la escritura en el archivo
 */
void escribirDeTecladoAArchivo(FILE *fp, char caracterDeParo) {
	char ch;
	printf("Escriba lo que guste y termine con signo de $\n");
	do {
		ch = getchar();
		// solo se escribe el caracter distinto del caracter de paro
		if(ch!=caracterDeParo) { 
			putc(ch, fp);	
		}
	} while (ch != caracterDeParo);
}
/* Funcion para escribir datos enteros al archivo, utiliza la funcion 
 * int fprintf(FILE *archivo, const char *formato[argumento1, argumento2,..,argumentoN])
 * archivo   : Apuntador al archivo donde se escribe
 * formato   : Igual que se hace en printf
 * return    : devuelve el numero de caracteres escritos en el archivo
 */
void escribirEnteroAArchivo( FILE *fp, int entero ) {
	if( fprintf( fp, "%d", entero )==0 ) {
		printf("No se pudo enviar el entero %d\n", entero);
	}
}
/* Funcion que lee datos flotantes dobles del archivo, utiliza la funcion
 * int fscanf(FILE *archivo, const char *formato[argumento1, argumento2,..,argumentoN])
 * fp : es el puntero al archivo que se lee
 */
int leerEnteroDeArchivo( FILE *fp ) {
	int entero = 0;
	if( fscanf( fp, "%d", &entero )==0 ) {
		printf("No se pudo leer el entero desde archivo\n");
	}
	return entero;
}
/* Funcion para escribir datos de caracter al archivo, utiliza la funcion 
 * int fprintf(FILE *archivo, const char *formato[argumento1, argumento2,..,argumentoN])
 * archivo   : Apuntador al archivo donde se escribe
 * formato   : Igual que se hace en printf
 * return    : devuelve el numero de caracteres escritos en el archivo
 */
void escribirCaracterAArchivo( FILE *fp, char caracter ) {
	if( fprintf( fp, "%c", caracter )==0 ) {
		printf("No se pudo escribir el caracter %c\n", caracter);
	}
}
/* Funcion que lee datos en caracter del archivo, utiliza la funcion
 * int fscanf(FILE *archivo, const char *formato[argumento1, argumento2,..,argumentoN])
 * fp : es el puntero al archivo que se lee
 */
char leerCaracterDeArchivo( FILE *fp ) {
	char caracter;
	if( fscanf( fp, "%c", &caracter )==0 ) {
		printf("No se pudo leer el caracter desde archivo\n");
	}
	return caracter;
}

/* Funcion para escribir datos enteros al archivo, utiliza la funcion 
 * int fprintf(FILE *archivo, const char *formato[argumento1, argumento2,..,argumenton])
 * archivo   : Apuntador al archivo donde se escribe
 * formato   : Igual que se hace en printf
 * return    : devuelve el numero de caracteres escritos en el archivo
 */
void escribirEnteroLargoAArchivo( FILE *fp, long enteroLargo ) {
	if( fprintf( fp, "%ld ", enteroLargo )==0 ) {
		printf("No se pudo escribir el entero largo desde archivo %ld\n", enteroLargo);
	}
}

/* Funcion que lee datos entero largo del archivo, utiliza la funcion
 * int fscanf(FILE *archivo, const char *formato[argumento1, argumento2,..,argumentoN])
 * fp : es el puntero al archivo que se lee
 */
long leerEnteroLargoDeArchivo( FILE *fp ) {
	long enteroLargo;
	if( fscanf( fp, "%ld", &enteroLargo )==0 ) {
		printf("No se pudo leer el entero largo desde archivo\n");
	}
	return enteroLargo;
}


/* Funcion para escribir datos flotantes dobles al archivo, utiliza la funcion 
 * int fprintf(FILE *archivo, const char *formato[argumento1, argumento2,..,argumenton])
 * archivo   : Apuntador al archivo donde se escribe
 * formato   : Igual que se hace en printf
 * return    : devuelve el numero de caracteres escritos en el archivo
 */
void escribirFlotanteAArchivo( FILE *fp, float flotante ) {
	if( fprintf( fp, "%f", flotante )==0 ) {
		printf("No se pudo escribir el flotante %f al archivo\n", flotante);
		}
}

/* Funcion que lee datos flotantes del archivo, utiliza la funcion
 * int fscanf(FILE *archivo, const char *formato[argumento1, argumento2,..,argumentoN])
 * fp : es el puntero al archivo que se lee
 */
float leerFlotanteDeArchivo( FILE *fp ) {
	float flotante = 0.0;
	if( fscanf( fp, "%f", &flotante )==0 ) {
		printf("No se pudo leer el flotante desde archivo\n");
		}
	return flotante;
}

/* Funcion para escribir datos flotantes dobles al archivo, utiliza la funcion 
 * int fprintf(FILE *archivo, const char *formato[argumento1, argumento2,..,argumenton])
 * archivo   : Apuntador al archivo donde se escribe
 * formato   : Igual que se hace en printf
 * return    : devuelve el numero de caracteres escritos en el archivo
 */
void escribirFlotanteDobleAArchivo( FILE *fp, double flotanteDoble ) {
	if( fprintf( fp, "%lf ", flotanteDoble )==0 ) {
		printf("No se pudo escribir el flotante doble %lf al archivo\n", flotanteDoble);
		}
}

/* Funcion que lee datos flotantes dobles del archivo, utiliza la funcion
 * int fscanf(FILE *archivo, const char *formato[argumento1, argumento2,..,argumentoN])
 * fp : es el puntero al archivo que se lee
 */
double leerFlotanteDobleAArchivo( FILE *fp ) {
	double flotanteDoble;
	if( fscanf( fp, "%lf ", &flotanteDoble )==0);{
		printf("No se pudo leer el flotante doble desde archivo\n");
	}
	return flotanteDoble;
}

/* Funcion para cerrar el archivo
 * fp : Apuntador al archivo que se cierra
 */
void cerrarArchivo( FILE *fp ) {
	if( fp!=NULL ) {
		fclose(fp);
	}
}


#endif 