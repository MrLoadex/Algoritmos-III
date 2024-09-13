/*
Para el Ejercicio de la Unidad anterior:  “Un Negocio necesita gestionar la atención a sus cliente, el mismo 
recibe los clientes en un Box de Atención que registra los clientes y los carga para su atención según su llegada.
Nos piden desarrollar un sistema de “Turnos” que se muestren en una pantalla.
La aplicación deberá registrar los clientes, mostrarlos en orden de llegada, 
llamarlos según ese orden por pantalla con una opción “próximo cliente – Box nro”
Nos Solicitan imprimir el tiempo de “Espera” de cada persona en la Lista, deberá Implementar esto de Forma recursiva.
*/

#include <iostream>
#include <queue>
#include <string>
#include <ctime>
#include <cstdlib>


using namespace std;

struct Customer {
    string name;
    time_t arrivalTime;

    Customer(string _name) : name(_name), arrivalTime(time(nullptr)) {}
};

class TurnSystem {
    private:
        queue<Customer> customersQueue;
        int boxNumber;

    public:
        TurnSystem() : boxNumber(1) {}

        void registerCustomer(string name) {
            customersQueue.push(Customer(name));
            cout << "Cliente " << name << " registrado.\n";
        }

        void callNextCustomer() {
            if (!customersQueue.empty()) {
                Customer customer = customersQueue.front();
                customersQueue.pop();
                cout << "Próximo cliente - Box nro " << boxNumber << ": " << customer.name << "\n";
                boxNumber = (boxNumber % 3) + 1;
            } else {
                cout << "No hay clientes en espera.\n";
            }
        }

        void showWaitingTimes() {
            cout << "Tiempos de espera:\n";
            showWaitingTimesRecursive(customersQueue);
        }

    private:
        void showWaitingTimesRecursive(queue<Customer> tempQueue) {
            if (tempQueue.empty()) {
                return;
            }

            Customer customer = tempQueue.front();
            tempQueue.pop();

            time_t currentTime = time(nullptr);
            int waitingTime = int(difftime(currentTime, customer.arrivalTime));

            cout << customer.name << ": " << waitingTime << " segundos\n";

            showWaitingTimesRecursive(tempQueue);
        }
};

int main() {
    TurnSystem system;
    string pause;
    system.registerCustomer("Juan");
    cout << "Presione Enter para continuar...";
    cin >> pause;
    system.registerCustomer("María");
    cout << "Presione Enter para continuar...";
    cin >> pause;
    system.registerCustomer("Pedro");
    cout << "Presione Enter para continuar...";
    cin >> pause;

    system.callNextCustomer();
    system.callNextCustomer();

    system.registerCustomer("Ana");

    system.showWaitingTimes();

    return 0;
}