//Torres Abonce Luis Miguel
#include <iostream>
using namespace std;

struct nodo
{
	int boleta;
	nodo *sig;	
};
typedef nodo *apu_nodo;

int main()
{
    int opcion,boleta,i;
    apu_nodo inicial,final,aux;
    apu_nodo lista = new(nodo);
    lista=NULL;
    inicial = new(nodo);
    while(1)
	{
        cout<<"\tMenu"<<endl;
        cout<<"1.Insertar una boleta"<<endl;
        cout<<"2.Mostrar lista"<<endl;
        cout<<"3.Salir"<<endl;
        cout<<"Elige una opcion: ";
        cin>>opcion;
        switch (opcion)
        {
            case 1:
            	cout<<"Boleta a instertar: ";
            	aux = new(nodo);
            	cin>>aux->boleta;
            	aux->sig=NULL;
            	if(lista==NULL)
            	{
                	inicial=aux;
                	lista=inicial;
                	final=inicial;
                	break;
            	}
            	else if(aux->boleta<=inicial->boleta)
            	{
                	//cout<<endl<<"inicial: "<<inicial->boleta<<endl;
                	//cout<<endl<<"nuevo inicial : "<<aux->boleta<<endl;
                	aux->sig=inicial;
                	inicial=aux;
                	lista=inicial;
                	//cout<<endl<<"inicial: "<<inicial->boleta<<endl;
                	//cout<<endl<<"inicial sig: "<<lista->boleta<<endl;
                	break;
            	}
            	else if(aux->boleta>=final->boleta)
            	{
                	//cout<<endl<<"final: "<<final->boleta<<endl;
                	//cout<<endl<<"Nuevo final : "<<aux->boleta<<endl;
                	final->sig=aux;
                	final=aux;
                	//cout<<endl<<"final: "<<final->boleta<<endl;
                	break;
            	}
            	apu_nodo recorrer1;
            	recorrer1=lista;
            	while(recorrer1!=NULL)
				{
					if(aux->boleta>recorrer1->boleta && aux->boleta<recorrer1->sig->boleta)
					{
						//cout<<endl<<"recorrer anterior: "<<recorrer1->boleta<<endl;
						//cout<<endl<<"recorrer siguiente: "<<recorrer1->sig->boleta<<endl;
						//cout<<endl<<"recorrer nuevo: "<<aux->boleta<<endl;
						aux->sig=recorrer1->sig;
						recorrer1->sig=aux;
						//cout<<endl<<"recorrer : "<<recorrer1->boleta<<endl;
						//cout<<endl<<"recorrer nuevo: "<<recorrer1->sig->boleta<<endl;
						//cout<<endl<<"recorrer siguiente: "<<recorrer1->sig->sig->boleta<<endl;
					}
					recorrer1=recorrer1->sig;
				}
        	break;
            case 2:
			cout<<endl;
            	apu_nodo recorrer;
            	recorrer=lista;
            	i=0;
            	while(recorrer!=NULL)
            	{
            		i++;
                	cout<<"Boleta #"<<i<<": "<<recorrer->boleta<<endl;
                	recorrer=recorrer->sig;
            	}
				cout<<endl;
        		break;
            case 3:
            	exit(1);
        	break;
        }
    }
    return 0;
}
