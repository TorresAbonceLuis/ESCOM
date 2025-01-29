#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

struct sigaction capturador_senial;

void capturaSIGUSR1(int sig){
    printf("%d",sig);
    if(sig==0){
        printf("aaaaaa");
    }else{
        printf("zzzzzzz");
    }
}
void capturaSIGTERM (int sig){
    
}

int main (void){
    int pid,fd,i;
    char escribir[20],leer[20];
    fd=open("archivo.txt",O_WRONLY | O_CREAT | O_TRUNC, 0600);
    while(1){
        if(pid=fork()==0){//Proceso receptor 
            printf("\nproceso receptor Esperando señal\n");
            sleep(2);
            //while(1){

                capturador_senial.sa_handler=capturaSIGUSR1;
                sigaction(SIGUSR1,&capturador_senial,NULL);
                if (i==1){
                    break;
                }
            //}
                read(fd,leer,strlen(escribir));
                printf("leyendo\n");
                printf("leido");
                kill(pid,SIGUSR1);
        }//else{
            //sleep(2);
            printf("Escribir en el archivo: ");
            gets(escribir);//guardar variable
            write(fd,escribir,strlen(escribir));
            printf("Escribiendo");
            sleep(3);
            printf("Escrito\n");
            sigaction(SIGUSR1,&capturador_senial,NULL);
            kill(pid,SIGUSR1);
        //}
        break;
    }
    //Proceso Emisor
    return 0;
}