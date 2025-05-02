class TreeNode:
    """Basic node in a binary tree."""
    
    def __init__(self, value):
        self.value = value       # 📊 Data stored in the node
        self.left = None         # 👈 Reference to left child
        self.right = None        # 👉 Reference to right child

def is_balanced(root):
    """Check if a binary tree is balanced (height difference between subtrees ≤ 1)."""

    def check_height(node):
        """Helper function that returns (is_balanced, height)."""
        # Base case: empty subtree is balanced with height -1
        if not node:
            return True, -1

        # Check left subtree
        left_balanced, left_height = check_height(node.left)
        if not left_balanced:
            return False, 0

        # Check right subtree
        right_balanced, right_height = check_height(node.right)
        if not right_balanced:
            return False, 0

        # Check balance at current node
        is_balanced_here = abs(left_height - right_height) <= 1
        height_here = max(left_height, right_height) + 1

        return is_balanced_here, height_here

    # Call the helper function and return the balanced status
    balanced, _ = check_height(root)
    return balanced

def test_is_balanced():
    print("🔧 TEST: is_balanced with different tree structures")

    # ✅ Test 1: Balanced tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(6)
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    print("🟢 Test 1 (Balanced):", is_balanced(root1))  # Expected: True

    # ❌ Test 2: Unbalanced tree (right-heavy)
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    root2.right.right = TreeNode(3)
    root2.right.right.right = TreeNode(4)
    # Tree structure:
    #   1
    #    \
    #     2
    #      \
    #       3
    #        \
    #         4
    print("🔴 Test 2 (Unbalanced):", is_balanced(root2))  # Expected: False

    # ⚖️ Test 3: Single node (trivially balanced)
    root3 = TreeNode(42)
    print("🟡 Test 3 (Single Node):", is_balanced(root3))  # Expected: True

test_is_balanced()