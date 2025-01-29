/*
    Autor: Torres Abonce Luis Miguel
*/

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>

struct sigaction capturador_senial;

void capturaSIGUSR1(int sig){
    //modificacion para que no termine con esta señal
}

int main (void){
    int pid,fd,*i,estado,pidP;
    char escribir[20],leer[20];
    fd=open("archivo.txt",O_WRONLY | O_CREAT | O_TRUNC, 0600);
    capturador_senial.sa_handler=capturaSIGUSR1;
    sigaction(SIGUSR1,&capturador_senial,NULL);
    pidP=getpid();
    pid=fork();
    while(1){
        if(pid==0){//Proceso emisor
            printf("Escribir en el archivo: ");
            gets(escribir);//guardar variable
            printf("Escribiendo\n");
            write(fd,escribir,strlen(escribir));//Escribe en el documento
            sleep(2);
            printf("Escrito\n");
            kill(pidP,SIGUSR1);
            pause();
            //esperar la señal
        }else{//proceso Receptor
            pause();//esperamos la señal
            read(fd,leer,strlen(escribir));
            printf("leyendo\n");
            sleep(2);
            printf("leido\n");
            sleep(2);
            system("clear");
            kill(0,SIGUSR1);
        }
    }
    //Proceso Emisor
    return 0;
}