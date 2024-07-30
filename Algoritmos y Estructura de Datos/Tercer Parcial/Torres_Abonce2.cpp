//Manejo de listas doblemente ligadas
//Torres Abonce Luis Miguel
#include <iostream>
#include <time.h>
using namespace std;
struct nodo
{
    int numero;
    nodo *sig;
    nodo *ant;
};
typedef nodo *apu_nodo;
void insertarNodoInicial(apu_nodo &inicial,apu_nodo &aux,apu_nodo &final,apu_nodo &lista)
{
    if(inicial==NULL)
    {
        inicial=aux;
        lista=inicial;
        final=inicial;
    }
    else
    {
        inicial->ant=aux;
        aux->sig=inicial;
        inicial=aux;
        lista=inicial;
    }
}
void insertarNodoFinal(apu_nodo &final,apu_nodo &aux)
{
    aux->ant=final;
    final->sig=aux;
    final=aux;
}
void insertarEnmedio(apu_nodo &actual,apu_nodo &aux)
{
    while(actual!=NULL)
    {
        if(actual->numero==aux->numero)
        {
            aux->sig=actual->sig;
            aux->ant=actual;
            actual->sig->ant=aux;
            actual->sig=aux;
            break;
        }
        if(aux->numero<actual->numero && aux->numero>actual->sig->numero)
        {
            aux->sig=actual->sig;
            aux->ant=actual;
            actual->sig->ant=aux;
            actual->sig=aux;
            break;
        }
        actual=actual->sig;
    }
}
void borrarNodoInicial(apu_nodo &inicial,apu_nodo &lista)
{
    if(inicial->sig!=NULL)
	{
		inicial=inicial->sig;
		delete(inicial->ant);
		inicial->ant=NULL;
		lista=inicial;
	}else
	{
		delete(inicial);
		inicial=NULL;
	}
}
void borrarNodoFinal(apu_nodo &final)
{
    if(final->ant != NULL)
	{
		final=final->ant;
		delete(final->sig);
		final->sig=NULL;
	}else
	{
		delete(final);
		final=NULL;
	}
}
void borrarEnmedio(apu_nodo &actual)
{
    apu_nodo borrar;
    borrar = actual;
	actual->ant->sig = actual->sig;
	actual->sig->ant = actual->ant;
	actual=actual->sig;
	delete(borrar);
	borrar=NULL;
}
int main()
{
    cout << "Desarrollado por: " << endl;
    cout << "Angelica Vite" << endl;
    cout << "Cesar López"<< endl;
    cout << "Luis Miguel Abonce"<< endl;
    int opcion=0,numAleat=0,z=0,i;
    srand(time(NULL));
    apu_nodo lista,inicio,final,actual,aux;
    inicio = NULL;
    while(1)
    {
        cout<<"\tMenu"<<endl;
        cout<<"1.Agregar n numeros aleatorios"<<endl;
        cout<<"2.Quitar los numeros pares"<<endl;
        cout<<"3.Quitar los numero impares"<<endl;
        cout<<"4.Mostrar la lista"<<endl;
        cout<<"5.Salir"<<endl;
        cout<<"Elige una opcion:";
        cin>>opcion;
        switch(opcion)
        {
            case 1:
                cout<<"Cantidad de numeros a agregar:";
                cin>>numAleat;
                i=0;
                z=0;
                while(z!=1)
                {
                    while(i!=numAleat)
                    {
                        aux = new(nodo);
                        aux->numero=rand()%40;
                        aux->ant=NULL;
                        aux->sig=NULL;
                        if( inicio==NULL || aux->numero>=inicio->numero )
                        {
                            insertarNodoInicial(inicio,aux,final,lista);
                            i++;
                            break;
                        }
                        if(aux->numero<=final->numero)
                        {
                            insertarNodoFinal(final,aux);
                            i++;
                            break;
                        }
                        actual=lista;
                        insertarEnmedio(actual,aux);
                        i++;
                    }
                    if(i==numAleat)
                    {
                        z=1;
                    }
                }
            break;
            case 2:
                if(inicio==NULL)
				{
					cout<<endl<<"No hay elementos en la lista"<<endl<<endl;
					break;
				}
                actual=lista;
                while(actual!=NULL)
                {
                    while(actual!=NULL)
                    {
                        if(actual->numero%2==0)
                        {
                            if(actual->numero==inicio->numero)
                            {
                                borrarNodoInicial(inicio,lista);
                                actual=actual->sig;
                                break;
                            }
                            else if(actual->numero==final->numero)
                            {
                                borrarNodoFinal(final);
                                actual=actual->sig;
                                break;
                            }
                            borrarEnmedio(actual);
                            break;
                        }else
                        {
                            actual=actual->sig;
                        }
                    }
                }
            break;
            case 3:
                if(inicio==NULL)
				    {
					    cout<<endl<<"No hay elementos en la lista"<<endl<<endl;
					    break;
				    }
                actual=lista;
                while(actual!=NULL)
                {
                    while(actual!=NULL)
                    {
                        if(actual->numero%2!=0)
                        {
                            if(actual->numero==inicio->numero)
                            {
                                borrarNodoInicial(inicio,lista);
                                actual=actual->sig;
                                break;
                            }
                            else if(actual->numero==final->numero)
                            {
                                borrarNodoFinal(final);
                                actual=actual->sig;
                                break;
                            }
                            borrarEnmedio(actual);
                            break;
                        }else{
                            actual=actual->sig;
                        }
                        
                    }
                }
            break;
            case 4:
                if(inicio==NULL)
				{
					cout<<endl<<"No hay elementos en la lista"<<endl<<endl;
					break;
				}
				cout<<endl<<"\tLista"<<endl<<endl;
            	actual=lista;
            	while(actual!=NULL)
            	{
                	cout<<actual->numero<<"\t";
                	actual=actual->sig;
            	}
				cout<<endl;
        	break;
            case 5:
                cout<<endl<<"Adios"<<endl;
            	exit(1);
            break;
            default:
                cout<<endl<<"Ingrese una opcion valida"<<endl<<endl;
        	break;
        }
    }
return 1;
}