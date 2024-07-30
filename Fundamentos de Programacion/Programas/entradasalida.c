#include<stdio.h>

int main(int argc, char *argv[]){
    char ca= ' ';
    char cadena[80];
    printf("introduzca un caracter: ");
    ca = getchar();
    printf("su caracter es :");
    putchar(ca);
    printf("\nIntroduzca una cadena de caracteres: ");
    scanf("%s",cadena);
    printf("Su cadena es: %s\n",cadena);
    printf("\nIntroduzca otra cadena de caracteres: ");
    gets(cadena);
    gets(cadena);
    printf("su otra cadena es :");
    puts(cadena);
    printf("\n");
    return 0;
}