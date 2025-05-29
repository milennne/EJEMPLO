class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def build_from_list(self, values):
        for val in values:
            self.insert(val)

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = Node(val)

    def is_valid_bst(self):
        """🧼 Check if the tree satisfies the BST property"""
        def validate(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(self.root, float('-inf'), float('inf'))

# 🧪 Test cases
def test_is_valid_bst():
    bst1 = BinarySearchTree()
    bst1.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 1:", bst1.is_valid_bst() == True)  # ✅ Valid tree

    bst2 = BinarySearchTree()
    bst2.root = Node(5)
    bst2.root.left = Node(6)  # ❌ Incorrect: left > root
    bst2.root.right = Node(7)
    print("🧪 Test 2:", bst2.is_valid_bst() == False)  # ❌ Left violation

    bst3 = BinarySearchTree()
    bst3.root = Node(5)
    bst3.root.left = Node(3)
    bst3.root.right = Node(4)  # ❌ Incorrect: right < root
    print("🧪 Test 3:", bst3.is_valid_bst() == False)  # ❌ Right violation

    bst4 = BinarySearchTree()
    bst4.build_from_list([42])
    print("🧪 Test 4:", bst4.is_valid_bst() == True)  # 🌱 Single node

    bst5 = BinarySearchTree()
    print("🧪 Test 5:", bst5.is_valid_bst() == True)  # 📭 Empty tree

# 🚀 Run tests
test_is_valid_bst()
