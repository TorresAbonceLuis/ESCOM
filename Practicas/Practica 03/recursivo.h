#ifndef LIBRERIA_H
#define LIBRERIA_H

#include <stdio.h>
#include <stdlib.h>

void limpiarBufferDeTeclado();
int calcularLosNPrimeroNumeros(int n);
int  calcularPotencia(int base,int exponente);
int esImpar(int n);
int esPar(int n);
int MultiplicarDosNumeros(int x, int y);

void MenuRecursivo(){
	int opcion = 1;
    int base, numero,x,y;
    int exponente;
	while(opcion != 5) {
		printf( "\nMenu de la aplicacion.\n" );
		printf( "1. Calcular potencia de un numero.\n" );
		printf( "2. Calcular la N suma de los primeros numeros.\n" );
		printf( "3. Saber si un numero es par o impar.\n" );
		printf( "4. Calcular la multiplicacion de 2 numeros.\n" );
        printf( "5. Salir al menu.\n" );
		printf( "Elija una opcion: " );
		scanf( "%d", &opcion );
		switch( opcion ) {
			case 1: 
				printf( "Dame el numero a elevar: " );
				scanf( "%d", &base );
				printf( "Exponente: " );
                scanf( "%d", &exponente );
                printf( "Resultado:%d\n\n",calcularPotencia(base,exponente) );
				break;
			case 2:
                limpiarBufferDeTeclado();
				printf( "Dame el numero:" );
                scanf( "%d",&numero );
                printf( "Resultado:%d\n\n",calcularLosNPrimeroNumeros(numero) );
				break;
			case 3:
				limpiarBufferDeTeclado();
                printf( "Dame el numero:" );
                scanf( "%d",&numero );
                if( esPar(numero) == 0){
                	printf( "Es impar" );
                }
                else{
                	printf( "Es par" );
                }
				break;
			case 4:
                printf( "Primer numero: " );
                scanf( "%d",&x );
                printf( "Segundo numero: " );
                scanf( "%d",&y );
                printf( "%d\n\n",MultiplicarDosNumeros(x,y) );
				break;
			case 5:
				printf( "Hasta luego\n\n" );
				break;
			default:
				printf( "Elija una opcion entre 1 y 5.\n" );
		}
	}
}
void limpiarBufferDeTeclado() {
	char ch;
	while( (ch=getchar())!='\n' && ch!=EOF);
}
int  calcularPotencia(int base,int exponente){
	if( exponente == 0 ){
		return 1;
	}
	return base*calcularPotencia(base, exponente-1);
}

int calcularLosNPrimeroNumeros(int n){
	if ( n == 1 ){
		return 1;
	}
	return n+calcularLosNPrimeroNumeros(n-1);
}

int esPar(int n){
	if(n == 0){
		return 1;
	}
	return esImpar(n-1);
}
int esImpar(int n){
	if ( n == 0){
		return 0;
	}
	return esPar(n-1);
}

int MultiplicarDosNumeros(int x, int y){
	if(y==0){
		return 0;
	}
	return x + MultiplicarDosNumeros(x,y-1);
}
#endif //LIBRERIA_H
