#include <stdio.h>
    // Tipos de datos Primitivos (comentario en c de una sola linea)
    // Enteros, flotantes, caracter
// Tipos de datos Compueestos
    // struct, union, enum
// declaracion y asignacion de variables globales
    short otroShort = 12;                      // es de 2 bytes = 16 bits
    int otroInt = -24;                          // es de 4 bytes = 32 bits
    long otroLong= 33;                       // es de 8 bytes = 64 bits
int main(int argc, char*argv[]){
    // declaracion de variables locales
    short unShort = -100;                      // es de 2 bytes = 16 bits
    int unInt = 45;                          // es de 4 bytes = 32 bits
    long unLong = 42;                       // es de 8 bytes = 64 bits
    short resultadoShort;
    int resultadoInt;
    long resultadoLong;
    // Operadores aritmeticos
    // * (multiplicacion),/ (division), %(modulo de la division)
    // + (suma), - (resta)

    printf("\nshort\n");
    resultadoShort = otroShort * unShort;
    printf("%d * %d = %d\n", otroShort, unShort, resultadoShort);
    resultadoShort = otroShort / unShort;
    printf("%d / %d = %d\n", otroShort, unShort, resultadoShort);
    resultadoShort = otroShort % unShort;
    printf("%d mod %d = %d\n", otroShort, unShort, resultadoShort);
    resultadoShort = otroShort + unShort;
    printf("%d + %d = %d\n", otroShort, unShort, resultadoShort);
    resultadoShort = otroShort - unShort;
    printf("%d - %d = %d\n", otroShort, unShort, resultadoShort);

    printf("\nInt\n");
    resultadoInt = otroInt * unInt;
    printf("%d * %d = %d\n", otroInt, unInt, resultadoInt);
    resultadoInt = otroInt / unInt;
    printf("%d / %d = %d\n", otroInt, unInt, resultadoInt);
    resultadoInt = otroInt % unInt;
    printf("%d mod %d = %d\n", otroInt, unInt, resultadoInt);
    resultadoInt = otroInt + unInt;
    printf("%d + %d = %d\n", otroInt, unInt, resultadoInt);
    resultadoInt = otroInt - unInt;
    printf("%d - %d = %d\n", otroInt, unInt, resultadoInt);

    printf("\nLong\n");
    resultadoLong = otroLong* unLong;
    printf("%d * %d = %d\n", otroLong, unLong, resultadoLong);
    resultadoLong = otroLong / unLong;
    printf("%d / %d = %d\n", otroLong, unLong, resultadoLong);
    resultadoLong = otroLong % unLong;
    printf("%d mod %d = %d\n", otroLong, unLong, resultadoLong);
    resultadoLong = otroLong + unLong;
    printf("%d + %d = %d\n", otroLong, unLong, resultadoLong);
    resultadoLong = otroLong - unLong;
    printf("%d - %d = %d\n", otroLong, unLong, resultadoLong);
    
    return 0;
}