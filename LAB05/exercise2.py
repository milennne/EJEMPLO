class Node:
    """Node for a linked queue."""

    def __init__(self, data):
        """Initialize a node with data and no next reference."""
        self.data = data
        self.next = None


class LinkedQueue:
    """Queue implementation using a linked list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.front = None  # For dequeue operations ⬅️
        self.rear = None   # For enqueue operations ➡️
        self.size_count = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        new_node = Node(item)

        # If queue is empty, both front and rear point to the new node 🏁
        if self.is_empty():
            self.front = new_node
        else:
            # Link the new node at the end 🔗
            self.rear.next = new_node

        # Update rear to the new node ➡️
        self.rear = new_node
        self.size_count += 1
        return True

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")

        # Store the front node's data 📦
        item = self.front.data

        # Move front pointer to the next node ⬅️
        self.front = self.front.next

        # If queue becomes empty, update rear pointer too
        if self.front is None:
            self.rear = None

        self.size_count -= 1
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.front.data

    def size(self):
        """Return the number of items in the queue."""
        return self.size_count

    def __str__(self):
        """Return a string representation of the queue."""
        if self.is_empty():
            return "Queue: []"

        result = []
        current = self.front
        while current:
            result.append(str(current.data))
            current = current.next

        return f"Queue: [{', '.join(result)}]"

class TreeNode:
    """Node for a binary tree."""

    def __init__(self, value):
        """Initialize a tree node with value and empty children."""
        self.value = value
        self.left = None
        self.right = None


def level_order_traversal(root):
    """Perform level-order traversal of a binary tree."""
    if not root:
        return []

    result = []  # To store traversal result
    queue = LinkedQueue()  # Use our LinkedQueue implementation

    # Start with the root node 🌱
    queue.enqueue(root)

    while not queue.is_empty():
        # Get the next node to process
        node = queue.dequeue()

        # Add node's value to result
        result.append(node.value)

        # Enqueue left child if exists 👈
        if node.left:
            queue.enqueue(node.left)

        # Enqueue right child if exists 👉
        if node.right:
            queue.enqueue(node.right)

    return result


def test_level_order_traversal():
    """Test level-order traversal on a binary tree."""
    # Create a binary tree 🌳
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Binary Tree Structure:")
    print("       1")
    print("     /   \\")
    print("    2     3")
    print("   / \\   / \\")
    print("  4   5 6   7")

    # Perform level-order traversal
    traversal = level_order_traversal(root)

    print("\nLevel-order traversal result:")
    print(" -> ".join(map(str, traversal)))

    # Verify the result
    expected = [1, 2, 3, 4, 5, 6, 7]
    print(f"Expected: {expected}")
    print(f"Traversal correct: {traversal == expected} ✅")


test_level_order_traversal()