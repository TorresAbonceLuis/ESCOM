#include<stdio.h>
/*
Se requiere calcular la siguiente ecuacion y = 2x^2+ 3,empleamos datos desde -3 hasta
3 para la variable x
*/
int main(int argc,char *argv[]){
    int y,x;
    printf("Problema para calcular la ecuacion: y=2x^2+3\n ");
    printf("Introdcuzca el valor de la variable x = ");
    scanf("%d",&x);
    //ecuacion y=2x^2+3
    y = 2*x*x+3;
    printf("Para el valor de x = %d, el calculo de y = %d\n",x,y);
    return 0;
}