class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1

class AVLTree:

    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def balance(self, node):
        return 0 if node is None else (self.get_height(node.left) - self.get_height(node.right))
    
    def rotate_left(self, node):
        y = node.right
         

        y.left = node
        node.right = None

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        return y
    
    def rotate_right(self, node):
        y = node.left 
        

        y.right = node
        node.left = None

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        return y
        
        


    def insert(self, node, key):
        if node is None:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node

            

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.balance(node)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def inorder(self, root):
        """📜 In-order traversal"""
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
    
    
# 🧪 Test cases
def test_avl_insert():
    avl = AVLTree()

    root = None
    for val in [10, 20, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1 (RR):", end=" ")
    avl.inorder(root)  # Expected: 10 20 30
    print()

    avl = AVLTree()
    root = None
    for val in [30, 20, 10]:
        root = avl.insert(root, val)
    print("🧪 Test 2 (LL):", end=" ")
    avl.inorder(root)  # Expected: 10 20 30
    print()

    avl = AVLTree()
    root = None
    for val in [30, 10, 20]:
        root = avl.insert(root, val)
    print("🧪 Test 3 (LR):", end=" ")
    avl.inorder(root)  # Expected: 10 20 30
    print()

    avl = AVLTree()
    root = None
    for val in [10, 30, 20]:
        root = avl.insert(root, val)
    print("🧪 Test 4 (RL):", end=" ")
    avl.inorder(root)  # Expected: 10 20 30
    print()

    avl = AVLTree()
    root = None
    for val in [15, 10, 20, 25, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 5 (Balanced):", end=" ")
    avl.inorder(root)  # Expected: 10 15 20 25 30
    print()

# 🚀 Run all tests
test_avl_insert()
