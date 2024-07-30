#ifndef HANOIITERADO_H
#define HANOIITERADO_H

#include <stdio.h>
#include <stdlib.h>

int hanoiIterado(int n){
    int contador,resultado =2;
    for(contador=n-1; contador>0; contador--){
        resultado*=2;
    }
    return resultado-1;
}

void menuHanoiIterado(){
    int n;
    printf("numero de discos: ");
    scanf( "%d",&n );
    printf("%d\n",hanoiIterado(n));
}

#endif //LIBRERIA_H