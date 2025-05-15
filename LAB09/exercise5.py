class ExpressionNode:
    """Node for expression tree."""

    def __init__(self, value):
        self.value = value    # 📊 Operator or operand
        self.left = None      # 👈 Left operand
        self.right = None     # 👉 Right operand

    def is_operator(self):
        """Check if node contains an operator."""
        return self.value in ['+', '-', '*', '/']  # 🔣 Check operators

class ExpressionTree:
    """Expression tree implementation"""
    
    def __init__(self, root=None):
        self.root = root
    
    def simplify(self):
        """Simplify the expression tree."""
        self.root = self._simplify_helper(self.root)

    def _simplify_helper(self, node):
        """Helper method for simplification."""
        if node is None:
            return None

        # If leaf node (operand) 🍃
        if not node.is_operator():
            return node

        # Recursively simplify children 🔄
        node.left = self._simplify_helper(node.left)
        node.right = self._simplify_helper(node.right)

        # If both children are constants, evaluate 🧮
        if (node.left and not node.left.is_operator() and
                node.right and not node.right.is_operator()):
            try:
                left_val = float(node.left.value)
                right_val = float(node.right.value)

                # Evaluate operation 🔣
                result = 0
                if node.value == '+':
                    result = left_val + right_val  # ➕
                elif node.value == '-':
                    result = left_val - right_val  # ➖
                elif node.value == '*':
                    result = left_val * right_val  # ✖️
                elif node.value == '/':
                    if right_val != 0:
                        result = left_val / right_val  # ➗
                    else:
                        return node  # Keep division by zero

                # Create new node with result 📊
                new_node = ExpressionNode(
                    str(int(result) if result == int(result) else result))
                return new_node
            except ValueError:
                # One of the values is not a number (variable) 🔤
                return node

        return node


def test_simplify():
    # ✅ Test cases
    # Test 1: All constants
    # Input: (2 + 3)
    # Tree:    +        Result: 5
    #         / \
    #        2   3
    const_tree = ExpressionTree()
    const_tree.root = ExpressionNode('+')
    const_tree.root.left = ExpressionNode('2')
    const_tree.root.right = ExpressionNode('3')
    const_tree.simplify()
    print(const_tree.root.value == '5' and const_tree.root.left is None and const_tree.root.right is None)  # 🔢 Single node

    # Test 2: Partial simplification
    # Input: (2 + 3) * x
    # Tree:    *         Result: *
    #         / \               / \
    #        +   x             5   x
    #       / \
    #      2   3
    partial_tree = ExpressionTree()
    partial_tree.root = ExpressionNode('*')
    add = ExpressionNode('+')
    add.left, add.right = ExpressionNode('2'), ExpressionNode('3')
    partial_tree.root.left = add
    partial_tree.root.right = ExpressionNode('x')
    partial_tree.simplify()
    print(partial_tree.root.value == '*' and partial_tree.root.left.value == '5' and partial_tree.root.right.value == 'x')  # ✨ Partial

    # Test 3: No simplification possible
    # Input: x + y
    # Tree:    +         Result: + (unchanged)
    #         / \               / \
    #        x   y             x   y
    no_simp_tree = ExpressionTree()
    no_simp_tree.root = ExpressionNode('+')
    no_simp_tree.root.left = ExpressionNode('x')
    no_simp_tree.root.right = ExpressionNode('y')
    no_simp_tree.simplify()
    print(no_simp_tree.root.value == '+' and no_simp_tree.root.left.value == 'x' and no_simp_tree.root.right.value == 'y')  # 🔤 No change

    # Test 4: Complex nested simplification
    # Input: ((2 * 3) + (8 / 4))
    # Tree:      +          Result: 8
    #          /   \
    #         *     /
    #        / \   / \
    #       2   3 8   4
    complex_tree = ExpressionTree()
    complex_tree.root = ExpressionNode('+')
    mult = ExpressionNode('*')
    div = ExpressionNode('/')
    mult.left, mult.right = ExpressionNode('2'), ExpressionNode('3')
    div.left, div.right = ExpressionNode('8'), ExpressionNode('4')
    complex_tree.root.left, complex_tree.root.right = mult, div
    complex_tree.simplify()
    print(complex_tree.root.value == '8' and complex_tree.root.left is None)  # 🎯 Fully simplified

    # Test 5: Mixed variables and constants
    # Input: x * (6 / 2)
    # Tree:    *         Result: *
    #         / \               / \
    #        x   /             x   3
    #           / \
    #          6   2
    mixed_tree = ExpressionTree()
    mixed_tree.root = ExpressionNode('*')
    div = ExpressionNode('/')
    div.left, div.right = ExpressionNode('6'), ExpressionNode('2')
    mixed_tree.root.left = ExpressionNode('x')
    mixed_tree.root.right = div
    mixed_tree.simplify()
    print(mixed_tree.root.value == '*' and mixed_tree.root.left.value == 'x' and mixed_tree.root.right.value == '3')  # 🔄 Right simplified

test_simplify()