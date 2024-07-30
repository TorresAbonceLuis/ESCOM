#include <stdio.h>
#include <string.h>

#define TAMANIO_PALABRA 120

void almacenarMensaje(char *mensajeClaro, int *numeroDeLetras){
    int contador;
    printf( "Mensaje a cifrar (maximo %d caracteres): ", TAMANIO_PALABRA );
    gets(mensajeClaro);
    *numeroDeLetras = strlen(mensajeClaro);
    for(contador = 0; contador < *numeroDeLetras; contador++ ){
        if( mensajeClaro[contador] < 65 && mensajeClaro[contador]< 32 && mensajeClaro[contador] > 32 || mensajeClaro[contador] > 90 ){
            printf( "Solo con mayusculas" );
            exit (0);
        }
    }
}
void cifradoDelMensajeEImpresion(char *ptrMensajeClaro, int numeroDeLetras){
    int contador;
    for(contador = 0; contador < numeroDeLetras; contador++){
        if( ptrMensajeClaro[contador] == 88 ){
            ptrMensajeClaro[contador] = 65;
        }
        if( ptrMensajeClaro[contador] == 89 ){
            ptrMensajeClaro[contador] = 66;
        }
        if( ptrMensajeClaro[contador] == 90 ){
            ptrMensajeClaro[contador] = 67;
        }else{
            ptrMensajeClaro[contador] += 3; 
        }
    }
    printf( "Mensaje Cifrado: %s", ptrMensajeClaro);
}

int main(int argc,char *argv){  
    char mensajeClaro[TAMANIO_PALABRA];
    int numeroDeLetras, contador;
    char *ptrMensajeClaro = &mensajeClaro;
    printf( "\t\t\tBienvenido al programa para cifrar un mensaje\n" );
    printf( "El mensaje debe ser en MAYUSCULA\n" );
    almacenarMensaje(mensajeClaro,&numeroDeLetras);
    cifradoDelMensajeEImpresion(ptrMensajeClaro, numeroDeLetras);
    return 0;
}   