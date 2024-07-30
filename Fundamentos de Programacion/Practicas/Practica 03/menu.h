#ifndef MENU_H
#define MENU_H

#include "recursivo.h"
#include "iterado.h"
#include "hanoiRecursivo.h"
#include "hanoiIterado.h"

void menu(){
    int opcion;
	while(opcion!=5){
		printf( "Menu de la aplicacion.\n" );
		printf( "1. Modo recursivo.\n" );
		printf( "2. Modo iterado.\n" );
		printf( "3. Torres de Hanoi Recursivo.\n" );
		printf( "4. Torres de Hanoi Iterado.\n" );
        printf( "5. Salir del programa.\n" );
		printf( "Elija una opcion: " );
		scanf( "%d", &opcion );
		switch(opcion){
			case 1:
				MenuRecursivo();
				break;
			case 2:
				MenuIterado();
				break;
			case 3:
				menuHanoiRecursivo();
				break;
			case 4:
				menuHanoiIterado();
				break;
			case 5:
				printf( "Hasta luego" );
				break;
			default:
				printf( "Elige una opcion entre 1 y 4" );
		}
	}
}
#endif 