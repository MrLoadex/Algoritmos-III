## Ejercicio 1. Construye un árbol binario de búsqueda a partir de la siguiente lista: G B Q A C K F P D E R H
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
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

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

# Create a list containing the given elements
bst_elements = ['G', 'B', 'Q', 'A', 'C', 'K', 'F', 'P', 'D', 'E', 'R', 'H']

# Create a new BST and insert all elements
bst = Tree()
for element in bst_elements:
    bst.insert(element)

# Print the BST to verify the order
print("Binary Search Tree (in-order traversal):")
bst.print_tree()