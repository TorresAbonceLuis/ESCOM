//Torres Abonce Luis Miguel
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int comprobarExistencia(long int a[],long int b,long int num){
    long int i;
    //if(b%2==1){
        for(i=0;i<num;i++)
        {
            if(b == a[i])
            {
                return 1;
            }
        }
        return 0;
    //}
    //return 1;
}
int main()
{
    float t1,t2;
    long int numero,i,b,c,j;
    srand(time(NULL));
    printf( "Cuantos numeros quieres generar?" );
    scanf( "%ld",&numero );
    long int a[numero];
    t1=clock();
    for(i=0;i<numero;i++)
    {
        //do
        //{
            a[i] = rand()%10;
        //}while(comprobarExistencia(a,b,numero)==1);
        //a[i] = b;
    }
    t2=clock(); 
    printf( "Tiempo en generar:%.2f segundos",t2-t1 );
    //for(i=0;i<numero;i++)
    //{
        //printf( "%ld",a[i] );
        //if( i != numero-1 )
        //{
            //printf( "," );
       // }
    //}
    printf( "\n\n" );
    t1 = clock();
    for(i=0;i<numero;i++)
    {
        for(j=0;j<numero;j++)
        {
            if(a[j]>a[j+1])
            {
                c=a[j];
                a[j]=a[j+1];
                a[j+1]=c;
            }   
        }
    }
    //for(i=0;i<numero;i++)
    //{
        //printf( "%ld",a[i] );
        //if( i != numero-1 )
        //{
            //printf( "," );
        //}
    //}
    t2 = clock();
    printf("tiempo en ordenar: %.2f segundos ",(t2 - t1)*0.001);
    return 0;
}