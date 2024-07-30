// Tonahtiu Ramirez
#include <stdio.h>
#include <iostream>

using namespace std;

struct nodo
{
	int edad;
	int peso;
	long int boleta;
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
	//crear nodo inicial
	apu_nodo auxiliar = new(nodo);
	apu_nodo actual, inicial;
	
	inicial = auxiliar;
	actual = inicial;
	
	actual->edad = 20;
	actual->peso = 65;
	actual->boleta = 202112312;
	actual->sig = NULL;
	
	//crear otro nodo
	auxiliar = new(nodo);
	auxiliar->edad = 1;
	auxiliar->peso = 2;
	auxiliar->boleta = 202112313;
	auxiliar->sig = NULL;
		//unir los nodos
		actual->sig = auxiliar;
		
	actual = auxiliar;
	
	//crear tercer nodo
	auxiliar = new(nodo);
	auxiliar->edad = 11;
	auxiliar->peso = 22;
	auxiliar->boleta = 202112314;
	auxiliar->sig = NULL;
		actual->sig = auxiliar;
	actual = auxiliar;
	
	//imprime lista
	auxiliar = inicial;
	int n=1;
	
	while(auxiliar != NULL)
	{
		cout << "Alumno: " << n << ", edad: " << auxiliar->edad << endl;
		n++;
		auxiliar = auxiliar->sig;
	}
	
	
	
	
	/*
	mi_lista.inicio = new(nodo);
	mi_lista.inicio->dato = 5;
	cout << endl << mi_lista.inicio->dato;
	*/
	return 1;
}


