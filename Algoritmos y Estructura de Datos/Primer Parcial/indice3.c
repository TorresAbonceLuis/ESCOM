//Torres Abonce Luis Miguel
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int *arreglo1,*arreglo2,*arreglo3,i,j=0,k=0,x;
    arreglo1  =  (int *) calloc(4, sizeof(int));
    arreglo2 =  (int *) calloc(5, sizeof(int));
    arreglo3 = (int *) calloc(10, sizeof(int));
    arreglo1[0]=-1,arreglo1[1]=0,arreglo1[2]=1,arreglo1[3]=2,arreglo1[4]=5;
    arreglo2[0]=7,arreglo2[1]=9,arreglo2[2]=11,arreglo2[3]=13,arreglo2[4]=15,arreglo2[5]=20;
    printf( "Indice1: " );
    for(i=0;i<5;i++)
    {
        printf( "%d ",arreglo1[i] );
    }
    printf( "\nIndice2: " );
    for(i=0;i<6;i++)
    {
        printf( "%d ",arreglo2[i] );
    }
    for(i=0;i<11;i++)
    {
        if(j!=4 || k!=5)
        {
            if(arreglo1[j]<arreglo2[k])
            {
                arreglo3[i]=arreglo1[j];
                j++;
            }else
            {
                arreglo3[i]=arreglo2[k];
                k++;
            }
        }
        else if (j==4)
        {
            for(x=k;x<6;x++)
            {
                arreglo3[i]=arreglo2[x];
                i++;
            }
            break;
        }
        else if (k==5)
        {
            for(x=j;x<5;x++)
            {
                arreglo3[i]=arreglo1[x];
                i++;
            }
            break;
        }
    }
    printf( "\nIndice3: " );
    for(i=0;i<11;i++)
    {
        printf( "%d ",arreglo3[i] );
    }
}