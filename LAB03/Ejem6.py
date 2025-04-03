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




    def delete_from_beginning(self):
        """Delete and return the data from the first node."""
        if self.head is None:
            return None

        data = self.head.get_data()
        self.head = self.head.get_next()
        self.length -= 1

        return data
    

# Create an empty linked list
linked_list = LinkedList()

# Attempt to delete the first node
deleted_data = linked_list.delete_from_beginning()

# Display the result
print(f"Deleted data: {deleted_data}")  # Expected output: None
print(f"List after deletion: {linked_list.head}")  # Expected output: None



# Create a linked list with one node
linked_list = LinkedList()
linked_list.insert_at_end(10)

# Delete the first node
deleted_data = linked_list.delete_from_beginning()

# Display the result
print(f"Deleted data: {deleted_data}")  # Expected output: 10
print(f"List after deletion: {linked_list.head}")  # Expected output: None



# Create a linked list with three nodes
linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

# Delete the first node
deleted_data = linked_list.delete_from_beginning()

# Display the result
print(f"Deleted data: {deleted_data}")  # Expected output: 10

# Display the updated list
current = linked_list.head
while current:
    print(current.get_data(), end=" -> " if current.get_next() else " -> None\n")
    current = current.get_next()

# Expected output: 20 -> 30 -> None
