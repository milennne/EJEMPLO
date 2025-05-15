def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation"""
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

def test_infix_to_postfix() :
    print("\n--- Challenge 1: Infix to Postfix ---")
    test_cases_1 = [
        (['2', '+', '3'], ['2', '3', '+']),
        (['2', '+', '3', '*', '4'], ['2', '3', '4', '*', '+']),
        (['(', '2', '+', '3', ')', '*', '4'], ['2', '3', '+', '4', '*']),
        (['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')'],
         ['1', '2', '+', '3', '4', '-', '*']),
        (['a', '+', 'b', '*', 'c', '/', 'd'],
         ['a', 'b', 'c', '*', 'd', '/', '+']),
    ]

    for infix, expected in test_cases_1:
        result = infix_to_postfix(infix)
        status = "✅" if result == expected else "❌"
        print(
            f"Infix: {' '.join(infix)} => Postfix: {' '.join(result)} {status}")


test_infix_to_postfix()
