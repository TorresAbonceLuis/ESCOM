// Asignacion de memoria dinamica (heap memoria del monton)
//malloc() free()
//prototipo de malloc es
// void malloc(int)

#include <stdio.h>
#include <stdlib.h>

#define MAX_MEM 20

int duplicador = 1;

int *crearMemoriaEntera(int cuantosEnteros){
    int *punteroInt = ( int *) malloc(sizeof(int)*cuantosEnteros);
    return punteroInt;
}

int *duplicarMemoria(int *apuntador){
    int contador = 0;
    int tamanioDeMemoria = sizeof(apuntador);

    // paso 1
    int *ptrTemporal = (int *) malloc(tamanioDeMemoria);
    // DEBUG
    printf( "%d\n",tamanioDeMemoria );
    if(ptrTemporal==NULL){
        printf( "No se pudo asignar la memoria de %d bytes\n", tamanioDeMemoria );
    }else{
    // paso 2
        for(contador=0; contador<MAX_MEM*duplicador; contador++){
            ptrTemporal[contador] = 0;
        ptrTemporal[contador] = apuntador[contador];
        // DEBUG 
        printf( "%d = %d\n",ptrTemporal[contador], apuntador[contador] );
        }
    // paso 3
    duplicador++;
        apuntador = (int *) malloc(tamanioDeMemoria*duplicador);
        if (apuntador!=NULL){
            for(contador=0; contador<MAX_MEM*duplicador; contador++){
                apuntador [contador] = 0;
            apuntador[contador] = ptrTemporal[contador]  ;
            //printf( "%d\n", punteroInt[contador] );
            }
        }else{
            duplicador--;
        }
    }
    free (ptrTemporal);
    return apuntador;

}

int main (int argc, char *argv[]){
    int contador =0;
    int *punteroInt = crearMemoriaEntera(MAX_MEM);
    if(punteroInt==NULL){
        printf( "No se pudo asignar la memoria de %d bytes\n", MAX_MEM*sizeof(int) );
    }else{
        for(contador=0; contador<MAX_MEM; contador++){
        punteroInt[contador] = contador*100;
        printf( "%d\n", punteroInt[contador] );
        }
    }
    punteroInt = duplicarMemoria(punteroInt);
    if(punteroInt==NULL){
        printf( "No se pudo asignar la memoria de %d bytes\n", MAX_MEM*sizeof(int)*(duplicador+1) );
    }else{
        for(contador=0; contador<MAX_MEM*duplicador; contador++){
        //punteroInt[contador] = contador*100;
        printf( "%d\n", punteroInt[contador] );
        }
    }
    if(punteroInt!=NULL){
        printf( "Liberando la memoria de %d bytes\n", MAX_MEM*sizeof(int)*duplicador );
        free(punteroInt);
    }
    return 0;
}