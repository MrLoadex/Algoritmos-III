/*
Una empresa necesita implementar un Historial de llamadas a sus cliente, la aplicación deberá ir cargando
los números telefónicos en un historial y el usuario podrá ir recorriendo el histórico de llamadas (similar al
botón Back del navegador).
Implementar una app que realice esta función.
*/

#include <iostream>
#include <string>
#include <stack>

using namespace std;

class User;

struct Call {
    User *user;
    string date;
};

class User{
    public:
    string name;
    string phoneNumber;
    stack<Call> callsHistory;
    void addCall(Call call);
    void showHistory();
};

void User::addCall(Call call){
    callsHistory.push(call);
}

void User::showHistory(){
    stack<Call> temp = callsHistory;
    cout << "Historial de llamadas de " << name << endl;
    while (!temp.empty())
    {
        cout << temp.top().user->name << endl;
        cout << temp.top().date << endl;
        temp.pop();
    }
}

void phoneSystem(User* mainUser, User contacts[], const int MAX_USERS){
    // Sistema para realizar una llamada o ver historial
    int option;
    int index;
    cout << "Ingrese 1 para realizar una llamada o 2 para ver el historial: ";
    cin >> option;
    if (option == 1)
    {
        for (int i = 0; i < MAX_USERS; i++)
        {
            cout << "ID: " << i << " - Nombre: " << contacts[i].name << endl;
            cout << "Telefono: " << contacts[i].phoneNumber << endl;
        }
        cout << "Ingrese el ID del usuario: ";
        cin >> index;
        for (int i = 0; i < MAX_USERS; i++)
        {
            if (index == i)
            {
                Call call;
                call.user = &contacts[i];
                //obtener la fecha actual
                time_t now = time(0);
                call.date = ctime(&now);

                mainUser->addCall(call);
                cout << "Llamada agregada al historial." << endl;
            }
        }
    }
    else if (option == 2)
    {
        mainUser->showHistory();
    }

}

main(){
    // Crear el usuario principal
    User* mainUser = new User();
    mainUser->name = "Juan";
    mainUser->phoneNumber = "1234567890";

    // Crear los contactos
    const int MAX_CONTACTS = 5;
    User contacts[MAX_CONTACTS];
    string names[] = {"Juan", "Pedro", "Maria", "Luisa", "Ana"};
    string phoneNumbers[] = {"1234567890", "1234567891", "1234567892", "1234567893", "1234567894"};


    for (int i = 0; i < MAX_CONTACTS; i++)
    {
        contacts[i].name = names[i];
        contacts[i].phoneNumber = phoneNumbers[i];
    }
    // Menu para realizar una llamada o ver historial
    int option;
    do{
        phoneSystem(mainUser, contacts, MAX_CONTACTS);
        cout << "Ingrese 1 para salir o 2 para continuar: ";
        cin.ignore();
        cin >> option;
    }while(option != 1);
    
}