#include<stdio.h>
#include<stdlib.h>
#include<string.h>


void decodificar(char *mensajeCodificado, char *lista);

int buscarLetra(char *lista, char letra){
	int tam=strlen(lista), i; 
	for(i=0;i<tam;i++){
		if(lista[i]==letra)
			return 1;
	}
	return 0;
}

char *listaLetras(char *frase, int tamFrase){
	int i, n=0; char *lista;
	lista=(char*)malloc(100*sizeof(char));
	for(i=0;i<tamFrase;i++){
		if(!buscarLetra(lista, frase[i])){	
			lista[n]=frase[i];
			n++;
			lista[n]='\0';
		}
	}
	return lista;
}

int *numxLetra(char *lista, char *frase){
	int i, j, tamLista=strlen(lista), tamFrase=strlen(frase);
	int *nLista = (int*)malloc(100*sizeof(int));
	for(i=0;i<tamLista; i++){
		nLista[i]=0;
		for(j=0;j<tamFrase; j++){
			if(lista[i]==frase[j])
				nLista[i]++;
		}
	}
	return nLista;
}

void acomodarLista(char *lista, int *nLista, int tamLista){
	char comodin1;
	int comodin2, i, j;
	for(i=0;i<tamLista;i++)
		for(j=0;j<tamLista-1;j++)
			if(nLista[j]>nLista[j+1]){
				comodin1 = lista[j];
				comodin2 = nLista[j];
				lista[j] = lista[j+1];
				nLista[j] = nLista[j+1];
				lista[j+1] = comodin1;
				nLista[j+1] = comodin2;
			}
}

int posicionLetra(char letra, char *lista){
	int i;
	for(i=0;i<strlen(lista);i++)
		if(lista[i]==letra)
			return i;
}

void agregarNumero(char letra, char valor, int pos){
	FILE *Temporal = fopen("Temporal.txt", "w");
	FILE *Arbol = fopen("Arbol.txt", "r");
	int i, tamAux; 
	char auxLetra, aux[100];
	for(i=0;i<pos;i++){
		fgets(aux, 100, Arbol);
		fprintf(Temporal, "%s", aux);
	}
	fscanf(Arbol, "%c", &auxLetra);
	fscanf(Arbol, "%s", aux);
	char valoraux[2];
	valoraux[0]=valor;
	valoraux[1]='\0';
	strcat(aux, valoraux);
	fprintf(Temporal, "%c %s", auxLetra, aux);
	
	fscanf(Arbol, "%c", &auxLetra);
	while( !feof(Arbol) ){
        fprintf(Temporal,"%c", auxLetra);
        fscanf(Arbol, "%c", &auxLetra);
    }
    fclose(Temporal);
    fclose(Arbol);
    remove("Arbol.txt");
    rename("Temporal.txt", "Arbol.txt");
}

void checarLetras(char *conjunto, char valor, char *lista){
	int i;
	for(i=0;i<strlen(conjunto);i++){
		agregarNumero(conjunto[i], valor, posicionLetra(conjunto[i], lista));
	}
}

void unir(char *lista){
	FILE *ListaArch = NULL, *Temporal = NULL;
	ListaArch = fopen("Lista.txt", "r");
	Temporal = fopen("Temporal.txt", "w");
	char conjunto1[100], conjunto2[100], data1;
	int valor1, valor2;
	fscanf(ListaArch, "%s", conjunto1);
	fscanf(ListaArch, "%d", &valor1);
	fscanf(ListaArch, "%s", conjunto2);
	fscanf(ListaArch, "%d", &valor2);
	fprintf(Temporal, "%s%s %d", conjunto1, conjunto2, valor1+valor2);
	fscanf(ListaArch, "%c", &data1);
	while( !feof(ListaArch) ){
        fprintf(Temporal,"%c", data1);
        fscanf(ListaArch, "%c", &data1);
    }
    fclose(ListaArch);
    fclose(Temporal);
    remove("Lista.txt");
    rename("Temporal.txt", "Lista.txt");    
    checarLetras(conjunto1, '0', lista);
	checarLetras(conjunto2, '1', lista);
}

int tamaLista(){
	FILE *ListaArch = fopen("Lista.txt", "r");
	char data1; int contador=0;
	fscanf(ListaArch, "%c", &data1);
	while( !feof(ListaArch) ){
       	if(data1=='\n')
       		contador++;
       	fscanf(ListaArch, "%c", &data1);
   	}
   	return contador--;
}

void ordenarLista(int tamLista){
	char *lista = (char*)malloc(100*sizeof(char));
	char *listaaux = (char*)malloc(100*sizeof(char));
	int i, j, nLista, aux;
	for(j=0;j<tamLista/2;j++){
		FILE *ListaArch = fopen("Lista.txt", "r");
		FILE *Temporal = fopen("Temporal.txt", "w");
		fscanf(ListaArch, "%s", lista);
		fscanf(ListaArch, "%d", &nLista);		
		for(i=0;i<tamLista-1;i++){
			fscanf(ListaArch, "%s", listaaux);
			fscanf(ListaArch, "%d", &aux);
			if(nLista>aux){
				fprintf(Temporal, "%s %d\n", listaaux, aux);
			}
			else{
				fprintf(Temporal, "%s %d\n", lista, nLista);
				strcpy(lista, listaaux);
				nLista=aux;
			}
		}
		fscanf(ListaArch, "%s", listaaux);
		fscanf(ListaArch, "%d", &aux);
		if(nLista>aux){
			fprintf(Temporal, "%s %d\n", lista, nLista);
			fprintf(Temporal, "%s %d\n", listaaux, aux);
			
		}else{
			fprintf(Temporal, "%s %d\n", listaaux, aux);
			fprintf(Temporal, "%s %d\n", lista, nLista);	
		}
		fclose(ListaArch);
		fclose(Temporal);
		remove("Lista.txt");
		rename("Temporal.txt", "Lista.txt");		
	}	
}

