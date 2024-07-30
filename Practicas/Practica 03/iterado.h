#ifndef ITERADO_H
#define ITERADO_H

#include <stdio.h>
#include <stdlib.h>



int  calcularPotenciaIterado(float base,int n){
    int contador;
    for(contador= n-1; contador>0; contador--){
        base*=base;
    }
    return base;
}

int calcularLosNPrimeroNumerosIterado(int n){
    int contador =n;
    for(contador=contador-1; contador>0; contador--){
        n+=contador;
    }
    return n;
}
int esImparIterado(int n);

int esParIterado(int n){
    int contador;
    for(contador=n-1; contador>1; contador--){
        if ( contador==0 ){
            return 1;
        }
        if( contador ==1 ){
            return 0;
        }
        contador = esImparIterado(contador-1);
        if( contador ==1 ){
            return 0;
        }
    }
}
int esImparIterado(int n){
    if ( n == 1){
        return 1;
    }
    return n;
}

int MultiplicarDosNumerosIterado(int x, int y){
    int contador, n =x;
    for(contador=y-1; contador>0; contador--){
        n+=x;
    }
    return n;
}

void MenuIterado(){
    int opcion = 1,base,exponente, numero,x,y;
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
                printf( "Numero:" );
                scanf( "%d",&base );
                printf( "Exponente:" );
                scanf( "%d",&exponente  );
                printf( "%d\n\n", calcularPotenciaIterado(base, exponente) );
				break;
			case 2:
                printf( "Numero:" );
                scanf( "%d", &numero );
                printf( "%d\n\n", calcularLosNPrimeroNumerosIterado(numero) );
				break;
			case 3:
                printf( "Numero: " );
                scanf( "%d",&numero );
                if( esParIterado(numero) == 0 ){
                    printf( "Es Impar \n" );
                }else
                    printf( "Es Par\n" );
				break;
			case 4:
                printf( "Primer Numero: " );
                scanf( "%d",&x );
                printf( "Segundo Numero: " );
                scanf( "%d",&y );
                printf( "%d\n\n", MultiplicarDosNumerosIterado(x,y) );
				break;
			case 5:
				printf( "Hasta luego\n\n" );
				break;
			default:
				printf( "Elija una opcion entre 1 y 5.\n" );
		}
	}

}
#endif //LIBRERIA_H