from node import Node

class LinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        self.head = None
        self.length = 0


    def insert_at_end(self, data):
        """Insert a new node with data at the end of the list."""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            
            # Traverse to the last node
            while current.get_next() is not None:
                current = current.get_next()
            
            current.set_next(new_node)
        
        self.length += 1
        return True




# Create an empty linked list
linked_list = LinkedList()

# Insert an element at the end (empty list)
linked_list.insert_at_end(10)

# Display the list
current = linked_list.head
while current:
    print(current.get_data(), end=" -> " if current.get_next() else " -> None\n")
    current = current.get_next()




# Create a linked list with a single node
linked_list = LinkedList()
linked_list.insert_at_end(10)

# Insert a second node at the end
linked_list.insert_at_end(2)

# Display the list
current = linked_list.head
while current:
    print(current.get_data(), end=" -> " if current.get_next() else " -> None\n")
    current = current.get_next()




# Create a linked list with three nodes
linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)

# Display the list
current = linked_list.head
while current:
    print(current.get_data(), end=" -> " if current.get_next() else " -> None\n")
    current = current.get_next()

# Expected output: 10 -> 2 -> 3 -> None
