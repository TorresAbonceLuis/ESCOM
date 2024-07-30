#include <stdio.h>
#define MAX 10

 int numeros[MAX];
 int *ptrNumero = numeros;
 int contador = 0;

int main(int argc, char *argv[]) {
 // recorer arreglo indice
 for( contador=0; contador<MAX; contador++) {
 	numeros[contador] = 0;
 	printf("%d\n", numeros[contador]);
 	}
 for( contador=0; contador<MAX; contador++) {
 	*ptrNumero++ = contador;
 	}
 for( contador=0; contador<MAX; contador++) {
 	printf("%d\n", numeros[contador]);
 	}
 contador--;
 *ptrNumero--;
 while(1) {
 	if(contador==-1) {
 		break;
 		}
 	else {
 		printf("%d\n", *ptrNumero--);
 		}
 	contador--;
 	}
 //*ptrNumero++;
 while(1) {
 	if(contador==9) {
 		break;
 		}
 	else {
 		printf("%d\n", *(ptrNumero+=1));
 		}
 	contador++;
 	}
 printf("%d\n", *ptrNumero);
 while(1) {
 	if(contador==0) {
 		break;
 		}
 	else {
 		printf("%d\n", *(ptrNumero-=1));
 		}
 	contador--;
 	}
   return 0;
 }