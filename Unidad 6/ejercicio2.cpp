/*
Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero
natural dado, conociendo solo que:
a. 1 es impar.
b. Si un número es impar, su antecesor es par; y viceversa.
*/

#include <iostream>

using namespace std;

void inpar(int n);
void par(int n);

void inpar(int n) {
    if (n == 1) 
    {
        cout << "es impar" << endl;
    }
    else 
    {
        par(n-1);
        //par(n+1); // Contempla el caso de n = 0
    }
}

void par(int n) {
    if (n == 1) {
        cout << "es par" << endl;
    }
    else {
        inpar(n-1);
        //inpar(n+1); // Contempla el caso de n = 0
    }
}


int main()
{
    int n;
    cout << "Ingrese un numero: ";
    cin >> n;
    inpar(n);
    return 0;
}

