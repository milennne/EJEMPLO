
import re #EXERCISE 5

def is_balanced(expression):
    """Check if an expression has balanced parentheses, brackets, and braces."""
    stack = []
    opening = "({["
    closing = ")}]"
    
    # Dictionary to match opening and closing brackets
    brackets_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:  # Stack is empty but we found a closing bracket
                return False
            
            top = stack.pop()
            if top != brackets_map[char]:
                return False
    
    # If stack is empty, all brackets were matched
    return len(stack) == 0


def test_balanced_parentheses():
    """Test parentheses balancing with various expressions."""
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("([])", True),
        ("([)]", False),
        ("{[]}", True),
        (")(", False),
        ("((((", False),
        ("))))", False),
        ("a*(b+c)-(d/e)", True)
    ]
    
    print("Testing parentheses balancing:")
    for expr, expected in test_cases:
        result = is_balanced(expr)
        print(f"Expression: '{expr}', Balanced: {result}, Expected: {expected}")
        assert result == expected, f"Test failed for '{expr}'"
    
    print("All balanced parentheses tests passed!")

#EXERCISE 5


def is_html_balanced(html):
    """Check if HTML tags are properly balanced using a stack."""
    stack = []


    tags = re.findall(r'</?[^>]+>', html)

    for tag in tags:
        if not tag.startswith('</'):
            tag_name = tag[1:].split()[0].rstrip('>')
            stack.append(tag_name)
        else:
            tag_name = tag[2:].rstrip('>')
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()

    return len(stack) == 0

def test_html_balancer():
    test_cases = [
        ("<html><body><h1>Title</h1></body></html>", True),
        ("<div><p>Hello</p></div>", True),
        ("<div><p>Hello</div></p>", False),
        ("<div><span>Hola</span><br/></div>", True),  
        ("<div><span></div></span>", False),
        ("<ul><li>Item 1</li><li>Item 2</li></ul>", True),
        ("<div><p><em>Test</em></p></div>", True),
        ("<div><p><em>Test</p></em></div>", False)
    ]

    print("Testing HTML tag balancing:")
    for html, expected in test_cases:
        result = is_html_balanced(html)
        print(f"HTML: {html}\n→ Balanced? {result} | Expected: {expected}\n")




# Example usage
if __name__ == "__main__":
    test_balanced_parentheses()
    test_html_balancer()
