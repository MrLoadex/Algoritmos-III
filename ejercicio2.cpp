#include <iostream>
#include <list>
#include <string>

using namespace std;

struct Patient
{
    int dni;
    string lastName;
    string details;
};

list<Patient> patients;

void RegisterPatient();
void ModifyPatient();
void DeletePatient();
void ListPatient();

int main() 
{
    bool exit = false;
    int option;
    
    do
    {
        cout << "Ingrese la opcion que desee:" << endl;
        cout << "1. Registrar paciente:" << endl;
        cout << "2. Modificar paciente:" << endl;
        cout << "3. Borrar paciente:" << endl;
        cout << "4. Listar pacientes:" << endl;
        cin >> option;
        
        switch (option)
        {
            case 1:
                RegisterPatient();
                break;
            case 2:
                ModifyPatient();
                break;
            case 3:
                DeletePatient();
                break;
            case 4:
                ListPatient();
                break;
            default:
                break;
        }
        
        cout << "Ingrese 0 para continuar o 1 para salir: ";
        cin >> exit;
        
    } while (!exit);

    return 0; 
}

void RegisterPatient()
{
    Patient newPatient;
    cout << "DNI: ";
    cin >> newPatient.dni;
    cout << "Apellido: ";
    cin >> newPatient.lastName;
    cout << "Detalles: ";
    cin.ignore();
    getline(cin, newPatient.details);
    
    patients.push_back(newPatient);
}

void ModifyPatient()
{
    int patientIndex;
    int atributeChangeOption;
    
    cout << "Ingrese el id del paciente: ";
    cin >> patientIndex;

    if (patientIndex >= patients.size()) return;

    // Puntero al primer elemento de patients
    auto it = patients.begin();
    // Mover el punter patientIndex lugares.
    advance(it, patientIndex);

    cout << "Ingrese el dato a modificar:" << endl;
    cout << "0 para DNI." << endl;
    cout << "1 para Apellido." << endl;
    cout << "2 para Detalles." << endl;
    cout << "Opcion: ";
    
    cin >> atributeChangeOption;

    switch (atributeChangeOption)
    {
        case 0:
            cin >> it->dni;
            break;
        case 1:
            cin >> it->lastName;
            break;
        case 2:
            cin.ignore();
            getline(cin, it->details);
            break;
        default:
            break;
    }
}

void DeletePatient()
{
    int patientIndex;
    cout << "Ingrese el id del paciente: ";
    cin >> patientIndex;

    if (patientIndex >= patients.size()) return;

    auto it = patients.begin();
    advance(it, patientIndex);
    patients.erase(it);
}

void ListPatient()
{
    int index = 0;
    for (const auto& patient : patients)
    {
        cout << "id: " << index++ << endl;
        cout << "DNI: " << patient.dni << endl;
        cout << "Apellido: " << patient.lastName << endl;
        cout << "Detalles: " << patient.details << endl;
    }
}
