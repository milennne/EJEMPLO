class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate_expression_tree(root):
    """Evaluate an expression tree and return the result"""
    
    if root is None:
        return 0  # Empty tree → treated as 0

    # If the node is a leaf (number), return its value as an integer
    if root.left is None and root.right is None:
        return int(root.value)
    
    # Recursively evaluate the left and right children
    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)

    # Apply the operation based on the node's value
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val // right_val  # Integer division
    else:
        raise ValueError(f"Unknown operator: {root.value}")

# ✅ Test cases
# Test 1: Simple addition
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(evaluate_expression_tree(node1) == 5)  # ➕ Basic addition

# Test 2: Multiplication
node2 = Node('*')
node2.left = Node('4')
node2.right = Node('5')
print(evaluate_expression_tree(node2) == 20)  # ✖️ Multiplication

# Test 3: Combined operations
node3 = Node('+')
node3.left = Node('2')
node3.right = Node('*')
node3.right.left = Node('3')
node3.right.right = Node('4')
print(evaluate_expression_tree(node3) == 14)  # 🔢 Combined operations

# Test 4: Division
node4 = Node('/')
node4.left = Node('8')
node4.right = Node('4')
print(evaluate_expression_tree(node4) == 2)  # ➗ Division

# Test 5: Complex tree
node5 = Node('*')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('1')
node5.left.right = Node('2')
node5.right.left = Node('8')
node5.right.right = Node('3')
print(evaluate_expression_tree(node5) == 15)  # 🧮 Complex calculation
