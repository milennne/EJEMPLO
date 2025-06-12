class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class AVLTree:
    def insert(self, root, key):
        """Insert a node like in a regular Binary Search Tree (no balancing logic)."""
        if root is None:
            return AVLNode(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def is_avl_balanced(self, root):
        """📏 Check if the tree is AVL-balanced"""

        def check(node):
            if node is None:
                return 0  # Height of an empty node is 0

            left_height = check(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced

            right_height = check(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced

            if abs(left_height - right_height) > 1:
                return -1  # Balance factor is out of range [-1, 1]

            return max(left_height, right_height) + 1  # Height of current node

        return check(root) != -1

# 🧪 Test cases
def test_is_avl_balanced():
    avl = AVLTree()
    root = None
    for val in [20, 10, 30]:
        root = avl.insert(root, val)
    print("Test 1:", avl.is_avl_balanced(root) == True)  # ✅ Balanced tree

    # Simulate manually unbalanced tree
    unbalanced = AVLNode(10)
    unbalanced.right = AVLNode(20)
    unbalanced.right.right = AVLNode(30)
    print("Test 2:", avl.is_avl_balanced(unbalanced) == False)  # ⚠️ Unbalanced

    print("Test 3:", avl.is_avl_balanced(None) == True)  # 🌱 Empty tree is balanced

    # Deep imbalance tree
    deep_unbalanced = AVLNode(10)
    deep_unbalanced.left = AVLNode(5)
    deep_unbalanced.left.left = AVLNode(2)
    deep_unbalanced.left.left.left = AVLNode(1)
    print("Test 4:", avl.is_avl_balanced(deep_unbalanced) == False)  # ⚠️ Deeply unbalanced

    # Valid AVL with multiple levels
    root2 = None
    for val in [50, 30, 70, 20, 40, 60, 80]:
        root2 = avl.insert(root2, val)
    print("Test 5:", avl.is_avl_balanced(root2) == True)  # ✅ Balanced tree

# 🚀 Run tests
test_is_avl_balanced()
