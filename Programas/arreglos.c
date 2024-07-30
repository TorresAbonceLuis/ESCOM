#include<stdio.h>
/*
Arreglos 
*/

#define MAX 10
#define MAX_Y 4
#define MAX_X 10
#define MAX_Z 3

int miArreglo[MAX];

int main(int argc, char* argv[]){
    int contador;
    long arreglo2D[MAX_Y][MAX_X];
    int y,x,z;
    float arreglo3D[MAX_Z][MAX_Y][MAX_X];
    // en una dimension
    printf("celda     memoria      valor en memoria\n");
    for(contador=0; contador<MAX; contador++){
        miArreglo[contador] = contador;
        printf("miArreglo[%d]: %x = %d\n",contador, &miArreglo[contador],miArreglo[contador]);
    }
    //en dos dimensiones
    for(y=0; y<MAX_Y; y++){
        for(x=0; x<MAX_X; x++){
            arreglo2D[y][x] = x*y;
        printf("arreglo2D[%d][%d] : %x = %d\n",y,x, &arreglo2D[y][x],arreglo2D[y][x]);
        }
        printf("/n");
    }
    //en tres dimensiones
    for(z=0;z<MAX_Z;z++){
        for(y=0; y<MAX_Y; y++){
          for(x=0; x<MAX_X; x++){
               arreglo2D[y][x] = x*y;
            printf("arreglo3D[%d][%d][%d] : %x = %f\n",
                z,y,x, &arreglo3D[z][y][x],arreglo3D[z][y][x]);
            }
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}