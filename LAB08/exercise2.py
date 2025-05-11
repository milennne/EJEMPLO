class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def preorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result

    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
        return result

    def level_order_traversal(self):
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def traverse(self, order="inorder"):
        if order == "preorder":
            return self.preorder_traversal(self.root)
        elif order == "inorder":
            return self.inorder_traversal(self.root)
        elif order == "postorder":
            return self.postorder_traversal(self.root)
        else:
            raise ValueError("Invalid traversal order. Use 'preorder', 'inorder', or 'postorder'")

    def build_tree_from_list(self, values):
        if not values:
            return
        self.root = TreeNode(values[0])
        queue = [self.root]
        i = 1
        while queue and i < len(values):
            current = queue.pop(0)
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

    def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        if node is None:
            print("Empty tree 🈳")
            return
        if node.right:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

    def serialize(self):
        """Serialize the binary tree to a string using level-order traversal."""
        if not self.root:
            return ""

        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current:
                result.append(str(current.value))  # ➕ Store node value
                queue.append(current.left)         # 👈 Add left child (can be None)
                queue.append(current.right)        # 👉 Add right child (can be None)
            else:
                result.append("null")              # 🚫 Mark null nodes explicitly

        # Remove trailing "null" entries to optimize output
        while result and result[-1] == "null":
            result.pop()

        return ",".join(result)  # 🔗 Use comma as delimiter

    def deserialize(self, data):
        """Deserialize a string back into a binary tree."""
        if not data:
            return None

        values = data.split(",")                 # 🔎 Split by delimiter
        self.root = TreeNode(int(values[0]))     # 🌱 Create root node
        queue = [self.root]
        i = 1

        while queue and i < len(values):
            current = queue.pop(0)

            # 👈 Process left child
            if values[i] != "null":
                current.left = TreeNode(int(values[i]))
                queue.append(current.left)
            i += 1

            # 👉 Process right child
            if i < len(values) and values[i] != "null":
                current.right = TreeNode(int(values[i]))
                queue.append(current.right)
            i += 1

        return self.root



def test_serialize_deserialize():
    """Test the serialize and deserialize functions. 💾"""

    def check(tree):
        """Helper: serialize, then deserialize, then serialize again and compare."""
        serialized = tree.serialize()
        new_tree = BinaryTree()
        new_tree.deserialize(serialized)
        return serialized == new_tree.serialize()  # ✅ Check consistency

    # Test Case 1: Normal binary tree 🌳
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    assert check(tree1), "Test Case 1 failed"

    # Test Case 2: Empty tree 🈳
    tree2 = BinaryTree()
    assert check(tree2), "Test Case 2 failed"

    # Test Case 3: Single node tree 🌱
    tree3 = BinaryTree()
    tree3.build_tree_from_list([42])
    assert check(tree3), "Test Case 3 failed"

    # Test Case 4: Left-skewed tree 📐⬅️
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, None, 3, None, None, None, 4])
    assert check(tree4), "Test Case 4 failed"

    # Test Case 5: Right-skewed tree 📐➡️
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4])
    assert check(tree5), "Test Case 5 failed"

    print("✅ All test cases passed!")

test_serialize_deserialize()
