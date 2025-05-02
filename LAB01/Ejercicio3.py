class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [] 

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None
stack = MinStack()
stack.push(3)
stack.push(5)
print(stack.getMin())
stack.push(2)
stack.push(2)
print(stack.getMin())
stack.pop()
print(stack.getMin())
stack.pop()
print(stack.getMin())
