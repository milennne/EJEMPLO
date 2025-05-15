class GenericTreeNode:
    """Node of a generic tree"""
    def __init__(self, value):
        self.value = value
        self.children = []

class GenericTree:
    """Generic tree implementation"""
    
    def __init__(self, root=None):
        self.root = root
    
    def height(self):
        """Calculate the height of the tree"""
        def _height(node):
            if node is None:
                return -1  # Empty tree
            if not node.children:
                return 0  # Leaf node
            return 1 + max(_height(child) for child in node.children)
        
        return _height(self.root)

# ✅ Test cases
# Test 1: Empty tree
# Tree: None
empty_tree = GenericTree(None)
print(empty_tree.height() == -1)  # 📭 Empty tree

# Test 2: Single node
# Tree: A
single = GenericTree(GenericTreeNode('A'))
print(single.height() == 0)  # 🌱 Leaf node

# Test 3: Linear tree
# Tree: A → B → C
#       A
#       |
#       B
#       |
#       C
linear_root = GenericTreeNode('A')
linear_b = GenericTreeNode('B')
linear_c = GenericTreeNode('C')
linear_root.children = [linear_b]
linear_b.children = [linear_c]
linear_tree = GenericTree(linear_root)
print(linear_tree.height() == 2)  # 📏 Linear path

# Test 4: Balanced tree
# Tree:     A
#         / | \
#        B  C  D
#       /|\    |
#      E F G   H
balanced_root = GenericTreeNode('A')
b, c, d = GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D')
e, f, g, h = GenericTreeNode('E'), GenericTreeNode('F'), GenericTreeNode('G'), GenericTreeNode('H')
balanced_root.children = [b, c, d]
b.children = [e, f, g]
d.children = [h]
balanced_tree = GenericTree(balanced_root)
print(balanced_tree.height() == 2)  # 🌳 Balanced tree

# Test 5: Unbalanced tree
# Tree:     A
#          /
#         B
#        /
#       C
#      /
#     D
unbalanced_root = GenericTreeNode('A')
ub_b = GenericTreeNode('B')
ub_c = GenericTreeNode('C')
ub_d = GenericTreeNode('D')
unbalanced_root.children = [ub_b]
ub_b.children = [ub_c]
ub_c.children = [ub_d]
unbalanced_tree = GenericTree(unbalanced_root)
print(unbalanced_tree.height() == 3)  # 📈 Deep path
