//Torres Abonce Luis Miguel
#include <iostream>
using namespace std;

struct nodo
{
	int boleta;
	nodo *sig;
    nodo *ant;	
};
typedef nodo *apu_nodo;

int main()
{
    int opcion,i;
    apu_nodo inicial,final,aux,actual;
    apu_nodo lista = new(nodo);
    lista=NULL;
	inicial=NULL;
	final=NULL;
	actual=NULL;
    while(1)
	{
        cout<<"\tMenu"<<endl;
        cout<<"1.Insertar una boleta"<<endl;
        cout<<"2.Mostrar lista"<<endl;
        cout<<"3.Eliminar boleta"<<endl;
		cout<<"4.Salir"<<endl;
        cout<<"Elige una opcion: ";
        cin>>opcion;
        switch (opcion)
        {
            case 1:
            	cout<<"Boleta a instertar: ";
            	aux = new(nodo);
            	cin>>aux->boleta;
            	aux->sig=NULL;
                aux->ant=NULL;
            	if(inicial==NULL)
            	{
                	inicial=aux;
                	lista=inicial;
                	final=inicial;
                	break;
            	}
            	else if(aux->boleta<=inicial->boleta)
            	{
                    inicial->ant=aux;
                	aux->sig=inicial;
                	inicial=aux;
                	lista=inicial;
                	break;
            	}
            	else if(aux->boleta>=final->boleta)
            	{
                    aux->ant=final;
                	final->sig=aux;
                	final=aux;
                	break;
            	}
            	actual=lista;
            	while(actual!=NULL)
				{
					if(aux->boleta>actual->boleta && aux->boleta<actual->sig->boleta)
					{
						aux->sig=actual->sig;
                        aux->ant=actual;
                        actual->sig->ant=aux;
						actual->sig=aux;
					}
					actual=actual->sig;
				}
        	break;
            case 2:
				if(inicial==NULL)
				{
					cout<<"No hay elementos en la lista"<<endl;
					break;
				}
				cout<<endl;
            	actual=lista;
            	i=0;
            	while(actual!=NULL)
            	{
            		i++;
                	cout<<"Boleta #"<<i<<": "<<actual->boleta<<endl;
                	actual=actual->sig;
            	}
				cout<<endl;
        		break;
            case 3:
				if(inicial==NULL)
				{
					cout<<"No hay elementos en la lista"<<endl;
					break;
				}	
				int boleta; 
            	cout<<"Boleta a eliminar:";
				cin>>boleta;
				if(boleta==inicial->boleta)
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
				else if(boleta==final->boleta)
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
				actual=lista;
				while(actual!=NULL)
				{
					if(boleta>actual->boleta && boleta<actual->sig->boleta)
					{
						
					}
					actual=actual->sig;
				}
        	break;
			case 4:
            	exit(1);
        	break;
        }
    }
    return 0;
}