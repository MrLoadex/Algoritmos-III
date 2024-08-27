#include <iostream>

using namespace std;

/*Un Clínica Local nos pide Implementar un Sistema para manejar Pacientes.
Debe tener un menú que permita implementar una Lista que facilite: registrar, modificar, eliminar y listar pacientes.*/


struct Patient
{
    int dni;
    string lastName;
    string details;
};

// Crear la lista
const int maxPatients = 125;
int actualPatients = 0;
Patient patients[maxPatients];

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
        cout << " Ingrese la opcion que desee:" << endl;
        cout << " 1. Registrar paciente:" << endl;
        cout << " 2. Modificar paciente:" << endl;
        cout << " 3. Borrar paciente:" << endl;
        cout << " 4. Listar pacientes:" << endl;
        cin >> option;
        switch (option)
        {
        case 1:
            // Registrar paciente
            RegisterPatient();
            break;
        case 2:
            // Modificar paciente
            ModifyPatient();
            break;
        case 3:
            // Eliminar paciente
            DeletePatient();
            break;
        case 4:
            // Listar pacientes
            ListPatient();
            break;
        
        default:
            break;
        }
        cout << "Ingrese 0 para cotinuar o 1 para salir: ";
        cin >> exit;
    } while (!exit);

    return 0; 
}

// Registrar paciente
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
    // Comprobacion de seguridad
    if (actualPatients >= maxPatients) return;
    patients[actualPatients] = newPatient;
    actualPatients ++;
}
// Modificar paciente
void ModifyPatient()
{
    // indice del paciente
    int patientIndex;
    int atributeChangeOption;

    cout << "Ingrese el id del paciente:";
    cin >> patientIndex;
    //Comprobacion de seguridad
    if (patientIndex >= actualPatients) return;

    cout << "Ingrese el el dato a modificar:" << endl;
    cout << "0 para DNI." << endl;
    cout << "1 para Apellido." << endl;
    cout << "2 para Detalles." << endl;
    cout << "Opcion: ";
    
    cin >> atributeChangeOption;

    // dato a modificar
    switch (atributeChangeOption)
    {
    case 0:
        //DNI
        cin >> patients[patientIndex].dni;
        break;
    case 1:
        //apellido
        cin >> patients[patientIndex].lastName;
        break;
    case 2:
        //detalles
        getline (cin, patients[patientIndex].details);
        break;
    default:
        break;
    }
}
// Eliminar paciente
void DeletePatient()
{
    int patientIndex;
    cout << "Ingrese el id del paciente: ";
    cin >> patientIndex;
    // Comprobacion de seguridad
    if (patientIndex >= actualPatients) return;
    // Si es el ultimo paciente en la lista solo se resta uno al numero actual de pacientes
    if (patientIndex+1 >= maxPatients)
    {
        actualPatients --;
        return;
    }
    //Restar uno al total
    actualPatients --;
    // Recorrer desde el id del paciente
    for (int i = patientIndex; i < actualPatients; i++)
    {
        // Reemplazar con el paciente siguiente
        patients[i] = patients[i+1];
    }
}
// Listar pacientes
void ListPatient()
{
    for (int i = 0; i < actualPatients; i++)
    {
        cout << "id: " << i << endl;
        cout << "DNI: " << patients[i].dni << endl;
        cout << "Apellido: " << patients[i].lastName << endl;
        cout << "Detalles: " << patients[i].details << endl;
    }
}
