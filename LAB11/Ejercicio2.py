class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return self.Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    def build_from_list(self, values):
        for value in values:
            self.insert(value)

    def find_lca(self, val1, val2):
        """🧬 Encuentra el ancestro común más bajo (LCA) usando recursividad"""
        def _find_lca(node, val1, val2):
            if not node:
                return None
            # Si ambos valores son menores al nodo actual → LCA está en la izquierda
            if val1 < node.value and val2 < node.value:
                return _find_lca(node.left, val1, val2)
            # Si ambos valores son mayores → LCA está en la derecha
            elif val1 > node.value and val2 > node.value:
                return _find_lca(node.right, val1, val2)
            else:
                # Si divergen o uno es igual al nodo actual → este es el LCA
                return node.value
        return _find_lca(self.root, val1, val2)

def test_find_lca():
    bst1 = BinarySearchTree()
    bst1.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 1:", bst1.find_lca(2, 8) == 6)  # 🌲 Root is LCA

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 2:", bst2.find_lca(0, 4) == 2)  # 📚 Subtree LCA

    bst3 = BinarySearchTree()
    bst3.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 3:", bst3.find_lca(2, 3) == 2)  # 🔗 Ancestor node

    bst4 = BinarySearchTree()
    bst4.build_from_list([5, 3, 7])
    print("🧪 Test 4:", bst4.find_lca(5, 5) == 5)  # 🎯 Same node

    bst5 = BinarySearchTree()
    bst5.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 5:", bst5.find_lca(1, 3) == 2)  # 🌿 Leaf node LCA

# Ejecutar tests
test_find_lca()

