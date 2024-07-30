#include <stdio.h>//librerias a utilizar
#include <stdlib.h>//librerias a utilizar

#define IVA .16
int main(int argc, char *argv){//inicio de programa
    float totaldecompra, cambio,totaldecompraiva;//declaracion de variables flotantes
    int Billetes[5], cantidaddebilletes[5], Monedas[4], cantidaddemonedas[4];//declaracion de arreglos enteros
    int contador;//declaracion de variables enteras
    char nombreCliente[30];//declaracion de cadena de caracteres
    for(contador=0;contador<5;contador++){//ciclo para inicializara los arreglos 
        cantidaddebilletes[contador]=0; //dar valor de 0 a los arreglos
        cantidaddemonedas[contador]=0;//dar valor de 0 a los arreglos
    }
    Monedas[0]=10,Monedas[1]=5,Monedas[2]=2,Monedas[3]=1;
    Billetes[0]=500, Billetes[1]=200, Billetes[2]=100, Billetes[3]=50,Billetes[4]=20;//dar los valores a los billetes de cada categoria
    printf("\nIntroducir Nombre del cliente: ");//imprimir en pantalla
    gets(nombreCliente);//guardar la informacion en la direccion
    printf("\n\n\t\tBienvenido a la caja %s\n",nombreCliente);//imprimir en pantalla
    printf("\nTotal de compra:$");//imprimir en pantalla
    scanf("%f",&totaldecompra);//guardar la informacion en la direccion requerida
    totaldecompraiva=totaldecompra*IVA;
    printf("IVA:%.2f",totaldecompraiva);
    totaldecompra+=totaldecompraiva;
    printf("\nTotal de compra + iva:$%.2f",totaldecompra);
    printf("\n\nCantidad depositada:$");//imprimir en pantalla
    scanf("%f",&cambio);//guardar la inforacion en la direccion requerida
    cambio -= totaldecompra;//restar el cambio a el total de compra para obtener el cambio a trabajar
    if(cambio>=0){//control de flujo
        printf("Cambio:$%.2f\n",cambio);//imprimir ne pantalla
        do{//ciclo para resatr el valor de cada categoria de billetes al cambio hasta lleagr a 0
           if(cambio>=Billetes[0]){//control de flujo que si el valor del cambio es mayor al valor del billete se cumple
                cambio-=Billetes[0];//se le resta el valor de billete al cambio cambio-=Billetes[0] es una simplificaicon de cambio=cambio-Billetes[0]
                cantidaddebilletes[0]++;//se le suma 1 a la cantidad de billetes para llevar la cuenta
            }
            else if(cambio>=Billetes[1]){//control de flujo que si el valor del cambio es mayor al valor del billete se cumple
                cambio-=Billetes[1];//se le resta el valor de billete al cambio cambio-=Billetes[0] es una simplificaicon de cambio=cambio-Billetes[1]          
                cantidaddebilletes[1]++;//se le suma 1 a la cantidad de billetes para llevar la cuenta
            }
            else if(cambio>=Billetes[2]){//control de flujo que si el valor del cambio es mayor al valor del billete se cumple
                cambio-=Billetes[2];//se le resta el valor de billete al cambio cambio-=Billetes[0] es una simplificaicon de cambio=cambio-Billetes[2]
                cantidaddebilletes[2]++;//se le suma 1 a la cantidad de billetes para llevar la cuenta
            }
            else if(cambio>=Billetes[3]){//control de flujo que si el valor del cambio es mayor al valor del billete se cumple
                cambio-=Billetes[3];//se le resta el valor de billete al cambio cambio-=Billetes[0] es una simplificaicon de cambio=cambio-Billetes[3]
                cantidaddebilletes[3]++;//se le suma 1 a la cantidad de billetes para llevar la cuenta
            }
            else if(cambio>=Billetes[4]){//control de flujo que si el valor del cambio es mayor al valor del billete se cumple
                cambio-=Billetes[4];//se le resta el valor de billete al cambio cambio-=Billetes[0] es una simplificaicon de cambio=cambio-Billetes[4]
                cantidaddebilletes[4]++;//se le suma 1 a la cantidad de billetes para llevar la cuenta
            }
            else if(cambio>=Monedas[0]){//control de flujo que si el valor del cambio es mayor al valor del billete se cumple
                cambio-=Monedas[0];//se le resta el valor de la moneda al cambio cambio-=Monedas[0] es una simplificaicon de cambio=cambio-Monedas[0]
                cantidaddemonedas[0]++;//se le suma 1 a la cantidad de monedas para llevar la cuenta
            }
            else if(cambio>=Monedas[1]){//control de flujo que si el valor del cambio es mayor al valor del billete se cumple
                cambio-=Monedas[1];//se le resta el valor de la moneda al cambio cambio-=Monedas[0] es una simplificaicon de cambio=cambio-Monedas[1]
                cantidaddemonedas[1]++;//se le suma 1 a la cantidad de monedas para llevar la cuenta
            }
            else if(cambio>=Monedas[1]){//control de flujo que si el valor del cambio es mayor al valor del billete se cumple
                cambio-=Monedas[2];//se le resta el valor de la moneda al cambio cambio-=Monedas[0] es una simplificaicon de cambio=cambio-Monedas[2]
                cantidaddemonedas[2]++;//se le suma 1 a la cantidad de monedas para llevar la cuenta
            }
            else if(cambio>=Monedas[3]){//control de flujo que si el valor del cambio es mayor al valor del billete se cumple
                cambio-=Monedas[3];//se le resta el valor de la moneda al cambio cambio-=Monedas[0] es una simplificaicon de cambio=cambio-Monedas[3]
                cantidaddemonedas[3]++;//se le suma 1 a la cantidad de monedas para llevar la cuenta
            }
        }while(cambio>=1);//solo podra salir del ciclo si no cumple la condicion
        cambio-=cambio;//se redondea el cambio para que este sea igual a 0
        for(contador=0;contador<5;contador++){//ciclo para mandar imprimir
        	if(cantidaddebilletes[contador]>0)//control de flujo para imprimir solo si la cantidad de billetes es mayor que 0 y ocupe lugar inesceario en la pantalla
                printf("\nCantidad a dar billetes de $%d:%d",Billetes[contador],cantidaddebilletes[contador]);//imprimir en pantalla la cantidad de billetes
        }
        for(contador=0;contador<4;contador++){
        	if(cantidaddemonedas[contador]>0)//control de flujo para imprimir solo si la cantidad de monedas es mayor que 0 y ocupe lugar inesceario en la pantalla
                printf("\nCantidad a dar monedas de $%d:%d",Monedas[contador],cantidaddemonedas[contador]);//imprimir en pantalla la cantidad de monedas
        }
        printf("\n\nVuelva pronto\n");//imprimir en pantalla una despedida
    }
    else{//control de flujo para verificar que al cliente si le alcanza con la cantidad dada la compra de sus productos
        printf("Falta dinero");//imprimir a pantalla el mensaje
    }
    return 0;//regresar un valor 
}