class GenericTreeNode:
    """Node for generic tree with multiple children."""

    def __init__(self, value):
        self.value = value  # 📊 Data stored in node
        self.children = []  # 👶 List of child nodes

    def add_child(self, child):
        """Add a child node."""
        self.children.append(child)  # ➕ Add to children list

    def remove_child(self, child):
        """Remove a child node."""
        self.children.remove(child)  # ➖ Remove from children list

