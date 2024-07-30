#include <stdio.h>
#include<stdlib.h>

//#define ARCHIVO "hola.txt"
//#define BINARIO_UNO "macaco.jpg"
//#define BINARIO_DOS "macacocp.jpg"

FILE *abrirArchivo(char archivo[80],char modo[10]){
    FILE *fp;
    if((fp = fopen(archivo,modo))==NULL){
        printf("No puedo abrir el archivo %s\n", archivo);
        exit (1);
    }
    return fp;
}

void leerArchivo( FILE *fp){
    char ch;
    do{
        ch = getc (fp);
        printf("%c",ch);
    }while(!feof(fp));
    printf( "\n" );
}
void escribirArchivo(FILE *fp, char mensaje[160]){
    int indice=0;
    while(mensaje[indice]!='\0'){
        putc (mensaje[indice], fp);
        indice++;
    }
}

void cerrarArchivo( FILE *fp){
    if(fp!=NULL){
        fclose(fp);
    }
}

void escribirDeTecladoAArchivo(FILE *fp){
    char ch;
    printf( "Escriba lo que guste y termine con signo $\n" );
    do{
        ch = getchar();
        putc(ch, fp);
    }while (ch != '$');
}

void copiarArchivo(FILE *in, FILE *out){
    char ch;
    while (!feof(in)){
        ch = getc(in);
        if(!feof(in)) putc(ch, out);
    }
}

int main(int argc, char *argv[]){
    FILE *fp;
    FILE *fp1;
    char ArchivoEntrada[30];
    char ArchivoSalida[30];
    printf( "nombre del archivo de entrada: " );
    gets(ArchivoEntrada);
    printf( "nombre del archivo de salida: " );
    gets(ArchivoSalida);
    /*
    fp = abrirArchivo("r");
    if(fp!=NULL){
        leerArchivo(fp);
        cerrarArchivo(fp);
    }
    fp = abrirArchivo(ARCHIVO,"a");
    if(fp!=NULL){
       // escribirArchivo(fp, "Ahora voy a incluir esto\n");
       escribirDeTecladoAArchivo(fp);
        cerrarArchivo(fp);
    }
    fp = abrirArchivo(ARCHIVO,"r");
    if(fp!=NULL){
        leerArchivo(fp);
        cerrarArchivo(fp);
    }
    */
   fp = abrirArchivo(ArchivoEntrada, "rb");
   fp1 = abrirArchivo(ArchivoSalida, "wb");
   if( fp!= NULL && fp1!=NULL ){
       copiarArchivo( fp,fp1 );
       cerrarArchivo(fp);
       cerrarArchivo(fp1);
   }
}