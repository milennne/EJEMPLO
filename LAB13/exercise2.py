class MinHeap:
    def __init__(self):
        # Initialize an empty list to represent the heap
        self.heap = []

    def insert(self, value):
        # Step 1: Add the value at the end of the heap
        self.heap.append(value)
        # Step 2: Restore the min-heap property by heapifying up
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Keep moving up the node while it's smaller than its parent
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                # Swap child with parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                # Update index to parent and continue
                index = parent_index
            else:
                # Stop if heap property is satisfied
                break

# 🧪 Test cases
def test_min_heap_insert():
    h = MinHeap()
    h.insert(5); print("🍀 Test 1:", h.heap == [5])
    h.insert(3); print("🍀 Test 2:", h.heap == [3, 5])
    h.insert(4); print("🍀 Test 3:", h.heap == [3, 5, 4])
    h.insert(1); print("🍀 Test 4:", h.heap == [1, 3, 4, 5])
    
    # 🍀 Test 5: Check if each parent is less than or equal to its children
    valid = all(
        (h.heap[i] <= h.heap[2*i+1] if 2*i+1 < len(h.heap) else True) and
        (h.heap[i] <= h.heap[2*i+2] if 2*i+2 < len(h.heap) else True)
        for i in range(len(h.heap))
    )
    print("🍀 Test 5:", valid)

test_min_heap_insert()
