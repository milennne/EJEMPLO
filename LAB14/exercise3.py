test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")
    
class MinHeap:
    def __init__(self):
        # Initialize the heap as an empty list
        self.heap = []
    
    def insert(self, value):
        # Add the new value at the end of the list
        self.heap.append(value)
        # Restore the min-heap property by bubbling up
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, index):
        # While not at the root and the current node is smaller than its parent
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] > self.heap[index]:
                # Swap with parent to maintain min-heap property
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent  # Move up the tree
                continue
            break  # Stop if heap property is satisfied
    
    def _parent_index(self, index):
        # Return the parent index or -1 if it's the root
        return (index - 1) // 2 if index > 0 else -1
    
    def size(self):
        # Return the number of elements in the heap
        return len(self.heap)
    
    def peek(self):
        # Return the minimum element (root) or None if heap is empty
        return self.heap[0] if self.heap else None


def test_1_3():
    heap = MinHeap()
    
    # 1.3.1 Single element insertion
    heap.insert(5)
    record_test("1.3.1 Single element insertion", heap.heap == [5])
    
    # 1.3.2 Multiple insertions
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    record_test("1.3.2 Multiple insertions", len(heap.heap) == 4)
    
    # 1.3.3 Minimum tracking
    record_test("1.3.3 Minimum tracking", heap.peek() == 1)
    
    # 1.3.4 Heap property validation
    valid_heap = all(
        heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.3.4 Heap property validation", valid_heap)
    
    # 1.3.5 Size consistency
    record_test("1.3.5 Size consistency", heap.size() == 4)

# 🚀 Run tests
test_1_3()

# 📋 Summary
for r in test_results:
    print(r)
