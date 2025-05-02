class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # Left child
        self.right = None  # Right child

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)
            count_leaves(2)+count_leave(3)
            count_leave(4)+count_leave(5)+count_leave(3)
            1+1+1=3


#         1
#        /\ 
#       2  3
#       /\
#      4  5

 
# Test function
def test_count_leaves():
    # Test 1: Normal tree (leaves: 4, 5, 3)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    result1 = count_leaves(root)
    print(f"Test 1 - {result1}")
    assert result1 == 3

    # Test 2: Empty tree
    empty_tree = None
    result2 = count_leaves(empty_tree)
    print(f"Test 2 - {result2}")
    assert result2 == 0

    # Test 3: Single node
    single_node = TreeNode(1)
    result3 = count_leaves(single_node)
    print(f"Test 3 - {result3}")
    assert result3 == 1

    # Test 4: Only root has children
    no_leaves_at_first = TreeNode(1)
    no_leaves_at_first.left = TreeNode(2)
    no_leaves_at_first.right = TreeNode(3)
    result4 = count_leaves(no_leaves_at_first)
    print(f"Test 4 - {result4}")
    assert result4 == 2

    # Test 5: All nodes except root are leaves
    all_leaves = TreeNode(1)
    all_leaves.left = TreeNode(2)
    all_leaves.right = TreeNode(3)
    all_leaves.left.left = TreeNode(4)
    all_leaves.left.right = TreeNode(5)
    all_leaves.right.left = TreeNode(6)
    all_leaves.right.right = TreeNode(7)
    result5 = count_leaves(all_leaves)
    print(f"Test 5 - {result5}")
    assert result5 == 4

    print("All tests passed successfully.")

test_count_leaves()
