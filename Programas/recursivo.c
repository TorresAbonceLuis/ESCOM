/*
2.4 Funciones recursivas

En logica matematica y en computacion las funciones recursivas son una clase de funciones
de los numeros naturales y estos son computables (calculables).

2.4.1 Recursion
Es una forma de atajar y solventar problemas, es resolver un problema mediante soluciones 
que dependen de instancias mas pequenas del mismo problema.
La mayoria de los lenguajes de programacion dan soporte a la recursion permitiendo llamarse 
a si misma a la funcion.

2.4.2 Pasos base y paseo recursivos
Pasos base
	Son aquellos que nos permiten parar la recursividad (condicion necesaria)
Pasos recursivos
	Son aquellos que nos permiten llamar a si misma a la funcion empleando la definicion de
	recursividad de una funcion matematica sobre los numeros naturales

2.4.3 Tipos de Recursion
Directa:
	Es la mas comun y se da cuando una funcion se llama a si misma una o varias veces
Indirecta:
	Se da cuando la funcion se llama de forma indirecta, es decir, por medio de otra funcion

2.4.4 Recursion versus iteracion
Factorial
	4! = 4*3*2*1 (iterado) = 24

	4! = 4*(4-1)!=4*3*(3-1)!=4*3*2*(2-1)!=4*3*2*1*(1-1)!=4*3*2*1*0!=4*3*2*1*1=24 (recursiva)
       / si n==0 => 0!=1
	n!=|
	   \ si n>=1 => n!=n*(n-1)!

Sin los pasos base la iteracion se acaba el stack o pila que es donde se almacenan los pasos intermedios de 
los calculos de la funcion recursiva.

*/

#include <stdio.h>

int calcularFactorialIterado(int n) {
	int factorial = n;
	int contador;
	for(contador=n-1; contador>0; contador--) {
		factorial *= contador;
		}
	return factorial;
}

int calcularFactorialRecursivo(int n) {
	// Pasos base
	if(n==0) {
		return 1;
	}
	// Pasos recursivos
	return n*calcularFactorialRecursivo(n-1);
}// 24 = 4 * 6 = 3 * 2 = 2  *  1 = 1 * 1
/*
fibonacci
 		  / si n == 0 ==> 0 // paso base
 fib(n) = | si n == 1 ==> 1 // paso base
 		  \ si n >= 2 ==> fib(n-2) + fib(n-1)
 n = numero
*/
int calcularFibonacci(int n) {
	// Paso base
	//if( n==0 ) {
	//	return 0;
	//	} 
	//if( n==1 ) {
	//	return 1;
	//	}
	// Paso base
	if(n==0 || n==1) {
		return n;
		}
	//printf("%d,", n);
	// Paso recursivo
	return calcularFibonacci(n-1)+calcularFibonacci(n-2);
}
/*
TAREA para entregar
1. Torres de hanoi (iterado y recursivo)
           / si n == 1 ==> 1
hanoi(n) = |
           \ si n >  1 ==> 2*hanoi(n-1)+1
2. Fibonacci iterado
*/
int main(int argc, char *argv[]) {
	int numero = 20;
	printf("Iterado\n" );
	printf("%d! = %d\n", numero, calcularFactorialIterado(numero));
	printf("Recursivo\n" );
	printf("%d! = %d\n", numero, calcularFactorialRecursivo(numero));
	printf("Fibonacci\n" );
	printf("\n%d = %d\n", numero, calcularFibonacci(numero));
	return 0;
}