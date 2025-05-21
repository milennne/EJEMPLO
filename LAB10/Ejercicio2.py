class ExpressionNode:
    """Node for expression tree."""

    def __init__(self, value):
        self.value = value    # 📊 Operator or operand
        self.left = None      # 👈 Left operand
        self.right = None     # 👉 Right operand

    def is_operator(self):
        """Check if node contains an operator."""
        return self.value in ['+', '-', '*', '/']  # 🔣 Check operators



def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation."""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}  # 📊 Operator precedence
    stack = []  # 📚 Operator stack
    postfix = []  # 📝 Result    

    for token in tokens:
        if token not in precedence and token not in '()':
            postfix.append(token)  # 🔢 Add operand
        elif token == '(':
            stack.append(token)  # 📥 Push (
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())  # 📤 Pop operators
            stack.pop()  # Remove (
        else:
            while (stack and stack[-1] != '(' and
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                postfix.append(stack.pop())  # 📤 Pop higher precedence
            stack.append(token)  # 📥 Push operator

    while stack:
        postfix.append(stack.pop())  # 📤 Pop remaining

    return postfix


class ExpressionTree:
    """Build expression tree from infix notation."""
    def __init__(self):
        self.root = None
    @classmethod
    def from_infix(cls, tokens):
        """Build expression tree from infix notation."""
        obj = cls()
        postfix = infix_to_postfix(tokens)  # Convert to postfix first 🔄
        stack = []  # 📚 Stack for building tree

        for token in postfix:
            node = ExpressionNode(token)

            if node.is_operator():
                node.right = stack.pop()  # 👉 Right operand
                node.left = stack.pop()   # 👈 Left operand

            stack.append(node)  # 📥 Push to stack

        obj.root = stack.pop()  # 🌱 Final node is root
        return obj

# ✅ Test cases
# Test 1: Simple addition
# Input: 2 + 3
# Tree:    +
#         / \
#        2   3
tree1 = ExpressionTree.from_infix(['2', '+', '3'])
print(tree1.root.value == '+' and tree1.root.left.value == '2' and tree1.root.right.value == '3')  # 🌱 Simple tree

# Test 2: Operator precedence
# Input: 2 + 3 * 4
# Tree:    +
#         / \
#        2   *
#           / \
#          3   4
tree2 = ExpressionTree.from_infix(['2', '+', '3', '*', '4'])
print(tree2.root.value == '+' and tree2.root.right.value == '*')  # 📊 Precedence structure

# Test 3: Parentheses change structure
# Input: (2 + 3) * 4
# Tree:    *
#         / \
#        +   4
#       / \
#      2   3
tree3 = ExpressionTree.from_infix(['(', '2', '+', '3', ')', '*', '4'])
print(tree3.root.value == '*' and tree3.root.left.value == '+')  # 🔗 Parentheses effect