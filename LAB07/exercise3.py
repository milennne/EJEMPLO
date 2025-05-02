class TreeNode:
    """Basic node in a binary tree."""
    
    def __init__(self, value):
        self.value = value       # 📊 Data stored in the node
        self.left = None         # 👈 Reference to left child
        self.right = None        # 👉 Reference to right child

class BinaryTree:
    """Binary tree implementation with basic traversals."""
    
    def __init__(self, root=None):
        self.root = root    # 🌱 Reference to the root node
    
    def preorder_traversal(self, node, result=None):
        """DLR: Process Data, then Left, then Right subtree."""
        if result is None:
            result = []
        
        if node:
            # Visit the node first (D)
            result.append(node.value)
            # Traverse left subtree (L)
            self.preorder_traversal(node.left, result)
            # Traverse right subtree (R)
            self.preorder_traversal(node.right, result)
        
        return result
    
    def inorder_traversal(self, node, result=None):
        """LDR: Process Left, then Data, then Right subtree."""
        if result is None:
            result = []
        
        if node:
            # Traverse left subtree (L)
            self.inorder_traversal(node.left, result)
            # Visit the node (D)
            result.append(node.value)
            # Traverse right subtree (R)
            self.inorder_traversal(node.right, result)
        
        return result
    
    def postorder_traversal(self, node, result=None):
        """LRD: Process Left, then Right, then Data."""
        if result is None:
            result = []
        
        if node:
            # Traverse left subtree (L)
            self.postorder_traversal(node.left, result)
            # Traverse right subtree (R)
            self.postorder_traversal(node.right, result)
            # Visit the node (D)
            result.append(node.value)
        
        return result
    
    def traverse(self, order="inorder"):
        """Traverse the tree in the specified order."""
        if order == "preorder":
            return self.preorder_traversal(self.root)
        elif order == "inorder":
            return self.inorder_traversal(self.root)
        elif order == "postorder":
            return self.postorder_traversal(self.root)
        else:
            raise ValueError("Invalid traversal order. Use 'preorder', 'inorder', or 'postorder'")
        
def create_sample_tree():
    """Create a sample binary tree for testing."""
    # Create the root node
    root = TreeNode(1)           # 🌱 Root
    
    # Level 1 nodes
    root.left = TreeNode(2)      # 👈 Left child
    root.right = TreeNode(3)     # 👉 Right child
    
    # Level 2 nodes
    root.left.left = TreeNode(4) # 👈👈 Left-left child
    root.left.right = TreeNode(5) # 👈👉 Left-right child
    root.right.right = TreeNode(6) # 👉👉 Right-right child
    
    # Our tree looks like:
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    
    return root

def mirror_tree(root):
    """Mirror a binary tree by swapping left and right children."""
    # Base case: empty tree or leaf node
    if not root:
        return

    # Swap left and right children
    root.left, root.right = root.right, root.left

    # Recursively mirror the subtrees
    mirror_tree(root.left)
    mirror_tree(root.right)

    return root     

def test_mirror_tree():
    print("🔧 TEST 1: mirror_tree with standard sample tree")
    root1 = create_sample_tree()
    tree1 = BinaryTree(root1)

    print("🟢 Inorder before mirroring:")
    print(tree1.traverse("inorder"))  # [4, 2, 5, 1, 3, 6]

    mirror_tree(root1)
    print("🔁 Inorder after mirroring:")
    print(tree1.traverse("inorder"))  # [6, 3, 1, 5, 2, 4]

    mirror_tree(root1)
    print("♻️ Inorder after restoring:")
    print(tree1.traverse("inorder"))  # [4, 2, 5, 1, 3, 6]
    print()

    print("🔧 TEST 2: mirror_tree with single-node tree")
    single_root = TreeNode(42)
    single_tree = BinaryTree(single_root)

    print("🟢 Inorder before mirroring:")
    print(single_tree.traverse("inorder"))  # [42]

    mirror_tree(single_root)
    print("🔁 Inorder after mirroring:")
    print(single_tree.traverse("inorder"))  # [42]
    print()

    print("🔧 TEST 3: mirror_tree with left-skewed tree")
    # Tree: 1 -> 2 -> 3 (all left)
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    tree3 = BinaryTree(root3)

    print("🟢 Inorder before mirroring:")
    print(tree3.traverse("inorder"))  # [3, 2, 1]

    mirror_tree(root3)
    print("🔁 Inorder after mirroring:")
    print(tree3.traverse("inorder"))  # [1, 2, 3]

test_mirror_tree()

