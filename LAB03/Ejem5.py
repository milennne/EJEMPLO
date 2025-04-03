from node import Node


class LinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        """Insert a new node with data at the beginning of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

        self.length += 1
        return True


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

    def insert_at_position(self, position, data):
        """Insert a new node at the specified position (0-based)."""
        # Check if position is valid
        if position < 0 or position > self.length:
            return False

        # Insert at the beginning
        if position == 0:
            return self.insert_at_beginning(data)

        # Insert at the end
        if position == self.length:
            return self.insert_at_end(data)

        # Insert at the middle
        new_node = Node(data)
        current = self.head
        count = 0

        # Traverse to the node just before the insertion point
        while count < position - 1:
            current = current.get_next()
            count += 1

        new_node.set_next(current.get_next())
        current.set_next(new_node)

        self.length += 1
        return True
    


# Create an empty linked list
linked_list = LinkedList()

# Try to insert at position 0 (the only valid option in an empty list)
linked_list.insert_at_position(0, 10)

# Display the list after insertion
current = linked_list.head
while current:
    print(current.get_data(), end=" -> " if current.get_next() else " -> None\n")
    current = current.get_next()

# Expected output: 10 -> None



# Create a list with three nodes
linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

# Insert at position 0 (at the beginning)
linked_list.insert_at_position(0, 5)

# Display the list after insertion
current = linked_list.head
while current:
    print(current.get_data(), end=" -> " if current.get_next() else " -> None\n")
    current = current.get_next()

# Expected output: 5 -> 10 -> 20 -> 30 -> None




# Create a list with three nodes
linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

# Insert at position 1 (in the middle)
linked_list.insert_at_position(1, 15)

# Display the list after insertion
current = linked_list.head
while current:
    print(current.get_data(), end=" -> " if current.get_next() else " -> None\n")
    current = current.get_next()

# Expected output: 10 -> 15 -> 20 -> 30 -> None
