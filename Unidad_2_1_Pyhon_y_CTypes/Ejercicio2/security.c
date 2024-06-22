// Definición de la función en C
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//Armar totalmente
char* fully_assemble() 
{
    return "Sistema completamente armado";
}

//Armar parcialmente
char* partially_assemble() 
{
    return "Sistema parcialmente armado.";
}

//Armar parcialmente
char* desactive() 
{
    return "Sistema desactivado.";
}

// Cancelar zona
char* cancelZone(int zone) {
    // Asignar suficiente espacio para la cadena resultante
    char* result = (char*)malloc(50 * sizeof(char));  // Ajustar el tamaño según sea necesario
    if (result != NULL) {
        // Formatear la cadena con el número de zona
        snprintf(result, 50, "Zona %d armada.", zone);
    }
    return result;
}

// Activar panico
char* activePanic() {
    return "Panico activado, llamando al 911.";
}

// LLamar a emergencias
char* callToEmergency()
{
    return "Llamando al 911";
}
