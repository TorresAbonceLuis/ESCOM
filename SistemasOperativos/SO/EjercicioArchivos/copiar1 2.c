#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<unistd.h>
#include<fcntl.h>
#define BLOQUE 4096
void error_fatal(int pid,int argc,int origen, int destino){
    if (argc==1){//si solo recibe un argumento no hay origen ni destino
       printf("No se ha especificado archivo origen ni destino\n");//Error
    }
    else if(argc==2){//si solo recibe un argumento no hay destino
        printf("No se ha especificado archivo destino\n");//Error
    }
    else if (origen==-1){//no existe el archivo o no lo pudo abrir
        printf("El archivo origen no existe o no se puede abrir\n");//Error
    }
    else if (destino==-1){//no existe el archivo o no lo pudo abrir
        printf("El archivo destino no existe o no se puede abrir\n");
    }
    exit(1);
}

int main(int argc,char *argv[]){
    char buffer[BLOQUE];
    int pid,origen,destino,leido=BLOQUE,escrito;
    if(pid=fork()==0){
        origen=open(argv[1],O_RDONLY);//abrir documento de origen
        destino=open(argv[2],O_WRONLY | O_CREAT | O_TRUNC, 0600);//abrir documento de destino
        error_fatal(pid,argc,origen,destino);//Error
        printf("Copiando el archivo \n");
        while(leido==BLOQUE){//se copia por bloques
            leido=read(origen,buffer,BLOQUE);//se guarda en el buffer
            escrito=write(destino,buffer,leido);//se escribe lo del buffer
        }
        sleep(1);
        printf("Se ha terminado de copiar todo \n");
        close(origen);//Se cierran archivos
        close(destino);
    }
    sleep(2);
    return 0;
}