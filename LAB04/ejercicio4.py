class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def type(self, char):
        self.history.append(self.text)
        self.text += char

    def delete(self):
        if self.text:
            self.history.append(self.text)
            self.text = self.text[:-1]

    def undo(self):
        if self.history:
            self.text = self.history.pop()

    def get_text(self):
        return self.text


# Ejemplo de uso
editor = TextEditor()

editor.type('H')
editor.type('o')
editor.type('l')
editor.type('a')
print(editor.get_text())  # Hola

editor.delete()
print(editor.get_text())  # Hol

editor.undo()
print(editor.get_text())  # Hola


editor = TextEditor()

editor.type('A')
editor.type('D')
editor.type('I')
editor.type('O')
editor.type('S')
print(editor.get_text())  # Hello

editor.undo()
print(editor.get_text())  # Hell

editor.undo()
print(editor.get_text())  # Hel

editor.undo()
print(editor.get_text())  # He
