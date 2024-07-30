#include <stdio.h>

#define MESES 6
#define TRABAJADORES 6
/*
Crear un programa que lea 6 meses de sueldo de un trabajador(no gana lo mismo cada mes),su
clave de empleadco y calcule su ingreso promedio mensual, e imprima como salida todo lo an-
terior y su ingreso total (utilice arreglos)
1.3 Programacion y diseno estructurado (paradigma )
    Modularidad de nuestros programas 
    1. TOP-DOWN
    2. DOWN-TOP
    Creacion de procesos, metodos o funciones
*/
// Este modulo lee la informacion del trabajdor
void leerInformacionDelTrabajador(float ingresoMensual[TRABAJADORES][MESES], 
    char claveDeEmpleado[TRABAJADORES][MESES],int numeroTrabajdor) {
	int contador;
	// 1. Lectura de informacion
	printf( "Introduzca el sueldo mensual del trabajador\n" );
	for( contador=0; contador<MESES; contador++ ) {
		printf( " mes(%d): ", (contador+1) );
		scanf( "%f", &ingresoMensual[TRABAJADORES][contador] );
	}
	printf( "Introduzca clave del trabajador: " );
	gets(claveDeEmpleado[numeroTrabajdor]);
	gets(claveDeEmpleado[numeroTrabajdor]);
}

void realizarCalculosDelTrabajador(float ingresoTotal[],float ingresoMensual[TRABAJADORES][MESES],
    float promedioMensual[],int numeroTrabajador) {
	int contador;
	// 2. Calculos solicitados
	for( contador=0; contador<MESES; contador++ ) {
		ingresoTotal [numeroTrabajador]+= ingresoMensual[numeroTrabajador][contador];
	}
	promedioMensual[numeroTrabajador] = ingresoTotal[numeroTrabajador] / (float)MESES;
}

void imprimirInformacion(char claveDeEmpleado[TRABAJADORES][6], float ingresoMensual[TRABAJADORES][MESES], 
    float ingresoTotal[],float promedioMensual[TRABAJADORES]) {
	int contador;
	printf(" Clave del empleado:\t %s\n", claveDeEmpleado);
	printf(" Ingreso mensual\n" );
	int numeroTrabajador;
    for(numeroTrabajador=0;numeroTrabajador<TRABAJADORES;numeroTrabajador++){
         for( contador=0; contador<MESES; contador++ ) {
		    printf( "\tmes %d $ %.2f M.N.\n", (contador+1), ingresoMensual[numeroTrabajador][contador] );
	    }
	    printf( " Ingreso total:   \t $ %.2f M.N.\n", ingresoTotal);
	    printf( " Promedio mensual:\t $ %.2f M.N.\n", promedioMensual);
    }
}

int main(int argc, char *argv[]){
    float ingresoMensual[TRABAJADORES][MESES];
    float ingresoTotal[TRABAJADORES];
    char claveDeEmpleado[TRABAJADORES][6];
    float promedioMensual[TRABAJADORES];
    // Haciendo el proceso para 5 trabajadores empleando u ciclo
    int contador=1;
    int numeroTrabajador;
    for(contador=0; contador<TRABAJADORES;contador++){
    //do{
        /* code */
    //while (contador<=5){
        printf("Trabajador No. %d\n",contador);
    // 1. Lectura de informacion
        leerInformacionDelTrabajador(ingresoMensual,claveDeEmpleado,numeroTrabajador);
   // printf("Introduzca el sueldo mensual del trabajado\n");
   // for(contador=0; contador<MESES;contador++){
  //      printf("mes(%d): ",(contador+1) );
  //      scanf("%f",&ingresoMensual[contador]);
  //  }
  //  printf("Introduzca la clave del trabajador: ");
  //  gets(claveDeEmpleado);
  //  gets(claveDeEmpleado);
    // 2. Calculos solicitados
        realizarCalculosDelTrabajador(ingresoTotal,ingresoMensual,promedioMensual,contador);
  //  for(contador=0; contador<MESES;contador++){
  //      ingresoTotal+=ingresoMensual[contador];
  //  }
  //  promedioMensual=ingresoTotal/(float)MESES;
    // 3. Salida a pantalla
        
  //  printf("Clave del empleado:\t %s\n",claveDeEmpleado);
   // printf("Ingreso mensual\n");
   // for(contador=0; contador<MESES;contador++){
   //     printf("mes %d $ %.2f M.N.\n",(contador+1),ingresoMensual[contador]);
  //  }
   // printf("Ingreso total:$\t %.2f M.N.\n",ingresoTotal);
   // printf("Promedio mensual:$\t %.2f M.N.\n",promedioMensual);
  //contador++;
  }
        imprimirInformacion(claveDeEmpleado,ingresoMensual,ingresoTotal,promedioMensual);
     //} while (contador++<=5);
  return 0;
}