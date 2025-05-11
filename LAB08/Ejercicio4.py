# Define the tree node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Class to build the tree from a list (level-order)
class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree_from_list(self, values):
        """Build a binary tree from a list of values in level order."""
        if not values:
            return

        self.root = TreeNode(values[0])
        queue = [self.root]
        i = 1

        while queue and i < len(values):
            current = queue.pop(0)

            # Left child
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            # Right child
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1


def vertical_order_traversal(root):
    if not root:
        return []

    column_table = {}  # key: horizontal distance, value: list of node values
    queue = [(root, 0)]  # simulate a queue with a list

    while queue:
        current = queue[0]
        node, hd = current
        queue = queue[1:]  # remove the first element (like popleft)

        if hd in column_table:
            column_table[hd].append(node.value)
        else:
            column_table[hd] = [node.value]

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    result = []
    for hd in sorted(column_table):
        result.append(column_table[hd])
    return result



# Test function
def test_vertical_order_traversal():

    # Test Case 1
    print("Running tests...\n")
    print("Test Case 1")
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    print(vertical_order_traversal(tree1.root))  # [[4], [2], [1, 5], [3], [6]]
    print("\nTest Case 1")
    # Test Case 2
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, None, 3])
    print(vertical_order_traversal(tree2.root))  # [[3], [2], [1]]
    print("\nTest Case 1")
    # Test Case 3
    tree3 = BinaryTree()
    print(vertical_order_traversal(tree3.root))  # []

# Run tests
test_vertical_order_traversal()