//Torres Abonce Luis Miguel
#include <iostream>

using namespace std;
typedef int entero;

struct estructura
{
	char pollo[15];
} gato;

class objeto
{
	public:
		entero variableX;
		int valor;
};

int main(void)
{
	cout << "Ingrese su nombre";
	cin.getline(gato.pollo,15,'\n');
	cout << gato.pollo;
	
	objeto mi_objeto[10];
	objeto un_objeto;
	mi_objeto.valor = 5;
	un_objeto.valor = 3;
	un_objeto.variableX = 17;

	cout << mi_objeto.valor;
	cout << endl << un_objeto.valor;
	cout << endl << un_objeto.variableX;
	
	return 0;
}
