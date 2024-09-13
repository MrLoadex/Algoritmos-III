**Instituto Superior de Formación Técnica Nº 151		  ![][image1]**  
**Carrera: Analista en Sistemas**  
**3 Año.  Algoritmos y Estructuras de Datos III.**

| Trabajo Práctico Nº5 | Unidad 5 |
| :---- | :---- |
| **Modalidad:** Semi \-Presencial | **Estratégica Didáctica:** Trabajo individual. |
| **Metodología de Desarrollo:**  Det. docente | **Metodología de Corrección:** Via Classroom. |
| **Carácter de Trabajo:** Obligatorio – Con Nota | **Fecha Entrega:** A confirmar por el Docente. |

**PILAS Y COLAS.**

**Marco Teórico:**

Responder el siguiente cuestionario en función de la bibliografía Obligatoria.

**1**. Describir el concepto de Pila y sus Operaciones Básicas

2\. Explicar el concepto de “StakOverFlow” y como evitarelo?

3\. Buscar describir las diferencias de Implementar Pilas en Clase vs via sTL

4\. Que es una Cola y cuales son las operaciones Básicas?

5\. Describir: Cola circular, Multicola, Deque y cola prioritaria.

6\. Dar ejemplos de utilización para Pilas, Colas y otros subtipos.

**RTAs:**

1. La pila es un tipo de dato abstracto. Es una colección de objetos donde el último en ser añadido es el primero en salir. Sus operaciones básicas son:  
   * push() \= Ingresa un elemento en el último lugar de la pila  
   * pop() \= Devuelve el último elemento en la pila y lo elimina.  
   * peek() \= Permite visualizar el último elemento de la pila, pero sin eliminarlo.  
   * isEmpty() \= Devuelve true si la pila está vacía.  
     

2. StackOverflow se produce por un uso excesivo de la pila. Para evitarlo, es fundamental:  
* Definir casos base claros en funciones recursivas.  
* Optimizar bucles y condiciones de salida.  
* Gestionar el alcance de las variables locales.  
* Considerar la tail recursión o la iteración cuando sea posible.  
  * **Optimización del compilador:** En algunos lenguajes, la tail recursión puede ser optimizada para evitar el crecimiento de la pila.  
  * **Eficiencia:** A menudo, los bucles son más eficientes que la recursión en términos de uso de memoria.

    

3.  Implementar una pila en **Clase** vs utilizar la pila de **STL**

| Cuándo utilizar | Implementar una pila en clase | Utilizar la pila de STL |
| :---- | :---- | :---- |
| Control sobre la implementación | Alto | Bajo |
| Optimización | Alto | Medio-alto |
| Aprendizaje | Excelente | Bueno |
| Tiempo de desarrollo | Alto | Bajo |
| Portabilidad | Baja | Alta |
| Características adicionales | Personalizadas | Muchas (iteradores, etc.) |
| Mantenibilidad | Puede ser baja | Alta |
| Colaboración | Puede ser difícil | Fácil |

   

4. Una cola es una estructura de datos donde los elementos se añaden por un extremo (final) y se eliminan por el otro (inicio).  
   * **push():** Agregar un elemento al final de la cola.  
   * **front():** Obtener el primer elemento sin eliminarlo.  
   * **pop():**  Eliminar el primer elemento.  
   * **empty():** Devuelve true si la cola está vacía, false en caso contrario.  
   * **size():** Obtener el tamaño actual de la cola.  
5. **Cola circular:** Cada elemento o nodo posee una dirección al siguiente elemento, y el último nodo posee la dirección del primero.   
   **Multicola:** Posee varias ‘cabeceras’, osea que se puede acceder a la cola de distintos lugares.

   **Deque:** Es la suma de una pila y una cola. Osea se pueden realizar operaciones en ambos extremos.

   **Cola prioritaria:** Se pueden insertar elementos en cualquier orden. A cada elemento se le debe asignar una prioridad. Se procesa el elemento de mayor prioridad. 

6. Para Pilas y Colas más subtipos, Dar ejemplos de Utilización de cada uno.

   * **Pilas:**

     * **Deshacer/rehacer:** Se utiliza una pila para almacenar los cambios realizados y permitir deshacer o rehacer acciones en un editor de texto.

     * **Gestión de llamadas a funciones:** En lenguajes de programación que utilizan una pila de llamadas, esta estructura es esencial para el correcto funcionamiento de las funciones recursivas y el seguimiento del flujo de ejecución del programa.

     * **Exploración de niveles:** En juegos con niveles procedimentales, las pilas se pueden utilizar para almacenar el camino recorrido por el jugador, permitiendo volver atrás en caso de que se encuentre un callejón sin salida.

   * **Colas:**

     * **Gestión de eventos:** Los eventos del juego (como colisiones, acciones del jugador) se suelen almacenar en una cola y procesarse en orden de llegada. Esto asegura que los eventos se manejen de manera secuencial y sin interferencias.

     * **Sistemas de partículas:** Las partículas (efectos visuales como explosiones, humo) se añaden a una cola y se actualizan y renderizan en cada frame.

**Marco Practico:**

1. Un Negocio necesita gestionar la atención a sus cliente, el mismo recibe los clientes en un Box de Atención que registra los clientes y los carga para su atención según su llegada.  
   Nos piden desarrollar un sistema de “Turnos” que se muestran en una pantalla.  
   La aplicación deberá registrar los clientes, mostrarlos en orden de llegada, llamarlos según ese orden por pantalla con una opción “próximo cliente – Box nro”

2. Ídem 1 pero Implementando Listas en STL

3. Una empresa necesita implementar un Historial de llamadas a sus clientes, la aplicación deberá ir cargando los números telefónicos en un historial y el usuario podrá ir recorriendo el histórico de llamadas (similar al botón Back del navegador).  
   Implementar una app que realice esta función.

Lic. Oemig José Luis.

[image1]: <data:image/png;base64,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>