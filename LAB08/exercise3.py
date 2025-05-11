class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree_from_list(self, values):
        """Builds a binary tree from a list of values in level order."""
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = [self.root]
        i = 1
        while i < len(values):
            current = queue.pop(0)
            if current:
                if i < len(values) and values[i] is not None:
                    current.left = TreeNode(values[i])
                    queue.append(current.left)
                i += 1
                if i < len(values) and values[i] is not None:
                    current.right = TreeNode(values[i])
                    queue.append(current.right)
                i += 1

def node_exists(root, val):
    """Checks if a node with the given value exists in the tree."""
    if not root:
        return False
    if root.val == val:
        return True
    return node_exists(root.left, val) or node_exists(root.right, val)

def lowest_common_ancestor(root, p, q):
    """Finds the lowest common ancestor of two nodes in a binary tree."""
    if not root:
        return None
    if root.val == p or root.val == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right

def find_lca_with_check(root, p, q):
    """Finds the LCA only if both nodes exist in the tree."""
    if node_exists(root, p) and node_exists(root, q):
        return lowest_common_ancestor(root, p, q)
    return None

def test_lowest_common_ancestor():
    """Runs test cases for the LCA function."""

    # Test Case 1: Nodes in different subtrees
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    lca1 = find_lca_with_check(tree1.root, 4, 6)
    print("LCA of 4 and 6:", lca1.val if lca1 else "Not found")  # Expected: 1

    # Test Case 2: One node is ancestor of the other
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, 3, 4])
    lca2 = find_lca_with_check(tree2.root, 2, 4)
    print("LCA of 2 and 4:", lca2.val if lca2 else "Not found")  # Expected: 2

    # Test Case 3: Sibling nodes
    tree3 = BinaryTree()
    tree3.build_tree_from_list([1, 2, 3])
    lca3 = find_lca_with_check(tree3.root, 2, 3)
    print("LCA of 2 and 3:", lca3.val if lca3 else "Not found")  # Expected: 1

    # Test Case 4: One node is the root
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])
    lca4 = find_lca_with_check(tree4.root, 1, 3)
    print("LCA of 1 and 3:", lca4.val if lca4 else "Not found")  # Expected: 1

    # Test Case 5: Node does not exist
    lca5 = find_lca_with_check(tree4.root, 2, 99)
    print("LCA of 2 and 99:", lca5.val if lca5 else "Not found")  # Expected: Not found

# Run tests
test_lowest_common_ancestor()
