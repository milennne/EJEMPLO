class MinHeap:
    # 📦 MinHeap data structure using a list
    def __init__(self):
        # Initialize an empty list to represent the heap
        self.heap = []

    def is_empty(self):
        # Return True if the heap is empty, otherwise False
        return len(self.heap) == 0

# 🧪 Test cases
def test_min_heap_init_and_empty():
    h = MinHeap()
    print("Test 1:", h.is_empty() == True)        # Heap should be empty
    h.heap.append(1)
    print("Test 2:", h.is_empty() == False)       # Heap has one element
    h.heap.clear()
    print("Test 3:", h.is_empty() == True)        # Heap cleared, should be empty
    h.heap.extend([2, 3, 4])
    print("Test 4:", h.is_empty() == False)       # Heap has multiple elements
    h.heap.pop(); h.heap.pop(); h.heap.pop()
    print("Test 5:", h.is_empty() == True)        # All elements removed, should be empty

test_min_heap_init_and_empty()
