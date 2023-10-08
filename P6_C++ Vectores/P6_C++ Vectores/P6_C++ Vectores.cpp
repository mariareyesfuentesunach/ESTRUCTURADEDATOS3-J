//Maria Jose Reyes Fuentes 3-J LSC
//Practica 06 - Vectores

#include <iostream>
#include <vector>

using namespace std;
int main() {

	//Declara un vector de cadenas
	vector<string> aves = { "Loro gris", "Paloma de diamante", "Coctel" };
	cout << "Los Valores del vector angtes de insertar:\n";

	//Itera sobre el vector para imprimir los valores
	for (int i = 0; i < aves.size(); ++i) {
		cout << aves[i] << " ";
	}

	cout << "\n";
	//Agrega tres valores al final del vector utilizando push_back()
	aves.push_back("Mayna");
	aves.push_back("Periquitos");
	aves.push_back("Cacatua");
	cout << "Los valores del vector despues de insertar:\n";

	//Itera sobre el vector para imprimir los valores
	for (int i = 0; i < aves.size(); ++i) {
		cout << aves[i] << " ";
	}

	cout << "\n";

	return 0;
}