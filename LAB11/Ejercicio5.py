# ✅ Tree node (also used as a node for the doubly linked list)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # 🔙 Pointer to the previous node in the DLL
        self.right = None  # 🔜 Pointer to the next node in the DLL

# ✅ Binary Search Tree (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """🔧 Inserts a value into the BST"""
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
        """📥 Builds the BST from a list of values"""
        for v in values:
            self.insert(v)

    def bst_to_dll(self):
        """🔁 Converts the BST to a sorted circular doubly linked list (DLL)"""
        if not self.root:
            return None

        self.first = None  # 🟢 First node of the DLL
        self.last = None   # 🔴 Last visited node

        def inorder(node):
            if not node:
                return

            # 📥 Visit left subtree
            inorder(node.left)

            # 🔗 Link the current node with the last visited node
            if self.last:
                self.last.right = node  # last points to current
                node.left = self.last   # current points back
            else:
                self.first = node  # Store the first (smallest) node

            self.last = node  # Update the last visited node

            # 📤 Visit right subtree
            inorder(node.right)

        # 🔁 Inorder traversal of the BST
        inorder(self.root)

        # 🔄 Make the list circular
        self.first.left = self.last
        self.last.right = self.first

        return self.first  # 🔚 Return the head of the DLL

# ✅ Circular DLL validator
def validate_circular_dll(head, expected_values):
    if not head:
        return expected_values == []
    values = []
    current = head
    while True:
        values.append(current.value)
        current = current.right
        if current == head:  # Completed the cycle
            break
    return values == expected_values

# ✅ Test cases
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

# 🚀 Run tests
test_bst_to_dll()
