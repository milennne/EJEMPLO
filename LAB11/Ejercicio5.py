# ✅ Nodo de árbol (también usado como nodo de la lista)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # 🔙 Puntero al nodo anterior en la DLL
        self.right = None  # 🔜 Puntero al siguiente nodo en la DLL

# ✅ Árbol binario de búsqueda (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """🔧 Inserta un valor en el BST"""
        def _insert(node, value):
            if not node:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def build_from_list(self, values):
        """📥 Construye el BST a partir de una lista de valores"""
        for v in values:
            self.insert(v)

    def bst_to_dll(self):
        """🔁 Convierte el BST a una lista doblemente enlazada circular ordenada"""
        if not self.root:
            return None

        self.first = None  # 🟢 Primer nodo del DLL
        self.last = None   # 🔴 Último nodo visitado

        def inorder(node):
            if not node:
                return

            # 📥 Visita izquierda
            inorder(node.left)

            # 🔗 Conectar el nodo actual al último visitado
            if self.last:
                self.last.right = node  # el último apunta al actual
                node.left = self.last   # el actual apunta hacia atrás
            else:
                self.first = node  # Guardamos el primer nodo (más pequeño)

            self.last = node  # Actualizamos el último nodo

            # 📤 Visita derecha
            inorder(node.right)

        # 🔁 Recorrido inorden del BST
        inorder(self.root)

        # 🔄 Hacer circular la lista
        self.first.left = self.last
        self.last.right = self.first

        return self.first  # 🔚 Retorna el inicio de la DLL

# ✅ Validador de la DLL circular
def validate_circular_dll(head, expected_values):
    if not head:
        return expected_values == []
    values = []
    current = head
    while True:
        values.append(current.value)
        current = current.right
        if current == head:  # Se completa el ciclo
            break
    return values == expected_values

# ✅ Casos de prueba
def test_bst_to_dll():
    bst1 = BinarySearchTree()
    bst1.build_from_list([2, 1, 3])
    head1 = bst1.bst_to_dll()
    print("🧪 Test 1:", validate_circular_dll(head1, [1, 2, 3]) == True)

    bst2 = BinarySearchTree()
    bst2.build_from_list([4, 2, 6, 1, 3, 5, 7])
    head2 = bst2.bst_to_dll()
    print("🧪 Test 2:", validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)

    bst3 = BinarySearchTree()
    bst3.build_from_list([5])
    head3 = bst3.bst_to_dll()
    print("🧪 Test 3:", validate_circular_dll(head3, [5]) == True)

    bst4 = BinarySearchTree()
    bst4.build_from_list([1, 2, 3, 4])
    head4 = bst4.bst_to_dll()
    print("🧪 Test 4:", validate_circular_dll(head4, [1, 2, 3, 4]) == True)

    bst5 = BinarySearchTree()
    head5 = bst5.bst_to_dll()
    print("🧪 Test 5:", head5 is None)

# 🚀 Ejecutar pruebas
test_bst_to_dll()
