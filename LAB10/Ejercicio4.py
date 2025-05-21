class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    # If the current node is None, return an empty list (base case)
    if node is None:
        return []
    # Recursively traverse the left subtree, then visit the current node,
    # then recursively traverse the right subtree and combine the results
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)

def preorder_traversal(node):
    # If the current node is None, return an empty list (base case)
    if node is None:
        return []
    # Visit the current node first, then recursively traverse the left subtree,
    # then recursively traverse the right subtree and combine the results
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)

def postorder_traversal(node):
    # If the current node is None, return an empty list (base case)
    if node is None:
        return []
    # Recursively traverse the left subtree, then the right subtree,
    # and finally visit the current node, combining the results
    return postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value]



# Test 1: Simple expression tree
node1 = Node('+')              # Create root node with value '+'
node1.left = Node('2')         # Left child with value '2'
node1.right = Node('3')        # Right child with value '3'
print(inorder_traversal(node1) == ['2', '+', '3'])     # Inorder: left-root-right
print(preorder_traversal(node1) == ['+', '2', '3'])    # Preorder: root-left-right
print(postorder_traversal(node1) == ['2', '3', '+'])   # Postorder: left-right-root

# Test 2: More complex tree with nested subtree
node2 = Node('+')              # Root node '+'
node2.left = Node('*')         # Left child '*'
node2.right = Node('5')        # Right child '5'
node2.left.left = Node('2')    # Left child of '*' is '2'
node2.left.right = Node('3')   # Right child of '*' is '3'
print(inorder_traversal(node2) == ['2', '*', '3', '+', '5'])     # Inorder: left-root-right
print(preorder_traversal(node2) == ['+', '*', '2', '3', '5'])    # Preorder: root-left-right
print(postorder_traversal(node2) == ['2', '3', '*', '5', '+'])   # Postorder: left-right-root

# Test 3: Single node tree (no children)
node3 = Node('X')              # Single node 'X'
print(inorder_traversal(node3) == ['X'])     # Inorder: just the node
print(preorder_traversal(node3) == ['X'])    # Preorder: just the node
print(postorder_traversal(node3) == ['X'])   # Postorder: just the node