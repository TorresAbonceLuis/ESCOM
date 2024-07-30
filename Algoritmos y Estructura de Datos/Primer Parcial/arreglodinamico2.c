//Torres Abonce Luis Miguel
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>

int main(void)
{
	float t1,t2,a=0,desviacion=0,sumatoria=0,x,promedio=0;
	int *vect1,n,i;
	// arreglo1 unidimensional
	srand(time(NULL));
	printf("Numero de elementos del arreglo1: ");
	scanf("%d", &n);
	// reservar memoria para almacenar n enteros 
	vect1 = (int *) malloc(n * sizeof(int));
	// Verificamos que la asignaci�n se haya realizado correctamente 
	if (vect1  == NULL) 
	{
		printf( "No se pudo reservar la memoria\n" );
		exit(1);
	// Error al intentar reservar memoria 
	}
	t1=clock();	
	for(i=0;i<n;i++)
	{
        vect1[i] = rand();
		promedio+=vect1[i];
		a++;
    }
	promedio/=a;
	for(i=0;i<n;i++)
	{
		x=vect1[i]-promedio;
		sumatoria=pow(x,2);
		desviacion+=sumatoria;
	}
	desviacion=sqrt(desviacion/a);
	t2=clock();
	printf( "Malloc:%d Tiempo:%.2fs Promedio: %.2f Desviacion: %.2f\n",vect1[i-1],(t2-t1)*0.001,promedio,desviacion);
	free(vect1);
	a=0;
	promedio=0;
	//vect1[1] = 333;
	//vect1[0] = 999;
	//printf("\n Malloc: %d", vect1[0]);
	//printf("\n Malloc: %i", vect1[1]);
	//arreglo1 con calloc
	// Reservar memoria para almacenar n enteros 
	/*
	vect1 =  (int *) calloc(n, sizeof(int));
	// Verificamos que la asignaci�n se haya realizado correctamente 
	if (vect1 == NULL) 
	{
		printf( "No se pudo reservar la memoria\n" );
		exit(1);
	// Error al intentar reservar memoria 
	}
	t1=clock();	
	for(i=0;i<n;i++)
	{
        vect1[i] = rand();
		promedio+=vect1[i];
		a++;
    }
	promedio/=a;
	desviacion=0;
	for(i=0;i<n;i++)
	{
		sumatoria=vect1[i]-promedio;
		sumatoria=pow(sumatoria,2);
		desviacion+=sumatoria;
	}
	desviacion=sqrt(desviacion/a);
	t2=clock();	
	printf( "Calloc:%d tiempo:%.2fs Promedio: %.2f Desviacion: %.2f",vect1[i-1],(t2-t1)*0.001,promedio,desviacion);
	//vect1[1] = 334;
	//printf("\n%d", vect1[1]);
	free(vect1);
	return 0;
	*/
}
	/*
	//arreglo1 bidimensional
	
	int **arr_dinamico;
	int i;
	int m=100;
	
	arr_dinamico = (int **)	malloc(n * sizeof(int *));
	
	for(i=0; i<n; i++)
	{
		arr_dinamico[i] = (int *) calloc(m, sizeof(int ));
	}
	
	
	arr_dinamico[0][98] = 5;
	printf("\n%d", arr_dinamico[0][98] );
	*/
	
	

