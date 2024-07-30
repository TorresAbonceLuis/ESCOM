//Torres Abonce Luis Miguel
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int unirArreglos(int arreglo1[],int arreglo2[],int tamanio1,int tamanio2)
{
    int i,*arreglo3;
    int tamanio3=tamanio1+tamanio2;
    arreglo3=(int *)calloc(tamanio3, sizeof(int));
    for(i=0;i<tamanio1;i++)
    {
        arreglo3[i]=arreglo1[i];
    }
    for(i=0;i<tamanio2;i++)
    {
        arreglo3[i+tamanio1]=arreglo2[i];
    }
    printf( "\n" );
    for(i=0;i<tamanio3;i++)
    {
        printf("%d ",arreglo3[i]);
    }
    return *arreglo3;
}

int main()
{
    srand(time(NULL));
    int *arregloPrincipal,tamanio,i,*izquierdo,*derecho,mitadI,mitadD;
    do{
        printf( "De que tamanio el arreglo (Debe ser > 2): " );
        scanf( "%d",&tamanio );
    }while(tamanio<2);
    arregloPrincipal=(int *)calloc(tamanio,sizeof(int));
    for(i=0;i<tamanio;i++)
    {
        arregloPrincipal[i]=rand()%10;
    }
    printf( "Arreglo sin ordenar:" );
    for(i=0;i<tamanio;i++)
    {
        printf( "%d",arregloPrincipal[i] );
        if(i!=tamanio-1)
        {
            printf( "," );
        }
    }
    /////////////////////////////////////////////////
    mitadI=tamanio/2;
    mitadD=tamanio-mitadI;
    izquierdo=(int *)calloc(mitadI, sizeof(int));
    derecho=(int *)calloc(mitadD, sizeof(int));
    for(i=0;i<mitadI;i++)
    {
        izquierdo[i]=arregloPrincipal[i];
    }
    for(i=0;i<mitadD;i++)
    {
        derecho[i]=arregloPrincipal[i+mitadI];
    }
    //if(mitadI==1 && mitadD==1)
    //{
        if(izquierdo[0]<derecho[0])
        {
            unirArreglos(izquierdo,derecho,mitadI,mitadD);
        }else
        {
            unirArreglos(derecho,izquierdo,mitadD,mitadI);
        }
    //}
    
    /*
    if(mitad==1){
        printf( "\nTiene solo un elemento Izquierdo. " );
    }
    printf( "\nIzquierdo: " );
    for(i=0;i<mitad;i++)
    {
        printf( "%d",izquierdo[i] );
        if(i!=mitad-1)
        {
            printf( "," );
        }
    }
    if(tamanio-mitad==1){
        printf( "\nTiene solo un elemento Derecho." );
    }
    printf( "\nderecho:   " );
    for(i=mitad;i<tamanio;i++)
    {
        printf( "%d",derecho[i] );
        if(i!=tamanio-1)
        {
            printf( "," );
        }
    }
    */
    return 0;
}