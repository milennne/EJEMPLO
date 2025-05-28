class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # 🔙 previous (in DLL)
        self.right = None  # 🔜 next (in DLL)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
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
        for v in values:
            self.insert(v)

    def bst_to_dll(self):
        """🔁 Convert BST to sorted circular doubly linked list"""
        if not self.root:
            return None

        self.first = None  # Primer nodo del DLL
        self.last = None   # Último nodo visitado

        def inorder(node):
            if not node:
                return

            # 🔁 Visita izquierda
            inorder(node.left)

            # 🔗 Conectar con el anterior
            if self.last:
                self.last.right = node
                node.left = self.last
            else:
                self.first = node  # El primer nodo (más pequeño)

            self.last = node  # Actualizar el último nodo

            # 🔁 Visita derecha
            inorder(node.right)

        inorder(self.root)

        # 🔄 Hacer la lista circular
        self.first.left = self.last
        self.last.right = self.first

        return self.first  # 🎉 Devuelve el inicio de la DLL
