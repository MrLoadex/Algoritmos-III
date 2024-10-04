# Ejercicio 2. Para el árbol obtenido en el ejercicio 1
# muestra el estado del mismo tras extraer de forma iterativa los siguientes elementos: 
# a) E 
# b) C 
# c) G 

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
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

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

    def print_tree(self):
        if self.root is not None:
            self.root.print_tree()

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

# Print the BST to verify the order
print("Binary Search Tree (in-order traversal):")
print(bst.print_tree() )
print(bst.search('H').value)
bst.delete('H')
print("Binary Search Tree (in-order traversal) after deleting 'H':")
print(bst.print_tree() )