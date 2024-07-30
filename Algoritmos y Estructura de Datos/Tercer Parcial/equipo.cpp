//Olguin Castillo Brayan Mauricio
//#include <stdio.h>
#include <iostream>
#include <ctime>
//#include <stdlib.h>

using namespace std;
 
struct nodo{
      	long int boleta;        
    	nodo *sig; 
    	nodo *ant;
};

int main()
{
	nodo *actual = NULL, *auxiliar, *inicial =  NULL, *auxImprimir, *auxImprimir2, *acomodar, *p, *t, *marca = NULL;
    int num, opcion, c=0;    
    long int aux, tem, borrar, hora = time(NULL), numero, tmp ;  
    
    //apu_nodo otro;
    
    
    
    while(1)
    {
    	cout << endl << endl;
    	cout<<"MANEJO DE LISTAS DOBLEMENTE LIGADAS" << endl;
    	cout << "Desarrollado por: " << endl;
    	cout << "Olguin Castillo Brayan Mauricio. " << endl;
    	cout << "Leon Martinez Ana Karen " << endl;
		cout << "Martinez Molina Diego " << endl;
   		cout << "Agregar N numeros = 1" << endl;
		cout << "Quitar los pares = 2" << endl;
		cout << "Quitar los impares = 3" << endl;
		cout << "Muestra numeros (separados por tabuladores) = 4" << endl;
		cout << "Salir = 5" << endl;
		
		cout << endl;
		
    	cout<<" Que opcion desea?: ";
		cin >> opcion;
 
        switch(opcion)
        {
            case 1:
            	cout << "Cuantos numeros aleatorios desea generar?: ";
            	cin >> num;
    			srand(hora);
    			for (c=0; c<num; c++)
    			{	
        			numero = rand() % 40;
        			//cout << numero;
        			auxiliar = new(nodo);
   			 		auxiliar->boleta = numero;
    				auxiliar->sig = NULL;
    				auxiliar->ant = NULL;
	    			if(inicial == NULL)
	    			{
	    				inicial = auxiliar;
	    				actual = auxiliar;
					}
					else
					{
						auxiliar->sig = inicial;
						inicial->ant = auxiliar;
						inicial = auxiliar;
					}
					if (inicial==NULL)  
				 	{ 
					 	cout << "La lista no contiene elementos :c" << endl;  
					}
				  else
				   {
						acomodar = auxiliar;
						while(acomodar->sig != NULL) //nuevo.inicio
		   				{
		          			auxiliar = acomodar->sig;
		          
			          		while(auxiliar!=NULL)
			          		{
			               		if(acomodar->boleta < auxiliar->boleta)
			               		{
			                   		tem = auxiliar->boleta;
			                    	auxiliar->boleta = acomodar->boleta;
			                    	acomodar->boleta = tem;          
			               		}
			               		auxiliar = auxiliar->sig;                    
			          		}    
			          		acomodar = acomodar->sig;
			          		auxiliar = acomodar->sig;
						}
					}
				}
            	break;
            case 2: //pares
            	actual = inicial;
            	if(actual == NULL)
            	{
            		cout << "La lista no contiene elementos";
				} 
				else
				{
					while(actual != NULL)
					{
						if(actual->boleta % 2 == 0)
						{
							if(actual->ant == NULL)
							{
								if(actual->sig==NULL)
								{
									auxiliar = actual;
									delete (auxiliar);
									auxiliar = NULL;
									inicial=NULL;
								}
								else
								{
									auxiliar = actual;
									inicial=inicial->sig;
									delete (auxiliar);
									auxiliar = NULL;
								}
							}
							else if(actual->sig == NULL)
							{
								auxiliar = actual;
								actual=actual->ant;
								actual->sig=NULL;
								delete (auxiliar);
								auxiliar = NULL;
							}
							else
							{
								auxiliar = actual;
								actual->ant->sig = actual->sig;
								actual->sig->ant = actual->ant;
								actual = actual->ant;
								delete(auxiliar);
								auxiliar = NULL;
								cout << "Se encontro la boleta y se ha borrado" << endl;
							}
						}
						actual = actual->sig;
					}
				}
				break;
			case 3: //impares
				actual = inicial;
            	if(actual == NULL)
            	{
            		cout << "La lista no contiene elementos";
				} 
				else
				{
					while(actual != NULL)
					{
						if(actual->boleta % 2 != 0)
						{
							if(actual->ant == NULL)
							{
								if(actual->sig==NULL)
								{
									auxiliar = actual;
									delete (auxiliar);
									auxiliar = NULL;
									inicial=NULL;
								}
								else
								{
									auxiliar = actual;
									inicial=inicial->sig;
									delete (auxiliar);
									auxiliar = NULL;
								}
							}
							else if(actual->sig == NULL)
							{
								auxiliar = actual;
								actual=actual->ant;
								actual->sig=NULL;
								delete (auxiliar);
								auxiliar = NULL;
							}
							else
							{
								auxiliar = actual;
								actual->ant->sig = actual->sig;
								actual->sig->ant = actual->ant;
								actual = actual->ant;
								delete(auxiliar);
								auxiliar = NULL;
								cout << "Se encontro la boleta y se ha borrado" << endl;
							}
						}
						actual = actual->sig;
					}
				}
				break;
			case 4:
				auxImprimir = inicial;
            	if(auxImprimir == NULL)
            	{
            		cout << "La lista no contiene elementos, por lo tanto no se imprime nada" << endl;
				}
            	
            	while(auxImprimir != NULL)
    			{
        			cout << auxImprimir->boleta << "\t";
        			auxImprimir = auxImprimir->sig;
        			
    			}
				break;
			case 5:
				return 0;
				break;		
        }
	}
        
	return 0;
}
