/*Tovar Vite Rocio Ang�lica
Lopez Cruz Cesar
Torres Abonce Luis Miguel*/
//Manejo de listas doblemente ligadas 
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;
struct nodo
{
	int dato;
	nodo *sig;
	nodo *ant;
};

typedef nodo *apu_nodo;
int main (void)
{
	int op, num, i;
	apu_nodo inicial, aux, actual, anterior;
	actual=NULL,anterior=NULL;
	srand(time(NULL));
	cout << "---MANEJO DE LISTAS DOBLEMENTE LIGADAS---" << endl;
	cout << "Desarrollado por:\n Angelica Vite\n Cesar Lopez Cruz\n Luis Miguel Abonce" << endl << endl;
	do
	{
		cout << "\tMENU" << endl;
		cout << "1.- Agregar n numeros aleatorios" << endl;
		cout << "2.- Quitar los pares" << endl;
		cout << "3.- Quitar los impares" << endl;
		cout << "4.- Muestra lista separados con tabulados" << endl;
		cout << "5.- Salir" << endl;
		cin >> op; cout << endl;
		switch (op)
		{
			case 1:
				cout << "Cuantos numeros desea generar  ";
				cin >> num;
				for (i=0; i<num;i++)
				{
					aux= new(nodo);
					aux->dato=rand()%40;
					
					if (inicial==NULL) //primer nodo 
					{
						inicial=aux;
						inicial->sig=NULL;
                        inicial->ant=NULL;
						actual=inicial;	
					}					
					else
					{
						while(actual->sig!=NULL && actual->dato>aux->dato) //Busca un siguiente nodo 
						{
							anterior=actual;
							actual=actual->sig;
						}
						
						if (actual->sig==NULL && actual->dato>aux->dato) //Ultima posici�n 
						{
							aux->sig=NULL;
							aux->ant=actual;
							actual->sig=aux;
							actual=inicial;
							anterior=NULL;
						}	
						else if (anterior==NULL) //Primera posici�n 
						{
							aux->ant=NULL;
							aux->sig=inicial;
							inicial->ant=aux;
							inicial=aux;
							actual=inicial;
						}
						else //Entre nodos
						{
							aux->sig=actual;
							aux->ant=anterior;
							anterior->sig=aux;
							actual->ant=aux;
							actual=inicial;
							anterior=NULL;
						}
					}
				}
				cout << "Listo" << endl;
			break;
			case 2:
				aux=inicial;
				if (inicial==NULL)
				{
					cout << endl << "No hay elementos en la lista" << endl;
				}
				while (aux!=NULL)
				{
					if(aux->dato%2==0)
				  	{
						if (aux->ant==NULL && aux->sig==NULL) //Unico nodo 
						{
							delete(aux);
							aux=NULL;
							inicial=aux;
							cout << endl << "No quedan elemntos en la lista" << endl;
						}
						else if(aux->ant==NULL)//inicio
						{
							aux=aux->sig;
							aux->ant=NULL;
							delete(inicial);
							inicial=NULL;
							inicial=aux;
						}
						else if(aux->sig!=NULL)//en medio
						{
							anterior=aux	;	
							aux->ant->sig=aux->sig;
							aux->sig->ant=aux->ant;		
							aux=aux->sig;
							delete(anterior);
							anterior=NULL;
						}
						else//eliminar el ultimo nodo
						{
							aux->ant->sig=NULL;
							delete(aux);
							aux=NULL;
						}
					}
					else 
					{
						aux=aux->sig;
					}
				}
			break;
			case 3:
				aux=inicial;
				if (inicial==NULL)
				{
					cout << endl << "No hay elementos en la lista" << endl;
				}
				while (aux!=NULL)
				{
					if(aux->dato%2==1)
				  	{
						if (aux->ant==NULL && aux->sig==NULL)
						{
							delete(aux);
							aux=NULL;
							inicial=aux;
							cout << endl << "No quedan elemntos en la lista" << endl;
						}
						else if(aux->ant==NULL)//inicio
						{
							aux=aux->sig;
							aux->ant=NULL;
							delete(inicial);
							inicial=NULL;
							inicial=aux;
						}
						else if(aux->sig!=NULL)//en medio
						{
							anterior=aux	;	
							aux->ant->sig=aux->sig;
							aux->sig->ant=aux->ant;		
							aux=aux->sig;
							delete(anterior);
							anterior=NULL;
						}
						else
						{
							aux->ant->sig=NULL;
							delete(aux);
							aux=NULL;
						}
					}
					else 
					{
						aux=aux->sig;
					}	
				}
			break;
			case 4:
				aux=inicial;
				if (inicial==NULL)
				{
					cout << endl << "No hay elementos en la lista" << endl;
				}
				while(aux!=NULL)
				{
					cout << aux->dato << "\t" ;
					aux=aux->sig;		
				}
				cout << endl;
			break;			
		}
	}while (op!=5);
	return 0;
}