char *obtenerCodigo(char letra){
	FILE *Arbol=fopen("Arbol.txt", "r");
	char codigo[20], letraCodigo;
	while(!feof(Arbol)){
		fscanf(Arbol, "%c", &letraCodigo);
		if(letraCodigo==letra){
			fscanf(Arbol, "%s", codigo);
			fclose(Arbol);
			return codigo;
		}
	}
}

char *girarCodigo(char letra){
	int i;
	char *Codigo = obtenerCodigo(letra);
	int tamCodigo = strlen(Codigo);
	char aux[20];
	for(i=0;i<tamCodigo;i++)
		aux[i]=Codigo[tamCodigo-i-1];
	aux[tamCodigo]='\0';
	return aux;
}

void girarCodigoArbol(char *lista){
	FILE *Temporal=fopen("Temporal.txt", "w");
	int i;
	for(i=0;i<strlen(lista);i++){
		fprintf(Temporal, "%c %s\n", lista[i], girarCodigo(lista[i]));
	}
	fclose(Temporal);
	remove("Arbol.txt");
	rename("Temporal.txt", "Arbol.txt");
}

void cambiarCaracter(char caracter){
	FILE *Arbol=fopen("Arbol.txt", "r");
	FILE *Temporal=fopen("Temporal.txt", "w");
	char c;
	fscanf(Arbol, "%c", &c);
	while(!feof(Arbol)){
		if(c!=caracter)
			fprintf(Temporal, "%c", c);
		fscanf(Arbol, "%c", &c);
	}
	fclose(Arbol);
	fclose(Temporal);
	remove("Arbol.txt");
	rename("Temporal.txt", "Arbol.txt");
}



char *codificar(char *frase){
	FILE *Arbol = NULL;
	FILE *ListaArch = NULL;
	Arbol = fopen("Arbol.txt", "w");
	ListaArch = fopen("Lista.txt", "w");
	int i, tamLista, tamMensaje=0, tamCodCarac=0;
	char menCodificado[800];
	for(i=0;i<strlen(frase);i++)
		if(frase[i]==' ')
			frase[i]='$';
	char *lista = listaLetras(frase, strlen(frase));
	tamLista=strlen(lista);
	int *nLista = numxLetra(lista, frase);
	acomodarLista(lista, nLista, tamLista);
	for(i=0; i<strlen(lista); i++){
		fprintf(ListaArch, "\n%c %d", lista[i], nLista[i]);
		fprintf(Arbol, "%c #\n", lista[i]);
	}
	fclose(Arbol);
	fclose(ListaArch);
	for(i=0;i<strlen(lista)-1;i++){
		unir(lista);
		tamLista--;
		ordenarLista(tamLista);	
	}
	remove("Lista.txt");
	cambiarCaracter('#');
	girarCodigoArbol(lista);
	printf("\n\nCaracter\tFrecuencia\tCodigo\t\tbits");
	for(i=0;i<strlen(lista);i++){
		printf("\n%-12c\t%-12d\t%-12s\t%dx%d=%d", lista[i], nLista[i], obtenerCodigo(lista[i]), strlen(obtenerCodigo(lista[i])), nLista[i], nLista[i]*strlen(obtenerCodigo(lista[i])));
		tamMensaje+=nLista[i]*(strlen(obtenerCodigo(lista[i])));
		tamCodCarac+=strlen(obtenerCodigo(lista[i]));
	}
	printf("\n\nCodificacion de caracteres en ASCII: %dx8=%d bits", strlen(lista), strlen(lista)*8);
	printf("\nCodificacion de caracteres: %d bits", tamCodCarac);
	printf("\nTotal de bits requeridos: %d bits", tamMensaje+strlen(lista)*8+tamCodCarac);
	printf("\n\nMensaje Codificado: \n");
	strcpy(menCodificado, obtenerCodigo(frase[0]));
	for(i=1;i<strlen(frase);i++){
		strcat(menCodificado, obtenerCodigo(frase[i]));
	}
	printf("\n%s", menCodificado);
	decodificar(menCodificado, lista);
	return menCodificado;
}

char letraCodigo(char *codigoArbol, char *lista){
	int i;
	for(i=0;i<strlen(lista);i++){
		if(!strcmp(codigoArbol, obtenerCodigo(lista[i])))
			return lista[i];
	}
	return '*';
}

void decodificar(char *mensajeCodificado, char *lista){
	char codigo[20], c;
	int i, aux=0, cont=1;
	printf("\n\nMensaje: \n");
	codigo[0]=mensajeCodificado[0];
	codigo[1]='\0';
	for(i=1;i<=strlen(mensajeCodificado);i++){
		
		c = letraCodigo(codigo, lista);
		if(c=='*'){
			codigo[cont]=mensajeCodificado[i];
			codigo[cont+1]='\0';	
			cont++;
		}else{
			if(c=='$')
				printf(" ");
			else
				printf("%c", c);
			codigo[0]=mensajeCodificado[i];
			codigo[1]='\0';
			cont=1;
		}		
	}
}

int main(){
	char frase[800], *menCodificado;
	printf("Inserta la frase: ");
	gets(frase);
	codificar(frase);
	printf("\n\n\n");
	system("pause");
	return 0;
}
