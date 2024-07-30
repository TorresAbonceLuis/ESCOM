#include "stdio.h"

//argc:cuenta los argumentos desde la linea de comando
//argv: alamcena los argumentos
//los argumentos para un programa desde la linea de comando se distingue con un espacion en 
//blanco

int main(int argc,char *argv[]) {
	int contador=0;
	printf("Hola Mundo en Lenguaje C\n");
	printf("Los argumetos son: \n");
	for(contador = 0; contador<argc; contador++){
		printf("argumento[%d]: %s\n",contador, argv[contador]);
		}
	return 0;
}