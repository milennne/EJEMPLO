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
editor.type('d')
editor.type('i')
editor.type('o')
editor.type('s')
print(editor.get_text())  # Adios

editor.undo()
print(editor.get_text())  # Adio

editor.undo()
print(editor.get_text())  # Adi

editor.undo()
print(editor.get_text())  # Ad


editor = TextEditor()

editor.type('M')
editor.type('o')
editor.type('n')
editor.type('g')
editor.type('o')
editor.type('D')
editor.type('B')
print(editor.get_text())  # MongoDB

editor.delete()
editor.delete()
print(editor.get_text())  # Mongo

editor.undo()
print(editor.get_text())  # MongoD

editor.undo()
print(editor.get_text())  # MongoDB
