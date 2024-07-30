/*
Algoritmo
Es una secuencia de pasos para resolver un problema y tiene las siguientes caracteristicas:
	1. Preciso: Cada paso debe ser claro y exacto en su construccion para que asi
				determine puntualmente lo que se desea hacer.
	2. Definido: Cada vez que se ejecute el algoritmo on los mismos datos de entrada
				debe generar el mismo resultado
	3. Finito: todo algoritmo debe tener un fin

Como se construye un algoritmo.

	- Utilizar las palabras del idioma nativo (espaniol Mexico) lo debe enterder cualquier persona
	- Se puede emplear un cuasi-codigo pseudo-codigo
	- Los pasos deben ser traducidos a un lenguaje de programacion

Pasos para construir un algoritmo

	1. Iniciar
	2. Conocer los datos que permitan resolver el problema (Entrar al programa, variables)
	3. Realizar procesamiento logico, calculos, resolucion de ecuaciones, etc.
	4. Mostrar los resultados, visualizar, imprimir del problema planteado.
	5. Finalizar

Ejemplo

Construya un algoritmo que calcule y muestre el valor del area de un rectangulo.

Algoritmo
	1. Iniciar
	2. Conocer la base y la altura
	3. Realizar el calculo del area
	4. Imprimir el resultado
	5. Finalizar

Algoritmo (parte 2)

	1. Iniciar
	2. Conocer la base y altura del rectangulo
	3. Realizar el calculo del area del rectangulo
		areaReactangulo <- baseRectangulo * alturaRectangulo
	4. Inprimir el resultado del calculo del area del rectangulo
	5. Finalizar

Algoritmo (parte 3)
	1. Iniciar
	2. baseRectangulo <- ?		// double centimetros 
	   alturaRectangulo <- ?	// double centimetros
	   areaRectangulo <- 0		// double
	3. areaReactangulo <- baseRectangulo * alturaRectangulo // centimetros^2
	4. print baseRectangulo "*" alturaRectangulo "=" areaRetangulo " centimetros^2"
	5. Finalizar
Tarea:
Poner las variables baseRectangulo, alturaRectangulo y areaRectangulo como variables locales del metodo
principal y redefinir los metodos:
	introducirBaseYAlturaDelRectangulo()
	calcularAreaDelRectangulo()
	imprimirResultadosDelCalculo()
*/
#include <stdio.h>


void introducirBaseYAlturaDelRectangulo(double *baseRectangulo, double *alturaRectangulo) {
	printf("Introduzca la base del rectangulo en centimetros: ");
	scanf( "%lf", baseRectangulo );
	printf("Introduzca la altura del rectangulo en centimetros: ");
	scanf( "%lf", alturaRectangulo );
	printf( "1. %.2lf * %.2lf\n", *baseRectangulo, *alturaRectangulo );
}

double calcularAreaDelRectangulo(double baseRectangulo, double alturaRectangulo) {
	printf( "2. %.2f * %.2f\n", baseRectangulo, alturaRectangulo );
	return baseRectangulo * alturaRectangulo;
}

void imprimirResultadosDelCalculo(double baseRectangulo, double alturaRectangulo,double areaRectangulo) {
	printf( "%.2f * %.2f = %.2f centimetros^2", baseRectangulo, alturaRectangulo, areaRectangulo );
}

int main(int argc, char *argv[]) { // 1. Iniciar
	double baseRectangulo, alturaRectangulo, areaRectangulo = 0;
	// 2. Introducir datos de base y altura
	introducirBaseYAlturaDelRectangulo(&baseRectangulo,&alturaRectangulo);
	// 3. Calcular el area del rectangulo
	areaRectangulo = calcularAreaDelRectangulo(baseRectangulo,alturaRectangulo);
	// 4. Mostrar el valor encontrado
	imprimirResultadosDelCalculo(baseRectangulo, alturaRectangulo,areaRectangulo);
	return 0;						// 5. Finalizar
}
