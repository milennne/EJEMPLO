class TreeNode:
    """Basic node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    """Perform level order traversal of a binary tree."""
    if not root:
        return []

    result = []     
    queue = [root]              

    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


def test_level_order_traversal():
    # Test Case 1: Full binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7

    print("Full binary tree")  
    print("Result:",level_order_traversal(root))  # Expected output: [1, 2, 3, 4, 5, 6, 7]

    # Test Case 2: Tree with only left children
    left_only = TreeNode(1)
    left_only.left = TreeNode(2)
    left_only.left.left = TreeNode(3)
    left_only.left.left.left = TreeNode(4)
    #     1
    #    /
    #   2
    #  /
    # 3
    #/
    #4
    print("\nTree with only left children")  
    print("Result:",level_order_traversal(left_only))  # Expected output: [1, 2, 3, 4]

    # Test Case 3: Tree with only right children
    right_only = TreeNode(1)                                                           
    right_only.right = TreeNode(2)
    right_only.right.right = TreeNode(3)
    right_only.right.right.right = TreeNode(4)
    # 1
    #  \
    #   2
    #    \
    #     3
    #      \
    #       4
    print("\nTree with only right children")  
    print("Result:",level_order_traversal(right_only))  # Expected output: [1, 2, 3, 4]


if __name__ == "__main__":
    test_level_order_traversal()