#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>

struct sigaction capturador_senial;

void capturaSIGINT(int sig) {
  printf("Proceso#:%d Señal SIGINT\n",sig);
}
void capturaSIGILL(int sig) {
  printf("Proceso#:%d Señal SIGILL\n",sig);
}
void capturaSIGTERM(int sig) {
  printf("Proceso#:%d Señal SIGTERM\n",sig);
}
void capturaSIGFPE(int sig) {
  printf("Proceso#:%d Señal SIGFPE\n",sig);
}
void capturaSIGUSR1(int sig) {
  printf("Proceso#:%d Señal SIGUSR1\n",sig);
  exit(-1);
}
int main (void){
  capturador_senial.sa_handler=capturaSIGINT;
  sigaction(SIGINT,&capturador_senial,NULL);
  capturador_senial.sa_handler=capturaSIGILL;
  sigaction(SIGILL,&capturador_senial,NULL);//nose
  capturador_senial.sa_handler=capturaSIGTERM;
  sigaction(SIGTERM,&capturador_senial,NULL);
  capturador_senial.sa_handler=capturaSIGFPE;
  sigaction(SIGFPE,&capturador_senial,NULL);
  capturador_senial.sa_handler=capturaSIGUSR1;
  sigaction(SIGUSR1,&capturador_senial,NULL);

  while(1){
    int pid;
    printf("Esperando las señales\n");
    if(pid=fork()==0){
      while(1){
        sleep(1);
      }
      exit(0);
    }
    sleep(1);
    kill(pid,SIGINT);
    kill(pid,SIGILL);
    kill(pid,SIGTERM);
    kill(pid,SIGFPE);
    kill(pid,SIGUSR1);
    sleep(999);
  }
}
