#ifndef MENU_H
#define MENU_H

#include <stdio.h>
#include <stdlib.h>
#include "milibreriaio.h"

void limpiarBufferDeTeclado() {
	char ch;
	while( (ch=getchar())!='\n' && ch!=EOF);
}

void menu(){
    FILE *fp;
    FILE *fp1;
    long enteroL;
    float flotante;
    double dobleFlotante;
    int opcion = 0, entero;
    char archivo[80], mensaje[160], copia[80],caracter;
    while(opcion!=16){
        printf( "Menu de aplicaciones para archivo\n" );
        printf( "1.Leer un archivo\n" );
        printf( "2.Escribir en archivo\n" );
        printf( "3.Sobreescribir un archivo\n" );
        printf( "4.Copiar un archivo\n" );
        printf( "5.Escribir desde el teclado\n" );
        printf( "6.Escribir un entero al archivo\n" );
        printf( "7.Leer entero del archivo\n");
        printf( "8.Escribir un caracter al archivo\n" );
        printf( "9.Leer un caracter del archivo\n" );
        printf( "10.Escribir un entero largo al archivo\n" );
        printf( "11.Leer entero largo del archivo\n");
        printf( "12.Escribir un flotante al archivo\n" );
        printf( "13.Leer un flotante del archivo\n");
        printf( "14.Escribir un flotante doble al archivo\n" );
        printf( "15.Leer un flotante doble del archivo\n");
        printf( "16.Salir del programa\n" );
        printf( "Seleccione su opcion:" );
        scanf( "%d",&opcion );
        switch (opcion){
        case 1:
            printf( "Nombre del archivo a leer: " );
            limpiarBufferDeTeclado();
            gets(archivo);
            fp = abrirArchivo(archivo,"r");
            if( fp!=NULL ) {
		        leerArchivo( fp );
		        cerraArchivo( fp );
		    }
            break;
        case 2:
            printf( "Nombre del archivo a escribir: " );
            limpiarBufferDeTeclado();
            gets(archivo);
            fp = abrirArchivo(archivo,"a");
            printf( "Mensaje a escribir en el archivo: " );
            gets(mensaje);
            if( fp!=NULL ) {
		        escribirArchivo(fp,mensaje);
		        cerraArchivo( fp );
		    }
            break;
        case 3:
            printf( "Nombre del archivo a sobreescribir: " );
            limpiarBufferDeTeclado();
            gets(archivo);
            fp = abrirArchivo(archivo,"w");
            printf( "Mensaje a escribir en el archivo: " );
            gets(mensaje);
            if( fp!=NULL ) {
		        escribirArchivo(fp,mensaje);
		        cerraArchivo( fp );
		    }
            break;
        case 4:
            printf( "Archivo a copiar: " );
            limpiarBufferDeTeclado();
            gets(archivo);
            printf("Nombre de la copia: ");
            gets(copia);
            fp = abrirArchivo(archivo,"rb" );
            fp1 = abrirArchivo(copia,"wb" );
            if( fp!=NULL && fp1!=NULL ) {
		        copiarArchivo(fp,archivo,fp1,copia);
		        cerraArchivo(fp);
		        cerraArchivo(fp1);
		    }
        break;
        case 5:
            printf( "Nombre del archivo:" );
            limpiarBufferDeTeclado();
            gets(archivo);
            fp = abrirArchivo(archivo,"at");
            escribirDeTecladoAArchivo(fp,'$');
            cerraArchivo(fp);
        break;
        case 6:
            printf( "Nombre del archivo:" );
            limpiarBufferDeTeclado();
            gets(archivo);
            printf( "Entero a mandar:" );
            scanf( "%d",&entero);
            fp = abrirArchivo(archivo,"wb");
            escribirEnteroAArchivo(fp,entero);
            cerraArchivo(fp);
        break;
        case 7:
            printf( "Nombre del archivo:" );
            limpiarBufferDeTeclado();
            gets(archivo);
            fp= abrirArchivo(archivo,"rb");
            printf( "%d\n",leerEnteroDeArchivo(fp));
            cerraArchivo(fp);
        break;
        case 8:
            printf( "Nombre del archivo:" );
            limpiarBufferDeTeclado();
            gets(archivo);
            printf( "Caracter a mandar:" );
            scanf( "%c",&caracter );
            fp = abrirArchivo(archivo,"wb");
            escribirCaracterAArchivo(fp,caracter);
            cerraArchivo(fp);
        break;
        case 9:
            printf( "Nombre del archivo:" );
            limpiarBufferDeTeclado();
            gets(archivo);
            fp= abrirArchivo(archivo,"rb");
            printf("%c\n",leerCaracterDeArchivo(fp));
            cerraArchivo(fp);
        break;
        case 10:
            printf( "Nombre del archivo:" );
            limpiarBufferDeTeclado();
            gets(archivo);
            printf( "Entero largo a mandar:" );
            scanf( "%ld",&enteroL);
            fp = abrirArchivo(archivo,"wb");
            escribirEnteroLargoAArchivo(fp,enteroL);
            cerraArchivo(fp);
        break;
        case 11:
            printf( "Nombre del archivo:" );
            limpiarBufferDeTeclado();
            gets(archivo);
            fp = abrirArchivo(archivo,"rb");
            printf( "%ld\n",leerEnteroLargoDeArchivo(fp));
            cerraArchivo(fp);
        break;
        case 12:
            printf( "Nombre del archivo:" );
            limpiarBufferDeTeclado();
            gets(archivo);
            printf( "Flotante a mandar:" );
            scanf( "%f",&flotante);
            fp = abrirArchivo(archivo,"wb");
            escribirFlotanteAArchivo(fp,flotante);
            cerraArchivo(fp);
        break;
        case 13:
            printf( "Nombre del archivo:" );
            limpiarBufferDeTeclado();
            gets(archivo);
            fp = abrirArchivo(archivo,"rb");
            printf( "%f\n",leerFlotanteDeArchivo(fp));
            cerraArchivo(fp);
        break;
        case 14:
            printf( "Nombre del archivo:" );
            limpiarBufferDeTeclado();
            gets(archivo);
            printf( "Flotante a mandar:" );
            scanf( "%lf",&dobleFlotante);
            fp = abrirArchivo(archivo,"wb");
            escribirFlotanteDobleAArchivo(fp,dobleFlotante);
            cerraArchivo(fp);
        break;
        case 15:
            printf( "Nombre del archivo:" );
            limpiarBufferDeTeclado();
            gets(archivo);
            fp = abrirArchivo(archivo,"rb");
            printf( "%lf\n",leerFlotanteDobleAArchivo(fp));
            cerraArchivo(fp);
        break;
        default:
            printf(" eliga una opcion.\n");
            break;
        }
    }
}
#endif 