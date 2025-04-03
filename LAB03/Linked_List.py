from node import Node


class LinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        self.head = None
        self.length = 0

    def display(self):
        """Return a string representation of the linked list."""
        if self.head is None:
            return "Empty list"

        current = self.head
        result = ""

        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()

        return result + "None"
    
    def list_length(self):
        """Count and return the number of nodes in the list."""
        count = 0
        current = self.head
        
        while current is not None:
            count += 1
            current = current.get_next()
        
        return count
    
    
    
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
    
    def delete_from_beginning(self):
        """Delete and return the data from the first node."""
        if self.head is None:
            return None
        
        data = self.head.get_data()
        self.head = self.head.get_next()
        self.length -= 1
        
        return data
    
    def delete_from_end(self):
        """Delete and return the data from the last node."""
        if self.head is None:
            return None
        
        # If there's only one node
        if self.head.get_next() is None:
            data = self.head.get_data()
            self.head = None
            self.length -= 1
            return data
        
        current = self.head
        
        # Traverse to the second-to-last node
        while current.get_next().get_next() is not None:
            current = current.get_next()
        
        data = current.get_next().get_data()
        current.set_next(None)
        self.length -= 1
        
        return data
    
    def delete_from_position(self, position):
        """Delete and return data from node at the specified position."""
        # Check if position is valid
        if position < 0 or position >= self.length or self.head is None:
            return None
        
        # Delete from the beginning
        if position == 0:
            return self.delete_from_beginning()
        
        # Delete from the end
        if position == self.length - 1:
            return self.delete_from_end()
        
        # Delete from the middle
        current = self.head
        count = 0
        
        # Traverse to the node just before the deletion point
        while count < position - 1:
            current = current.get_next()
            count += 1
        
        node_to_delete = current.get_next()
        data = node_to_delete.get_data()
        
        current.set_next(node_to_delete.get_next())
        self.length -= 1
        
        return data
    
    def search(self, data):
        """Find the position of data in the list, or return -1 if not found."""
        if self.head is None:
            return -1
        
        current = self.head
        position = 0
        
        while current is not None:
            if current.get_data() == data:
                return position
            current = current.get_next()
            position += 1
        
        return -1



