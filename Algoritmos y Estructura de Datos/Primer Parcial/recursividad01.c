//Torres Abonce Luis Miguel
//Recursividad 01
//Este programa imprime numeros
//5 4 3 2 1
#include <stdio.h>

int funcion1(int a,int suma)
{
	if(a==0){
		return suma;
	}
	suma+=a;
	printf("\nVuelta: %d",a);
	return funcion1(a-1,suma);
}

int main()
{
	int a;
	printf("Cuantas veces se repite: ");
	scanf("%d",&a);
	//funcion1(a,0);
	printf( "\nSuma:  %d",funcion1(a,0));
	return 1;
}
