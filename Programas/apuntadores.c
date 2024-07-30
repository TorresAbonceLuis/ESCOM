#include <stdio.h>

void imprimirUnCaracter( char *apellidos[],int a, int b ) {
    printf( "\n%c", *(*(apellidos+a)+b));
}

int main(int argc, char *argv[]){
    char *apellidos[] = {"Perez","Gomez","Diaz","Peralta" };
    printf( "%c", apellidos[2][0] );
    //printf( "%c\n", *(*(apellidos+2)+0));
    imprimirUnCaracter(apellidos, 2, 1);
    int numero = 10;
    int *ptrNumero = &numero;
    printf( "\nvalor de numero %d memoria de numero %d, valor de ptrnumero %d ", numero,&numero, ptrNumero );
    *ptrNumero = 1000;
    printf("\nvalor de numero %d", numero);
    return 0;
}