#include<stdio.h>
#include<stdlib.h>
/*
1.2.4 Sentencias de control 
Las sentencias de control son (bloques de codigo {})

1. if
2. if-else
3. if-else-if 
4. switch-case-brak-default

1,2 y 3 trabajan evaluando sentencias a verdadero(logica positiva), pudiendo
evaluar a logica negativa

4. se puede evaluar con enteros o caracteres

Las sentencias de control se utilizan para cambiar el flujo de ejecucion de un 
programa
*/
int main(int argc, char *argv[]){
    int numero;
    //Primer sentencia
    if(argc<2){
        printf("Olvido incluir al menos un argumento con el nombre del programa\n");
    }
    //segunda forma de control 
    if (argc>=2){
        printf("Tu segundo argumento es: %s\n",argv[1]);
    }
    else{
        printf("Olvido incluir al menos un argumento con el nombre del programa\n");
    }
    //Tercera forma de control 
    if (argc>=2){
        printf("Tu segundo argumento es: %s\n",argv[1]);
    }
    else
    if(argc>2 && argc<4){
        printf("Tu segundo argumento es: %s\n",argv[1]);
        printf("Tu tercer argumento es: %s\n",argv[2]);
    }
    else{
        printf("Olvido incluir al menos un argumento con el nombre del programa\n");
    }
    if(argc>=4){
        //cuarta forma de control evalua a caracter
        switch (argv[3][0]){
         case 'a':
            printf("Primer caracter de tu tercer argumento es: %c\n",argv[3][0]);
            break;
          case 'e':
          case 'i':
            printf("Primer caracter de tu tercer argumento es: %c\n",argv[3][0]);
            break;
          case 'o':
          case 'u':
            printf("Primer caracter de tu tercer argumento es: %c\n",argv[3][0]);
            break;
     default:
           printf("El primer caracter de tu tercer argumento no tiene vocal\n");
        break;
      }
    }
    if(argc==5){
        //cuarta froma de control evalua a entero
        numero=atoi(argv[3]);
      switch (numero){
        case 100:
            printf("Introdujo un: %d\n",numero);
            break;
        case 10:
        case 20:
            printf("Introdujo un: %d\n",numero);
            break;
        case -10:
        case -20:
            printf("Introdujo un: %d\n",numero);
            break;
        default:
            printf("No introdujo un numero 100, 10, 20,-10,-20");
      }
    }
    return 0;
}