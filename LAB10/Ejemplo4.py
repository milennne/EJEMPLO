class Node:
    def __init__(self, value):
        # Initialize a new node with a given value
        self.value = value
        # Set left child to None initially
        self.left = None
        # Set right child to None initially
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
