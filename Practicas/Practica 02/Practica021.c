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
void cifradoDelMensajeEImpresionCinco(char *ptrMensajeClaro, int numeroDeLetras, int numeroDePosicion){
    int contador;
    for(contador = 0; contador < numeroDeLetras; contador++){
        if( ptrMensajeClaro[contador] == 86 ){
            ptrMensajeClaro[contador] = 63;
        }
        if( ptrMensajeClaro[contador] == 87 ){
            ptrMensajeClaro[contador] = 64;
        }
        if( ptrMensajeClaro[contador] == 88 ){
            ptrMensajeClaro[contador] = 65;
        }
        if( ptrMensajeClaro[contador] == 89 ){
            ptrMensajeClaro[contador] = 66;
        }
        if( ptrMensajeClaro[contador] == 90 ){
            ptrMensajeClaro[contador] = 67;
        }else{
            ptrMensajeClaro[contador] += numeroDePosicion; 
        }
    }
    printf( "Mensaje Cifrado: %s", ptrMensajeClaro);
}
void cifradoDelMensajeEImpresionSiete(char *ptrMensajeClaro, int numeroDeLetras, int numeroDePosicion){
    int contador;
    for(contador = 0; contador < numeroDeLetras; contador++){
        if( ptrMensajeClaro[contador] == 84 ){
            ptrMensajeClaro[contador] = 61;
        }
        if( ptrMensajeClaro[contador] == 85 ){
            ptrMensajeClaro[contador] = 62;
        }
        if( ptrMensajeClaro[contador] == 86 ){
            ptrMensajeClaro[contador] = 63;
        }
        if( ptrMensajeClaro[contador] == 87 ){
            ptrMensajeClaro[contador] = 64;
        }
        if( ptrMensajeClaro[contador] == 88 ){
            ptrMensajeClaro[contador] = 65;
        }
        if( ptrMensajeClaro[contador] == 89 ){
            ptrMensajeClaro[contador] = 66;
        }
        if( ptrMensajeClaro[contador] == 90 ){
            ptrMensajeClaro[contador] = 67;
        }else{
            ptrMensajeClaro[contador] += numeroDePosicion; 
        }
    }
    printf( "Mensaje Cifrado: %s", ptrMensajeClaro);
}
void cifradoDelMensajeEImpresionOnce(char *ptrMensajeClaro, int numeroDeLetras, int numeroDePosicion){
    int contador;
    for(contador = 0; contador < numeroDeLetras; contador++){
        if( ptrMensajeClaro[contador] == 80 ){
            ptrMensajeClaro[contador] = 57;
        }
        if( ptrMensajeClaro[contador] == 81 ){
            ptrMensajeClaro[contador] = 58;
        }
        if( ptrMensajeClaro[contador] == 82 ){
            ptrMensajeClaro[contador] = 59;
        }
        if( ptrMensajeClaro[contador] == 83 ){
            ptrMensajeClaro[contador] = 66;
        }
        if( ptrMensajeClaro[contador] == 84 ){
            ptrMensajeClaro[contador] = 61;
        }
        if( ptrMensajeClaro[contador] == 85 ){
            ptrMensajeClaro[contador] = 62;
        }
        if( ptrMensajeClaro[contador] == 86 ){
            ptrMensajeClaro[contador] = 63;
        }
        if( ptrMensajeClaro[contador] == 87 ){
            ptrMensajeClaro[contador] = 64;
        }
        if( ptrMensajeClaro[contador] == 88 ){
            ptrMensajeClaro[contador] = 65;
        }
        if( ptrMensajeClaro[contador] == 89 ){
            ptrMensajeClaro[contador] = 66;
        }
        if( ptrMensajeClaro[contador] == 90 ){
            ptrMensajeClaro[contador] = 67;
        }else{
            ptrMensajeClaro[contador] += numeroDePosicion; 
        }
    }
    printf( "Mensaje Cifrado: %s", ptrMensajeClaro);
}
int main(int argc,char *argv){
    char mensajeClaro[TAMANIO_PALABRA];
    int numeroDeLetras, contador, numeroDePosicion;
    char *ptrMensajeClaro = &mensajeClaro;
    printf( "\t\t\tBienvenido al programa para cifrar un mensaje\n" );
    printf( "El mensaje debe ser en MAYUSCULA\n" );
    printf( "El mensaje se puede cifrar en 5, 7 y 11 posiciones\n" );
    printf( "Posiciones a cifrar: " );
    scanf( "%d", &numeroDePosicion );
    fflush(stdin);
    if(numeroDePosicion == 5){
        almacenarMensaje( mensajeClaro,&numeroDeLetras );
        cifradoDelMensajeEImpresionCinco( ptrMensajeClaro, numeroDeLetras, numeroDePosicion );
        exit (0);
    }else if(numeroDePosicion == 7 ){
        almacenarMensaje( mensajeClaro,&numeroDeLetras );
        cifradoDelMensajeEImpresionSiete( ptrMensajeClaro, numeroDeLetras, numeroDePosicion );
        exit (0);
    }else if(numeroDePosicion == 11){
        almacenarMensaje( mensajeClaro,&numeroDeLetras );
        cifradoDelMensajeEImpresionOnce( ptrMensajeClaro, numeroDeLetras, numeroDePosicion );
        exit (0);
    }else{
        printf( "Solo se puede cifrar en 5, 7, 11 posiciones" );
    }
}       