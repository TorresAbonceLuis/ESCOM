/*
1. Torres de hanoi (iterado y recursivo)
           / si n == 1 ==> 1
hanoi(n) = |
           \ si n >  1 ==> 2*hanoi(n-1)+1
            */
#ifndef HANOIRECURSIVO_H
#define HANOIRECURSIVO_H

#include <stdio.h>
#include <stdlib.h>

int hanoiRecursivo(int n){
    if (n==1){
        return 1;
    }
    return 2*hanoiRecursivo(n-1)+1;
}

void menuHanoiRecursivo(){
    int discos;
    printf( "Cuantos discos: " );
    scanf( "%d",&discos );
    printf("%d\n",hanoiRecursivo(discos));
}

#endif //LIBRERIA_H