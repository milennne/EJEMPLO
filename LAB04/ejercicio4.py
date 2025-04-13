class DynamicArrayStack:

    def __init__(self, initial_capacity=10):
        self.data = [None] * initial_capacity
        self.capacity = initial_capacity
        self.top = -1
    
    def is_empty(self):
        return self.top == -1
    
    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.top + 1):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
    
    def push(self, item):
        if self.top == self.capacity - 1:
            self.resize(2 * self.capacity)
        self.top += 1
        self.data[self.top] = item
        return True
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
        item = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        if 0 < self.top + 1 <= self.capacity // 4 and self.capacity > 10:
            self.resize(self.capacity // 2)
        return item
    


class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = DynamicArrayStack()

    def type_text(self, new_text):
        self.history.push(('type', new_text))
        self.text += new_text

    def delete(self, n):
        deleted = self.text[-n:]
        self.history.push(('delete', deleted))
        self.text = self.text[:-n]

    def undo(self):
        if self.history.is_empty():
            print("No undo operations.")
            return

        action, data = self.history.pop()
        if action == 'type':
            self.text = self.text[:-len(data)]
        elif action == 'delete':
            self.text += data

    def get_text(self):
        return self.text


editor = TextEditor()

editor.type_text("Hola")
print(editor.get_text())  #  "Hola"

editor.type_text(" mundo")
print(editor.get_text())  #  "Hola mundo"

editor.undo()
print(editor.get_text())  #  "Hola"

editor.undo()
print(editor.get_text())  #  ""



editor = TextEditor()

editor.type_text("Python es genial")
print(editor.get_text()) 

editor.delete(7)
print(editor.get_text()) 

editor.undo()
print(editor.get_text())  



editor = TextEditor()

editor.type_text("Aprendiendo")
editor.type_text(" estructuras")
editor.type_text(" de datos")
print(editor.get_text())  

editor.delete(10)
print(editor.get_text())  

editor.undo()
print(editor.get_text()) 

editor.undo()
print(editor.get_text())  

editor.undo()
print(editor.get_text()) 

editor.undo()
print(editor.get_text()) 
