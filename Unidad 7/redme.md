**Instituto Superior de Formación Técnica Nº 151		  ![][image1]**  
**Carrera: Analista en Sistemas**  
**3 Año.  Algoritmos y Estructuras de Datos III.**

| Trabajo Práctico Nº7 | Unidad 7 |
| :---- | :---- |
| **Modalidad:** Semi \-Presencial | **Estratégica Didáctica:** Trabajo individual. |
| **Metodología de Desarrollo:**  Det. docente | **Metodología de Corrección:** Via Classroom. |
| **Carácter de Trabajo:** Obligatorio – Con Nota | **Fecha Entrega:** A confirmar por el Docente. |

**ARBOLES.**

**Marco Teórico:**

Responder el siguiente cuestionario en función de la bibliografía Obligatoria.

**1**. Que es un Grafo

Un grafo es un conjunto de puntos (llamados nodos) que están conectados por líneas (llamadas aristas). Cada nodo representa algo, como una tarea o un lugar, y las aristas muestran cómo están relacionados esos nodos.

2\. Que es un Árbol y que tipos de Problemas resuelve.

Un árbol es un tipo de estructura de datos abstracta que se utiliza para organizar elementos jerárquicamente. Consiste en nodos conectados por aristas, donde cada nodo puede tener múltiples hijos, pero solo un padre (excepto el nodo raíz, que no tiene padre). Los árboles se utilizan ampliamente debido a su eficiencia en diversas operaciones, como búsqueda, inserción, y eliminación de datos.

3\. Qué función tiene un Árbol Binario. Qué operaciones posee.

Un árbol binario organiza datos de manera jerárquica para facilitar la búsqueda, inserción y eliminación. Cada nodo puede tener hasta dos hijos, lo que lo hace eficiente para tareas de búsqueda y ordenación.

Las operaciones principales son:

* **Inserción**: Agregar un nuevo nodo en la posición adecuada.  
* **Búsqueda**: Encontrar un nodo con un valor específico.  
* **Eliminación**: Quitar un nodo, reorganizando el árbol si es necesario.  
* **Recorridos**: Preorden, inorden y postorden para visitar nodos del árbol en diferentes secuencias.

4\. Que es un Árbol Balanceado, dar ejemplos de su uso.

Un árbol balanceado es aquel en el que la altura de sus subárboles difiere en no más de una unidad, lo que garantiza un rendimiento óptimo en operaciones como búsqueda, inserción y eliminación, manteniendo el tiempo de ejecución logarítmico.

Ejemplos de su uso:

* **Árbol AVL**: Utilizado en bases de datos y sistemas de archivos para asegurar una búsqueda eficiente.  
* **Árbol rojo-negro**: Implementado en bibliotecas estándar como `map` y `set` en C++, para operaciones rápidas de búsqueda y ordenación.

5\. ¿Qué es un Árbol B y B+, cual es la diferencia?  
Un **árbol B** es una estructura de datos auto-balanceada que mantiene los datos ordenados y permite búsquedas, inserciones y eliminaciones eficientes, incluso en grandes volúmenes de datos. Es comúnmente utilizado en sistemas de bases de datos y sistemas de archivos.

Un **árbol B+** es una variante del árbol B, con la diferencia de que:

* En el **árbol B**, los datos pueden almacenarse tanto en nodos internos como en hojas.  
* En el **árbol B+**, todos los datos se almacenan únicamente en las hojas, mientras que los nodos internos solo contienen punteros para facilitar la búsqueda. Además, las hojas en un árbol B+ están enlazadas entre sí, lo que permite recorridos secuenciales más rápidos.

**Marco Practico:**

1. Ejercicio 1\. Construye un árbol binario de búsqueda a partir de la siguiente lista: G B Q A C K F P D E R H 

2. Ejercicio 2\. Para el árbol obtenido en el ejercicio 1 muestra el estado del mismo tras extraer de forma iterativa los siguientes elementos: a) E b) C c) G 

3. Ejercicio 3\. Para el árbol obtenido en el ejercicio 1 muestra la evolución de los siguientes algoritmos de recorrido de árboles binarios: 

   a) Recorrido en preorden   
   b) Recorrido en inorden   
   c) Recorrido en postorden

Lic. Oemig José Luis.

[image1]: <data:image/png;base64,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>