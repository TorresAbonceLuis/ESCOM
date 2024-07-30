/*
Desarrolle un algoritmo para el juego de dados

Descripcion del juego
	- El juego de dados se juega con dos dados (Puede salir numeros entre 2 y 12)
	- Cada dado cuenta con seis caras (cada cara tiene un numero entre 1 y 6)
	- Un jugador juega el juego
	- El juego comienza con el jugador tomando los dados
	- El jugador dice su numero con el cual pinsa ganar
	- El jugador agita los dados
	- El jugador sopla los dados
	- El jugador lanza los dados
	- El juego termina cuando los dados dejan de moverse
		El jugador GANO si la suma de los numeros de las caras superiores de cada dado suma
		el mismo numero con el cual solicito el juagor al principio.
		El jugador PIERDE de lo contrario.

Algoritmo

1. Iniciar el juego
2. Entradas por teclado
	numeroDelJugador
	Variables del juego
		caraSuperiorDado1, caraSuperiorDado2, sumaDeLosDados
3. Generar el ritual del jugador
	3.1 Tomar los dados
	3.2 Soplar los dados
	3.3 Agitar los dados
	3.4 Lanzar los dados
		En las variables caraSuperiorDado1 y caraSuperiorDado2 se almacenan los numeros que la 
		computadora va a Generar (numeros pseudo-aleatorios) entre 1 y 6 (imprimir valor de cara 
		superior del dado), estos dos numeros se suman y se asignan a sumaDeLosDados
4. Realizar la comprobacion de sumaDeLosDados contra numeroDelJugador, si son iguales se imprime que 
	el jugador GANO, de lo contrario se indica que PERDIO y porque ocurrio
5. Fin del juego
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#define CARAS_DADO 6

// Variables globales
int numeroDelJugador, caraSuperiorDado1, caraSuperiorDado2, sumaDeLosDados;

void elegirTuNumeroDeJugador() {
	printf("Introduzca su numero del juego (2 y 12): " );
	scanf("%d", &numeroDelJugador);
}

// Devuelve numeros entre 1 y 6
int lanzarDado() {
	return (rand()%CARAS_DADO)+1;
}

void tomarLosDados() {
	caraSuperiorDado1 = caraSuperiorDado2 = 0;
	printf( "Tomando los dados\n" );
}

void soplarLosDados() {
	printf( "pfpfpfpf....\n" );
}

void agitarLosDados() {
	printf( "taka, taka, taka,....., taka\n" );
}

void imprimirResultadoDeJuego() {
	if(numeroDelJugador==sumaDeLosDados) {
		printf("Felicidades has GANADO con %d\n", numeroDelJugador);
	}
	else {
		printf("Lo sentimos has PERDIDO porque %d es distinto de %d\n", numeroDelJugador, sumaDeLosDados);
	}
}

void jugarALosDados() {
	elegirTuNumeroDeJugador();
	tomarLosDados();
	soplarLosDados();
	agitarLosDados();
	caraSuperiorDado1 = lanzarDado();
	caraSuperiorDado2 = lanzarDado();
	printf("Dado1: %d y Dado2: %d\n", caraSuperiorDado1, caraSuperiorDado2 );
	sumaDeLosDados = caraSuperiorDado1 + caraSuperiorDado2;
	imprimirResultadoDeJuego();
}

int main(int argc, char *argv[]) {
	srand(time(NULL));
	jugarALosDados();
	return 0;
}