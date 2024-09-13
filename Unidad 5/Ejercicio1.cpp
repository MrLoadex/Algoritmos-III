/*
Un Negocio necesita gestionar la atención a sus cliente, el mismo recibe los clientes en un Box de Atención que registra los clientes y los carga para su atención según su llegada.
Nos piden desarrollar un sistema de “Turnos” que se muestran en una pantalla.
La aplicación deberá registrar los clientes, mostrarlos en orden de llegada, llamarlos según ese orden por pantalla con una opción “próximo cliente – Box nro”
Lo importante es no usar la stl.
*/

#include <iostream>
#include <string>

using namespace std;

struct Customer {
    string name;
    int dni;
};

struct Node {
    Customer customer;
    Node* nextNode;
};

class Turns {
    private:
        Node* head;
        Node* tail;

    public:
        Turns();
        void registerCustomer(const string name, int dni);
        void showTurns();
        void callCustomer(int box);
};

Turns::Turns() {
    head = nullptr;
    tail = nullptr;
}

void Turns::registerCustomer(const string name, int dni) {
    Node* newNode = new Node();
    newNode->customer.name = name;
    newNode->customer.dni = dni;
    newNode->nextNode = nullptr;

    if (head == nullptr) {
        head = newNode;
        tail = newNode;
    } 
    else {
        tail->nextNode = newNode;
        tail = newNode;
    }
}

void Turns::showTurns() {
    Node* current = head;
    while (current != nullptr) {
        cout << "Cliente: " << current->customer.name << ", DNI: " << current->customer.dni << endl; 
        current = current->nextNode;
    }
}

void Turns::callCustomer(int box) {
    if (head == nullptr) { 
        cout << "No hay clientes en la lista" << endl;
        return;
    }
    cout << "Próximo cliente: " << head->customer.name << ", DNI: " << head->customer.dni << endl;
    cout << "Box: " << box << endl;
    Node* temp = head;
    head = head->nextNode;

    if (head == nullptr) {
        tail = nullptr;
        delete temp;
        return;
    }
    else if (head->nextNode == nullptr) {
        tail = head;
    }
    delete temp;
}

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