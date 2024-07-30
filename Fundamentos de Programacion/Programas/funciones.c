#include <stdio.h>
#include <string.h>

#define MAX_NOMBRE 80

struct Trabajador {
    char nombre[MAX_NOMBRE];
    double salario;
};
// paso por referencia 
void cambiarValoresDeTrabajador(struct Trabajador *alguien){
    strcpy(alguien->nombre , "Luis Torres");
    alguien->salario = 2000;
}

// se crea una copia de jose y se trabaja con la copia dentro de la funcion 
void cambiarValorDeJosePasoPorValor(int jose){
    printf( "dentro del metodo cambiarValorDejose()\n %d\n",jose );
    jose = 1000;
    printf( "dentro de cambiarValorDejose()\n %d\n",jose );
}

void cambiarValorDeJosePorReferencia(int *pepe){
    printf( "dentro del metodo cambiarValorDejose()\n %d\n",*pepe );
    *pepe = 1000;
    printf( "dentro de cambiarValorDejose()\n %d\n",*pepe );
}
int main (int argc, char *argv){
    struct Trabajador alguien;
    int jose = 0;
    int *pepe = &jose;
    printf( "jose %d\n",jose );
    *pepe = 10;
    printf( "jose %d\n",jose );
    cambiarValorDeJosePasoPorValor(jose);// pasando por valor
    printf( "regreso al main \njose %d\n",jose );
    cambiarValorDeJosePorReferencia(&jose);// pasando por valor
    printf( "regreso al main \njose %d\n",jose );

    printf( "Trabajador \n nombre  %s\n",alguien.nombre );
    printf( "Salario  %f\n",alguien.salario );

    cambiarValoresDeTrabajador(&alguien);

    printf( "Trabajador \n nombre  %s\n",alguien.nombre );
    printf( "Salario  %f\n",alguien.salario );
    
    return 0;
}