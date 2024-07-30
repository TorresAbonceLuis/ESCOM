#include <stdio.h>

int main ( int argc, char *argv[] ){
    int numero = 5;
    int * ptrPi = &numero;

    printf( "Direccion de numero: %d valor: %d\n", &numero, numero  );
    printf( "Direccion de ptrPi : %d valor: %d\n\n", &ptrPi, ptrPi );
    printf( "Direccion de ptrPi : %d valor: %d\n", &ptrPi, ptrPi );
    printf( "Direccion de ptrPi : %d valor: %d\n", &ptrPi, ptrPi );

    *ptrPi = 200;

    printf( "%p\n", *ptrPi );
    printf( "%d\n", *ptrPi );
    printf( "%d\n", numero );

    return 0;

}