//Torres Abonce Luis Miguel
#include <iostream>
#include <string.h>

using namespace std;
typedef int entero;

struct estructura
{
	int id;
	char nombre[15];
	char equipo[15];
} jugador[50];

class objeto
{
	public:
		//entero variableX;
		int id;
		char nombre[15];
} equipo[10];

int main(void)
{
	/*objeto mi_objeto;
	mi_objeto.valor = 5;
	un_objeto.valor = 3;
	un_objeto.variableX = 17;
	
	cout << mi_objeto.valor;
	cout << endl << un_objeto.valor;
	cout << endl << un_objeto.variableX;*/
	int opc, j=0, e=0, acc=0;
	while(acc!=3)
	{
		cout << "Seleccione el tipo de registro que desea hacer" << endl;
		cout << "Jugador -> 1" << endl;
		cout << "equipo -> 2" << endl;
		cout << "terminar registros -> 3" << endl;
		cin >> opc;
		switch(opc)
		{
			case 1: 
				if(j<50)
				{
					cout << "Ingrese su nombre: ";
					cin >> jugador[j].nombre;
					cout << "Ingrese el nombre de su equipo:" ;
					cin >> jugador[j].equipo;
					jugador[j].id = j+1;
					j+=1;	
				}
				else
				{
					cout << "Ya no hay cupo para mas jugadores" ;
				}
			break;
		
			case 2:
				if(e<10)
				{	
					//memset(equipo[e].nombre, '\0', sizeof(equipo[e].nombre));//limpia la cadena de caracteres
					cout << "Ingrese el nombre del equipo:" ;
					//getline(cin, equipo[e].nombre);
					//cin.ignore();//Limpia el buffer
					fflush(stdin);// otra forma de limpiar el buffer
					cin.getline(equipo[e].nombre,20,'\n');
					cout << equipo[e].nombre << endl ; 
					equipo[e].id = e+1;
					e=e+1;
				}
				else
				{
					cout << "Ya no hay espacio para mas equipos";
				}
			break;
		
			case 3:
				acc= opc;
			break;
		
			default:
				cout << "Seleccione una opccion valida";
			break;
		}
				
	}
	cout << "Impresion de los jugadores ingresado"<<endl;
	for(int i=0; i<j; i++)
	{
		cout << jugador[i].id << endl;
		cout << jugador[i].nombre << endl;
		cout << jugador[i].equipo << endl;
		cout << endl;
	}
	
	cout << "Impresion de los equipos ingresado" <<endl;
	for(int i=0; i<e; i++)
	{
		cout << equipo[i].id << endl;
		cout << equipo[i].nombre << endl;
		cout << endl; 
	}

	return 0;
}
