/*
Un Negocio necesita gestionar la atención a sus cliente, el mismo recibe los clientes en un Box de Atención que registra los clientes y los carga para su atención según su llegada.
Nos piden desarrollar un sistema de “Turnos” que se muestran en una pantalla.
La aplicación deberá registrar los clientes, mostrarlos en orden de llegada, llamarlos según ese orden por pantalla con una opción “próximo cliente – Box nro”
*/

#include <iostream>
#include <string>
#include <queue>

using namespace std;

struct Customer {
    string name;
    int dni;
};

class Turns {
    private:
        queue<Customer> customers;


    public:
        Turns();
        void registerCustomer(const string name, int dni);
        void showTurns();
        void callCustomer(int box);
        ~Turns();
};

Turns::Turns() {}

void Turns::registerCustomer(const string name, int dni) {
    Customer newCustomer;
    newCustomer.name = name;
    newCustomer.dni = dni;
    customers.push(newCustomer);
}

void Turns::showTurns() {
    queue<Customer> tempQueue = customers;
    while (!tempQueue.empty()) {
        cout << "Cliente: " << tempQueue.front().name << ", DNI: " << tempQueue.front().dni << endl;
        tempQueue.pop();
    }
}

void Turns::callCustomer(int box) {
    Customer currentCustomer = customers.front();
    cout << "Próximo cliente: " << currentCustomer.name << ", DNI: " << currentCustomer.dni << endl;
    cout << "Box: " << box << endl;
    customers.pop();
}

Turns::~Turns() {}

int main() {
    Turns turns;
    int option, dni;
    string name;
    int box;

    do {
        cout << "1. Registrar Cliente" << endl;
        cout << "2. Mostrar Turnos" << endl;
        cout << "3. Llamar Cliente" << endl;
        cout << "4. Salir" << endl;
        cout << "Ingrese una opcion: ";
        cin >> option;
        switch (option) {
            case 1:
                cout << "Ingrese el nombre del cliente: ";
                cin >> name;
                cout << "Ingrese el DNI del cliente: ";
                cin >> dni;
                turns.registerCustomer(name, dni);
                break;
            case 2:
                turns.showTurns();
                break;
            case 3:
                cout << "Ingrese el Box de atencion: ";
                cin >> box;
                turns.callCustomer(box);
                break;
            case 4:
                cout << "Saliendo..." << endl;
                break;
        }
    } while (option != 4);

    return 0;
}