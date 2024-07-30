#include <stdio.h>
int main(int argc,char *argv[]){
    char nombreUsuario[10];                                 //Memoria
    printf("Introduzca su nombre:");                        //Unidad de control->>Monitor
    scanf("%s",nombreUsuario);                              //Unidad de control->>Teclado
    printf("Hola %s como estas hoy?\n",nombreUsuario);      //Unidad de control->>Monitor
    return 0;
}