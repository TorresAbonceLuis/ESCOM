#include<stdio.h>
#include<math.h>

/*
Un alumno requiere de un programa en lenguaje c que realize el siguiente calculo
             -b+-sqrt(b^2-4ac)
        x1,2=------------------------------
                        2a
la cual resuleve la ecuacion de segundo grado ax^2+bx+c=0 
*/
int main(int argc, char *argv[]){
    double raiz1,raiz2;
    int a,b,c;
    int discriminante;
    printf("Este programa resuelve la ecuacion general:\n");
    printf("    -b+-sqrt(b^2-4ac)\n");
    printf( " x1,2=------------------------------\n");
    printf("                 2a\n");
    printf("para la ecuacion ax^2+bx+c=0\n ");
    printf("Introduzca los valores de a,b,c separados por espacio en blanco\n");
    printf("a b c: ");
    scanf("%d %d %d",&a,&b,&c);
    discriminante=b*b-(4*a*c);
    if(discriminante>=0){
    raiz1=(-b+sqrt(discriminante))/(2*a);
    raiz2=(-b-sqrt(discriminante))/(2*a);
    printf("Las raices son: raiz1=%.5f y raiz2=%f\n",raiz1,raiz2);
    }
    else{
        printf("no se pueden obtener las raices reales");
    }
    
    return 0;
}