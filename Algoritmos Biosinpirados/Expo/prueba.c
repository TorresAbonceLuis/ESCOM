#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;

#define MAX_BITS 8

int validarCadena(char *cadena);
void mostrarMenu();
int abrirArchivo(const char *nombreArchivo, char *contenido);
void imprimirArchivo(char *contenido);
int convertirCadena(char *cadena);

int main() {
int opcion;
char contenido[MAX_BITS + 1] = {0};
const char *nombreArchivo = &quot;escom.txt&quot;;

do {
mostrarMenu();
printf(&quot;Selecciona una opcion: &quot;);
if (scanf(&quot;%d&quot;, &amp;opcion) != 1) {
printf(&quot;Error: Entrada no válida. Inténtalo de nuevo.\n&quot;);
while (getchar() != &#39;\n&#39;);
continue;
}
getchar();

switch (opcion) {
case 1: {
printf(&quot;Intentando abrir el archivo...\n&quot;);
if (abrirArchivo(nombreArchivo, contenido)) {
if (validarCadena(contenido)) {
printf(&quot;Archivo abierto correctamente.\n&quot;);
} else {
printf(&quot;El contenido del archivo no es binario.\n&quot;);
contenido[0] = &#39;\0&#39;;
}
} else {
printf(&quot;Error al abrir el archivo.\n&quot;);
}
break;
}
case 2: {
if (strlen(contenido) &gt; 0) {
imprimirArchivo(contenido);
} else {
printf(&quot;No hay contenido para mostrar. Abre un archivo primero.\n&quot;);
}
break;
}
case 3: {
if (strlen(contenido) &gt; 0 &amp;&amp; validarCadena(contenido)) {
printf(&quot;Cadena de bits del archivo \&quot;%s\&quot;\n&quot;, nombreArchivo);
printf(&quot;%s\n&quot;, contenido);
printf(&quot;Valor de la cadena en bits: %d\n&quot;, convertirCadena(contenido));
} else {

printf(&quot;No hay una cadena válida para convertir. Abre un archivo válido primero.\n&quot;);
}
break;
}
case 4: {
printf(&quot;Hasta pronto.\n&quot;);
break;
}
default:
printf(&quot;Opción no válida. Intenta nuevamente.\n&quot;);
}
} while (opcion != 4);

return 0;
}

void mostrarMenu() {
printf(&quot;\n*ALONDRA MARGARITA DE LA O BERNAL*\n&quot;);
printf(&quot;MENU CONVERSION DE BIT A DECIMAL\n&quot;);
printf(&quot;1. Abrir archivo (.txt)\n&quot;);
printf(&quot;2. Imprimir en pantalla contenido de archivo .txt\n&quot;);
printf(&quot;3. Convertir bit a decimal\n&quot;);
printf(&quot;4. Salir\n&quot;);
}

int abrirArchivo(const char *nombreArchivo, char *contenido) {
FILE *archivo = fopen(nombreArchivo, &quot;r&quot;);
if (archivo == NULL) {

perror(&quot;Error al abrir el archivo&quot;);
return 0;
}

if (fgets(contenido, MAX_BITS + 1, archivo) == NULL) {
fclose(archivo);
printf(&quot;Error: no se pudo leer contenido del archivo.\n&quot;);
return 0;
}