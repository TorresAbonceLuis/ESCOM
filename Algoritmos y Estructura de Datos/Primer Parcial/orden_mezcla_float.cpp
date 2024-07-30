// Autor: Tonahtiu Arturo Ramirez Romero
// Funcion: Ordenamiento por mezcla float con comentarios
//fecha: 2018-Sep-22
#include <stdio.h>


void mezclador(float arreglo[], float arreglo_izq[], int izq_elems, float arreglo_der[], int der_elems)
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

void  ordena_divide(float arreglo[], int num_elementos, int muestra_proceso)
{
	if (num_elementos > 1) 
	{
		int i,j,izq_elems, der_elems;  //numero de elementos en ambos arreglos
		float *arreglo_izq, *arreglo_der;

		der_elems = izq_elems = num_elementos / 2;
		if (num_elementos % 2 != 0)
			izq_elems++;
	
    	//printf("\n %d - %d", izq_elems, der_elems);
    	
    	arreglo_izq = new float [izq_elems];
    	arreglo_der = new float [der_elems];
 
 		//if(muestra_proceso)
			printf("\n\nSubarreglo izquierdo: ");
        for(i = 0; i < izq_elems; i++)
        {
            arreglo_izq[i] = arreglo[i];
            //if(muestra_proceso)
            	printf("%3.1f, \t",arreglo_izq[i]);
        }
 
  		//if(muestra_proceso)
			printf("\nSubarreglo derecho: ");
        for(j=0; j < der_elems; j++, i++ )
        {
        	arreglo_der[j] = arreglo[i];
        	//if(muestra_proceso)
            	printf("%3.1f, \t",arreglo_der[j]);        	
		}
            	
		//Se procesa el segmento izquierdo, luego el derecho		
		ordena_divide(arreglo_izq, izq_elems, muestra_proceso);
		ordena_divide(arreglo_der, der_elems, muestra_proceso);
		
		//Hace la mezcla ordenada de los arreglo izquiero y derecho lo sube al arreglo de esta iteracion
		//if(muestra_proceso)
			printf("\n Mezcla");
		mezclador(arreglo, arreglo_izq, izq_elems, arreglo_der, der_elems);
		
		//if(muestra_proceso)
		//{
			printf("\nUltima mezcla: ");
        	for(j=0; j < num_elementos; j++)
            	printf("%3.1f, \t",arreglo[j]);        	
		//}
		
		//Libera los arreglos ya trabajados
		delete(arreglo_izq);
		delete(arreglo_der);
	}
}

int main(void)
{
	float arreglo[]={4,3,5,-1, 8,7,14,34,9,-1};
	//float arreglo[]={1,3,1,2};
	int i, num_regs;
	num_regs = 10;
	
	printf("Lista desordenada\n");
    for(i = 0; i < num_regs; i++)
        printf("%.2f \t",arreglo[i]);

    ordena_divide(arreglo, num_regs,1);
    
    printf("\nLista ordenada\n");
    for(i = 0; i < num_regs; i++)
        printf("%.2f \t",arreglo[i]);
       
	return 0;
}
