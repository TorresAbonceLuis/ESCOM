#include <stdio.h>

#define MESES 6

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
void leerInformacionDelTrabajador(float ingresoMensual[], char claveDeEmpleado[]) {
	int contador;
	// 1. Lectura de informacion
	printf( "Introduzca el sueldo mensual del trabajador\n" );
	for( contador=0; contador<MESES; contador++ ) {
		printf( " mes(%d): ", (contador+1) );
		scanf( "%f", &ingresoMensual[contador] );
	}
	printf( "Introduzca clave del trabajador: " );
	gets(claveDeEmpleado);
	gets(claveDeEmpleado);
}

void realizarCalculosDelTrabajador(float *ingresoTotal,float ingresoMensual[],float *promedioMensual) {
	int contador;
	// 2. Calculos solicitados
	for( contador=0; contador<MESES; contador++ ) {
		*ingresoTotal += ingresoMensual[contador];
	}
	*promedioMensual = *ingresoTotal / (float)MESES;
}

void imprimirInformacion(char claveDeEmpleado[], float ingresoMensual[], float ingresoTotal,
	float promedioMensual ) {
	int contador;
	printf(" Clave del empleado:\t %s\n", claveDeEmpleado);
	printf(" Ingreso mensual\n" );
	for( contador=0; contador<MESES; contador++ ) {
		printf( "\tmes %d $ %.2f M.N.\n", (contador+1), ingresoMensual[contador] );
	}
	printf( " Ingreso total:   \t $ %.2f M.N.\n", ingresoTotal );
	printf( " Promedio mensual:\t $ %.2f M.N.\n", promedioMensual );
}

int main(int argc, char *argv[]){
    float ingresoMensual[MESES];
    float ingresoTotal=0.0;
    char claveDeEmpleado[6];
    float promedioMensual=0.0;
    // Haciendo el proceso para 5 trabajadores empleando u ciclo
    int contador=1;
    for(contador=1; contador<5;contador++){
    //do{
        /* code */
    //while (contador<=5){
        printf("Trabajador No. %d\n",contador);
    // 1. Lectura de informacion
        leerInformacionDelTrabajador(ingresoMensual,claveDeEmpleado);
   // printf("Introduzca el sueldo mensual del trabajado\n");
   // for(contador=0; contador<MESES;contador++){
  //      printf("mes(%d): ",(contador+1) );
  //      scanf("%f",&ingresoMensual[contador]);
  //  }
  //  printf("Introduzca la clave del trabajador: ");
  //  gets(claveDeEmpleado);
  //  gets(claveDeEmpleado);
    // 2. Calculos solicitados
        realizarCalculosDelTrabajador(&ingresoTotal,ingresoMensual,&promedioMensual);
  //  for(contador=0; contador<MESES;contador++){
  //      ingresoTotal+=ingresoMensual[contador];
  //  }
  //  promedioMensual=ingresoTotal/(float)MESES;
    // 3. Salida a pantalla
        imprimirInformacion(claveDeEmpleado,ingresoMensual,ingresoTotal,promedioMensual );
  //  printf("Clave del empleado:\t %s\n",claveDeEmpleado);
   // printf("Ingreso mensual\n");
   // for(contador=0; contador<MESES;contador++){
   //     printf("mes %d $ %.2f M.N.\n",(contador+1),ingresoMensual[contador]);
  //  }
   // printf("Ingreso total:$\t %.2f M.N.\n",ingresoTotal);
   // printf("Promedio mensual:$\t %.2f M.N.\n",promedioMensual);
  //contador++;
 // }
    // } while (contador++<=5);
    }
  return 0;
  
}