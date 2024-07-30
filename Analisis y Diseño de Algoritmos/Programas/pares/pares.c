#include<stdio.h>

void pares(){
    int i,j=0;
    for(i=0;i<200;i=i+2){
        printf("%d ",i);
    }
}

int main (){
    pares();
    return 0;
}