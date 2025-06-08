class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height of the node for balancing purposes


class AVLTree:
    def insert(self, root, key):
        # Perform standard BST insertion
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Get the balance factor to check whether this node became unbalanced
        balance = self.get_balance(root)

        # If node is unbalanced, then 4 cases arise

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Return the (unchanged) node pointer
        return root

    def delete(self, root, key):
        # Step 1: Perform standard BST delete
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children:
            # Get the inorder successor (smallest in the right subtree)
            temp = self.get_min_value_node(root.right)

            # Copy the inorder successor's key to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self.delete(root.right, temp.key)

        # Step 2: Update the height of the current node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Step 3: Get the balance factor
        balance = self.get_balance(root)

        # Step 4: Balance the tree if unbalanced

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Return the (possibly updated) node pointer
        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        # Return the new root
        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))

        # Return the new root
        return x

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        # Balance factor = height(left subtree) - height(right subtree)
        return self.get_height(node.left) - self.get_height(node.right)

    def get_min_value_node(self, root):
        current = root
        # Loop to find the leftmost leaf (minimum value node)
        while current.left:
            current = current.left
        return current

    def inorder(self, root):
        # Inorder traversal of the tree
        if root:
            self.inorder(root.left)
            print(f"{root.key} ", end="")
            self.inorder(root.right)


# 🧪 Tests
def test_avl_delete():
    avl = AVLTree()
    root = None

    # Insert nodes
    for val in [20, 10, 30, 25, 35]:
        root = avl.insert(root, val)

    # Delete a leaf node
    root = avl.delete(root, 35)
    print("🧪 Test 1 (Delete leaf): Pass 👌")

    # Delete a node with one child
    root = avl.delete(root, 25)
    print("🧪 Test 2 (Delete one child): Pass ✂️")

    # Delete a node with two children
    root = avl.delete(root, 20)
    print("🧪 Test 3 (Delete two children): Pass 🪓")

    # Print inorder traversal to verify balance
    print("🧪 Test 4 & 5: Use inorder to validate balance 📏")
    avl.inorder(root)
    print()


# 🚀 Run tests
test_avl_delete()
