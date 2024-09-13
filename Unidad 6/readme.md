**Instituto Superior de Formación Técnica Nº 151		  ![][image1]**  
**Carrera: Analista en Sistemas**  
**3 Año.  Algoritmos y Estructuras de Datos III.**

| Trabajo Práctico Nº6 | Unidad 6 |
| :---- | :---- |
| **Modalidad:** Semi \-Presencial | **Estratégica Didáctica:** Trabajo individual. |
| **Metodología de Desarrollo:**  Det. docente | **Metodología de Corrección:** Via Classroom. |
| **Carácter de Trabajo:** Obligatorio – Con Nota | **Fecha Entrega:** A confirmar por el Docente. |

**RECURSION.**

**Marco Teórico:**

Responder el siguiente cuestionario en función de la bibliografía Obligatoria.

**1**. Que entiende por Recursión

2\. Que es una función Recursiva y que entiende por Recurrencia , dar ejemplos.

3\. Explicar le uso del Stack del sistema operativo en Funciones Recursivas, dar un ejemplo.

4\. Explicar las distintas variantes de Recursión.

5\. Describir las diferencias entre Iteración y Recursión.

**Marco Practico:**

1. Para el Ejercicio de la Unidad anterior:  “*Un Negocio necesita gestionar la atención a sus cliente, el mismo recibe los clientes en un Box de Atención que registra los clientes y los carga para su atención según su llegada.*  
   *Nos piden desarrollar un sistema de “Turnos” que se muestren en una pantalla.*  
   *La aplicación deberá registrar los clientes, mostrarlos en orden de llegada, llamarlos según ese orden por pantalla con una opción “próximo cliente – Box nro”*  
   Nos Solicitan imprimir el tiempo de “Espera” de cada persona en la Lista, deberá Implementar esto de Forma recursiva.

2. Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:

   1. 1 es impar.

   2. Si un número es impar, su antecesor es par; y viceversa.

     
      

   

   ---

   

   **RTAs:**

**1**. Es la especificación de un proceso en su propia definición.

2\. Una función recursiva de una función que, directa o indirectamente, se llama a sí misma. Se utiliza la recursión para solucionar problemas complejos, dividiendo la solución final en soluciones del mismo problema pero con datos más sencillos o con menos datos.

3\. La función recursiva va ‘acumulando’ sus instancias de ejecución como elementos de una pila y al finalizar debe ‘volver al principio’ para retornar un dato. Por ejemplo:

int factorial(int n) {

    if (n \== 0\) {

        return 1; // Caso base

    } else {

        return n \* factorial(n \- 1); // Llamada recursiva

    }

}

4\. 

* **Recursión Directa:** Una función se llama a sí misma directamente. Es la forma más común.  
* **Recursión Indirecta o Cruzada:** Dos o más funciones se llaman entre sí de forma circular.  
* **Recursión Múltiple:** Una función se llama a sí misma varias veces en una misma llamada.  
* **Recursión de Cola:** La última operación de una función es una llamada recursiva. Puede ser optimizada en algunos lenguajes.  
* **Recursión Estructural:** Se aplica a estructuras de datos recursivas como árboles o listas.

5\.  La principal diferencia entre la iteración y la recursión radica en la forma en que se repiten las operaciones y en el uso de la memoria. La iteración utiliza un bucle para repetir un bloque de código un número determinado de veces, modificando los datos dentro de ese mismo bloque. Por otro lado, la recursión implica que una función se llame a sí misma, creando una nueva instancia de la función cada vez que se realiza la llamada. Estas instancias se apilan en la memoria hasta que se alcanza un caso base, lo que genera un mayor consumo de memoria en comparación con la iteración.

Lic. Oemig José Luis.

[image1]: <data:image/png;base64,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>