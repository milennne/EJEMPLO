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

    def range_query(self, min_val, max_val):
        """🎯 Devuelve todos los valores dentro del rango [min_val, max_val] en orden ascendente"""
        result = []

        def _inorder(node):
            if not node:
                return
            if node.value > min_val:
                _inorder(node.left)
            if min_val <= node.value <= max_val:
                result.append(node.value)
            if node.value < max_val:
                _inorder(node.right)

        _inorder(self.root)
        return result

    def find_lca(self, val1, val2):
        """🧬 Encuentra el ancestro común más bajo (LCA) usando recursividad"""
        def _find_lca(node, val1, val2):
            if not node:
                return None
            if val1 < node.value and val2 < node.value:
                return _find_lca(node.left, val1, val2)
            elif val1 > node.value and val2 > node.value:
                return _find_lca(node.right, val1, val2)
            else:
                return node.value
        return _find_lca(self.root, val1, val2)

# 🧪 Test cases para range_query
def test_range_query():
    bst1 = BinarySearchTree()
    bst1.build_from_list([7, 3, 11, 1, 5, 9, 13])
    print("Test 1:", bst1.range_query(5, 10) == [5, 7, 9])  # ✅

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 4, 8, 2])
    print("Test 2:", bst2.range_query(1, 10) == [2, 4, 6, 8])  # 🌐

    bst3 = BinarySearchTree()
    bst3.build_from_list([20, 10, 30])
    print("Test 3:", bst3.range_query(1, 5) == [])  # 📭

    bst4 = BinarySearchTree()
    bst4.build_from_list([15])
    print("Test 4:", bst4.range_query(10, 20) == [15])  # 🌱

    bst5 = BinarySearchTree()
    bst5.build_from_list([15, 10, 20, 5, 25])
    print("Test 5:", bst5.range_query(10, 20) == [10, 15, 20])  # 🔗

# 🚀 Ejecutar tests
test_range_query()
