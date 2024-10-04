#Ejercicio 3. Para el árbol obtenido en el ejercicio 1 muestra la evolución de los siguientes algoritmos de recorrido de árboles binarios: 

# a) Recorrido en preorden 
# b) Recorrido en inorden 
# c) Recorrido en postorden

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def search(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(value)
            
        elif value > self.value:    
            if self.right is None:
                return False
            else:
                return self.right.search(value)
            
        else:
            return self

    def inorderPrint(self):
        if self.left:
            self.left.inorderPrint()
        print(self.value)
        if self.right:
            self.right.inorderPrint()

    def preorderPrint(self):
        print(self.value)
        if self.left:
            self.left.preorderPrint()
        if self.right:
            self.right.preorderPrint()

    def postorderPrint(self):
        if self.left:
            self.left.postorderPrint()
        if self.right:
            self.right.postorderPrint()
        print(self.value)

    def delete(self):
        # Método para eliminar un nodo del árbol
        if self.right is None and self.left is None:
            # Si el nodo no tiene hijos, eliminarlo
            self = None
        elif self.right is None:
            # Si el nodo solo tiene un hijo izquierdo, igualar a ese hijo
            self = self.left
        elif self.left is None:
            # Si el nodo solo tiene un hijo derecho, igualar a ese hijo
            self = self.right
        else:
            # Si el nodo tiene ambos hijos
            temp = self.right
            # Encontrar el nodo más a la izquierda en el subárbol derecho
            while temp.left:
                temp = temp.left
            # Establecer el hijo izquierdo del nodo más a la izquierda como el subárbol izquierdo del nodo actual
            temp.left = self.left
            # Igualar al nodo actual al nodo derecho, que ahora contiene todos los nodos
            self = self.right   


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def print_postorder(self):
        if self.root is not None:
            self.root.postorderPrint()
    
    def print_preorder(self):
        if self.root is not None:
            self.root.preorderPrint()

    def print_inorder(self):
        if self.root is not None:
            self.root.inorderPrint()


    def search(self, value):
        if self.root is not None:
            return self.root.search(value)
        else:
            return False
        
    def delete(self, value):
        if self.root is not None:
            #buscar el nodo a eliminar
            node = self.search(value)
            #eliminar el nodo
            node.delete()
            print("Element deleted successfully")
        else:
            print("Element not found")
    
    
# Create a list containing the given elements
bst_elements = ['G', 'B', 'Q', 'A', 'C', 'K', 'F', 'P', 'D', 'E', 'R', 'H']

# Create a new BST and insert all elements
bst = Tree()
for element in bst_elements:
    bst.insert(element)

#Recorrido en preorden
print("Recorrido en preorden:")
bst.root.preorderPrint()

#Recorrido en inorden
print("Recorrido en inorden:")
bst.root.inorderPrint()

#Recorrido en postorden
print("Recorrido en postorden:")
bst.root.postorderPrint()


