class TreeNode:
    def __init__(self, val=0):
        self.val = val       # Value of the node
        self.left = None    # Left child
        self.right = None   # Right child

def tree_height(root):
    if root is None:
        return -1
   
    # Recursively find the height of left and right subtrees
    left_height = tree_height(root.left )
    right_height = tree_height(root.right)


    # Height is 1 + the maximum of the two subtrees
    return 1 + max(left_height, right_height)

def test_tree_height():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(tree_height(root))  # Expected: 2

    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5

    # Test Case 2: Empty tree
    empty_tree = None
    print(tree_height(empty_tree))  # Expected: -1

    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    print(tree_height(single_node))  # Expected: 0

    # Test Case 4: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    print(tree_height(left_skewed))  # Expected: 3
   
    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    print(tree_height(perfect))  # Expected: 2

test_tree_height()