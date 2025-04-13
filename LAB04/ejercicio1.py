class Stack:
    """Simple Stack implementation using a list."""
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
        
    def size(self):
        return len(self.items)


def reverse_string(input_str):
    stack = Stack()
    
    # Push each character to the stack
    for char in input_str:
        stack.push(char)
    
    # Pop all characters to get the reversed string
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str


# Test the function
if __name__ == "__main__":
    test_str = "hello world"
    print("Original:", test_str)
    print("Reversed:", reverse_string(test_str))

print(reverse_string("abc"))         # cba
print(reverse_string("12345"))       # 54321
print(reverse_string("stack"))       # kcats
