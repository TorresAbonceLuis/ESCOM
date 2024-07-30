// Autor: Tonahtiu Arturo Ramirez Romero
// Funcion: Ordenamiento por mezcla enteros, minimo
//fecha: 2018-Sep-22
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void mezclador(int arreglo[], int arreglo_izq[], int izq_elems, int arreglo_der[], int der_elems)
{
	int completado=0;
	int i_izq=0, i_der=0, i_mezcla=0;
	
	while(!completado)	
	{
		if( (i_izq < izq_elems) && (i_der < der_elems) )
		{
			if(arreglo_izq[i_izq] > arreglo_der[i_der])
			{
				arreglo[i_mezcla] = arreglo_der[i_der];
				i_der++;
			}
			else
			{
				arreglo[i_mezcla] = arreglo_izq[i_izq];
				i_izq++;
			}
		}
		else
		{
			if(i_izq < izq_elems)
			{
				arreglo[i_mezcla] = arreglo_izq[i_izq];
				i_izq++;
			}
			else
			{
				arreglo[i_mezcla] = arreglo_der[i_der];
				i_der++;
			}
		}
		i_mezcla++;
		
		if( (i_izq+i_der) == (izq_elems+der_elems))
			completado = 1;
	}
}

void  ordena_divide(int arreglo[], int num_elementos)
{
	if (num_elementos > 1) 
	{
		int i,j,izq_elems, der_elems;  //numero de elementos en ambos arreglos
		int *arreglo_izq, *arreglo_der;

		der_elems = izq_elems = num_elementos / 2;
		if (num_elementos % 2 != 0)
			izq_elems++;

    	arreglo_izq = new int [izq_elems];
    	arreglo_der = new int [der_elems];
 
        for(i = 0; i < izq_elems; i++)
            arreglo_izq[i] = arreglo[i];
 
        for(j=0; j < der_elems; j++, i++ )
        	arreglo_der[j] = arreglo[i];
   	
		//Se procesa el segmento izquierdo, luego el derecho		
		ordena_divide(arreglo_izq, izq_elems);
		ordena_divide(arreglo_der, der_elems);
		
		//Hace la mezcla ordenada de los arreglo izquiero y derecho lo sube al arreglo de esta iteracion
		mezclador(arreglo, arreglo_izq, izq_elems, arreglo_der, der_elems);
		
		//Libera los arreglos ya trabajados
		delete(arreglo_izq);
		delete(arreglo_der);
	}
}

int main(void)
{
	float t1,t2;
	int tamanio,i,*arreglo;
	srand(time(NULL));
	printf( "Tamanio del arreglo: " );
	scanf( "%d",&tamanio );
	arreglo=(int *)calloc(tamanio,sizeof(int));
	if(arreglo==NULL){
		printf("No se pudo generar el arreglo");
		exit (1);
	}
	for(i=0;i<tamanio;i++)
    {
        arreglo[i]=rand()%20;
    }
    t1=clock();
	//printf("Lista desordenada\n");
    //for(i = 0; i < tamanio; i++)
    //    printf("%d \t",arreglo[i]);

    ordena_divide(arreglo, tamanio);
    
    t2=clock();
    printf("tiempo en ordenar: %.2f segundos ",(t2 - t1)*0.001);
    //printf("\nLista ordenada\n");
    //for(i = 0; i < tamanio; i++)
    //    printf("%d \t",arreglo[i]);
    
	return 0;
}
