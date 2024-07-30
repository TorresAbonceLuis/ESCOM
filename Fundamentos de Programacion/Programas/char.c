#include <stdio.h>
char otroChar = 'a';
int main(int argc, char *argv[]){
    char UnChar = 'b';
    char resultadoChar;
    resultadoChar = otroChar * UnChar;
    printf("%c * %c = %c\n",otroChar,UnChar,resultadoChar);
    printf("%d * %d = %d\n",otroChar,UnChar,resultadoChar);
    resultadoChar = otroChar / UnChar;
    printf("%c / %c = %c\n",otroChar,UnChar,resultadoChar);
    printf("%d / %d = %d\n",otroChar,UnChar,resultadoChar);
    resultadoChar = otroChar % UnChar;
    printf("%d mod %d = %d\n",otroChar,UnChar,resultadoChar);
    printf("%c mod %c = %c\n",otroChar,UnChar,resultadoChar);
    resultadoChar = otroChar + UnChar;
    printf("%c + %c = %c\n",otroChar,UnChar,resultadoChar);
    printf("%d + %d = %d\n",otroChar,UnChar,resultadoChar);
    resultadoChar = otroChar - UnChar;
    printf("%c - %c = %c\n",otroChar,UnChar,resultadoChar);
    printf("%d - %d = %d\n",otroChar,UnChar,resultadoChar);

    return 0;
}