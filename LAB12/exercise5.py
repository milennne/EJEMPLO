from collections import deque


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



        
    def print_level_order(self, root):
        """📡 Traverse the tree level by level and print key and height of each node"""
        
        if root is None: return  # 🕳️ If the tree is empty, exit early
        q = deque([root])        # 🚪 Start the queue with the root node

        while q:                 # 🔁 While there are nodes to visit...
            node = q.popleft()   # 🎯 Dequeue the next node (FIFO)
            print(f"{node.key}(h{node.height})", end=" ")  # 🖨️ Print key and height

            if node.left: q.append(node.left)    # 👈 If there's a left child, enqueue it
            if node.right: q.append(node.right)  # 👉 If there's a right child, enqueue it
        
        print()  # ⬇️ Final line break for clean output



# 🧪 Test it!   
def test_level_order_heights():
    avl = AVLTree()

    print("🧪 Test 1: AVL [10, 5, 15]")
    root = None
    for val in [10, 5, 15]:
        root = avl.insert(root, val)
    avl.print_level_order(root)
    # Expected: 10(h2) 5(h1) 15(h1)

    print("\n🧪 Test 2: Larger tree [10, 5, 15, 2, 7]")
    avl = AVLTree()
    root = None
    for val in [10, 5, 15, 2, 7]:
        root = avl.insert(root, val)
    avl.print_level_order(root)
    # Expected: 10(h3) 5(h2) 15(h1) 2(h1) 7(h1)

    print("\n🧪 Test 3: Unbalanced tree (manually created)")
    class FakeNode:
        def __init__(self, key, height, left=None, right=None):
            self.key = key
            self.height = height
            self.left = left
            self.right = right

    fake_root = FakeNode(10, 4,
        left=FakeNode(5, 3,
            left=FakeNode(2, 2,
                left=FakeNode(1, 1),
                right=None
            ),
            right=None
        ),
        right=None
    )
    print("Simulated unbalanced tree (incorrect heights):")
    avl.print_level_order(fake_root)
    # Expected (heights may be inconsistent): 10(h4) 5(h3) 2(h2) 1(h1)

    print("\n🧪 Test 4: Empty tree")
    avl.print_level_order(None)
    # Expected: (prints nothing)

    print("\n🧪 Test 5: Tree with many levels [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]")
    avl = AVLTree()
    root = None
    for val in [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]:
        root = avl.insert(root, val)
    avl.print_level_order(root)
    # Expected: 50(h4) 30(h3) 70(h3) 20(h2) 40(h2) 60(h2) 80(h1) 10(h1) 25(h1) 35(h1) 45(h1)


# 🚀 Go!
test_level_order_heights()