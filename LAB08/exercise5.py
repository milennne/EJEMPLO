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

    def prune(self, target):
            """Poda los subárboles que no contienen el valor objetivo."""
            def _prune(node):
                if node is None:
                    return None
                node.left = _prune(node.left)
                node.right = _prune(node.right)
                if node.value != target and node.left is None and node.right is None:
                    return None
                return node

            self.root = _prune(self.root)

def test_prune_tree():
    """Testea la función prune dentro de BinaryTree."""
    def run_test(name, tree_values, target, expected_output):
        print(f"\n{name}")
        tree = BinaryTree()
        tree.build_tree_from_list(tree_values)
        print("Original:")
        tree.print_tree()
        tree.prune(target)
        print("Pruned:")
        tree.print_tree()
        result = tree.level_order_traversal()
        if result == expected_output:
            print(f"✅ Passed: {result}")
        else:
            print(f"❌ Failed: got {result}, expected {expected_output}")

    run_test(
        "Test 1: Solo debe quedar el nodo raíz con valor 1 🌱",
        [1, 2, 3, 4, 5, None, 6],
        1,
        [1]
    )

    run_test(
        "Test 2: Mantener todos los caminos hacia nodos con valor 1 🛣️",
        [1, 2, 3, 1, 5, None, 1],
        1,
        [1, 2, 3, 1, 1]
    )

    run_test(
        "Test 3: Árbol vacío 🈳",
        [],
        1,
        []
    )

    run_test(
        "Test 4: Ningún nodo contiene 4 ❌",
        [1, 2, 3],
        4,
        []
    )

    run_test(
        "Test 5: Todos los nodos tienen valor 5 🎯",
        [5, 5, 5],
        5,
        [5, 5, 5]
    )
test_prune_tree()

