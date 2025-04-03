from node import Node

class LinkedList:
    """Class representing a singly linked list."""
    def __init__(self):
        self.head = None

    def display(self):
        """Returns a string representation of the linked list."""
        if self.head is None:
            return "Empty list"
        
        current = self.head
        result = ""
        
        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()
        
        return result + "None"

    def list_length(self):
        """Counts and returns the number of nodes in the list."""
        count = 0
        current = self.head
        
        while current is not None:
            count += 1
            current = current.get_next()
        
        return count

# Test cases
lista = LinkedList()
print(lista.display())        # "Empty list"
print(lista.list_length())    # 0 (empty list)

lista.head = Node(10)
print(lista.display())        # "10 -> None"
print(lista.list_length())    # 1 (one node)

lista.head.set_next(Node(20))
lista.head.get_next().set_next(Node(30))
print(lista.display())        # "10 -> 20 -> 30 -> None"
print(lista.list_length())    # 3 (three nodes)
