//Torres Abonce Luis Miguel
#include <stdio.h>
#include <iostream>

using namespace std;

struct nodo
{
	int boleta;
	nodo *sig;	
};
typedef nodo *apu_nodo;
/*
class lista
{
	public:
	apu_nodo inicio;
};*/
int main(void)
{
	int i=0;
	char a='b';
	apu_nodo inicial;
	inicial=new(nodo);/*
	while(a!='s' && a!='n')
	{
		cout<< "Quieres agregar una boleta? (s/n): ";
		cin>>a;
	}
	if(a=='n')
	{
		exit (1);
	}*/
	cout<<"Boleta:";
	cin>>inicial->boleta;
	inicial->sig=NULL;
	inicial=inicial->sig;
	apu_nodo final;
	final=inicial;
	while(i<2)
	{
		apu_nodo actual;
		actual= new(nodo);
		final = new(nodo);
		cout<<"Boleta:";
		cin >>actual->boleta;
		actual->sig = NULL;
		final->sig=actual;
		cout<<endl<<final->sig->boleta<<endl;
		final=final->sig;
		a='b';
		i++;
	}
	while(inicial!=NULL)
	{
		cout<<inicial->boleta<<endl;
		inicial = inicial->sig;
	}
	/*
	apu_nodo nuevo;
	nuevo = new(nodo);
	cout<<"Boleta:";
	cin>>nuevo->boleta;
	nuevo->sig = inicial;
	while(nuevo!=NULL)
	{
		cout<<nuevo->boleta<<endl;
		nuevo = nuevo->sig;
	}
	*/return 0;
}