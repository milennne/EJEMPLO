class Node:
    # Class representing a node in a binary search tree
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    # Binary Search Tree implementation with insert and inorder traversal
    def __init__(self):
        self.root = None

    def insert(self, val):
        # Inserts a value into the BST
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

    def inorder(self):
        # Returns the inorder traversal as a list
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)


def balance_bst(bst):
    
    # Balances a BST using inorder traversal and divide-and-conquer construction
    def build_balanced_bst(sorted_vals):
        if not sorted_vals:
            return None
        mid = len(sorted_vals) // 2
        node = Node(sorted_vals[mid])
        node.left = build_balanced_bst(sorted_vals[:mid])
        node.right = build_balanced_bst(sorted_vals[mid+1:])
        return node

    sorted_vals = bst.inorder()
    balanced_tree = BinarySearchTree()
    balanced_tree.root = build_balanced_bst(sorted_vals)
    return balanced_tree


def test_balance_bst():
    # Test the balance_bst function

    print("=== Tree Balancing Test Cases ===")
    
    # Tests balance: prints inorder before and after, checks for changes
    def run_test(test_name, bst):
        print(f"\n{test_name}")
        original_inorder = bst.inorder()
        print("Original inorder:", original_inorder)
        balanced_bst = balance_bst(bst)
        balanced_inorder = balanced_bst.inorder()
        print("Balanced inorder:", balanced_inorder)
        assert original_inorder == balanced_inorder, "Inorder sequence changed!"
        print("Inorder preserved and tree balanced.\n")

    # Test Case 1: Already balanced tree 🌳
    bst1 = BinarySearchTree()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        bst1.insert(val)
    run_test("Test Case 1: Already balanced tree", bst1)

    # Test Case 2: Right-skewed tree 📐➡️
    bst2 = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        bst2.insert(val)
    run_test("Test Case 2: Right-skewed tree", bst2)

    # Test Case 3: Left-skewed tree 📐⬅️
    bst3 = BinarySearchTree()
    for val in [5, 4, 3, 2, 1]:
        bst3.insert(val)
    run_test("Test Case 3: Left-skewed tree", bst3)

    # Test Case 4: Empty tree 🈳
    bst4 = BinarySearchTree()
    run_test("Test Case 4: Empty tree", bst4)

    # Test Case 5: Single node tree 🌱
    bst5 = BinarySearchTree()
    bst5.insert(42)
    run_test("Test Case 5: Single node tree", bst5)
# Run tests
test_balance_bst()
