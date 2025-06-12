class AVLNode:
    def __init__(self, key):
        # Initialize a node with a key and default height of 1
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def rotate_left(self, z):
        # Perform a left rotation on node z
        y = z.right              # y becomes the new root after rotation
        T2 = y.left              # Save y's left subtree to attach later

        # Rotation
        y.left = z               # z becomes the left child of y
        z.right = T2             # T2 becomes the right child of z

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y                 # Return new root

    def rotate_right(self, z):
        # Perform a right rotation on node z
        y = z.left               # y becomes the new root after rotation
        T3 = y.right             # Save y's right subtree to attach later

        # Rotation
        y.right = z              # z becomes the right child of y
        z.left = T3              # T3 becomes the left child of z

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y                 # Return new root

    def get_height(self, node):
        # Utility function to return the height of a node
        return node.height if node else 0

# 🧪 Test rotations
def test_rotations():
    tree = AVLTree()

    # Test 1: Simple left rotation should convert [10, 20, 30] to [20, 10, 30]
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z = tree.rotate_left(z)
    print("🧪 Test 1:", z.key == 20)

    # Test 2: Simple right rotation should convert [30, 20, 10] to [20, 10, 30]
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    z = tree.rotate_right(z)
    print("🧪 Test 2:", z.key == 20)

    # Test 3: Check height values after left rotation
    # After rotation: root=20 (height=2), left=10 (h=1), right=30 (h=1)
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z = tree.rotate_left(z)
    test3 = z.height == 2 and z.left.height == 1 and z.right.height == 1
    print("🧪 Test 3:", test3)

    # Test 4: Check height values after right rotation
    # After rotation: root=20 (height=2), left=10 (h=1), right=30 (h=1)
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    z = tree.rotate_right(z)
    test4 = z.height == 2 and z.left.height == 1 and z.right.height == 1
    print("🧪 Test 4:", test4)

    # Test 5: Confirm correct child structure after right rotation
    # Should result in root=20, with left=10 and right=30
    test5 = z.key == 20 and z.left.key == 10 and z.right.key == 30
    print("🧪 Test 5:", test5)

# 🚀 Run all tests
test_rotations()
