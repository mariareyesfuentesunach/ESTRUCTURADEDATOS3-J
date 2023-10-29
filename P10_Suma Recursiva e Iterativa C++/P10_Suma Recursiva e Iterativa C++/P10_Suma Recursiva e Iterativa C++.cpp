// Maria Jose Reyes Fuentes 3-J LSC
// Practica 10 -Suma Recursiva e Iterativa C++.cpp 

#include <iostream>
using namespace std;

int SumaIterativa(int n) {
    int suma = 0;
    while (n > 9) {
        suma += n % 10;
        n /= 10;
    }
    suma += n;
    return suma;
}

int SumaRecursiva(int n) {
    if (n <= 9)
        return n;
    else
        return SumaRecursiva(n / 10) + n % 10;
}

void main() {
    int OPCION, Numero;

    cout << "Ingrese El Numero: ";
    cin >> Numero;

    cout << "Escoga una opcion (1 para suma Iterativa, 2 para suma Recusrsiva): ";
    cin >> OPCION;



    if (OPCION == 1) {
        cout << "Resultado: " << SumaIterativa(Numero) << endl;
    }

    else if (OPCION == 2) {
        cout << "Resultado: " << SumaRecursiva(Numero) << endl;
    }
    else {
        cout << "NO VALIDO" << endl;
    }

}

