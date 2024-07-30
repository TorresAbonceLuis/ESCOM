#include <stdio.h>

float otroFloat = 3.141516;
double otroDouble = 2.71;

int main(int argc, char *argv[]){
    float unFloat = 13.141516;
    double unDouble = 12.71;
    float resultadoFloat;
    double resultadoDouble;
    printf("\n Flotantes \n");
    resultadoFloat = otroFloat * unFloat;
    printf("%f * %f = %f\n", otroFloat, unFloat, resultadoFloat);
    resultadoFloat = otroFloat / unFloat;
    printf("%f * %f = %f\n", otroFloat, unFloat, resultadoFloat);
    //resultadoFloat = otroFloat % unFloat;
    //printf("%f * %f = %f", otroFloat, unFloat, resultadoFloat);
    resultadoFloat = otroFloat + unFloat;
    printf("%f * %f = %f\n", otroFloat, unFloat, resultadoFloat);
    resultadoFloat = otroFloat - unFloat;
    printf("%f * %f = %f\n", otroFloat, unFloat, resultadoFloat);

    printf("\n Double \n");
    resultadoDouble = otroDouble * unDouble;
    printf("%f * %f = %f\n", otroDouble, unDouble, resultadoDouble);
    resultadoDouble = otroDouble / unDouble;
    printf("%f * %f = %f\n", otroDouble, unDouble, resultadoDouble);
    //resultadoDouble = otroDouble % unDouble;
    //printf("%f * %f = %f", otroDouble, unDouble, resultadoDouble);
    resultadoDouble = otroDouble + unDouble;
    printf("%f * %f = %f\n", otroDouble, unDouble, resultadoDouble);
    resultadoDouble = otroDouble - unDouble;
    printf("%f * %f = %f\n", otroDouble, unDouble, resultadoDouble);

    
    return 0;
}